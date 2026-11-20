"""The canonical items, as one type, and what every item gives: its stream, venue, market, and time."""

from __future__ import annotations

from typing import Final

from atp.marketdata._contracts import (
    BookSnapshot,
    BookUpdate,
    FundingRate,
    MarketMetadata,
    MarketRef,
    OhlcvBar,
    Stream,
    Ticker,
    Trade,
    VenueState,
)

MarketItem = (
    MarketMetadata
    | Ticker
    | Trade
    | BookSnapshot
    | BookUpdate
    | OhlcvBar
    | FundingRate
    | VenueState
)
"""An item an adapter translates a venue's data into (EXA-013)."""

_STREAMS: Final[dict[type, Stream]] = {
    MarketMetadata: Stream.MARKETS,
    Ticker: Stream.TICKER,
    Trade: Stream.TRADES,
    BookSnapshot: Stream.BOOK,
    BookUpdate: Stream.BOOK,
    OhlcvBar: Stream.OHLCV,
    FundingRate: Stream.FUNDING,
    VenueState: Stream.VENUE_STATUS,
}
_NANOSECONDS_PER_SECOND: Final = 1_000_000_000


def stream_of(item: MarketItem) -> Stream:
    """The stream `item` belongs to."""
    return _STREAMS[type(item)]


def market_of(item: MarketItem) -> MarketRef | None:
    """The market `item` names; a venue's state names none."""
    if isinstance(item, VenueState):
        return None
    return item.market


def venue_of(item: MarketItem) -> str:
    """The venue `item` comes from."""
    if isinstance(item, VenueState):
        return item.venue
    return item.market.venue


def bar_end_ns(bar: OhlcvBar) -> int:
    """The end of `bar`'s interval: its opening time and its length."""
    return bar.open_time_ns + bar.interval_seconds * _NANOSECONDS_PER_SECOND


def venue_time_ns(item: MarketItem) -> int | None:
    """The time the venue gives for `item`: its event time; else, for a closed bar, whose values
    are final, the end of its interval; else none."""
    if item.event_time_ns is not None:
        return item.event_time_ns
    if isinstance(item, OhlcvBar) and item.closed:
        return bar_end_ns(item)
    return None


def item_time_ns(item: MarketItem) -> int:
    """The time `item` describes: the venue's time for it (`venue_time_ns`), else the local
    receipt time."""
    venue_time = venue_time_ns(item)
    return item.receive_time_ns if venue_time is None else venue_time
