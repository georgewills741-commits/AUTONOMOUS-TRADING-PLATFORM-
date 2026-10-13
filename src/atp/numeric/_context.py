"""The process-wide decimal context (ARCH-010, TEC-003; docs/architecture/numerical-policy.md)."""

from __future__ import annotations

import decimal
from typing import Final

PRECISION: Final = 34
"""Significant digits of every financial calculation (values register V-40)."""

TRAPPED_SIGNALS: Final[frozenset[type[decimal.DecimalException]]] = frozenset(
    {
        decimal.FloatOperation,
        decimal.InvalidOperation,
        decimal.DivisionByZero,
        decimal.Overflow,
        decimal.Inexact,
    }
)
"""The signals that raise instead of being recorded as flags."""

_EMAX: Final = 999_999
_EMIN: Final = -999_999


class DecimalContextError(RuntimeError):
    """The current decimal context is not the platform's: a process configuration error."""


def _apply(context: decimal.Context) -> None:
    """Set the platform's fields on one context, in place."""
    context.prec = PRECISION
    context.rounding = decimal.ROUND_HALF_EVEN
    context.Emax = _EMAX
    context.Emin = _EMIN
    context.capitals = 1
    context.clamp = 0
    for signal in list(context.traps):
        context.traps[signal] = signal in TRAPPED_SIGNALS
    context.clear_flags()


def configure_decimal_context() -> None:
    """Set the platform's decimal context once, at process start.

    The fields of `decimal.DefaultContext` and of the current context are set in place:
    rebinding the name `DefaultContext` would not reach new threads, which copy the object the
    `decimal` module holds. New threads start from `DefaultContext`; new asyncio tasks copy the
    current context. Calling it again changes nothing.
    """
    _apply(decimal.DefaultContext)
    _apply(decimal.getcontext())


def decimal_context_is_configured(context: decimal.Context | None = None) -> bool:
    """Whether `context` (by default the current one) has the platform's fields."""
    checked = decimal.getcontext() if context is None else context
    return (
        checked.prec == PRECISION
        and checked.rounding == decimal.ROUND_HALF_EVEN
        and checked.Emax == _EMAX
        and checked.Emin == _EMIN
        and checked.capitals == 1
        and checked.clamp == 0
        and all(
            checked.traps[signal] == (signal in TRAPPED_SIGNALS)
            for signal in checked.traps
        )
    )


def require_configured_context() -> decimal.Context:
    """Return the current context, or raise if it is not the platform's."""
    context = decimal.getcontext()
    if not decimal_context_is_configured(context):
        msg = (
            "the decimal context is not configured; "
            "call atp.numeric.configure_decimal_context() at process start"
        )
        raise DecimalContextError(msg)
    return context
