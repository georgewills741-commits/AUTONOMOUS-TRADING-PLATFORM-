# Owner Decisions 34 — The approval to plan Stage 2 and three answers of 2026-11-10, with the owner's message on their conditions

> **Status:** HISTORICAL — source input: the owner's answers of 2026-11-10, 04:31 UTC, to the four questions the builder asked at 02:49 UTC, after the commit of Stage 1's completion certificate (`3b7a41d`) and its machine checks; and the owner's message of 07:04 UTC, queued at 07:02 UTC, which confirms the second, third, and fourth answers and gives their conditions. The answers approve proceeding to Stage 2 planning, X8 of Stage 1's exit checklist; read the daily figure of about 1.2% net of [owner decisions 29](owner-decisions-29-universal-opportunity-intelligence-and-profit-optimization.md) as a measurement only; approve, of adaptive execution (EXE-011), the maker-or-taker decision alone; and keep the certificate's backup branch with the twelve retired ones if its deletion is refused again. This is **not** an active source of truth. The answers and the message are applied through [DEC-067](../decisions/DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md).
>
> **Formatting note:** the four questions were asked together, as multiple choices; each is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the owner's answer as recorded, inside a text block. The owner's message follows, inside one text block, exactly as received. Nothing was added, removed, or changed in what was shown, answered, or written; the headings and the bold field names are the builder's.

## The questions of 2026-11-10, 02:49 UTC, and the answers of 04:31 UTC

### Q1 — Stage 2 planning

**Label shown:** Stage 2

**Question as asked:** Stage 1 (Foundation) is complete and committed (3b7a41d): all three verification gates passed and GitHub's full checks pass on it. Do you approve moving on to Stage 2 (Data Foundation) PLANNING? This is planning only: first the mapping of your 2026-11-06 directive, then Stage 2's plan, which comes back to you for approval before any Stage 2 work begins.

**Options shown:**

- Approve Stage 2 planning (Recommended) — Stage 1 closes. Next: map your 2026-11-06 directive into the requirements, then draft Stage 2's plan for your approval.
- Not yet — Stage 1 stays open. Tell me what you want checked or changed first.

**Owner's answer:**

```text
Approve Stage 2 planning (Recommended)
```

### Q2 — the daily figure of about 1.2%

**Label shown:** 1.2% daily

**Question as asked:** Your 2026-11-06 directive mentions an aspirational daily objective of about 1.2% net, never forced. The existing rules say the platform has no fixed daily percentage (PLT-008) and no fixed daily target (TNP-014), so it never forces trades to reach a number. How should the ~1.2% be read?

**Options shown:**

- Measurement only (Recommended) — Used in reports, such as how often days reach it, never as an input to scanning, sizing, risk or execution. PLT-008 and TNP-014 stay as they are.
- A soft target to steer toward — The system would lean toward reaching it. This changes PLT-008 and TNP-014 and needs a recorded decision, with its risk of pressure to over-trade.

**Owner's answer:**

```text
Measurement only (Recommended)
```

### Q3 — adaptive execution

**Label shown:** Execution

**Question as asked:** Your directive lists 'maker-versus-taker execution decisions' among the execution engine's priorities. Adaptive execution (EXE-011: choosing the order type, splitting orders, pricing to liquidity and volatility) stays future work until you approve it (DEC-027). What does your directive approve, for the stage that builds execution?

**Options shown:**

- Only maker-or-taker (Recommended) — The maker-versus-taker order-type decision is approved. Order splitting and adaptive pricing stay future work until you approve them.
- All of adaptive execution — EXE-011 is approved in full for the stage that builds execution.
- Nothing yet — EXE-011 stays future work. Decide when that stage is planned.

**Owner's answer:**

```text
Only maker-or-taker (Recommended)
```

### Q4 — the certificate's backup branch

**Label shown:** Backup branch

**Question as asked:** This change's temporary backup branch (claude/unverified-backup-x6) is retired in the next change. If this environment again can't delete it, as with the other twelve, may it be kept with those twelve until you remove them?

**Options shown:**

- Keep it with the others (Recommended) — Kept, unused, with the twelve retired branches, until you delete them on GitHub.
- Ask me again then — The next change asks you again when it retires the branch.

**Owner's answer:**

```text
Keep it with the others (Recommended)
```

## 2026-11-10, 07:04 UTC

```text
I approve Measurement only (Recommended) for the approximately 1.2% net daily performance objective.

However, preserve the full meaning of our previously approved trading requirements.

The 1.2% figure is an aspirational performance benchmark, not a mandatory daily target, trading quota, minimum opportunity threshold, or instruction to increase risk.

The platform must continue to:

1. Aggressively and continuously discover genuine opportunities across supported markets, exchanges, assets, and approved strategies.
2. Evaluate both small and large opportunities, including 0.1%, 0.2%, 0.3%, 0.4%, 1%, 1.2%, 2%, and higher net returns where realistically achievable.
3. Select opportunities using executable net profitability, expected dollar profit, risk-adjusted expected value, capital efficiency, liquidity, fees, slippage, execution reliability, and existing safety constraints.
4. Capture the best qualifying opportunities when 1.2% is not achievable, rather than forcing trades.
5. Continue discovering and evaluating opportunities even after daily performance exceeds 1.2%.
6. Accept zero-return, no-trade, and unavoidable loss days without revenge trading or risk escalation.
7. Measure the 1.2% benchmark against actual net whole-account daily returns, correctly accounting for costs and capital changes.

Maintain PLT-008, TNP-014, and all existing risk, capital, execution, security, and AI-authority constraints.

The daily benchmark must not directly determine trade frequency, position sizing, risk limits, execution decisions, or whether scanning continues.

Research and system improvements should aim to improve actual long-term risk-adjusted performance using evidence, not by chasing the benchmark.

Before making changes, inspect the existing canonical requirements. Reuse and reinforce what already exists. Do not introduce duplicate rules, conflicting objectives, additional systems, or unauthorized architectural changes.

Preserve our original objective: discover aggressively, evaluate intelligently, execute selectively, protect capital, and maximize genuine achievable net returns without forcing trades.

Continue the approved work under the established three-gate verification and repository-continuity rules.

I approve Only maker-or-taker (Recommended).

Preserve our company-grade execution architecture and all previously approved requirements.

Maker-versus-taker selection must evaluate the best genuinely executable, risk-adjusted net outcome, accounting for trading fees, slippage, liquidity, fill probability, latency, opportunity expiration, adverse selection, and execution reliability.

Do not automatically prefer maker orders simply because their fees may be lower, or taker orders simply because they execute faster.

Keep advanced order splitting and adaptive pricing as future capabilities under EXE-011, subject to their respective stage planning, approval, implementation, and verification.

This approval does not authorize immediate execution-system implementation during Stage 2 Data Foundation.

When the execution stage is reached, integrate this capability through the existing deterministic Execution Engine without creating duplicate logic, weakening risk or capital controls, or introducing architectural drift.

Preserve the approved three-gate verification process, root-cause correction, and repository traceability.

Continue according to the approved roadmap.

I approve Keep it with the others (Recommended).

Before retiring "claude/unverified-backup-x6", complete the existing canonical reconciliation and verification checks. Confirm that all valid unique work is durably preserved and no active work depends on this branch.

If GitHub refuses deletion again, retain it with the twelve previously retired branches, following DEC-052, DEC-054, DEC-064, and the established repository rules.

Mark it clearly as:

RETIRED — DELETION BLOCKED — NON-AUTHORITATIVE — SAFE TO DELETE WHEN PERMITTED, only when all applicable conditions are verified.

Do not create duplicate archive branches, repeat failed deletion attempts unnecessarily, or treat retained backups as active development branches.

Preserve traceability, prevent unnecessary CI failures and notifications, and ensure that no important work can be lost.

Do not repeatedly ask me for the same decision when the existing approved branch-retirement policy already applies.

Continue the authorized Stage 2 planning process without weakening any security, verification, repository-integrity, or company-grade engineering requirements.
```
