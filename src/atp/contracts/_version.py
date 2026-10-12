"""Contract versions and their compatibility rule (ARCH-026, GOV-006; docs/architecture/contracts.md)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Final

_VERSION_RE: Final = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", flags=re.ASCII)


@dataclass(frozen=True, order=True, slots=True)
class ContractVersion:
    """A contract's version, MAJOR.MINOR.

    A change that can break a consumer needs a new major version. A minor version only adds
    what an older reader of the same major version never receives unless it asked for that
    minor version or a later one.
    """

    major: int
    minor: int

    def __post_init__(self) -> None:
        for part in (self.major, self.minor):
            if type(part) is not int or part < 0:
                msg = "a version's parts are non-negative integers"
                raise ValueError(msg)
        if self.major == 0:
            msg = "a contract's major version starts at 1"
            raise ValueError(msg)

    @classmethod
    def parse(cls, text: str) -> ContractVersion:
        """Read `MAJOR.MINOR`, for example `1.0`."""
        matched = _VERSION_RE.fullmatch(text) if type(text) is str else None
        if matched is None:
            msg = "a contract version is written MAJOR.MINOR"
            raise ValueError(msg)
        return cls(int(matched.group(1)), int(matched.group(2)))

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}"


def is_compatible(produced: ContractVersion, understood: ContractVersion) -> bool:
    """Whether a reader that understands version `understood` can read data of version `produced`.

    Different major versions are never compatible. Within one major version, a reader
    understands every minor version up to its own: contracts refuse unknown fields, so data of
    a later minor version can carry a field an earlier reader would refuse.
    """
    return produced.major == understood.major and produced.minor <= understood.minor
