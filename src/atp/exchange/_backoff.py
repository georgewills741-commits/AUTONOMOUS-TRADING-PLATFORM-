"""Backoff: how long to wait after failures in a row (EXA-014, EXA-015)."""

from __future__ import annotations

from typing import Final

from pydantic import Field, ValidationInfo, field_validator

from atp.contracts import Contract, ContractVersion, PydanticCustomError

_INT64_MAX: Final = 2**63 - 1


class Backoff(Contract):
    """How long to wait after failures in a row: `initial_ns` after the first, twice as long
    after each further one, and never longer than `maximum_ns`, which is at least
    `initial_ns`."""

    contract_id = "atp.exchange.backoff"
    contract_version = ContractVersion(1, 0)

    initial_ns: int = Field(gt=0, le=_INT64_MAX)
    maximum_ns: int = Field(gt=0, le=_INT64_MAX)

    @field_validator("maximum_ns")
    @classmethod
    def _check_order(cls, maximum: int, info: ValidationInfo) -> int:
        initial = info.data.get("initial_ns")
        if initial is not None and maximum < initial:
            raise PydanticCustomError(
                "backoff_order", "the longest wait is at least the first"
            )
        return maximum

    def delay_ns(self, failures: int) -> int:
        """The wait after `failures` failures in a row, one or more."""
        if type(failures) is not int or failures < 1:
            msg = "a wait follows one failure or more"
            raise ValueError(msg)
        delay = self.initial_ns
        for _ in range(failures - 1):
            if delay >= self.maximum_ns:
                break
            delay *= 2
        return min(delay, self.maximum_ns)
