"""The outcome type: four results, read only through fold (ARCH-042)."""

from __future__ import annotations

import copy
import pickle
from decimal import Decimal
from typing import Any

import pytest
from pydantic import ValidationError

from atp.contracts import (
    OUTCOME_RESULTS,
    Amount,
    Contract,
    ContractError,
    ContractVersion,
    Outcome,
)
from atp.numeric import amount


def _name(outcome: Outcome[Any, Any]) -> str:
    return outcome.fold(
        on_success=lambda value: f"SUCCESS {value}",
        on_failure=lambda error: f"FAILURE {error}",
        on_timeout=lambda: "TIMEOUT",
        on_unknown=lambda: "UNKNOWN",
    )


class Report(Contract):
    contract_id = "test.report"
    contract_version = ContractVersion(1, 0)
    outcome: Outcome[Amount, str]


@pytest.mark.parametrize(
    ("text", "location"),
    [
        (
            '{"outcome": {"result": "SUCCESS", "value": 0.1}}',
            ("outcome", "SUCCESS", "value"),
        ),
        (
            '{"outcome": {"result": "FAILURE", "error": 5}}',
            ("outcome", "FAILURE", "error"),
        ),
    ],
)
def test_a_refusal_inside_an_outcome_names_its_result_and_member(
    text: str, location: tuple[str, ...]
) -> None:
    # Locations keep only the names the platform declares; the outcome declares its results
    # and members, so they are not redacted.
    with pytest.raises(ContractError) as refused:
        Report.from_json(text)
    assert refused.value.details[0].location == location


@pytest.mark.req("ARCH-042")
def test_there_are_exactly_four_results() -> None:
    assert OUTCOME_RESULTS == ("SUCCESS", "FAILURE", "TIMEOUT", "UNKNOWN")


@pytest.mark.req("ARCH-042")
def test_fold_calls_the_handler_of_each_result() -> None:
    assert _name(Outcome.success(5)) == "SUCCESS 5"
    assert _name(Outcome.failure("refused")) == "FAILURE refused"
    assert _name(Outcome.timeout()) == "TIMEOUT"
    assert _name(Outcome.unknown()) == "UNKNOWN"


@pytest.mark.parametrize(
    "outcome",
    [Outcome.success(1), Outcome.failure("x"), Outcome.timeout(), Outcome.unknown()],
)
@pytest.mark.req("ARCH-042")
def test_an_outcome_has_no_truth_value(outcome: Outcome[Any, Any]) -> None:
    with pytest.raises(TypeError, match="truth value"):
        bool(outcome)


def test_outcomes_are_not_compared() -> None:
    with pytest.raises(TypeError, match="not compared"):
        _ = Outcome.unknown() == Outcome.unknown()
    with pytest.raises(TypeError):
        hash(Outcome.success(1))


def test_an_outcome_is_immutable() -> None:
    outcome = Outcome.success(1)
    for name in (*Outcome.__slots__, "anything"):
        with pytest.raises(AttributeError):
            setattr(outcome, name, None)
        with pytest.raises(AttributeError):
            delattr(outcome, name)


def test_an_outcome_is_built_only_through_its_four_constructors() -> None:
    with pytest.raises(TypeError, match="build an outcome"):
        Outcome(object(), None, None)  # type: ignore[arg-type]


def test_the_representation_names_only_the_result() -> None:
    assert repr(Outcome.success("a value that is not shown")) == "<Outcome SUCCESS>"


@pytest.mark.parametrize(
    ("outcome", "text"),
    [
        (
            Outcome.success(amount("1.50")),
            '{"outcome":{"result":"SUCCESS","value":"1.50"}}',
        ),
        (
            Outcome.failure("refused"),
            '{"outcome":{"result":"FAILURE","error":"refused"}}',
        ),
        (Outcome.timeout(), '{"outcome":{"result":"TIMEOUT"}}'),
        (Outcome.unknown(), '{"outcome":{"result":"UNKNOWN"}}'),
    ],
)
def test_an_outcome_round_trips_through_json(
    outcome: Outcome[Any, Any], text: str
) -> None:
    report = Report(outcome=outcome)
    assert report.to_json() == text
    assert _name(Report.from_json(text).outcome) == _name(outcome)


@pytest.mark.parametrize(
    "text",
    [
        '{"outcome": {"result": "SUCCESS"}}',
        '{"outcome": {"result": "SUCCESS", "value": 1.5}}',
        '{"outcome": {"result": "PENDING"}}',
        '{"outcome": {"result": "UNKNOWN", "value": "1"}}',
        '{"outcome": {}}',
        '{"outcome": "SUCCESS"}',
    ],
)
def test_malformed_outcomes_are_refused(text: str) -> None:
    with pytest.raises(ContractError):
        Report.from_json(text)


class Batch(Contract):
    contract_id = "test.batch"
    contract_version = ContractVersion(1, 0)
    outcome: Outcome[tuple[int, ...], str]


def test_an_instance_value_must_have_the_declared_type() -> None:
    with pytest.raises(ValidationError):
        Report(outcome=Outcome.success(1.5))  # type: ignore[arg-type]
    with pytest.raises(ContractError):
        Report.from_python({"outcome": Outcome.success(1.5)})
    with pytest.raises(ContractError):
        Report.from_python({"outcome": Outcome.failure(7)})
    with pytest.raises(ContractError):
        Batch.from_python({"outcome": Outcome.success([1, 2])})


def test_an_instance_value_of_the_right_type_is_validated_again() -> None:
    # A Decimal with more digits than the precision has the declared type, so only
    # validating the instance through its envelope refuses it.
    too_precise = Decimal("1." + "1" * 40)
    with pytest.raises(ContractError) as refused:
        Report.from_python({"outcome": Outcome.success(too_precise)})
    assert refused.value.details[0].type == "amount_invalid"


def test_a_valid_instance_is_accepted_and_keeps_its_value() -> None:
    report = Report.from_python({"outcome": Outcome.success(amount("2.50"))})
    assert _name(report.outcome) == "SUCCESS 2.50"
    assert _name(Batch(outcome=Outcome.success((1, 2))).outcome) == "SUCCESS (1, 2)"


def test_a_python_dump_keeps_the_outcome_object() -> None:
    dumped = Report(outcome=Outcome.timeout()).model_dump()
    assert isinstance(dumped["outcome"], Outcome)


def test_an_outcome_cannot_be_subclassed() -> None:
    with pytest.raises(TypeError, match="subclassed"):

        class Special(Outcome[int, str]):  # type: ignore[misc]
            pass


@pytest.mark.parametrize(
    "outcome",
    [
        Outcome.success(amount("1.5")),
        Outcome.failure("x"),
        Outcome.timeout(),
        Outcome.unknown(),
    ],
)
def test_an_outcome_can_be_copied_and_pickled(outcome: Outcome[Any, Any]) -> None:
    for clone in (
        copy.copy(outcome),
        copy.deepcopy(outcome),
        pickle.loads(pickle.dumps(outcome)),  # noqa: S301 -- the bytes were made by this test
    ):
        assert _name(clone) == _name(outcome)


def test_an_outcome_cannot_be_given_unparametrized() -> None:
    with pytest.raises(TypeError, match="Outcome\\[ValueType, ErrorType\\]"):

        class Bare(Contract):
            contract_id = "test.bare"
            contract_version = ContractVersion(1, 0)
            outcome: Outcome  # type: ignore[type-arg]
