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

## Decisions applied (2026-09-30)

- **EXE-007** Reconciliation is invoked, not reimplemented · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The Execution Engine invokes Recovery and Reconciliation for order-level reconciliation (EXE-002, EXE-006); it does not implement its own reconciliation logic.
- **EXE-008** Client order IDs · CONSTRAINT · DEC-008 — Every order carries a unique client order ID, so its state can be queried after a timeout (EXA-008).

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **EXE-009** Transfer execution and state verification · CONFIRMED REQUIREMENT · DEC-019 — A transfer timeout must never automatically mean the transfer failed. After a timeout or an unknown result, the engine queries the venue, and the blockchain where relevant, to determine the actual state: success, pending, failed, or unknown. If the state remains unknown, it makes no duplicate transfer, hands the transfer to reconciliation, and keeps the platform in a safe state for it. This applies to all autonomous transfer operations.
- **EXE-010** Only the active instance acts · CONSTRAINT · DEC-019 — Only the instance holding the current execution lease (REC-013) may submit, amend, or cancel orders or initiate transfers. Every such request is checked against the lease, so two instances can never both act as the live trading authority.

Placement (builder): the Global Capital Authority decides a transfer (CAP-023); this engine executes it, with the same idempotency discipline as orders (EXE-006).

## Handoff Part 2 (2026-09-30)

[Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md) adds no new execution requirement. Order and transfer timeouts (P2§84, §85, §307, §308) are EXE-005, EXE-006, and EXE-009. Paper/live parity (PAP-006) places a paper executor and a live executor behind this system's execution interface; the paper executor belongs to [Paper Trading](strategy/paper-trading.md). Only the active execution instance may act (EXE-010), across local and server hosts as well (REC-019, REC-020).

## Owner decisions applied (Part 2 findings, 2026-09-30)

From [DEC-027](../decisions/DEC-027-part-2-open-questions.md) ([owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), Q4), resolving OQ-26:

- **EXE-011** Adaptive execution · FUTURE · DEC-027 — Adaptive execution: execution that adjusts order type, order splitting, and price to liquidity and volatility, inside risk limits. It is not built until the owner approves it.

When it is approved, it stays deterministic (EXE-001) and inside the safety envelope (RSK-034, RSK-036).

## Boundary (§92)

- **Owns:** order construction, submission, and execution state (EXE-002).
- **Consumes:** risk-approved, capital-reserved decisions (CAP-004); venue access through the [Exchange Adapter Layer](exchange-adapters.md).
- **Must not:** accept AI assertions about order state (EXE-003), or resubmit after a timeout without querying the venue first (EXE-006).
- **Not yet specified in Part 1:** order-type support, the revalidation criteria and time limits, the retry policy, interfaces, tests.

## Findings (all resolved)

DUP-16 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (EXE-007). TC-05 → [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md) (EXE-008, EXA-008). CF-03 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-021).
