"""Contract versions and compatibility (ARCH-026, GOV-006)."""

from __future__ import annotations

import pytest

from atp.contracts import ContractVersion, is_compatible


@pytest.mark.parametrize(("text", "major", "minor"), [("1.0", 1, 0), ("2.13", 2, 13)])
def test_a_version_is_read_and_written_as_major_dot_minor(
    text: str, major: int, minor: int
) -> None:
    version = ContractVersion.parse(text)
    assert (version.major, version.minor) == (major, minor)
    assert str(version) == text


@pytest.mark.parametrize(
    "text", ["1", "1.0.0", "01.0", "1.01", "v1.0", " 1.0", "0.1", "-1.0", ""]
)
def test_malformed_or_zero_major_versions_are_refused(text: str) -> None:
    with pytest.raises(ValueError, match="version"):
        ContractVersion.parse(text)


@pytest.mark.parametrize(("major", "minor"), [(0, 1), (1, -1), (True, 0)])
def test_invalid_parts_are_refused(major: int, minor: int) -> None:
    with pytest.raises(ValueError, match="version"):
        ContractVersion(major, minor)


def test_different_major_versions_are_never_compatible() -> None:
    assert not is_compatible(ContractVersion(1, 0), ContractVersion(2, 0))
    assert not is_compatible(ContractVersion(2, 0), ContractVersion(1, 9))


def test_a_reader_understands_its_own_and_earlier_minor_versions() -> None:
    assert is_compatible(ContractVersion(1, 2), ContractVersion(1, 2))
    assert is_compatible(ContractVersion(1, 1), ContractVersion(1, 2))
    assert not is_compatible(ContractVersion(1, 3), ContractVersion(1, 2))


def test_a_version_is_immutable() -> None:
    version = ContractVersion(1, 0)
    with pytest.raises(AttributeError):
        version.major = 2  # type: ignore[misc]
