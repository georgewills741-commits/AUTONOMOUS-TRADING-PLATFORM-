"""The Quantitative Engine's indicators, in floats (TEC-003; the Stage 2 plan's U7 and D5),
against values worked by hand from their definitions."""

from __future__ import annotations

import itertools
import json
import math
from collections.abc import Callable, Sequence
from decimal import Decimal

import pytest

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


def _bar(prices: Ohlc, index: int, base: str, closed: bool) -> OhlcvBar:
    market = MarketRef.from_json(json.dumps(_market_json(base)))
    key = evidence_id(
        venue="example", stream=Stream.OHLCV, market=market, venue_key=str(next(_keys))
    )
    opened = START + index * INTERVAL * SECOND
    fields = {
        "market": _market_json(base),
        "interval_seconds": INTERVAL,
        "open_time_ns": opened,
        "open": prices[0],
        "high": prices[1],
        "low": prices[2],
        "close": prices[3],
        "base_volume": "1",
        "closed": closed,
        "receive_time_ns": opened + INTERVAL * SECOND,
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
    for index, given in enumerate(prices):
        if index == skip:
            continue
        ohlc = (given, given, given, given) if isinstance(given, str) else given
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
def test_only_the_last_bar_must_have_been_valid_when_assessed() -> None:
    bars = series(_closes(1, 2, 3))
    old = MarketDataValidator(LIMITS).validate(
        bars[0].item, now_ns=START + 3600 * SECOND, drifting_venues=frozenset()
    )
    assert isinstance(old, Validated) and not old.eligible
    assert sma([old, *bars[1:]], 3, now_ns=USE, limits=LIMITS).value == 2.0
    with pytest.raises(CalculationRefused) as refused:
        sma(series(_closes(1, 2, 3), late=True), 3, now_ns=USE, limits=LIMITS)
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
