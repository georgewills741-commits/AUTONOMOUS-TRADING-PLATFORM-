"""Indicators over a market's closed bars, in floats (QNT-002; TEC-003 allows floats for
indicators; the Stage 2 plan's U7 and D5).

This is the one module of the engine that computes in floats, and it builds no amount: it
imports nothing from `atp.numeric`, which alone builds amounts (the structure test), and
`atp.numeric.amount` and every amount field of a contract refuse a float. A bar's prices become
floats here, each the float nearest its exact value; sums are taken with `math.fsum`, rounded
once. The results are the same for the same bars on the same platform; across platforms the
last digits can differ (the Stage 2 plan's risks), so a result's evidence identifier digests its
inputs and parameters, never its value.

Every indicator reads a series of `Validated` bars of one market and one interval, closed, in
order, one per interval: anything else raises `TypeError` or `ValueError`. A series with bars
missing between two of its bars is refused (GAP), as is one shorter than the indicator's periods
need (INSUFFICIENT_DATA), and one whose last bar was not VALID when assessed (MKD-012); earlier
bars are history, which is older than a freshness limit by nature. A value the definition does
not give, or a float cannot hold, is refused (UNDEFINED).
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from decimal import Decimal
from itertools import pairwise
from typing import Final

from atp.marketdata import OhlcvBar, Validated, bar_end_ns
from atp.quant._common import (
    CalculationRefused,
    RefusalCause,
    calculation_id,
    require_eligible,
)
from atp.quant._contracts import Correlation, IndicatorKind, IndicatorValue

INDICATOR_CALCULATION: Final = "atp.quant.indicator"
CORRELATION_CALCULATION: Final = "atp.quant.correlation"
INDICATOR_VERSION: Final = "1.0"
"""The version of this module's definitions; a change to any of them is a new version."""

_NANOSECONDS_PER_SECOND: Final = 1_000_000_000


def _check_period(period: int, what: str = "period", minimum: int = 1) -> None:
    if type(period) is not int:
        msg = f"the {what} is a whole number"
        raise TypeError(msg)
    if period < minimum:
        msg = f"the {what} is at least {minimum}"
        raise ValueError(msg)


def _series(bars: Sequence[Validated[OhlcvBar]], needed: int) -> list[OhlcvBar]:
    """The bars of `bars`, checked as the module's docstring says."""
    given = list(bars)
    items: list[OhlcvBar] = []
    for data in given:
        entry: object = data  # typed code cannot pass anything else; other code can
        if type(entry) is not Validated or type(data.item) is not OhlcvBar:
            msg = "an indicator reads bars validated by atp.marketdata"
            raise TypeError(msg)
        if not data.item.closed:
            msg = "an indicator reads closed bars, whose values are final"
            raise ValueError(msg)
        items.append(data.item)
    for previous, bar in pairwise(items):
        if (
            bar.market != items[0].market
            or bar.interval_seconds != items[0].interval_seconds
        ):
            msg = "the bars are of one market and one interval"
            raise ValueError(msg)
        step = bar.open_time_ns - previous.open_time_ns
        interval = bar.interval_seconds * _NANOSECONDS_PER_SECOND
        if step < interval:
            msg = "the bars are in order, one per interval"
            raise ValueError(msg)
        if step > interval:
            raise CalculationRefused(
                RefusalCause.GAP, "bars are missing between two of the bars given"
            )
    if len(items) < needed:
        raise CalculationRefused(
            RefusalCause.INSUFFICIENT_DATA,
            f"the indicator needs {needed} bars; {len(items)} were given",
        )
    require_eligible(given[-1], "last bar")
    return items


def _price(value: Decimal) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise CalculationRefused(
            RefusalCause.UNDEFINED, "a price is beyond what a float holds"
        )
    return number


def _sum(values: Iterable[float]) -> float:
    """The sum of `values`, rounded once (`math.fsum`); a sum beyond what a float holds is
    refused."""
    try:
        return math.fsum(values)
    except OverflowError:
        raise CalculationRefused(
            RefusalCause.UNDEFINED, "a sum is beyond what a float holds"
        ) from None


def _closes(series: Sequence[OhlcvBar]) -> list[float]:
    return [_price(bar.close) for bar in series]


def _finite(value: float) -> float:
    if not math.isfinite(value):
        raise CalculationRefused(
            RefusalCause.UNDEFINED, "the result is beyond what a float holds"
        )
    return value


def _indicator(
    kind: IndicatorKind,
    periods: tuple[int, ...],
    value: float,
    series: Sequence[OhlcvBar],
) -> IndicatorValue:
    inputs = tuple(bar.evidence_id for bar in series)
    parameters = [
        ("indicator", kind.value),
        ("periods", ",".join(str(period) for period in periods)),
    ]
    return IndicatorValue(
        market=series[-1].market,
        interval_seconds=series[-1].interval_seconds,
        indicator=kind,
        periods=periods,
        value=_finite(value),
        time_ns=bar_end_ns(series[-1]),
        inputs=inputs,
        calculation_version=INDICATOR_VERSION,
        evidence_id=calculation_id(
            INDICATOR_CALCULATION, INDICATOR_VERSION, parameters, inputs
        ),
    )


def _ema_series(values: Sequence[float], period: int) -> list[float]:
    """The exponential moving average of `values` from its `period`-th value on: the first is
    the mean of the first `period` values, and each next one EMA + (value - EMA) × k, with
    k = 2 / (period + 1)."""
    k = 2.0 / (period + 1)
    current = _sum(values[:period]) / period
    averages = [current]
    for value in values[period:]:
        current = (value - current) * k + current
        averages.append(current)
    return averages


def sma(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """The simple moving average of the last `period` closes."""
    _check_period(period)
    series = _series(bars, period)[-period:]
    return _indicator(
        IndicatorKind.SMA, (period,), _sum(_closes(series)) / period, series
    )


def ema(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """The exponential moving average of the closes of all the bars given, at least `period`:
    started from the simple average of the first `period` (`_ema_series`)."""
    _check_period(period)
    series = _series(bars, period)
    value = _ema_series(_closes(series), period)[-1]
    return _indicator(IndicatorKind.EMA, (period,), value, series)


def rsi(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """Wilder's relative strength index of all the bars given, at least `period` + 1.

    Each close's change from the one before is a gain or a loss. The first average gain and loss
    are the means of the first `period`; each next one is (average × (period - 1) + this one) /
    period. The RSI is 100 - 100 / (1 + average gain / average loss): 100 with no loss, and
    refused (UNDEFINED) with neither a gain nor a loss.
    """
    _check_period(period)
    series = _series(bars, period + 1)
    changes = [later - earlier for earlier, later in pairwise(_closes(series))]
    gains = [max(change, 0.0) for change in changes]
    losses = [max(-change, 0.0) for change in changes]
    average_gain = _sum(gains[:period]) / period
    average_loss = _sum(losses[:period]) / period
    for gain, loss in zip(gains[period:], losses[period:], strict=True):
        average_gain = (average_gain * (period - 1) + gain) / period
        average_loss = (average_loss * (period - 1) + loss) / period
    if average_loss == 0:
        if average_gain == 0:
            raise CalculationRefused(
                RefusalCause.UNDEFINED,
                "the RSI of prices that never moved is not defined",
            )
        value = 100.0
    else:
        value = 100.0 - 100.0 / (1.0 + average_gain / average_loss)
    return _indicator(IndicatorKind.RSI, (period,), value, series)


def macd(
    bars: Sequence[Validated[OhlcvBar]], fast: int, slow: int, signal: int
) -> tuple[IndicatorValue, IndicatorValue, IndicatorValue]:
    """Appel's MACD of all the bars given, at least `slow` + `signal` - 1: its line, the fast
    EMA of the closes less the slow one, from the first close the slow one has; its signal, the
    `signal`-period EMA of the line; and its histogram, the line less the signal. The periods
    are given in the order (fast, slow, signal), the fast below the slow."""
    for name, period in (("fast", fast), ("slow", slow), ("signal", signal)):
        _check_period(period, f"{name} period")
    if fast >= slow:
        msg = "the fast period is below the slow one"
        raise ValueError(msg)
    series = _series(bars, slow + signal - 1)
    closes = _closes(series)
    fast_averages = _ema_series(closes, fast)[slow - fast :]
    slow_averages = _ema_series(closes, slow)
    line = [
        fast_value - slow_value
        for fast_value, slow_value in zip(fast_averages, slow_averages, strict=True)
    ]
    signal_value = _ema_series(line, signal)[-1]
    periods = (fast, slow, signal)
    return (
        _indicator(IndicatorKind.MACD_LINE, periods, line[-1], series),
        _indicator(IndicatorKind.MACD_SIGNAL, periods, signal_value, series),
        _indicator(
            IndicatorKind.MACD_HISTOGRAM, periods, line[-1] - signal_value, series
        ),
    )


def atr(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """Wilder's average true range of all the bars given, at least `period` + 1.

    A bar's true range, from the second bar on, is the largest of its high less its low, and the
    distances of its high and of its low from the close before it. The first average is the mean
    of the first `period` true ranges; each next one is (average × (period - 1) + this one) /
    period.
    """
    _check_period(period)
    series = _series(bars, period + 1)
    ranges = []
    for earlier, bar in pairwise(series):
        high, low, close = _price(bar.high), _price(bar.low), _price(earlier.close)
        ranges.append(max(high - low, abs(high - close), abs(low - close)))
    value = _sum(ranges[:period]) / period
    for true_range in ranges[period:]:
        value = (value * (period - 1) + true_range) / period
    return _indicator(IndicatorKind.ATR, (period,), value, series)


def _ends(bars: Sequence[Validated[OhlcvBar]], period: int) -> list[OhlcvBar]:
    return _series(bars, period + 1)[-(period + 1) :]


def simple_return(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """The return over the last `period` bars: the last close over the close `period` bars
    before it, less one."""
    _check_period(period)
    series = _ends(bars, period)
    value = _price(series[-1].close) / _price(series[0].close) - 1.0
    return _indicator(IndicatorKind.SIMPLE_RETURN, (period,), value, series)


def log_return(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """The logarithmic return over the last `period` bars: the natural logarithm of the last
    close over the close `period` bars before it."""
    _check_period(period)
    series = _ends(bars, period)
    value = math.log(_price(series[-1].close) / _price(series[0].close))
    return _indicator(IndicatorKind.LOG_RETURN, (period,), value, series)


def _log_returns(series: Sequence[OhlcvBar]) -> list[float]:
    return [math.log(later / earlier) for earlier, later in pairwise(_closes(series))]


def volatility(bars: Sequence[Validated[OhlcvBar]], period: int) -> IndicatorValue:
    """The volatility of the last `period` one-bar log returns, at least two: their sample
    standard deviation, the square root of the sum of their squared distances from their mean
    over `period` - 1. It is per bar, not scaled to a year."""
    _check_period(period, minimum=2)
    series = _ends(bars, period)
    returns = _log_returns(series)
    mean = _sum(returns) / period
    variance = _sum((value - mean) ** 2 for value in returns) / (period - 1)
    return _indicator(IndicatorKind.VOLATILITY, (period,), math.sqrt(variance), series)


def correlation(
    bars: Sequence[Validated[OhlcvBar]],
    other: Sequence[Validated[OhlcvBar]],
    period: int,
) -> Correlation:
    """Pearson's correlation of two markets' last `period` one-bar log returns, at least two,
    over bars of one interval opening at the same times: the sum of the products of their
    distances from their means, over the square root of the product of the sums of their
    squares. Returns that never vary give no correlation (UNDEFINED). A result a float's
    rounding puts just beyond -1 or 1 is that bound."""
    _check_period(period, minimum=2)
    first, second = _ends(bars, period), _ends(other, period)
    if any(
        a.open_time_ns != b.open_time_ns or a.interval_seconds != b.interval_seconds
        for a, b in zip(first, second, strict=True)
    ):
        msg = "the two series are of one interval and open at the same times"
        raise ValueError(msg)
    x, y = _log_returns(first), _log_returns(second)
    x_mean, y_mean = _sum(x) / period, _sum(y) / period
    covariance = _sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y, strict=True))
    x_spread = _sum((a - x_mean) ** 2 for a in x)
    y_spread = _sum((b - y_mean) ** 2 for b in y)
    if x_spread == 0 or y_spread == 0:
        raise CalculationRefused(
            RefusalCause.UNDEFINED, "returns that never vary have no correlation"
        )
    value = _finite(covariance / math.sqrt(x_spread * y_spread))
    inputs = tuple(bar.evidence_id for bar in (*first, *second))
    return Correlation(
        market=first[-1].market,
        other=second[-1].market,
        interval_seconds=first[-1].interval_seconds,
        period=period,
        value=max(-1.0, min(1.0, value)),
        time_ns=bar_end_ns(first[-1]),
        inputs=inputs,
        calculation_version=INDICATOR_VERSION,
        evidence_id=calculation_id(
            CORRELATION_CALCULATION,
            INDICATOR_VERSION,
            [("period", str(period))],
            inputs,
        ),
    )
