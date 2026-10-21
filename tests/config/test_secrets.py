"""Secrets: read from the process environment through one interface, never shown (SEC-005)."""

from __future__ import annotations

import copy
import pickle

import pytest

from atp.config import REDACTED, ProcessEnvironment, Secret, SecretSource

# Assembled at run time so that no file holds a credential-shaped sample.
SECRET = "sk" + "_live_" + "Q7x9Z2" + "secretvalue"


def test_a_secret_is_never_shown() -> None:
    secret = Secret(SECRET)
    assert str(secret) == REDACTED
    assert repr(secret) == f"Secret({REDACTED})"
    assert f"{secret}" == REDACTED
    assert f"{secret:>40}" == REDACTED
    assert "{}".format(secret) == REDACTED  # noqa: UP032 - the form under test
    assert "%s %r" % (secret, secret) == f"{REDACTED} Secret({REDACTED})"  # noqa: UP031
    assert SECRET not in repr([secret, {"k": secret}])


def test_the_value_is_revealed_only_on_request() -> None:
    assert Secret(SECRET).reveal() == SECRET


@pytest.mark.parametrize("value", ["", b"bytes", 7, None])
def test_a_secret_is_a_non_empty_str(value: object) -> None:
    with pytest.raises(ValueError, match="non-empty str") as error:
        Secret(value)  # type: ignore[arg-type]
    assert SECRET not in str(error.value)


def test_a_secret_is_not_pickled_or_copied() -> None:
    secret = Secret(SECRET)
    for write in (pickle.dumps, copy.copy, copy.deepcopy):
        with pytest.raises(TypeError, match="not pickled or copied"):
            write(secret)


def test_a_secret_is_immutable_and_final() -> None:
    secret = Secret(SECRET)
    with pytest.raises(AttributeError):
        secret._value = "other"  # noqa: SLF001
    with pytest.raises(AttributeError):
        del secret._value  # noqa: SLF001
    assert secret.reveal() == SECRET
    with pytest.raises(TypeError, match="cannot be subclassed"):
        type("Sub", (Secret,), {})


def test_the_process_environment_is_a_secret_source(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ATP_TEST_SECRET", SECRET)
    monkeypatch.delenv("ATP_TEST_ABSENT", raising=False)
    source: SecretSource = ProcessEnvironment()
    assert source.secret_value("ATP_TEST_SECRET") == SECRET
    assert source.secret_value("ATP_TEST_ABSENT") is None


def test_a_given_mapping_is_read_instead_of_the_process_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ATP_TEST_SECRET", "from-the-process")
    source = ProcessEnvironment({"ATP_TEST_SECRET": SECRET})
    assert source.secret_value("ATP_TEST_SECRET") == SECRET
    assert source.secret_value("ATP_OTHER") is None
