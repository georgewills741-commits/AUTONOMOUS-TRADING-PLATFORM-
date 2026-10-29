"""The decimal context (ARCH-010, TEC-003): set once, inherited, and refusing silent rounding."""

from __future__ import annotations

import asyncio
import decimal
import threading
from decimal import Decimal

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from atp.numeric import (
    PRECISION,
    TRAPPED_SIGNALS,
    DecimalContextError,
    Rounding,
    amount,
    configure_decimal_context,
    decimal_context_is_configured,
    quantize,
)


@pytest.mark.req("ARCH-010", "TEC-003")
def test_the_session_context_is_configured() -> None:
    context = decimal.getcontext()
    assert decimal_context_is_configured()
    assert context.prec == PRECISION == 34
    assert {
        signal for signal in context.traps if context.traps[signal]
    } == TRAPPED_SIGNALS


def test_exactly_the_five_signals_are_trapped() -> None:
    assert (
        frozenset(
            {
                decimal.FloatOperation,
                decimal.InvalidOperation,
                decimal.DivisionByZero,
                decimal.Overflow,
                decimal.Inexact,
            }
        )
        == TRAPPED_SIGNALS
    )


def _platform_context(**changes: object) -> decimal.Context:
    context = decimal.getcontext().copy()
    for name, value in changes.items():
        setattr(context, name, value)
    return context


@pytest.mark.parametrize(
    "changes",
    [
        {"prec": 28},
        {"prec": 50},
        {"rounding": decimal.ROUND_DOWN},
        {"Emax": 99},
        {"Emin": -99},
        {"clamp": 1},
        {"capitals": 0},
    ],
)
def test_a_context_differing_in_one_field_is_not_configured(
    changes: dict[str, object],
) -> None:
    assert not decimal_context_is_configured(_platform_context(**changes))


@pytest.mark.parametrize("signal", [*TRAPPED_SIGNALS, decimal.Rounded, decimal.Clamped])
def test_a_context_with_one_trap_changed_is_not_configured(
    signal: type[decimal.DecimalException],
) -> None:
    context = _platform_context()
    context.traps[signal] = not context.traps[signal]
    assert not decimal_context_is_configured(context)


def test_division_by_zero_raises() -> None:
    with pytest.raises(decimal.DivisionByZero):
        _ = amount("1") / amount("0")


def test_overflow_raises() -> None:
    with pytest.raises(decimal.Overflow):
        _ = amount("9e999999") * amount("10")


def test_the_default_context_is_configured_in_place() -> None:
    assert decimal_context_is_configured(decimal.DefaultContext)


def test_configuring_again_changes_nothing() -> None:
    configure_decimal_context()
    assert decimal_context_is_configured()
    assert decimal_context_is_configured(decimal.DefaultContext)


def test_a_new_thread_inherits_the_context() -> None:
    seen: list[bool] = []

    def worker() -> None:
        seen.append(decimal_context_is_configured())

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()
    assert seen == [True]


def test_a_new_asyncio_task_inherits_the_context() -> None:
    async def check() -> bool:
        return await asyncio.create_task(_configured_in_task())

    assert asyncio.run(check())


async def _configured_in_task() -> bool:
    return decimal_context_is_configured()


def test_an_unconfigured_context_is_refused() -> None:
    # Python's own defaults (decimal.Context() would copy the configured DefaultContext).
    with decimal.localcontext(
        decimal.Context(prec=28, traps=[decimal.InvalidOperation])
    ):
        assert not decimal_context_is_configured()
        # Its own type, a RuntimeError, so callers can tell it from refused input.
        with pytest.raises(DecimalContextError, match="not configured"):
            amount("1")
        with pytest.raises(DecimalContextError, match="not configured"):
            quantize(Decimal(1), Decimal("0.1"), Rounding.TOWARD_ZERO)
    assert issubclass(DecimalContextError, RuntimeError)


@pytest.mark.req("TEC-003")
def test_a_float_cannot_become_a_decimal() -> None:
    with pytest.raises(decimal.FloatOperation):
        Decimal(0.1)  # noqa: RUF032 -- the float is the point: the trap must refuse it


def test_an_ordering_comparison_with_a_float_raises() -> None:
    with pytest.raises(decimal.FloatOperation):
        _ = amount("1") < 1.5


@pytest.mark.req("ARCH-010", "TEC-003")
def test_an_inexact_result_raises() -> None:
    with pytest.raises(decimal.Inexact):
        _ = amount("1") / amount("3")


@given(st.integers(min_value=1, max_value=10**9), st.sampled_from([3, 7, 11, 13]))
def test_any_division_with_an_inexact_result_raises(
    numerator: int, divisor: int
) -> None:
    # A divisor coprime with 10 that does not divide the numerator gives a repeating decimal.
    assume(numerator % divisor != 0)
    with pytest.raises(decimal.Inexact):
        _ = amount(numerator) / amount(divisor)


def test_an_exact_result_does_not_raise() -> None:
    assert amount("1") / amount("4") == amount("0.25")
