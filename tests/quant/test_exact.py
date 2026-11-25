"""The Quantitative Engine's exact calculations: spread, depth, the Fee Engine, and the Slippage
Engine (the Stage 2 plan's U7), with hand-worked values from their definitions."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections.abc import Callable
from decimal import Decimal

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.config import VenueSettings
from atp.contracts import Contract
from atp.marketdata import (
    BookSnapshot,
    FundingRate,
    MarketDataValidator,
    MarketItem,
    MarketRef,
    QuarantineRecord,
    Stream,
    StreamLimits,
    TakerSide,
    Ticker,
    Validated,
    ValidationLimits,
    evidence_id,
)
from atp.numeric import Rounding, amount, divide
from atp.quant import (
    CALCULATION_FORM,
    CalculationRefused,
    DepthMetrics,
    FeeEstimate,
    FundingEstimate,
    LiquidityRole,
    PositionSide,
    RefusalCause,
    SlippageEstimate,
    SpreadMetrics,
    calculation_id,
    depth_metrics,
    estimate_fee,
    estimate_funding,
    sma,
    spread_metrics,
    walk_book,
)

SECOND = 1_000_000_000
NOW = 1_763_600_000 * SECOND
LIMITS = ValidationLimits(
    streams=tuple(
        StreamLimits(stream=stream, stale_after_ns=SECOND, invalid_after_ns=10 * SECOND)
        for stream in Stream
    ),
    max_event_ahead_ns=100_000_000,
    duplicate_memory=4,
    outlier_limit=Decimal(100),
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
Fields = dict[str, object]


def market_json(kind: str = "spot", venue: str = "example") -> Fields:
    fields: Fields = {
        "venue": venue,
        "base": "BTC",
        "quote": "USDT",
        "instrument_type": kind,
    }
    if kind == "perpetual":
        fields["settle"] = "USDT"
    return fields


def market(kind: str = "spot", venue: str = "example") -> MarketRef:
    return MarketRef.from_json(json.dumps(market_json(kind, venue)))


def common(stream: Stream, kind: str = "spot") -> Fields:
    key = evidence_id(
        venue="example", stream=stream, market=market(kind), venue_key=str(next(_keys))
    )
    return {
        "market": market_json(kind),
        "evidence_id": key,
        "lineage": LINEAGE,
        "event_time_ns": NOW,
        "event_time_resolution": "nanosecond",
        "receive_time_ns": NOW,
    }


def validated[T: MarketItem](item: T, now: int = NOW) -> Validated[T]:
    result = MarketDataValidator(LIMITS).validate(
        item, now_ns=now, drifting_venues=frozenset()
    )
    assert not isinstance(result, QuarantineRecord), result
    return result


def ticker(bid: str | None, ask: str | None) -> Ticker:
    fields = common(Stream.TICKER)
    for name, value in (("bid", bid), ("ask", ask)):
        if value is not None:
            fields |= {name: value, f"{name}_size": "1"}
    return Ticker.from_json(json.dumps(fields))


def book(
    bids: list[tuple[str, str]] | None = None,
    asks: list[tuple[str, str]] | None = None,
) -> BookSnapshot:
    fields = common(Stream.BOOK)
    sides = {
        "bids": [("100", "1"), ("99.5", "2"), ("98", "5")] if bids is None else bids,
        "asks": [("101", "1"), ("102", "2"), ("105", "5")] if asks is None else asks,
    }
    for name, levels in sides.items():
        fields[name] = [{"price": price, "quantity": size} for price, size in levels]
    return BookSnapshot.from_json(json.dumps(fields))


def funding(rate: str) -> FundingRate:
    fields = common(Stream.FUNDING, "perpetual")
    fields |= {
        "rate": rate,
        "funding_time_ns": NOW + 3600 * SECOND,
        "interval_seconds": 28800,
    }
    return FundingRate.from_json(json.dumps(fields))


def venue(maker: str = "0.001", taker: str = "0.002") -> VenueSettings:
    return VenueSettings.from_json(
        json.dumps(
            {
                "venue": "example",
                "instrument_types": ["spot", "perpetual"],
                "fees": [
                    {
                        "instrument_type": "spot",
                        "maker": maker,
                        "taker": taker,
                        "source": "https://example.test/fees",
                        "as_of": "2026-11-01",
                    }
                ],
            }
        )
    )


# Spread and depth.


@pytest.mark.req("QNT-001", "QNT-002", "QNT-003", "TEC-003")
def test_the_spread_of_a_ticker_is_exact_and_its_relative_spread_rounded_up() -> None:
    data = validated(ticker("100", "101"))
    result = spread_metrics(data, amount("0.0001"), now_ns=NOW, limits=LIMITS)
    assert (result.bid, result.ask) == (amount("100"), amount("101"))
    assert str(result.mid) == "100.5"
    assert str(result.spread) == "1"
    # 1 / 100.5 = 0.00995024..., rounded up to a multiple of 0.0001.
    assert str(result.relative_spread) == "0.0100"
    assert result.inputs == (data.item.evidence_id,)
    assert result.time_ns == NOW


def test_the_spread_of_a_book_snapshot_reads_its_best_levels() -> None:
    result = spread_metrics(
        validated(book()), amount("0.00001"), now_ns=NOW, limits=LIMITS
    )
    assert (str(result.bid), str(result.ask), str(result.mid)) == (
        "100",
        "101",
        "100.5",
    )
    # 1 / 100.5 = 0.0099502..., up to 0.00996.
    assert str(result.relative_spread) == "0.00996"


@pytest.mark.parametrize(("bid", "ask"), [(None, "101"), ("100", None)])
def test_a_spread_without_both_sides_is_refused(
    bid: str | None, ask: str | None
) -> None:
    with pytest.raises(CalculationRefused) as refused:
        spread_metrics(
            validated(ticker(bid, ask)), amount("0.0001"), now_ns=NOW, limits=LIMITS
        )
    assert refused.value.cause is RefusalCause.MISSING_INPUT


@pytest.mark.req("QNT-002")
def test_depth_within_a_band_counts_the_levels_inside_it() -> None:
    # The mid 100.5; the bounds 100.5 × 0.99 = 99.495 and 100.5 × 1.01 = 101.505, each
    # within the band.
    snapshot = book(
        bids=[("100", "1"), ("99.495", "2"), ("98", "5")],
        asks=[("101", "1"), ("101.505", "2"), ("103", "5")],
    )
    result = depth_metrics(
        validated(snapshot), amount("0.01"), now_ns=NOW, limits=LIMITS
    )
    assert (str(result.bid_bound), str(result.ask_bound)) == ("99.495", "101.505")
    assert (result.bid_quantity, result.bid_notional) == (
        amount("3"),
        amount("298.990"),
    )
    assert (result.ask_quantity, result.ask_notional) == (
        amount("3"),
        amount("304.010"),
    )
    assert result.bid_complete and result.ask_complete
    assert result.mid == amount("100.5") and result.band == amount("0.01")


def test_depth_is_incomplete_when_the_snapshot_ends_inside_the_band() -> None:
    data = validated(book(bids=[("100", "1")], asks=[("101", "1"), ("101.5", "2")]))
    result = depth_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS)
    assert not result.bid_complete and not result.ask_complete
    assert (result.bid_quantity, result.ask_quantity) == (amount("1"), amount("3"))


@pytest.mark.parametrize("band", ["0", "1", "-0.01", "1.5"])
def test_a_band_outside_zero_and_one_is_refused(band: str) -> None:
    with pytest.raises(ValueError, match="band"):
        depth_metrics(validated(book()), amount(band), now_ns=NOW, limits=LIMITS)


def test_depth_without_both_sides_is_refused() -> None:
    with pytest.raises(CalculationRefused) as refused:
        depth_metrics(
            validated(book(asks=[])), amount("0.01"), now_ns=NOW, limits=LIMITS
        )
    assert refused.value.cause is RefusalCause.MISSING_INPUT


# The Slippage Engine.


@pytest.mark.req("QNT-006", "QNT-007")
def test_a_buy_walks_the_asks_best_first() -> None:
    data = validated(book())
    result = walk_book(
        data, TakerSide.BUY, amount("2.5"), amount("0.01"), now_ns=NOW, limits=LIMITS
    )
    # 1 at 101 and 1.5 at 102: 254 for 2.5, an average of 101.6.
    assert (result.filled, result.notional) == (amount("2.5"), amount("254"))
    assert result.complete and result.levels == 2
    assert (result.best, result.worst) == (amount("101"), amount("102"))
    assert str(result.average_price) == "101.60"
    # Beyond the best: 254 - 2.5 × 101 = 1.5; beyond the mid: 254 - 2.5 × 100.5 = 2.75.
    assert (result.slippage, result.impact) == (amount("1.5"), amount("2.75"))
    assert result.mid == amount("100.5")


def test_a_sell_walks_the_bids_and_rounds_its_average_down() -> None:
    result = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("3"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    # 1 at 100 and 2 at 99.5: 299 for 3, an average of 99.666..., down to 99.66.
    assert (result.filled, result.notional) == (amount("3"), amount("299.0"))
    assert str(result.average_price) == "99.66"
    # 3 × 100 - 299 = 1; 3 × 100.5 - 299 = 2.5.
    assert (result.slippage, result.impact) == (amount("1.0"), amount("2.5"))


def test_a_buy_rounds_its_average_up() -> None:
    data = validated(book(asks=[("101", "1"), ("102", "2")]))
    result = walk_book(
        data, TakerSide.BUY, amount("3"), amount("0.01"), now_ns=NOW, limits=LIMITS
    )
    # 101 + 204 = 305 for 3: 101.666..., up to 101.67.
    assert str(result.average_price) == "101.67"


def test_an_order_larger_than_the_book_fills_what_the_book_shows() -> None:
    result = walk_book(
        validated(book()),
        TakerSide.BUY,
        amount("10"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (result.filled, result.notional) == (amount("8"), amount("830"))
    assert not result.complete and result.levels == 3
    assert result.worst == amount("105")
    assert str(result.average_price) == "103.75"


def test_an_order_left_with_less_than_one_unit_unfilled_is_incomplete() -> None:
    result = walk_book(
        validated(book()),
        TakerSide.BUY,
        amount("8.5"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert result.filled == amount("8")
    assert not result.complete


def test_a_limit_price_below_one_is_a_limit() -> None:
    result = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("1"),
        amount("0.01"),
        amount("0.5"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert result.filled == amount("1")
    assert result.complete
    # A limit price no higher than the increment is still a limit above zero.
    at_increment = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("1"),
        amount("0.01"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert at_increment.filled == amount("1")
    assert at_increment.limit_price == amount("0.01")


def test_a_limit_price_stops_the_walk() -> None:
    data = validated(book())
    result = walk_book(
        data,
        TakerSide.BUY,
        amount("5"),
        amount("0.01"),
        amount("102"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (result.filled, result.levels, result.complete) == (amount("3"), 2, False)
    assert result.limit_price == amount("102")
    nothing = walk_book(
        data,
        TakerSide.SELL,
        amount("1"),
        amount("0.01"),
        amount("100.5"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (nothing.filled, nothing.levels, nothing.notional) == (
        amount("0"),
        0,
        amount("0"),
    )
    assert nothing.average_price is None and nothing.worst is None
    assert nothing.impact is not None
    for value in (nothing.slippage, nothing.impact):
        assert value == 0 and not value.is_signed()


def test_a_book_without_the_other_side_has_no_mid_and_no_impact() -> None:
    result = walk_book(
        validated(book(bids=[])),
        TakerSide.BUY,
        amount("1"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert result.mid is None and result.impact is None
    assert result.slippage == amount("0")


@pytest.mark.parametrize("side", [TakerSide.BUY, TakerSide.SELL])
def test_walking_an_empty_side_is_refused(side: TakerSide) -> None:
    empty = book(bids=[]) if side is TakerSide.SELL else book(asks=[])
    with pytest.raises(CalculationRefused) as refused:
        walk_book(
            validated(empty),
            side,
            amount("1"),
            amount("0.01"),
            now_ns=NOW,
            limits=LIMITS,
        )
    assert refused.value.cause is RefusalCause.MISSING_INPUT


@pytest.mark.parametrize(
    ("quantity", "limit"), [("0", None), ("-1", None), ("1", "0"), ("1", "-5")]
)
def test_a_quantity_or_limit_not_above_zero_is_refused(
    quantity: str, limit: str | None
) -> None:
    with pytest.raises(ValueError, match="above zero"):
        walk_book(
            validated(book()),
            TakerSide.BUY,
            amount(quantity),
            amount("0.01"),
            None if limit is None else amount(limit),
            now_ns=NOW,
            limits=LIMITS,
        )


PRICES = st.integers(min_value=1, max_value=10**6)
SIZES = st.integers(min_value=1, max_value=10**4)


@st.composite
def books(draw: st.DrawFn) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    best_bid = draw(PRICES)
    bid_steps = draw(st.lists(PRICES, max_size=5))
    ask_steps = draw(st.lists(PRICES, min_size=1, max_size=6))
    bids, price = [], best_bid
    for step in [0, *bid_steps]:
        price -= step
        if price <= 0:
            break
        bids.append((f"{price}.00", f"{draw(SIZES)}.000"))
    asks, price = [], best_bid
    for step in ask_steps:
        price += step
        asks.append((f"{price}.00", f"{draw(SIZES)}.000"))
    return bids, asks


@given(books(), st.sampled_from(TakerSide), SIZES, st.sampled_from(["0.01", "1", "7"]))
@pytest.mark.req("QNT-006", "TEC-003")
def test_a_walked_taker_price_is_never_better_than_the_best(
    sides: tuple[list[tuple[str, str]], list[tuple[str, str]]],
    side: TakerSide,
    quantity: int,
    increment: str,
) -> None:
    bids, asks = sides
    if side is TakerSide.SELL and not bids:
        return
    data = validated(book(bids=bids, asks=asks))
    result = walk_book(
        data, side, amount(quantity), amount(increment), now_ns=NOW, limits=LIMITS
    )
    levels = data.item.asks if side is TakerSide.BUY else data.item.bids
    assert result.average_price is not None
    if side is TakerSide.BUY:
        assert result.average_price >= result.best
    else:
        assert result.average_price <= result.best
    assert result.filled <= amount(quantity)
    assert result.complete == (result.filled == amount(quantity))
    assert result.slippage >= 0
    if result.impact is not None:
        assert result.impact >= result.slippage
    # Exact: the value filled is the sum of each level's price times what was taken there.
    taken, total = amount(quantity), amount(0)
    for level in levels:
        part = min(level.quantity, taken)
        total += part * level.price
        taken -= part
    assert result.notional == total
    # Repeatable: the same walk gives the same result and the same identifier.
    assert (
        walk_book(
            data, side, amount(quantity), amount(increment), now_ns=NOW, limits=LIMITS
        )
        == result
    )


# The Fee Engine.


@pytest.mark.req("QNT-005", "QNT-007")
def test_a_fee_is_the_notional_times_the_schedule_s_rate() -> None:
    settings = venue()
    taker = estimate_fee(settings, market(), LiquidityRole.TAKER, amount("1000"))
    maker = estimate_fee(settings, market(), LiquidityRole.MAKER, amount("1000"))
    assert (str(taker.fee), str(maker.fee)) == ("2.000", "1.000")
    assert (taker.rate, maker.rate) == (amount("0.002"), amount("0.001"))
    assert taker.tier == "base"
    assert taker.schedule == settings.fees[0]
    assert taker.schedule.source == "https://example.test/fees"
    assert taker.schedule.as_of == "2026-11-01"
    assert taker.inputs == ()


def test_a_maker_rebate_is_a_fee_below_zero() -> None:
    result = estimate_fee(
        venue(maker="-0.0001"), market(), LiquidityRole.MAKER, amount("1000")
    )
    assert str(result.fee) == "-0.1000"
    zero = estimate_fee(
        venue(maker="-0.0001"), market(), LiquidityRole.MAKER, amount("0")
    )
    assert str(zero.fee) == "0.0000"


def test_a_fee_names_the_results_its_notional_came_from() -> None:
    walk = walk_book(
        validated(book()),
        TakerSide.BUY,
        amount("1"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    result = estimate_fee(
        venue(), market(), LiquidityRole.TAKER, walk.notional, (walk.evidence_id,)
    )
    assert result.inputs == (walk.evidence_id,)
    listed = estimate_fee(
        venue(), market(), LiquidityRole.TAKER, walk.notional, [walk.evidence_id]
    )
    assert listed.inputs == (walk.evidence_id,)
    with pytest.raises(ValueError, match="evidence identifier"):
        estimate_fee(venue(), market(), LiquidityRole.TAKER, walk.notional, ("x",))


def test_a_fee_without_a_schedule_is_refused_never_zero() -> None:
    with pytest.raises(CalculationRefused) as refused:
        estimate_fee(venue(), market("perpetual"), LiquidityRole.TAKER, amount("1"))
    assert refused.value.cause is RefusalCause.MISSING_INPUT


def test_an_indicator_given_a_validated_item_other_than_a_bar_raises() -> None:
    # The class search of Gate 3's run 5: a ticker, though validated, is not a bar.
    item: object = validated(ticker("99", "101"))
    with pytest.raises(TypeError, match="bars validated by atp.marketdata"):
        sma([item], 1, now_ns=NOW, limits=LIMITS)  # type: ignore[list-item]


def test_a_fee_for_another_venue_s_market_or_a_negative_notional_is_refused() -> None:
    with pytest.raises(ValueError, match="not of the venue"):
        estimate_fee(venue(), market(venue="other"), LiquidityRole.TAKER, amount("1"))
    # A venue named before the settings' venue, as well as one named after it.
    with pytest.raises(ValueError, match="not of the venue"):
        estimate_fee(venue(), market(venue="another"), LiquidityRole.TAKER, amount("1"))
    with pytest.raises(ValueError, match="zero or above"):
        estimate_fee(venue(), market(), LiquidityRole.TAKER, amount("-1"))


@given(
    st.decimals(min_value=0, max_value=10**9, places=4, allow_nan=False),
    st.decimals(min_value=0, max_value=10**9, places=4, allow_nan=False),
    st.sampled_from(LiquidityRole),
)
@pytest.mark.req("QNT-005")
def test_fees_grow_with_notional(
    first: Decimal, second: Decimal, role: LiquidityRole
) -> None:
    low, high = sorted((first, second))
    settings = venue()
    fee_low = estimate_fee(settings, market(), role, amount(low)).fee
    fee_high = estimate_fee(settings, market(), role, amount(high)).fee
    assert fee_low <= fee_high


@pytest.mark.req("QNT-005")
@pytest.mark.parametrize(
    ("rate", "side", "cost"),
    [
        ("0.0001", PositionSide.LONG, "1.0000"),
        ("0.0001", PositionSide.SHORT, "-1.0000"),
        ("-0.0002", PositionSide.LONG, "-2.0000"),
        ("-0.0002", PositionSide.SHORT, "2.0000"),
        ("0", PositionSide.SHORT, "0"),
    ],
)
def test_funding_is_paid_by_the_side_the_rate_names(
    rate: str, side: PositionSide, cost: str
) -> None:
    data = validated(funding(rate))
    result = estimate_funding(data, side, amount("10000"), now_ns=NOW, limits=LIMITS)
    assert str(result.cost) == cost
    assert result.rate == amount(rate)
    assert (result.funding_time_ns, result.interval_seconds) == (
        NOW + 3600 * SECOND,
        28800,
    )
    assert result.inputs == (data.item.evidence_id,)


# Inputs, refusals, and identifiers.


@pytest.mark.req("MKD-012")
def test_market_data_that_was_not_valid_when_validated_is_refused() -> None:
    stale = validated(book(), now=NOW + 5 * SECOND)
    assert not stale.eligible
    calls: list[Callable[[], object]] = [
        lambda: spread_metrics(
            validated(ticker("1", "2"), now=NOW + 5 * SECOND),
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        ),
        lambda: depth_metrics(stale, amount("0.01"), now_ns=NOW, limits=LIMITS),
        lambda: walk_book(
            stale, TakerSide.BUY, amount("1"), amount("0.01"), now_ns=NOW, limits=LIMITS
        ),
        lambda: estimate_funding(
            validated(funding("0.0001"), now=NOW + 5 * SECOND),
            PositionSide.LONG,
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        ),
    ]
    for call in calls:
        with pytest.raises(CalculationRefused) as refused:
            call()
        assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT


@pytest.mark.req("MKD-012")
def test_market_data_no_longer_valid_at_the_time_of_use_is_refused() -> None:
    data = validated(book())
    assert data.eligible
    with pytest.raises(CalculationRefused, match="at the time of use") as refused:
        walk_book(
            data,
            TakerSide.BUY,
            amount("1"),
            amount("0.01"),
            now_ns=NOW + 5 * SECOND,
            limits=LIMITS,
        )
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    # VALID up to its stale limit.
    result = walk_book(
        data,
        TakerSide.BUY,
        amount("1"),
        amount("0.01"),
        now_ns=NOW + SECOND,
        limits=LIMITS,
    )
    assert result.filled == amount("1")


@pytest.mark.req("MKD-012")
def test_a_time_of_use_before_the_validation_is_refused() -> None:
    later = NOW + SECOND  # VALID when validated, and at the validation's own time
    calls: list[Callable[[Validated[BookSnapshot]], object]] = [
        lambda data: depth_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS),
        lambda data: walk_book(
            data, TakerSide.BUY, amount("1"), amount("0.01"), now_ns=NOW, limits=LIMITS
        ),
        lambda data: spread_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS),
    ]
    for call in calls:
        with pytest.raises(
            CalculationRefused, match="before the .* was validated"
        ) as refused:
            call(validated(book(), now=later))
        assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    with pytest.raises(
        CalculationRefused, match="before the .* was validated"
    ) as refused:
        spread_metrics(
            validated(ticker("1", "2"), now=later),
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        )
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    with pytest.raises(
        CalculationRefused, match="before the .* was validated"
    ) as refused:
        estimate_funding(
            validated(funding("0.0001"), now=later),
            PositionSide.LONG,
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        )
    assert refused.value.cause is RefusalCause.INELIGIBLE_INPUT
    data = validated(book(), now=later)
    assert depth_metrics(data, amount("0.01"), now_ns=later, limits=LIMITS).inputs == (
        data.item.evidence_id,
    )


def test_the_time_of_use_and_the_limits_are_checked() -> None:
    data = validated(book())
    with pytest.raises(TypeError, match="whole number of nanoseconds"):
        depth_metrics(data, amount("0.01"), now_ns=float(NOW), limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="whole number of nanoseconds"):
        depth_metrics(data, amount("0.01"), now_ns=True, limits=LIMITS)
    with pytest.raises(TypeError, match="ValidationLimits"):
        depth_metrics(data, amount("0.01"), now_ns=NOW, limits=None)  # type: ignore[arg-type]


def test_market_data_that_was_not_validated_is_refused() -> None:
    with pytest.raises(TypeError, match="Validated"):
        spread_metrics(ticker("1", "2"), amount("1"), now_ns=NOW, limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="Validated"):
        walk_book(
            book(),  # type: ignore[arg-type]
            TakerSide.BUY,
            amount("1"),
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        )
    snapshot_wanted: Validated[BookSnapshot] = validated(ticker("1", "2"))  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        depth_metrics(snapshot_wanted, amount("0.01"), now_ns=NOW, limits=LIMITS)


def test_a_side_a_role_a_venue_or_a_market_of_another_type_is_refused() -> None:
    data = validated(book())
    with pytest.raises(TypeError, match="TakerSide"):
        walk_book(
            data,
            "buy",  # type: ignore[arg-type]
            amount("1"),
            amount("0.01"),
            now_ns=NOW,
            limits=LIMITS,
        )
    with pytest.raises(TypeError, match="PositionSide"):
        estimate_funding(
            validated(funding("0.0001")),
            "long",  # type: ignore[arg-type]
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        )
    with pytest.raises(TypeError, match="LiquidityRole"):
        estimate_fee(venue(), market(), "taker", amount("1"))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="a venue's settings"):
        estimate_fee(None, market(), LiquidityRole.TAKER, amount("1"))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="a venue's settings"):
        estimate_fee(venue(), None, LiquidityRole.TAKER, amount("1"))  # type: ignore[arg-type]


def test_market_data_of_another_kind_is_refused() -> None:
    ticker_wanted: Validated[BookSnapshot] = validated(ticker("1", "2"))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="book snapshot"):
        walk_book(
            ticker_wanted,
            TakerSide.BUY,
            amount("1"),
            amount("0.01"),
            now_ns=NOW,
            limits=LIMITS,
        )
    book_wanted: Validated[FundingRate] = validated(book())  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="funding rate"):
        estimate_funding(
            book_wanted, PositionSide.LONG, amount("1"), now_ns=NOW, limits=LIMITS
        )
    funding_wanted: Validated[Ticker] = validated(funding("0.0001"))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="ticker or a book snapshot"):
        spread_metrics(funding_wanted, amount("0.01"), now_ns=NOW, limits=LIMITS)
    with pytest.raises(TypeError, match="depth is computed from a book snapshot"):
        depth_metrics(ticker_wanted, amount("0.01"), now_ns=NOW, limits=LIMITS)


def test_parameters_that_are_not_finite_amounts_are_refused() -> None:
    data = validated(book())
    with pytest.raises(TypeError, match="increment is an amount"):
        walk_book(data, TakerSide.BUY, amount("1"), 0.01, now_ns=NOW, limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="limit price is an amount"):
        walk_book(
            data,
            TakerSide.BUY,
            amount("1"),
            amount("0.01"),
            200.0,  # type: ignore[arg-type]
            now_ns=NOW,
            limits=LIMITS,
        )
    rate = validated(funding("0.0001"))
    with pytest.raises(TypeError, match="notional is an amount"):
        estimate_funding(rate, PositionSide.LONG, 1.0, now_ns=NOW, limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="zero or above"):
        estimate_funding(
            rate, PositionSide.LONG, amount("-1"), now_ns=NOW, limits=LIMITS
        )
    with pytest.raises(ValueError, match="band is finite"):
        depth_metrics(data, Decimal("NaN"), now_ns=NOW, limits=LIMITS)
    with pytest.raises(ValueError, match="quantity is finite"):
        walk_book(
            data,
            TakerSide.BUY,
            Decimal("Infinity"),
            amount("0.01"),
            now_ns=NOW,
            limits=LIMITS,
        )
    with pytest.raises(ValueError, match="notional is finite"):
        estimate_fee(venue(), market(), LiquidityRole.TAKER, Decimal("Infinity"))
    with pytest.raises(TypeError, match="band is an amount"):
        depth_metrics(data, 0.01, now_ns=NOW, limits=LIMITS)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="increment is an amount"):
        spread_metrics(validated(ticker("1", "2")), 0.01, now_ns=NOW, limits=LIMITS)  # type: ignore[arg-type]


@pytest.mark.req("MKD-005", "MKD-010")
def test_a_result_s_identifier_digests_its_calculation_parameters_and_inputs() -> None:
    data = validated(ticker("100", "101"))
    result = spread_metrics(data, amount("0.0001"), now_ns=NOW, limits=LIMITS)
    form = json.dumps(
        [
            CALCULATION_FORM,
            "atp.quant.spread",
            "1.0",
            [["increment", "0.0001"]],
            [data.item.evidence_id],
        ],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    assert result.evidence_id == hashlib.sha256(form.encode("ascii")).hexdigest()
    assert result.calculation_version == "1.0"
    # The same calculation of the same input gets the same identifier; another increment,
    # another one.
    assert (
        spread_metrics(data, amount("0.0001"), now_ns=NOW, limits=LIMITS).evidence_id
        == result.evidence_id
    )
    assert (
        spread_metrics(data, amount("0.001"), now_ns=NOW, limits=LIMITS).evidence_id
        != result.evidence_id
    )


def settings_with(
    venue_name: str = "example", schedules: list[tuple[str, ...]] | None = None
) -> VenueSettings:
    """A venue's settings with fee schedules: instrument type, maker, taker, source, date."""
    given = schedules or [SCHEDULE]
    return VenueSettings.from_json(
        json.dumps(
            {
                "venue": venue_name,
                "instrument_types": sorted({kind for kind, *_ in given}),
                "fees": [
                    {
                        "instrument_type": kind,
                        "maker": maker,
                        "taker": taker,
                        "source": source,
                        "as_of": as_of,
                    }
                    for kind, maker, taker, source, as_of in given
                ],
            }
        )
    )


SCHEDULE = ("spot", "0.002", "0.002", "https://example.test/fees", "2026-11-01")


@pytest.mark.req("MKD-005", "MKD-010")
def test_a_fee_s_identifier_digests_each_of_its_parameters() -> None:
    # Each estimate differs from the first in one parameter alone; the maker and taker rates
    # are equal, so that the role alone differs between a maker's fee and a taker's.
    eth = MarketRef.from_json(json.dumps(market_json() | {"base": "ETH"}))
    first = estimate_fee(settings_with(), market(), LiquidityRole.TAKER, amount("100"))
    others = {
        "role": estimate_fee(
            settings_with(), market(), LiquidityRole.MAKER, amount("100")
        ),
        "notional": estimate_fee(
            settings_with(), market(), LiquidityRole.TAKER, amount("200")
        ),
        "venue": estimate_fee(
            settings_with("other"),
            market(venue="other"),
            LiquidityRole.TAKER,
            amount("100"),
        ),
        "market": estimate_fee(
            settings_with(), eth, LiquidityRole.TAKER, amount("100")
        ),
        "instrument type": estimate_fee(
            settings_with(schedules=[SCHEDULE, ("margin", *SCHEDULE[1:])]),
            market("margin"),
            LiquidityRole.TAKER,
            amount("100"),
        ),
        "rate": estimate_fee(
            settings_with(schedules=[("spot", "0.003", "0.003", *SCHEDULE[3:])]),
            market(),
            LiquidityRole.TAKER,
            amount("100"),
        ),
        "source": estimate_fee(
            settings_with(
                schedules=[(*SCHEDULE[:3], "https://example.test/x", "2026-11-01")]
            ),
            market(),
            LiquidityRole.TAKER,
            amount("100"),
        ),
        "date": estimate_fee(
            settings_with(schedules=[(*SCHEDULE[:4], "2026-11-02")]),
            market(),
            LiquidityRole.TAKER,
            amount("100"),
        ),
    }
    again = estimate_fee(settings_with(), market(), LiquidityRole.TAKER, amount("100"))
    assert again.evidence_id == first.evidence_id
    for name, other in others.items():
        assert other.evidence_id != first.evidence_id, name


@pytest.mark.req("MKD-005", "MKD-010")
def test_the_walk_funding_and_depth_identifiers_digest_their_parameters() -> None:
    data = validated(book())

    def walk(side: TakerSide, quantity: str, increment: str, limit: str | None) -> str:
        price = None if limit is None else amount(limit)
        return walk_book(
            data,
            side,
            amount(quantity),
            amount(increment),
            price,
            now_ns=NOW,
            limits=LIMITS,
        ).evidence_id

    first = walk(TakerSide.BUY, "1", "0.01", None)
    assert walk(TakerSide.BUY, "1", "0.01", None) == first
    for other in (
        walk(TakerSide.SELL, "1", "0.01", None),
        walk(TakerSide.BUY, "2", "0.01", None),
        walk(TakerSide.BUY, "1", "0.001", None),
        walk(TakerSide.BUY, "1", "0.01", "200"),
    ):
        assert other != first
    assert walk(TakerSide.BUY, "1", "0.01", "300") != walk(
        TakerSide.BUY, "1", "0.01", "200"
    )
    rate = validated(funding("0.0001"))

    def fund(side: PositionSide, notional: str) -> str:
        return estimate_funding(
            rate, side, amount(notional), now_ns=NOW, limits=LIMITS
        ).evidence_id

    assert fund(PositionSide.SHORT, "100") != fund(PositionSide.LONG, "100")
    assert fund(PositionSide.LONG, "200") != fund(PositionSide.LONG, "100")
    assert (
        depth_metrics(data, amount("0.02"), now_ns=NOW, limits=LIMITS).evidence_id
        != depth_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS).evidence_id
    )


def test_a_parameter_s_text_is_digested_in_ascii() -> None:
    form = json.dumps(
        [CALCULATION_FORM, "c", "1.0", [["name", "\u00e9"]], []],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    assert calculation_id("c", "1.0", [("name", "\u00e9")], []) == (
        hashlib.sha256(form.encode("ascii")).hexdigest()
    )


def test_a_refusal_states_its_cause_and_detail() -> None:
    refused = CalculationRefused(RefusalCause.GAP, "two bars apart")
    assert refused.cause is RefusalCause.GAP
    assert str(refused) == "gap: two bars apart"


def test_an_identifier_s_inputs_are_evidence_identifiers() -> None:
    with pytest.raises(ValueError, match="evidence identifier"):
        calculation_id("atp.quant.spread", "1.0", [], ["not-an-identifier"])
    with pytest.raises(ValueError, match="evidence identifier"):
        calculation_id("atp.quant.spread", "1.0", [], ["a" * 64 + "\n"])
    first, second = "a" * 64, "b" * 64
    assert calculation_id("a", "1.0", [], [first, second]) != calculation_id(
        "a", "1.0", [], [second, first]
    )
    assert calculation_id("a", "1.0", [], []) != calculation_id("b", "1.0", [], [])


@pytest.mark.req("QNT-004")
def test_no_result_combines_costs_into_a_net_figure() -> None:
    # Primitive metrics only: combining fees, slippage, and funding into a net result is the
    # True Net-Profit Engine's (TNP-017), so no result holds a net, total, or profit figure.
    import atp.quant

    results = [
        value
        for value in vars(atp.quant).values()
        if isinstance(value, type)
        and value.__module__ == "atp.quant._contracts"
        and issubclass(value, Contract)
    ]
    assert len(results) == 7
    for result in results:
        for name in result.model_fields:
            words = set(name.split("_"))
            assert not words & {"net", "total", "profit", "pnl"}, (
                result.__name__,
                name,
            )


@pytest.mark.req("ARCH-025", "MKD-005")
def test_each_result_survives_its_written_form() -> None:
    walked = walk_book(
        validated(book()),
        TakerSide.BUY,
        amount("2.5"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    results = [
        spread_metrics(
            validated(ticker("100", "101")), amount("0.0001"), now_ns=NOW, limits=LIMITS
        ),
        depth_metrics(validated(book()), amount("0.01"), now_ns=NOW, limits=LIMITS),
        walked,
        estimate_fee(venue(), market(), LiquidityRole.TAKER, walked.notional),
        estimate_funding(
            validated(funding("0.0001")),
            PositionSide.LONG,
            amount("1"),
            now_ns=NOW,
            limits=LIMITS,
        ),
    ]
    kinds = (
        SpreadMetrics,
        DepthMetrics,
        SlippageEstimate,
        FeeEstimate,
        FundingEstimate,
    )
    assert [type(result) for result in results] == list(kinds)
    for result in results:
        assert type(result).from_json(result.to_json()) == result


# Gate 3's run 3: arguments checked whatever the data (F-17), and a zero's sign (F-15).


@pytest.mark.parametrize("increment", ["0", "-1"])
def test_an_increment_not_above_zero_is_refused_whatever_the_data(
    increment: str,
) -> None:
    # A sell limited above the best bid fills nothing, and a ticker without a bid has no spread:
    # neither reaches the division that refuses such an increment.
    with pytest.raises(ValueError, match="increment is above zero"):
        walk_book(
            validated(book()),
            TakerSide.SELL,
            amount("1"),
            amount(increment),
            amount("100.5"),
            now_ns=NOW,
            limits=LIMITS,
        )
    with pytest.raises(ValueError, match="increment is above zero"):
        spread_metrics(
            validated(ticker(None, "101")),
            amount(increment),
            now_ns=NOW,
            limits=LIMITS,
        )


@pytest.mark.parametrize(
    ("rate", "side"),
    [("-0.0002", PositionSide.LONG), ("0.0002", PositionSide.SHORT)],
)
def test_a_zero_funding_cost_has_no_sign(rate: str, side: PositionSide) -> None:
    result = estimate_funding(
        validated(funding(rate)), side, amount("0"), now_ns=NOW, limits=LIMITS
    )
    assert result.cost == 0 and not result.cost.is_signed()


# The class search of Gate 3's run 3 (F-15): calls removed or replaced, and what else survived.


class _Forged(Validated[BookSnapshot]):  # type: ignore[misc]
    """Data passed off as validated: a subclass that skips the validator's check."""

    def __post_init__(self, creator: object) -> None:
        pass


class _Limits(ValidationLimits):
    contract_id = "test.limits"
    contract_version = ValidationLimits.contract_version


class _Venue(VenueSettings):
    contract_id = "test.venue"
    contract_version = VenueSettings.contract_version


class _Market(MarketRef):
    contract_id = "test.market"
    contract_version = MarketRef.contract_version


class _Amount(Decimal):
    """A `Decimal` that `atp.numeric.amount` did not build."""


class _Text(str):
    """Text in the shape of an evidence identifier, of another type."""

    __slots__ = ()


def test_data_settings_amounts_and_names_of_a_subclass_are_refused() -> None:
    # Each is checked as its exact type: a subclass could skip the validator's check, or change
    # what a value means.
    data = validated(book())
    forged = _Forged(data.item, data.assessment, creator=None)
    with pytest.raises(TypeError, match="only as atp.marketdata's Validated"):
        depth_metrics(forged, amount("0.01"), now_ns=NOW, limits=LIMITS)
    limits = _Limits.from_json(LIMITS.model_dump_json())
    with pytest.raises(TypeError, match="ValidationLimits"):
        depth_metrics(data, amount("0.01"), now_ns=NOW, limits=limits)
    with pytest.raises(TypeError, match="built with atp.numeric.amount"):
        depth_metrics(data, _Amount("0.01"), now_ns=NOW, limits=LIMITS)
    settings = _Venue.from_json(venue().model_dump_json())
    other = _Market.from_json(market().model_dump_json())
    for given_venue, given_market in ((settings, market()), (venue(), other)):
        with pytest.raises(TypeError, match="venue's settings and one of its markets"):
            estimate_fee(given_venue, given_market, LiquidityRole.TAKER, amount("1"))
    with pytest.raises(ValueError, match="evidence identifier"):
        calculation_id("atp.quant.spread", "1.0", [], [_Text("a" * 64)])
    with pytest.raises(TypeError, match="built with atp.numeric.amount"):
        divide(_Amount("1"), amount("3"), amount("0.01"), Rounding.TOWARD_ZERO)


def _digest(calculation: str, parameters: list[list[str]], inputs: list[str]) -> str:
    form = json.dumps(
        [CALCULATION_FORM, calculation, "1.0", parameters, inputs],
        ensure_ascii=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(form.encode("ascii")).hexdigest()


def test_each_result_s_identifier_has_the_form_the_specification_gives() -> None:
    # The calculation's name and version, each parameter as its name and its text, and the
    # inputs, in that order (`atp.calculation/1`; the spread's is checked above).
    data = validated(book())
    source = [data.item.evidence_id]
    depth = depth_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS)
    assert depth.evidence_id == _digest("atp.quant.depth", [["band", "0.01"]], source)
    walk = walk_book(
        data,
        TakerSide.BUY,
        amount("2"),
        amount("0.01"),
        amount("102"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert walk.evidence_id == _digest(
        "atp.quant.slippage",
        [
            ["side", "buy"],
            ["quantity", "2"],
            ["increment", "0.01"],
            ["limit_price", "102"],
        ],
        source,
    )
    fee = estimate_fee(
        venue(), market(), LiquidityRole.TAKER, amount("1500"), (walk.evidence_id,)
    )
    assert fee.evidence_id == _digest(
        "atp.quant.fee",
        [
            ["venue", "example"],
            ["market", "BTC/USDT"],
            ["instrument_type", "spot"],
            ["role", "taker"],
            ["tier", "base"],
            ["rate", "0.002"],
            ["source", "https://example.test/fees"],
            ["as_of", "2026-11-01"],
            ["notional", "1500"],
        ],
        [walk.evidence_id],
    )
    rate = validated(funding("0.0001"))
    paid = estimate_funding(
        rate, PositionSide.LONG, amount("1000"), now_ns=NOW, limits=LIMITS
    )
    assert paid.evidence_id == _digest(
        "atp.quant.funding",
        [["side", "long"], ["notional", "1000"]],
        [rate.item.evidence_id],
    )


def test_a_sell_takes_a_level_at_its_limit() -> None:
    # A level worse than the limit stops the walk; a level at it does not.
    result = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("2"),
        amount("0.01"),
        amount("99.5"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (result.filled, result.levels) == (amount("2"), 2)


def test_a_side_without_a_level_inside_the_band_shows_no_depth() -> None:
    # The mid is 50.5, so neither best level lies within 1% of it.
    wide = validated(book(bids=[("1", "1")], asks=[("100", "1")]))
    result = depth_metrics(wide, amount("0.01"), now_ns=NOW, limits=LIMITS)
    assert (
        result.bid_quantity,
        result.bid_notional,
        result.ask_quantity,
        result.ask_notional,
    ) == (amount("0"),) * 4
    assert result.bid_complete and result.ask_complete


# Gate 3's run 4: each side's completeness, the schedule of the market's type (F-22), the
# arguments a result repeats (F-23), and every input of an identifier (F-24).


def test_each_side_s_completeness_is_counted_on_that_side() -> None:
    # Every level inside the band: neither side is complete, whatever the other side's count.
    for bids, asks in (
        ([("100", "1"), ("99.9", "1"), ("99.8", "1")], [("101", "1"), ("101.1", "1")]),
        ([("100", "1"), ("99.9", "1")], [("101", "1"), ("101.1", "1"), ("101.2", "1")]),
    ):
        data = validated(book(bids=bids, asks=asks))
        result = depth_metrics(data, amount("0.05"), now_ns=NOW, limits=LIMITS)
        assert (result.bid_complete, result.ask_complete) == (False, False)


def test_a_fee_takes_the_schedule_of_its_market_s_type() -> None:
    settings = VenueSettings.from_json(
        json.dumps(
            {
                "venue": "example",
                "instrument_types": ["spot", "perpetual"],
                "fees": [
                    {
                        "instrument_type": "spot",
                        "maker": "0.001",
                        "taker": "0.002",
                        "source": "https://example.test/fees",
                        "as_of": "2026-11-01",
                    },
                    {
                        "instrument_type": "perpetual",
                        "maker": "0.0002",
                        "taker": "0.0005",
                        "source": "https://example.test/perpetual-fees",
                        "as_of": "2026-10-15",
                    },
                ],
            }
        )
    )
    result = estimate_fee(
        settings, market("perpetual"), LiquidityRole.TAKER, amount("1000")
    )
    assert result.schedule == settings.fees[1]
    assert (result.rate, str(result.fee)) == (amount("0.0005"), "0.5000")


def test_each_result_repeats_the_arguments_it_was_given() -> None:
    # Each argument given a value that no other field of its result holds.
    walk = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("10"),
        amount("0.5"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (walk.side, walk.quantity, walk.increment) == (
        TakerSide.SELL,
        amount("10"),
        amount("0.5"),
    )
    assert walk.filled == amount("8")
    cost = estimate_funding(
        validated(funding("0.0001")),
        PositionSide.SHORT,
        amount("5000"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (cost.side, cost.notional) == (PositionSide.SHORT, amount("5000"))
    fee = estimate_fee(venue(), market(), LiquidityRole.MAKER, amount("1000"))
    assert (fee.role, fee.notional) == (LiquidityRole.MAKER, amount("1000"))
    spread = spread_metrics(
        validated(ticker("100", "101")), amount("0.0001"), now_ns=NOW, limits=LIMITS
    )
    assert spread.increment == amount("0.0001")


def test_every_input_of_an_identifier_is_checked() -> None:
    with pytest.raises(ValueError, match="evidence identifier"):
        calculation_id("atp.quant.spread", "1.0", [], ["a" * 64, "not-an-identifier"])


# The class search of Gate 3's run 4 (F-22): a book missing a side, and the walk's quantity and
# limit price.


@pytest.mark.parametrize("side", ["bids", "asks"])
def test_a_book_without_one_side_has_no_spread_and_no_depth(side: str) -> None:
    data = validated(book(bids=[]) if side == "bids" else book(asks=[]))
    with pytest.raises(CalculationRefused) as refused:
        spread_metrics(data, amount("0.0001"), now_ns=NOW, limits=LIMITS)
    assert refused.value.cause is RefusalCause.MISSING_INPUT
    with pytest.raises(CalculationRefused) as refused:
        depth_metrics(data, amount("0.01"), now_ns=NOW, limits=LIMITS)
    assert refused.value.cause is RefusalCause.MISSING_INPUT


def test_a_sell_on_a_book_without_asks_has_no_mid_and_no_impact() -> None:
    result = walk_book(
        validated(book(asks=[])),
        TakerSide.SELL,
        amount("1"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert result.mid is None and result.impact is None


def test_a_walk_s_identifier_digests_the_quantity_asked() -> None:
    # Both orders, on one book, exceed its bids' 8 and fill 8 at 3 levels: only the quantity
    # asked differs.
    data = validated(book())
    first, second = (
        walk_book(
            data,
            TakerSide.SELL,
            amount(quantity),
            amount("0.01"),
            now_ns=NOW,
            limits=LIMITS,
        )
        for quantity in ("10", "20")
    )
    assert (first.filled, first.levels) == (second.filled, second.levels)
    assert first.evidence_id != second.evidence_id


def test_a_walk_repeats_its_limit_price() -> None:
    limited = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("10"),
        amount("0.01"),
        amount("99"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert (limited.limit_price, limited.worst) == (amount("99"), amount("99.5"))
    free = walk_book(
        validated(book()),
        TakerSide.SELL,
        amount("10"),
        amount("0.01"),
        now_ns=NOW,
        limits=LIMITS,
    )
    assert free.limit_price is None
