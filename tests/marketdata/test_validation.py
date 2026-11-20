"""Validation before use, freshness, quality, and quarantine (the Stage 2 plan's U5)."""

from __future__ import annotations

import itertools
import json
from collections.abc import Callable
from decimal import Decimal
from random import Random

import pytest
from hypothesis import given
from hypothesis import strategies as st

from atp.health import ClockLimits, ClockMonitor, ClockSample
from atp.marketdata import (
    QUALITY_RULE_VERSION,
    VALIDATION_RULE_VERSION,
    BookSnapshot,
    BookUpdate,
    Freshness,
    FundingRate,
    MarketDataValidator,
    MarketItem,
    MarketMetadata,
    MarketRef,
    OhlcvBar,
    QuarantineCause,
    QuarantineRecord,
    Stream,
    StreamFreshness,
    StreamLimits,
    Ticker,
    Trade,
    Validated,
    ValidationLimits,
    VenueState,
    assess,
    deduplicate,
    evidence_id,
    freshness,
    in_order,
    quality_score,
)

SECOND = 1_000_000_000
NOW = 1_763_600_000 * SECOND
STALE = SECOND
INVALID = 10 * SECOND
AHEAD = 100_000_000
LIMITS = ValidationLimits(
    streams=tuple(
        StreamLimits(stream=stream, stale_after_ns=STALE, invalid_after_ns=INVALID)
        for stream in Stream
    ),
    max_event_ahead_ns=AHEAD,
    duplicate_memory=4,
    outlier_limit=Decimal("0.10"),
    outlier_confirmations=2,
    inconsistency_limit=Decimal("0.05"),
    minimum_other_venues=2,
)
LINEAGE = {
    "source": "wss://example/ws",
    "adapter": "atp.exchange.example",
    "adapter_version": "1.0",
}
_keys = itertools.count()

Fields = dict[str, object]


def market_json(venue: str = "example", kind: str = "spot") -> Fields:
    fields: Fields = {
        "venue": venue,
        "base": "BTC",
        "quote": "USDT",
        "instrument_type": kind,
    }
    if kind == "perpetual":
        fields["settle"] = "USDT"
    return fields


def market(venue: str = "example", kind: str = "spot") -> MarketRef:
    return MarketRef.from_json(json.dumps(market_json(venue, kind)))


SPOT = market()


def stamp(event: int | None = NOW, receive: int = NOW) -> Fields:
    fields: Fields = {"receive_time_ns": receive}
    if event is not None:
        fields |= {"event_time_ns": event, "event_time_resolution": "nanosecond"}
    return fields


def common(
    stream: Stream, at: Fields | None, event: int | None, receive: int
) -> Fields:
    ref = None if at is None else MarketRef.from_json(json.dumps(at))
    venue = ref.venue if ref is not None else "example"
    key = evidence_id(
        venue=venue, stream=stream, market=ref, venue_key=str(next(_keys))
    )
    fields: Fields = {"evidence_id": key, "lineage": LINEAGE, **stamp(event, receive)}
    if at is not None:
        fields["market"] = at
    return fields


def trade(
    price: str = "100",
    quantity: str = "1",
    venue: str = "example",
    event: int | None = NOW,
    receive: int = NOW,
    kind: str = "spot",
) -> Trade:
    fields = common(Stream.TRADES, market_json(venue, kind), event, receive)
    return Trade.from_json(json.dumps({**fields, "price": price, "quantity": quantity}))


def ticker(
    bid: str | None, ask: str | None, last: str | None, bid_size: str | None = None
) -> Ticker:
    fields = common(Stream.TICKER, market_json(), NOW, NOW)
    prices = {"bid": bid, "ask": ask, "last": last, "bid_size": bid_size}
    fields |= {name: value for name, value in prices.items() if value is not None}
    if bid is not None and bid_size is None:
        fields["bid_size"] = "1"
    if ask is not None:
        fields["ask_size"] = "1"
    return Ticker.from_json(json.dumps(fields))


def levels(*pairs: tuple[str, str]) -> list[list[str]]:
    return [[price, quantity] for price, quantity in pairs]


def _levels(pairs: list[list[str]]) -> list[Fields]:
    return [{"price": price, "quantity": quantity} for price, quantity in pairs]


def snapshot(
    bids: list[list[str]] | None = None,
    asks: list[list[str]] | None = None,
    sequence: int | None = 10,
) -> BookSnapshot:
    fields = common(Stream.BOOK, market_json(), NOW, NOW)
    fields["bids"] = _levels(
        levels(("100", "1"), ("99", "1")) if bids is None else bids
    )
    fields["asks"] = _levels(
        levels(("101", "1"), ("102", "1")) if asks is None else asks
    )
    if sequence is not None:
        fields["sequence"] = sequence
    return BookSnapshot.from_json(json.dumps(fields))


def update(
    first: int | None = None,
    last: int | None = None,
    previous: int | None = None,
    bids: list[list[str]] | None = None,
) -> BookUpdate:
    fields = common(Stream.BOOK, market_json(), NOW, NOW)
    fields |= {
        "bids": _levels(levels(("100", "2")) if bids is None else bids),
        "asks": [],
    }
    sequences = {
        "first_sequence": first,
        "last_sequence": last,
        "previous_sequence": previous,
    }
    fields |= {name: value for name, value in sequences.items() if value is not None}
    return BookUpdate.from_json(json.dumps(fields))


def bar(
    o: str,
    h: str,
    low: str,
    c: str,
    volume: str = "5",
    open_time: int = NOW - 60 * SECOND,
    closed: bool = True,
    event: int | None = NOW,
    quote_volume: str | None = None,
) -> OhlcvBar:
    fields = common(Stream.OHLCV, market_json(), event, NOW)
    fields |= {
        "open": o,
        "high": h,
        "low": low,
        "close": c,
        "base_volume": volume,
        "open_time_ns": open_time,
        "interval_seconds": 60,
        "closed": closed,
    }
    if quote_volume is not None:
        fields["quote_volume"] = quote_volume
    return OhlcvBar.from_json(json.dumps(fields))


def metadata(status: str = "trading", **amounts: str | None) -> MarketMetadata:
    fields = common(Stream.MARKETS, market_json(), NOW, NOW)
    values = {"price_increment": "0.01", "quantity_increment": "0.0001", **amounts}
    fields |= {name: value for name, value in values.items() if value is not None}
    fields |= {"venue_symbol": "BTCUSDT", "status": status}
    return MarketMetadata.from_json(json.dumps(fields))


def funding(rate: str) -> FundingRate:
    fields = common(Stream.FUNDING, market_json(kind="perpetual"), NOW, NOW)
    return FundingRate.from_json(json.dumps({**fields, "rate": rate}))


def venue_state() -> VenueState:
    fields = common(Stream.VENUE_STATUS, None, NOW, NOW)
    return VenueState.from_json(
        json.dumps({**fields, "venue": "example", "status": "available"})
    )


def check(
    item: MarketItem,
    validator: MarketDataValidator | None = None,
    drifting: frozenset[str] = frozenset(),
) -> QuarantineCause | None:
    result = (validator or MarketDataValidator(LIMITS)).validate(
        item, now_ns=NOW, drifting_venues=drifting
    )
    return result.cause if isinstance(result, QuarantineRecord) else None


def validated(item: MarketItem) -> Validated[MarketItem]:
    result = MarketDataValidator(LIMITS).validate(
        item, now_ns=NOW, drifting_venues=frozenset()
    )
    assert isinstance(result, Validated)
    return result


# Each quarantine cause (MKD-013; SR-13).


@pytest.mark.req("MKD-009", "MKD-013", "HLT-013")
def test_a_drifting_venue_s_data_is_quarantined_for_its_clock() -> None:
    assert (
        check(trade(), drifting=frozenset({"example"})) is QuarantineCause.CLOCK_PROBLEM
    )
    assert check(trade(), drifting=frozenset({"other"})) is None


@pytest.mark.req("MKD-004", "MKD-013")
@pytest.mark.parametrize(
    ("make", "cause"),
    [
        (lambda: trade(event=NOW + AHEAD + 1), QuarantineCause.INVALID_TIMESTAMP),
        (lambda: trade(event=NOW + AHEAD), None),
        # Received after the time it is checked at: its age cannot be known.
        (lambda: trade(event=None, receive=NOW + 1), QuarantineCause.INVALID_TIMESTAMP),
        (
            lambda: bar("1", "1", "1", "1", open_time=NOW + AHEAD + 1, closed=False),
            QuarantineCause.INVALID_TIMESTAMP,
        ),
        (lambda: bar("1", "1", "1", "1", open_time=NOW + AHEAD, closed=False), None),
        (
            lambda: bar("1", "1", "1", "1", open_time=NOW - 30 * SECOND),
            QuarantineCause.INVALID_TIMESTAMP,
        ),
        (lambda: bar("1", "1", "1", "1", open_time=NOW + AHEAD - 60 * SECOND), None),
        (
            lambda: bar("1", "1", "1", "1", open_time=NOW - 30 * SECOND, closed=False),
            None,
        ),
    ],
)
def test_an_invalid_timestamp_is_quarantined(
    make: Callable[[], MarketItem], cause: QuarantineCause | None
) -> None:
    assert check(make()) is cause


@pytest.mark.req("MKD-013")
def test_an_item_missing_what_its_use_needs_is_quarantined() -> None:
    assert check(ticker(None, None, None)) is QuarantineCause.MISSING_FIELD
    assert check(ticker(None, None, "100")) is None
    assert check(metadata(price_increment=None)) is QuarantineCause.MISSING_FIELD
    assert check(metadata(quantity_increment=None)) is QuarantineCause.MISSING_FIELD
    assert check(metadata("halted", price_increment=None)) is None


@pytest.mark.req("MKD-008", "MKD-013")
@pytest.mark.parametrize(
    "make",
    [
        lambda: trade(price="0"),
        lambda: trade(price="-1"),
        lambda: trade(quantity="0"),
        lambda: ticker("101", "100", None),
        lambda: ticker("100", "100", None),
        lambda: ticker(None, None, "0"),
        lambda: ticker("100", "101", None, bid_size="-1"),
        lambda: snapshot(bids=levels(("101", "1")), asks=levels(("101", "1"))),
        lambda: snapshot(bids=levels(("99", "1"), ("100", "1"))),
        lambda: snapshot(asks=levels(("102", "1"), ("101", "1"))),
        lambda: snapshot(bids=levels(("100", "1"), ("100", "1"))),
        lambda: snapshot(asks=levels(("101", "1"), ("101", "1"))),
        lambda: snapshot(bids=levels(("100", "0"))),
        lambda: snapshot(asks=levels(("0", "1"))),
        lambda: update(bids=levels(("100", "-1"))),
        lambda: update(bids=levels(("0", "1"))),
        lambda: bar("100", "99.5", "98", "99"),
        lambda: bar("100", "101", "99", "102"),
        lambda: bar("100", "101", "100.5", "101"),
        lambda: bar("101", "102", "100.5", "100"),
        lambda: bar("100", "101", "99", "100", volume="-1"),
        lambda: bar("100", "101", "99", "100", quote_volume="-1"),
        lambda: bar("0", "0", "0", "0"),
        lambda: metadata(price_increment="0"),
        lambda: metadata(quantity_increment="0"),
        lambda: metadata(minimum_quantity="-1"),
        lambda: metadata(minimum_notional="-1"),
        lambda: metadata(contract_size="0"),
    ],
)
def test_an_impossible_value_is_quarantined(make: Callable[[], MarketItem]) -> None:
    assert check(make()) is QuarantineCause.IMPOSSIBLE_PRICE


@pytest.mark.req("MKD-008")
@pytest.mark.parametrize(
    "make",
    [
        lambda: update(bids=levels(("100", "0"))),
        lambda: update(bids=levels(("99", "1"), ("100", "1"))),
        lambda: snapshot(bids=[], asks=[]),
        lambda: bar("100", "101", "99", "100", volume="0"),
        lambda: metadata(minimum_quantity="0", minimum_notional="0"),
        lambda: funding("-0.0001"),
    ],
)
def test_a_possible_value_is_not_quarantined(make: Callable[[], MarketItem]) -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(snapshot(sequence=None), validator) is None
    assert check(make(), validator) is None


@pytest.mark.req("MKD-003", "MKD-013")
def test_the_checks_run_in_their_order_and_the_first_failed_names_the_cause() -> None:
    impossible_and_late = trade(price="0", event=NOW + AHEAD + 1)
    assert check(impossible_and_late, drifting=frozenset({"example"})) is (
        QuarantineCause.CLOCK_PROBLEM
    )
    assert check(impossible_and_late) is QuarantineCause.INVALID_TIMESTAMP
    assert check(metadata(price_increment=None, quantity_increment="0")) is (
        QuarantineCause.MISSING_FIELD
    )
    validator = MarketDataValidator(LIMITS)
    seen = trade("100")
    assert check(seen, validator) is None
    assert check(trade("150"), validator) is QuarantineCause.OUTLIER
    # Seen before, and an outlier no longer: the duplicate is named first.
    assert check(seen, validator) is QuarantineCause.DUPLICATE_EVENT


@pytest.mark.req("MKD-004", "MKD-013")
def test_a_duplicate_is_quarantined_and_memory_is_bounded() -> None:
    validator = MarketDataValidator(LIMITS)
    first = trade()
    assert check(first, validator) is None
    assert check(first, validator) is QuarantineCause.DUPLICATE_EVENT
    for _ in range(LIMITS.duplicate_memory - 1):
        assert check(trade(), validator) is None
    # The memory is full, and still holds the first identifier.
    assert check(first, validator) is QuarantineCause.DUPLICATE_EVENT
    assert check(trade(), validator) is None
    # The oldest identifier was forgotten: the item is no longer known as a duplicate.
    assert check(first, validator) is None


@pytest.mark.req("MKD-004", "MKD-013")
def test_book_sequences_follow_their_snapshot_and_a_gap_waits_for_a_fresh_one() -> None:
    validator = MarketDataValidator(LIMITS)
    assert validator.needs_snapshot(SPOT)
    assert check(update(first=11, last=11), validator) is QuarantineCause.SEQUENCE_GAP
    assert check(snapshot(sequence=10), validator) is None
    assert not validator.needs_snapshot(SPOT)
    assert check(update(first=8, last=10), validator) is QuarantineCause.DUPLICATE_EVENT
    assert check(update(first=9, last=12), validator) is None
    assert check(update(previous=12, last=13), validator) is None
    assert (
        check(update(previous=12, last=13), validator)
        is QuarantineCause.DUPLICATE_EVENT
    )
    assert (
        check(update(previous=13, last=13), validator) is None
    )  # no change, as some venues send
    assert check(update(first=15, last=16), validator) is QuarantineCause.SEQUENCE_GAP
    assert validator.needs_snapshot(SPOT)
    # Broken: even a continuous update waits for the fresh snapshot, whatever its number.
    assert check(update(first=14, last=14), validator) is QuarantineCause.SEQUENCE_GAP
    assert check(update(first=0, last=0), validator) is QuarantineCause.SEQUENCE_GAP
    assert check(snapshot(sequence=20), validator) is None
    assert (
        check(update(previous=19, last=21), validator) is QuarantineCause.SEQUENCE_GAP
    )
    assert check(snapshot(sequence=30), validator) is None
    assert check(update(first=31), validator) is None
    assert check(update(first=32, last=32), validator) is None
    # An update without a number of its own cannot be placed in a numbered book.
    assert check(update(), validator) is QuarantineCause.SEQUENCE_GAP
    assert validator.needs_snapshot(SPOT)


@pytest.mark.req("MKD-004")
def test_updates_after_a_snapshot_without_a_sequence_are_not_checked() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(snapshot(sequence=None), validator) is None
    assert check(update(first=500, last=501), validator) is None
    assert check(update(), validator) is None
    assert not validator.needs_snapshot(SPOT)


@pytest.mark.req("MKD-004")
def test_an_update_behind_its_own_previous_number_is_not_applied() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(snapshot(), validator) is None
    # Its previous number is the book's, but its own numbers are already held.
    held = update(5, 8, previous=10)
    assert check(held, validator) is QuarantineCause.DUPLICATE_EVENT
    # The book stays at 10: a keep-alive naming it as its previous number is applied.
    assert check(update(10, 10, previous=10), validator) is None
    assert check(update(11, 11, previous=10), validator) is None
    assert not validator.needs_snapshot(SPOT)


@pytest.mark.req("MKD-008", "MKD-013")
def test_an_outlier_is_quarantined_until_the_move_is_confirmed() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("100"), validator) is None
    assert check(trade("110"), validator) is None  # exactly the limit: not beyond it
    assert check(trade("121.1"), validator) is QuarantineCause.OUTLIER
    assert (
        check(trade("150"), validator) is QuarantineCause.OUTLIER
    )  # not near 121.1: restarts
    assert check(trade("151"), validator) is QuarantineCause.OUTLIER
    # Two outliers in a row agree: the next that agrees is accepted and is the reference.
    assert check(trade("152"), validator) is None
    assert check(trade("160"), validator) is None


@pytest.mark.req("MKD-008", "MKD-013")
def test_an_outlier_beyond_the_run_s_last_starts_a_new_run() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("50"), validator) is None
    assert check(trade("100"), validator) is QuarantineCause.OUTLIER
    assert (
        check(trade("115"), validator) is QuarantineCause.OUTLIER
    )  # beyond 100: a new run
    # Within both earlier outliers, but the new run holds one: not yet confirmed.
    assert check(trade("107"), validator) is QuarantineCause.OUTLIER
    assert check(trade("108"), validator) is None


@pytest.mark.req("MKD-008", "MKD-013")
def test_an_earlier_price_never_replaces_a_later_reference() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("100"), validator) is None
    assert check(trade("105", event=NOW - 1), validator) is None
    # Compared with 100, the reference, not with 105, which describes an earlier time.
    assert check(trade("115"), validator) is QuarantineCause.OUTLIER


@pytest.mark.req("MKD-008", "MKD-013")
def test_a_price_that_is_not_an_outlier_ends_the_run() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("100"), validator) is None
    assert check(trade("150"), validator) is QuarantineCause.OUTLIER
    assert check(trade("150"), validator) is QuarantineCause.OUTLIER
    # Within the limit, though of an earlier time and so not the reference: the run ends.
    assert check(trade("101", event=NOW - 1), validator) is None
    assert check(trade("150"), validator) is QuarantineCause.OUTLIER


@pytest.mark.req("MKD-008")
def test_an_outlier_run_keeps_only_what_a_confirmation_needs() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("100"), validator) is None
    for price in ("150", "160", "170", "180", "190"):
        assert check(trade(price), validator) is QuarantineCause.OUTLIER
    run = validator._references[(SPOT, Stream.TRADES)].outliers  # noqa: SLF001
    assert list(run) == [Decimal(180), Decimal(190)]


@pytest.mark.req("MKD-008", "MKD-013")
def test_a_price_unlike_every_other_venue_s_is_inconsistent() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(trade("100", venue="one"), validator) is None
    assert check(trade("100", venue="two"), validator) is None
    assert (
        check(trade("106", venue="three"), validator)
        is QuarantineCause.EXCHANGE_INCONSISTENCY
    )
    assert check(trade("105", venue="three"), validator) is None  # exactly the limit
    # A price no longer valid itself is not compared: it is not eligible for use anyway.
    assert check(trade("200", venue="four", event=NOW - STALE - 1), validator) is None
    # One other venue is not enough to compare against, and a venue is not compared with itself.
    lone = MarketDataValidator(LIMITS)
    assert check(trade("100", venue="one"), lone) is None
    assert check(trade("200", venue="two"), lone) is None
    assert check(trade("106", venue="one"), lone) is None
    # Within the limit of one other venue's price: consistent.
    near = MarketDataValidator(LIMITS)
    assert check(trade("100", venue="one"), near) is None
    assert check(trade("104", venue="two"), near) is None
    assert check(trade("106", venue="three"), near) is None
    # A venue's earlier price never replaces its later one.
    later = MarketDataValidator(LIMITS)
    assert check(trade("100", venue="one"), later) is None
    assert check(trade("90", venue="two"), later) is None
    assert check(trade("104", venue="one", event=NOW - 1), later) is None
    assert (
        check(trade("108", venue="three"), later)
        is QuarantineCause.EXCHANGE_INCONSISTENCY
    )
    # Another instrument of the same assets is another market.
    other = MarketDataValidator(LIMITS)
    assert check(trade("100", venue="one"), other) is None
    assert check(trade("100", venue="two"), other) is None
    assert check(trade("110", venue="three", kind="perpetual"), other) is None
    # Another venue's price that is no longer valid is not compared.
    aged = MarketDataValidator(LIMITS)
    for venue in ("one", "two"):
        assert check(trade("100", venue=venue, event=NOW - STALE - 1), aged) is None
    assert check(trade("200", venue="three"), aged) is None


# Freshness and quality (MKD-006, MKD-012; D3).


@pytest.mark.req("MKD-006", "MKD-012")
@pytest.mark.parametrize(
    ("age", "state"),
    [
        (0, Freshness.VALID),
        (STALE, Freshness.VALID),
        (STALE + 1, Freshness.STALE),
        (INVALID, Freshness.STALE),
        (INVALID + 1, Freshness.INVALID),
    ],
)
def test_freshness_moves_from_valid_to_stale_to_invalid(
    age: int, state: Freshness
) -> None:
    assert freshness(age, LIMITS.for_stream(Stream.TRADES)) is state
    result = validated(trade(event=NOW - age))
    assert result.assessment.freshness is state
    assert result.assessment.age_ns == age
    assert result.eligible is (state is Freshness.VALID)


@pytest.mark.req("MKD-008", "MKD-012")
def test_the_quality_score_follows_its_rule() -> None:
    assert [quality_score(state, venue_timed=True) for state in Freshness] == [
        100,
        50,
        0,
    ]
    assert [quality_score(state, venue_timed=False) for state in Freshness] == [
        90,
        40,
        0,
    ]
    unstamped = assess(trade(event=None, receive=NOW - STALE - 1), NOW, LIMITS)
    assert (unstamped.freshness, unstamped.score) == (Freshness.STALE, 40)
    assert unstamped.rule_version == QUALITY_RULE_VERSION
    ahead = assess(trade(event=NOW + 5), NOW, LIMITS)
    assert (ahead.age_ns, ahead.freshness) == (0, Freshness.VALID)


@pytest.mark.req("MKD-006", "MKD-012")
def test_a_closed_bar_is_as_old_as_its_end() -> None:
    closed = bar("1", "1", "1", "1", event=None, open_time=NOW - 70 * SECOND)
    assessed = assess(closed, NOW, LIMITS)
    assert (assessed.age_ns, assessed.freshness, assessed.score) == (
        INVALID,
        Freshness.STALE,
        50,
    )
    still_open = bar(
        "1", "1", "1", "1", event=None, open_time=NOW - 30 * SECOND, closed=False
    )
    assert (
        assess(still_open, NOW, LIMITS).age_ns,
        assess(still_open, NOW, LIMITS).score,
    ) == (
        0,
        90,
    )


@pytest.mark.req("MKD-006", "MKD-012")
def test_a_stream_s_freshness_follows_its_latest_item() -> None:
    streams = StreamFreshness(LIMITS)
    assert streams.state("example", Stream.TRADES, SPOT, NOW) is Freshness.INVALID
    streams.observe(validated(trade(event=NOW)))
    streams.observe(validated(trade(event=NOW - INVALID)))  # older: changes nothing
    assert streams.state("example", Stream.TRADES, SPOT, NOW + STALE) is Freshness.VALID
    assert (
        streams.state("example", Stream.TRADES, SPOT, NOW + STALE + 1)
        is Freshness.STALE
    )
    assert (
        streams.state("example", Stream.TRADES, SPOT, NOW + INVALID + 1)
        is Freshness.INVALID
    )
    assert streams.state("example", Stream.TICKER, SPOT, NOW) is Freshness.INVALID


# The validated type and the quarantine record (MKD-008, MKD-009, MKD-011).


@pytest.mark.req("MKD-008", "MKD-011")
def test_only_the_validator_creates_validated_data_and_none_changes() -> None:
    item = trade()
    result = validated(item)
    assert result.item is item
    assert result.validation_version == VALIDATION_RULE_VERSION
    with pytest.raises(TypeError, match="only atp.marketdata's validator"):
        Validated(item, result.assessment, creator=object())
    with pytest.raises(AttributeError):
        result.item = trade()  # type: ignore[misc]
    with pytest.raises(AttributeError):
        del result.assessment


@pytest.mark.req("MKD-009", "MKD-013")
def test_a_quarantine_record_keeps_the_item_s_evidence() -> None:
    item = trade(price="0")
    record = MarketDataValidator(LIMITS).validate(
        item, now_ns=NOW, drifting_venues=frozenset()
    )
    assert isinstance(record, QuarantineRecord)
    assert (record.evidence_id, record.venue, record.market, record.stream) == (
        item.evidence_id,
        "example",
        SPOT,
        Stream.TRADES,
    )
    assert (record.quarantined_time_ns, record.rule_version) == (
        NOW,
        VALIDATION_RULE_VERSION,
    )
    held = MarketDataValidator(LIMITS).validate(
        venue_state(), now_ns=NOW, drifting_venues=frozenset({"example"})
    )
    assert isinstance(held, QuarantineRecord)
    assert (held.market, held.stream) == (None, Stream.VENUE_STATUS)


# Drift injection (HLT-013, SR-14): the clock monitor's verdict quarantines the venue's data.


@pytest.mark.req("HLT-013", "MKD-013")
def test_an_injected_venue_drift_quarantines_that_venue_s_data() -> None:
    monitor = ClockMonitor(
        ClockLimits(
            drift_limit_ns=50_000_000, sample_max_age_ns=60 * SECOND, minimum_venues=2
        )
    )
    monitor.observe(ClockSample("example", NOW + SECOND, NOW - 1_000_000, NOW))
    monitor.observe(ClockSample("other", NOW, NOW - 1_000_000, NOW))
    verdict = monitor.verdict(NOW)
    assert verdict.drifting_venues == frozenset({"example"})
    assert (
        check(trade(), drifting=verdict.drifting_venues)
        is QuarantineCause.CLOCK_PROBLEM
    )
    assert check(trade(venue="other"), drifting=verdict.drifting_venues) is None


# Properties: deduplication idempotent, ordering stable, quality repeatable, and nothing
# quarantined, or stale when validated, is eligible.

_PAIRS = st.lists(
    st.tuples(
        st.integers(min_value=1, max_value=10**6),
        st.integers(min_value=0, max_value=2 * INVALID),
        st.booleans(),
    ),
    max_size=12,
)


def _items(pairs: list[tuple[int, int, bool]], *, repeats: bool) -> list[MarketItem]:
    items: list[MarketItem] = []
    for price, age, repeat in pairs:
        item = trade(str(price), event=NOW - age)
        items.extend([item, item] if repeats and repeat else [item])
    return items


@pytest.mark.req("MKD-004")
@given(_PAIRS)
def test_deduplication_is_idempotent_and_keeps_the_first_of_each(
    pairs: list[tuple[int, int, bool]],
) -> None:
    items = _items(pairs, repeats=True)
    once = deduplicate(items)
    assert deduplicate(once) == once
    assert [item.evidence_id for item in once] == list(
        dict.fromkeys(item.evidence_id for item in items)
    )


@pytest.mark.req("MKD-004")
@given(_PAIRS, st.randoms(use_true_random=False))
def test_ordering_is_one_order_for_the_same_items(
    pairs: list[tuple[int, int, bool]], random: Random
) -> None:
    items = _items(pairs, repeats=False)
    shuffled = list(items)
    random.shuffle(shuffled)
    ordered = in_order(items)
    assert in_order(shuffled) == ordered
    times = [item.event_time_ns or 0 for item in ordered]
    assert times == sorted(times)


@pytest.mark.req("MKD-008", "MKD-012")
@given(_PAIRS)
def test_the_quality_assessment_is_repeatable(
    pairs: list[tuple[int, int, bool]],
) -> None:
    for item in _items(pairs, repeats=False):
        assert assess(item, NOW, LIMITS) == assess(item, NOW, LIMITS)


@pytest.mark.req("MKD-009", "MKD-012")
@given(_PAIRS)
def test_nothing_quarantined_or_stale_is_eligible(
    pairs: list[tuple[int, int, bool]],
) -> None:
    validator = MarketDataValidator(LIMITS)
    for item in _items(pairs, repeats=True):
        result = validator.validate(item, now_ns=NOW, drifting_venues=frozenset())
        if isinstance(result, Validated):
            event = result.item.event_time_ns
            assert event is not None
            assert result.eligible is (NOW - event <= STALE)
        else:
            assert isinstance(result, QuarantineRecord)


@pytest.mark.req("MKD-008", "MKD-013")
def test_a_ticker_without_a_last_price_is_checked_by_its_bid_else_its_ask() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(ticker("99", "101", "100"), validator) is None
    assert check(ticker("80", "105", None), validator) is QuarantineCause.OUTLIER
    assert check(ticker(None, "150", None), validator) is QuarantineCause.OUTLIER


@pytest.mark.req("MKD-008", "MKD-013")
def test_a_snapshot_without_bids_is_checked_by_its_best_ask() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(snapshot(), validator) is None
    lone_ask = snapshot(bids=[], asks=levels(("200", "1")), sequence=11)
    assert check(lone_ask, validator) is QuarantineCause.OUTLIER


@pytest.mark.req("MKD-004")
def test_items_of_one_time_are_in_the_venue_s_sequence() -> None:
    pairs = ((update(1, 1), update(2, 2)) for _ in range(64))
    one, two = next((a, b) for a, b in pairs if a.evidence_id > b.evidence_id)
    assert in_order([two, one]) == [one, two]


@pytest.mark.req("MKD-009", "MKD-013")
def test_a_quarantine_record_is_timed_by_its_check() -> None:
    record = MarketDataValidator(LIMITS).validate(
        trade(price="0"), now_ns=NOW + 1, drifting_venues=frozenset()
    )
    assert isinstance(record, QuarantineRecord)
    assert record.quarantined_time_ns == NOW + 1


@pytest.mark.req("MKD-008", "MKD-013")
def test_a_bar_is_checked_by_its_close() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(bar("100", "100", "100", "100"), validator) is None
    # Its close within the limit, its open and high beyond it: accepted.
    assert check(bar("150", "150", "99", "101"), validator) is None
    # Its close beyond the limit, its open and low within it: an outlier.
    assert check(bar("100", "150", "100", "150"), validator) is QuarantineCause.OUTLIER


@pytest.mark.req("MKD-004")
def test_snapshots_of_one_time_are_in_the_venue_s_sequence() -> None:
    pairs = ((snapshot(sequence=10), snapshot(sequence=11)) for _ in range(64))
    one, two = next((a, b) for a, b in pairs if a.evidence_id > b.evidence_id)
    assert in_order([two, one]) == [one, two]


@pytest.mark.req("MKD-004")
def test_a_book_from_sequence_zero_follows_its_updates() -> None:
    validator = MarketDataValidator(LIMITS)
    assert check(snapshot(sequence=0), validator) is None
    assert check(update(1, 1), validator) is None
    assert check(update(2, 2), validator) is None
    assert not validator.needs_snapshot(SPOT)
