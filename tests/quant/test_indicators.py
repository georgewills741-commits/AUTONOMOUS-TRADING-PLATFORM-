"""The Quantitative Engine's indicators, in floats (TEC-003; the Stage 2 plan's U7 and D5),
against values worked by hand from their definitions."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from collections.abc import Callable, Sequence
from decimal import Decimal
from functools import partial

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.marketdata import (
    MarketDataValidator,
    MarketRef,
    OhlcvBar,
    QuarantineRecord,
    Stream,
    StreamLimits,
    Validated,
    ValidationLimits,
    evidence_id,
)
from atp.quant import (
    CALCULATION_FORM,
    INDICATOR_VERSION,
    CalculationRefused,
    Correlation,
    IndicatorKind,
    IndicatorValue,
    RefusalCause,
    atr,
    correlation,
    ema,
    log_return,
    macd,
    rsi,
    simple_return,
    sma,
    volatility,
)

SECOND = 1_000_000_000
START = 1_763_600_000 * SECOND
INTERVAL = 60
# The time of use: ten minutes after the first bar opened, when the last bar of every series
# below, at most seven bars long, is VALID.
USE = START + 600 * SECOND
LIMITS = ValidationLimits(
    streams=tuple(
        StreamLimits(
            stream=stream, stale_after_ns=600 * SECOND, invalid_after_ns=3600 * SECOND
        )
        for stream in Stream
    ),
    max_event_ahead_ns=100_000_000,
    duplicate_memory=4,
    outlier_limit=Decimal("1e999"),
    outlier_confirmations=2,
    inconsistency_limit=Decimal(100),
    minimum_other_venues=2,
)
LINEAGE = {
    "source": "wss://example/ws",
    "adapter": "atp.exchange.example",
    "adapter_version": "1.0",
}
_keys = itertools.count()
Ohlc = tuple[str, str, str, str]


def _market_json(base: str) -> dict[str, str]:
    return {
        "venue": "example",
        "base": base,
        "quote": "USDT",
        "instrument_type": "spot",
    }


def _bar(
    prices: Ohlc, index: int, base: str, closed: bool, interval: int = INTERVAL
) -> OhlcvBar:
    market = MarketRef.from_json(json.dumps(_market_json(base)))
    key = evidence_id(
        venue="example", stream=Stream.OHLCV, market=market, venue_key=str(next(_keys))
    )
    opened = START + index * INTERVAL * SECOND
    fields = {
        "market": _market_json(base),
        "interval_seconds": interval,
        "open_time_ns": opened,
        "open": prices[0],
        "high": prices[1],
        "low": prices[2],
        "close": prices[3],
        "base_volume": "1",
        "closed": closed,
        "receive_time_ns": opened + interval * SECOND,
        "evidence_id": key,
        "lineage": LINEAGE,
    }
    return OhlcvBar.from_json(json.dumps(fields))


def series(
    prices: Sequence[Ohlc | str],
    base: str = "BTC",
    skip: int | None = None,
    late: bool = False,
    closed_last: bool = True,
) -> list[Validated[OhlcvBar]]:
    """Validated bars, one per interval, each validated when it closed; a price given alone is
    a bar that opened, peaked, bottomed, and closed at it. `skip` leaves a bar out (a gap), and
    `late` validates the last bar when it is no longer VALID."""
    validator = MarketDataValidator(LIMITS)
    result: list[Validated[OhlcvBar]] = []
    for index, price in enumerate(prices):
        if index == skip:
            continue
        ohlc = (price, price, price, price) if isinstance(price, str) else price
        last = index == len(prices) - 1
        item = _bar(ohlc, index, base, closed=closed_last or not last)
        now = (
            START
            + (index + 1) * INTERVAL * SECOND
            + (7200 * SECOND if late and last else 0)
        )
        validated = validator.validate(item, now_ns=now, drifting_venues=frozenset())
        assert not isinstance(validated, QuarantineRecord), validated
        result.append(validated)
    return result


def _closes(*values: float) -> list[str]:
    return [str(value) for value in values]


@pytest.mark.req("QNT-001", "QNT-002", "QNT-003", "TEC-003")
def test_the_simple_moving_average_reads_the_last_period_closes() -> None:
    bars = series(_closes(1, 2, 3, 4, 5))
    result = sma(bars, 3, now_ns=USE, limits=LIMITS)
    assert result.value == 4.0
    assert result.indicator is IndicatorKind.SMA and result.periods == (3,)
    assert result.inputs == tuple(bar.item.evidence_id for bar in bars[-3:])
    assert result.time_ns == START + 5 * INTERVAL * SECOND
    assert result.interval_seconds == INTERVAL
    assert result.calculation_version == INDICATOR_VERSION == "1.0"


@pytest.mark.req("QNT-002")
def test_the_exponential_moving_average_starts_from_the_simple_one() -> None:
    # k = 2 / 4 = 0.5; the first average (2 + 4 + 6) / 3 = 4; then 4 + (8 - 4) × 0.5 = 6,
    # and 6 + (10 - 6) × 0.5 = 8.
    bars = series(_closes(2, 4, 6, 8, 10))
    result = ema(bars, 3, now_ns=USE, limits=LIMITS)
    assert result.value == 8.0
    assert result.inputs == tuple(bar.item.evidence_id for bar in bars)


@pytest.mark.req("QNT-002")
def test_wilder_s_rsi() -> None:
    # Changes +1, -1, +2. Period 2: first averages, gain (1 + 0) / 2 = 0.5, loss
    # (0 + 1) / 2 = 0.5; then gain (0.5 + 2) / 2 = 1.25, loss (0.5 + 0) / 2 = 0.25; RS = 5,
    # RSI = 100 - 100 / 6.
    assert rsi(
        series(_closes(10, 11, 10, 12)), 2, now_ns=USE, limits=LIMITS
    ).value == pytest.approx(250 / 3, rel=1e-12)
    # One more change, -1: gain 1.25 / 2 = 0.625, loss (0.25 + 1) / 2 = 0.625; RS = 1.
    assert rsi(
        series(_closes(10, 11, 10, 12, 11)), 2, now_ns=USE, limits=LIMITS
    ).value == pytest.approx(50.0)
    # Period 3, where Wilder's smoothing weighs the average by 2 / 3: changes +1, -1, +2,
    # -1, +2; first averages, gain 3 / 3 = 1, loss 1 / 3; then gain (1 * 2 + 0) / 3 = 2 / 3,
    # loss (1 / 3 * 2 + 1) / 3 = 5 / 9; then gain (2 / 3 * 2 + 2) / 3 = 10 / 9, loss
    # (5 / 9 * 2 + 0) / 3 = 10 / 27; RS = 3, RSI = 100 - 100 / 4 = 75.
    assert rsi(
        series(_closes(10, 11, 10, 12, 11, 13)), 3, now_ns=USE, limits=LIMITS
    ).value == pytest.approx(75.0, rel=1e-12)
    # No loss at all: 100.
    assert rsi(series(_closes(1, 2, 3)), 2, now_ns=USE, limits=LIMITS).value == 100.0


def test_the_rsi_of_prices_that_never_moved_is_refused() -> None:
    with pytest.raises(CalculationRefused) as refused:
        rsi(series(_closes(5, 5, 5)), 2, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.UNDEFINED


@pytest.mark.req("QNT-002")
def test_appel_s_macd() -> None:
    # Closes 1, 3, 2, 5, 4, 6; fast 2 (k = 2/3), slow 3 (k = 1/2), signal 2.
    # Fast EMA from the second close: 2, 2, 4, 4, 16/3. Slow from the third: 2, 3.5, 3.75,
    # 4.875. Line from the third: 0, 0.5, 0.25, 11/24. Signal: (0 + 0.5) / 2 = 0.25, then
    # 0.25, then 0.25 + (11/24 - 0.25) × 2/3 = 7/18. Histogram 11/24 - 7/18 = 5/72.
    bars = series(_closes(1, 3, 2, 5, 4, 6))
    line, signal, histogram = macd(bars, 2, 3, 2, now_ns=USE, limits=LIMITS)
    assert line.value == pytest.approx(11 / 24, rel=1e-12)
    assert signal.value == pytest.approx(7 / 18, rel=1e-12)
    assert histogram.value == pytest.approx(5 / 72, rel=1e-12)
    assert [value.indicator for value in (line, signal, histogram)] == [
        IndicatorKind.MACD_LINE,
        IndicatorKind.MACD_SIGNAL,
        IndicatorKind.MACD_HISTOGRAM,
    ]
    assert {value.periods for value in (line, signal, histogram)} == {(2, 3, 2)}
    assert len({value.evidence_id for value in (line, signal, histogram)}) == 3


def test_macd_needs_slow_plus_signal_less_one_bars_and_a_fast_below_the_slow() -> None:
    assert macd(series(_closes(1, 3, 2, 5)), 2, 3, 2, now_ns=USE, limits=LIMITS)[
        0
    ].value == pytest.approx(0.5)
    with pytest.raises(CalculationRefused) as refused:
        macd(series(_closes(1, 3, 2)), 2, 3, 2, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INSUFFICIENT_DATA
    with pytest.raises(ValueError, match="fast period is below"):
        macd(series(_closes(1, 3, 2, 5)), 3, 3, 2, now_ns=USE, limits=LIMITS)


@pytest.mark.req("QNT-002")
def test_wilder_s_average_true_range() -> None:
    # True ranges from the second bar: max(2, 2, 0) = 2; max(2, 2, 0) = 2; max(4, 4, 0) = 4;
    # max(2, 0, 2) = 2; and, after a jump, max(1, 7, 6) = 7. Period 2: the first average
    # (2 + 2) / 2 = 2, then (2 + 4) / 2 = 3, (3 + 2) / 2 = 2.5, (2.5 + 7) / 2 = 4.75.
    bars = series(
        [
            ("9", "10", "8", "9"),
            ("10", "11", "9", "10"),
            ("11", "12", "10", "11"),
            ("14", "15", "11", "14"),
            ("13", "14", "12", "13"),
            ("19.5", "20", "19", "19.5"),
        ]
    )
    assert atr(bars, 2, now_ns=USE, limits=LIMITS).value == pytest.approx(4.75)
    assert atr(bars[:3], 2, now_ns=USE, limits=LIMITS).value == pytest.approx(2.0)


@pytest.mark.req("QNT-002")
def test_returns_over_a_period() -> None:
    bars = series(_closes(90, 100, 105, 110))
    assert simple_return(bars, 2, now_ns=USE, limits=LIMITS).value == pytest.approx(
        0.1, rel=1e-12
    )
    assert log_return(bars, 2, now_ns=USE, limits=LIMITS).value == pytest.approx(
        math.log(1.1), rel=1e-12
    )
    assert simple_return(bars, 2, now_ns=USE, limits=LIMITS).inputs == tuple(
        b.item.evidence_id for b in bars[-3:]
    )


@pytest.mark.req("QNT-002")
def test_volatility_is_the_sample_deviation_of_log_returns() -> None:
    # Log returns a, b, a with a = ln 1.1 and b = ln 0.9: the mean is (2a + b) / 3, the squared
    # distances sum to 2(a - b)² / 3, so the sample variance is (a - b)² / 3 and the deviation
    # ln(1.1 / 0.9) / √3.
    bars = series(["100", "110", "99", "108.9"])
    result = volatility(bars, 3, now_ns=USE, limits=LIMITS)
    assert result.value == pytest.approx(math.log(11 / 9) / math.sqrt(3), rel=1e-12)
    with pytest.raises(ValueError, match="at least 2"):
        volatility(bars, 1, now_ns=USE, limits=LIMITS)


@pytest.mark.req("QNT-002")
def test_correlation_of_two_markets_returns() -> None:
    # Returns a, b, a and b, a, b move exactly against each other.
    first = series(["100", "110", "99", "108.9"], base="BTC")
    second = series(["50", "45", "49.5", "44.55"], base="ETH")
    result = correlation(first, second, 3, now_ns=USE, limits=LIMITS)
    assert result.value == pytest.approx(-1.0, abs=1e-12)
    assert type(result) is Correlation
    assert (result.market.base, result.other.base, result.period) == ("BTC", "ETH", 3)
    assert result.inputs == tuple(b.item.evidence_id for b in (*first, *second))
    # Returns a, b, a, b and a, a, b, b: the products of their distances from the means cancel.
    first = series(["100", "110", "99", "108.9", "98.01"], base="BTC")
    second = series(["100", "110", "121", "108.9", "98.01"], base="ETH")
    assert correlation(
        first, second, 4, now_ns=USE, limits=LIMITS
    ).value == pytest.approx(0.0, abs=1e-9)


def test_correlation_needs_returns_that_vary_and_aligned_bars() -> None:
    flat = series(_closes(5, 5, 5), base="ETH")
    with pytest.raises(CalculationRefused) as refused:
        correlation(series(_closes(1, 2, 4)), flat, 2, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.UNDEFINED
    shifted = series(_closes(1, 2, 4, 8), base="ETH")[1:]
    with pytest.raises(ValueError, match="open at the same times"):
        correlation(series(_closes(1, 2, 4)), shifted, 2, now_ns=USE, limits=LIMITS)


@pytest.mark.req("MKD-012")
def test_every_bar_must_have_been_valid_when_validated() -> None:
    bars = series(_closes(1, 2, 3))
    old = MarketDataValidator(LIMITS).validate(
        bars[0].item, now_ns=START + 3600 * SECOND, drifting_venues=frozenset()
    )
    assert isinstance(old, Validated) and not old.eligible
    with pytest.raises(CalculationRefused, match="the bar was not VALID") as refused:
        sma([old, *bars[1:]], 3, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    with pytest.raises(CalculationRefused, match="last bar was not VALID") as refused:
        sma(series(_closes(1, 2, 3), late=True), 3, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT


@pytest.mark.req("MKD-012")
def test_earlier_bars_are_history_not_assessed_again() -> None:
    # Twelve bars, the last validated when it closed, 720 seconds after the first opened; at
    # that time the first bar, which closed 660 seconds earlier, is past the stale limit.
    bars = series(_closes(*range(1, 13)))
    assert sma(bars, 12, now_ns=START + 720 * SECOND, limits=LIMITS).value == 6.5


@pytest.mark.req("MKD-012")
def test_a_time_of_use_before_a_bar_was_validated_is_refused() -> None:
    bars = series(_closes(1, 2, 3))  # validated 60, 120, and 180 seconds after START
    with pytest.raises(
        CalculationRefused, match="before the last bar was validated"
    ) as refused:
        sma(bars, 3, now_ns=START + 179 * SECOND, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    assert sma(bars, 3, now_ns=START + 180 * SECOND, limits=LIMITS).value == 2.0
    again = MarketDataValidator(LIMITS).validate(
        bars[0].item, now_ns=START + 200 * SECOND, drifting_venues=frozenset()
    )
    assert isinstance(again, Validated) and again.eligible
    with pytest.raises(
        CalculationRefused, match="before the bar was validated"
    ) as refused:
        sma([again, *bars[1:]], 3, now_ns=START + 190 * SECOND, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT


def test_a_series_no_longer_valid_at_the_time_of_use_is_refused() -> None:
    bars = series(_closes(1, 2, 3))
    with pytest.raises(CalculationRefused, match="at the time of use") as refused:
        sma(bars, 3, now_ns=USE + 3600 * SECOND, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT


def test_a_gap_and_too_few_bars_are_refused() -> None:
    with pytest.raises(CalculationRefused) as refused:
        sma(series(_closes(1, 2, 3, 4), skip=1), 2, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.GAP
    with pytest.raises(CalculationRefused) as refused:
        sma(series(_closes(1, 2)), 3, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INSUFFICIENT_DATA


def test_bars_out_of_order_mixed_or_open_are_wrong_arguments() -> None:
    bars = series(_closes(1, 2, 3))
    with pytest.raises(ValueError, match="in order"):
        sma([bars[1], bars[0], bars[2]], 2, now_ns=USE, limits=LIMITS)
    with pytest.raises(ValueError, match="one market"):
        sma(
            [*bars[:2], series(_closes(1, 2, 3), base="ETH")[2]],
            2,
            now_ns=USE,
            limits=LIMITS,
        )
    with pytest.raises(ValueError, match="closed bars"):
        sma(series(_closes(1, 2, 3), closed_last=False), 2, now_ns=USE, limits=LIMITS)
    with pytest.raises(TypeError, match="validated"):
        sma([bar.item for bar in bars], 2, now_ns=USE, limits=LIMITS)  # type: ignore[misc]
    with pytest.raises(TypeError, match="whole number"):
        sma(bars, 2.0, now_ns=USE, limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="at least 1"):
        sma(bars, 0, now_ns=USE, limits=LIMITS)


def test_a_bar_given_twice_or_within_its_interval_is_a_wrong_argument() -> None:
    # Gate 3's F-26: each bar opens one interval after the bar before, so a bar given twice,
    # and one that opens half an interval after the bar before, are wrong arguments.
    bars = series(_closes(1, 2, 3))
    with pytest.raises(ValueError, match="one per interval"):
        sma([bars[0], bars[0], bars[1]], 3, now_ns=USE, limits=LIMITS)
    # Bars of two minutes, which `_bar` opens a minute apart.
    validator = MarketDataValidator(LIMITS)
    halves: list[Validated[OhlcvBar]] = []
    for index in (0, 1):
        half = validator.validate(
            _bar(
                ("1", "1", "1", "1"), index, "BTC", closed=True, interval=2 * INTERVAL
            ),
            now_ns=START + (index + 2) * INTERVAL * SECOND,
            drifting_venues=frozenset(),
        )
        assert isinstance(half, Validated) and half.eligible
        halves.append(half)
    with pytest.raises(ValueError, match="one per interval"):
        sma(halves, 2, now_ns=USE, limits=LIMITS)


def test_a_first_bar_of_another_market_or_interval_is_a_wrong_argument() -> None:
    bars = series(_closes(1, 2, 3))
    first = series(_closes(1, 2, 3), base="ETH")[0]
    with pytest.raises(ValueError, match="one market and one interval"):
        sma([first, *bars[1:]], 2, now_ns=USE, limits=LIMITS)
    odd = MarketDataValidator(LIMITS).validate(
        _bar(("1", "1", "1", "1"), -1, "BTC", closed=True, interval=2 * INTERVAL),
        now_ns=START + INTERVAL * SECOND,
        drifting_venues=frozenset(),
    )
    assert isinstance(odd, Validated) and odd.eligible
    with pytest.raises(ValueError, match="one market and one interval"):
        sma([odd, *bars[1:]], 2, now_ns=USE, limits=LIMITS)


def test_the_bar_before_the_last_must_have_been_valid_when_validated() -> None:
    bars = series(_closes(1, 2, 3))
    old = MarketDataValidator(LIMITS).validate(
        bars[1].item, now_ns=START + 3600 * SECOND, drifting_venues=frozenset()
    )
    assert isinstance(old, Validated) and not old.eligible
    with pytest.raises(CalculationRefused, match="the bar was not VALID") as refused:
        sma([bars[0], old, bars[2]], 3, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT


def test_prices_below_one_are_read() -> None:
    assert sma(
        series(["0.5", "0.25", "0.75"]), 3, now_ns=USE, limits=LIMITS
    ).value == pytest.approx(0.5)


def test_the_rsi_needs_one_bar_more_than_its_period() -> None:
    with pytest.raises(CalculationRefused) as refused:
        rsi(series(_closes(1, 2, 3)), 3, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.INSUFFICIENT_DATA


@pytest.mark.parametrize(
    ("name", "minimum"),
    [
        ("sma", 1),
        ("ema", 1),
        ("rsi", 1),
        ("atr", 1),
        ("simple_return", 1),
        ("log_return", 1),
        ("volatility", 2),
        ("correlation", 2),
        ("macd fast", 1),
        ("macd slow", 1),
        ("macd signal", 1),
    ],
)
def test_each_indicator_checks_its_periods(name: str, minimum: int) -> None:
    bars = series(_closes(1, 2, 3, 5, 4, 6, 7))
    other = series(_closes(2, 3, 5, 4, 6, 7, 9), base="ETH")
    calls: dict[str, Callable[[int], object]] = {
        "sma": lambda p: sma(bars, p, now_ns=USE, limits=LIMITS),
        "ema": lambda p: ema(bars, p, now_ns=USE, limits=LIMITS),
        "rsi": lambda p: rsi(bars, p, now_ns=USE, limits=LIMITS),
        "atr": lambda p: atr(bars, p, now_ns=USE, limits=LIMITS),
        "simple_return": lambda p: simple_return(bars, p, now_ns=USE, limits=LIMITS),
        "log_return": lambda p: log_return(bars, p, now_ns=USE, limits=LIMITS),
        "volatility": lambda p: volatility(bars, p, now_ns=USE, limits=LIMITS),
        "correlation": lambda p: correlation(bars, other, p, now_ns=USE, limits=LIMITS),
        "macd fast": lambda p: macd(bars, p, 3, 2, now_ns=USE, limits=LIMITS),
        "macd slow": lambda p: macd(bars, 1, p, 2, now_ns=USE, limits=LIMITS),
        "macd signal": lambda p: macd(bars, 1, 3, p, now_ns=USE, limits=LIMITS),
    }
    with pytest.raises(ValueError, match=f"at least {minimum}"):
        calls[name](minimum - 1)
    with pytest.raises(TypeError, match="whole number"):
        calls[name](float(minimum))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="whole number"):
        calls[name](True)


def test_bars_of_another_interval_are_wrong_arguments() -> None:
    # A bar of twice the interval, opened one of its own intervals after the bar before it, so
    # that only the check of the interval stops it.
    odd = MarketDataValidator(LIMITS).validate(
        _bar(("3", "3", "3", "3"), 3, "BTC", closed=True, interval=2 * INTERVAL),
        now_ns=START + 5 * INTERVAL * SECOND,
        drifting_venues=frozenset(),
    )
    assert isinstance(odd, Validated) and odd.eligible
    with pytest.raises(ValueError, match="one market and one interval"):
        sma([*series(_closes(1, 2)), odd], 2, now_ns=USE, limits=LIMITS)


@pytest.mark.parametrize(
    ("prices", "calculate"),
    [
        # A price beyond what a float holds, and one a float holds only as zero.
        (["1e400", "1e400"], lambda bars: sma(bars, 2, now_ns=USE, limits=LIMITS)),
        (
            ["1e-400", "1e-400"],
            lambda bars: log_return(bars, 1, now_ns=USE, limits=LIMITS),
        ),
        # A sum beyond what a float holds, and a result beyond it.
        (["1e308", "1.5e308"], lambda bars: sma(bars, 2, now_ns=USE, limits=LIMITS)),
        (
            ["1e-300", "1e300"],
            lambda bars: simple_return(bars, 1, now_ns=USE, limits=LIMITS),
        ),
    ],
)
def test_values_beyond_what_a_float_holds_are_refused(
    prices: list[str], calculate: Callable[[list[Validated[OhlcvBar]]], object]
) -> None:
    with pytest.raises(CalculationRefused) as refused:
        calculate(series(prices))
    assert refused.value.cause is RefusalCause.UNDEFINED


def test_a_correlation_rounded_below_minus_one_is_minus_one() -> None:
    # In floats, these returns' correlation comes to -1.0000000000000002 (Gate 3's F-09).
    pair = correlation(
        series(["671", "758", "632", "667"], base="BTC"),
        series(["319530352", "282856024", "339248206", "321446576"], base="ETH"),
        3,
        now_ns=USE,
        limits=LIMITS,
    )
    assert pair.value == -1.0


def test_a_correlation_rounded_beyond_one_is_one() -> None:
    # In floats, these returns' correlation with themselves comes to 1.0000000000000002.
    prices = ["914", "427", "96", "761"]
    pair = correlation(
        series(prices, base="BTC"),
        series(prices, base="ETH"),
        3,
        now_ns=USE,
        limits=LIMITS,
    )
    assert pair.value == 1.0


@pytest.mark.req("MKD-005", "MKD-010")
def test_an_indicator_is_repeatable_and_survives_its_written_form() -> None:
    bars = series(_closes(10, 11, 10, 12, 11, 13))
    first, second = (
        rsi(bars, 3, now_ns=USE, limits=LIMITS),
        rsi(bars, 3, now_ns=USE, limits=LIMITS),
    )
    assert first == second
    assert IndicatorValue.from_json(first.to_json()) == first
    assert rsi(bars, 2, now_ns=USE, limits=LIMITS).evidence_id != first.evidence_id
    pair = correlation(
        bars,
        series(_closes(5, 6, 5, 7, 5, 6), base="ETH"),
        3,
        now_ns=USE,
        limits=LIMITS,
    )
    assert Correlation.from_json(pair.to_json()) == pair


# Gate 3's run 3: the limits of floats (F-14 and F-15) and the rules no test covered (F-15, F-19).


@pytest.mark.parametrize(
    "name",
    [
        "log return down",
        "log return up",
        "volatility down",
        "volatility up",
        "correlation down",
        "correlation up",
    ],
)
def test_a_ratio_of_closes_beyond_what_a_float_holds_is_refused(name: str) -> None:
    # 1e-200 over 1e200 is below the smallest float and reads as zero, whose logarithm Python
    # refuses with ValueError; 1e200 over 1e-200 is above the largest and reads as infinite,
    # which makes the result infinite or not a number: each is refused (UNDEFINED).
    down, up = ["1", "1e200", "1e-200"], ["1", "1e-200", "1e200"]
    other = series(_closes(1, 2, 1), base="ETH")
    calls: dict[str, Callable[[], object]] = {
        "log return down": lambda: log_return(
            series(down[1:]), 1, now_ns=USE, limits=LIMITS
        ),
        "log return up": lambda: log_return(
            series(up[1:]), 1, now_ns=USE, limits=LIMITS
        ),
        "volatility down": lambda: volatility(
            series(down), 2, now_ns=USE, limits=LIMITS
        ),
        "volatility up": lambda: volatility(series(up), 2, now_ns=USE, limits=LIMITS),
        "correlation down": lambda: correlation(
            series(down), other, 2, now_ns=USE, limits=LIMITS
        ),
        "correlation up": lambda: correlation(
            series(up), other, 2, now_ns=USE, limits=LIMITS
        ),
    }
    with pytest.raises(CalculationRefused) as refused:
        calls[name]()
    assert refused.value.cause is RefusalCause.UNDEFINED


def test_a_true_range_reaches_down_from_the_close_before() -> None:
    # A bar that opens below the close before it: max(15 - 14, |15 - 20|, |14 - 20|) = 6, the
    # distance of its low from that close.
    bars = series(["20", ("15", "15", "14", "14.5")])
    assert atr(bars, 1, now_ns=USE, limits=LIMITS).value == pytest.approx(6.0)


def test_a_correlation_s_identifier_digests_the_order_of_its_series() -> None:
    # The two orders give one value for the same markets, named the other way round; the
    # inputs are digested in their order, so the identifiers differ.
    btc, eth = series(_closes(1, 2, 3)), series(_closes(3, 5, 4), base="ETH")
    forward = correlation(btc, eth, 2, now_ns=USE, limits=LIMITS)
    backward = correlation(eth, btc, 2, now_ns=USE, limits=LIMITS)
    assert forward.value == pytest.approx(backward.value)
    assert (forward.market, forward.other) == (backward.other, backward.market)
    assert forward.evidence_id != backward.evidence_id


def test_a_sum_is_rounded_once() -> None:
    # These closes' sum rounded once (`math.fsum`) is 134086961822059248; Python's own `sum`,
    # whose compensation is not exact, gives 134086961822059232.
    closes = ["4.216507376378148e-19", "3.1896766332234296e16", "1.0219019548982494e17"]
    value = sma(series(closes), 3, now_ns=USE, limits=LIMITS).value
    assert value == math.fsum(float(close) for close in closes) / 3


# Closes across the float range: the largest and smallest normal floats, subnormal ones, and
# values beyond both, which a float holds as infinite or zero.
CLOSES = st.builds(
    "{}e{}".format,
    st.sampled_from(["1", "1.7976931348623157", "2.2250738585072014", "4.9", "5"]),
    st.sampled_from([-330, -320, -308, -300, -200, -16, 0, 16, 200, 300, 307, 308]),
)


@given(st.lists(CLOSES, min_size=3, max_size=6), st.data())
def test_every_indicator_gives_a_finite_value_or_a_refusal(
    closes: list[str], data: st.DataObject
) -> None:
    # Gate 3's F-14 and F-21: at every period its bars allow, no exception but a refusal leaves
    # an indicator, and no value it gives is infinite or not a number.
    others = data.draw(st.lists(CLOSES, min_size=len(closes), max_size=len(closes)))
    bars, other = series(closes), series(others, base="ETH")
    count = len(bars)

    def period(low: int, high: int) -> int:
        return data.draw(st.integers(low, high))

    slow = period(2, count)
    fast, signal = period(1, slow - 1), period(1, count - slow + 1)
    calls: list[Callable[[], object]] = [
        lambda: sma(bars, period(1, count), now_ns=USE, limits=LIMITS),
        lambda: ema(bars, period(1, count), now_ns=USE, limits=LIMITS),
        lambda: rsi(bars, period(1, count - 1), now_ns=USE, limits=LIMITS),
        lambda: macd(bars, fast, slow, signal, now_ns=USE, limits=LIMITS),
        lambda: atr(bars, period(1, count - 1), now_ns=USE, limits=LIMITS),
        lambda: simple_return(bars, period(1, count - 1), now_ns=USE, limits=LIMITS),
        lambda: log_return(bars, period(1, count - 1), now_ns=USE, limits=LIMITS),
        lambda: volatility(bars, period(2, count - 1), now_ns=USE, limits=LIMITS),
        lambda: correlation(
            bars, other, period(2, count - 1), now_ns=USE, limits=LIMITS
        ),
    ]
    for call in calls:
        _gives_a_finite_value_or_a_refusal(call, closes)


# The ends of the range in which a float holds a price at full precision, and values between
# them: the ratio of two of them is within a float's normal range, above it, or below it.
EDGES = ("2.2250738585072014e-308", "1e-200", "1", "1e200", "1.7976931348623157e308")


def test_every_indicator_of_closes_at_a_float_s_limits_gives_a_finite_value_or_a_refusal() -> (
    None
):
    # Gate 3's F-21, whose case the property test seldom draws: every four closes taken from
    # EDGES, at every period their bars allow, with a correlation against closes whose returns
    # differ in sign, in either order.
    other = series(["1", "2", "1", "1"], base="ETH")
    for closes in itertools.product(EDGES, repeat=4):
        bars = series(list(closes))
        cases: list[tuple[Callable[..., object], tuple[object, ...]]] = [
            *((sma, (bars, period)) for period in range(1, 5)),
            *((ema, (bars, period)) for period in range(1, 5)),
            *((rsi, (bars, period)) for period in range(1, 4)),
            *((atr, (bars, period)) for period in range(1, 4)),
            *((simple_return, (bars, period)) for period in range(1, 4)),
            *((log_return, (bars, period)) for period in range(1, 4)),
            *((volatility, (bars, period)) for period in range(2, 4)),
            *((correlation, (bars, other, period)) for period in range(2, 4)),
            *((correlation, (other, bars, period)) for period in range(2, 4)),
            *(
                (macd, (bars, fast, slow, signal))
                for slow in range(2, 5)
                for fast in range(1, slow)
                for signal in range(1, 6 - slow)
            ),
        ]
        for function, arguments in cases:
            named = [
                argument
                if isinstance(argument, int)
                else "bars"
                if argument is bars
                else "other"
                for argument in arguments
            ]
            _gives_a_finite_value_or_a_refusal(
                partial(function, *arguments, now_ns=USE, limits=LIMITS),
                f"{function.__name__}{named} of the closes {closes}",
            )


def _gives_a_finite_value_or_a_refusal(
    call: Callable[[], object], case: object
) -> None:
    """Check that `call` gives finite values or is refused, and raises nothing else; a failure
    names `case`."""
    try:
        result = call()
    except CalculationRefused:
        return
    except Exception as error:
        error.add_note(f"the case: {case}")
        raise
    results = result if isinstance(result, tuple) else (result,)
    assert all(math.isfinite(item.value) for item in results), case


class _Forged(Validated[OhlcvBar]):  # type: ignore[misc]
    """A bar passed off as validated: a subclass that skips the validator's check."""

    def __post_init__(self, creator: object) -> None:
        pass


def test_a_bar_passed_off_as_validated_is_refused() -> None:
    bars = series(_closes(1, 2))
    forged = _Forged(bars[0].item, bars[0].assessment, creator=None)
    with pytest.raises(TypeError, match="validated by atp.marketdata"):
        sma([forged, bars[1]], 2, now_ns=USE, limits=LIMITS)


def test_an_indicator_s_and_a_correlation_s_identifiers_have_their_form() -> None:
    def digest(calculation: str, parameters: list[list[str]], inputs: list[str]) -> str:
        form = json.dumps(
            [CALCULATION_FORM, calculation, "1.0", parameters, inputs],
            ensure_ascii=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(form.encode("ascii")).hexdigest()

    btc, eth = series(_closes(1, 2, 3)), series(_closes(3, 5, 4), base="ETH")
    average = sma(btc, 2, now_ns=USE, limits=LIMITS)
    assert average.evidence_id == digest(
        "atp.quant.indicator",
        [["indicator", "sma"], ["periods", "2"]],
        [bar.item.evidence_id for bar in btc[-2:]],
    )
    pair = correlation(btc, eth, 2, now_ns=USE, limits=LIMITS)
    assert pair.evidence_id == digest(
        "atp.quant.correlation",
        [["period", "2"]],
        [bar.item.evidence_id for bar in (*btc, *eth)],
    )


def test_a_close_beyond_what_a_float_holds_is_refused_not_read_as_infinite() -> None:
    # Read as infinite, it would give an RSI of 100: a gain, and no loss.
    with pytest.raises(CalculationRefused) as refused:
        rsi(series(["1", "1e400"]), 1, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.UNDEFINED


@pytest.mark.parametrize(
    "name", ["atr", "simple_return", "log_return", "volatility", "correlation"]
)
def test_an_indicator_of_changes_needs_one_bar_more_than_its_period(name: str) -> None:
    bars, other = series(_closes(1, 2, 4)), series(_closes(2, 3, 5), base="ETH")
    calls: dict[str, Callable[[], object]] = {
        "atr": lambda: atr(bars, 3, now_ns=USE, limits=LIMITS),
        "simple_return": lambda: simple_return(bars, 3, now_ns=USE, limits=LIMITS),
        "log_return": lambda: log_return(bars, 3, now_ns=USE, limits=LIMITS),
        "volatility": lambda: volatility(bars, 3, now_ns=USE, limits=LIMITS),
        "correlation": lambda: correlation(bars, other, 3, now_ns=USE, limits=LIMITS),
    }
    with pytest.raises(
        CalculationRefused, match="needs 4 bars; 3 were given"
    ) as refused:
        calls[name]()
    assert refused.value.cause is RefusalCause.INSUFFICIENT_DATA


def test_wilder_s_average_true_range_over_three_bars() -> None:
    # True ranges from the second bar: max(3, 2, 1) = 3; max(2, 1, 1) = 2; max(4, 4, 0) = 4;
    # max(1, 0, 1) = 1; max(6, 0, 6) = 6. Period 3: the first average (3 + 2 + 4) / 3 = 3,
    # then (3 × 2 + 1) / 3 = 7/3, and (7/3 × 2 + 6) / 3 = 32/9.
    bars = series(
        [
            ("10", "10", "10", "10"),
            ("10", "12", "9", "11"),
            ("11", "12", "10", "12"),
            ("12", "16", "12", "15"),
            ("15", "15", "14", "14"),
            ("14", "14", "8", "9"),
        ]
    )
    assert atr(bars, 3, now_ns=USE, limits=LIMITS).value == pytest.approx(32 / 9)


@pytest.mark.parametrize("flat_first", [True, False])
def test_a_correlation_with_one_series_that_never_varies_is_refused(
    flat_first: bool,
) -> None:
    varying, flat = series(_closes(1, 2, 3)), series(_closes(5, 5, 5), base="ETH")
    first, second = (flat, varying) if flat_first else (varying, flat)
    with pytest.raises(CalculationRefused) as refused:
        correlation(first, second, 2, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.UNDEFINED


@pytest.mark.parametrize("ratio", ["7", "1.5"])
def test_returns_that_never_vary_have_no_correlation_whatever_their_mean(
    ratio: str,
) -> None:
    # Closes that each rise by one ratio have five equal returns, whose mean, their sum over
    # five, is not that return in floats, so that their spread about it is not zero.
    closes = [str(Decimal(ratio) ** power) for power in range(6)]
    steady, other = series(closes), series(["1", "3", "2", "5", "4", "7"], base="ETH")
    for first, second in ((steady, other), (other, steady)):
        with pytest.raises(CalculationRefused) as refused:
            correlation(first, second, 5, now_ns=USE, limits=LIMITS)
        assert refused.value.cause is RefusalCause.UNDEFINED


def test_a_correlation_s_time_is_the_end_of_its_last_bars() -> None:
    btc, eth = series(_closes(1, 2, 3)), series(_closes(3, 5, 4), base="ETH")
    pair = correlation(btc, eth, 2, now_ns=USE, limits=LIMITS)
    assert pair.time_ns == START + 3 * INTERVAL * SECOND


# Gate 3's run 4: ratios and prices outside a float's normal range (F-21, F-25), closes read as
# closes (F-22), and the interval a result carries (F-23).


@pytest.mark.parametrize(
    ("first", "second", "period"),
    [
        (["1", "2", "1e-200", "1e200"], ["1", "2", "1", "1"], 3),
        (["1", "2", "1", "1"], ["1", "2", "1e-200", "1e200"], 3),
        (["1", "2", "3", "1e-200", "1e200"], ["1", "2", "3", "1", "1"], 4),
    ],
)
def test_a_correlation_over_a_ratio_beyond_a_float_is_refused_at_any_period(
    first: list[str], second: list[str], period: int
) -> None:
    # An infinite log return made the mean infinite, and its products with the other series'
    # deviations of both signs gave math.fsum both infinities, which it refuses with ValueError.
    with pytest.raises(CalculationRefused) as refused:
        correlation(
            series(first), series(second, base="ETH"), period, now_ns=USE, limits=LIMITS
        )
    assert refused.value.cause is RefusalCause.UNDEFINED


def test_a_ratio_of_closes_below_a_float_s_normal_range_is_refused() -> None:
    # 7e-170 over 1e154 is held as 5e-324, one bit, whose logarithm is -744.44 against -744.09.
    with pytest.raises(CalculationRefused) as refused:
        log_return(series(["1e154", "7e-170"]), 1, now_ns=USE, limits=LIMITS)
    assert refused.value.cause is RefusalCause.UNDEFINED
    # Ratios below the smallest normal float: one well below, and the float just below it.
    for closes in (["2", "4.4e-308"], ["2", "4.450147717014402e-308"]):
        with pytest.raises(CalculationRefused):
            log_return(series(closes), 1, now_ns=USE, limits=LIMITS)
    # The smallest normal float, and the largest, are ratios a float holds in full.
    lowest = log_return(
        series(["2", "4.450147717014403e-308"]), 1, now_ns=USE, limits=LIMITS
    )
    assert lowest.value == math.log(sys.float_info.min)
    highest = log_return(
        series(["1", "1.7976931348623157e308"]), 1, now_ns=USE, limits=LIMITS
    )
    assert highest.value == math.log(sys.float_info.max)


@pytest.mark.parametrize("name", ["volatility", "correlation"])
def test_a_one_bar_ratio_is_the_later_close_over_the_earlier(name: str) -> None:
    # Gate 3's F-27: a one-bar ratio of 1e-307 over 10, below a float's normal range, is
    # refused, and one of 1e308 over 1, within it, is not; their inverses are the opposite.
    other = series(["1", "2", "1", "3"], base="ETH")

    def call(closes: list[str]) -> float:
        bars = series(closes)
        if name == "volatility":
            return volatility(bars, 3, now_ns=USE, limits=LIMITS).value
        return correlation(bars, other, 3, now_ns=USE, limits=LIMITS).value

    with pytest.raises(CalculationRefused) as refused:
        call(["10", "1e-307", "1e-307", "1.5e-307"])
    assert refused.value.cause is RefusalCause.UNDEFINED
    assert math.isfinite(call(["1", "1e308", "1e308", "1.5e308"]))


def test_a_price_below_a_float_s_normal_range_is_refused() -> None:
    # A price well below the smallest normal float, and the float just below it.
    for close in ("2.2e-308", "2.225073858507201e-308"):
        with pytest.raises(CalculationRefused) as refused:
            sma(series([close]), 1, now_ns=USE, limits=LIMITS)
        assert refused.value.cause is RefusalCause.UNDEFINED
    lowest = sma(series(["2.2250738585072014e-308"]), 1, now_ns=USE, limits=LIMITS)
    assert lowest.value == sys.float_info.min


# Bars whose open, high, and low differ from their close, each by its own amount.
_OFFSETS = [
    ("-0.5", "1", "1"),
    ("0.25", "1.5", "0.5"),
    ("-0.75", "1.25", "1.5"),
    ("0.5", "2", "1.25"),
    ("-0.25", "1.75", "0.75"),
    ("0.75", "1.1", "2"),
]


def _ohlc(closes: Sequence[int]) -> list[Ohlc]:
    return [
        (
            str(close + Decimal(opened)),
            str(close + Decimal(high)),
            str(close - Decimal(low)),
            str(close),
        )
        for close, (opened, high, low) in zip(closes, _OFFSETS, strict=True)
    ]


def test_an_indicator_of_closes_reads_the_closes() -> None:
    first, second = [10, 11, 13, 12, 14, 13], [20, 22, 21, 25, 24, 26]
    bars, other = series(_ohlc(first)), series(_ohlc(second), base="ETH")
    plain = series([str(close) for close in first])
    plain_other = series([str(close) for close in second], base="ETH")
    calls: dict[
        str,
        Callable[
            [Sequence[Validated[OhlcvBar]], Sequence[Validated[OhlcvBar]]], object
        ],
    ] = {
        "sma": lambda b, o: sma(b, 3, now_ns=USE, limits=LIMITS),
        "ema": lambda b, o: ema(b, 3, now_ns=USE, limits=LIMITS),
        "rsi": lambda b, o: rsi(b, 3, now_ns=USE, limits=LIMITS),
        "macd": lambda b, o: macd(b, 2, 3, 2, now_ns=USE, limits=LIMITS),
        "simple_return": lambda b, o: simple_return(b, 5, now_ns=USE, limits=LIMITS),
        "log_return": lambda b, o: log_return(b, 5, now_ns=USE, limits=LIMITS),
        "volatility": lambda b, o: volatility(b, 3, now_ns=USE, limits=LIMITS),
        "correlation": lambda b, o: correlation(b, o, 3, now_ns=USE, limits=LIMITS),
    }
    for name, call in calls.items():
        results, expected = call(bars, other), call(plain, plain_other)
        values = results if isinstance(results, tuple) else (results,)
        wanted = expected if isinstance(expected, tuple) else (expected,)
        assert [item.value for item in values] == [item.value for item in wanted], name


def _hourly(closes: Sequence[str], base: str = "BTC") -> list[Validated[OhlcvBar]]:
    # `_bar` opens bar `index` at `index` minutes, so every sixtieth index opens an hour apart.
    validator = MarketDataValidator(LIMITS)
    result: list[Validated[OhlcvBar]] = []
    for index, price in enumerate(closes):
        item = _bar(
            (price, price, price, price), 60 * index, base, closed=True, interval=3600
        )
        checked = validator.validate(
            item,
            now_ns=START + (index + 1) * 3600 * SECOND,
            drifting_venues=frozenset(),
        )
        assert isinstance(checked, Validated), checked
        result.append(checked)
    return result


def test_an_indicator_and_a_correlation_carry_their_bars_interval() -> None:
    first, second = _hourly(["1", "2", "3"]), _hourly(["3", "5", "4"], base="ETH")
    use = START + 3 * 3600 * SECOND
    assert sma(first, 2, now_ns=use, limits=LIMITS).interval_seconds == 3600
    assert (
        correlation(first, second, 2, now_ns=use, limits=LIMITS).interval_seconds
        == 3600
    )


# The class search of Gate 3's run 4 (F-22): each indicator's kind and periods, and MACD's signal
# over its own period.


def test_each_indicator_reports_its_kind_and_periods() -> None:
    bars = series(_closes(1, 2, 4, 3, 5, 6))
    results = {
        IndicatorKind.SMA: sma(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.EMA: ema(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.RSI: rsi(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.ATR: atr(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.SIMPLE_RETURN: simple_return(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.LOG_RETURN: log_return(bars, 3, now_ns=USE, limits=LIMITS),
        IndicatorKind.VOLATILITY: volatility(bars, 3, now_ns=USE, limits=LIMITS),
    }
    for kind, result in results.items():
        assert (result.indicator, result.periods) == (kind, (3,))
    parts = macd(bars, 1, 3, 2, now_ns=USE, limits=LIMITS)
    assert [(part.indicator, part.periods) for part in parts] == [
        (IndicatorKind.MACD_LINE, (1, 3, 2)),
        (IndicatorKind.MACD_SIGNAL, (1, 3, 2)),
        (IndicatorKind.MACD_HISTOGRAM, (1, 3, 2)),
    ]


def test_macd_s_signal_smooths_the_line_over_its_own_period() -> None:
    # Fast, slow, and signal periods all different. The fast EMA of period 1 is the closes; the
    # slow one of period 3 starts at 7/3 and gives 8/3, 23/6, and 59/12; so the line is 5/3,
    # 1/3, 7/6, and 13/12; the signal of period 2 starts at 1 and gives 10/9 and 59/54.
    line, signal, histogram = macd(
        series(_closes(1, 2, 4, 3, 5, 6)), 1, 3, 2, now_ns=USE, limits=LIMITS
    )
    assert line.value == pytest.approx(13 / 12)
    assert signal.value == pytest.approx(59 / 54)
    assert histogram.value == pytest.approx(-1 / 108)
