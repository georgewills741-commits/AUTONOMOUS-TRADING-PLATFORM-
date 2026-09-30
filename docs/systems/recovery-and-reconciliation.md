# Recovery and Reconciliation

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-11 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Reconciliation") and OPERATIONALIZATION ("Recovery", "Reconciliation"), see CF-05 · **Sources:** §71–§73

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

- **REC-007** Verify the database before loading from it · DEPRECATED / REPLACED · DEC-010 — Database integrity is verified before internal state is loaded from it. "Load verified internal state" in REC-002 means loading state from the database after that check.
- **REC-008** Sole owner of reconciliation · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This system owns all reconciliation logic (orders, balances, positions, ledger); other systems invoke it.
- **REC-009** Resuming after a restart · DEPRECATED / REPLACED · DEC-012 — After a restart, trading resumes only when REC-004 is met and the operator confirms. The operator may enable automatic resume, which then applies only when the platform was HEALTHY before the interruption and reconciliation found no mismatches.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

REC-009 (resume needs the operator unless enabled) is replaced by REC-010 to REC-013.

- **REC-010** Automatic 24/7 recovery · CONFIRMED REQUIREMENT · DEC-019 — The platform should automatically recover from: process crashes; service restarts; server restarts; container restarts; network interruptions; exchange disconnections; WebSocket failures; temporary AI-provider failures; database/service interruptions where recoverable. Recovery must be based on verified external state, not assumptions. Automatic restart must never mean blind automatic trading.
- **REC-011** Recovery checks and decision · DEPRECATED / REPLACED · DEC-019 — After a failure, crash, or restart: service recovery → load persistent state → verify database → verify policy → verify strategy state → verify capital → verify positions → verify open orders → verify exchange state → reconcile → verify risk state → verify system health → verify active-instance ownership → recovery decision. If safe to resume: automatic resumption. If partially safe: restricted operation. If unknown or unsafe: SAFE MODE, no trade.
- **REC-012** Recovery failure handling · CONFIRMED REQUIREMENT · DEC-019 — If recovery cannot establish sufficient certainty: no new trades → SAFE MODE → retry / reconcile → alert / incident. The system should continue operating its recovery and monitoring functions where possible. A human should only be required when the system reaches a condition outside its authorized recovery capabilities.
- **REC-013** Active-instance protection · CONSTRAINT · DEC-019 — A restarted instance must first establish that it is the authorized active execution instance: acquire / verify execution lease → check other instances → verify active ownership → reconcile → resume. Ownership is verified again immediately before the recovery decision in REC-011. Two instances must never independently believe that they are the active live trading authority.

## Owner decisions applied (CF-11 to CF-13, 2026-09-30)

REC-007 is replaced by REC-014. REC-011 is replaced by REC-015 and REC-016 ([DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)). REC-011's "partially safe → restricted operation" outcome is carried into REC-016. References to REC-011 elsewhere (REC-013, HLT-012, RSK-020) now resolve to REC-015 and REC-016.

- **REC-014** Persisted state is untrusted context · CONSTRAINT · DEC-022 — After restart, persisted state may be loaded as recovery context, but it must never be blindly trusted as authoritative financial state. It should be compared against authoritative external state rather than assumed correct.
- **REC-015** Recovery sequence · CONFIRMED REQUIREMENT · DEC-022 — The recovery sequence should be: restart → load persisted state as untrusted recovery context → verify database integrity → verify schema / version → verify configuration and policy → verify exchange connectivity and health → fetch authoritative external state → reconcile balances → reconcile positions → reconcile open orders → reconcile capital reservations → reconcile pending transfers → verify risk state → verify strategy state → verify market-data freshness → verify execution state → run safety checks → enter SAFE/RESTRICTED mode → authorize resumption → resume normal operation.
- **REC-016** Recovery outcomes · CONFIRMED REQUIREMENT · DEC-022 — The system should recover automatically 24/7 where the state is deterministically verified and safe to resume. While the state is only partially verified, the platform operates in restricted mode. If any critical state cannot be reconciled with sufficient confidence, the platform must not resume new trading. It must enter NO-TRADE / SAFE MODE, continue recovery and reconciliation where safe, and escalate when human intervention is required.
- **REC-017** Idempotent recovery · CONSTRAINT · DEC-022 — The recovery process must be idempotent and must prevent duplicate orders, duplicate executions, incorrect capital reservations, or inconsistent portfolio state after restart.
- **REC-018** Recovery never bypasses controls · CONSTRAINT · DEC-022 — Automatic recovery must never bypass reconciliation, risk controls, capital controls, policy enforcement, or execution safety.

Lease (REC-013): acquired right after restart, before any step that contacts external systems, and verified again before "authorize resumption" ([DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **REC-019** Split-brain protection across hosts · CONSTRAINT · P2§155, P2§264 — The platform must prevent both local and server instances from simultaneously executing live trades against the same account without authorization. Possible mechanisms: deployment lease; active-instance lock; coordinator; activation token; production ownership state. The exact mechanism requires architecture design.
- **REC-020** One active execution authority per account · CONSTRAINT · P2§156, P2§265 — For each production account there must be a clearly identifiable active execution authority. Other instances may be standby, read-only, development, paper, or recovery, but not accidentally active.
- **REC-021** Failover, if high availability is approved · FUTURE · P2§157, P2§266 — If high availability is eventually approved: failover → check instance ownership → check orders → check positions → check capital → check exchange state → reconcile → activate. Failover must begin with reconciliation.
- **REC-022** Standby activation · CONSTRAINT · P2§158, P2§267 — A standby instance must not automatically become active without: authorization; lease/ownership; state validation; reconciliation. Standby must require explicit activation.

Notes:

- **Already covered.** Recovery after a crash (P2§83, §306) is REC-014 and REC-015. Restart safety (P2§86, §309) is REC-004, REC-015, and RSK-023.
- **The lease and separate hosts (TC-07).** The execution lease (REC-013, TEC-013) is the chosen mechanism for REC-019. It protects instances that share one database. After a local ↔ server migration, the source and destination have separate databases, so the lease alone cannot stop both from trading. The mechanism that closes this gap must be decided before migration is built ([open-question register](../open-questions/register.md), TC-07).
- **REC-021 is FUTURE.** High availability is not approved, so there is no failover. If it is approved, the owner also decides whether "explicit activation" (REC-022) may be a policy authorization or must be a human action.

## Boundary (§92)

- **Owns:** the restart sequence, reconciliation of internal vs venue state, and the safe-resume decision.
- **Consumes:** venue state via the [Exchange Adapter Layer](exchange-adapters.md). Validates against the [Risk Engine](../risk/risk-engine.md), [Global Capital Authority](capital-management.md), [Policy System](policy/policy-system.md), and [Strategy Management](strategy/strategy-management.md).
- **Called by:** the Execution Engine after a timeout (EXE-006).
- **Not yet specified:** mismatch-resolution procedures per mismatch type (expected with Part 2 contracts), interfaces, tests. Resuming is governed by REC-009.

## Findings

Open: TC-07 (split-brain across hosts with separate databases). All earlier findings are resolved: CF-09 → DEC-010 (REC-007, since replaced). DUP-16 → DEC-011 (REC-008). CF-05 → DEC-016. CF-12 → [DEC-022](../decisions/DEC-022-restart-recovery-sequence.md) (REC-014 to REC-018).
