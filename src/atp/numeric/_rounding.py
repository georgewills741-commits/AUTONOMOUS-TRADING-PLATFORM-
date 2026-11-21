"""Rounding with a named direction, and division rounded the same way (ARCH-010, ARCH-011;
docs/architecture/numerical-policy.md)."""

from __future__ import annotations

import enum
from decimal import Decimal
from typing import assert_never

from atp.numeric._amount import AmountError
from atp.numeric._context import require_configured_context


class Rounding(enum.Enum):
    """The direction a rounding moves a value, defined for negative values too."""

    TOWARD_ZERO = "toward zero"
    AWAY_FROM_ZERO = "away from zero"
    TOWARD_NEGATIVE_INFINITY = "toward negative infinity"
    TOWARD_POSITIVE_INFINITY = "toward positive infinity"


def _check(value: Decimal, what: str) -> None:
    if type(value) is not Decimal:
        msg = f"the {what} must be a Decimal built with atp.numeric.amount"
        raise TypeError(msg)
    if not value.is_finite():
        msg = f"the {what} must be finite"
        raise AmountError(msg)


def _check_request(increment: Decimal, rounding: Rounding) -> None:
    _check(increment, "increment")
    if type(rounding) is not Rounding:
        msg = "the rounding must be a Rounding direction"
        raise TypeError(msg)
    if increment <= 0:
        msg = "an increment must be greater than zero"
        raise AmountError(msg)


def _to_multiple(
    dividend: Decimal,
    step: Decimal,
    increment: Decimal,
    positive: bool,
    rounding: Rounding,
) -> Decimal:
    """`dividend / step` whole increments, rounded in the named direction, where `step` is the
    divisor times `increment` and `positive` says whether the exact quotient is above zero.

    The whole number of increments and the remainder come from `divmod`, which truncates toward
    zero exactly; the direction then moves the result by at most one increment.
    """
    whole, remainder = divmod(dividend, step)
    toward_zero = whole * increment
    if remainder.is_zero() or rounding is Rounding.TOWARD_ZERO:
        result = toward_zero
    elif rounding is Rounding.AWAY_FROM_ZERO:
        result = toward_zero + increment if positive else toward_zero - increment
    elif rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
        result = toward_zero if positive else toward_zero - increment
    elif rounding is Rounding.TOWARD_POSITIVE_INFINITY:
        result = toward_zero + increment if positive else toward_zero
    else:
        assert_never(rounding)
    return result.copy_abs() if result.is_zero() else result


def quantize(value: Decimal, increment: Decimal, rounding: Rounding) -> Decimal:
    """Round `value` to a multiple of `increment` (a tick or step size) in the named direction.

    Every step is exact: the integer quotient and the remainder come from `divmod`, never from
    a rounded division, which could move a value the wrong way at full precision. The result
    is a multiple of `increment`, less than one increment from `value`, and equal to `value`
    when `value` already is a multiple. A step that would need more digits than the platform's
    precision raises the trapped decimal signal instead of rounding silently: the result, or
    the whole-number quotient (more than 34 digits raises even when the result itself would
    fit, as for 1E+40 rounded to a multiple of 1).
    """
    require_configured_context()
    _check(value, "value")
    _check_request(increment, rounding)
    return _to_multiple(value, increment, increment, value > 0, rounding)


def divide(
    dividend: Decimal, divisor: Decimal, increment: Decimal, rounding: Rounding
) -> Decimal:
    """Divide `dividend` by `divisor`, rounding the quotient to a multiple of `increment` in the
    named direction: the one division that may round (N4, N5).

    The quotient is never computed rounded. The whole number of increments it holds, and the
    remainder, come from `divmod` of the dividend by the divisor times the increment, so the
    direction applies to the exact quotient, whose sign comes from both operands. The result is
    a multiple of `increment`, less than one increment from the exact quotient, and equal to it
    when the quotient already is a multiple. A step that would need more digits than the
    platform's precision raises the trapped decimal signal instead of rounding silently: the
    divisor times the increment, the whole-number quotient, or the result. A zero divisor is
    refused, as are a zero or negative increment, a non-finite operand, and an operand that is
    not a `Decimal`.
    """
    require_configured_context()
    _check(dividend, "dividend")
    _check(divisor, "divisor")
    _check_request(increment, rounding)
    if divisor.is_zero():
        msg = "the divisor must not be zero"
        raise AmountError(msg)
    positive = (dividend > 0) == (divisor > 0)
    return _to_multiple(dividend, divisor * increment, increment, positive, rounding)
