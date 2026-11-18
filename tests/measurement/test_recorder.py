"""Measurement points and the recorder (PERF-008, PERF-009, PERF-010, PERF-020; the Stage 2 plan's
U3)."""

from __future__ import annotations

import pytest

from atp.measurement import Kind, Path, Point, Recorder, Summary, statistics_of

NORMALIZATION = Point("normalization", Path.MARKET_DATA, "atp.marketdata")
RECEIVE = Point("receive", Path.MARKET_DATA, "atp.exchange")


class FakeClock:
    """Clocks a test moves by hand."""

    def __init__(self) -> None:
        self.monotonic = 0
        self.wall = 0

    def monotonic_ns(self) -> int:
        return self.monotonic

    def wall_ns(self) -> int:
        return self.wall


def _recorder(
    capacity: int = 100, *, reliable: bool = True
) -> tuple[Recorder, FakeClock]:
    clock = FakeClock()
    return Recorder(capacity, clock=clock, clock_reliable=lambda: reliable), clock


@pytest.mark.req("PERF-009")
def test_the_paths_are_those_stage_2_runs_on() -> None:
    assert [path.value for path in Path] == [
        "market-data",
        "arbitrage-detection",
        "directional-detection",
        "monitoring",
    ]


@pytest.mark.req("PERF-008", "PERF-010")
def test_durations_come_from_the_monotonic_clock_and_give_exact_statistics() -> None:
    recorder, clock = _recorder()
    for duration in (300, 100, 200, 400):
        started = recorder.now()
        clock.monotonic += duration
        clock.wall += 1_000_000_007  # the wall clock moving changes no duration
        recorder.duration(NORMALIZATION, started)
    samples = recorder.drain().samples
    assert [sample.value_ns for sample in samples] == [300, 100, 200, 400]
    assert {(sample.point, sample.kind) for sample in samples} == {
        (NORMALIZATION, Kind.DURATION)
    }
    assert statistics_of([sample.value_ns for sample in samples]).samples == Summary(
        count=4, p50=200, p95=None, p99=None, p99_9=None, maximum=400
    )


@pytest.mark.req("PERF-010")
def test_a_delay_measured_while_the_local_clock_drifts_is_marked_unreliable() -> None:
    reliable = [True]
    recorder = Recorder(10, clock=FakeClock(), clock_reliable=lambda: reliable[0])
    recorder.delay(RECEIVE, event_time_ns=1_000, receive_time_ns=1_250)
    reliable[0] = False
    recorder.delay(RECEIVE, event_time_ns=1_000, receive_time_ns=900)
    assert [
        (sample.kind, sample.value_ns, sample.reliable)
        for sample in recorder.drain().samples
    ] == [(Kind.DELAY, 250, True), (Kind.DELAY, -100, False)]


@pytest.mark.req("PERF-020")
def test_a_full_buffer_drops_and_counts_and_returns_at_once() -> None:
    recorder, _clock = _recorder(capacity=2)
    for _ in range(5):
        recorder.duration(NORMALIZATION, recorder.now())
    drained = recorder.drain()
    assert len(drained.samples) == 2
    assert drained.dropped == 3
    after = recorder.drain()
    assert (after.samples, after.dropped) == ((), 0)


@pytest.mark.req("PERF-020")
def test_errors_shed_work_and_queues_are_counted_by_point() -> None:
    recorder, _clock = _recorder()
    recorder.error(RECEIVE)
    recorder.error(RECEIVE)
    recorder.shed(NORMALIZATION, 3)
    recorder.shed(NORMALIZATION)
    recorder.queue(NORMALIZATION, depth=7, waited_ns=1_500)
    drained = recorder.drain()
    assert drained.errors == {RECEIVE: 2}
    assert drained.shed == {NORMALIZATION: 4}
    assert drained.queue_depths == {NORMALIZATION: 7}
    assert [(sample.kind, sample.value_ns) for sample in drained.samples] == [
        (Kind.QUEUE_DELAY, 1_500)
    ]
    assert recorder.drain().errors == {}


@pytest.mark.parametrize("capacity", [0, -1, True, 1.5])
def test_a_capacity_is_a_whole_number_of_at_least_one(capacity: object) -> None:
    with pytest.raises(ValueError, match="capacity"):
        Recorder(capacity, clock_reliable=lambda: True)  # type: ignore[arg-type]


def test_misuse_is_refused() -> None:
    recorder, clock = _recorder()
    clock.monotonic = 10
    with pytest.raises(ValueError, match="monotonic"):
        recorder.duration(NORMALIZATION, started_ns=11)
    with pytest.raises(ValueError, match="negative"):
        recorder.queue(NORMALIZATION, depth=-1, waited_ns=0)
    with pytest.raises(ValueError, match="at least 1"):
        recorder.shed(NORMALIZATION, 0)


@pytest.mark.parametrize(
    ("name", "component"),
    [
        ("Normalization", "atp.marketdata"),
        ("normal ization", "atp.marketdata"),
        ("normalization", "atp..marketdata"),
        ("normalization", ""),
    ],
)
def test_a_point_is_named_in_lowercase_words(name: str, component: str) -> None:
    with pytest.raises(ValueError, match="point"):
        Point(name, Path.MARKET_DATA, component)
