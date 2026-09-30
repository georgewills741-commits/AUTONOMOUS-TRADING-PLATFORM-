# Recovery and Reconciliation

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-11 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Reconciliation") and OPERATIONALIZATION ("Recovery", "Reconciliation"), see CF-05 · **Sources:** §71–§73

Canonical definition of what happens after a restart or interruption and how internal state is reconciled with venues.

## Recovery

- **REC-001** External reality changes while offline · CONFIRMED ARCHITECTURAL PRINCIPLE · §71 — The platform must assume external reality can change while offline.
- **REC-002** Recovery sequence · CONFIRMED REQUIREMENT · §71 — System restart → load verified internal state → verify database → connect external systems → check exchanges → fetch balances → fetch positions → fetch open orders → fetch fills → reconcile → resolve mismatches → refresh market data → validate risk → validate capital → validate policy → validate strategy state → safe resume.

## Safe resume

- **REC-003** Restart does not authorize trading · CONSTRAINT · §72 — Restarting does not automatically authorize trading.
- **REC-004** Resume preconditions · CONFIRMED REQUIREMENT · §72 — Before resuming, these must be established: data integrity; exchange connectivity; account state; balance state; position state; order state; capital state; risk state; strategy state; policy state; system health.

## Active trade recovery

- **REC-005** Determine real trade state · CONFIRMED REQUIREMENT · §73 — After interruption determine: open positions; filled orders; partial fills; cancelled orders; triggered stops/targets; actual execution prices; balances; exposure; market conditions; strategy validity; emergency requirements.
- **REC-006** Never restore stale memory · CONSTRAINT · §73 — Never simply restore an old in-memory state.

## Decisions applied (2026-09-30)

- **REC-007** Verify the database before loading from it · CONFIRMED REQUIREMENT · DEC-010 — Database integrity is verified before internal state is loaded from it. "Load verified internal state" in REC-002 means loading state from the database after that check.
- **REC-008** Sole owner of reconciliation · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This system owns all reconciliation logic (orders, balances, positions, ledger); other systems invoke it.
- **REC-009** Resuming after a restart · CONSTRAINT · DEC-012 — After a restart, trading resumes only when REC-004 is met and the operator confirms. The operator may enable automatic resume, which then applies only when the platform was HEALTHY before the interruption and reconciliation found no mismatches.

## Boundary (§92)

- **Owns:** the restart sequence, reconciliation of internal vs venue state, and the safe-resume decision.
- **Consumes:** venue state via the [Exchange Adapter Layer](exchange-adapters.md). Validates against the [Risk Engine](../risk/risk-engine.md), [Global Capital Authority](capital-management.md), [Policy System](policy/policy-system.md), and [Strategy Management](strategy/strategy-management.md).
- **Called by:** the Execution Engine after a timeout (EXE-006).
- **Not yet specified:** mismatch-resolution procedures per mismatch type (expected with Part 2 contracts), interfaces, tests. Resuming is governed by REC-009.

## Findings (all resolved)

CF-09 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (REC-007). DUP-16 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (REC-008). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (core reconciliation in CORE TRADING FOUNDATION, hardening in OPERATIONALIZATION).
