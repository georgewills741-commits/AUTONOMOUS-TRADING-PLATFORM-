"""Secrets: read only from the runtime environment, never shown (SEC-005; constitution Rule 153).

A secret's value is held by a `Secret`, whose text, representation, and formatted forms are
`<redacted>`; the code that needs the value calls `reveal()`. Values are read through one
interface, `SecretSource`, so that a secret manager can implement it later; the process
environment is its only implementation now.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Final, NoReturn, Protocol, final

REDACTED: Final = "<redacted>"
"""Shown wherever a secret's value would be."""


@final
class Secret:
    """A secret's value, never shown: `str`, `repr`, and `format` give `<redacted>`.

    It cannot be pickled or copied, which would write the value out, and cannot be subclassed.
    """

    __slots__ = ("_value",)
    _value: str

    def __init__(self, value: str) -> None:
        if type(value) is not str or not value:
            msg = "a secret's value is a non-empty str"
            raise ValueError(msg)
        object.__setattr__(self, "_value", value)

    def __init_subclass__(cls, **kwargs: object) -> None:
        msg = "Secret cannot be subclassed"
        raise TypeError(msg)

    def reveal(self) -> str:
        """The value, for the code that hands it to the service it is for."""
        return self._value

    def __repr__(self) -> str:
        return f"Secret({REDACTED})"

    def __str__(self) -> str:
        return REDACTED

    def __format__(self, format_spec: str) -> str:
        return REDACTED

    def __setattr__(self, name: str, value: object) -> NoReturn:
        msg = "a secret is immutable"
        raise AttributeError(msg)

    def __delattr__(self, name: str) -> NoReturn:
        msg = "a secret is immutable"
        raise AttributeError(msg)

    def __reduce__(self) -> NoReturn:
        msg = "a secret is not pickled or copied"
        raise TypeError(msg)


class SecretSource(Protocol):
    """Where secret values come from: the process environment now, a secret manager later."""

    def secret_value(self, name: str) -> str | None:
        """The named secret's value, or None if it is not set."""
        ...


@final
class ProcessEnvironment:
    """The process environment as a `SecretSource`: a secret's name is a variable's name."""

    __slots__ = ("_variables",)

    def __init__(self, variables: Mapping[str, str] | None = None) -> None:
        # Tests give their own mapping; a process reads its environment.
        self._variables: Mapping[str, str] = (
            os.environ if variables is None else variables
        )

    def secret_value(self, name: str) -> str | None:
        return self._variables.get(name)
