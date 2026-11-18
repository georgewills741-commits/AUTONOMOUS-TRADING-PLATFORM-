"""The values the code uses are those the values register records (ARCH-018; V-40, V-41, V-45,
V-46).

Read from docs/requirements/values-register.md, its "Current value" column, so that a value
changed in the code or in the register alone fails.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from atp.config import MAXIMUM_DOCUMENT_SIZE
from atp.measurement import BUCKETS_NS, PERCENTILES, percentile
from atp.numeric import PRECISION

REGISTER = (
    Path(__file__).resolve().parents[2] / "docs" / "requirements" / "values-register.md"
)


def _current_text(value_id: str) -> str:
    """The current value of one row of the values register, as written."""
    lines = REGISTER.read_text(encoding="utf-8").splitlines()
    header = next(line for line in lines if line.startswith("| ID |"))
    column = [cell.strip() for cell in header.split("|")].index("Current value")
    (row,) = [line for line in lines if line.startswith(f"| {value_id} |")]
    return row.split("|")[column].strip()


def _current_value(value_id: str) -> int:
    """The current value of one row of the values register, as an integer."""
    return int(_current_text(value_id).replace(",", ""))


@pytest.mark.req("ARCH-018")
def test_the_code_uses_the_values_of_the_values_register() -> None:
    assert PRECISION == _current_value("V-40")
    assert MAXIMUM_DOCUMENT_SIZE == _current_value("V-41")


@pytest.mark.req("ARCH-018", "PERF-010")
def test_the_measurement_values_are_those_of_the_values_register() -> None:
    fewest = {
        name: int(count.replace(",", ""))
        for name, count in re.findall(r"(p[0-9.]+): ([0-9,]+)", _current_text("V-45"))
    }
    assert set(fewest) == {name for name, _share in PERCENTILES}
    for name, share in PERCENTILES:
        samples = list(range(fewest[name]))
        assert percentile(samples[:-1], share) is None
        assert percentile(samples, share) is not None
    edges = _current_text("V-46")
    assert f"from {BUCKETS_NS[0]:,} " in edges
    assert f"to {BUCKETS_NS[-1]:,} " in edges
    assert f"{len(BUCKETS_NS)} edges" in edges
