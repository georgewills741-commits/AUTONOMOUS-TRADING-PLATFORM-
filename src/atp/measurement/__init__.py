"""Performance measurement: named points, a recorder that never waits, exact statistics, and
OpenTelemetry metrics (U3 of the Stage 2 plan).

Requirements: PERF-008, PERF-009, PERF-010, PERF-018, PERF-020, TEC-010. Each point names what it
measures, its latency path, and its component, so latency is decomposed (PERF-008) and kept per
path (PERF-009) and per service (PERF-018); the recorder measures durations on the monotonic
clock and delays from venues' event times, marking those taken while the local clock drifts
(PERF-010), and counts errors, shed work, and queues (PERF-020); figures are exact, a percentile
reported only with enough samples (PERF-010); the exporter turns them into OpenTelemetry metrics
(TEC-010). No target is set here: targets come from measured evidence, set where the
requirements say (PERF-018, SR-41). Built first, so that the later units are measured as they
are built.
"""

from atp.measurement._recorder import (
    Clock,
    Drained,
    Kind,
    Path,
    Point,
    Recorder,
    Sample,
    SystemClock,
)
from atp.measurement._statistics import (
    PERCENTILES,
    Statistics,
    Summary,
    percentile,
    statistics_of,
    summarize,
)
from atp.measurement._telemetry import BUCKETS_NS, TelemetryExporter

__all__ = [
    "BUCKETS_NS",
    "PERCENTILES",
    "Clock",
    "Drained",
    "Kind",
    "Path",
    "Point",
    "Recorder",
    "Sample",
    "Statistics",
    "Summary",
    "SystemClock",
    "TelemetryExporter",
    "percentile",
    "statistics_of",
    "summarize",
]
