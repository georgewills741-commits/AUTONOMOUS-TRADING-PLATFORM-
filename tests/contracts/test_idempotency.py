"""The idempotency key (ARCH-041)."""

from __future__ import annotations

import copy
import pickle
import re

import pytest

from atp.contracts import Contract, ContractError, ContractVersion, IdempotencyKey


class Request(Contract):
    contract_id = "test.request"
    contract_version = ContractVersion(1, 0)
    key: IdempotencyKey


def test_a_new_key_is_32_lowercase_hex_characters() -> None:
    key = IdempotencyKey.new()
    assert re.fullmatch(IdempotencyKey.PATTERN, str(key))


def test_new_keys_differ() -> None:
    assert len({str(IdempotencyKey.new()) for _ in range(1000)}) == 1000


@pytest.mark.parametrize(
    "text",
    ["", "0" * 31, "0" * 33, "G" * 32, "A" * 32, " " + "0" * 32, "0" * 32 + "\n"],
)
def test_malformed_keys_are_refused(text: str) -> None:
    with pytest.raises(ValueError, match="idempotency key"):
        IdempotencyKey(text)


def test_keys_compare_by_value_and_are_immutable() -> None:
    text = "0123456789abcdef0123456789abcdef"
    assert IdempotencyKey(text) == IdempotencyKey(text)
    assert hash(IdempotencyKey(text)) == hash(IdempotencyKey(text))
    assert IdempotencyKey(text) != text
    key = IdempotencyKey(text)
    for name in (*IdempotencyKey.__slots__, "anything"):
        with pytest.raises(AttributeError):
            setattr(key, name, "f" * 32)
        with pytest.raises(AttributeError):
            delattr(key, name)
    assert str(key) == text


def test_a_key_travels_as_a_json_string() -> None:
    key = IdempotencyKey.new()
    request = Request(key=key)
    assert request.to_json() == f'{{"key":"{key}"}}'
    assert Request.from_json(request.to_json()) == request


def test_a_key_cannot_be_subclassed() -> None:
    with pytest.raises(TypeError, match="subclassed"):

        class Special(IdempotencyKey):  # type: ignore[misc]
            pass


def test_a_key_can_be_copied_and_pickled() -> None:
    key = IdempotencyKey.new()
    for clone in (
        copy.copy(key),
        copy.deepcopy(key),
        pickle.loads(pickle.dumps(key)),  # noqa: S301 -- the bytes were made by this test
    ):
        assert clone == key


@pytest.mark.parametrize(
    ("value", "kind"),
    [(7, "idempotency_key_type"), ("ABC", "idempotency_key_invalid")],
)
def test_a_refused_key_has_its_own_error_type(value: object, kind: str) -> None:
    with pytest.raises(ContractError) as refused:
        Request.from_python({"key": value})
    assert refused.value.details[0].type == kind


def test_a_key_that_is_not_a_string_is_refused() -> None:
    with pytest.raises(ContractError):
        Request.from_json('{"key": 1234}')
