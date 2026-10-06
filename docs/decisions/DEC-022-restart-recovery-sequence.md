# DEC-022 — Staged restart recovery: persisted state is untrusted until reconciled

- **Status:** ACCEPTED
- **Later changes:** The options shown with the question are now preserved in [owner decisions 2: options shown](../handoffs/owner-decisions-02-options-shown.md) ([DEC-037](DEC-037-final-decision-and-integrity-checkpoint.md)); the statement under "Alternatives considered" that they are not in the repository no longer holds. The text below is kept as written.
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 2, CF-12](../handoffs/owner-decisions-02-cf-11-to-cf-13.md))
- **Resolves:** CF-12
- **Supersedes:** REC-007 ([DEC-010](DEC-010-pre-trade-decision-flow.md): verify the database before loading) and REC-011 ([DEC-019](DEC-019-company-grade-autonomous-operating-model.md): the OC-1 item 11 recovery sequence)

## Decision

| Requirement | What it says |
|---|---|
| REC-014 | Persisted state may be loaded as recovery context but is never trusted as authoritative financial state; it is compared against authoritative external state |
| REC-015 | The canonical recovery sequence, from RESTART to RESUME NORMAL OPERATION, as the owner wrote it |
| REC-016 | Outcomes: automatic resumption when deterministically verified and safe; restricted operation while partly verified; NO-TRADE / SAFE MODE with continued recovery and escalation when critical state cannot be reconciled with sufficient confidence |
| REC-017 | Recovery is idempotent and prevents duplicate orders or executions, wrong capital reservations, and inconsistent portfolio state |
| REC-018 | Automatic recovery never bypasses reconciliation, risk controls, capital controls, policy enforcement, or execution safety |
| AUD-009 | Every recovery step, discrepancy, reconciliation result, decision, and final operating state is recorded in the audit trail |

## Carried forward from REC-011 (not removed)

REC-011 (OC-1 item 11) included a "partially safe → restricted operation" outcome. The owner's new sequence passes through "ENTER SAFE/RESTRICTED MODE" and does not remove that outcome, so it is carried into REC-016.

## How this fits the other recovery requirements (no conflict)

| Requirement | Relationship |
|---|---|
| REC-002 (§71 handoff sequence) | Kept as written. REC-015 contains every §71 step in more detail ("fetch fills" is part of fetching authoritative external state; "resolve mismatches" is governed by REC-016) |
| REC-012 (OC-1 item 14, recovery failure handling) | Consistent; unchanged |
| REC-013 (OC-1 item 15, execution lease) | Still in force. REC-015 does not mention the lease; REC-013 requires it to be established *first*. So the lease is acquired right after restart, before any external step, and verified again before AUTHORIZE RESUMPTION |
| RSK-023 (kill-switch recovery) | The same verify-then-resume discipline, applied per trip rather than per restart |

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **REC-007's order** ([DEC-010](DEC-010-pre-trade-decision-flow.md)): verify database integrity before loading any state.
- **The order of §71 and REC-011** (OC-1 item 11): load state, then verify the database. REC-011 also checked capital, positions, and orders before reconciliation, where §71 validates capital after it.
- **The builder's proposal** (CF-12): rely on no loaded state until database integrity is verified; check internal consistency before reconciliation, and validate again against exchange state after it.
- The owner's own answer replaced REC-007 and REC-011 (REC-014 to REC-016): persisted state is loaded first, as recovery context, but "must never be blindly trusted as authoritative financial state" and "should be compared against authoritative external state rather than assumed correct" (REC-014).
- The options listed with the question are not in the repository: [owner decisions 2](../handoffs/owner-decisions-02-cf-11-to-cf-13.md) records the question and the owner's free-text answer only. They are not reconstructed here.
