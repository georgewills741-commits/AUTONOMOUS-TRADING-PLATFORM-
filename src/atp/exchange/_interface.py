"""The interface a venue adapter gives the rest of the platform (EXA-001, EXA-004, EXA-006,
EXA-011, EXA-013; the Stage 2 plan's U4).

One adapter per enabled venue implements `VenueAdapter`; nothing else talks to a venue (EXA-004),
and a venue's behavior stays in its adapter (EXA-011), so a venue is added by its adapter and its
configuration alone (EXA-006). In Stage 2 an adapter reads public market data, with no
credential (the plan's D1); EXA-003's other duties come with CORE TRADING FOUNDATION. Each
request's result is an outcome (`request_outcome`), and what an answer holds is a
`Translation`: the canonical items of SYS-02's contracts (EXA-013) and, for what could not be
translated, its record with the cause.
"""

from __future__ import annotations

import re
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Final, Protocol

from atp.contracts import Outcome
from atp.exchange._requests import RequestFailure
from atp.exchange._resilience import FeedEvent
from atp.marketdata import (
    VENUE_PATTERN,
    BookSnapshot,
    FundingRate,
    MarketItem,
    MarketMetadata,
    MarketRef,
    OhlcvBar,
    Stream,
    Ticker,
    Trade,
    UntranslatableInput,
    VenueState,
)

_INT64_MAX: Final = 2**63 - 1


@dataclass(frozen=True, slots=True)
class Translation[ItemT]:
    """What one answer or message of a venue holds: its canonical items, and the record of
    each part that could not be translated, which goes to SYS-02 with them."""

    items: tuple[ItemT, ...]
    untranslatable: tuple[UntranslatableInput, ...] = ()


@dataclass(frozen=True, slots=True)
class ServerTime:
    """A venue's server time, with the local times its request was sent and its answer
    received, all from the wall clock, in nanoseconds since the Unix epoch, UTC: what SYS-29's
    clock monitor compares (HLT-013)."""

    venue: str
    venue_time_ns: int
    sent_ns: int
    received_ns: int

    def __post_init__(self) -> None:
        if (
            type(self.venue) is not str
            or re.fullmatch(VENUE_PATTERN, self.venue) is None
        ):
            msg = "a server time names a venue"
            raise ValueError(msg)
        times = (self.venue_time_ns, self.sent_ns, self.received_ns)
        if any(type(time) is not int or not 0 <= time <= _INT64_MAX for time in times):
            msg = "a server time's times are whole nanoseconds since the epoch"
            raise ValueError(msg)
        if self.sent_ns > self.received_ns:
            msg = "a request is sent before its answer is received"
            raise ValueError(msg)


class VenueAdapter(Protocol):
    """A venue's public market data, as the rest of the platform reads it."""

    @property
    def venue(self) -> str:
        """The venue's identifier."""
        ...

    async def server_time(self) -> Outcome[ServerTime, RequestFailure]:
        """The venue's server time."""
        ...

    async def markets(self) -> Outcome[Translation[MarketMetadata], RequestFailure]:
        """The venue's markets, with their increments and minimums (ARCH-011)."""
        ...

    async def ticker(
        self, market: MarketRef
    ) -> Outcome[Translation[Ticker], RequestFailure]:
        """A market's ticker."""
        ...

    async def trades(
        self, market: MarketRef
    ) -> Outcome[Translation[Trade], RequestFailure]:
        """A market's recent trades."""
        ...

    async def book(
        self, market: MarketRef, depth: int
    ) -> Outcome[Translation[BookSnapshot], RequestFailure]:
        """A snapshot of a market's book, `depth` levels a side at most."""
        ...

    async def ohlcv(
        self, market: MarketRef, interval_seconds: int
    ) -> Outcome[Translation[OhlcvBar], RequestFailure]:
        """A market's recent bars of `interval_seconds`."""
        ...

    async def funding_rate(
        self, market: MarketRef
    ) -> Outcome[Translation[FundingRate], RequestFailure]:
        """A perpetual market's funding rate."""
        ...

    async def venue_state(self) -> Outcome[Translation[VenueState], RequestFailure]:
        """The venue's state, as it states it."""
        ...

    async def stream(
        self,
        markets: tuple[MarketRef, ...],
        stream: Stream,
        deliver: Callable[[Translation[MarketItem]], Awaitable[None]],
        report: Callable[[FeedEvent], None],
    ) -> None:
        """Keep one stream of these markets until the task is cancelled, or the venue refuses
        the region: each message delivered as a translation, and what happens to the feed
        reported (`maintain_connection`)."""
        ...
