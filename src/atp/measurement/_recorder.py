"""Measurement points and the recorder (U3 of the Stage 2 plan; PERF-008, PERF-009, PERF-020)."""

from __future__ import annotations

import enum
import re
import time
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Final, Protocol

_POINT_NAME: Final = re.compile(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*")
_COMPONENT: Final = re.compile(r"[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*")


class Path(enum.Enum):
    """A latency path of PERF-009 that Stage 2's code runs on: market data, the detection part of
    the arbitrage and directional paths, and monitoring. Each has its own budget (PERF-009):
    every sample carries its point's path, and every metric is labelled with it, so that figures
    can be kept per path."""

    MARKET_DATA = "market-data"
    ARBITRAGE_DETECTION = "arbitrage-detection"
    DIRECTIONAL_DETECTION = "directional-detection"
    MONITORING = "monitoring"


class Kind(enum.Enum):
    """What a sample measures: a duration on the monotonic clock, a delay from a venue's event
    time to its local receipt on the wall clock, or the time an item waited in a queue."""

    DURATION = "duration"
    DELAY = "delay"
    QUEUE_DELAY = "queue-delay"


@dataclass(frozen=True, slots=True)
class Point:
    """A named place where something is measured, on one path, in one component (PERF-008's
    decomposition): for example `normalization` on the market-data path in `atp.marketdata`."""

    name: str
    path: Path
    component: str

    def __post_init__(self) -> None:
        if type(self.name) is not str or not _POINT_NAME.fullmatch(self.name):
            msg = "a point's name is lowercase words joined by dots"
            raise ValueError(msg)
        if type(self.path) is not Path:
            msg = "a point's path is a Path"
            raise TypeError(msg)
        if type(self.component) is not str or not _COMPONENT.fullmatch(self.component):
            msg = "a point's component is a module path"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class Sample:
    """One measurement, in nanoseconds. `reliable` is false for a delay measured while the local
    clock's drift was beyond its limit (the Stage 2 plan's D3), and true otherwise."""

    point: Point
    kind: Kind
    value_ns: int
    reliable: bool


class Clock(Protocol):
    """The clocks of measurement, injected in tests: a recorder reads `monotonic_ns` for
    durations; `wall_ns` is the clock callers read for the receipt times they pass to
    `delay`."""

    def monotonic_ns(self) -> int:
        """Nanoseconds on a clock that never goes back, for durations."""
        ...

    def wall_ns(self) -> int:
        """Nanoseconds since the Unix epoch, UTC, for comparison with a venue's times."""
        ...


class SystemClock:
    """The process's clocks: `time.monotonic_ns` and `time.time_ns`."""

    def monotonic_ns(self) -> int:
        return time.monotonic_ns()

    def wall_ns(self) -> int:
        return time.time_ns()


@dataclass(frozen=True, slots=True)
class Drained:
    """What a recorder held when it was drained: its samples in the order they were recorded,
    the samples dropped because its buffer was full, and the counts and queue depths kept
    since the last drain, by point."""

    samples: tuple[Sample, ...]
    dropped: int
    errors: dict[Point, int] = field(default_factory=dict)
    shed: dict[Point, int] = field(default_factory=dict)
    queue_depths: dict[Point, int] = field(default_factory=dict)


class Recorder:
    """Records measurements on the hot path without ever waiting (U3; PERF-010, PERF-020).

    Samples go into a buffer of a fixed capacity; when it is full a sample is dropped and
    counted, and the call returns at once. The cold path drains the buffer, to export metrics
    and, in baseline runs, to keep every sample. A recorder is used from the platform process's
    event loop (TEC-008) and is not shared between threads. `clock_reliable` tells whether the
    local clock's drift is within its limit: delays measured when it is not are kept, marked
    unreliable. A recorder sets no target and judges no figure (PERF-018).
    """

    def __init__(
        self,
        capacity: int,
        *,
        clock_reliable: Callable[[], bool],
        clock: Clock | None = None,
    ) -> None:
        if type(capacity) is not int or capacity < 1:
            msg = "a recorder's capacity is a whole number of samples, at least 1"
            raise ValueError(msg)
        self._capacity = capacity
        self._clock: Clock = SystemClock() if clock is None else clock
        self._clock_reliable = clock_reliable
        self._samples: deque[Sample] = deque()
        self._dropped = 0
        self._errors: dict[Point, int] = {}
        self._shed: dict[Point, int] = {}
        self._queue_depths: dict[Point, int] = {}

    def now(self) -> int:
        """The monotonic clock, in nanoseconds: the start of a duration."""
        return self._clock.monotonic_ns()

    def duration(self, point: Point, started_ns: int) -> None:
        """Record the time from `started_ns`, read with `now()`, until now."""
        value = self._clock.monotonic_ns() - started_ns
        if value < 0:
            msg = "a duration starts from this recorder's monotonic clock"
            raise ValueError(msg)
        self._put(Sample(point, Kind.DURATION, value, reliable=True))

    def delay(self, point: Point, event_time_ns: int, receive_time_ns: int) -> None:
        """Record the delay from a venue's event time to the item's local receipt, both on the
        wall clock: negative when the clocks disagree, and marked unreliable while the local
        clock's drift is beyond its limit."""
        value = receive_time_ns - event_time_ns
        self._put(Sample(point, Kind.DELAY, value, reliable=self._clock_reliable()))

    def queue(self, point: Point, depth: int, waited_ns: int) -> None:
        """Record a queue's depth now and the time an item just taken from it waited."""
        if depth < 0 or waited_ns < 0:
            msg = "a queue's depth and an item's wait are not negative"
            raise ValueError(msg)
        self._queue_depths[point] = depth
        self._put(Sample(point, Kind.QUEUE_DELAY, waited_ns, reliable=True))

    def error(self, point: Point) -> None:
        """Count one error at a point (PERF-020's error rate)."""
        self._errors[point] = self._errors.get(point, 0) + 1

    def shed(self, point: Point, count: int = 1) -> None:
        """Count work shed at a point under load (PERF-020's backpressure)."""
        if count < 1:
            msg = "shed work is counted in whole items, at least 1"
            raise ValueError(msg)
        self._shed[point] = self._shed.get(point, 0) + count

    def drain(self) -> Drained:
        """Take everything recorded since the last drain, and start again from empty."""
        drained = Drained(
            tuple(self._samples),
            self._dropped,
            self._errors,
            self._shed,
            self._queue_depths,
        )
        self._samples = deque()
        self._dropped = 0
        self._errors = {}
        self._shed = {}
        self._queue_depths = {}
        return drained

    def _put(self, sample: Sample) -> None:
        if len(self._samples) < self._capacity:
            self._samples.append(sample)
        else:
            self._dropped += 1
