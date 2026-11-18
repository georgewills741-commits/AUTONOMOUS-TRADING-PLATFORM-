"""OpenTelemetry metrics from drained measurements (TEC-010; the Stage 2 plan's U3 and D7)."""

from __future__ import annotations

import logging

import pytest
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    HistogramDataPoint,
    InMemoryMetricReader,
    NumberDataPoint,
)

from atp.measurement import BUCKETS_NS, Path, Point, Recorder, TelemetryExporter

NORMALIZATION = Point("normalization", Path.MARKET_DATA, "atp.marketdata")
RECEIVE = Point("receive", Path.MARKET_DATA, "atp.exchange")


class StoppedClock:
    def monotonic_ns(self) -> int:
        return 0

    def wall_ns(self) -> int:
        return 0


def _points(reader: InMemoryMetricReader) -> dict[str, list[object]]:
    data = reader.get_metrics_data()
    assert data is not None
    return {
        metric.name: list(metric.data.data_points)
        for resource in data.resource_metrics
        for scope in resource.scope_metrics
        for metric in scope.metrics
    }


def _histogram(points: dict[str, list[object]], name: str) -> HistogramDataPoint:
    (point,) = points[name]
    assert isinstance(point, HistogramDataPoint)
    return point


def _number(points: dict[str, list[object]], name: str) -> NumberDataPoint:
    (point,) = points[name]
    assert isinstance(point, NumberDataPoint)
    return point


@pytest.mark.req("TEC-010", "PERF-020")
def test_drained_measurements_become_opentelemetry_metrics() -> None:
    reader = InMemoryMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    try:
        exporter = TelemetryExporter(provider.get_meter("atp.measurement.test"))
        recorder = Recorder(2, clock=StoppedClock(), clock_reliable=lambda: False)
        recorder.delay(RECEIVE, event_time_ns=0, receive_time_ns=2_000)
        recorder.queue(NORMALIZATION, depth=4, waited_ns=500)
        recorder.duration(NORMALIZATION, recorder.now())  # the buffer is full: dropped
        recorder.error(RECEIVE)
        recorder.shed(NORMALIZATION, 2)
        exporter.export(recorder.drain())
        points = _points(reader)
    finally:
        provider.shutdown()

    delay = _histogram(points, "atp.delay")
    assert (delay.count, delay.sum) == (1, 2_000)
    assert tuple(delay.explicit_bounds) == BUCKETS_NS
    assert dict(delay.attributes or {}) == {
        "atp.point": "receive",
        "atp.path": "market-data",
        "atp.component": "atp.exchange",
        "atp.reliable": False,
    }
    assert _histogram(points, "atp.queue.delay").sum == 500
    assert "atp.duration" not in points
    assert _number(points, "atp.queue.depth").value == 4
    assert _number(points, "atp.errors").value == 1
    assert _number(points, "atp.shed").value == 2
    assert _number(points, "atp.measurement.dropped").value == 1


@pytest.mark.req("TEC-010", "PERF-010")
def test_a_delay_below_zero_is_counted_never_lost(
    caplog: pytest.LogCaptureFixture,
) -> None:
    reader = InMemoryMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    try:
        exporter = TelemetryExporter(provider.get_meter("atp.measurement.test"))
        recorder = Recorder(3, clock=StoppedClock(), clock_reliable=lambda: False)
        # The clocks disagree: a delay below zero.
        recorder.delay(RECEIVE, event_time_ns=100, receive_time_ns=0)
        recorder.delay(RECEIVE, event_time_ns=0, receive_time_ns=250)
        # A delay of zero is no disagreement: the histogram holds it.
        recorder.delay(RECEIVE, event_time_ns=0, receive_time_ns=0)
        with caplog.at_level(logging.WARNING):
            exporter.export(recorder.drain())
        points = _points(reader)
    finally:
        provider.shutdown()

    delay = _histogram(points, "atp.delay")
    assert (delay.count, delay.sum) == (2, 250)
    negative = _number(points, "atp.delay.negative")
    assert negative.value == 1
    assert dict(negative.attributes or {})["atp.reliable"] is False
    # OpenTelemetry would log a warning for each negative value given to a histogram.
    assert not [
        record for record in caplog.records if record.levelno >= logging.WARNING
    ]


def test_the_buckets_rise_from_one_microsecond_and_set_no_target() -> None:
    assert BUCKETS_NS[0] == 1_000
    assert BUCKETS_NS[-1] == 50_000_000_000
    assert list(BUCKETS_NS) == sorted(set(BUCKETS_NS))
