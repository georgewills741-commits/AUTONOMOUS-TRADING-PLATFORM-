"""Each request's result as an outcome (ARCH-042; the Stage 2 plan's U4).

A transport reports what happened to one request as a `TransportResult`; `request_outcome`
gives its outcome: SUCCESS with the body of a complete 2xx answer; FAILURE with a
`RequestFailure` when the venue refused the request, or when it was never sent; TIMEOUT when no
complete answer came in time; UNKNOWN when the answer is ambiguous, a 5xx, a status outside
2xx and 4xx, or a connection broken after the request was sent. A venue's own signals, such as
an error code in a 2xx body, are read by its adapter, which may refine a FAILURE's cause from
them; it never turns a TIMEOUT or an UNKNOWN into a SUCCESS.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, assert_never

from atp.contracts import Outcome
from atp.marketdata import UnavailableCause

_INT64_MAX: Final = 2**63 - 1

RATE_LIMIT_STATUSES: Final = frozenset({418, 429})
"""The statuses of a rate-limit refusal: 429 Too Many Requests, and 418, which some venues send
when they ban an address that kept sending past a 429."""

REGION_REFUSAL_STATUS: Final = 451
"""Unavailable For Legal Reasons: the venue refuses the request from where it was sent."""


def _check_wait(retry_after_ns: int | None) -> None:
    if retry_after_ns is not None and (
        type(retry_after_ns) is not int or not 0 <= retry_after_ns <= _INT64_MAX
    ):
        msg = "a wait the venue asks for is whole nanoseconds, from zero"
        raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class Answered:
    """The venue's complete answer: its HTTP status, its body, and how long it asked to wait
    before the next request, when it said (`Retry-After`)."""

    status: int
    body: bytes
    retry_after_ns: int | None = None

    def __post_init__(self) -> None:
        if type(self.status) is not int or not 100 <= self.status <= 999:
            msg = "an HTTP status has three digits"
            raise ValueError(msg)
        if type(self.body) is not bytes:
            msg = "an answer's body is bytes"
            raise TypeError(msg)
        _check_wait(self.retry_after_ns)


@dataclass(frozen=True, slots=True)
class NotSent:
    """The request never reached the venue: its name was not resolved, the connection was
    refused, or the venue's certificate failed TLS verification."""


@dataclass(frozen=True, slots=True)
class NoAnswerInTime:
    """The request was sent, and no complete answer came before its deadline."""


@dataclass(frozen=True, slots=True)
class Interrupted:
    """The request was sent, and the connection broke before a complete answer came."""


type TransportResult = Answered | NotSent | NoAnswerInTime | Interrupted
"""What happened to one request, as its transport reports it."""


@dataclass(frozen=True, slots=True)
class RequestFailure:
    """Why a request was not done, confirmed: the cause, the venue's HTTP status when it
    answered with one, and the wait it asked for when it said. A timeout is never a failure: it
    is an outcome of its own, since the request may have been done."""

    cause: UnavailableCause
    status: int | None = None
    retry_after_ns: int | None = None

    def __post_init__(self) -> None:
        if type(self.cause) is not UnavailableCause:
            msg = "a failure's cause is an UnavailableCause"
            raise TypeError(msg)
        if self.cause is UnavailableCause.TIMEOUT:
            msg = "a timeout is an outcome of its own, not a failure"
            raise ValueError(msg)
        if self.status is not None and (
            type(self.status) is not int or not 100 <= self.status <= 999
        ):
            msg = "an HTTP status has three digits"
            raise ValueError(msg)
        _check_wait(self.retry_after_ns)


def request_outcome(result: TransportResult) -> Outcome[bytes, RequestFailure]:
    """The outcome of one request, from what its transport reports."""
    if isinstance(result, Answered):
        status = result.status
        if 200 <= status <= 299:
            return Outcome.success(result.body)
        if status in RATE_LIMIT_STATUSES:
            return Outcome.failure(
                RequestFailure(
                    UnavailableCause.RATE_LIMITED, status, result.retry_after_ns
                )
            )
        if status == REGION_REFUSAL_STATUS:
            return Outcome.failure(
                RequestFailure(UnavailableCause.REGION_REFUSED, status)
            )
        if 400 <= status <= 499:
            return Outcome.failure(RequestFailure(UnavailableCause.VENUE_ERROR, status))
        return Outcome.unknown()
    if isinstance(result, NotSent):
        return Outcome.failure(RequestFailure(UnavailableCause.CONNECTION_FAILED))
    if isinstance(result, NoAnswerInTime):
        return Outcome.timeout()
    if isinstance(result, Interrupted):
        return Outcome.unknown()
    assert_never(result)
