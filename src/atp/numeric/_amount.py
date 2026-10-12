"""The one amount constructor (ARCH-010, TEC-003; docs/architecture/numerical-policy.md)."""

from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation
from typing import Final

from atp.numeric._context import PRECISION, require_configured_context

_AMOUNT_FORM: Final = r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
_AMOUNT_RE: Final = re.compile(_AMOUNT_FORM, flags=re.ASCII)

AMOUNT_PATTERN: Final = f"^{_AMOUNT_FORM}$"
"""The accepted text form of an amount: ASCII digits, an optional sign, point, and exponent.

No spaces, no digit separators, no other digits, no NaN or infinity. The committed JSON
schemas use this pattern.
"""


_NOT_IN_TEXT_FORM: Final = (
    "an amount must be a decimal number in the accepted text form"
)
_EXPONENT_OUT_OF_RANGE: Final = "an amount's exponent is outside the supported range"
_NOT_FINITE: Final = "an amount must be finite"
_TOO_MANY_DIGITS: Final = f"an amount has at most {PRECISION} significant digits"

AMOUNT_REFUSALS: Final = frozenset(
    {_NOT_IN_TEXT_FORM, _EXPONENT_OUT_OF_RANGE, _NOT_FINITE, _TOO_MANY_DIGITS}
)
"""Every message an `AmountError` carries: fixed text, never the refused value."""


class AmountError(ValueError):
    """An amount was refused. The message is one of `AMOUNT_REFUSALS`, never the value."""


def amount(value: str | int | Decimal) -> Decimal:
    """Build an amount from text, an integer, or a `Decimal`.

    A float, a `bool`, any other type, and subclasses of `str`, `int`, or `Decimal` are
    refused (`TypeError`). NaN, infinities, more significant digits than `PRECISION`, and an
    exponent outside the context's range are refused (`AmountError`), so an amount that could
    not be computed with exactly is refused when it enters, not later inside arithmetic.
    """
    context = require_configured_context()
    if type(value) is str:
        if _AMOUNT_RE.fullmatch(value) is None:
            raise AmountError(_NOT_IN_TEXT_FORM)
        try:
            result = Decimal(value)
        except InvalidOperation:
            # The text form is valid, so only an exponent beyond what Python's decimal module
            # can hold is left to fail here.
            raise AmountError(_EXPONENT_OUT_OF_RANGE) from None
    elif type(value) is int:
        result = Decimal(value)
    elif type(value) is Decimal:
        result = value
    else:
        msg = "an amount is built only from str, int (not bool), or Decimal"
        raise TypeError(msg)
    if not result.is_finite():
        raise AmountError(_NOT_FINITE)
    _sign, digits, exponent = result.as_tuple()
    if len(digits) > PRECISION:
        raise AmountError(_TOO_MANY_DIGITS)
    if (
        not isinstance(exponent, int)
        or exponent < context.Etiny()
        or result.adjusted() > context.Emax
    ):
        raise AmountError(_EXPONENT_OUT_OF_RANGE)
    return result


def amount_from_toml(text: str) -> Decimal:
    """Read a TOML float as an amount; for `tomllib`'s `parse_float`.

    TOML allows underscores between digits; they are removed before the text reaches the
    amount constructor, which does not accept them. TOML's `inf` and `nan` are refused.
    """
    return amount(text.replace("_", ""))
