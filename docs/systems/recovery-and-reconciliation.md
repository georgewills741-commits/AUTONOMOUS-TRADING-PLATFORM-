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

## Boundary (§92)

- **Owns:** the restart sequence, reconciliation of internal vs venue state, and the safe-resume decision.
- **Consumes:** venue state via the [Exchange Adapter Layer](exchange-adapters.md). Validates against the [Risk Engine](../risk/risk-engine.md), [Global Capital Authority](capital-management.md), [Policy System](policy/policy-system.md), and [Strategy Management](strategy/strategy-management.md).
- **Called by:** the Execution Engine after a timeout (EXE-006).
- **Not yet specified in Part 1:** how mismatches are resolved, who authorizes resuming, interfaces, tests.

## Findings

- CF-09: REC-002 loads verified internal state before verifying the database. The intended order needs confirming.
- DUP-16: the Execution Engine also lists reconciliation (EXE-002), and custody would need its own reconciliation (CUS-002).
- CF-05: reconciliation is mapped to two roadmap stages.
