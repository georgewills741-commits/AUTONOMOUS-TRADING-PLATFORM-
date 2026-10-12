"""The contract kernel: the base every interface contract is built on.

Requirements: ARCH-025 and GOV-007 (contracts first), ARCH-026 and GOV-006 (versioning),
TEC-004 (Pydantic v2 models validated at every boundary), ARCH-041 (the idempotency key),
ARCH-042 (UNKNOWN is never SUCCESS). The conventions are in docs/architecture/contracts.md.

No system contract (market data, orders, positions, risk, capital, and so on) is defined here;
each is written on this kernel when its stage is planned.
"""

from pydantic_core import PydanticCustomError

from atp.contracts._amount import Amount
from atp.contracts._errors import (
    GENERIC_MESSAGE,
    REDACTED,
    ContractError,
    ErrorDetail,
    validation_error_details,
)
from atp.contracts._idempotency import IdempotencyKey
from atp.contracts._model import Contract
from atp.contracts._outcome import OUTCOME_RESULTS, Outcome
from atp.contracts._schemas import (
    SCHEMA_DIALECT,
    SchemaDocument,
    schema_documents,
    write_schema_files,
)
from atp.contracts._version import ContractVersion, is_compatible

__all__ = [
    "GENERIC_MESSAGE",
    "OUTCOME_RESULTS",
    "REDACTED",
    "SCHEMA_DIALECT",
    "Amount",
    "Contract",
    "ContractError",
    "ContractVersion",
    "ErrorDetail",
    "IdempotencyKey",
    "Outcome",
    "PydanticCustomError",
    "SchemaDocument",
    "is_compatible",
    "schema_documents",
    "validation_error_details",
    "write_schema_files",
]
