"""The amount constructor (ARCH-010, TEC-003): what it accepts and what it refuses."""

from __future__ import annotations

import re
import tomllib
from decimal import Decimal

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.numeric import (
    AMOUNT_PATTERN,
    AMOUNT_REFUSALS,
    PRECISION,
    AmountError,
    amount,
    amount_from_toml,
)

FINITE = st.decimals(
    min_value=Decimal("-1e12"),
    max_value=Decimal("1e12"),
    places=12,
    allow_nan=False,
    allow_infinity=False,
)


@given(st.floats(allow_nan=True, allow_infinity=True))
def test_a_float_is_refused(value: float) -> None:
    with pytest.raises(TypeError):
        amount(value)  # type: ignore[arg-type]


@pytest.mark.parametrize("value", [True, False])
def test_a_bool_is_refused(value: bool) -> None:
    with pytest.raises(TypeError):
        amount(value)


@pytest.mark.parametrize("value", [None, b"1", bytearray(b"1"), [1], (1,), object()])
def test_other_types_are_refused(value: object) -> None:
    with pytest.raises(TypeError):
        amount(value)  # type: ignore[arg-type]


def test_subclasses_are_refused() -> None:
    class Text(str):
        pass

    class Number(int):
        pass

    class Exact(Decimal):
        pass

    with pytest.raises(TypeError):
        amount(Text("1"))
    with pytest.raises(TypeError):
        amount(Number(1))
    with pytest.raises(TypeError):
        amount(Exact("1"))


@pytest.mark.parametrize(
    "text", ["NaN", "nan", "sNaN", "Infinity", "-Infinity", "inf", "-inf", "+inf"]
)
def test_nan_and_infinities_are_refused_as_text(text: str) -> None:
    with pytest.raises(AmountError):
        amount(text)


@pytest.mark.parametrize("text", ["NaN", "sNaN", "Infinity", "-Infinity"])
def test_nan_and_infinities_are_refused_as_decimals(text: str) -> None:
    with pytest.raises(AmountError, match="finite"):
        amount(Decimal(text))


@pytest.mark.parametrize(
    "text",
    [
        "",
        " 1",
        "1 ",
        "1_000",
        "1,5",
        "0x10",
        "\u0661",
        "1e",
        "e5",
        ".",
        "+",
        "--1",
        "1.2.3",
        "1\n",
    ],
)
def test_malformed_text_is_refused(text: str) -> None:
    with pytest.raises(AmountError):
        amount(text)


@pytest.mark.parametrize(
    "text",
    ["0", "-0", "1", "-1", "1.50", "+2", ".5", "5.", "1e-8", "1E+3", "123.456000"],
)
def test_well_formed_text_is_accepted(text: str) -> None:
    assert amount(text) == Decimal(text)
    assert re.fullmatch(AMOUNT_PATTERN, text)


@pytest.mark.parametrize("text", ["1_000", " 1", "\u0661", "1e", "NaN", "inf"])
def test_the_published_pattern_refuses_what_the_constructor_refuses(text: str) -> None:
    assert re.fullmatch(AMOUNT_PATTERN, text) is None


@given(FINITE)
def test_the_string_round_trip_is_exact(value: Decimal) -> None:
    built = amount(str(value))
    assert built == value
    assert str(built) == str(value)


@given(st.integers(min_value=-(10**PRECISION) + 1, max_value=10**PRECISION - 1))
def test_integers_within_the_precision_are_accepted_exactly(value: int) -> None:
    assert amount(value) == value


def test_an_amount_with_more_digits_than_the_precision_is_refused() -> None:
    longest = "1" * PRECISION
    assert amount(longest) == Decimal(longest)
    with pytest.raises(AmountError, match="significant digits"):
        amount("1" * (PRECISION + 1))
    with pytest.raises(AmountError, match="significant digits"):
        amount("0." + "1" * (PRECISION + 1))
    with pytest.raises(AmountError, match="significant digits"):
        amount(10**PRECISION)


@pytest.mark.parametrize(
    "text",
    [
        "1e1000000",
        "1e-1000033",
        "0e-1000033",
        "1e999999999999999999999999",
        "1e-999999999999999999999999",
    ],
)
def test_an_exponent_out_of_range_is_refused(text: str) -> None:
    with pytest.raises(AmountError, match="exponent"):
        amount(text)


@pytest.mark.parametrize(
    "text", ["1e999999", "9.99e999999", "1e-1000032", "0e-1000032"]
)
def test_the_exponent_range_ends_at_the_context_limits(text: str) -> None:
    # Emax is 999999; the smallest exponent is Etiny = Emin - precision + 1 = -1000032.
    assert amount(text) == Decimal(text)


@given(st.text(alphabet="0123456789", min_size=PRECISION + 1, max_size=60))
def test_any_amount_longer_than_the_precision_is_refused(digits: str) -> None:
    text = "1" + digits
    with pytest.raises(AmountError, match="significant digits"):
        amount(text)
    with pytest.raises(AmountError, match="significant digits"):
        amount("0." + text)


def test_a_refusal_never_repeats_the_value() -> None:
    secret = "9" * (PRECISION + 1)
    with pytest.raises(AmountError) as refused:
        amount(secret)
    assert secret not in str(refused.value)


def test_a_toml_number_becomes_a_decimal() -> None:
    document = tomllib.loads(
        "price = 1_000.25\nsize = 1e-8\nlimit = 3\nbig = 1_000_000.5",
        parse_float=amount_from_toml,
    )
    assert document["price"] == amount("1000.25")
    assert document["big"] == amount("1000000.5")
    assert type(document["price"]) is Decimal
    assert document["size"] == amount("1e-8")
    assert document["limit"] == 3


def test_a_toml_number_beyond_the_decimal_module_is_refused() -> None:
    with pytest.raises(AmountError, match="exponent"):
        tomllib.loads("x = 1e999999999999999999999999", parse_float=amount_from_toml)


@pytest.mark.parametrize("text", ["x = inf", "x = -inf", "x = nan", "x = +nan"])
def test_toml_nan_and_infinities_are_refused(text: str) -> None:
    with pytest.raises(AmountError):
        tomllib.loads(text, parse_float=amount_from_toml)


@pytest.mark.parametrize(
    "value",
    [
        "x",
        "1 ",
        "NaN",
        "1" * (PRECISION + 1),
        "1E+999999999999",
        "1E-99999999",
        Decimal("Infinity"),
    ],
)
def test_every_refusal_carries_one_of_the_listed_messages(value: str | Decimal) -> None:
    # The contract kernel keeps these messages in refusals; none may contain the value.
    with pytest.raises(AmountError) as refused:
        amount(value)
    assert str(refused.value) in AMOUNT_REFUSALS
