"""The base contract (ARCH-025, ARCH-026, GOV-006, TEC-004, SEC-005): strict, immutable, redacted errors."""

from __future__ import annotations

import copy
import datetime
import decimal
import enum
import fractions
import json
import logging
import pickle
import uuid
from collections import deque
from collections.abc import Mapping, Sequence
from decimal import Decimal
from typing import Annotated, Any, Literal, TypedDict, get_args

import pytest
from pydantic import (
    AfterValidator,
    AliasChoices,
    AliasPath,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    GetCoreSchemaHandler,
    PlainSerializer,
    PlainValidator,
    PrivateAttr,
    PydanticSchemaGenerationError,
    Strict,
    ValidationError,
    ValidationInfo,
    WrapValidator,
    computed_field,
    field_serializer,
    field_validator,
    model_serializer,
    model_validator,
)
from pydantic.fields import FieldInfo

from atp.contracts import (
    GENERIC_MESSAGE,
    REDACTED,
    Amount,
    Contract,
    ContractError,
    ContractVersion,
    ErrorDetail,
    IdempotencyKey,
    Outcome,
    PydanticCustomError,
    validation_error_details,
)
from atp.numeric import DecimalContextError, Rounding, amount, quantize

# The constraint class `Field(gt=...)` produces, written directly in some tests.
_GT: Any = type(Field(gt=0).metadata[0])

# Assembled at run time so that no file holds a credential-shaped sample.
SECRET = "sk" + "_live_" + "Q7x9Z2" + "secretvalue"


class Leg(Contract):
    contract_id = "test.leg"
    contract_version = ContractVersion(1, 0)
    price: Amount
    venue: str


class Order(Contract):
    contract_id = "test.order"
    contract_version = ContractVersion(1, 0)
    legs: tuple[Leg, ...]
    note: str = "none"


def _order() -> Order:
    return Order(legs=(Leg(price=amount("1.50"), venue="a"),))


def test_a_valid_contract_round_trips_through_json() -> None:
    order = _order()
    assert order.to_json() == '{"legs":[{"price":"1.50","venue":"a"}],"note":"none"}'
    assert Order.from_json(order.to_json()) == order


def test_equal_contracts_are_equal_and_hashable() -> None:
    assert _order() == _order()
    assert hash(_order()) == hash(_order())


def test_an_amount_is_a_decimal_in_python() -> None:
    assert type(_order().legs[0].price) is Decimal


@pytest.mark.req("ARCH-025", "TEC-004")
def test_an_unknown_field_is_refused() -> None:
    with pytest.raises(ContractError):
        Leg.from_python({"price": "1", "venue": "a", "extra": 1})


@pytest.mark.parametrize(
    "data",
    [
        {"price": 1.5, "venue": "a"},
        {"price": 1, "venue": "a"},
        {"price": True, "venue": "a"},
        {"price": "NaN", "venue": "a"},
        {"price": "1", "venue": 5},
        {"price": "1"},
    ],
)
@pytest.mark.req("TEC-004")
def test_wrong_types_floats_and_missing_fields_are_refused(
    data: dict[str, object],
) -> None:
    with pytest.raises(ContractError):
        Leg.from_python(data)


@pytest.mark.parametrize(
    "text", ['{"price": 1.5, "venue": "a"}', '{"price": 2, "venue": "a"}']
)
@pytest.mark.req("TEC-003", "TEC-004")
def test_a_json_number_for_an_amount_is_refused(text: str) -> None:
    with pytest.raises(ContractError):
        Leg.from_json(text)


@pytest.mark.req("ARCH-025")
def test_a_contract_is_immutable_including_nested_values() -> None:
    order = _order()
    with pytest.raises(AttributeError, match="immutable"):
        order.note = "changed"
    with pytest.raises(AttributeError, match="immutable"):
        order.legs[0].venue = "b"
    with pytest.raises(AttributeError, match="immutable"):
        del order.note
    with pytest.raises(TypeError):
        order.legs[0] = order.legs[0]  # type: ignore[index]


def test_refusing_an_assignment_never_repeats_the_value() -> None:
    with pytest.raises(AttributeError) as refused:
        _order().note = SECRET
    assert SECRET not in str(refused.value)
    assert SECRET not in repr(refused.value)


def test_a_default_is_validated_like_any_other_value() -> None:
    class Defaulted(Contract):
        contract_id = "test.defaulted"
        contract_version = ContractVersion(1, 0)
        price: Amount = "not an amount"  # type: ignore[assignment]

    with pytest.raises(ContractError):
        Defaulted.from_python({})


class KeyHolder(Contract):
    contract_id = "test.key-holder"
    contract_version = ContractVersion(1, 0)
    key: IdempotencyKey = Field(default_factory=IdempotencyKey.new)


@pytest.mark.parametrize(
    "body",
    [
        "    key: IdempotencyKey = IdempotencyKey.new()\n",
        "    key: IdempotencyKey = Field(default=IdempotencyKey.new())\n",
        "    keys: tuple[IdempotencyKey, ...] = (IdempotencyKey.new(),)\n",
        "    keys: frozenset[IdempotencyKey] = frozenset({IdempotencyKey.new()})\n",
        "    holder: KeyHolder = KeyHolder()\n",
        "    result: Outcome[IdempotencyKey, str] = Outcome.success(IdempotencyKey.new())\n",
        # A key's text becomes a key when the default is validated.
        "    key: IdempotencyKey = '0123456789abcdef' * 2\n",
        "    key: IdempotencyKey = Field(default='0123456789abcdef' * 2)\n",
        "    key: IdempotencyKey | None = '0123456789abcdef' * 2\n",
        "    keys: tuple[IdempotencyKey, ...] = ('0123456789abcdef' * 2,)\n",
        (
            "    keys: tuple[Annotated[IdempotencyKey, Field(description='k')], ...] = "
            "('0123456789abcdef' * 2,)\n"
        ),
        "    holder: KeyHolder = {'key': '0123456789abcdef' * 2}\n",
        "    result: Outcome[IdempotencyKey, str] = Outcome.success('0123456789abcdef' * 2)\n",
    ],
)
def test_a_key_held_by_a_default_is_refused(body: str) -> None:
    # Every instance built without the field would share it, so two operations would carry
    # one key.
    with pytest.raises(TypeError, match="can hold an idempotency key"):
        _define_body(body, {"KeyHolder": KeyHolder})


def test_a_key_default_comes_from_a_factory() -> None:
    holder: Any = _define_body(
        "    key: IdempotencyKey = Field(default_factory=IdempotencyKey.new)\n"
        "    maybe: IdempotencyKey | None = None\n"
        "    keys: tuple[IdempotencyKey, ...] = ()\n"
        "    pool: frozenset[IdempotencyKey] = frozenset()\n"
        "    nested: KeyHolder = Field(default_factory=KeyHolder)\n"
        "    other: KeyHolder | None = None\n",
        {"KeyHolder": KeyHolder},
    )
    first, second = holder(), holder()
    assert (first.key != second.key, first.nested.key != second.nested.key) == (
        True,
        True,
    )
    assert (first.maybe, first.keys, first.pool, first.other) == (
        None,
        (),
        frozenset(),
        None,
    )


def test_a_list_is_refused_where_a_tuple_is_declared_in_python() -> None:
    with pytest.raises(ContractError):
        Order.from_python({"legs": [{"price": "1", "venue": "a"}]})


def test_strict_mode_still_makes_the_listed_conversions() -> None:
    # The contract conventions list these; a Pydantic upgrade that changed one fails here.
    holder: Any = _define_body(
        "    ratio: float\n    count: int\n    name: str\n"
        "    day: datetime.date | None = None\n"
        "    at: datetime.datetime | None = None\n"
        "    clock: datetime.time | None = None\n"
        "    period: datetime.timedelta | None = None\n"
        "    ident: uuid.UUID | None = None\n"
    )
    converted = holder.from_python(
        {"ratio": amount("0.1"), "count": Size.SMALL, "name": Side.BUY}
    )
    assert (converted.ratio, type(converted.count), type(converted.name)) == (
        0.1,
        int,
        str,
    )
    assert (
        type(holder.from_python({"ratio": 1, "count": 1, "name": "a"}).ratio) is float
    )
    read = holder.from_json(
        json.dumps(
            {
                "ratio": 1,
                "count": 1,
                "name": "a",
                "day": "86400",
                "at": "1",
                "clock": "01:02",
                "period": "01:02",
                "ident": "{" + str(uuid.UUID(int=5)) + "}",
            }
        )
    )
    assert type(read.ratio) is float
    assert read.day == datetime.date(1970, 1, 2)
    assert read.at == datetime.datetime(1970, 1, 1, 0, 0, 1, tzinfo=datetime.UTC)
    assert read.clock == datetime.time(1, 2)
    assert read.period == datetime.timedelta(hours=1, minutes=2)
    assert read.ident == uuid.UUID(int=5)
    naive = holder.from_json(
        '{"ratio": 1, "count": 1, "name": "a", "at": "2026-01-01T00:00:00"}'
    )
    assert (naive.at.tzinfo, read.at.tzinfo is not None) == (None, True)
    aware = holder.from_json(
        '{"ratio": 1, "count": 1, "name": "a", "clock": "01:02:03Z"}'
    )
    assert (read.clock.tzinfo, aware.clock.tzinfo is not None) == (None, True)


class _Day(datetime.date):
    pass


class _Pair(tuple[int, ...]):
    pass


class _Pool(frozenset[int]):
    pass


class _Half:
    def __float__(self) -> float:
        return 0.5


def test_strict_mode_reads_these_python_values_as_listed() -> None:
    # Also listed in the contract conventions: a float field takes any value Python turns into a
    # float except a bool; a subclass of tuple or frozenset becomes the plain type; a subclass of
    # a date is kept as given.
    holder: Any = _define_body(
        "    ratio: float\n    items: tuple[int, ...]\n    pool: frozenset[int]\n"
        "    day: datetime.date\n"
    )
    for ratio, expected in ((fractions.Fraction(1, 4), 0.25), (_Half(), 0.5)):
        read = holder.from_python(
            {
                "ratio": ratio,
                "items": _Pair((1, 2)),
                "pool": _Pool({1}),
                "day": _Day(2026, 1, 1),
            }
        )
        assert (read.ratio, type(read.items), type(read.pool), type(read.day)) == (
            expected,
            tuple,
            frozenset,
            _Day,
        )
    with pytest.raises(ContractError):
        holder.from_python(
            {"ratio": True, "items": (), "pool": frozenset(), "day": _Day(2026, 1, 1)}
        )


class Colour(enum.Enum):
    RED = "red"


class Loose(BaseModel):  # not a contract: not frozen
    value: int


class Shape(TypedDict):
    value: int


_NAMESPACE: dict[str, object] = {
    "Contract": Contract,
    "ContractVersion": ContractVersion,
    "AfterValidator": AfterValidator,
    "AliasChoices": AliasChoices,
    "AliasPath": AliasPath,
    "Amount": Amount,
    "AmountSchema": get_args(Amount.__value__)[1],
    "Annotated": Annotated,
    "Any": Any,
    "BeforeValidator": BeforeValidator,
    "Colour": Colour,
    "Decimal": Decimal,
    "Field": Field,
    "Gt": _GT,
    "IdempotencyKey": IdempotencyKey,
    "Leg": Leg,
    "Literal": Literal,
    "Loose": Loose,
    "Order": Order,
    "Mapping": Mapping,
    "Outcome": Outcome,
    "PlainSerializer": PlainSerializer,
    "PlainValidator": PlainValidator,
    "Sequence": Sequence,
    "Shape": Shape,
    "Strict": Strict,
    "WrapValidator": WrapValidator,
    "amount": amount,
    "computed_field": computed_field,
    "datetime": datetime,
    "deque": deque,
    "field_serializer": field_serializer,
    "field_validator": field_validator,
    "model_serializer": model_serializer,
    "model_validator": model_validator,
    "uuid": uuid,
}


def _define_body(body: str, extra: dict[str, object] | None = None) -> type[Contract]:
    source = (
        "class Holder(Contract):\n"
        "    contract_id = 'test.holder'\n"
        "    contract_version = ContractVersion(1, 0)\n"
        f"{body}"
    )
    # Compiled without this module's `from __future__ import annotations`, as a module
    # without it would be, so the annotation is resolved when the class is defined.
    code = compile(source, "<holder>", "exec", dont_inherit=True)
    namespace: dict[str, Any] = {"__name__": "holder", **_NAMESPACE, **(extra or {})}
    exec(code, namespace)  # noqa: S102 -- a fixed test string
    holder: type[Contract] = namespace["Holder"]
    return holder


def _define(annotation: str) -> None:
    _define_body(f"    items: {annotation}\n")


@pytest.mark.parametrize(
    "annotation",
    [
        "list[str]",
        "dict[str, str]",
        "set[str]",
        "tuple[list[int], ...]",
        "list",
        "tuple",
        "tuple[int, ...] | list[int]",
        "Mapping[str, int]",
        "Sequence[int]",
        "deque[int]",
        "Any",
        "object",
        "Shape",
        "Loose",
        "tuple[Loose, ...]",
        "Outcome[list[int], str]",
        "bytes",
    ],
)
def test_a_field_that_could_hold_a_mutable_value_is_refused(annotation: str) -> None:
    with pytest.raises(TypeError, match="immutable"):
        _define(annotation)


def test_a_bytearray_field_is_refused() -> None:
    with pytest.raises(PydanticSchemaGenerationError):  # Pydantic has no schema for it
        _define("bytearray")


@pytest.mark.parametrize(
    "setting",
    [
        {"extra": "ignore"},
        {"extra": "allow"},
        {"strict": False},
        {"frozen": False},
        {"hide_input_in_errors": False},
        {"validate_default": False},
        {"revalidate_instances": "never"},
        {"allow_inf_nan": True},
        {"json_encoders": {Decimal: float}},
        {"use_enum_values": True},
        {"coerce_numbers_to_str": True},
        {"title": "renamed"},
    ],
)
def test_a_contract_cannot_change_the_base_settings(setting: dict[str, object]) -> None:
    with pytest.raises(TypeError, match="cannot change the contract setting"):

        class Loosened(Contract):
            model_config = ConfigDict(**setting)  # type: ignore[typeddict-item]
            contract_id = "test.loosened"
            contract_version = ContractVersion(1, 0)
            name: str


class Tolerant(BaseModel):
    model_config = ConfigDict(extra="ignore", strict=False)


def test_a_setting_inherited_from_another_model_is_refused() -> None:
    with pytest.raises(TypeError, match="cannot change the contract setting"):

        class Mixed(Contract, Tolerant):
            contract_id = "test.mixed"
            contract_version = ContractVersion(1, 0)
            name: str


@pytest.mark.parametrize(
    "annotation",
    [
        "Annotated[int, Field(strict=False)]",
        "Annotated[float, Field(allow_inf_nan=True)]",
        "tuple[Annotated[int, Field(strict=False)], ...]",
        "tuple[Annotated[float, Field(allow_inf_nan=True)], ...]",
    ],
)
def test_a_field_cannot_loosen_the_settings(annotation: str) -> None:
    with pytest.raises(TypeError, match="cannot turn off strictness"):
        _define(annotation)


def test_a_private_attribute_is_refused() -> None:
    with pytest.raises(TypeError, match="private attributes"):

        class Cached(Contract):
            contract_id = "test.cached"
            contract_version = ContractVersion(1, 0)
            name: str
            _cache: dict[str, int] = PrivateAttr(default_factory=dict)


class Sorted(Contract):
    contract_id = "test.sorted"
    contract_version = ContractVersion(1, 0)
    names: Annotated[tuple[str, ...], AfterValidator(sorted)]


class Nested(Contract):
    contract_id = "test.nested"
    contract_version = ContractVersion(1, 0)
    names: Annotated[tuple[str, ...], AfterValidator(lambda names: (list(names),))]


def test_a_validator_cannot_store_a_mutable_value() -> None:
    with pytest.raises(ContractError) as refused:
        Sorted.from_python({"names": ("b", "a")})
    assert refused.value.details[0].type == "contract_value_type"
    with pytest.raises(ContractError):
        Nested.from_python({"names": ("a",)})


@pytest.mark.parametrize(
    ("annotation", "valid", "wrong"),
    [
        ("Amount", "amount('1')", "0.1"),
        ("Amount", "amount('1')", "'1'"),
        ("Amount", "amount('1')", "Decimal('NaN')"),
        ("float", "1.5", "float('inf')"),
        ("float", "1.5", "float('nan')"),
        ("float", "1.5", "1"),
        ("int", "1", "True"),
        ("bool", "True", "1"),
        ("str", "'a'", "None"),
        ("None", "None", "0"),
        ("datetime.date", "datetime.date(2026, 1, 1)", "datetime.datetime(2026, 1, 1)"),
        (
            "datetime.datetime",
            "datetime.datetime(2026, 1, 1)",
            "datetime.date(2026, 1, 1)",
        ),
        ("uuid.UUID", "uuid.UUID(int=1)", "'1'"),
        ("IdempotencyKey", "Field(default_factory=IdempotencyKey.new)", "'k'"),
        ("Literal['a']", "'a'", "type('Sub', (str,), {})('a')"),
        ("Colour", "Colour.RED", "'red'"),
        ("Leg", "Leg(price=amount('1'), venue='a')", "Order(legs=())"),
        (
            "Leg",
            "Leg(price=amount('1'), venue='a')",
            "Leg.model_construct(price=0.1, venue='a')",
        ),
        (
            "tuple[Leg, ...]",
            "()",
            "(Leg.model_construct(price=amount('1'), venue=1),)",
        ),
        ("int | None", "None", "'a'"),
        ("frozenset[int]", "frozenset({1})", "{1}"),
        ("frozenset[int]", "frozenset({1})", "frozenset({'a'})"),
        ("frozenset[int]", "frozenset({1})", "type('Sub', (frozenset,), {})({1})"),
        ("tuple[int, ...]", "(1,)", "[1]"),
        ("tuple[int, ...]", "(1,)", "('a',)"),
        ("tuple[int, str]", "(1, 'a')", "(1,)"),
        ("tuple[int, str]", "(1, 'a')", "(1, 2)"),
        # A type with metadata inside another type is checked through to its base.
        ("tuple[Annotated[int, Field(ge=0)], ...]", "(1,)", "('a',)"),
        ("tuple[Annotated[Amount, Field(gt=0)], ...]", "(amount('1'),)", "(0.1,)"),
        ("Outcome[int, str]", "Outcome.success(1)", "1"),
        ("Outcome[int, str]", "Outcome.success(1)", "Outcome.success('a')"),
        ("Outcome[int, str]", "Outcome.failure('a')", "Outcome.failure(1)"),
    ],
)
def test_a_value_that_does_not_have_the_declared_type_is_refused(
    annotation: str, valid: str, wrong: str
) -> None:
    # The same field accepts a valid value, and refuses the same validator's wrong one.
    accepting = _define_body(
        f"    items: Annotated[{annotation}, AfterValidator(lambda value: value)] = {valid}\n"
    )
    accepting.from_python({})
    refusing = _define_body(
        f"    items: Annotated[{annotation}, AfterValidator(lambda value: {wrong})] = {valid}\n"
    )
    with pytest.raises(ContractError) as refused:
        refusing.from_python({})
    assert refused.value.details[0].type == "contract_value_type"


class Text(str):
    pass


class Exact(Decimal):
    pass


def test_a_subclass_of_text_or_decimal_is_refused_as_an_amount_type() -> None:
    # Only the classes themselves: a subclass could change how the value reads.
    for value in (Text("1.5"), Exact("1.5")):
        with pytest.raises(ContractError) as refused:
            Leg.from_python({"price": value, "venue": "a"})
        assert refused.value.details[0].type == "amount_type"


def test_an_after_field_validator_cannot_turn_an_amount_into_a_float() -> None:
    holder = _define_body(
        "    price: Amount\n"
        "    @field_validator('price')\n"
        "    @classmethod\n"
        "    def _to_float(cls, value):\n"
        "        return float(value)\n"
    )
    with pytest.raises(ContractError) as refused:
        holder.from_json('{"price": "0.1"}')
    assert refused.value.details[0].type == "contract_value_type"


@pytest.mark.parametrize(
    "annotation",
    [
        "Annotated[Amount, BeforeValidator(str)]",
        "Annotated[Amount, PlainValidator(lambda value: value)]",
        "Annotated[Amount, WrapValidator(lambda value, handler: handler(value))]",
        "Annotated[Amount, PlainSerializer(float)]",
        "Annotated[int, PlainValidator(lambda value: [value])]",
        "Annotated[int, 'a note']",
        "Annotated[str, Field(coerce_numbers_to_str=True)]",
        "Annotated[int | str, Field(union_mode='left_to_right')]",
        "tuple[Annotated[Amount, BeforeValidator(str)], ...]",
        "tuple[Annotated[str, Field(coerce_numbers_to_str=True)], ...]",
        "str | Annotated[int, BeforeValidator(int)]",
    ],
)
def test_metadata_that_could_change_how_input_is_read_is_refused(
    annotation: str,
) -> None:
    with pytest.raises(TypeError, match="metadata holds only"):
        _define(annotation)


@pytest.mark.parametrize(
    "annotation",
    [
        "Annotated[str, AmountSchema]",
        "Annotated[Decimal, AmountSchema]",
        "tuple[Annotated[Decimal, AmountSchema], ...]",
    ],
)
def test_the_amount_schema_is_used_only_through_amount(annotation: str) -> None:
    with pytest.raises(TypeError, match="only through Amount"):
        _define(annotation)


@pytest.mark.parametrize(
    "annotation",
    [
        "Annotated[Amount, Field(gt=0)]",
        "Annotated[str, Field(min_length=1, max_length=8, pattern='^[a-z]+$')]",
        "Annotated[int, Field(ge=0, lt=10, multiple_of=2)]",
        "Annotated[int, Field(strict=True)]",
        "Annotated[int, AfterValidator(abs)]",
    ],
)
def test_listed_constraints_are_accepted(annotation: str) -> None:
    _define(annotation)


WRITTEN_AS_FIELD = "metadata holds only Field"


def _float_to_text(value: object) -> object:
    return str(value) if type(value) is float else value


class _ReadsFirst(AfterValidator):
    """Calls itself an after validator, but reads the input before the declared type does, as
    a before validator would."""

    def __get_pydantic_core_schema__(
        self, source_type: Any, handler: GetCoreSchemaHandler
    ) -> Any:
        return BeforeValidator(self.func).__get_pydantic_core_schema__(
            source_type, handler
        )


class _StrictReadsFirst(Strict):
    """Strictness that reads the input before the declared type does."""

    def __get_pydantic_core_schema__(
        self, source_type: Any, handler: GetCoreSchemaHandler
    ) -> Any:
        return BeforeValidator(_float_to_text).__get_pydantic_core_schema__(
            source_type, handler
        )


# Pydantic marks the class final for type checkers; at run time it can still be subclassed.
class _OwnField(FieldInfo):  # type: ignore[misc]
    """A subclass of what `Field(...)` returns."""


@pytest.mark.parametrize(
    "annotation",
    [
        "Annotated[Amount, Gt(1)]",
        "Annotated[int, Gt(1)]",
        "Annotated[int, Strict()]",
        "Annotated[float, Strict(False)]",
        "tuple[Annotated[int, Strict(False)], ...]",
        "tuple[Annotated[Amount, Gt(1)], ...]",
        "Annotated[Amount, Gt(1)] | None",
        "Annotated[Amount, ReadsFirst(float_to_text)]",
        "tuple[Annotated[Amount, ReadsFirst(float_to_text)], ...]",
        "Annotated[int, OwnField()]",
    ],
)
def test_metadata_is_written_only_as_field_or_after_validator(annotation: str) -> None:
    # A constraint object written directly could come back from typing's cache as an earlier
    # equal one (Gt(1.0) == Gt(1)); a subclass could read the input before the declared type.
    with pytest.raises(TypeError, match=WRITTEN_AS_FIELD):
        _define_body(
            f"    items: {annotation}\n",
            {
                "ReadsFirst": _ReadsFirst,
                "float_to_text": _float_to_text,
                "OwnField": _OwnField,
            },
        )


@pytest.mark.parametrize(
    "reads_first", [_ReadsFirst(_float_to_text), _StrictReadsFirst()]
)
def test_a_subclass_of_listed_metadata_inside_a_field_is_refused(
    reads_first: object,
) -> None:
    # The subclass does read first: a strict model given it reads a JSON number as text.
    class Plain(BaseModel):
        model_config = ConfigDict(strict=True)
        venue: Annotated[str, reads_first]

    assert Plain.model_validate_json('{"venue": 0.5}').venue == "0.5"
    # Inside a field's own metadata, which holds only the constraints `Field` produces.
    annotated: Any = Annotated[Amount, reads_first]
    inside = FieldInfo.from_annotation(annotated)
    for annotation in (
        "Annotated[Amount, inside]",
        "tuple[Annotated[Amount, inside], ...]",
    ):
        with pytest.raises(TypeError, match="metadata holds only constraints"):
            _define_body(f"    price: {annotation}\n", {"inside": inside})


def test_a_constraint_written_directly_in_an_inherited_field_is_refused() -> None:
    class Bounded(BaseModel):
        q: Annotated[Amount, _GT(1)]

    with pytest.raises(TypeError, match=WRITTEN_AS_FIELD):

        class Inherits(Contract, Bounded):
            contract_id = "test.inherits"
            contract_version = ContractVersion(1, 0)


def test_the_reviewers_float_paths_into_an_amount_are_refused() -> None:
    with pytest.raises(TypeError, match="validates every default"):
        _define_body("    fee: Amount = Field(default=0.001, validate_default=False)\n")
    with pytest.raises(TypeError, match="field validators run in after mode only"):
        _define_body(
            "    price: Amount\n"
            "    @field_validator('price', mode='before')\n"
            "    @classmethod\n"
            "    def _to_text(cls, value):\n"
            "        return str(value)\n"
        )
    with pytest.raises(TypeError, match="metadata holds only"):
        _define("Annotated[Amount, BeforeValidator(str)]")


AFTER_ONLY = "field validators run in after mode only"
NO_MODEL_VALIDATORS = "no model validators of its own"
DECLARED_TYPES_ONLY = "written by its declared types only"


@pytest.mark.parametrize(
    ("decorated", "message"),
    [
        (
            (
                "    @field_validator('items', mode='before')\n    @classmethod\n"
                "    def _v(cls, value):\n        return value\n"
            ),
            AFTER_ONLY,
        ),
        (
            (
                "    @field_validator('items', mode='plain')\n    @classmethod\n"
                "    def _v(cls, value):\n        return value\n"
            ),
            AFTER_ONLY,
        ),
        (
            (
                "    @field_validator('items', mode='wrap')\n    @classmethod\n"
                "    def _v(cls, value, handler):\n        return handler(value)\n"
            ),
            AFTER_ONLY,
        ),
        (
            (
                "    @model_validator(mode='before')\n    @classmethod\n"
                "    def _v(cls, data):\n        return data\n"
            ),
            NO_MODEL_VALIDATORS,
        ),
        (
            (
                "    @model_validator(mode='after')\n"
                "    def _v(self):\n        return self\n"
            ),
            NO_MODEL_VALIDATORS,
        ),
        (
            (
                "    @model_validator(mode='wrap')\n    @classmethod\n"
                "    def _v(cls, data, handler):\n        return handler(data)\n"
            ),
            NO_MODEL_VALIDATORS,
        ),
        (
            (
                "    @field_serializer('items')\n"
                "    def _s(self, value):\n        return float(value)\n"
            ),
            DECLARED_TYPES_ONLY,
        ),
        (
            "    @model_serializer\n    def _s(self):\n        return {}\n",
            DECLARED_TYPES_ONLY,
        ),
        (
            (
                "    @computed_field\n    @property\n"
                "    def doubled(self) -> int:\n        return 2\n"
            ),
            DECLARED_TYPES_ONLY,
        ),
    ],
)
def test_validators_and_serializers_outside_the_list_are_refused(
    decorated: str, message: str
) -> None:
    with pytest.raises(TypeError, match=message):
        _define_body(f"    items: int = 1\n{decorated}")


def test_a_version_1_validator_is_refused() -> None:
    import pydantic

    with (
        pytest.warns(DeprecationWarning),
        pytest.raises(TypeError, match="version 1 validators"),
    ):
        _define_body(
            "    items: int = 1\n"
            "    @validator('items')\n"
            "    def _v(cls, value):\n"
            "        return value\n",
            {"validator": pydantic.validator},
        )


@pytest.mark.parametrize("spelling", ["default", "annotated"])
@pytest.mark.parametrize(
    ("constraint", "refused", "accepted", "error_type"),
    [
        ("gt=0", "-5", "1", "greater_than"),
        ("ge=1", "0", "1", "greater_than_equal"),
        ("lt=10", "10", "9", "less_than"),
        ("le=10", "99", "10", "less_than_equal"),
        ("multiple_of=amount('0.5')", "0.3", "1.5", "multiple_of"),
        ("max_digits=3", "1234", "123", "decimal_max_digits"),
        ("decimal_places=2", "1.234", "1.23", "decimal_max_places"),
    ],
)
def test_a_constraint_on_an_amount_holds_in_either_spelling(
    spelling: str, constraint: str, refused: str, accepted: str, error_type: str
) -> None:
    # `q: Amount = Field(...)` puts the constraint before the amount's own schema;
    # `Annotated[Amount, Field(...)]` puts it after. Both must apply it.
    body = (
        f"    q: Amount = Field({constraint})\n"
        if spelling == "default"
        else f"    q: Annotated[Amount, Field({constraint})]\n"
    )
    holder = _define_body(body)
    with pytest.raises(ContractError) as refusal:
        holder.from_json(json.dumps({"q": refused}))
    assert refusal.value.details[0].type == error_type
    assert holder.from_json(json.dumps({"q": accepted})).to_json() == json.dumps(
        {"q": accepted}, separators=(",", ":")
    )


@pytest.mark.parametrize(
    "body",
    [
        "    q: Amount = Field(strict=True, gt=0)\n",
        "    q: Annotated[Amount, Field(strict=True), Field(gt=0)]\n",
    ],
)
def test_strict_true_on_an_amount_is_accepted(body: str) -> None:
    # A listed setting: Pydantic puts it into the amount's inner decimal schema, which a plain
    # function schema would not have (defining the class would then fail).
    holder = _define_body(body)
    assert holder.from_json('{"q": "1.5"}').to_json() == '{"q":"1.5"}'
    for text, error_type in (
        ('{"q": 1.5}', "amount_type"),
        ('{"q": "-1"}', "greater_than"),
    ):
        with pytest.raises(ContractError) as refusal:
            holder.from_json(text)
        assert refusal.value.details[0].type == error_type


def test_a_bound_is_checked_as_written_whatever_was_defined_before() -> None:
    # typing caches `Annotated[...]` by equality, and 1.0 == 1 == True: the kernel checks a
    # field's own metadata, and refuses a constraint object written directly, so its verdict
    # does not depend on what was defined earlier.
    float_bound = "not a float"
    for annotation, refusal in (
        ("Amount = Field(gt=1)", None),
        ("Amount = Field(gt=1.0)", float_bound),
        ("Amount = Field(gt=1)", None),
        ("Amount = Field(ge=True)", float_bound),
        ("Amount = Field(ge=1)", None),
        ("Annotated[Amount, Gt(1.0)]", WRITTEN_AS_FIELD),
        ("Annotated[Amount, Gt(1)]", WRITTEN_AS_FIELD),
        ("Annotated[Amount, Field(gt=1)]", None),
        ("tuple[Annotated[Amount, Gt(1)], ...]", WRITTEN_AS_FIELD),
        ("tuple[Annotated[Amount, Gt(1.0)], ...]", WRITTEN_AS_FIELD),
        ("tuple[Annotated[Amount, Field(gt=1)], ...]", None),
        ("tuple[Annotated[Amount, Field(gt=1.0)], ...]", float_bound),
        ("tuple[Annotated[Amount, Field(gt=1)], ...]", None),
    ):
        body = f"    q: {annotation}\n"
        if refusal is None:
            _define_body(body)
        else:
            with pytest.raises(TypeError, match=refusal):
                _define_body(body)


def test_a_multiple_of_check_that_cannot_be_exact_refuses_the_value() -> None:
    # The remainder needs the whole quotient, 1E+38: 39 digits, more than the precision. The
    # decimal module raises InvalidOperation rather than give a wrong remainder, so the value
    # is refused, without a location.
    holder = _define_body("    q: Amount = Field(multiple_of=amount('1E-8'))\n")
    with pytest.raises(ContractError) as refusal:
        holder.from_json('{"q": "1E+30"}')
    assert [(detail.location, detail.type) for detail in refusal.value.details] == [
        ((), "validator_failed")
    ]


@pytest.mark.parametrize(
    "body",
    [
        "    q: Amount = Field(gt=0.5)\n",
        "    q: Annotated[Amount, Field(le=1.5)]\n",
        "    q: Amount | None = Field(default=None, gt=0.5)\n",
        "    q: Annotated[Amount | None, Field(gt=0.5)] = None\n",
        "    q: Annotated[Amount, Field(gt=0)] | None = Field(default=None, lt=0.1)\n",
        "    q: Amount = Field(gt='0')\n",
        "    q: Amount = Field(ge=True)\n",
        "    q: Amount = Field(lt=Decimal('NaN'))\n",
        "    q: Annotated[Annotated[Amount | None, Field(description='d')] | None, Field(gt=1.5)]\n",
    ],
)
def test_a_float_bound_on_an_amount_is_refused(body: str) -> None:
    with pytest.raises(TypeError, match="not a float"):
        _define_body(body)


@pytest.mark.parametrize(
    "annotation",
    [
        "Amount | float",
        "Amount | int",
        "Amount | str",
        "tuple[Amount | float, ...]",
        "Amount | Literal[1]",
        "Annotated[Amount, Field(gt=0)] | float",
        "Annotated[Amount, AfterValidator(abs)] | int",
        "Annotated[Amount, Field(strict=True)] | str",
        "tuple[Annotated[Amount, Field(gt=0)] | float, ...]",
        "Outcome[Annotated[Amount, Field(gt=0)] | float, str]",
        # A union written inside metadata stands in the same union.
        "Annotated[Amount | None, Field(gt=0)] | float",
        "Annotated[Amount | Literal['m'], Field(gt=0)] | bool",
        "tuple[Annotated[Amount | None, Field(description='d')] | int, ...]",
    ],
)
def test_an_amount_is_combined_in_a_union_only_with_none(annotation: str) -> None:
    # Another branch would accept what the amount refuses (a JSON number as a float), also when
    # the amount carries a constraint or a validator.
    with pytest.raises(TypeError, match="union only with None"):
        _define(annotation)


@pytest.mark.parametrize(
    "annotation",
    [
        "Amount | Literal['market']",
        "Annotated[Amount, Field(gt=0)] | Literal['market', 'limit'] | None",
    ],
)
def test_an_amount_may_stand_beside_a_literal_of_strings(annotation: str) -> None:
    holder = _define_body(f"    price: {annotation}\n")
    assert holder.from_json('{"price": "market"}').to_json() == '{"price":"market"}'
    assert holder.from_json('{"price": "1.5"}').to_json() == '{"price":"1.5"}'
    with pytest.raises(ContractError):
        holder.from_json('{"price": 1.5}')


class Deposit(Contract):
    contract_id = "test.deposit"
    contract_version = ContractVersion(1, 0)
    asset: str
    quantity: Amount


class Withdrawal(Contract):
    contract_id = "test.withdrawal"
    contract_version = ContractVersion(1, 0)
    asset: str
    quantity: Amount


class Movement(BaseModel):  # not a contract: shows what the union rule prevents
    model_config = ConfigDict(strict=True)
    movement: Deposit | Withdrawal


def test_strict_pydantic_reads_a_union_back_as_its_first_member_that_accepts_it() -> (
    None
):
    withdrawal = Withdrawal(asset="BTC", quantity=amount("1"))
    written = Movement(movement=withdrawal).model_dump_json()
    assert type(Movement.model_validate_json(written).movement) is Deposit


def _union_namespace() -> dict[str, object]:
    return {"Deposit": Deposit, "Withdrawal": Withdrawal, "Side": Side, "Size": Size}


@pytest.mark.parametrize(
    "annotation",
    [
        "Deposit | Withdrawal",
        "tuple[Deposit | Withdrawal, ...]",
        "Outcome[Deposit | Withdrawal, str]",
        "Outcome[int, str] | Leg",
        "Annotated[Deposit | None, Field(description='d')] | Withdrawal",
        "str | datetime.date",
        "str | datetime.datetime",
        "str | datetime.time",
        "str | datetime.timedelta",
        "str | uuid.UUID",
        "str | Side",
        "Side | Colour",
        "datetime.date | datetime.datetime",
        "int | float",
        "int | Size",
        "tuple[int, ...] | tuple[str, ...]",
        "tuple[int, ...] | frozenset[int]",
        "Annotated[Literal['a'] | int, Field(description='d')] | str",
        "Annotated[Annotated[int, Field(ge=0)] | None, Field(description='d')] | int",
    ],
)
def test_union_members_written_as_the_same_kind_of_json_value_are_refused(
    annotation: str,
) -> None:
    # Reading the written form back picks the first member that accepts a value, so a
    # withdrawal would come back as a deposit, and a date as text.
    with pytest.raises(TypeError, match="same kind of JSON value"):
        _define_body(f"    items: {annotation}\n", _union_namespace())


@pytest.mark.parametrize(
    "annotation",
    [
        "IdempotencyKey | int",
        "int | IdempotencyKey",
        "str | IdempotencyKey",
        "IdempotencyKey | Leg",
        "tuple[IdempotencyKey | bool, ...]",
        "Outcome[IdempotencyKey | int, str]",
        "Annotated[IdempotencyKey | None, Field(description='d')] | float",
    ],
)
def test_an_idempotency_key_is_combined_in_a_union_only_with_none(
    annotation: str,
) -> None:
    # A key's writer writes any value it is given as text, and a union can give it another
    # member's value: `IdempotencyKey | int` would write 7 as "7".
    with pytest.raises(TypeError, match="idempotency key is combined in a union only"):
        _define_body(f"    items: {annotation}\n", _union_namespace())


def test_an_optional_key_reads_its_own_json() -> None:
    holder = _define_body("    key: IdempotencyKey | None\n")
    for value in (IdempotencyKey.new(), None):
        written = holder.from_python({"key": value}).to_json()
        assert holder.from_json(written).to_json() == written


@pytest.mark.parametrize(
    "annotation",
    [
        "Amount | Literal['1']",
        "Amount | Literal['market', '1E+5']",
        "Annotated[Amount, Field(gt=0)] | Literal['-1']",
        "datetime.datetime | Literal['1']",
        "datetime.date | Literal['today']",
        "Side | Literal['BUY']",
        "uuid.UUID | Literal['none']",
    ],
)
def test_a_literal_beside_another_member_written_as_text_is_refused(
    annotation: str,
) -> None:
    # The member could read the literal's text as one of its own values ("1" as an amount, or
    # as a datetime one second after 1970 began); only `str`, and an amount refusing the text,
    # are known to read it back as the literal.
    with pytest.raises(TypeError, match="literal stands in a union"):
        _define_body(f"    items: {annotation}\n", _union_namespace())


@pytest.mark.parametrize(
    ("annotation", "values"),
    [
        ("int | str", "1, '1'"),
        ("bool | int", "True, 1, False, 0"),
        ("int | bool", "1, True, 0, False"),
        ("Leg | str", "Leg(price=amount('1'), venue='a'), 'a'"),
        ("datetime.date | int", "datetime.date(2026, 1, 1), 1"),
        ("str | Literal['a']", "'a', 'b'"),
        ("Annotated[Literal['a'], Field(description='d')] | str", "'a', 'b'"),
        ("Amount | Literal['market']", "amount('1'), 'market'"),
        ("Literal['a'] | Literal['b'] | int", "'a', 'b', 1"),
        ("Literal['a', None] | int", "'a', None, 1"),
        ("tuple[int, ...] | str", "(1,), 'a'"),
        ("Side | None", "Side.BUY, None"),
        ("Size | str", "Size.SMALL, 'a'"),
        ("Outcome[int, str] | None", "Outcome.success(1), None"),
        (
            "Annotated[Leg | None, Field(description='d')] | None",
            "Leg(price=amount('1'), venue='a'), None",
        ),
    ],
)
def test_a_union_whose_members_are_written_differently_reads_its_own_json(
    annotation: str, values: str
) -> None:
    holder: Any = _define_body(
        f"    items: tuple[{annotation}, ...] = ({values},)\n", _union_namespace()
    )
    written = holder()
    read = holder.from_json(written.to_json())
    # Outcomes are not compared, so the values are compared through their written form.
    assert read.to_json() == written.to_json()
    assert [type(item) for item in read.items] == [type(item) for item in written.items]


def _percent_to_fraction(value: Decimal) -> Decimal:
    return value / amount("100")


def _not_blank(value: str) -> str:
    if not value.strip():
        raise PydanticCustomError("blank", "the text is blank")
    return value


def _to_cents(value: Decimal) -> Decimal:
    return quantize(value, amount("0.01"), Rounding.TOWARD_ZERO)


def test_a_validator_is_applied_again_whenever_a_contract_is_validated_again() -> None:
    # Why a validator returns the value it was given, unchanged: an instance given as input,
    # and a contract's own JSON read back, are validated again, so a conversion (a percentage
    # to a fraction) would be applied again, silently.
    fee: Any = _define_body(
        "    rate: Annotated[Amount, AfterValidator(to_fraction)]\n",
        {"to_fraction": _percent_to_fraction},
    )
    once = fee.from_json('{"rate": "10"}')
    assert once.rate == amount("0.1")
    assert fee.from_python(once).rate == amount("0.001")
    assert fee.from_json(once.to_json()).rate == amount("0.001")
    # A validator that only checks returns the same value every time.
    name: Any = _define_body(
        "    name: Annotated[str, AfterValidator(not_blank)]\n",
        {"not_blank": _not_blank},
    )
    checked = name.from_json('{"name": " a "}')
    assert name.from_python(checked).name == " a "
    assert name.from_json(checked.to_json()).name == " a "


def test_a_constraint_is_not_checked_again_on_the_value_a_validator_returns() -> None:
    # Why a validator does not normalize either: a constraint written before it is checked on
    # the value the validator was given. Rounding 0.004 down to a step of 0.01 stores 0 in a
    # field declared greater than 0, which the contract then refuses as input.
    order: Any = _define_body(
        "    qty: Annotated[Amount, Field(gt=0), AfterValidator(to_cents)]\n",
        {"to_cents": _to_cents},
    )
    rounded = order.from_json('{"qty": "0.004"}')
    assert rounded.qty == amount("0")
    with pytest.raises(ContractError) as refused:
        order.from_json(rounded.to_json())
    assert refused.value.details[0].type == "greater_than"


def test_a_message_built_from_the_schema_is_kept() -> None:
    # Allowed values and limits are facts of the schema, not of the input.
    holder = _define_body(
        "    kind: Literal['a', 'b']\n    code: Annotated[str, Field(max_length=3)]\n"
    )
    with pytest.raises(ContractError) as refused:
        holder.from_json('{"kind": "c", "code": "abcd"}')
    assert [detail.message for detail in refused.value.details] == [
        "Input should be 'a' or 'b'",
        "String should have at most 3 characters",
    ]


def test_a_validators_own_exception_becomes_a_refusal_without_input() -> None:
    holder = _define_body(
        "    venue: Annotated[str, AfterValidator(lambda value: {'a': 'A'}[value])]\n"
    )
    for through_json in (False, True):
        with pytest.raises(ContractError) as refused:
            if through_json:
                holder.from_json(json.dumps({"venue": SECRET}))
            else:
                holder.from_python({"venue": SECRET})
        assert refused.value.details == (
            ErrorDetail((), "validator_failed", "a validator raised KeyError"),
        )
        for text in _texts_of(refused.value):
            assert SECRET not in text
        assert refused.value.__context__ is None
        assert refused.value.__cause__ is None


def test_a_cross_field_check_reads_earlier_fields_through_validation_info() -> None:
    class Band(Contract):
        contract_id = "test.band"
        contract_version = ContractVersion(1, 0)
        low: int
        high: int

        @field_validator("high")
        @classmethod
        def _above_low(cls, value: int, info: ValidationInfo) -> int:
            # A field that failed validation is absent from `info.data`.
            low = info.data.get("low")
            if low is not None and value < low:
                msg = "high is below low"
                raise ValueError(msg)
            return value

    assert Band.from_python({"low": 1, "high": 2}).high == 2
    with pytest.raises(ContractError):
        Band.from_python({"low": 3, "high": 2})
    with pytest.raises(ContractError) as refused:
        Band.from_python({"low": "x", "high": 2})
    assert [detail.type for detail in refused.value.details] == ["int_type"]


def test_a_contract_with_an_alias_reads_its_own_json() -> None:
    holder = _define_body("    price: Amount = Field(alias='unit-price')\n")
    written = holder.from_json('{"unit-price": "1.5"}').to_json()
    assert written == '{"unit-price":"1.5"}'
    assert holder.from_json(written).to_json() == written


@pytest.mark.parametrize(
    ("declared", "message"),
    [
        ("Field(default=1, validation_alias='other')", "under one name"),
        ("Field(default=1, validation_alias=AliasChoices('a', 'b'))", "under one name"),
        ("Field(default=1, validation_alias=AliasPath('a', 0))", "under one name"),
        ("Field(default=1, serialization_alias='other')", "under one name"),
        ("Field(default=1, alias='a', serialization_alias='b')", "under one name"),
        ("Field(default=1, frozen=True)", "does not set frozen"),
        ("Field(default=1, kw_only=True)", "does not set kw_only"),
        ("Field(default=1, init=False)", "does not set init"),
        ("Field(default=1, init_var=True)", "does not set init_var"),
        (
            "Field(default=1, field_title_generator=lambda name, field: name)",
            "does not set",
        ),
    ],
)
def test_a_field_setting_that_is_not_listed_is_refused(
    declared: str, message: str
) -> None:
    with pytest.raises(TypeError, match=message):
        _define_body(f"    items: int = {declared}\n")


@pytest.mark.parametrize(
    "extra",
    ["{'type': 'number'}", "{'x-unit': 'item', 'minimum': 0}", "lambda schema: None"],
)
def test_json_schema_extra_holds_only_extension_keys(extra: str) -> None:
    # The committed schema says what the contract validates; a JSON Schema keyword, or a
    # function that rewrites the schema, could contradict it.
    with pytest.raises(TypeError, match="keys are extensions starting with x-"):
        _define_body(f"    price: Amount = Field(json_schema_extra={extra})\n")


class KindA(Contract):
    contract_id = "test.kind-a"
    contract_version = ContractVersion(1, 0)
    kind: Literal["a"]


class KindB(Contract):
    contract_id = "test.kind-b"
    contract_version = ContractVersion(1, 0)
    kind: Literal["b"]


@pytest.mark.parametrize(
    ("annotation", "message"),
    [
        (
            "tuple[Annotated[Amount, Field(json_schema_extra={'type': 'number'})], ...]",
            "keys are extensions starting with x-",
        ),
        ("tuple[Annotated[str, Field(validation_alias='other')], ...]", "one name"),
        (
            "tuple[Annotated[KindA | KindB, Field(discriminator='kind')], ...]",
            "does not set discriminator",
        ),
        ("tuple[Annotated[int, Field(exclude=True)], ...]", "writes every field"),
    ],
)
# Pydantic warns that a second name or `exclude` has no effect there; the kernel refuses it.
@pytest.mark.filterwarnings(
    "ignore::pydantic.warnings.UnsupportedFieldAttributeWarning"
)
def test_a_field_inside_a_type_has_the_same_list_of_settings(
    annotation: str, message: str
) -> None:
    with pytest.raises(TypeError, match=message):
        _define_body(f"    items: {annotation}\n", {"KindA": KindA, "KindB": KindB})


def test_the_listed_settings_are_accepted_on_a_field_inside_a_type() -> None:
    holder = _define_body(
        "    items: tuple[Annotated[int, Field(ge=0, title='Count', "
        "description='How many', examples=[1], json_schema_extra={'x-unit': 'item'})], "
        "...]\n"
    )
    assert holder.from_json('{"items": [2]}').to_json() == '{"items":[2]}'


def test_the_listed_field_settings_are_accepted() -> None:
    holder = _define_body(
        "    items: int = Field(default=1, alias='count', title='Count', "
        "description='How many', examples=[1], json_schema_extra={'x-unit': 'item'}, "
        "repr=False)\n"
    )
    assert holder.from_python({"count": 2}).to_json() == '{"count":2}'


class DumpMixin:
    def to_json(self) -> str:
        return "{}"


def test_a_mixin_cannot_redefine_a_kernel_method() -> None:
    with pytest.raises(TypeError, match="cannot redefine the contract method to_json"):

        class Mixed(DumpMixin, Contract):
            contract_id = "test.mixed-dump"
            contract_version = ContractVersion(1, 0)
            price: Amount


def test_a_version_1_root_validator_is_refused() -> None:
    import pydantic

    with (
        pytest.warns(DeprecationWarning),
        pytest.raises(TypeError, match="version 1 validators"),
    ):
        _define_body(
            "    items: int = 1\n"
            "    @root_validator(skip_on_failure=True)\n"
            "    def _v(cls, values):\n"
            "        return values\n",
            {"root_validator": pydantic.root_validator},
        )


@pytest.mark.parametrize(
    "declared",
    [
        "Field(default=1, exclude=True)",
        "Field(default=1, exclude_if=lambda value: value == 1)",
    ],
)
def test_a_field_left_out_of_the_written_form_is_refused(declared: str) -> None:
    with pytest.raises(TypeError, match="writes every field"):
        _define_body(f"    items: int = {declared}\n")


KERNEL_METHODS = [
    "__init__",
    "__setattr__",
    "__delattr__",
    "__replace__",
    "__get_pydantic_core_schema__",
    "__get_pydantic_json_schema__",
    "model_post_init",
    "model_validate",
    "model_validate_json",
    "model_validate_strings",
    "model_dump",
    "model_dump_json",
    "from_python",
    "from_json",
    "to_json",
    "_check_declared_types",
]


def _method(name: str) -> str:
    # The schema hooks are class methods; the core one is called while the class is built,
    # so it returns a working schema.
    if name in {"__get_pydantic_core_schema__", "__get_pydantic_json_schema__"}:
        return (
            "    @classmethod\n"
            f"    def {name}(cls, source, handler):\n"
            "        return handler(source)\n"
        )
    return f"    def {name}(self, *args, **kwargs):\n        pass\n"


@pytest.mark.parametrize("name", KERNEL_METHODS)
def test_a_contract_cannot_redefine_a_kernel_method(name: str) -> None:
    with pytest.raises(TypeError, match=f"cannot redefine the contract method {name}"):
        _define_body(f"    items: int = 1\n{_method(name)}")


@pytest.mark.parametrize("name", KERNEL_METHODS)
def test_a_mixin_cannot_redefine_a_kernel_method_either(name: str) -> None:
    source = (
        f"class Mixin:\n{_method(name)}"
        "class Holder(Mixin, Contract):\n"
        "    contract_id = 'test.holder'\n"
        "    contract_version = ContractVersion(1, 0)\n"
        "    items: int = 1\n"
    )
    code = compile(source, "<mixin>", "exec", dont_inherit=True)
    with pytest.raises(TypeError, match=f"cannot redefine the contract method {name}"):
        exec(code, {"__name__": "holder", **_NAMESPACE})  # noqa: S102 -- a fixed test string


class Registering:
    """A mixin whose class hook does not call the next one: it must not skip the checks."""

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: object) -> None:
        pass


def test_a_mixin_with_its_own_class_hook_does_not_skip_the_checks() -> None:
    with pytest.raises(TypeError, match="immutable"):

        class Listed(Registering, Contract):
            contract_id = "test.listed"
            contract_version = ContractVersion(1, 0)
            items: list[int]


def test_a_contract_is_not_replaced_without_validation() -> None:
    # `copy.replace` calls `__replace__` from Python 3.13; Pydantic's copies unvalidated.
    with pytest.raises(TypeError, match="not replaced"):
        _order().__replace__(note="changed")


class PriceSourceDownError(Exception):
    pass


def _unavailable(value: str) -> str:
    raise PriceSourceDownError(value)


def test_any_exception_a_validator_raises_becomes_a_refusal_without_input() -> None:
    holder = _define_body(
        "    venue: Annotated[str, AfterValidator(_unavailable)]\n",
        {"_unavailable": _unavailable},
    )
    for through_json in (False, True):
        with pytest.raises(ContractError) as refused:
            if through_json:
                holder.from_json(json.dumps({"venue": SECRET}))
            else:
                holder.from_python({"venue": SECRET})
        assert refused.value.details == (
            ErrorDetail(
                (), "validator_failed", "a validator raised PriceSourceDownError"
            ),
        )
        for text in _texts_of(refused.value):
            assert SECRET not in text


def test_an_unconfigured_decimal_context_is_not_reported_as_refused_input() -> None:
    # Python's own defaults, not the platform's: a process configuration error, which
    # propagates instead of becoming a refusal of the input.
    defaults = decimal.Context(
        prec=28,
        rounding=decimal.ROUND_HALF_EVEN,
        Emin=-999999,
        Emax=999999,
        capitals=1,
        clamp=0,
        flags=[],
        traps=[decimal.InvalidOperation, decimal.DivisionByZero, decimal.Overflow],
    )
    with decimal.localcontext(defaults):
        with pytest.raises(DecimalContextError):
            Leg.from_json('{"price": "1", "venue": "a"}')
        with pytest.raises(DecimalContextError):
            Leg.from_python({"price": "1", "venue": "a"})


def test_a_deprecated_field_validates_without_warnings() -> None:
    # The declared-type check reads values without the warning a deprecated field's
    # attribute gives (tests turn warnings into errors).
    holder = _define_body(
        "    old: int = Field(default=0, deprecated='use new')\n    new: int = 0\n"
    )
    assert holder.from_python({"new": 1}).to_json() == '{"old":0,"new":1}'


class Cat(Contract):
    contract_id = "test.cat"
    contract_version = ContractVersion(1, 0)
    kind: Literal["cat"] = "cat"


class Dog(Contract):
    contract_id = "test.dog"
    contract_version = ContractVersion(1, 0)
    kind: Literal["dog"] = "dog"


def test_a_discriminator_is_refused() -> None:
    with pytest.raises(TypeError, match="does not set discriminator"):
        _define_body(
            "    pet: Cat | Dog = Field(discriminator='kind')\n",
            {"Cat": Cat, "Dog": Dog},
        )


def test_a_message_that_counts_the_input_is_replaced() -> None:
    holder = _define_body(
        "    items: Annotated[tuple[int, ...], Field(max_length=2)]\n"
    )
    with pytest.raises(ContractError) as refused:
        holder.from_python({"items": (1, 2, 3)})
    assert refused.value.details[0].type == "too_long"
    assert refused.value.details[0].message == GENERIC_MESSAGE


def test_a_validator_raises_its_own_error_type_through_the_kernel() -> None:
    # `PydanticCustomError` comes from atp.contracts: other modules do not import pydantic_core.
    def _on_tick(value: str) -> str:
        raise PydanticCustomError("price_off_tick", "the price is not on a tick")

    holder = _define_body(
        "    price: Annotated[str, AfterValidator(_on_tick)]\n", {"_on_tick": _on_tick}
    )
    with pytest.raises(ContractError) as refused:
        holder.from_python({"price": "1"})
    assert refused.value.details[0].type == "price_off_tick"
    # Not a kernel error type, so its message is not kept.
    assert refused.value.details[0].message == GENERIC_MESSAGE


def test_an_after_field_validator_is_accepted() -> None:
    holder = _define_body(
        "    items: int\n"
        "    @field_validator('items')\n"
        "    @classmethod\n"
        "    def _check(cls, value):\n"
        "        return value\n"
    )
    assert holder.from_python({"items": 3}).to_json() == '{"items":3}'


class Measured(Contract):
    contract_id = "test.measured"
    contract_version = ContractVersion(1, 0)
    count: int = 0
    ratio: float = 0.0


@pytest.mark.parametrize(
    ("text", "error_type"),
    [
        ('{"ratio": 1e400}', "finite_number"),
        ('{"ratio": NaN}', "finite_number"),
        ('{"count": "1"}', "int_type"),
    ],
)
def test_json_input_is_strict_and_finite(text: str, error_type: str) -> None:
    # Refused when it is read, not only by the declared-type check that runs after.
    with pytest.raises(ContractError) as refused:
        Measured.from_json(text)
    assert refused.value.details[0].type == error_type


def test_a_mapping_key_that_is_not_a_string_is_redacted() -> None:
    key = int("4111" * 4)
    with pytest.raises(ContractError) as refused:
        Leg.from_python({"price": "1", "venue": "a", key: 1})
    for text in _texts_of(refused.value):
        assert str(key) not in text
    assert refused.value.details[0].location[-1] == REDACTED


def test_an_assertion_message_that_quotes_the_input_is_replaced() -> None:
    class Asserted(Contract):
        contract_id = "test.asserted"
        contract_version = ContractVersion(1, 0)
        name: str

        @field_validator("name")
        @classmethod
        def _check(cls, value: str) -> str:
            assert value == "allowed", f"not allowed: {value}"
            return value

    with pytest.raises(ContractError) as refused:
        Asserted.from_python({"name": SECRET})
    for text in _texts_of(refused.value):
        assert SECRET not in text


def test_an_error_detail_is_immutable() -> None:
    detail = ErrorDetail(("name",), "missing", "Field required")
    with pytest.raises(AttributeError):
        detail.message = "changed"  # type: ignore[misc]


def test_a_python_dump_keeps_amounts_as_decimals() -> None:
    assert type(_order().model_dump()["legs"][0]["price"]) is Decimal


def test_amount_is_a_type_alias_that_builds_nothing() -> None:
    # An alias made by assignment could be called, and `Amount("NaN")` would build a Decimal
    # outside atp.numeric without the amount's checks (the numerical policy, N1 and N2).
    with pytest.raises(TypeError, match="not callable"):
        Amount("NaN")  # type: ignore[operator]
    with pytest.raises(TypeError):
        exec("class Money(Amount):\n    pass\n", {"Amount": Amount})  # noqa: S102 -- a fixed test string


@pytest.mark.parametrize(
    ("alias", "annotation"),
    [
        ("type Price = Amount", "Price"),
        ("type Name = str", "Name"),
        ("type Pair[T] = tuple[T, T]", "Pair[int]"),
        ("type Prices = tuple[Amount, ...]", "Annotated[Prices, Field(min_length=1)]"),
    ],
)
def test_a_type_alias_other_than_amount_is_refused(alias: str, annotation: str) -> None:
    namespace = dict(_NAMESPACE)
    exec(compile(alias, "<alias>", "exec", dont_inherit=True), namespace)  # noqa: S102 -- a fixed test string
    with pytest.raises(TypeError, match="its one type alias is Amount"):
        _define_body(f"    items: {annotation}\n", namespace)


class Mutable(enum.Enum):
    A = ["x"]  # noqa: RUF012 -- the mutable value the kernel refuses


class Ratio(enum.Enum):
    HALF = 0.5


class Switch(enum.Enum):
    OFF = 0
    ON = 1


class Size(enum.IntEnum):
    SMALL = 1


class Side(enum.StrEnum):
    BUY = "BUY"


@pytest.mark.parametrize(
    "annotation", ["Mutable", "Ratio", "Switch", "tuple[Mutable, ...]"]
)
def test_an_enum_holds_strings_unless_it_is_an_int_enum(annotation: str) -> None:
    # A member's value must be immutable, and Pydantic reads an enum of integers that is not
    # an `IntEnum` by equality, so it would read JSON `true` as the member 1.
    with pytest.raises(
        TypeError, match="member values are strings, or it is an IntEnum"
    ):
        _define_body(
            f"    items: {annotation}\n",
            {"Mutable": Mutable, "Ratio": Ratio, "Switch": Switch},
        )


@pytest.mark.parametrize("annotation", ["Size", "Side", "Colour"])
def test_an_enum_of_strings_or_an_int_enum_is_accepted(annotation: str) -> None:
    _define_body(f"    items: {annotation}\n", {"Size": Size, "Side": Side})


def test_an_int_enum_reads_only_its_integers() -> None:
    holder = _define_body("    size: Size\n", {"Size": Size})
    assert holder.from_json('{"size": 1}').to_json() == '{"size":1}'
    for text in ('{"size": true}', '{"size": 1.0}', '{"size": "1"}'):
        with pytest.raises(ContractError):
            holder.from_json(text)
    with pytest.raises(ContractError):
        holder.from_python({"size": 1})


@pytest.mark.parametrize(
    "annotation",
    [
        "Literal[1]",
        "Literal[True]",
        "Literal[1.0]",
        "Literal[b'x']",
        "Literal['a', 0]",
        "Literal[Side.BUY]",
        "Literal[Size.SMALL]",
        "Literal[Colour.RED]",
        "tuple[Literal[0], ...]",
        "Outcome[Literal[1], str]",
    ],
)
def test_a_literal_holds_only_strings_or_none(annotation: str) -> None:
    with pytest.raises(TypeError, match="literal's values are strings or None"):
        _define_body(f"    items: {annotation}\n", {"Size": Size, "Side": Side})


def test_a_literal_of_strings_or_none_reads_its_own_json() -> None:
    holder = _define_body(
        "    kind: Literal['a', None]\n    other: Literal['b'] | None = None\n"
    )
    for text in ('{"kind":"a","other":"b"}', '{"kind":null,"other":null}'):
        assert holder.from_json(text).to_json() == text


class Lenient(enum.StrEnum):
    FILLED = "FILLED"

    @classmethod
    def _missing_(cls, value: object) -> Lenient:
        return cls.FILLED


class LenientBase(enum.Enum):
    @classmethod
    def _missing_(cls, value: object) -> Any:
        return None


class InheritsLenience(LenientBase):
    PLAIN = "plain"


class Permissions(enum.IntFlag):
    READ = 1
    WRITE = 2


class StrictPermissions(enum.IntFlag, boundary=enum.STRICT):
    READ = 1
    WRITE = 2


class Bits(enum.Flag):
    A = 1
    B = 2


@pytest.mark.parametrize(
    "annotation",
    [
        "Lenient",
        "Permissions",
        "StrictPermissions",
        "Bits",
        "tuple[Lenient, ...]",
        "InheritsLenience",
    ],
)
def test_an_enum_that_reads_values_other_than_its_members_is_refused(
    annotation: str,
) -> None:
    # A `_missing_` of its own or from a base enum (a fallback, a case-insensitive lookup)
    # would read a value that is no member as one; every flag has one from `Flag`, which
    # reads combinations of members, and from JSON `true` and `false`.
    with pytest.raises(TypeError, match="reads only its own members"):
        _define_body(
            f"    items: {annotation}\n",
            {
                "Lenient": Lenient,
                "Permissions": Permissions,
                "StrictPermissions": StrictPermissions,
                "Bits": Bits,
                "InheritsLenience": InheritsLenience,
            },
        )


class ByEquality(
    BaseModel
):  # not a contract: shows what the literal and enum rules prevent
    model_config = ConfigDict(strict=True)
    one: Literal[1] = 1
    yes: Literal[True] = True
    switch: Switch = Switch.OFF
    permissions: StrictPermissions = StrictPermissions.READ
    side: Literal[Side.BUY] = Side.BUY


def test_strict_pydantic_matches_literals_and_most_enums_by_equality() -> None:
    read = ByEquality.model_validate_json(
        '{"one": true, "yes": 1, "switch": true, "permissions": false}'
    )
    assert (type(read.one), type(read.yes)) == (int, bool)
    assert read.switch is Switch.ON
    assert read.permissions == StrictPermissions(0)
    assert ByEquality.model_validate_json('{"one": 1.0}').one == 1
    assert ByEquality.model_validate({"side": "BUY"}).side is Side.BUY


def test_a_field_type_that_cannot_be_resolved_is_refused() -> None:
    with pytest.raises(TypeError, match="resolvable"):
        _define("'Later'")


@pytest.mark.parametrize(
    "annotation",
    [
        "Decimal",
        "Decimal | None",
        "tuple[Decimal, ...]",
        "Annotated[Decimal, Field(gt=0)]",
    ],
)
def test_a_plain_decimal_field_is_refused(annotation: str) -> None:
    with pytest.raises(TypeError, match="as Amount"):
        _define(annotation)


@pytest.mark.parametrize(
    "annotation",
    [
        "str",
        "int",
        "bool",
        "float",
        "Amount",
        "Amount | None",
        "tuple[Amount, ...]",
        "tuple[int, str]",
        "frozenset[str]",
        "Colour",
        "Literal['a', 'b']",
        "Leg",
        "tuple[Leg, ...]",
        "Outcome[Amount, str]",
        "IdempotencyKey",
        "datetime.datetime",
        "datetime.timedelta",
        "uuid.UUID",
        "Annotated[int, Field(ge=0)]",
    ],
)
def test_a_field_of_immutable_types_is_accepted(annotation: str) -> None:
    _define(annotation)


@pytest.mark.req("ARCH-026", "GOV-006")
def test_a_contract_without_identity_or_version_is_refused() -> None:
    with pytest.raises(TypeError, match="contract_id"):

        class Anonymous(Contract):
            contract_version = ContractVersion(1, 0)

    with pytest.raises(TypeError, match="contract_version"):

        class Unversioned(Contract):
            contract_id = "test.unversioned"

    with pytest.raises(TypeError, match="contract_id"):

        class Inheriting(Leg):
            pass


@pytest.mark.parametrize(
    "identity",
    ["", "Test.upper", "test/slash", "../test", "test..double", "1test", "test."],
)
def test_a_malformed_contract_identity_is_refused(identity: str) -> None:
    with pytest.raises(TypeError, match="contract_id"):

        class Misnamed(Contract):
            contract_id = identity
            contract_version = ContractVersion(1, 0)


def _texts_of(error: ContractError) -> list[str]:
    return [
        str(error),
        error.to_json(),
        json.dumps([detail.as_dict() for detail in error.details]),
    ]


@pytest.mark.req("SEC-005", "TEC-004")
def test_a_secret_given_as_a_field_value_never_appears_in_the_error() -> None:
    with pytest.raises(ContractError) as refused:
        Leg.from_python({"price": SECRET, "venue": "a"})
    for text in _texts_of(refused.value):
        assert SECRET not in text


def test_a_secret_given_as_an_unknown_key_never_appears_in_the_error() -> None:
    with pytest.raises(ContractError) as refused:
        Leg.from_json(json.dumps({"price": "1", "venue": "a", SECRET: SECRET}))
    for text in _texts_of(refused.value):
        assert SECRET not in text
    assert refused.value.details[0].location == (REDACTED,)


def test_a_secret_in_a_nested_unknown_key_never_appears_in_the_error() -> None:
    data = {"legs": [{"price": "1", "venue": "a", SECRET: 1}]}
    with pytest.raises(ContractError) as refused:
        Order.from_json(json.dumps(data))
    for text in _texts_of(refused.value):
        assert SECRET not in text
    assert refused.value.details[0].location == ("legs", 0, REDACTED)


def test_a_secret_as_an_outcome_tag_never_appears_in_the_error() -> None:
    class Report(Contract):
        contract_id = "test.tagged"
        contract_version = ContractVersion(1, 0)
        outcome: Outcome[int, str]

    with pytest.raises(ContractError) as refused:
        Report.from_json(json.dumps({"outcome": {"result": SECRET}}))
    for text in _texts_of(refused.value):
        assert SECRET not in text
    assert refused.value.details[0].message == GENERIC_MESSAGE


def test_an_unknown_key_is_redacted_even_when_another_contract_declares_its_name() -> (
    None
):
    with pytest.raises(ContractError) as refused:
        Order.from_json(json.dumps({"legs": [], "venue": "a"}))
    assert refused.value.details[0].location == (REDACTED,)


def test_a_location_part_from_the_input_is_redacted_for_any_error_type() -> None:
    class Mapping(BaseModel):  # not a contract: contracts refuse mappings
        amounts: dict[str, int]

    try:
        Mapping.model_validate({"amounts": {SECRET: "not a number"}})
    except ValidationError as error:
        details = validation_error_details(error)
    else:
        pytest.fail("the input should have been refused")
    assert details[0].type != "extra_forbidden"
    assert details[0].location[-1] == REDACTED
    assert SECRET not in json.dumps([detail.as_dict() for detail in details])


def test_a_contract_built_in_code_hides_the_value_in_its_error_text() -> None:
    with pytest.raises(ValidationError) as refused:
        Leg(price=SECRET, venue="a")  # type: ignore[arg-type]
    assert SECRET not in str(refused.value)


def _quote_the_input(value: str) -> str:
    msg = "not upper: " + value
    raise ValueError(msg)


class Tagged(Contract):
    contract_id = "test.tagged-built"
    contract_version = ContractVersion(1, 0)
    outcome: Outcome[int, str]


def test_a_contract_built_in_code_can_show_input_in_its_error_text() -> None:
    # Why outside data never goes through the constructor, and why a validation error is
    # rendered only through `validation_error_details`: the error's own text can show input,
    # as an unknown keyword, a validator's own message, or an outcome's unknown tag.
    quoting: Any = _define_body(
        "    name: Annotated[str, AfterValidator(quote)]\n", {"quote": _quote_the_input}
    )
    unknown: dict[str, Any] = {"price": amount("1"), "venue": "a", SECRET: 1}
    builds: list[Any] = [
        lambda: Leg(**unknown),
        lambda: quoting(name=SECRET),
        lambda: Tagged(outcome={"result": SECRET}),  # type: ignore[arg-type]
    ]
    for build in builds:
        with pytest.raises(ValidationError) as refused:
            build()
        assert SECRET in str(refused.value)
        details = validation_error_details(refused.value)
        assert SECRET not in json.dumps([detail.as_dict() for detail in details])


def test_the_refusal_holds_no_reference_to_the_original_error() -> None:
    with pytest.raises(ContractError) as from_python:
        Leg.from_python({"price": SECRET, "venue": "a", SECRET: 1})
    with pytest.raises(ContractError) as from_json:
        Leg.from_json(json.dumps({"price": SECRET, "venue": "a", SECRET: 1}))
    for refused in (from_python, from_json):
        assert refused.value.__context__ is None
        assert refused.value.__cause__ is None


def test_a_validator_message_that_quotes_the_input_is_replaced() -> None:
    class Checked(Contract):
        contract_id = "test.checked"
        contract_version = ContractVersion(1, 0)
        name: str

        @field_validator("name")
        @classmethod
        def _check(cls, value: str) -> str:
            msg = f"not allowed: {value}"
            raise ValueError(msg)

    with pytest.raises(ContractError) as refused:
        Checked.from_python({"name": SECRET})
    for text in _texts_of(refused.value):
        assert SECRET not in text
    assert refused.value.details[0].message == GENERIC_MESSAGE


@pytest.mark.parametrize("kind", ["string_type", "amount_invalid", "tuple_type"])
def test_a_listed_error_type_reused_with_a_message_of_its_own_is_replaced(
    kind: str,
) -> None:
    # The listed types keep their messages only when the message is the type's own
    # (Pydantic's, or the kernel's fixed text), so a validator reusing one cannot leak.
    class Reused(Contract):
        contract_id = "test.reused"
        contract_version = ContractVersion(1, 0)
        name: str

        @field_validator("name")
        @classmethod
        def _check(cls, value: str) -> str:
            raise PydanticCustomError(kind, "not allowed: {value}", {"value": value})

    with pytest.raises(ContractError) as refused:
        Reused.from_python({"name": SECRET})
    for text in _texts_of(refused.value):
        assert SECRET not in text
    assert refused.value.details[0].type == kind
    assert refused.value.details[0].message == GENERIC_MESSAGE


@pytest.mark.parametrize(
    ("text", "error_type", "message"),
    [
        (
            '{"price": "NaN", "venue": "a"}',
            "amount_invalid",
            "an amount must be a decimal number in the accepted text form",
        ),
        (
            '{"price": 1.5, "venue": "a"}',
            "amount_type",
            "an amount is given as a decimal string (or as a Decimal from Python code)",
        ),
        ('{"price": "1", "venue": 5}', "string_type", "Input should be a valid string"),
    ],
)
def test_a_listed_error_keeps_its_own_message(
    text: str, error_type: str, message: str
) -> None:
    with pytest.raises(ContractError) as refused:
        Leg.from_json(text)
    assert (refused.value.details[0].type, refused.value.details[0].message) == (
        error_type,
        message,
    )


def test_pydantics_json_wording_is_kept() -> None:
    # Pydantic words some messages differently for JSON input.
    with pytest.raises(ContractError) as refused:
        Order.from_json('{"legs": "none"}')
    assert refused.value.details[0].message == "Input should be a valid array"


@pytest.mark.parametrize(
    "exponent", ["1e999999999999999999999999", "1e-999999999999999999999"]
)
def test_an_amount_beyond_the_decimal_module_is_refused_as_input(exponent: str) -> None:
    with pytest.raises(ContractError):
        Leg.from_json(json.dumps({"price": exponent, "venue": "a"}))
    with pytest.raises(ContractError):
        Leg.from_python({"price": exponent, "venue": "a"})


def test_a_constructed_instance_is_validated_again() -> None:
    unchecked = Leg.model_construct(price=1.5, venue="a")
    with pytest.raises(ContractError):
        Leg.from_python(unchecked)
    with pytest.raises(ContractError):
        Order.from_python({"legs": (unchecked,)})


def test_a_constructed_instance_with_values_of_the_right_type_is_validated_again() -> (
    None
):
    # A Decimal with more digits than the precision has the declared type, so only
    # validating the instance again refuses it.
    too_precise = Decimal("1." + "1" * 40)
    unchecked = Leg.model_construct(price=too_precise, venue="a")
    with pytest.raises(ContractError) as refused:
        Order.from_python({"legs": (unchecked,)})
    assert refused.value.details[0].type == "amount_invalid"


def test_an_alias_is_shown_in_a_refusal_location() -> None:
    class Aliased(Contract):
        contract_id = "test.aliased"
        contract_version = ContractVersion(1, 0)
        price: Amount = Field(alias="unit-price")

    with pytest.raises(ContractError) as refused:
        Aliased.from_python({"unit-price": "not an amount"})
    assert refused.value.details[0].location == ("unit-price",)


def test_a_refusal_as_json_has_a_fixed_shape() -> None:
    with pytest.raises(ContractError) as refused:
        Leg.from_python({"price": "1", "venue": "a", SECRET: 1})
    assert json.loads(refused.value.to_json()) == {
        "contract": "test.leg",
        "errors": [
            {
                "location": [REDACTED],
                "type": "extra_forbidden",
                "message": "Extra inputs are not permitted",
            }
        ],
    }


def test_an_error_detail_renders_as_a_dictionary() -> None:
    detail = ErrorDetail(("legs", 0, REDACTED), "missing", "Field required")
    assert detail.as_dict() == {
        "location": ["legs", 0, REDACTED],
        "type": "missing",
        "message": "Field required",
    }


def test_a_refusal_can_be_copied_and_pickled() -> None:
    with pytest.raises(ContractError) as refused:
        Leg.from_python({"price": "x", "venue": "a"})
    error = refused.value
    for clone in (
        copy.copy(error),
        copy.deepcopy(error),
        pickle.loads(pickle.dumps(error)),  # noqa: S301 -- the bytes were made by this test
    ):
        assert str(clone) == str(error)
        assert clone.details == error.details


class Copyable(Contract):
    contract_id = "test.copyable"
    contract_version = ContractVersion(1, 0)
    key: IdempotencyKey
    result: Outcome[Amount, str]


def test_a_contract_with_an_outcome_and_a_key_can_be_copied_and_pickled() -> None:
    request = Copyable(key=IdempotencyKey.new(), result=Outcome.success(amount("2.5")))
    for clone in (
        copy.deepcopy(request),
        request.model_copy(deep=True),
        pickle.loads(pickle.dumps(request)),  # noqa: S301 -- the bytes were made by this test
    ):
        assert clone.to_json() == request.to_json()


def test_a_logged_refusal_never_contains_the_secret(
    caplog: pytest.LogCaptureFixture,
) -> None:
    logger = logging.getLogger("test.contracts")
    try:
        Leg.from_python({"price": SECRET, "venue": "a", SECRET: SECRET})
    except ContractError:
        logger.exception("contract refused input")
    assert caplog.records
    assert SECRET not in caplog.text


def test_validation_error_details_leaves_input_out_of_a_raw_error() -> None:
    try:
        Leg.model_validate({"price": SECRET, "venue": "a", SECRET: 1})
    except ValidationError as error:
        details = validation_error_details(error)
    else:
        pytest.fail("the input should have been refused")
    rendered = json.dumps([detail.as_dict() for detail in details])
    assert SECRET not in rendered
    assert {detail.type for detail in details} == {"amount_invalid", "extra_forbidden"}
