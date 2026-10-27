"""Rounding to an increment in a named direction (ARCH-010, ARCH-011)."""

from __future__ import annotations

import decimal
from decimal import Decimal, localcontext

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.numeric import PRECISION, AmountError, Rounding, amount, quantize

INCREMENTS = st.decimals(
    min_value=Decimal("0.0001"), max_value=Decimal(1000), places=4, allow_nan=False
)
VALUES = st.decimals(
    min_value=Decimal("-1e9"),
    max_value=Decimal("1e9"),
    places=10,
    allow_nan=False,
    allow_infinity=False,
)
ROUNDINGS = st.sampled_from(Rounding)


def _expected_side(
    value: Decimal, floor: Decimal, ceiling: Decimal, rounding: Rounding
) -> Decimal:
    """The multiple a rounding must choose, given the two multiples around `value`."""
    if rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
        return floor
    if rounding is Rounding.TOWARD_POSITIVE_INFINITY:
        return ceiling
    if rounding is Rounding.TOWARD_ZERO:
        return floor if value > 0 else ceiling
    return ceiling if value > 0 else floor


@given(VALUES, INCREMENTS, ROUNDINGS)
@pytest.mark.req("ARCH-010", "ARCH-011")
def test_quantize_moves_only_in_the_named_direction(
    value: Decimal, increment: Decimal, rounding: Rounding
) -> None:
    result = quantize(value, increment, rounding)
    with localcontext() as wide:
        wide.prec = 200  # the checks themselves are exact; Inexact stays trapped
        assert divmod(result, increment)[1] == 0
        assert abs(result - value) < increment
        if divmod(value, increment)[1] == 0:
            assert result == value
        if rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
            assert result <= value
        elif rounding is Rounding.TOWARD_POSITIVE_INFINITY:
            assert result >= value
        elif rounding is Rounding.TOWARD_ZERO:
            assert abs(result) <= abs(value)
            assert result == 0 or (result > 0) == (value > 0)
        else:
            assert abs(result) >= abs(value)


@given(
    st.integers(min_value=-(10**6), max_value=10**6).filter(lambda k: k != 0),
    INCREMENTS,
    st.booleans(),
    ROUNDINGS,
)
def test_quantize_at_full_precision_next_to_a_boundary(
    multiple: int, increment: Decimal, above: bool, rounding: Rounding
) -> None:
    boundary = amount(multiple) * increment
    unit = amount(1).scaleb(boundary.adjusted() - PRECISION + 1)
    value = boundary + unit if above else boundary - unit
    assert len(value.as_tuple().digits) <= PRECISION
    floor, ceiling = (
        (boundary, boundary + increment) if above else (boundary - increment, boundary)
    )
    assert quantize(value, increment, rounding) == _expected_side(
        value, floor, ceiling, rounding
    )


@pytest.mark.parametrize(
    ("rounding", "positive", "negative"),
    [
        (Rounding.TOWARD_ZERO, "9.6", "-9.6"),
        (Rounding.AWAY_FROM_ZERO, "9.9", "-9.9"),
        (Rounding.TOWARD_NEGATIVE_INFINITY, "9.6", "-9.9"),
        (Rounding.TOWARD_POSITIVE_INFINITY, "9.9", "-9.6"),
    ],
)
def test_the_plan_example_at_34_digits(
    rounding: Rounding, positive: str, negative: str
) -> None:
    value = amount("9.8" + "9" * 32)
    assert len(value.as_tuple().digits) == PRECISION
    increment = amount("0.3")
    assert quantize(value, increment, rounding) == amount(positive)
    assert quantize(-value, increment, rounding) == amount(negative)


def test_a_multiple_is_returned_unchanged_with_the_increments_exponent() -> None:
    assert (
        str(quantize(amount("1.20"), amount("0.01"), Rounding.AWAY_FROM_ZERO)) == "1.20"
    )
    assert str(quantize(amount("12.5"), amount("0.5"), Rounding.TOWARD_ZERO)) == "12.5"


def test_a_zero_result_has_no_sign() -> None:
    result = quantize(amount("-0.0001"), amount("0.01"), Rounding.TOWARD_ZERO)
    assert str(result) == "0.00"


@pytest.mark.parametrize("increment", ["0", "-0.01", "-1"])
def test_a_zero_or_negative_increment_is_refused(increment: str) -> None:
    with pytest.raises(AmountError, match="greater than zero"):
        quantize(amount("1"), amount(increment), Rounding.TOWARD_ZERO)


def test_non_finite_operands_are_refused() -> None:
    with pytest.raises(AmountError):
        quantize(Decimal("NaN"), amount("0.01"), Rounding.TOWARD_ZERO)
    with pytest.raises(AmountError):
        quantize(amount("1"), Decimal("Infinity"), Rounding.TOWARD_ZERO)


def test_a_float_operand_is_refused() -> None:
    with pytest.raises(TypeError):
        quantize(1.5, amount("0.01"), Rounding.TOWARD_ZERO)  # type: ignore[arg-type]


@pytest.mark.parametrize("value", ["2", "2.5"])
def test_a_rounding_that_is_not_a_named_direction_is_refused(value: str) -> None:
    # Refused whether or not the value needs rounding.
    with pytest.raises(TypeError, match="Rounding direction"):
        quantize(amount(value), amount("1"), "toward zero")  # type: ignore[arg-type]


@pytest.mark.req("ARCH-010")
def test_a_result_beyond_the_precision_raises_instead_of_rounding() -> None:
    with pytest.raises(decimal.InvalidOperation):
        quantize(amount("1e30"), amount("1e-7"), Rounding.TOWARD_ZERO)
