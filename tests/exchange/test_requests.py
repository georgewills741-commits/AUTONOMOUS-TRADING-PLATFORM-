"""Each request's result as an outcome (ARCH-042; EXA-007, EXA-014, EXA-015; the Stage 2 plan's
U4): TIMEOUT for a timeout, UNKNOWN for an ambiguous answer."""

from __future__ import annotations

import pytest

from atp.contracts import Outcome
from atp.exchange import (
    Answered,
    Interrupted,
    NoAnswerInTime,
    NotSent,
    RequestFailure,
    TransportResult,
    request_outcome,
)
from atp.marketdata import UnavailableCause


def kind(outcome: Outcome[bytes, RequestFailure]) -> str:
    return outcome.fold(
        on_success=lambda _: "success",
        on_failure=lambda failure: f"failure {failure.cause.value}",
        on_timeout=lambda: "timeout",
        on_unknown=lambda: "unknown",
    )


def failure(outcome: Outcome[bytes, RequestFailure]) -> RequestFailure:
    found = outcome.fold(
        on_success=lambda _: None,
        on_failure=lambda error: error,
        on_timeout=lambda: None,
        on_unknown=lambda: None,
    )
    assert found is not None
    return found


@pytest.mark.req("EXA-015")
@pytest.mark.parametrize("status", [200, 201, 204, 299])
def test_a_complete_2xx_answer_is_a_success_with_its_body(status: int) -> None:
    outcome = request_outcome(Answered(status, b"[]"))
    assert (
        outcome.fold(
            on_success=lambda body: body,
            on_failure=lambda _: None,
            on_timeout=lambda: None,
            on_unknown=lambda: None,
        )
        == b"[]"
    )


@pytest.mark.req("EXA-014")
@pytest.mark.parametrize("status", [418, 429])
def test_a_rate_limit_refusal_is_a_failure_with_the_wait_asked_for(status: int) -> None:
    refused = failure(request_outcome(Answered(status, b"", retry_after_ns=5)))
    assert refused == RequestFailure(UnavailableCause.RATE_LIMITED, status, 5)


@pytest.mark.req("EXA-007")
def test_a_region_refusal_is_a_failure_of_its_own() -> None:
    refused = failure(request_outcome(Answered(451, b"")))
    assert refused == RequestFailure(UnavailableCause.REGION_REFUSED, 451)


@pytest.mark.req("EXA-015")
@pytest.mark.parametrize("status", [400, 403, 404, 417, 419, 428, 430, 450, 452, 499])
def test_another_4xx_is_the_venue_s_refusal(status: int) -> None:
    refused = failure(request_outcome(Answered(status, b"")))
    assert refused == RequestFailure(UnavailableCause.VENUE_ERROR, status)


@pytest.mark.req("EXA-015")
@pytest.mark.parametrize(
    "status", [100, 199, 300, 301, 304, 399, 500, 502, 503, 504, 599, 600, 999]
)
def test_any_other_status_is_an_ambiguous_answer(status: int) -> None:
    assert kind(request_outcome(Answered(status, b"{}"))) == "unknown"


@pytest.mark.req("EXA-015")
@pytest.mark.parametrize(
    ("result", "expected"),
    [
        (NotSent(), "failure connection-failed"),
        (NoAnswerInTime(), "timeout"),
        (Interrupted(), "unknown"),
    ],
)
def test_a_request_without_a_complete_answer(
    result: TransportResult, expected: str
) -> None:
    assert kind(request_outcome(result)) == expected


@pytest.mark.parametrize("status", [99, 1000, -200, True, 200.0])
def test_an_answer_s_status_has_three_digits(status: object) -> None:
    with pytest.raises(ValueError, match="three digits"):
        Answered(status, b"")  # type: ignore[arg-type]


def test_an_answer_s_body_is_bytes() -> None:
    with pytest.raises(TypeError, match="bytes"):
        Answered(200, "[]")  # type: ignore[arg-type]


@pytest.mark.parametrize("wait", [-1, True, 1.5, 2**63])
def test_a_wait_asked_for_is_whole_nanoseconds_from_zero(wait: object) -> None:
    with pytest.raises(ValueError, match="whole nanoseconds"):
        Answered(429, b"", retry_after_ns=wait)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="whole nanoseconds"):
        RequestFailure(UnavailableCause.RATE_LIMITED, 429, wait)  # type: ignore[arg-type]


def test_a_timeout_is_never_a_failure() -> None:
    with pytest.raises(ValueError, match="outcome of its own"):
        RequestFailure(UnavailableCause.TIMEOUT)


def test_a_failure_s_cause_is_an_unavailable_cause() -> None:
    with pytest.raises(TypeError, match="UnavailableCause"):
        RequestFailure("rate-limited")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="three digits"):
        RequestFailure(UnavailableCause.VENUE_ERROR, 42)
