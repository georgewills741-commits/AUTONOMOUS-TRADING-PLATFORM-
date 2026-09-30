# DEC-021 — Cause-based, risk-aware kill-switch recovery with escalation

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 2, CF-11](../handoffs/owner-decisions-02-cf-11-to-cf-13.md))
- **Resolves:** CF-11
- **Supersedes:** RSK-009 ([DEC-012](DEC-012-safety-architecture.md): only the operator could reset a kill switch)

## Decision

Ordinary transient failures recover automatically where safe. Serious or uncertain conditions stay latched until someone explicitly authorizes a reset.

| Requirement | What it says |
|---|---|
| RSK-021 | Automatic recovery for known, transient, measurable infrastructure conditions, only after the condition has cleared and deterministic recovery checks pass |
| RSK-022 | Latched kill switches for security events, unknown financial state, abnormal losses, data-integrity failures, suspected duplicate execution, reconciliation failures, custody/withdrawal issues, repeated abnormal behavior, and any other high-risk or uncertain condition |
| RSK-023 | Progressive, scoped recovery (TRIPPED → … → FULL OPERATION), with the state verified before affected trading resumes. Full trading never resumes merely because the error seems gone |
| RSK-024 | Failed or repeatedly tripping recovery → SAFE MODE / NO-TRADE and escalation |
| RSK-025 | Recovery never overrides higher-level safety, security, policy, financial-integrity, or reconciliation requirements |
| AUD-008 | Recovery actions, triggers, checks, decisions, and final states are recorded in the audit trail |

## Carried forward from RSK-009 (not removed)

RSK-009 also said that kill switches may be activated automatically by deterministic rules or by the operator, and that AI cannot activate or reset a kill switch, only recommend activation. The owner's answer does not change either point, so both carry into RSK-025 (constitution Rule 56: no silent removal).

## Interpretation (builder), for owner awareness

The answer makes automatic recovery apply to "known, transient and measurable infrastructure conditions", and keeps "any other high-risk or uncertain condition" latched. A cause in neither list therefore stays latched by default. That includes a kill switch the operator activated by hand, which is a human decision rather than a transient infrastructure condition. RSK-022 states this default. The classification of causes is a policy value (V-27 in the [values register](../requirements/values-register.md)).
