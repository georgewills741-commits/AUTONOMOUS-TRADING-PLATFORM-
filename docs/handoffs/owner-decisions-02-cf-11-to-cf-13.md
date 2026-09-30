# Owner Decisions 2 — CF-11, CF-12, CF-13

> **Status:** HISTORICAL — source input: the owner's answers of 2026-09-30 to the three conflicts raised by owner correction 1. This is **not** an active source of truth. Each answer is applied through the decision record linked under it.
>
> **Formatting note:** questions are quoted as asked. Each answer is reproduced inside a text block exactly as given; nothing was added, removed, or changed. The owner wrote each answer as free text rather than choosing a listed option.

## CF-11

**Question as asked:** CF-11: Who may reset a kill switch after it trips? The current rule is operator-only, so any automatic trip (for example an exchange API outage) stops that part of the platform until you act, even after the problem clears.

**Applied by:** [DEC-021](../decisions/DEC-021-kill-switch-recovery.md)

**Owner's answer (verbatim):**

```text
Cause-based, risk-aware automatic recovery with escalation.

The platform must automatically recover from known, transient and measurable infrastructure conditions such as temporary exchange/API instability, connectivity interruptions, stale market data, rate-limit conditions, or temporary performance degradation, but only after the triggering condition has cleared and deterministic recovery checks pass.

Kill switches triggered by security events, unknown financial state, unexplained or abnormal losses, data-integrity failures, suspected duplicate execution, reconciliation failures, custody/withdrawal issues, repeated abnormal behavior, or any other high-risk or uncertain condition must remain latched and require explicit authorization before reset.

Recovery must be progressive and scoped:

TRIPPED → DIAGNOSE → WAIT FOR CONDITION TO CLEAR → HEALTH CHECKS → RECONCILIATION → SAFE/RESTRICTED MODE → LIMITED RECOVERY → FULL OPERATION

Before resuming affected trading, verify exchange connectivity, market-data freshness, balances, positions, open orders, capital reservations, risk state, policy state, and execution state.

The system must not automatically resume full trading merely because the original error appears to have disappeared.

If recovery fails, repeatedly trips, or the system cannot establish a known-safe state, remain in SAFE MODE / NO-TRADE and escalate to the operator.

Recovery actions, triggers, checks, decisions, and final states must be recorded in the audit trail.

Automatic recovery must never override higher-level safety, security, policy, financial-integrity, or reconciliation requirements.

The system is intended to operate autonomously 24/7, so ordinary transient failures should recover automatically where safe, while serious or uncertain conditions require human authorization.
```

## CF-12

**Question as asked:** CF-12: After a restart, in what order should saved state and the database be checked? This is low impact: every option still requires all checks to pass before trading resumes.

**Applied by:** [DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)

**Owner's answer (verbatim):**

```text
After restart, use a staged recovery and reconciliation process. Persisted state may be loaded as recovery context, but it must never be blindly trusted as authoritative financial state.

The recovery sequence should be:

RESTART
→ LOAD PERSISTED STATE AS UNTRUSTED RECOVERY CONTEXT
→ VERIFY DATABASE INTEGRITY
→ VERIFY SCHEMA / VERSION
→ VERIFY CONFIGURATION AND POLICY
→ VERIFY EXCHANGE CONNECTIVITY AND HEALTH
→ FETCH AUTHORITATIVE EXTERNAL STATE
→ RECONCILE BALANCES
→ RECONCILE POSITIONS
→ RECONCILE OPEN ORDERS
→ RECONCILE CAPITAL RESERVATIONS
→ RECONCILE PENDING TRANSFERS
→ VERIFY RISK STATE
→ VERIFY STRATEGY STATE
→ VERIFY MARKET-DATA FRESHNESS
→ VERIFY EXECUTION STATE
→ RUN SAFETY CHECKS
→ ENTER SAFE/RESTRICTED MODE
→ AUTHORIZE RESUMPTION
→ RESUME NORMAL OPERATION

Persisted state should be compared against authoritative external state rather than assumed correct.

If any critical state cannot be reconciled with sufficient confidence, the platform must NOT resume new trading. It must enter NO-TRADE / SAFE MODE, continue recovery and reconciliation where safe, and escalate when human intervention is required.

The system should recover automatically 24/7 where the state is deterministically verified and safe to resume. Automatic recovery must never bypass reconciliation, risk controls, capital controls, policy enforcement, or execution safety.

The recovery process must be idempotent and must prevent duplicate orders, duplicate executions, incorrect capital reservations, or inconsistent portfolio state after restart.

Every recovery step, discrepancy, reconciliation result, decision, and final operating state must be recorded in the audit trail.
```

## CF-13

**Question as asked:** CF-13: Part 1's strategy lifecycle has an APPROVAL stage before canary (live trading with small capital). Who performs that approval?

**Applied by:** [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md)

**Owner's answer (verbatim):**

```text
Policy-driven autonomous approval.

The platform’s deterministic Governance and Readiness Engine performs the approval automatically when all mandatory readiness, risk, validation, capital, data-integrity, liquidity, execution, and operational checks pass.

A strategy may enter canary automatically only when it satisfies the defined eligibility policy and sufficient capital is available. The canary allocation, exposure limits, duration, and promotion criteria are enforced by deterministic controls.

Human approval is required only when policy explicitly marks a deployment as requiring human authorization, such as a brand-new strategy class, material risk-model change, exceptional capital increase, security-sensitive change, or any unresolved governance exception.

No AI agent or human may bypass the deterministic safety gates. Failure of any mandatory gate prevents canary deployment and places the strategy into a blocked/readiness-failed state until the required conditions are satisfied.
```
