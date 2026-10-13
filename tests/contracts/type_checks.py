"""Lines that must not type-check (ARCH-042; the Stage 1 plan, U3).

This module is never run; strict mypy checks it with the rest of `tests/`. Each marked line is
an error the type checker must keep reporting, silenced by an ignore comment naming the error
code; `and` and `or` also report the operand mypy then considers redundant or unreachable. mypy
reports an ignore that no longer silences anything (strict mode), so if one of these errors
ever disappeared, the type check would fail. `test_type_checks.py` checks that the lines
are still here. Each truth-value use is in its own function: mypy treats an outcome as always
true, so code after a first use would be reported as unreachable instead.
"""

from __future__ import annotations

from atp.contracts import Outcome


def an_unhandled_outcome(outcome: Outcome[int, str]) -> int:
    return outcome.fold(  # type: ignore[call-arg]
        on_success=lambda value: value,
        on_failure=lambda error: 0,
        on_timeout=lambda: 0,
    )


def an_outcome_in_if(outcome: Outcome[int, str]) -> None:
    if outcome:  # type: ignore[truthy-bool]
        pass


def an_outcome_in_while(outcome: Outcome[int, str]) -> None:
    while outcome:  # type: ignore[truthy-bool]
        break


def an_outcome_in_assert(outcome: Outcome[int, str]) -> None:
    assert outcome  # type: ignore[truthy-bool]


def an_outcome_in_not(outcome: Outcome[int, str]) -> bool:
    return not outcome  # type: ignore[truthy-bool]


def an_outcome_in_and(outcome: Outcome[int, str]) -> object:
    return outcome and 1  # type: ignore[truthy-bool,redundant-expr]


def an_outcome_in_or(outcome: Outcome[int, str]) -> object:
    return outcome or 1  # type: ignore[truthy-bool,unreachable]
