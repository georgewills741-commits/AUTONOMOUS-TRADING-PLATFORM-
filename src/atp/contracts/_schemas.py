"""Committed JSON schemas of the contracts (ARCH-026, GOV-006, GOV-007; docs/architecture/contracts.md).

Each contract's schema is committed under `contracts/<contract id>/<version>.schema.json`. The
tests compare every committed schema with the one the code produces, so a contract whose schema
changes without a new version fails. `write_schema_files` adds the file of a new version and
refuses to overwrite a committed version with different content.
"""

from __future__ import annotations

import importlib
import json
import pkgutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final

from pydantic import TypeAdapter

import atp
from atp.contracts._amount import Amount
from atp.contracts._idempotency import IdempotencyKey
from atp.contracts._model import Contract
from atp.contracts._outcome import Outcome
from atp.contracts._version import ContractVersion

SCHEMA_DIALECT: Final = "https://json-schema.org/draft/2020-12/schema"

# The kernel's own types, which every later contract uses. Each has an identity and a version
# like a contract model.
_KERNEL_TYPES: Final[tuple[tuple[str, ContractVersion, Any], ...]] = (
    ("atp.amount", ContractVersion(1, 0), Amount),
    ("atp.idempotency-key", ContractVersion(1, 0), IdempotencyKey),
    ("atp.outcome", ContractVersion(1, 0), Outcome[Any, Any]),
)


@dataclass(frozen=True, slots=True)
class SchemaDocument:
    """One contract's JSON schema at one version."""

    contract_id: str
    version: ContractVersion
    schema: dict[str, Any]

    @property
    def relative_path(self) -> Path:
        return Path(self.contract_id) / f"{self.version}.schema.json"

    def text(self) -> str:
        return (
            json.dumps(self.schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        )


def _document(contract_id: str, version: ContractVersion, type_: Any) -> SchemaDocument:
    generated = TypeAdapter(type_).json_schema(mode="validation")
    header = {
        "$schema": SCHEMA_DIALECT,
        "$id": f"{contract_id}/{version}",
        "title": contract_id,
    }
    return SchemaDocument(contract_id, version, header | generated)


def import_platform_modules() -> list[str]:
    """Import every module of the `atp` package, so that every contract it defines is known."""
    names = [
        module.name for module in pkgutil.walk_packages(atp.__path__, prefix="atp.")
    ]
    for name in names:
        importlib.import_module(name)
    return names


def _platform_contracts() -> list[type[Contract]]:
    import_platform_modules()
    found: list[type[Contract]] = []
    pending = list(Contract.__subclasses__())
    while pending:
        model = pending.pop()
        pending.extend(model.__subclasses__())
        if model.__module__.startswith("atp."):
            found.append(model)
    return found


def schema_documents() -> tuple[SchemaDocument, ...]:
    """The schema of every kernel type and every contract the platform's modules define."""
    documents = [_document(*entry) for entry in _KERNEL_TYPES]
    documents.extend(
        _document(model.contract_id, model.contract_version, model)
        for model in _platform_contracts()
    )
    identities = [document.contract_id for document in documents]
    duplicates = sorted(
        {identity for identity in identities if identities.count(identity) > 1}
    )
    if duplicates:
        msg = f"contract identities declared more than once: {', '.join(duplicates)}"
        raise ValueError(msg)
    return tuple(sorted(documents, key=lambda document: document.contract_id))


def write_schema_files(directory: Path) -> list[Path]:
    """Write the schema file of each contract version not yet committed under `directory`.

    A committed file whose content differs from the code's schema is never overwritten: that
    is a change without a new version, which must get one.
    """
    written: list[Path] = []
    for document in schema_documents():
        path = directory / document.relative_path
        if path.exists():
            if path.read_text(encoding="utf-8") != document.text():
                msg = (
                    f"the schema of {document.contract_id} {document.version} changed without "
                    "a version change; give the contract a new version"
                )
                raise FileExistsError(msg)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(document.text(), encoding="utf-8")
        written.append(path)
    return written
