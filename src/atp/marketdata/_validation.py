"""Validation before use, once, in this system (MKD-003, MKD-004, MKD-008, MKD-009, MKD-011,
MKD-013; SR-12, SR-13; the Stage 2 plan's U5).

Every item an adapter gives is checked in this order, and the first check it fails quarantines it
with that cause and its evidence; a quarantined item is never passed on (MKD-009):

1. CLOCK_PROBLEM: its venue's clock is drifting, as SYS-29's clock monitor finds (D3).
2. INVALID_TIMESTAMP: it was received after the time it is checked at, so its age cannot be
   known; or its event time is ahead of its local receipt by more than the limit, or a bar
   opened, or a closed bar ended, that far after its receipt.
3. MISSING_FIELD: a ticker gives no price at all; a trading market's metadata lacks its price or
   quantity increment (ARCH-011 needs both).
4. IMPOSSIBLE_PRICE, for impossible values: a price, increment, or contract size not above zero;
   a quantity, volume, or minimum below zero; a trade, or a level of a book snapshot, of zero
   quantity; a ticker or snapshot whose best bid is not below its best ask; a snapshot's bids
   not strictly falling or asks not strictly rising; a bar whose high is below its open or
   close, or whose low is above either, and so also one whose high is below its low. The levels
   of a book update, which lists only what changed, may come in any order, and a funding rate
   may be below zero.
5. DUPLICATE_EVENT: its evidence identifier is among the last ones seen; a book update whose
   sequence numbers the market's book already holds is a duplicate too.
6. SEQUENCE_GAP: a book update that does not follow the market's last snapshot or update, by the
   venue's sequence numbers; the book then stays broken, every update a gap, until a fresh
   snapshot (`needs_snapshot`). An update before any snapshot is a gap, and so is one without
   a sequence number of its own in a book whose snapshot has one. Where the venue's snapshot
   gives no sequence number, its updates cannot be checked, and are not.
7. OUTLIER: its price differs from its market's and stream's reference price, the accepted one
   that describes the latest time, by more than the outlier limit. Outliers in a row form a run,
   and an outlier beyond the limit of the run's last starts a new run; a price that is not an
   outlier ends the run. Once the run holds `outlier_confirmations` outliers, the next outlier
   within the limit of each of them is accepted and ends the run: the market moved.
8. EXCHANGE_INCONSISTENCY: its price, valid when checked, differs by more than the inconsistency
   limit from every other venue's valid latest price for the same market and stream, and at
   least `minimum_other_venues` other venues give one. A price no longer valid is not compared:
   it is not eligible for use (MKD-012).

The checks follow MKD-003's order: validation (1 to 4), then normalization (deduplication and
ordering, 5 and 6, with `deduplicate` and `in_order`), then quality checks (7, 8, and the
assessment); storage follows (U6). The price checked is a trade's price, a bar's close, a
ticker's last price (else its bid, else its ask), and a snapshot's best bid (else its best ask);
book updates, funding rates, metadata, and venue states have none. Prices are compared exactly,
as integer ratios, without division or rounding. An item that passes is assessed (`assess`) and
returned as `Validated`, the only form in which consumers accept market data; it is eligible for
use only if VALID when assessed (MKD-012, SR-12): `eligible` keeps that assessment, so an item
used later is assessed again at the time of use (`assess`).

Out-of-order data (MKD-004) is still checked and assessed, but an item never replaces a
reference or latest price that describes a later time, and a book update out of the venue's
sequence is a duplicate or a gap. A market's book is checked in the order its adapter gives it,
as its venue's procedure has it (U4): a snapshot, then the updates that follow it.
"""

from __future__ import annotations

from collections import OrderedDict, deque
from dataclasses import InitVar, dataclass
from decimal import Decimal
from itertools import pairwise
from typing import Final, final

from atp.marketdata._contracts import (
    BookLevel,
    BookSnapshot,
    BookUpdate,
    Freshness,
    InstrumentType,
    MarketMetadata,
    MarketRef,
    MarketStatus,
    OhlcvBar,
    QualityAssessment,
    QuarantineCause,
    QuarantineRecord,
    Stream,
    Ticker,
    Trade,
)
from atp.marketdata._items import (
    MarketItem,
    bar_end_ns,
    item_time_ns,
    market_of,
    stream_of,
    venue_of,
)
from atp.marketdata._limits import ValidationLimits
from atp.marketdata._quality import age_ns, assess, freshness

VALIDATION_RULE_VERSION: Final = "1.0"
"""The version of the checks above; a change to them is a new version, which every quarantine
record and validated item carries."""

# The token only this module holds, without which `Validated` refuses to be created.
_CREATOR: Final = object()


@final
@dataclass(frozen=True, slots=True)
class Validated[ItemT: MarketItem]:
    """An item this system validated, and its quality assessment when validated. Only
    `MarketDataValidator` creates one, and none is changed after."""

    item: ItemT
    assessment: QualityAssessment
    creator: InitVar[object]

    def __post_init__(self, creator: object) -> None:
        if creator is not _CREATOR:
            msg = "only atp.marketdata's validator creates validated data"
            raise TypeError(msg)

    @property
    def validation_version(self) -> str:
        """The version of the validation rules it passed (MKD-010)."""
        return VALIDATION_RULE_VERSION

    @property
    def eligible(self) -> bool:
        """Whether it was VALID when assessed (MKD-012, SR-12); it does not change as the item
        ages."""
        return self.assessment.freshness is Freshness.VALID


# The state of a market's book chain: the last sequence number applied (0 or more), or one of
# these. A gap was found, and every update is a gap until a fresh snapshot:
_BROKEN: Final = -1
# The last snapshot gave no sequence number, and updates are not checked:
_UNSEQUENCED: Final = -2

_CanonicalKey = tuple[str, str, InstrumentType, str | None, Stream]


@dataclass
class _Reference:
    """A market's and stream's reference price and its time, and the run of outliers since:
    its last `outlier_confirmations`, all a confirmation needs (a deque of that length)."""

    price: Decimal
    time_ns: int
    outliers: deque[Decimal]


def _beyond(price: Decimal, reference: Decimal, limit: Decimal) -> bool:
    """Whether `price` differs from `reference`, which is above zero, by more than `limit` times
    `reference`, compared exactly as integer ratios."""
    price_n, price_d = price.as_integer_ratio()
    reference_n, reference_d = reference.as_integer_ratio()
    limit_n, limit_d = limit.as_integer_ratio()
    difference = abs(price_n * reference_d - reference_n * price_d)
    return difference * limit_d > limit_n * reference_n * price_d


def _confirms(run: deque[Decimal], price: Decimal, limit: Decimal) -> bool:
    """Whether `price`, an outlier, confirms the run of outliers before it: the run is full and
    `price` is within `limit` of each one in it. If not, `price` joins the run, or starts a new
    one when it is beyond `limit` of the run's last."""
    if len(run) == run.maxlen and not any(
        _beyond(price, earlier, limit) for earlier in run
    ):
        return True
    if run and _beyond(price, run[-1], limit):
        run.clear()
    run.append(price)
    return False


def _checked_price(item: MarketItem) -> Decimal | None:
    if isinstance(item, Trade):
        return item.price
    if isinstance(item, OhlcvBar):
        return item.close
    if isinstance(item, Ticker):
        for price in (item.last, item.bid, item.ask):
            if price is not None:
                return price
        return None
    if isinstance(item, BookSnapshot):
        best = item.bids or item.asks
        return best[0].price if best else None
    return None


def _levels_impossible(
    levels: tuple[BookLevel, ...], *, falling: bool, snapshot: bool
) -> bool:
    for level in levels:
        if level.price <= 0 or level.quantity < 0 or (snapshot and level.quantity == 0):
            return True
    if not snapshot:
        return False
    prices = [level.price for level in levels]
    pairs = pairwise(prices)
    if falling:
        return any(later >= earlier for earlier, later in pairs)
    return any(later <= earlier for earlier, later in pairs)


def _impossible(item: MarketItem) -> bool:
    if isinstance(item, Trade):
        return item.price <= 0 or item.quantity <= 0
    if isinstance(item, Ticker):
        prices = [
            price for price in (item.bid, item.ask, item.last) if price is not None
        ]
        sizes = [size for size in (item.bid_size, item.ask_size) if size is not None]
        if any(price <= 0 for price in prices) or any(size < 0 for size in sizes):
            return True
        return item.bid is not None and item.ask is not None and item.bid >= item.ask
    if isinstance(item, BookSnapshot):
        if _levels_impossible(
            item.bids, falling=True, snapshot=True
        ) or _levels_impossible(item.asks, falling=False, snapshot=True):
            return True
        return bool(
            item.bids and item.asks and item.bids[0].price >= item.asks[0].price
        )
    if isinstance(item, BookUpdate):
        return _levels_impossible(
            item.bids, falling=True, snapshot=False
        ) or _levels_impossible(item.asks, falling=False, snapshot=False)
    if isinstance(item, OhlcvBar):
        if min(item.open, item.high, item.low, item.close) <= 0:
            return True
        if item.base_volume < 0 or (
            item.quote_volume is not None and item.quote_volume < 0
        ):
            return True
        return item.high < max(item.open, item.close) or item.low > min(
            item.open, item.close
        )
    if isinstance(item, MarketMetadata):
        positive = (item.price_increment, item.quantity_increment, item.contract_size)
        not_negative = (item.minimum_quantity, item.minimum_notional)
        return any(value is not None and value <= 0 for value in positive) or any(
            value is not None and value < 0 for value in not_negative
        )
    return False


def _missing(item: MarketItem) -> bool:
    if isinstance(item, Ticker):
        return item.bid is None and item.ask is None and item.last is None
    if isinstance(item, MarketMetadata):
        return item.status is MarketStatus.TRADING and (
            item.price_increment is None or item.quantity_increment is None
        )
    return False


def _timestamp_invalid(item: MarketItem, max_ahead_ns: int) -> bool:
    latest = item.receive_time_ns + max_ahead_ns
    if item.event_time_ns is not None and item.event_time_ns > latest:
        return True
    if isinstance(item, OhlcvBar):
        return item.open_time_ns > latest or (item.closed and bar_end_ns(item) > latest)
    return False


def _sequence_key(item: MarketItem) -> int:
    if isinstance(item, BookSnapshot) and item.sequence is not None:
        return item.sequence
    if isinstance(item, BookUpdate):
        for sequence in (
            item.first_sequence,
            item.last_sequence,
            item.previous_sequence,
        ):
            if sequence is not None:
                return sequence
    return -1


def deduplicate(items: list[MarketItem]) -> list[MarketItem]:
    """The items without duplicates: the first of each evidence identifier, in their order."""
    seen: set[str] = set()
    kept: list[MarketItem] = []
    for item in items:
        if item.evidence_id not in seen:
            seen.add(item.evidence_id)
            kept.append(item)
    return kept


def in_order(items: list[MarketItem]) -> list[MarketItem]:
    """The items in the order of the time they describe, then of the venue's sequence number,
    then of their evidence identifiers: one order for the same items, however they arrived. A
    market's book is not put in this order: its adapter gives a snapshot, then the updates that
    follow it, in its venue's sequence."""
    return sorted(
        items,
        key=lambda item: (item_time_ns(item), _sequence_key(item), item.evidence_id),
    )


class MarketDataValidator:
    """The checks above, with the state they need: the last evidence identifiers seen, each
    market's book chain, each market's reference prices, and each venue's latest prices, one
    entry per market and stream of the configured universe. One validator serves one process;
    its state is not shared between threads."""

    def __init__(self, limits: ValidationLimits) -> None:
        self._limits = limits
        self._seen: OrderedDict[str, None] = OrderedDict()
        self._chains: dict[MarketRef, int] = {}
        self._references: dict[tuple[MarketRef, Stream], _Reference] = {}
        self._latest: dict[_CanonicalKey, dict[str, tuple[Decimal, int]]] = {}

    def needs_snapshot(self, market: MarketRef) -> bool:
        """Whether `market`'s book needs a fresh snapshot: it has none yet, or a gap broke it.

        Until then each update given is quarantined and its evidence identifier remembered, so
        the same update given again after the snapshot is a duplicate while it is remembered: an
        adapter holds the updates it receives until the snapshot and gives only those that follow
        it, as its venue's procedure has it (U4)."""
        state = self._chains.get(market)
        return state is None or state == _BROKEN

    def validate[T: MarketItem](
        self, item: T, *, now_ns: int, drifting_venues: frozenset[str]
    ) -> Validated[T] | QuarantineRecord:
        """Check `item` at `now_ns`, the local time, with the venues whose clocks SYS-29 finds
        drifting: the validated item, or the record of its quarantine."""
        cause = self._check(item, now_ns, drifting_venues)
        if cause is not None:
            return QuarantineRecord(
                evidence_id=item.evidence_id,
                venue=venue_of(item),
                market=market_of(item),
                stream=stream_of(item),
                cause=cause,
                quarantined_time_ns=now_ns,
                rule_version=VALIDATION_RULE_VERSION,
            )
        return Validated(item, assess(item, now_ns, self._limits), creator=_CREATOR)

    def _check(
        self, item: MarketItem, now_ns: int, drifting_venues: frozenset[str]
    ) -> QuarantineCause | None:
        limits = self._limits
        if venue_of(item) in drifting_venues:
            return QuarantineCause.CLOCK_PROBLEM
        if item.receive_time_ns > now_ns or _timestamp_invalid(
            item, limits.max_event_ahead_ns
        ):
            return QuarantineCause.INVALID_TIMESTAMP
        if _missing(item):
            return QuarantineCause.MISSING_FIELD
        if _impossible(item):
            return QuarantineCause.IMPOSSIBLE_PRICE
        if item.evidence_id in self._seen:
            return QuarantineCause.DUPLICATE_EVENT
        self._remember(item.evidence_id)
        if isinstance(item, BookUpdate):
            cause = self._check_sequence(item)
            if cause is not None:
                return cause
        price = _checked_price(item)
        market = market_of(item)
        if price is None or market is None:
            self._accept_book(item)
            return None
        stream = stream_of(item)
        reference = self._references.get((market, stream))
        if reference is not None:
            limit = limits.outlier_limit
            if _beyond(price, reference.price, limit) and not _confirms(
                reference.outliers, price, limit
            ):
                return QuarantineCause.OUTLIER
            reference.outliers.clear()
        if self._inconsistent(item, market, stream, price, now_ns):
            return QuarantineCause.EXCHANGE_INCONSISTENCY
        self._accept_book(item)
        self._accept_price(item, market, stream, price)
        return None

    def _remember(self, evidence_id: str) -> None:
        self._seen[evidence_id] = None
        while len(self._seen) > self._limits.duplicate_memory:
            self._seen.popitem(last=False)

    def _check_sequence(self, update: BookUpdate) -> QuarantineCause | None:
        state = self._chains.get(update.market)
        if state is None or state == _BROKEN:
            return self._gap(update.market)
        if state == _UNSEQUENCED:
            return None
        last = (
            update.last_sequence
            if update.last_sequence is not None
            else update.first_sequence
        )
        if last is None:
            return self._gap(update.market)
        if update.previous_sequence == state and last >= state:
            return None
        if last <= state:
            return QuarantineCause.DUPLICATE_EVENT
        if update.previous_sequence is not None:
            return self._gap(update.market)
        first = update.first_sequence if update.first_sequence is not None else last
        if first > state + 1:
            return self._gap(update.market)
        return None

    def _gap(self, market: MarketRef) -> QuarantineCause:
        """Break `market`'s book: every update is a gap until a fresh snapshot."""
        self._chains[market] = _BROKEN
        return QuarantineCause.SEQUENCE_GAP

    def _accept_book(self, item: MarketItem) -> None:
        if isinstance(item, BookSnapshot):
            self._chains[item.market] = (
                item.sequence if item.sequence is not None else _UNSEQUENCED
            )
        elif (
            isinstance(item, BookUpdate) and self._chains.get(item.market, _BROKEN) >= 0
        ):
            last = (
                item.last_sequence
                if item.last_sequence is not None
                else item.first_sequence
            )
            if last is not None:
                self._chains[item.market] = last

    def _inconsistent(
        self,
        item: MarketItem,
        market: MarketRef,
        stream: Stream,
        price: Decimal,
        now_ns: int,
    ) -> bool:
        limits = self._limits
        stream_limits = limits.for_stream(stream)
        if freshness(age_ns(item, now_ns), stream_limits) is not Freshness.VALID:
            return False
        latest = self._latest.get(_canonical(market, stream), {})
        others = [
            other_price
            for venue, (other_price, time) in latest.items()
            if venue != market.venue
            and freshness(max(now_ns - time, 0), stream_limits) is Freshness.VALID
        ]
        return len(others) >= limits.minimum_other_venues and all(
            _beyond(price, other, limits.inconsistency_limit) for other in others
        )

    def _accept_price(
        self, item: MarketItem, market: MarketRef, stream: Stream, price: Decimal
    ) -> None:
        time = item_time_ns(item)
        reference = self._references.get((market, stream))
        if reference is None or time >= reference.time_ns:
            run: deque[Decimal] = deque(maxlen=self._limits.outlier_confirmations)
            self._references[(market, stream)] = _Reference(price, time, run)
        latest = self._latest.setdefault(_canonical(market, stream), {})
        known = latest.get(market.venue)
        if known is None or time >= known[1]:
            latest[market.venue] = (price, time)


def _canonical(market: MarketRef, stream: Stream) -> _CanonicalKey:
    return (market.base, market.quote, market.instrument_type, market.settle, stream)


class StreamFreshness:
    """Each stream's freshness from the time of its latest validated item (MKD-006, MKD-012):
    a stream with no validated item yet is INVALID. Only validated items count, so a quarantined
    item never makes a stream look fresh."""

    def __init__(self, limits: ValidationLimits) -> None:
        self._limits = limits
        self._latest: dict[tuple[str, Stream, MarketRef | None], int] = {}

    def observe(self, validated: Validated[MarketItem]) -> None:
        """Note a validated item; one older than its stream's latest changes nothing."""
        item = validated.item
        key = (venue_of(item), stream_of(item), market_of(item))
        time = item_time_ns(item)
        if time > self._latest.get(key, -1):
            self._latest[key] = time

    def state(
        self, venue: str, stream: Stream, market: MarketRef | None, now_ns: int
    ) -> Freshness:
        """The stream's freshness at `now_ns`."""
        latest = self._latest.get((venue, stream, market))
        if latest is None:
            return Freshness.INVALID
        return freshness(max(now_ns - latest, 0), self._limits.for_stream(stream))
