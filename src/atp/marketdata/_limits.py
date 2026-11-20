"""The limits market-data validation applies (the Stage 2 plan's D3).

Each is an IMPLEMENTATION CHOICE value, set from the first live measurements and given to the
validator by the code that runs the market-data path; none has a default here. They mark data in
Stage 2 only, and are never presented as V-17, each stream's freshness limit, a HARD LIMIT that
the owner sets in policy once CORE TRADING FOUNDATION builds the Policy System (MKD-006; the
plan's D2).
"""

from __future__ import annotations

from decimal import Decimal

from pydantic import Field, ValidationInfo, field_validator

from atp.contracts import Amount, Contract, ContractVersion, PydanticCustomError
from atp.marketdata._contracts import _INT64_MAX, Stream


class StreamLimits(Contract):
    """A stream's freshness limits (MKD-006, MKD-012): an item older than `stale_after_ns` is
    STALE, and one older than `invalid_after_ns`, which is later, is INVALID."""

    contract_id = "atp.marketdata.stream-limits"
    contract_version = ContractVersion(1, 0)

    stream: Stream
    stale_after_ns: int = Field(gt=0, le=_INT64_MAX)
    invalid_after_ns: int = Field(gt=0, le=_INT64_MAX)

    @field_validator("invalid_after_ns")
    @classmethod
    def _check_order(cls, invalid: int, info: ValidationInfo) -> int:
        stale = info.data.get("stale_after_ns")
        if stale is not None and invalid <= stale:
            raise PydanticCustomError(
                "limit_order", "an item turns invalid only after it turns stale"
            )
        return invalid


def _check_fraction(fraction: Decimal) -> Decimal:
    if fraction <= 0:
        raise PydanticCustomError(
            "fraction_not_positive", "a deviation limit is a fraction above zero"
        )
    return fraction


class ValidationLimits(Contract):
    """The limits of the market-data checks (MKD-008, MKD-012, MKD-013), one set per process.

    - `streams`: each stream's freshness limits, every stream exactly once.
    - `max_event_ahead_ns`: how far a venue's event time may be ahead of its local receipt
      before the time is invalid.
    - `duplicate_memory`: how many evidence identifiers are remembered to find duplicates; the
      oldest is forgotten first.
    - `outlier_limit`: the fraction by which a price may differ from its market's reference
      price before it is an outlier; `outlier_confirmations`: how many outliers in a row a run
      holds before the next outlier within that fraction of each of them is accepted.
    - `inconsistency_limit`: the fraction by which a price may differ from every other venue's
      price for the same market before it is inconsistent; `minimum_other_venues`: how many
      other venues' valid prices the comparison needs.
    """

    contract_id = "atp.marketdata.validation-limits"
    contract_version = ContractVersion(1, 0)

    streams: tuple[StreamLimits, ...]
    max_event_ahead_ns: int = Field(ge=0, le=_INT64_MAX)
    duplicate_memory: int = Field(gt=0, le=_INT64_MAX)
    outlier_limit: Amount
    outlier_confirmations: int = Field(ge=1, le=_INT64_MAX)
    inconsistency_limit: Amount
    minimum_other_venues: int = Field(ge=1, le=_INT64_MAX)

    @field_validator("streams")
    @classmethod
    def _check_streams(
        cls, streams: tuple[StreamLimits, ...]
    ) -> tuple[StreamLimits, ...]:
        named = [limits.stream for limits in streams]
        if sorted(named, key=lambda stream: stream.value) != sorted(
            Stream, key=lambda stream: stream.value
        ):
            raise PydanticCustomError(
                "streams_incomplete", "every stream has its limits, each once"
            )
        return streams

    @field_validator("outlier_limit", "inconsistency_limit")
    @classmethod
    def _check_limit(cls, fraction: Decimal) -> Decimal:
        return _check_fraction(fraction)

    def for_stream(self, stream: Stream) -> StreamLimits:
        """The freshness limits of `stream`."""
        (limits,) = [limits for limits in self.streams if limits.stream is stream]
        return limits
