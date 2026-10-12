"""Rounding with a named direction (ARCH-010, ARCH-011; docs/architecture/numerical-policy.md)."""

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
    _check(increment, "increment")
    if type(rounding) is not Rounding:
        msg = "the rounding must be a Rounding direction"
        raise TypeError(msg)
    if increment <= 0:
        msg = "an increment must be greater than zero"
        raise AmountError(msg)
    whole, remainder = divmod(value, increment)
    toward_zero = whole * increment
    if remainder.is_zero() or rounding is Rounding.TOWARD_ZERO:
        result = toward_zero
    elif rounding is Rounding.AWAY_FROM_ZERO:
        result = toward_zero + increment if value > 0 else toward_zero - increment
    elif rounding is Rounding.TOWARD_NEGATIVE_INFINITY:
        result = toward_zero if value > 0 else toward_zero - increment
    elif rounding is Rounding.TOWARD_POSITIVE_INFINITY:
        result = toward_zero + increment if value > 0 else toward_zero
    else:
        assert_never(rounding)
    return result.copy_abs() if result.is_zero() else result
