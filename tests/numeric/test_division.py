"""Division rounded to an increment in a named direction (ARCH-010, TEC-003; the numerical
policy's N4 and N5; the Stage 2 plan's U7)."""

from __future__ import annotations

import decimal
from decimal import Decimal
from fractions import Fraction

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.numeric import (
    PRECISION,
    AmountError,
    DecimalContextError,
    Rounding,
    amount,
    divide,
    quantize,
)

DIVIDENDS = st.decimals(
    min_value=Decimal("-1e9"),
    max_value=Decimal("1e9"),
    places=8,
    allow_nan=False,
    allow_infinity=False,
)
DIVISORS = st.decimals(
    min_value=Decimal("-1e6"),
    max_value=Decimal("1e6"),
    places=6,
    allow_nan=False,
    allow_infinity=False,
).filter(lambda divisor: divisor != 0)
INCREMENTS = st.decimals(
    min_value=Decimal("0.0001"), max_value=Decimal(1000), places=4, allow_nan=False
)
ROUNDINGS = st.sampled_from(Rounding)


@given(DIVIDENDS, DIVISORS, INCREMENTS, ROUNDINGS)
@pytest.mark.req("ARCH-010", "TEC-003")
def test_divide_moves_the_exact_quotient_only_in_the_named_direction(
    dividend: Decimal, divisor: Decimal, increment: Decimal, rounding: Rounding
) -> None:
    result = Fraction(divide(dividend, divisor, increment, rounding))
    quotient = Fraction(dividend) / Fraction(divisor)
    step = Fraction(increment)
    assert (result / step).denominator == 1
    assert abs(result - quotient) < step
    if (quotient / step).denominator == 1:
        assert result == quotient
    if rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
        assert result <= quotient
    elif rounding is Rounding.TOWARD_POSITIVE_INFINITY:
        assert result >= quotient
    elif rounding is Rounding.TOWARD_ZERO:
        assert abs(result) <= abs(quotient)
        assert result == 0 or (result > 0) == (quotient > 0)
    else:
        assert abs(result) >= abs(quotient)


@given(DIVIDENDS, INCREMENTS, ROUNDINGS)
def test_dividing_by_one_is_quantizing(
    value: Decimal, increment: Decimal, rounding: Rounding
) -> None:
    divided = divide(value, amount(1), increment, rounding)
    rounded = quantize(value, increment, rounding)
    assert divided == rounded
    assert str(divided) == str(rounded)


@given(
    st.integers(min_value=-(10**6), max_value=10**6).filter(lambda k: k != 0),
    INCREMENTS,
    st.booleans(),
    ROUNDINGS,
)
def test_divide_at_full_precision_next_to_a_boundary_with_a_negative_divisor(
    multiple: int, increment: Decimal, above: bool, rounding: Rounding
) -> None:
    boundary = amount(multiple) * increment
    unit = amount(1).scaleb(boundary.adjusted() - PRECISION + 1)
    value = boundary + unit if above else boundary - unit
    assert len(value.as_tuple().digits) <= PRECISION
    # The quotient is -value: the direction applies to it, not to the dividend.
    quotient = -value
    floor, ceiling = (
        (-boundary - increment, -boundary)
        if above
        else (-boundary, -boundary + increment)
    )
    if rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
        expected = floor
    elif rounding is Rounding.TOWARD_POSITIVE_INFINITY:
        expected = ceiling
    elif rounding is Rounding.TOWARD_ZERO:
        expected = floor if quotient > 0 else ceiling
    else:
        expected = ceiling if quotient > 0 else floor
    assert divide(value, amount(-1), increment, rounding) == expected


@pytest.mark.parametrize(
    ("rounding", "negative", "positive"),
    [
        (Rounding.TOWARD_ZERO, "-0.33", "0.33"),
        (Rounding.AWAY_FROM_ZERO, "-0.34", "0.34"),
        (Rounding.TOWARD_NEGATIVE_INFINITY, "-0.34", "0.33"),
        (Rounding.TOWARD_POSITIVE_INFINITY, "-0.33", "0.34"),
    ],
)
def test_the_quotient_takes_its_sign_from_both_operands(
    rounding: Rounding, negative: str, positive: str
) -> None:
    one, three, cent = amount("1"), amount("3"), amount("0.01")
    assert str(divide(one, -three, cent, rounding)) == negative
    assert str(divide(-one, three, cent, rounding)) == negative
    assert str(divide(-one, -three, cent, rounding)) == positive
    assert str(divide(one, three, cent, rounding)) == positive


def test_an_exact_quotient_keeps_the_increments_exponent() -> None:
    assert str(
        divide(amount("1"), amount("4"), amount("0.01"), Rounding.TOWARD_ZERO)
    ) == ("0.25")
    assert str(
        divide(amount("10"), amount("4"), amount("0.5"), Rounding.AWAY_FROM_ZERO)
    ) == ("2.5")


def test_a_zero_quotient_has_no_sign() -> None:
    result = divide(amount("-1"), amount("3"), amount("1"), Rounding.TOWARD_ZERO)
    assert str(result) == "0"
    result = divide(amount("0"), amount("-3"), amount("0.1"), Rounding.AWAY_FROM_ZERO)
    assert str(result) == "0.0"


@pytest.mark.parametrize("divisor", ["0", "-0", "0.000"])
def test_a_zero_divisor_is_refused(divisor: str) -> None:
    with pytest.raises(AmountError, match="divisor must not be zero"):
        divide(amount("1"), amount(divisor), amount("0.01"), Rounding.TOWARD_ZERO)


@pytest.mark.parametrize("increment", ["0", "-0.01"])
def test_a_zero_or_negative_increment_is_refused(increment: str) -> None:
    with pytest.raises(AmountError, match="greater than zero"):
        divide(amount("1"), amount("3"), amount(increment), Rounding.TOWARD_ZERO)


def test_operands_that_are_not_finite_decimals_are_refused() -> None:
    one, cent = amount("1"), amount("0.01")
    with pytest.raises(TypeError, match="dividend"):
        divide(1.5, one, cent, Rounding.TOWARD_ZERO)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="divisor"):
        divide(one, 3, cent, Rounding.TOWARD_ZERO)  # type: ignore[arg-type]
    with pytest.raises(AmountError, match="dividend must be finite"):
        divide(Decimal("NaN"), one, cent, Rounding.TOWARD_ZERO)
    with pytest.raises(AmountError, match="divisor must be finite"):
        divide(one, Decimal("Infinity"), cent, Rounding.TOWARD_ZERO)
    with pytest.raises(TypeError, match="Rounding direction"):
        divide(one, one, cent, "toward zero")  # type: ignore[arg-type]


def test_an_unconfigured_context_is_refused() -> None:
    with (
        decimal.localcontext(
            decimal.Context(prec=28, traps=[decimal.InvalidOperation])
        ),
        pytest.raises(DecimalContextError, match="not configured"),
    ):
        divide(Decimal(1), Decimal(3), Decimal("0.1"), Rounding.TOWARD_ZERO)


@pytest.mark.req("ARCH-010")
def test_a_step_beyond_the_precision_raises_instead_of_rounding() -> None:
    # The whole-number quotient would need 38 digits.
    with pytest.raises(decimal.InvalidOperation):
        divide(amount("1e30"), amount("1"), amount("1e-7"), Rounding.TOWARD_ZERO)
    # The divisor times the increment would need 35 digits.
    divisor = amount("9." + "9" * 33)
    assert len(divisor.as_tuple().digits) == PRECISION
    with pytest.raises(decimal.Inexact):
        divide(amount("1"), divisor, amount("0.7"), Rounding.TOWARD_ZERO)
