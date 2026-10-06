# Owner Decisions 2 — Options shown with the questions

> **Status:** HISTORICAL — source input: the options shown to the owner on 2026-09-30 with the three questions of [owner decisions 2](owner-decisions-02-cf-11-to-cf-13.md), which holds the owner's answers. This is **not** an active source of truth. The answers are applied through [DEC-021](../decisions/DEC-021-kill-switch-recovery.md), [DEC-022](../decisions/DEC-022-restart-recovery-sequence.md), and [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md). Preserved on 2026-10-05 from the session record ([DEC-037](../decisions/DEC-037-final-decision-and-integrity-checkpoint.md)), closing the second part of the master knowledge-base audit's finding A-17.
>
> **Formatting note:** each question is recorded with the short label shown above it, the question as asked, and the options shown (label, then description), exactly as shown. The owner wrote each answer instead of choosing an option; the answers are in owner decisions 2, not repeated here. The question headings and the bold field names are the builder's.

## CF-11

**Label shown:** Kill switch

**Question as asked:** CF-11: Who may reset a kill switch after it trips? The current rule is operator-only, so any automatic trip (for example an exchange API outage) stops that part of the platform until you act, even after the problem clears.

**Options shown:**

- Reset by cause (Recommended) — Recoverable, measurable causes (exchange or API instability, stale data, slow performance, liquidity collapse) reset automatically once cleared for a policy-set period and recovery checks pass. Security events, unknown balances, loss-based trips, and switches you activated need your reset.
- Always manual — Keep the current rule: only you can reset any kill switch. Safest, but the platform stays stopped in that area until you act, even at 3 a.m.
- Always automatic — Every kill switch resets automatically once its condition clears and checks pass, including loss-based ones such as repeated losses. Most autonomous, but a losing strategy could restart without review.

## CF-12

**Label shown:** Recovery

**Question as asked:** CF-12: After a restart, in what order should saved state and the database be checked? This is low impact: every option still requires all checks to pass before trading resumes.

**Options shown:**

- Verify before trusting (Recommended) — Saved state may be loaded first, but nothing loaded is used until the database is verified. Capital, position, and order checks are repeated against exchange data after reconciliation. Satisfies Part 1, your correction, and the current rule together.
- Strict verify-first — Keep the current rule exactly: verify the database before loading anything from it.

## CF-13

**Label shown:** Approval

**Question as asked:** CF-13: Part 1's strategy lifecycle has an APPROVAL stage before canary (live trading with small capital). Who performs that approval?

**Options shown:**

- Automatic by default (Recommended) — The platform's deterministic readiness checks count as approval, so canary starts automatically as your correction describes. You can mark all strategies, or specific ones, as needing your approval in policy.
- Human for new strategies — The first live deployment of a brand-new strategy needs your approval. New versions of a strategy that is already live go through automatic approval.
- Always human — Every new strategy and every new version needs your approval before canary. Maximum control, but less autonomy than your correction describes.
