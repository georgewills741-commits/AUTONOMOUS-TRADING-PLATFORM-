"""Committed contract schemas (ARCH-026, GOV-006, GOV-007): a schema never changes without a new version."""

from __future__ import annotations

import importlib
import re
import types
from pathlib import Path

import pytest
from pydantic import Field

from atp.contracts import (
    SCHEMA_DIALECT,
    Amount,
    Contract,
    ContractVersion,
    SchemaDocument,
    _schemas,
    schema_documents,
    write_schema_files,
)

CONTRACTS_ROOT = Path(__file__).resolve().parents[2] / "contracts"


def test_every_contract_schema_is_committed_and_unchanged() -> None:
    for document in schema_documents():
        committed = CONTRACTS_ROOT / document.relative_path
        assert committed.is_file(), (
            f"{document.relative_path} is not committed: write it with write_schema_files"
        )
        assert committed.read_text(encoding="utf-8") == document.text(), (
            f"the schema of {document.contract_id} {document.version} changed without a "
            "version change: give the contract a new version"
        )


def test_every_committed_schema_belongs_to_a_known_contract() -> None:
    known = {document.contract_id for document in schema_documents()}
    for path in CONTRACTS_ROOT.rglob("*"):
        if path.is_file():
            assert path.name.endswith(".schema.json"), path
            assert path.parent.name in known, path


def test_a_schema_document_has_its_path_and_text() -> None:
    document = SchemaDocument("atp.example", ContractVersion(2, 1), {"b": 1, "a": "é"})
    assert document.relative_path == Path("atp.example") / "2.1.schema.json"
    assert document.text() == '{\n  "a": "é",\n  "b": 1\n}\n'


def test_the_kernel_schemas_are_present() -> None:
    identities = {document.contract_id for document in schema_documents()}
    assert {"atp.amount", "atp.idempotency-key", "atp.outcome"} <= identities


def test_each_schema_names_its_dialect_identity_and_version() -> None:
    for document in schema_documents():
        assert re.fullmatch(r"[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*", document.contract_id)
        assert document.schema["$schema"] == SCHEMA_DIALECT
        assert document.schema["$id"] == f"{document.contract_id}/{document.version}"


def test_the_amount_schema_refuses_json_numbers() -> None:
    (amount,) = (d for d in schema_documents() if d.contract_id == "atp.amount")
    assert amount.schema["type"] == "string"
    assert '"number"' not in amount.text()
    assert '"integer"' not in amount.text()


class _First(Contract):
    contract_id = "test.duplicate"
    contract_version = ContractVersion(1, 0)


class _Second(Contract):
    contract_id = "test.duplicate"
    contract_version = ContractVersion(1, 0)


class _Lot(Contract):
    contract_id = "test.lot"
    contract_version = ContractVersion(1, 0)
    quantity: Amount = Field(gt=0)


def test_an_amount_in_a_contract_schema_refers_to_the_amount_definition(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # `Amount` is a `type` alias, so a contract's schema refers to one definition of it, the
    # committed `atp.amount` schema without its header. A bound is written beside the reference
    # under Pydantic's name for it, which is not a JSON Schema keyword: JSON Schema's bounds
    # apply to numbers, and an amount is a string. The contract enforces the bound.
    monkeypatch.setattr(_schemas, "_platform_contracts", lambda: [_Lot])
    documents = {
        document.contract_id: document.schema for document in schema_documents()
    }
    lot, amount = documents["test.lot"], documents["atp.amount"]
    header = {"$schema", "$id", "title"}
    assert lot["$defs"]["Amount"] == {
        key: value for key, value in amount.items() if key not in header
    }
    assert lot["properties"]["quantity"] == {"$ref": "#/$defs/Amount", "gt": 0}


def test_every_platform_module_is_imported_before_schemas_are_collected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    imported: list[str] = []
    original = importlib.import_module

    def record(name: str, package: str | None = None) -> types.ModuleType:
        imported.append(name)
        return original(name, package)

    monkeypatch.setattr(importlib, "import_module", record)
    schema_documents()
    assert {"atp.numeric._amount", "atp.contracts._outcome"} <= set(imported)


def test_two_contracts_with_one_identity_are_refused(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Contracts defined in tests are not the platform's, so the platform's list is replaced.
    monkeypatch.setattr(_schemas, "_platform_contracts", lambda: [_First, _Second])
    with pytest.raises(ValueError, match="test.duplicate"):
        schema_documents()


def test_writing_never_overwrites_a_changed_version(tmp_path: Path) -> None:
    written = write_schema_files(tmp_path)
    assert written
    assert write_schema_files(tmp_path) == []
    changed = written[0]
    changed.write_text(
        changed.read_text(encoding="utf-8").replace('"title"', '"titel"'),
        encoding="utf-8",
    )
    with pytest.raises(FileExistsError, match="without a version change"):
        write_schema_files(tmp_path)
