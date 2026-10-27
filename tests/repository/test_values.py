"""The values the code uses are those the values register records (ARCH-018; V-40, V-41).

Read from docs/requirements/values-register.md, its "Current value" column, so that a value
changed in the code or in the register alone fails.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from atp.config import MAXIMUM_DOCUMENT_SIZE
from atp.numeric import PRECISION

REGISTER = (
    Path(__file__).resolve().parents[2] / "docs" / "requirements" / "values-register.md"
)


def _current_value(value_id: str) -> int:
    """The current value of one row of the values register, as an integer."""
    lines = REGISTER.read_text(encoding="utf-8").splitlines()
    header = next(line for line in lines if line.startswith("| ID |"))
    column = [cell.strip() for cell in header.split("|")].index("Current value")
    (row,) = [line for line in lines if line.startswith(f"| {value_id} |")]
    return int(row.split("|")[column].strip().replace(",", ""))


@pytest.mark.req("ARCH-018")
def test_the_code_uses_the_values_of_the_values_register() -> None:
    assert PRECISION == _current_value("V-40")
    assert MAXIMUM_DOCUMENT_SIZE == _current_value("V-41")
