"""The validation limits (the Stage 2 plan's D3): checked before any check uses them."""

from __future__ import annotations

import json

import pytest

from atp.contracts import ContractError
from atp.marketdata import Stream, StreamLimits, ValidationLimits

SECOND = 1_000_000_000
STREAMS = [
    {"stream": stream.value, "stale_after_ns": SECOND, "invalid_after_ns": 2 * SECOND}
    for stream in Stream
]
VALID = {
    "streams": STREAMS,
    "max_event_ahead_ns": 0,
    "duplicate_memory": 1,
    "outlier_limit": "0.1",
    "outlier_confirmations": 1,
    "inconsistency_limit": "0.05",
    "minimum_other_venues": 1,
}


def _types(data: dict[str, object]) -> list[str]:
    with pytest.raises(ContractError) as refused:
        ValidationLimits.from_json(json.dumps(data))
    return [detail.type for detail in refused.value.details]


@pytest.mark.req("MKD-006")
def test_the_limits_are_read_and_each_stream_s_found() -> None:
    limits = ValidationLimits.from_json(json.dumps(VALID))
    assert limits.for_stream(Stream.BOOK).invalid_after_ns == 2 * SECOND


@pytest.mark.req("MKD-006", "MKD-012")
@pytest.mark.parametrize("invalid", [SECOND, SECOND - 1])
def test_a_stream_turns_invalid_only_after_it_turns_stale(invalid: int) -> None:
    with pytest.raises(ContractError) as refused:
        StreamLimits.from_json(
            json.dumps(
                {
                    "stream": "ticker",
                    "stale_after_ns": SECOND,
                    "invalid_after_ns": invalid,
                }
            )
        )
    assert [detail.type for detail in refused.value.details] == ["limit_order"]


@pytest.mark.req("MKD-006")
@pytest.mark.parametrize("streams", [STREAMS[1:], [*STREAMS, STREAMS[0]]])
def test_every_stream_has_its_limits_each_once(
    streams: list[dict[str, object]],
) -> None:
    assert _types({**VALID, "streams": streams}) == ["streams_incomplete"]


@pytest.mark.req("MKD-008")
@pytest.mark.parametrize("field", ["outlier_limit", "inconsistency_limit"])
@pytest.mark.parametrize("fraction", ["0", "-0.1"])
def test_a_deviation_limit_is_a_fraction_above_zero(field: str, fraction: str) -> None:
    assert _types({**VALID, field: fraction}) == ["fraction_not_positive"]


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("max_event_ahead_ns", -1),
        ("duplicate_memory", 0),
        ("outlier_confirmations", 0),
        ("minimum_other_venues", 0),
    ],
)
def test_a_count_or_duration_out_of_range_is_refused(field: str, value: int) -> None:
    assert _types({**VALID, field: value})


@pytest.mark.req("MKD-006")
@pytest.mark.parametrize("field", ["stale_after_ns", "invalid_after_ns"])
def test_a_stream_limit_of_zero_is_refused_alone(field: str) -> None:
    limits = {
        "stream": "ticker",
        "stale_after_ns": SECOND,
        "invalid_after_ns": 2 * SECOND,
        field: 0,
    }
    with pytest.raises(ContractError) as refused:
        StreamLimits.from_json(json.dumps(limits))
    assert [detail.type for detail in refused.value.details] == ["greater_than"]
