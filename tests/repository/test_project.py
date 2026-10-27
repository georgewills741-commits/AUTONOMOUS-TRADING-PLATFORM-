"""The project definition (TEC-001, TEC-009, GOV-012; U1 and U6 of the Stage 1 plan).

Read from `pyproject.toml` and the repository's layout: the language and its strict type check,
the locked tools, and a test package for every package of the platform.
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]


def _project() -> dict[str, Any]:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


@pytest.mark.req("TEC-001")
def test_the_platform_needs_python_3_12_and_strict_type_checks() -> None:
    project = _project()
    assert project["project"]["requires-python"] == ">=3.12"
    assert sys.version_info >= (3, 12)
    assert project["tool"]["mypy"]["strict"] is True


@pytest.mark.req("TEC-009")
def test_the_tools_and_their_versions_are_locked() -> None:
    project = _project()
    assert (ROOT / "uv.lock").is_file()
    assert project["tool"]["uv"]["required-version"].startswith("==")
    tools = {
        requirement.split(">")[0].split("=")[0].split("<")[0]
        for requirement in project["dependency-groups"]["dev"]
    }
    assert {"hypothesis", "mypy", "pytest", "ruff"} <= tools


@pytest.mark.req("GOV-012")
def test_every_package_of_the_platform_has_its_tests() -> None:
    packages = {
        path.name
        for path in (ROOT / "src" / "atp").iterdir()
        if path.is_dir() and path.name != "__pycache__"
    }
    assert packages
    for package in sorted(packages):
        assert any((ROOT / "tests" / package).glob("test_*.py")), package
