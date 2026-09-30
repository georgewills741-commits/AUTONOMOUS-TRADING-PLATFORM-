# DEC-026 — Safety floor and layered control model

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 3, Q1](../handoffs/owner-decisions-03-part-2-findings.md))
- **Resolves:** CF-14

## Decision

The owner answered CF-14 with a layered control model. System-safety invariants stay at the top and nobody can bypass them: not an AI agent, a strategy, a policy, an administrator, or an automatic process. Above that floor, everything operational is configurable and may adapt automatically.

| Requirement | What it says |
|---|---|
| RSK-034 | The immutable safety invariants, as the owner listed them. They cannot be overridden, and the safety floor is not the same thing as ordinary operational limits |
| RSK-035 | The configurable policy layer: capital allocation, strategy limits, exposure limits, execution parameters, opportunity thresholds, and other operational policies may be changed automatically or administratively, but only inside the safety envelope |
| RSK-036 | Adaptive operation: the platform may adjust operational limits, execution methods, capital allocation, strategy availability, and opportunity thresholds to conditions, without violating an invariant |
| RSK-037 | Recovery and fail-safe behavior: diagnose, recover safely, revalidate, and resume only when safety is satisfied |
| RSK-038 | No deadlock by safety: isolate what is affected and keep healthy parts running where safe |
| RSK-039 | Changing an invariant needs a formal, versioned, audited, human-controlled policy change. AI may analyze and propose such a change, never authorize or implement it |
| PLT-021 | The objective: maximum autonomy inside a deterministic safety envelope, 24/7, recovering intelligently without giving up the safety guarantees |

## CF-14 outcome

System safety stays first, so RSK-004 is unchanged. Part 2's "user hard policy above system safety" (P2§101, §279) is not adopted in that form: an invariant can only be changed through RSK-039, never overridden. The other rule of P2§101, that no lower layer may override a higher hard constraint, is RSK-005.

## How this fits the existing requirements (builder reading; the owner may correct it)

| Requirement | Relationship |
|---|---|
| RSK-010 (system safety rules, [DEC-012](DEC-012-safety-architecture.md)) | The safety floor is RSK-034's list together with RSK-010's rules. Both define the same top layer, and where they overlap they are one rule. RSK-010 adds: no order unless system health permits; no order without Risk Engine authorization and a capital reservation; no real order outside live mode; active kill switches are always respected; orders satisfy exchange rules; trading credentials cannot withdraw |
| HARD LIMIT values (V-08, V-12, V-17, V-29) | These are the numbers inside the invariants: absolute risk boundaries, data freshness, reconciliation confidence. Changing one is an RSK-039 change |
| POL-005 to POL-007 (policy change governance) | They still govern changes to the operator's policy, meaning the bounds and authorizations: absolute limits, authorized capital, leverage, venues, instrument types, hard constraints, human-controlled gates, and the platform's maximum mode. RSK-036's adjustments happen inside those bounds. Like dynamic capital allocation (CAP-006) and dynamic canary allocation (STR-015), they are operating decisions, not policy changes needing confirmation, and they are versioned and audited. Widening a bound or an authorization still needs the operator |
| PLT-020, POL-011 | Adaptive operation never invents authorization. An unset bound still means the action it governs is not authorized |
| RSK-021 to RSK-025 (kill-switch recovery) | RSK-037 applies the same discipline to every safety block. Causes that RSK-022 latches still wait for authorization |
| RSK-020 (actions scoped to what is affected) | RSK-038 generalizes it |
| PLT-014 (human intervention by exception) | Invariant changes (RSK-039) are among the human-controlled changes |
| RSK-003, AIL-003 | RSK-034's last invariant says the same for AI |
| EXE-011 (adaptive execution, FUTURE, [DEC-027](DEC-027-part-2-open-questions.md)) | RSK-036 allows execution methods to be adjusted. The adaptive-execution feature itself is built only when the owner approves it |
