"""Clock-drift detection (HLT-013, HLT-014; SR-14; the Stage 2 plan's D3): drift injection."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from atp.health import ClockLimits, ClockMonitor, ClockSample, ClockVerdict, LocalClock

SECOND = 1_000_000_000
NOW = 1_763_600_000 * SECOND
LIMIT = 50_000_000
ROUND_TRIP = 2_000_000
LIMITS = ClockLimits(
    drift_limit_ns=LIMIT, sample_max_age_ns=60 * SECOND, minimum_venues=2
)


def server(
    venue: str, offset: int, received: int = NOW, round_trip: int = ROUND_TRIP
) -> ClockSample:
    """A server-time sample whose venue clock is `offset` ahead of the local one, read at the
    middle of the request."""
    sent = received - round_trip
    return ClockSample(venue, sent + round_trip // 2 + offset, sent, received)


def verdict(*samples: ClockSample, now: int = NOW) -> ClockVerdict:
    monitor = ClockMonitor(LIMITS)
    for sample in samples:
        monitor.observe(sample)
    return monitor.verdict(now)


@pytest.mark.req("HLT-013", "HLT-014")
def test_a_server_time_shows_drift_only_beyond_the_round_trip_s_doubt() -> None:
    assert not server("one", 0).ahead_by_more_than(LIMIT)
    assert not server("one", LIMIT).ahead_by_more_than(LIMIT)
    assert server("one", LIMIT + ROUND_TRIP).ahead_by_more_than(LIMIT)
    assert not server("one", -LIMIT).behind_by_more_than(LIMIT)
    assert server("one", -LIMIT - ROUND_TRIP).behind_by_more_than(LIMIT)
    # A long round trip leaves the offset too uncertain to call a drift, or to call it in time.
    doubtful = server("one", LIMIT + 1, round_trip=4 * LIMIT)
    assert not doubtful.ahead_by_more_than(LIMIT)
    assert not doubtful.within(LIMIT)
    assert server("one", 0).within(LIMIT)
    assert not server("one", LIMIT).within(LIMIT)
    # The boundaries: exactly the limit is not beyond it.
    assert ClockSample("one", NOW - LIMIT, NOW - LIMIT, NOW).within(LIMIT)
    assert ClockSample("one", NOW + LIMIT, NOW, NOW).within(LIMIT)
    assert not ClockSample("one", NOW + LIMIT, NOW, NOW).ahead_by_more_than(LIMIT)
    exactly_behind = ClockSample("one", NOW - ROUND_TRIP - LIMIT, NOW - ROUND_TRIP, NOW)
    assert not exactly_behind.behind_by_more_than(LIMIT)
    assert ClockSample(
        "one", NOW - ROUND_TRIP - LIMIT - 1, NOW - ROUND_TRIP, NOW
    ).behind_by_more_than(LIMIT)


@pytest.mark.req("HLT-013", "HLT-014")
def test_an_event_time_shows_a_venue_ahead_but_never_one_behind() -> None:
    ahead = ClockSample("one", NOW + LIMIT + 1, None, NOW)
    assert ahead.ahead_by_more_than(LIMIT)
    late = ClockSample("one", NOW - 10 * SECOND, None, NOW)
    assert not late.behind_by_more_than(LIMIT)
    assert not late.ahead_by_more_than(LIMIT)
    assert not ClockSample("one", NOW, None, NOW).within(LIMIT)


@pytest.mark.req("HLT-013")
def test_without_a_recent_sample_the_local_clock_is_undetermined() -> None:
    result = verdict()
    assert (result.local_clock, result.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset(),
    )
    assert not result.data_degraded
    assert not result.delays_reliable
    old = verdict(server("one", 10 * SECOND, received=NOW - 61 * SECOND))
    assert (old.local_clock, old.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset(),
    )
    # A sample exactly the age limit old still counts.
    edge = verdict(server("one", 10 * SECOND, received=NOW - 60 * SECOND))
    assert edge.drifting_venues == frozenset({"one"})


@pytest.mark.req("HLT-013", "HLT-014")
def test_venues_in_time_keep_the_local_clock_in_sync() -> None:
    result = verdict(server("one", 0), server("two", LIMIT // 2))
    assert result == ClockVerdict(NOW, frozenset(), LocalClock.IN_SYNC)
    assert result.delays_reliable
    assert not result.data_degraded


@pytest.mark.req("HLT-013")
def test_one_venue_drifting_among_venues_in_time_is_that_venue_s_drift() -> None:
    result = verdict(server("one", 0), server("two", SECOND), server("three", -SECOND))
    assert result.drifting_venues == frozenset({"two", "three"})
    assert result.local_clock is LocalClock.IN_SYNC
    assert result.data_degraded
    assert result.delays_reliable


@pytest.mark.req("HLT-013")
def test_every_venue_drifting_the_same_way_is_the_local_clock_s_drift() -> None:
    result = verdict(server("one", SECOND), server("two", 2 * SECOND))
    assert (result.local_clock, result.drifting_venues) == (
        LocalClock.DRIFTING,
        frozenset(),
    )
    assert result.data_degraded
    assert not result.delays_reliable
    behind = verdict(server("one", -SECOND), server("two", -SECOND))
    assert behind.local_clock is LocalClock.DRIFTING


@pytest.mark.req("HLT-013")
def test_a_drift_that_cannot_be_told_gets_both_responses() -> None:
    alone = verdict(server("one", SECOND))
    assert (alone.local_clock, alone.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset({"one"}),
    )
    assert alone.data_degraded
    assert not alone.delays_reliable
    split = verdict(server("one", SECOND), server("two", -SECOND))
    assert (split.local_clock, split.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset({"one", "two"}),
    )


@pytest.mark.req("HLT-013", "HLT-014")
def test_an_event_time_never_hides_a_server_time_s_finding() -> None:
    monitor = ClockMonitor(LIMITS)
    monitor.observe(server("one", -SECOND))
    monitor.observe(server("two", 0))
    # A later event time, which cannot show a venue behind, keeps the server time's finding.
    monitor.observe(ClockSample("one", NOW - SECOND, None, NOW + 1))
    assert monitor.verdict(NOW + 1).drifting_venues == frozenset({"one"})


@pytest.mark.req("HLT-013", "HLT-014")
def test_a_venue_drifting_by_one_sample_is_not_in_time_by_another() -> None:
    result = verdict(server("one", 0), ClockSample("one", NOW + SECOND, None, NOW))
    assert (result.local_clock, result.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset({"one"}),
    )


@pytest.mark.req("HLT-013", "HLT-014")
def test_event_times_show_a_drift_but_never_a_clock_in_time() -> None:
    unknown = verdict(ClockSample("one", NOW, None, NOW), server("two", SECOND))
    assert (unknown.local_clock, unknown.drifting_venues) == (
        LocalClock.UNDETERMINED,
        frozenset({"two"}),
    )
    ahead = verdict(
        ClockSample("one", NOW + SECOND, None, NOW),
        ClockSample("two", NOW + SECOND, None, NOW),
    )
    assert (ahead.local_clock, ahead.drifting_venues) == (
        LocalClock.DRIFTING,
        frozenset(),
    )


@pytest.mark.req("HLT-013")
def test_the_latest_sample_of_each_venue_counts() -> None:
    monitor = ClockMonitor(LIMITS)
    monitor.observe(server("one", SECOND, received=NOW))
    monitor.observe(server("one", 0, received=NOW - SECOND))  # older: ignored
    monitor.observe(server("two", 0))
    assert monitor.verdict(NOW).drifting_venues == frozenset({"one"})
    monitor.observe(server("one", 0, received=NOW + SECOND))
    assert monitor.verdict(NOW + SECOND).drifting_venues == frozenset()


@pytest.mark.parametrize(
    ("venue", "venue_time", "sent", "received"),
    [
        ("Not A Venue", NOW, None, NOW),
        ("one", -1, None, NOW),
        ("one", NOW, None, 2**63),
        ("one", True, None, NOW),
        ("one", NOW, NOW + 1, NOW),
    ],
)
def test_a_malformed_sample_is_refused(
    venue: str, venue_time: int, sent: int | None, received: int
) -> None:
    with pytest.raises(ValueError, match="clock sample|sent before"):
        ClockSample(venue, venue_time, sent, received)


def test_the_limits_need_two_venues_to_find_the_local_clock_drifting() -> None:
    with pytest.raises(ValidationError):
        ClockLimits(drift_limit_ns=LIMIT, sample_max_age_ns=SECOND, minimum_venues=1)
    with pytest.raises(ValidationError):
        ClockLimits(drift_limit_ns=0, sample_max_age_ns=SECOND, minimum_venues=2)
    with pytest.raises(ValidationError):
        ClockLimits(drift_limit_ns=LIMIT, sample_max_age_ns=0, minimum_venues=2)
