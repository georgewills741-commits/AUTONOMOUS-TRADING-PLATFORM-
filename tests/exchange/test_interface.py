"""The interface a venue adapter gives the rest of the platform (EXA-001, EXA-004, EXA-006,
EXA-013; the Stage 2 plan's U4). A sample adapter, written to the interface, is checked against
it by the strict type check; the server time and the translation are checked here."""

from __future__ import annotations

from collections.abc import Awaitable, Callable

import pytest

from atp.contracts import Outcome
from atp.exchange import FeedEvent, RequestFailure, ServerTime, Translation, VenueAdapter
from atp.marketdata import (
    BookSnapshot,
    FundingRate,
    MarketItem,
    MarketMetadata,
    MarketRef,
    OhlcvBar,
    Stream,
    Ticker,
    Trade,
    UnavailableCause,
    VenueState,
)

NOW = 1_763_600_000_000_000_000
REFUSED = Outcome.failure(RequestFailure(UnavailableCause.REGION_REFUSED, 451))


class SampleAdapter:
    """An adapter whose venue refuses every request from this region."""

    @property
    def venue(self) -> str:
        return "sample"

    async def server_time(self) -> Outcome[ServerTime, RequestFailure]:
        return Outcome.success(ServerTime("sample", NOW, NOW - 2, NOW + 3))

    async def markets(self) -> Outcome[Translation[MarketMetadata], RequestFailure]:
        return REFUSED

    async def ticker(self, market: MarketRef) -> Outcome[Translation[Ticker], RequestFailure]:
        return REFUSED

    async def trades(self, market: MarketRef) -> Outcome[Translation[Trade], RequestFailure]:
        return REFUSED

    async def book(
        self, market: MarketRef, depth: int
    ) -> Outcome[Translation[BookSnapshot], RequestFailure]:
        return REFUSED

    async def ohlcv(
        self, market: MarketRef, interval_seconds: int
    ) -> Outcome[Translation[OhlcvBar], RequestFailure]:
        return REFUSED

    async def funding_rate(
        self, market: MarketRef
    ) -> Outcome[Translation[FundingRate], RequestFailure]:
        return REFUSED

    async def venue_state(self) -> Outcome[Translation[VenueState], RequestFailure]:
        return REFUSED

    async def stream(
        self,
        markets: tuple[MarketRef, ...],
        stream: Stream,
        deliver: Callable[[Translation[MarketItem]], Awaitable[None]],
        report: Callable[[FeedEvent], None],
    ) -> None:
        return None


ADAPTER: VenueAdapter = SampleAdapter()


@pytest.mark.req("EXA-001", "EXA-004", "EXA-006")
def test_an_adapter_written_to_the_interface_is_one() -> None:
    assert ADAPTER.venue == "sample"


@pytest.mark.req("EXA-013")
def test_a_translation_without_untranslatable_input_has_none() -> None:
    assert Translation(items=(1, 2)).untranslatable == ()


def test_a_server_time_keeps_its_three_times() -> None:
    time = ServerTime("sample", NOW, NOW - 2, NOW + 3)
    assert (time.venue_time_ns, time.sent_ns, time.received_ns) == (NOW, NOW - 2, NOW + 3)
    # The venue's clock may be anywhere: it is what the clock monitor compares.
    assert ServerTime("sample", 0, NOW, NOW).venue_time_ns == 0


@pytest.mark.parametrize(
    ("venue", "times", "message"),
    [
        ("Sample", (NOW, NOW, NOW), "names a venue"),
        ("", (NOW, NOW, NOW), "names a venue"),
        ("sample", (-1, NOW, NOW), "whole nanoseconds"),
        ("sample", (NOW, NOW, 2**63), "whole nanoseconds"),
        ("sample", (NOW, True, NOW), "whole nanoseconds"),
        ("sample", (NOW, NOW + 1, NOW), "sent before its answer"),
    ],
)
def test_a_server_time_is_checked(
    venue: str, times: tuple[int, int, int], message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        ServerTime(venue, *times)
