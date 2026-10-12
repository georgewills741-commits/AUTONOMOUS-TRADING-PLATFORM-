"""The base every interface contract is built on (ARCH-025, ARCH-026, GOV-006, GOV-007, TEC-004).

A contract is a Pydantic v2 model that is strict (no type coercion), immutable, and refuses
unknown fields. Its fields hold only immutable types, checked when the class is defined, so
nested values are immutable too. What a contract may add is listed, not what it may not: the
base's settings, field constraints written with `Field`, `AfterValidator`, and field
validators in "after" mode; anything else that could change how input is read or how values
are written (before, plain, or wrap validators, model validators, serializers, computed
fields, other metadata, unvalidated defaults, a redefined kernel method) is refused when the
class is created, by the contract's metaclass, so no base class or mixin can skip the checks.
After validation, every value is checked against its field's declared type.
Each concrete contract declares its own identity and version. Input from outside the platform
is validated with `from_python` or `from_json`, which raise `ContractError` with redacted
details only.
"""

from __future__ import annotations

import datetime
import enum
import re
import types
import typing
import uuid
from collections.abc import Sequence
from decimal import Decimal
from typing import (
    Annotated,
    Any,
    ClassVar,
    Final,
    Literal,
    NoReturn,
    Self,
    dataclass_transform,
)

from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    ValidationError,
    model_validator,
)
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.fields import FieldInfo
from pydantic_core import PydanticCustomError

from atp.contracts._amount import Amount, AmountSchema
from atp.contracts._errors import (
    ContractError,
    ErrorDetail,
    register_kernel_messages,
    register_known_names,
    validation_error_details,
)
from atp.contracts._idempotency import IdempotencyKey
from atp.contracts._outcome import Outcome
from atp.contracts._version import ContractVersion
from atp.numeric import DecimalContextError

_VALUE_TYPE: Final = "a contract value must have its field's declared type"
register_kernel_messages("contract_value_type", [_VALUE_TYPE])

# A contract's identity names its directory of committed schemas: lowercase letters and digits,
# in parts joined by dots or hyphens, starting with a letter (for example `atp.outcome`).
_CONTRACT_ID: Final = re.compile(r"[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*", flags=re.ASCII)

# The immutable types a field may hold, besides enums, literals, contracts, amounts, outcomes,
# and tuples, frozensets, and unions of allowed types. A float is allowed only for values that
# are not financial amounts (TEC-003); amounts are `Amount`. No bytes: JSON has no bytes, and
# binary data gets an encoding by decision when a contract first needs it. A tuple, not a set:
# annotations are compared by equality, and some are not hashable.
_IMMUTABLE_LEAVES: Final[tuple[type, ...]] = (
    str,
    int,
    bool,
    float,
    type(None),
    datetime.datetime,
    datetime.date,
    datetime.time,
    datetime.timedelta,
    uuid.UUID,
    IdempotencyKey,
)
_IMMUTABLE_TYPES: Final[tuple[object, ...]] = _IMMUTABLE_LEAVES

# Validation returns these exact types for them (subclasses are converted), so a value of
# another type was put there by code, not by validation.
_EXACT_LEAVES: Final[tuple[type, ...]] = (str, int, bool, float, IdempotencyKey)

# The metadata a field may carry: the constraint types `Field` itself produces, and
# `AfterValidator`, whose result is checked against the field's type. `Amount`'s own schema is
# not among them: an amount is declared as `Amount`, the `type` alias recognized by identity.
_CONSTRAINT_TYPES: Final = frozenset(
    type(item)
    for item in Field(
        gt=0,
        ge=0,
        lt=1,
        le=1,
        multiple_of=1,
        min_length=0,
        max_length=1,
        pattern="a",
        strict=True,
    ).metadata
)
# `Field`'s other settings share one metadata type; only these are constraints.
_GENERAL_METADATA: Final = type(Field(pattern="a").metadata[0])
_GENERAL_CONSTRAINTS: Final = frozenset({"pattern", "max_digits", "decimal_places"})

# The settings of `Field` a contract field may use; the others change how input is read or how
# values are written (another name for reading or writing, a discriminator, exclusion, per-field
# freezing) or belong to dataclasses. Each is compared with its default.
_DEFAULT_FIELD: Final = Field()
_FIELD_SETTINGS: Final = tuple(
    name for name in FieldInfo.__slots__ if not name.startswith("_")
)
_ALLOWED_FIELD_SETTINGS: Final = frozenset(
    {
        "annotation",
        "default",
        "default_factory",
        "alias",
        "alias_priority",
        "validation_alias",
        "serialization_alias",
        "title",
        "description",
        "examples",
        "json_schema_extra",
        "deprecated",
        "repr",
        "validate_default",
        "metadata",
    }
)
_BOUNDS: Final = ("gt", "ge", "lt", "le", "multiple_of")

# Methods of the kernel a contract does not redefine: they validate, write, or protect values.
_KERNEL_NAMES: Final = frozenset(
    {
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
    }
)


def _is_finite_float(value: float) -> bool:
    # An infinity or NaN minus itself is NaN, which equals nothing.
    return value - value == 0


def _conforms(value: object, annotation: object) -> bool:
    """Whether a validated value has the declared type, at any depth.

    Validation alone guarantees it; this catches a value put there by a validator or a
    default. The annotation was accepted by `_refuse_field_type` when the class was defined.
    """
    origin = typing.get_origin(annotation)
    arguments = typing.get_args(annotation)
    if origin is Annotated:
        return _conforms(value, arguments[0])
    if annotation is Amount:
        return type(value) is Decimal and value.is_finite()
    if annotation is float:
        return type(value) is float and _is_finite_float(value)
    if annotation is type(None):
        return value is None
    if annotation is datetime.date:
        return isinstance(value, datetime.date) and not isinstance(
            value, datetime.datetime
        )
    if annotation in _EXACT_LEAVES:
        return type(value) is annotation
    if annotation in _IMMUTABLE_LEAVES:
        return isinstance(value, annotation)
    if origin is Literal:
        return any(
            type(value) is type(allowed) and value == allowed for allowed in arguments
        )
    if isinstance(annotation, type) and issubclass(annotation, enum.Enum):
        return isinstance(value, annotation)
    if isinstance(annotation, type) and issubclass(annotation, Contract):
        # Its own fields too: a validator could return an instance never validated.
        return isinstance(value, annotation) and _fields_conform(value)
    if origin in (typing.Union, types.UnionType):
        return any(_conforms(value, argument) for argument in arguments)
    if origin is frozenset:
        return type(value) is frozenset and all(
            _conforms(item, arguments[0]) for item in value
        )
    if origin is tuple:
        if type(value) is not tuple:
            return False
        if len(arguments) == 2 and arguments[1] is Ellipsis:
            return all(_conforms(item, arguments[0]) for item in value)
        return len(value) == len(arguments) and all(
            _conforms(item, argument)
            for item, argument in zip(value, arguments, strict=True)
        )
    if origin is Outcome:
        if not isinstance(value, Outcome):
            return False
        # Read inside atp.contracts, where the outcome is defined.
        kind = value._kind.value  # noqa: SLF001
        payload: object = value._payload  # noqa: SLF001
        if kind == "SUCCESS":
            return _conforms(payload, arguments[0])
        if kind == "FAILURE":
            return _conforms(payload, arguments[1])
        return True  # TIMEOUT and UNKNOWN carry no value: their constructors take none
    return False


def _fields_conform(contract: Contract) -> bool:
    # Read from the instance's own dictionary: reading a deprecated field as an attribute warns.
    values = contract.__dict__
    return all(
        _conforms(values[name], field.annotation)
        for name, field in type(contract).model_fields.items()
    )


def _loosens(item: object) -> bool:
    """Whether field metadata loosens a base setting (`Strict(False)`, `allow_inf_nan=True`)."""
    if isinstance(item, FieldInfo):
        return any(_loosens(inner) for inner in item.metadata)
    return (
        getattr(item, "strict", None) is False
        or getattr(item, "allow_inf_nan", None) is True
    )


def _refuse_metadata(base: object, item: object, where: str) -> None:
    """Refuse field metadata that is not a listed constraint or `AfterValidator`."""
    if isinstance(item, FieldInfo):
        for inner in item.metadata:
            _refuse_metadata(base, inner, where)
        return
    bounds = [getattr(item, bound, None) for bound in _BOUNDS]
    if _holds_amount(base) and not all(
        value is None or _is_amount_bound(value) for value in bounds
    ):
        msg = f"{where}: an amount's bound is an amount or an integer, not a float or text"
        raise TypeError(msg)
    # The class itself, not a subclass, which could run before the declared type.
    if type(item) is AfterValidator:
        return
    if type(item) in _CONSTRAINT_TYPES and (
        type(item) is not _GENERAL_METADATA or set(vars(item)) <= _GENERAL_CONSTRAINTS
    ):
        return
    msg = (
        f"{where}: a field's metadata holds only constraints that Field expresses and "
        "AfterValidator"
    )
    raise TypeError(msg)


def _is_amount(annotation: object) -> bool:
    """Whether a type is an amount: `Amount`, with or without metadata (`Annotated[Amount, ...]`)."""
    while typing.get_origin(annotation) is Annotated:
        annotation = typing.get_args(annotation)[0]
    return annotation is Amount


def _beside_an_amount(annotation: object) -> bool:
    """Whether a union member may stand beside an amount: `None`, or a literal of strings,
    which accepts only its own words, so a JSON number is still refused."""
    return annotation is type(None) or (
        typing.get_origin(annotation) is Literal
        and all(type(value) is str for value in typing.get_args(annotation))
    )


def _is_amount_bound(value: object) -> bool:
    """Whether a bound fits an amount: an integer (not a bool) or a finite `Decimal`."""
    return type(value) is int or (type(value) is Decimal and value.is_finite())


def _holds_amount(annotation: object) -> bool:
    """Whether a constraint's base is an amount, or a union with one (`Amount | None`)."""
    if _is_amount(annotation):
        return True
    return typing.get_origin(annotation) in (typing.Union, types.UnionType) and any(
        _holds_amount(argument) for argument in typing.get_args(annotation)
    )


def _refuse_field_settings(field: FieldInfo, where: str) -> None:
    """Refuse `Field` settings that are not listed, and a second name for reading or writing."""
    if field.validate_default is False:
        msg = f"{where}: a contract validates every default"
        raise TypeError(msg)
    if field.exclude or field.exclude_if is not None:
        msg = f"{where}: a contract writes every field"
        raise TypeError(msg)
    if field.validation_alias not in (None, field.alias) or (
        field.serialization_alias not in (None, field.alias)
    ):
        msg = f"{where}: a field is read and written under one name, its alias"
        raise TypeError(msg)
    for setting in _FIELD_SETTINGS:
        if setting not in _ALLOWED_FIELD_SETTINGS and getattr(
            field, setting
        ) != getattr(_DEFAULT_FIELD, setting):
            msg = f"{where}: a contract field does not set {setting}"
            raise TypeError(msg)
    extra = field.json_schema_extra
    if extra is not None and (
        not isinstance(extra, dict)
        or not all(str(key).startswith("x-") for key in extra)
    ):
        # The committed schema must say what the contract validates: an extra key named like
        # a JSON Schema keyword (`type`, `minimum`), or a function, could contradict it.
        msg = (
            f"{where}: a field's json_schema_extra is a mapping whose keys are extensions "
            "starting with x-"
        )
        raise TypeError(msg)


def _refuse_written_metadata(metadata: Sequence[object], where: str) -> None:
    """Refuse metadata written in `Annotated[...]` other than `Field(...)` and `AfterValidator`.

    Only these classes themselves: a subclass could run before the declared type. And no
    constraint object written directly: typing caches `Annotated[...]` by equality, and
    `annotated_types.Gt(1.0)` equals `Gt(1)` and `Gt(True)`, so it could come back as an
    earlier equal object, and the verdict would depend on what was evaluated before. A
    `Field(...)` equals only itself, and an `AfterValidator` only one with the same function.
    """
    for item in metadata:
        if item is AmountSchema:
            msg = f"{where}: an amount's schema is used only through Amount"
            raise TypeError(msg)
        if type(item) not in (FieldInfo, AfterValidator):
            msg = f"{where}: a field's metadata holds only Field(...) and AfterValidator(...)"
            raise TypeError(msg)


def _refuse_annotated(base: object, metadata: Sequence[object], where: str) -> None:
    """Refuse metadata that could change how input is read, then the type it annotates.

    A field's own metadata is checked as Pydantic holds it, never through a rebuilt
    `Annotated[...]`: typing caches those by equality, so `Gt(gt=1.0)` could come back as an
    earlier `Gt(gt=1)`, and the check would depend on which contracts were defined before.
    """
    if any(_loosens(item) for item in metadata):
        msg = f"{where}: a field cannot turn off strictness or allow infinities"
        raise TypeError(msg)
    for item in metadata:
        _refuse_metadata(base, item, where)
    _refuse_field_type(base, where)


def _refuse_field_type(annotation: object, where: str) -> None:
    """Refuse a field type that is not built only from immutable types, or whose metadata
    could change how input is read."""
    if isinstance(annotation, str | typing.ForwardRef):
        msg = f"{where}: a contract's field types must be resolvable when it is defined"
        raise TypeError(msg)
    origin = typing.get_origin(annotation)
    arguments = typing.get_args(annotation)
    if annotation in _IMMUTABLE_TYPES or annotation is Amount:
        return
    if origin is Literal:
        # A literal's values are immutable, except that an enum member carries its value.
        for argument in arguments:
            if isinstance(argument, enum.Enum):
                _refuse_field_type(type(argument), where)
        return
    if isinstance(annotation, typing.TypeAliasType) or isinstance(
        origin, typing.TypeAliasType
    ):
        # Another alias would hide its value from these checks (`type Price = Amount`, or a
        # generic one such as `Pair[Amount]`).
        msg = f"{where}: a contract's field types are written out; its one type alias is Amount"
        raise TypeError(msg)
    if origin is Annotated:
        base, *metadata = arguments
        _refuse_written_metadata(metadata, where)
        _refuse_annotated(base, metadata, where)
        return
    if annotation is Decimal:
        msg = f"{where}: a contract holds an amount as Amount, not as a plain Decimal"
        raise TypeError(msg)
    if isinstance(annotation, type) and issubclass(annotation, enum.Enum):
        # A member's value is reachable through every contract that holds the member, so
        # it must be immutable too (`class W(Enum): A = ["x"]` would share one list).
        if any(
            type(member.value) not in (str, int)
            for member in annotation.__members__.values()
        ):
            msg = f"{where}: an enum's member values are strings or integers"
            raise TypeError(msg)
        # A `_missing_` of its own, or a flag that keeps, conforms, or ejects unknown bits, would
        # read a value that is no member as one (a fallback, a case-insensitive lookup).
        if any(
            "_missing_" in vars(klass)
            for klass in annotation.__mro__
            if klass not in (enum.Enum, enum.Flag)
        ) or (
            issubclass(annotation, enum.Flag)
            and getattr(annotation, "_boundary_", None) is not enum.FlagBoundary.STRICT
        ):
            msg = (
                f"{where}: an enum reads only its own members: no _missing_ of its own, "
                "and a flag's boundary is STRICT"
            )
            raise TypeError(msg)
        return
    if isinstance(annotation, type) and issubclass(annotation, Contract):
        return
    if (
        origin in (typing.Union, types.UnionType)
        and any(_is_amount(argument) for argument in arguments)
        and not all(
            _is_amount(argument) or _beside_an_amount(argument)
            for argument in arguments
        )
    ):
        # Another branch would accept what the amount refuses (a JSON number as a float).
        msg = (
            f"{where}: an amount is combined in a union only with None or a literal of "
            "strings"
        )
        raise TypeError(msg)
    if origin in (typing.Union, types.UnionType, frozenset, Outcome) or (
        origin is tuple and arguments
    ):
        for argument in arguments:
            if argument is not Ellipsis:
                _refuse_field_type(argument, where)
        return
    msg = (
        f"{where}: a contract holds only immutable types (tuples, not lists; "
        "contracts, not mappings)"
    )
    raise TypeError(msg)


# Repeats Pydantic's own declaration on its metaclass, which type checkers do not carry over to
# a subclass: without it, strict mypy would stop checking a contract's constructor arguments.
@dataclass_transform(kw_only_default=True, field_specifiers=(Field, PrivateAttr))
class _ContractMeta(ModelMetaclass):
    """Runs the contract checks on every contract class, after Pydantic has built it.

    A metaclass, not `__pydantic_init_subclass__`: Pydantic calls that hook through the first
    base class, so a mixin listed before `Contract` that defined it would skip the checks.
    `ModelMetaclass` is internal to Pydantic, which is pinned to one version.
    """

    def __new__(
        mcs,
        cls_name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> type:
        cls = super().__new__(mcs, cls_name, bases, namespace, **kwargs)
        if any(isinstance(base, _ContractMeta) for base in bases):
            _check_contract_class(typing.cast("type[Contract]", cls))
        return cls


class Contract(BaseModel, metaclass=_ContractMeta):
    """Base of every contract. Subclasses set `contract_id` and `contract_version`."""

    model_config = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
        hide_input_in_errors=True,
        validate_default=True,
        revalidate_instances="always",
        allow_inf_nan=False,
        serialize_by_alias=True,
    )

    contract_id: ClassVar[str]
    contract_version: ClassVar[ContractVersion]

    @model_validator(mode="after")
    def _check_declared_types(self) -> Self:
        # An after validator could return a value of another type (a float for an amount, a
        # list for a tuple). This is the contract's only model validator, so it runs last.
        if not _fields_conform(self):
            raise PydanticCustomError("contract_value_type", _VALUE_TYPE)
        return self

    @classmethod
    def from_python(cls, data: object) -> Self:
        """Validate Python data received from outside, given in the contract's own types.

        Validation is strict, so a tuple field takes a tuple, not a list, and an enum field a
        member, not its value: a parsed TOML document, whose arrays are lists and whose values
        are plain strings, is refused here wherever the contract has a tuple or an enum. JSON is
        read with `from_json`, which takes arrays and values in their JSON forms.
        """
        details: tuple[ErrorDetail, ...]
        try:
            return cls.model_validate(data)
        except ValidationError as error:
            details = validation_error_details(error)
        except Exception as error:
            if isinstance(error, DecimalContextError):
                raise  # the process is misconfigured; that is not refused input
            # A validator's own exception (a KeyError from a lookup, say), whose text may
            # quote the input: only its type is kept.
            details = (_validator_failed(error),)
        # Raised outside the except block, so the refusal carries no reference to the
        # original error, whose structured forms or text hold the input.
        raise ContractError(cls.contract_id, details)

    @classmethod
    def from_json(cls, data: str | bytes) -> Self:
        """Validate JSON received from outside."""
        details: tuple[ErrorDetail, ...]
        try:
            return cls.model_validate_json(data)
        except ValidationError as error:
            details = validation_error_details(error)
        except Exception as error:
            if isinstance(error, DecimalContextError):
                raise
            details = (_validator_failed(error),)
        raise ContractError(cls.contract_id, details)

    def to_json(self) -> str:
        """The contract as JSON: amounts as strings, collections as arrays."""
        return self.model_dump_json()

    def __setattr__(self, name: str, value: object) -> NoReturn:
        # Pydantic's own refusal for a frozen model repeats the assigned value in its text.
        msg = "a contract is immutable"
        raise AttributeError(msg)

    def __delattr__(self, name: str) -> NoReturn:
        msg = "a contract is immutable"
        raise AttributeError(msg)

    def __replace__(self, **changes: object) -> NoReturn:
        # Pydantic's version (which `copy.replace` calls from Python 3.13) copies without
        # validating, so a float could reach an amount. A changed contract is a new one.
        msg = (
            "a contract is not replaced; validate the changed values as a new contract"
        )
        raise TypeError(msg)


def _check_contract_class(cls: type[Contract]) -> None:
    """The checks every contract class passes when it is created (see the module docstring)."""
    declared = cls.__dict__
    contract_id = declared.get("contract_id")
    if type(contract_id) is not str:
        msg = f"{cls.__name__} must declare its own contract_id"
        raise TypeError(msg)
    if _CONTRACT_ID.fullmatch(contract_id) is None:
        msg = (
            f"{cls.__name__}'s contract_id must be lowercase letters and digits in "
            "parts joined by dots or hyphens, starting with a letter"
        )
        raise TypeError(msg)
    if not isinstance(declared.get("contract_version"), ContractVersion):
        msg = f"{cls.__name__} must declare its own contract_version"
        raise TypeError(msg)
    for key in sorted(_BASE_CONFIG.keys() | cls.model_config.keys()):
        # Also catches a setting inherited from a non-contract base class, and a setting
        # the base does not make (for example `json_encoders` or `use_enum_values`).
        if cls.model_config.get(key) != _BASE_CONFIG.get(key):
            msg = f"{cls.__name__} cannot change the contract setting {key}"
            raise TypeError(msg)
    if cls.__private_attributes__:
        msg = f"{cls.__name__}: a contract holds no private attributes"
        raise TypeError(msg)
    for klass in cls.__mro__:
        if klass is Contract:
            break
        # A mixin listed before Contract would override the kernel too.
        redefined = sorted(_KERNEL_NAMES & vars(klass).keys())
        if redefined:
            msg = f"{cls.__name__} cannot redefine the contract method {redefined[0]}"
            raise TypeError(msg)
    _refuse_decorators(cls)
    names: list[str] = []
    for name, field in cls.model_fields.items():
        where = f"{cls.__name__}.{name}"
        _refuse_field_settings(field, where)
        # Pydantic merges the metadata of a field's own `Annotated[...]` into `field.metadata`,
        # where a constraint written directly looks like one written with `Field`; it keeps
        # the annotation as written (internal to Pydantic, which is pinned to one version).
        written = field._original_annotation  # noqa: SLF001
        if typing.get_origin(written) is Annotated:
            _refuse_written_metadata(typing.get_args(written)[1:], where)
        _refuse_annotated(field.annotation, field.metadata, where)
        names.append(name)
        if field.alias is not None:
            names.append(field.alias)
    register_known_names(names)


def _validator_failed(error: Exception) -> ErrorDetail:
    """A validator raised something other than a validation error (a `KeyError` from a lookup,
    for example), whose text may quote the input: only its type is kept."""
    return ErrorDetail(
        (), "validator_failed", f"a validator raised {type(error).__name__}"
    )


_BASE_CONFIG: Final = dict(Contract.model_config)
_BASE_MODEL_VALIDATORS: Final = {
    name: decorator.func
    for name, decorator in Contract.__pydantic_decorators__.model_validators.items()
}


def _refuse_decorators(cls: type[Contract]) -> None:
    """Refuse validators that read input before the declared types do, and serializers."""
    decorators = cls.__pydantic_decorators__
    if decorators.validators or decorators.root_validators:
        msg = f"{cls.__name__}: a contract uses no version 1 validators"
        raise TypeError(msg)
    for decorator in decorators.field_validators.values():
        if decorator.info.mode != "after":
            msg = (
                f"{cls.__name__}: a contract's field validators run in after mode only"
            )
            raise TypeError(msg)
    model_validators = {
        name: decorator.func for name, decorator in decorators.model_validators.items()
    }
    if model_validators != _BASE_MODEL_VALIDATORS:
        msg = f"{cls.__name__}: a contract has no model validators of its own"
        raise TypeError(msg)
    if (
        decorators.field_serializers
        or decorators.model_serializers
        or decorators.computed_fields
    ):
        msg = f"{cls.__name__}: a contract is written by its declared types only"
        raise TypeError(msg)
