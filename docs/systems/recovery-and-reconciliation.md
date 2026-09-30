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
- **REC-009** Resuming after a restart · DEPRECATED / REPLACED · DEC-012 — After a restart, trading resumes only when REC-004 is met and the operator confirms. The operator may enable automatic resume, which then applies only when the platform was HEALTHY before the interruption and reconciliation found no mismatches.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

REC-009 (resume needs the operator unless enabled) is replaced by REC-010 to REC-013.

- **REC-010** Automatic 24/7 recovery · CONFIRMED REQUIREMENT · DEC-019 — The platform should automatically recover from: process crashes; service restarts; server restarts; container restarts; network interruptions; exchange disconnections; WebSocket failures; temporary AI-provider failures; database/service interruptions where recoverable. Recovery must be based on verified external state, not assumptions. Automatic restart must never mean blind automatic trading.
- **REC-011** Recovery checks and decision · CONFIRMED REQUIREMENT · DEC-019 — After a failure, crash, or restart: service recovery → load persistent state → verify database → verify policy → verify strategy state → verify capital → verify positions → verify open orders → verify exchange state → reconcile → verify risk state → verify system health → verify active-instance ownership → recovery decision. If safe to resume: automatic resumption. If partially safe: restricted operation. If unknown or unsafe: SAFE MODE, no trade.
- **REC-012** Recovery failure handling · CONFIRMED REQUIREMENT · DEC-019 — If recovery cannot establish sufficient certainty: no new trades → SAFE MODE → retry / reconcile → alert / incident. The system should continue operating its recovery and monitoring functions where possible. A human should only be required when the system reaches a condition outside its authorized recovery capabilities.
- **REC-013** Active-instance protection · CONSTRAINT · DEC-019 — A restarted instance must first establish that it is the authorized active execution instance: acquire / verify execution lease → check other instances → verify active ownership → reconcile → resume. Ownership is verified again immediately before the recovery decision in REC-011. Two instances must never independently believe that they are the active live trading authority.

## Boundary (§92)

- **Owns:** the restart sequence, reconciliation of internal vs venue state, and the safe-resume decision.
- **Consumes:** venue state via the [Exchange Adapter Layer](exchange-adapters.md). Validates against the [Risk Engine](../risk/risk-engine.md), [Global Capital Authority](capital-management.md), [Policy System](policy/policy-system.md), and [Strategy Management](strategy/strategy-management.md).
- **Called by:** the Execution Engine after a timeout (EXE-006).
- **Not yet specified:** mismatch-resolution procedures per mismatch type (expected with Part 2 contracts), interfaces, tests. Resuming is governed by REC-009.

## Findings

CF-09 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (REC-007). DUP-16 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (REC-008). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (core reconciliation in CORE TRADING FOUNDATION, hardening in OPERATIONALIZATION).

Open: CF-12 (recovery ordering): REC-007 says verify the database before loading from it; REC-002 (§71) and REC-011 (OC-1 item 11) load, then verify. Awaiting owner review; see the [findings register](../conflicts/register.md).
