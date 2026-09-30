# Execution Engine

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-10 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Execution") · **Sources:** §39–§41
>
> Canonical location for execution per §98 (`docs/systems/execution-engine.md`).

Canonical definition of deterministic order execution, stale-decision protection, and idempotent execution.

## Deterministic execution

- **EXE-001** Deterministic execution · CONFIRMED ARCHITECTURAL PRINCIPLE · §39 — The Execution Engine is deterministic.
- **EXE-002** Responsibilities · SYSTEM REQUIREMENT · §39 — Order validation; exchange rules; quantity precision; price precision; minimum orders; order construction; submission; monitoring; fill handling; partial fills; cancellation; reconciliation; retry handling; execution-state management.
- **EXE-003** Never trust AI claims of success · CONSTRAINT · §39 — The system must never trust an AI statement that an order succeeded.

## Stale-decision protection

- **EXE-004** Revalidate before execution · CONFIRMED REQUIREMENT · §40 — Before execution: opportunity → analysis → proposal → market changes → revalidation → valid? If yes: execute. If no: reject / recalculate.

## Idempotent execution

- **EXE-005** A timeout is not a failure · CONSTRAINT · §41 — A timeout does not prove an order failed.
- **EXE-006** Timeout handling · CONFIRMED REQUIREMENT · §41 — Order submission → network timeout → do not blindly resubmit → query exchange → determine actual state → reconcile → continue safely. This prevents duplicate orders.

## Boundary (§92)

- **Owns:** order construction, submission, and execution state (EXE-002).
- **Consumes:** risk-approved, capital-reserved decisions (CAP-004); venue access through the [Exchange Adapter Layer](exchange-adapters.md).
- **Must not:** accept AI assertions about order state (EXE-003), or resubmit after a timeout without querying the venue first (EXE-006).
- **Not yet specified in Part 1:** order-type support, the revalidation criteria and time limits, the retry policy, interfaces, tests.

## Findings

- DUP-16: "reconciliation" is an Execution Engine responsibility here and also the purpose of [Recovery and Reconciliation](recovery-and-reconciliation.md).
- TC-05: EXE-006 requires every venue adapter to support querying order state.
- CF-03: capital reservation is missing from the latency-sensitive path.
