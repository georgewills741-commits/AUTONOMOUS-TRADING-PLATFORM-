"""The result of one external operation: SUCCESS, FAILURE, TIMEOUT, or UNKNOWN (ARCH-042).

An outcome is read only through `fold`, which needs one handler for each of the four results,
so the type checker rejects code that forgets one, and UNKNOWN can never be read as SUCCESS by
omission. Using an outcome as a truth value raises at run time; `if`, `while`, `not`, `and`,
`or`, and `assert` on an outcome are also type errors (mypy's `truthy-bool`), because the
`__bool__` that raises is hidden from the type checker. Comparing outcomes with `==` raises:
it would test the kind outside `fold`. The kind and the value are private. In a contract, an
outcome's value or error is validated against the field's declared types, also when an
`Outcome` instance is given; the result/value envelope appears only in JSON.

States particular to one operation, such as a transfer's "pending" (EXE-009), belong to that
operation's own contract, defined in its stage; they are never mapped to SUCCESS unless the
operation is confirmed complete.
"""

from __future__ import annotations

import enum
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Final, Never, assert_never, cast, final, get_args

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

from atp.contracts._errors import register_known_names


class _Kind(enum.Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    TIMEOUT = "TIMEOUT"
    UNKNOWN = "UNKNOWN"


OUTCOME_RESULTS: Final = tuple(kind.value for kind in _Kind)
"""The four results, as they are written in JSON (the `result` field)."""

_TOKEN: Final = object()

register_known_names([*OUTCOME_RESULTS, "result", "value", "error"])


@final
class Outcome[ValueT, ErrorT]:
    """SUCCESS with a value, FAILURE with an error, TIMEOUT, or UNKNOWN."""

    __slots__ = ("_kind", "_payload")
    _kind: _Kind
    _payload: object

    def __init__(self, token: object, kind: _Kind, payload: object) -> None:
        if token is not _TOKEN:
            msg = (
                "build an outcome with Outcome.success, .failure, .timeout, or .unknown"
            )
            raise TypeError(msg)
        object.__setattr__(self, "_kind", kind)
        object.__setattr__(self, "_payload", payload)

    @staticmethod
    def success[T](value: T) -> Outcome[T, Never]:
        """The operation is confirmed complete, with this value."""
        return Outcome(_TOKEN, _Kind.SUCCESS, value)

    @staticmethod
    def failure[E](error: E) -> Outcome[Never, E]:
        """The operation is confirmed not done, for this reason."""
        return Outcome(_TOKEN, _Kind.FAILURE, error)

    @staticmethod
    def timeout() -> Outcome[Never, Never]:
        """No answer arrived in time; the operation may or may not have happened."""
        return Outcome(_TOKEN, _Kind.TIMEOUT, None)

    @staticmethod
    def unknown() -> Outcome[Never, Never]:
        """The result cannot be determined; it must be reconciled, never assumed."""
        return Outcome(_TOKEN, _Kind.UNKNOWN, None)

    def fold[R](
        self,
        *,
        on_success: Callable[[ValueT], R],
        on_failure: Callable[[ErrorT], R],
        on_timeout: Callable[[], R],
        on_unknown: Callable[[], R],
    ) -> R:
        """Handle each of the four results; the only way to read an outcome."""
        kind = self._kind
        if kind is _Kind.SUCCESS:
            return on_success(cast("ValueT", self._payload))
        if kind is _Kind.FAILURE:
            return on_failure(cast("ErrorT", self._payload))
        if kind is _Kind.TIMEOUT:
            return on_timeout()
        if kind is _Kind.UNKNOWN:
            return on_unknown()
        assert_never(kind)

    def __init_subclass__(cls, **kwargs: object) -> None:
        msg = "Outcome cannot be subclassed"
        raise TypeError(msg)

    def __reduce__(
        self,
    ) -> tuple[Callable[[str, object], Outcome[Any, Any]], tuple[str, object]]:
        # Copying and pickling rebuild the outcome through its constructors.
        return (_rebuild, (self._kind.value, self._payload))

    def __setattr__(self, name: str, value: object) -> None:
        msg = "an outcome is immutable"
        raise AttributeError(msg)

    def __delattr__(self, name: str) -> None:
        msg = "an outcome is immutable"
        raise AttributeError(msg)

    def __repr__(self) -> str:
        return f"<Outcome {self._kind.value}>"

    if not TYPE_CHECKING:
        # Hidden from the type checker on purpose: mypy then reports truth-value use of an
        # outcome (truthy-bool), which it would not if it saw a __bool__.

        def __bool__(self):
            msg = "an outcome has no truth value; read it with fold"
            raise TypeError(msg)

        def __eq__(self, other):
            msg = "outcomes are not compared; read them with fold"
            raise TypeError(msg)

        __hash__ = None

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        arguments = get_args(source)
        if len(arguments) != 2:
            msg = "a contract field holds Outcome[ValueType, ErrorType]"
            raise TypeError(msg)
        value_schema = handler.generate_schema(arguments[0])
        error_schema = handler.generate_schema(arguments[1])

        def shape(
            result: str, **fields: core_schema.CoreSchema
        ) -> core_schema.CoreSchema:
            members = {
                "result": core_schema.typed_dict_field(
                    core_schema.literal_schema([result])
                )
            }
            members.update(
                {
                    name: core_schema.typed_dict_field(schema)
                    for name, schema in fields.items()
                }
            )
            # Strict here too: the model's strict setting does not reach this custom schema.
            return core_schema.typed_dict_schema(
                members,
                extra_behavior="forbid",
                config=core_schema.CoreConfig(strict=True),
            )

        envelope = core_schema.tagged_union_schema(
            {
                "SUCCESS": shape("SUCCESS", value=value_schema),
                "FAILURE": shape("FAILURE", error=error_schema),
                "TIMEOUT": shape("TIMEOUT"),
                "UNKNOWN": shape("UNKNOWN"),
            },
            discriminator="result",
        )
        from_envelope = core_schema.no_info_after_validator_function(
            _from_envelope, envelope
        )

        def revalidate_instance(
            value: object, handler: core_schema.ValidatorFunctionWrapHandler
        ) -> object:
            # An instance is validated like its envelope, so its value and error must have
            # the field's declared types too.
            if isinstance(value, Outcome):
                value = _to_envelope(value)
            return handler(value)

        return core_schema.json_or_python_schema(
            json_schema=from_envelope,
            python_schema=core_schema.no_info_wrap_validator_function(
                revalidate_instance,
                from_envelope,
                # A Python dump keeps the outcome object; only JSON shows the envelope.
                serialization=core_schema.plain_serializer_function_ser_schema(
                    _same, when_used="always"
                ),
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                _to_envelope, return_schema=envelope, when_used="json"
            ),
        )


def _same(outcome: Outcome[Any, Any]) -> Outcome[Any, Any]:
    return outcome


def _rebuild(kind: str, payload: object) -> Outcome[Any, Any]:
    return Outcome(_TOKEN, _Kind(kind), payload)


def _from_envelope(envelope: dict[str, Any]) -> Outcome[Any, Any]:
    result = envelope["result"]
    if result == "SUCCESS":
        return Outcome.success(envelope["value"])
    if result == "FAILURE":
        return Outcome.failure(envelope["error"])
    if result == "TIMEOUT":
        return Outcome.timeout()
    return Outcome.unknown()


def _to_envelope(outcome: Outcome[Any, Any]) -> dict[str, Any]:
    return outcome.fold(
        on_success=lambda value: {"result": "SUCCESS", "value": value},
        on_failure=lambda error: {"result": "FAILURE", "error": error},
        on_timeout=lambda: {"result": "TIMEOUT"},
        on_unknown=lambda: {"result": "UNKNOWN"},
    )
