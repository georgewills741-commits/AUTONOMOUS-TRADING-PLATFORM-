"""The canonical market-data contracts: what adapters produce and this system validates.

Each item names its market (or, for a venue's state, its venue), the venue's event time where
the venue gives one, the local receipt time, an evidence identifier, and its lineage (the Stage 2
plan's D5). Times are integer nanoseconds since the Unix epoch, UTC: lossless at every venue's
resolution, which is recorded beside the time. Amounts are `Amount`, built from the venue's own
text, never from a float (TEC-003). The contracts check structure only (types, forms, and pairs
of fields that belong together); whether a value is plausible (a price above zero, a bid below
the ask, a sequence without a gap) is this system's validation (MKD-008, MKD-013), so a
well-formed but wrong item reaches it and is quarantined with its evidence, never dropped.
"""

from __future__ import annotations

import enum
from typing import Annotated, Final

from pydantic import AfterValidator, Field, ValidationInfo, field_validator

from atp.contracts import Amount, Contract, ContractVersion, PydanticCustomError

VENUE_PATTERN: Final = r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"
"""A venue's identifier: lowercase letters and digits, in parts joined by hyphens."""

ASSET_PATTERN: Final = r"^[A-Z0-9]{1,32}$"
"""An asset's code, as the platform writes it: capital letters and digits."""

EVIDENCE_ID_PATTERN: Final = r"^[0-9a-f]{64}$"
"""An evidence identifier: a SHA-256 digest in lowercase hexadecimal (`evidence_id`)."""

VERSION_PATTERN: Final = r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$"
"""A version written MAJOR.MINOR, without leading zeros."""

# A venue's own text (a symbol, an endpoint or channel name): printable ASCII, so that no
# control character reaches a log or a report.
_VENUE_TEXT: Final = r"^[\x20-\x7e]{1,200}$"
# A module path, such as atp.exchange.example.
_COMPONENT: Final = r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*$"
# Times and sequences fit a signed 64-bit integer, as the database stores them (D6).
_INT64_MAX: Final = 2**63 - 1


class InstrumentType(enum.Enum):
    """An instrument type of PLT-011."""

    SPOT = "spot"
    PERPETUAL = "perpetual"
    MARGIN = "margin"


class TimeResolution(enum.Enum):
    """The resolution of a venue's event times."""

    SECOND = "second"
    MILLISECOND = "millisecond"
    MICROSECOND = "microsecond"
    NANOSECOND = "nanosecond"


class Stream(enum.Enum):
    """A kind of market data, as an adapter receives it."""

    MARKETS = "markets"
    TICKER = "ticker"
    TRADES = "trades"
    BOOK = "book"
    OHLCV = "ohlcv"
    FUNDING = "funding"
    VENUE_STATUS = "venue-status"


class TakerSide(enum.Enum):
    """The side of the taker, the order that crossed the book, in a trade."""

    BUY = "buy"
    SELL = "sell"


class MarketStatus(enum.Enum):
    """Whether a market is open for trading at its venue, as the venue states it."""

    TRADING = "trading"
    HALTED = "halted"
    DELISTED = "delisted"
    UNKNOWN = "unknown"


class VenueStatus(enum.Enum):
    """Whether a venue answers, as its adapter observes it."""

    AVAILABLE = "available"
    MAINTENANCE = "maintenance"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


class UnavailableCause(enum.Enum):
    """Why a venue is unavailable."""

    REGION_REFUSED = "region-refused"
    RATE_LIMITED = "rate-limited"
    CONNECTION_FAILED = "connection-failed"
    TIMEOUT = "timeout"
    VENUE_ERROR = "venue-error"


class Freshness(enum.Enum):
    """How fresh a stream's data is (MKD-012): valid, stale past its limit, invalid beyond it."""

    VALID = "valid"
    STALE = "stale"
    INVALID = "invalid"


class QuarantineCause(enum.Enum):
    """Why an item was quarantined: the causes of MKD-013."""

    INVALID_TIMESTAMP = "invalid-timestamp"
    MISSING_FIELD = "missing-field"
    IMPOSSIBLE_PRICE = "impossible-price"
    DUPLICATE_EVENT = "duplicate-event"
    SEQUENCE_GAP = "sequence-gap"
    EXCHANGE_INCONSISTENCY = "exchange-inconsistency"
    OUTLIER = "outlier"
    CLOCK_PROBLEM = "clock-problem"


class UntranslatableCause(enum.Enum):
    """Why an adapter could not translate a venue's input into a canonical item."""

    MALFORMED = "malformed"
    OVERSIZED = "oversized"
    MISSING_FIELD = "missing-field"
    AMOUNT_NOT_TEXT = "amount-not-text"
    UNKNOWN_MARKET = "unknown-market"
    REFUSED_BY_CONTRACT = "refused-by-contract"


def _check_resolution(
    resolution: TimeResolution | None, info: ValidationInfo
) -> TimeResolution | None:
    # A refused event time is absent from the data: its own refusal is reported instead.
    if "event_time_ns" in info.data and (info.data["event_time_ns"] is None) != (
        resolution is None
    ):
        raise PydanticCustomError(
            "event_time_resolution",
            "an event time and its resolution are given together",
        )
    return resolution


# Nanoseconds since the Unix epoch, UTC, or a count of nanoseconds.
Nanoseconds = Annotated[int, Field(ge=0, le=_INT64_MAX)]
# A venue's sequence or update number.
SequenceNumber = Annotated[int, Field(ge=0, le=_INT64_MAX)]
# The resolution of the event time beside it; given exactly when the event time is.
EventTimeResolution = Annotated[
    TimeResolution | None, AfterValidator(_check_resolution)
]


class Lineage(Contract):
    """Where an item came from and what produced it (MKD-010): the venue's endpoint or channel,
    and the adapter and its version."""

    contract_id = "atp.marketdata.lineage"
    contract_version = ContractVersion(1, 0)

    source: str = Field(pattern=_VENUE_TEXT)
    adapter: str = Field(pattern=_COMPONENT)
    adapter_version: str = Field(pattern=VERSION_PATTERN)


class MarketRef(Contract):
    """A market: its venue, its base and quote assets, its instrument type, and, for a perpetual,
    the asset it settles in. A margin market trades its spot market's book."""

    contract_id = "atp.marketdata.market"
    contract_version = ContractVersion(1, 0)

    venue: str = Field(pattern=VENUE_PATTERN)
    base: str = Field(pattern=ASSET_PATTERN)
    quote: str = Field(pattern=ASSET_PATTERN)
    instrument_type: InstrumentType
    settle: str | None = Field(default=None, pattern=ASSET_PATTERN)

    @field_validator("settle")
    @classmethod
    def _check_settle(cls, settle: str | None, info: ValidationInfo) -> str | None:
        kind = info.data.get("instrument_type")
        if kind is InstrumentType.PERPETUAL and settle is None:
            raise PydanticCustomError(
                "settle_missing", "a perpetual market names the asset it settles in"
            )
        if kind in (InstrumentType.SPOT, InstrumentType.MARGIN) and settle is not None:
            raise PydanticCustomError(
                "settle_not_allowed",
                "only a perpetual market names an asset it settles in",
            )
        return settle

    def symbol(self) -> str:
        """The market's symbol: `BASE/QUOTE`, and `:SETTLE` after it for a perpetual."""
        settle = "" if self.settle is None else f":{self.settle}"
        return f"{self.base}/{self.quote}{settle}"


class MarketMetadata(Contract):
    """A market's description at its venue: the venue's own symbol, its status, and its
    increments and minimums, each as the venue states it, or absent where it states none."""

    contract_id = "atp.marketdata.market-metadata"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    venue_symbol: str = Field(pattern=_VENUE_TEXT)
    status: MarketStatus
    price_increment: Amount | None = None
    quantity_increment: Amount | None = None
    minimum_quantity: Amount | None = None
    minimum_notional: Amount | None = None
    contract_size: Amount | None = None
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class Ticker(Contract):
    """A market's best bid and ask, last price, and volume over the venue's last 24 hours, each
    absent where the venue gives none."""

    contract_id = "atp.marketdata.ticker"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    bid: Amount | None = None
    bid_size: Amount | None = None
    ask: Amount | None = None
    ask_size: Amount | None = None
    last: Amount | None = None
    base_volume_24h: Amount | None = None
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class Trade(Contract):
    """One trade in a market: its price, its quantity in the base asset, the taker's side where
    the venue gives it, and the venue's identifier of the trade where it has one."""

    contract_id = "atp.marketdata.trade"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    price: Amount
    quantity: Amount
    taker_side: TakerSide | None = None
    venue_trade_id: str | None = Field(default=None, pattern=_VENUE_TEXT)
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class BookLevel(Contract):
    """One price level of an order book: its price and the quantity there, in the base asset.
    In a book update, a quantity of zero removes the level."""

    contract_id = "atp.marketdata.book-level"
    contract_version = ContractVersion(1, 0)

    price: Amount
    quantity: Amount


class BookSnapshot(Contract):
    """A market's order book at one time: its bid levels, best first, its ask levels, best
    first, and the venue's sequence number of the snapshot where it gives one."""

    contract_id = "atp.marketdata.book-snapshot"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    bids: tuple[BookLevel, ...]
    asks: tuple[BookLevel, ...]
    sequence: SequenceNumber | None = None
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class BookUpdate(Contract):
    """A change to a market's order book: the levels that changed, and the venue's sequence
    numbers that place it, the first and last it covers and the last before it, each where the
    venue gives one, so that a gap can be found."""

    contract_id = "atp.marketdata.book-update"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    bids: tuple[BookLevel, ...]
    asks: tuple[BookLevel, ...]
    first_sequence: SequenceNumber | None = None
    last_sequence: SequenceNumber | None = None
    previous_sequence: SequenceNumber | None = None
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage

    @field_validator("last_sequence")
    @classmethod
    def _check_sequence_order(
        cls, last: int | None, info: ValidationInfo
    ) -> int | None:
        first = info.data.get("first_sequence")
        if first is not None and last is not None and last < first:
            raise PydanticCustomError(
                "sequence_order", "the last sequence number is not before the first"
            )
        return last


class OhlcvBar(Contract):
    """One bar of a market's prices: the interval it covers, in seconds, from its opening time;
    its open, high, low, and close; its volume in the base asset, and in the quote asset where
    the venue gives it; and whether the bar is closed, so its values are final."""

    contract_id = "atp.marketdata.ohlcv-bar"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    interval_seconds: int = Field(gt=0, le=_INT64_MAX)
    open_time_ns: Nanoseconds
    open: Amount
    high: Amount
    low: Amount
    close: Amount
    base_volume: Amount
    quote_volume: Amount | None = None
    closed: bool
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class FundingRate(Contract):
    """A perpetual market's funding rate, as a fraction of the position's value for one funding
    interval; the time it applies at, and the interval in seconds, where the venue gives them."""

    contract_id = "atp.marketdata.funding-rate"
    contract_version = ContractVersion(1, 0)

    market: MarketRef
    rate: Amount
    funding_time_ns: Nanoseconds | None = None
    interval_seconds: int | None = Field(default=None, gt=0, le=_INT64_MAX)
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage


class VenueState(Contract):
    """Whether a venue answers, as its adapter observes it, and why it is unavailable when it
    is."""

    contract_id = "atp.marketdata.venue-state"
    contract_version = ContractVersion(1, 0)

    venue: str = Field(pattern=VENUE_PATTERN)
    status: VenueStatus
    cause: UnavailableCause | None = None
    event_time_ns: Nanoseconds | None = None
    event_time_resolution: EventTimeResolution = None
    receive_time_ns: Nanoseconds
    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    lineage: Lineage

    @field_validator("cause")
    @classmethod
    def _check_cause(
        cls, cause: UnavailableCause | None, info: ValidationInfo
    ) -> UnavailableCause | None:
        status = info.data.get("status")
        if status is VenueStatus.UNAVAILABLE and cause is None:
            raise PydanticCustomError(
                "cause_missing", "an unavailable venue has a cause"
            )
        if (
            status is not None
            and status is not VenueStatus.UNAVAILABLE
            and cause is not None
        ):
            raise PydanticCustomError(
                "cause_not_allowed", "only an unavailable venue has a cause"
            )
        return cause


class QualityAssessment(Contract):
    """This system's assessment of one item (MKD-008, MKD-012): its freshness and age when
    assessed, and its quality score, from 0 to 100, under the named version of the rules."""

    contract_id = "atp.marketdata.quality"
    contract_version = ContractVersion(1, 0)

    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    assessed_time_ns: Nanoseconds
    freshness: Freshness
    age_ns: Nanoseconds
    score: int = Field(ge=0, le=100)
    rule_version: str = Field(pattern=VERSION_PATTERN)


class QuarantineRecord(Contract):
    """An item held back from consumers (MKD-009, MKD-013): the item's evidence identifier, its
    venue, its market, of that venue, given exactly when its stream is not the venue's status,
    its stream, the cause, and the version of the rule that found it."""

    contract_id = "atp.marketdata.quarantine-record"
    # 2.0 narrows 1.0, which paired any market, or none, with any stream (J-28).
    contract_version = ContractVersion(2, 0)

    evidence_id: str = Field(pattern=EVIDENCE_ID_PATTERN)
    venue: str = Field(pattern=VENUE_PATTERN)
    market: MarketRef | None = None
    stream: Stream
    cause: QuarantineCause
    quarantined_time_ns: Nanoseconds
    rule_version: str = Field(pattern=VERSION_PATTERN)

    @field_validator("stream")
    @classmethod
    def _check_market(cls, stream: Stream, info: ValidationInfo) -> Stream:
        # A refused market or venue is absent from the data: its own refusal is reported.
        if "market" not in info.data:
            return stream
        market = info.data["market"]
        if (market is None) != (stream is Stream.VENUE_STATUS):
            raise PydanticCustomError(
                "market_for_stream",
                "a record names its market exactly when its stream is not the venue's status",
            )
        venue = info.data.get("venue")
        if market is not None and venue is not None and market.venue != venue:
            raise PydanticCustomError(
                "market_venue", "a record's market is of the record's venue"
            )
        return stream


class UntranslatableInput(Contract):
    """A venue's input an adapter could not translate (EXA-013): where it came from, when it was
    received, why it was refused, and the SHA-256 digest and length in bytes of its content,
    which itself is not kept here."""

    contract_id = "atp.marketdata.untranslatable-input"
    contract_version = ContractVersion(1, 0)

    venue: str = Field(pattern=VENUE_PATTERN)
    stream: Stream
    lineage: Lineage
    receive_time_ns: Nanoseconds
    cause: UntranslatableCause
    content_sha256: str = Field(pattern=EVIDENCE_ID_PATTERN)
    content_length: int = Field(ge=0, le=_INT64_MAX)
