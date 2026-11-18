"""OpenTelemetry metrics from drained measurements (U3 of the Stage 2 plan; TEC-010, D7).

The exporter runs on the cold path: it records what a recorder drained into OpenTelemetry
instruments, which only the process's meter provider sends anywhere. Histograms approximate the
live distribution in buckets; the exact figures come from the samples themselves
(`atp.measurement.statistics_of`).
"""

from __future__ import annotations

from typing import Final

from opentelemetry.metrics import Meter

from atp.measurement._recorder import Drained, Kind, Point

# Bucket edges in nanoseconds, 1, 2, and 5 in each decade from 1 microsecond to 50 seconds: they
# set the live histograms' resolution only, never a target.
BUCKETS_NS: Final = tuple(
    step * 10**exponent for exponent in range(3, 11) for step in (1, 2, 5)
)


def _attributes(point: Point) -> dict[str, str]:
    return {
        "atp.point": point.name,
        "atp.path": point.path.value,
        "atp.component": point.component,
    }


class TelemetryExporter:
    """Records drained measurements as OpenTelemetry metrics, on the cold path."""

    def __init__(self, meter: Meter) -> None:
        self._histograms = {
            Kind.DURATION: meter.create_histogram(
                "atp.duration",
                unit="ns",
                description="Durations on the monotonic clock",
                explicit_bucket_boundaries_advisory=BUCKETS_NS,
            ),
            Kind.DELAY: meter.create_histogram(
                "atp.delay",
                unit="ns",
                description="Delays from a venue's event time to local receipt",
                explicit_bucket_boundaries_advisory=BUCKETS_NS,
            ),
            Kind.QUEUE_DELAY: meter.create_histogram(
                "atp.queue.delay",
                unit="ns",
                description="Time items waited in a queue",
                explicit_bucket_boundaries_advisory=BUCKETS_NS,
            ),
        }
        self._queue_depth = meter.create_gauge(
            "atp.queue.depth", unit="{item}", description="Items waiting in a queue"
        )
        self._errors = meter.create_counter(
            "atp.errors", unit="{error}", description="Errors, by point"
        )
        self._shed = meter.create_counter(
            "atp.shed", unit="{item}", description="Work shed under load, by point"
        )
        self._dropped = meter.create_counter(
            "atp.measurement.dropped",
            unit="{sample}",
            description="Samples dropped because the recorder's buffer was full",
        )

    def export(self, drained: Drained) -> None:
        """Record one drain's samples, counts, queue depths, and dropped samples."""
        for sample in drained.samples:
            attributes: dict[str, str | bool] = dict(_attributes(sample.point))
            if sample.kind is Kind.DELAY:
                attributes["atp.reliable"] = sample.reliable
            self._histograms[sample.kind].record(sample.value_ns, attributes)
        for point, count in drained.errors.items():
            self._errors.add(count, _attributes(point))
        for point, count in drained.shed.items():
            self._shed.add(count, _attributes(point))
        for point, depth in drained.queue_depths.items():
            self._queue_depth.set(depth, _attributes(point))
        if drained.dropped:
            self._dropped.add(drained.dropped)
