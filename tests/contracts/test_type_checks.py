"""The type-test lines of `type_checks.py` are still there (ARCH-042; the Stage 1 plan, U3)."""

from __future__ import annotations

from pathlib import Path

TYPE_CHECKS = Path(__file__).with_name("type_checks.py")


def test_the_lines_that_must_not_type_check_are_present() -> None:
    text = TYPE_CHECKS.read_text(encoding="utf-8")
    assert text.count("fold(  # type: ignore[call-arg]") == 1
    for use in ("if outcome:", "while outcome:", "assert outcome", "not outcome"):
        assert f"{use}  # type: ignore[truthy-bool]" in text
    assert "outcome and 1  # type: ignore[truthy-bool,redundant-expr]" in text
    assert "outcome or 1  # type: ignore[truthy-bool,unreachable]" in text
