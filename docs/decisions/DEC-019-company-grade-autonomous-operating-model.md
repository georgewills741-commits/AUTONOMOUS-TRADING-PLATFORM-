# DEC-019 — Company-grade autonomous operating model

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner, in the directive [Owner correction 1: company-grade autonomous operating defaults](../handoffs/owner-correction-01-autonomous-operating-defaults.md) ("OC-1"). Items 1–30 and 32–33 are applied here; item 31 is applied in [DEC-020](DEC-020-value-classification.md).
- **Supersedes in part:** [DEC-012](DEC-012-safety-architecture.md), [DEC-015](DEC-015-modes-canary-and-policy-governance.md), [DEC-017](DEC-017-reporting-alerting-and-performance-targets.md)
- **Raised for owner review:** CF-11, CF-12, CF-13 ([findings register](../conflicts/register.md)); decided by the owner in [DEC-021](DEC-021-kill-switch-recovery.md), [DEC-022](DEC-022-restart-recovery-sequence.md), [DEC-023](DEC-023-autonomous-canary-approval.md)
- **Later changes:** REC-011 is superseded by DEC-022

## Context

After the Part 1 open items were resolved, five operating defaults were shown to the owner:

- rebalancing needs confirmation
- emergency cancels orders but keeps positions
- no automatic resume after restart
- canary at 5% for 14 days and 50 trades
- 50 ms / 500 ms latency targets

The owner replaced them. The platform is to be a production-grade autonomous financial platform operating 24/7: "automatic + verified", autonomous without being uncontrolled.

## Decision

The operating model is autonomous within policy, risk, and capital boundaries; evidence-driven; self-monitoring; self-recovering; and reconciliation-aware. Human intervention is for exceptions only. Concretely:

| Area | Model | Canonical requirements |
|---|---|---|
| Autonomy | Act autonomously when authority, capital, information, infrastructure health, and state certainty suffice; otherwise wait, don't act, reconcile, or enter a safety state | PLT-013, PLT-014, PLT-015 |
| Rebalancing | Autonomous, economically justified, policy-bounded; never invents authorization | CAP-023, CAP-024, CAP-025 |
| Transfer authority and security | Three separate authorities; restricted transfer credentials; full transfer audit record | SEC-006, SEC-007, AUD-007 |
| Transfer execution | Timeout ≠ failure; query venue and blockchain; no duplicate transfers; reconcile | EXE-009, EXA-010 |
| Emergency | Graduated deterministic safety levels; response by emergency type; policy-driven position handling; no AI; idempotent actions | RSK-015 to RSK-020, HLT-011 |
| Restart and recovery | Automatic restart, reconciliation, and health checks, then automatic safe resumption; restricted or SAFE MODE when state is uncertain; lease-protected active instance | REC-010 to REC-013, HLT-012, EXE-010, OPS-006, TEC-013 |
| Canary | Readiness-driven automatic canary; dynamic allocation within policy; gradual scaling; automatic stop and rollback; evidence, not time alone | STR-013 to STR-018, MODE-007 |
| Performance | Measured, path-specific budgets; percentile metrics; hard limits vs soft targets vs observed; latency in the economics; automatic degradation handling | PERF-008 to PERF-012, TNP-023 |
| Boundaries live in policy | All the limits above are policy values, not code | POL-011 |

## Requirements superseded

Each is marked DEPRECATED / REPLACED in its specification; its text is kept for traceability.

| Superseded | Replaced by | Reason |
|---|---|---|
| CAP-022 (transfers need confirmation) | CAP-023, CAP-024, CAP-025 | OC-1 items 1, 3, 30 |
| SEC-003 (trading keys cannot withdraw; transfer key tied to CAP-022) | SEC-006 | OC-1 item 4. The no-withdrawal rule for trading keys is carried into SEC-006 |
| HLT-007 (overall platform states incl. SAFE MODE / TRADING HALTED / EMERGENCY) | HLT-011, RSK-015 | OC-1 item 8 introduces graduated safety levels; health and safety level are separated |
| HLT-008 (trading per state; EMERGENCY cancel-only) | RSK-015, RSK-016, RSK-017 | OC-1 items 7–9, 30 |
| HLT-009 (leaving SAFE MODE / EMERGENCY requires the operator) | HLT-012, RSK-020 | OC-1 items 8 (CRITICAL RECOVERY → RESUME), 13, 14, 29 |
| REC-009 (resume needs the operator unless enabled) | REC-010 to REC-013 | OC-1 items 11–15, 30 |
| STR-011 (canary: 5%, 14 days, 50 trades) | STR-013 to STR-018 | OC-1 items 16–21, 30, 31 |
| MODE-004 (more permissive mode needs operator confirmation) | MODE-007 | Contradicts OC-1 item 17 ("only then may the platform automatically enter canary operation") |
| PERF-007 (50 ms / 500 ms targets) | PERF-008 to PERF-012 | OC-1 items 22–27, 30, 31. The numbers are kept only as DESIGN TARGETS (DEC-020) |

## Conflicts surfaced for owner review (OC-1 item 33)

These are **not** changed by this decision. The existing requirement stays in force until the owner decides.

- **CF-11:** kill-switch reset. RSK-009 (operator-only reset) vs OC-1's exception-based human intervention.
- **CF-12:** recovery ordering. REC-007 (verify database before loading) vs OC-1 item 11 and §71 (load, then verify).
- **CF-13:** the lifecycle APPROVAL stage (§34, §38) vs automatic canary entry.

## Reconciliation notes (no conflict)

| Point | Why it is consistent |
|---|---|
| OC-1 item 11 verifies ownership near the end; item 15 acquires the lease first | Both hold: the lease is acquired first and verified again before the recovery decision (REC-013) |
| §45 / ARB-005: no automatic transfer after every arbitrage trade | Same principle as CAP-023 ("not simply because balances are unequal") |
| ARB-006 (§45 evaluation inputs) vs CAP-024 (decision considerations) | DEC-011 split: Arbitrage Intelligence evaluates, the Global Capital Authority decides |
| DEC-006 custody FUTURE vs transfers | Rebalancing between the operator's own venue accounts is not custody. The platform holds no general withdrawal or custody authority (SEC-006). Querying the status of its own transfers on-chain is not the custody-scale "blockchain monitoring" of CUS-002 |
| TNP-005 (no universal minimum profit threshold) vs TNP-023 (reject opportunities likely to vanish) | Latency decay is part of each opportunity's economics, not a threshold |
| POL-005 (important policy changes need confirmation) | Matches OC-1 item 29 ("policy changes requiring approval") |
| PFC-008 (controller's own permitted actions) vs PERF-011 actions | The Performance Controller detects; the Risk Engine applies the restrictions through safety levels |
| HLT-001 (§74 state names) | Kept as written; HLT-011 maps each name to a health state or a safety level |

## Traceability: OC-1 item → result

| Item | Result |
|---|---|
| 1 | CAP-023 |
| 2 | CAP-024 |
| 3 | CAP-025 |
| 4 | SEC-006 |
| 5 | SEC-007, AUD-007 |
| 6 | EXE-009, EXA-010 |
| 7 | RSK-016 |
| 8 | RSK-015, HLT-011, RSK-020 |
| 9 | RSK-017, RSK-018 |
| 10 | RSK-019 |
| 11 | REC-011 (CF-12) |
| 12 | REC-010, OPS-006, TEC-013 |
| 13 | REC-010, REC-011, HLT-012 |
| 14 | REC-012, OPS-006 |
| 15 | REC-013, EXE-010, TEC-013 |
| 16 | STR-013, STR-014 |
| 17 | STR-013, STR-014, MODE-007 (CF-13) |
| 18 | STR-015 |
| 19 | STR-016 |
| 20 | STR-017 |
| 21 | STR-018 |
| 22 | PERF-008 |
| 23 | PERF-009 |
| 24 | PERF-010 |
| 25 | TNP-023 |
| 26 | PERF-011 |
| 27 | PERF-012 |
| 28 | PLT-013 |
| 29 | PLT-014 |
| 30 | The supersession table above |
| 31 | [DEC-020](DEC-020-value-classification.md): ARCH-018, values register |
| 32 | PLT-015 |
| 33 | This reconciliation; CF-11 to CF-13 |
| Closing note ("automatic + verified") | Recorded as the intent behind PLT-013 and PLT-015 |

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **The five operating defaults shown to the owner before this decision** (Context): rebalancing needs confirmation; emergency cancels orders but keeps positions; no automatic resume after restart; canary at 5% for 14 days and 50 trades; 50 ms / 500 ms latency targets. The owner replaced them with the model above ([OC-1](../handoffs/owner-correction-01-autonomous-operating-defaults.md)). The requirements that held them are DEPRECATED / REPLACED ("Requirements superseded" above).
- **Other approaches OC-1 rules out, each set against the one it wants:**
  - moving funds whenever balances differ: "The platform should not move funds simply because balances are unequal" (item 1; CAP-023);
  - closing every position in an emergency: "The system must not blindly close every position during an emergency" (item 9; RSK-017);
  - readiness from elapsed time alone: "A strategy should not become production-ready merely because: “14 days passed.”" (item 21; STR-018);
  - waiting for the owner to activate canary by hand: "rather than waiting for you to manually activate it" (closing note; STR-014);
  - "restart → immediately send orders", set against "restart → reconcile → verify → resume automatically" (closing note; REC-010 to REC-013).

## Consequences

- Autonomous rebalancing, automatic canary, and automatic resumption cannot run until their policy boundaries are set (POL-011; values register). An unset boundary means that autonomous action is outside authorization (CAP-025, PLT-015).
- Implementation is still not authorized (handoff §101).
