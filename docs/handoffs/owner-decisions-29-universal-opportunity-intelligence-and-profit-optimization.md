# Owner Decisions 29 — Universal opportunity intelligence, profit optimization, and controlled implementation, with the instruction to place its most valuable parts where they belong

> **Status:** HISTORICAL — source input: a message of the owner of 2026-11-06, 11:59 UTC, sent when the session resumed, while the change that repeats Stage 1's stage-transition audit and writes the stage's completion certificate (X6) was in progress. Its first line asks the builder to continue that work, to take the most valuable parts of the directive that follows and put them where they belong, without mistakes, and to ask for any permission it needs on the GitHub repository, such as the permission to delete. The directive, in twenty sections and a final directive, restates the builder's role and the repository audit before any implementation; the platform's objective, aggressive opportunity discovery with conservative risk and capital preservation, and an aspirational daily objective of about 1.2% net that is never forced; universal discovery, small opportunities, and the preference ladder; discovery intensity, multiple exchanges, net profitability, capital allocation, small gains, the coordination of strategies, AI's cost and authority, daily performance, execution quality, performance measurement, and capital protection; and three verification gates, root-cause correction, change management, a workflow, and a final report. This is **not** an active source of truth. It is preserved by [DEC-062](../decisions/DEC-062-preserve-and-map-universal-opportunity-directive.md), which maps its parts to the canonical requirements and applies them through the existing mechanisms ([owner decisions 17](owner-decisions-17-reuse-reinforce-and-enhance-existing-controls.md), Rule 0).
>
> **Formatting note:** the message is reproduced inside one text block exactly as received, including the space that ends its first line and the line break that ends its last. Nothing was added, removed, or changed in it. The title, this banner, and the dated heading are the builder's.

## 2026-11-06, 11:59 UTC

```text
Continue doing what you're doing while taking they use part of this prompt choose the most valuable part and put them to where the belong dont make any mistakes please and if you need permission on Github repository you ask it like the permission to delete 

AUTONOMOUS TRADING PLATFORM — UNIVERSAL OPPORTUNITY INTELLIGENCE, PROFIT OPTIMIZATION & CONTROLLED IMPLEMENTATION

1. ROLE AND OPERATING STANDARD

Act as a senior quantitative trading systems architect, institutional trading infrastructure engineer, algorithmic trading researcher, full-stack engineer, application security engineer, DevOps engineer, and independent QA auditor.

SERIOUS MODE ALWAYS.

This project is a real, company-grade autonomous trading infrastructure platform intended for continuous 24/7 operation, not a simple trading bot, prototype, or demonstration.

Your responsibilities are to inspect, understand, validate, refine, implement, test, and document the platform without introducing unnecessary complexity, conflicting components, duplicate functionality, architectural drift, or unverified claims.

IMPORTANT: The requirements below may already exist partially or completely in the repository. Never assume they are new.

Do not blindly create new modules, files, services, databases, agents, or trading strategies.

First establish what already exists and how the components interact.

Continue from the exact verified repository checkpoint. Do not reset, redesign, or discard working functionality.

---

2. MANDATORY REPOSITORY AUDIT BEFORE IMPLEMENTATION

Before making changes:

1. Inspect the existing repository structure, application architecture, configuration, documentation, source code, tests, database schemas, relevant branches, and active development work.
2. Identify the current implementation stage and latest verified checkpoint.
3. Read the existing master specifications, engineering policies, trading rules, architecture decisions, implementation plans, and verification records.
4. Determine which requirements in this prompt are already implemented, partially implemented, planned, missing, conflicting, or obsolete.
5. Identify functionality that already addresses the same underlying requirement under a different name.
6. Trace shared dependencies before proposing changes.
7. Check current branches and pull requests to avoid repeating work already underway.
8. Examine existing failures and their root causes instead of building parallel workarounds.

Use connected repository-intelligence tools, including Graphify when available and materially useful for dependency analysis, architecture mapping, change impact, or repository-wide understanding.

Do not fabricate findings if a tool or repository is inaccessible.

Required audit classification

For every requirement, determine its status:

- VERIFIED EXISTING: Implemented and supported by current evidence.
- EXISTING BUT INCOMPLETE: Present but missing required functionality.
- IMPLEMENTED BUT UNVERIFIED: Code exists but adequate verification is missing.
- MISSING: No valid implementation exists.
- CONFLICTING: Existing behavior conflicts with approved requirements.
- UNNECESSARY DUPLICATE: Existing components already satisfy the requirement.
- BLOCKED: Cannot safely proceed until a dependency or authorization is resolved.

Record the evidence, affected components, and proposed disposition.

A requirement must not be marked complete merely because its name appears in a document or its code exists.

Verified completion requires appropriate test and operational evidence.

---

3. PRIMARY PLATFORM OBJECTIVE

The platform must continuously discover, evaluate, rank, and capture eligible trading opportunities across supported markets, exchanges, instruments, and strategies.

Its operating philosophy is:

AGGRESSIVE OPPORTUNITY DISCOVERY + INTELLIGENT PROFIT SELECTION + CONSERVATIVE RISK MANAGEMENT + CAPITAL PRESERVATION.

The system should seek substantial profitable opportunities while also taking advantage of smaller, repeatable net-positive opportunities.

Its desired daily profitability objective is approximately 1.2% net or higher when market conditions genuinely support it.

However:

- The daily objective is aspirational, not guaranteed.
- The platform must never force trades to reach it.
- It must never increase unacceptable exposure or leverage to compensate for insufficient returns.
- It must never weaken risk controls to satisfy performance targets.
- It may achieve less than 1.2% if that is what acceptable opportunities provide.
- A 0% day is acceptable.
- Losing days remain possible despite proper controls.
- The platform must not make unsubstantiated claims of profitability.

Capital preservation and risk authorization always take priority over profit targets.

The engineering objective is to improve the probability of capturing legitimate profitable opportunities, not to manufacture or guarantee a specified daily return.

---

4. UNIVERSAL OPPORTUNITY DISCOVERY

Inspect and strengthen the existing universal opportunity-discovery architecture.

The platform should actively search for opportunities across its authorized trading universe, rather than concentrating exclusively on one strategy or return threshold.

Eligible opportunities may include projected net returns such as:

- 0.1%
- 0.2%
- 0.3%
- 0.4%
- 0.5%
- 0.9%
- 1.0%
- 1.2%
- 1.5%
- 2.0%
- 3.0%
- Higher values where legitimately available

These are examples, not guaranteed returns or compulsory execution thresholds.

Do not reject a legitimate 0.1% opportunity solely because the platform is seeking 1.2% daily.

Likewise, do not execute a tiny opportunity merely because its estimated return is positive.

Every opportunity must independently pass profitability, risk, liquidity, execution-quality, and capital-allocation requirements.

Preserve the previously discussed opportunity preference ladder:

3% → 2% → 1.5% → 1% → 0.9% → lower profitable opportunities.

Refinement: The ladder must represent preference and opportunity quality, not a blocking sequence that prevents worthwhile smaller opportunities from being considered while larger opportunities are being searched for.

The platform may evaluate multiple opportunity tiers simultaneously.

---

5. AGGRESSIVE DISCOVERY, NOT AGGRESSIVE RISK

Create or refine an Adaptive Opportunity Intensity Controller using existing infrastructure wherever possible.

Its responsibility is to improve opportunity discovery without weakening execution discipline.

Evaluate:

- Adaptive market-scanning frequency.
- Market prioritization based on demonstrated opportunity quality.
- Expansion across supported liquid trading pairs.
- Cross-exchange opportunity comparisons.
- Concurrent strategy evaluations.
- Market-regime awareness.
- Efficient order-book updates.
- Opportunity expiration and detection latency.
- Detection of changing spreads, volatility, and liquidity.
- Intelligent allocation of computing resources.
- Exchange API rate-limit compliance.
- Avoidance of unnecessary API requests and duplicate scanning.

The system should search aggressively where useful, but it must not waste resources by repeatedly analyzing identical or stale market conditions.

More aggressive scanning must not automatically cause more trades, larger positions, higher leverage, or relaxed risk limits.

---

6. MULTI-EXCHANGE INTELLIGENCE

Support a minimum initial design objective of three connected exchanges, where legally accessible, operationally compatible, and approved for the platform.

Do not assume exchange accounts, API permissions, available balances, or production connectivity already exist.

Inspect existing exchange adapters and inventory-management infrastructure before making additions.

Required capabilities include:

- Concurrent monitoring of multiple exchanges.
- Exchange-to-exchange price comparisons.
- Same-exchange triangular arbitrage route discovery.
- Executable order-book depth analysis.
- Inventory tracking per exchange.
- Available versus locked balance reconciliation.
- Fee schedules and relevant account trading tiers.
- API reliability and response latency.
- Partial-fill and failed-order protection.
- Exchange health scoring.
- Exchange-specific exposure limits.
- Cross-exchange inventory imbalance detection.
- Cost-aware autonomous rebalancing within approved controls.
- Safe exchange isolation when reliability deteriorates.

Pre-positioned inventory should be evaluated where cross-exchange arbitrage would otherwise be too slow.

The platform must account for all capital tied up across exchanges.

Connecting three exchanges creates additional possible trading relationships, but does not guarantee profitable opportunities.

---

7. DYNAMIC NET PROFITABILITY ENGINE

Before authorizing any trade, calculate a conservative estimate of net executable profitability.

Account for relevant costs and execution risks, including:

- Entry and exit trading fees.
- Bid/ask spreads.
- Expected slippage.
- Available market depth.
- Market impact.
- Funding payments.
- Borrowing costs where applicable.
- Transfer and rebalancing costs.
- Partial-fill exposure.
- Hedging or emergency unwind costs.
- Price movement during execution.
- Execution uncertainty and estimation error.
- Required safety margins.

Prevent double counting when costs are already included in executable bid/ask prices.

Do not confuse a gross market spread with actual net profitability.

Implement or refine a dynamic minimum economically worthwhile edge, calibrated to the strategy, market conditions, execution characteristics, and observed uncertainty.

Avoid imposing a universal fixed return floor that unnecessarily rejects good opportunities.

At the same time, reject small theoretical edges that are unlikely to remain profitable after realistic execution.

---

8. INTELLIGENT PORTFOLIO CAPITAL ALLOCATION

Inspect the existing capital allocator and improve it rather than creating a duplicate.

The allocator must coordinate opportunities across strategies, markets, and exchanges.

Evaluate:

1. Expected net dollar profit.
2. Expected return on allocated capital.
3. Expected holding or execution duration.
4. Capital efficiency.
5. Liquidity.
6. Fill probability.
7. Execution uncertainty.
8. Exchange reliability.
9. Correlation and overlapping exposure.
10. Opportunity cost.
11. Available capital.
12. Emergency reserves.
13. Portfolio-wide risk limits.

Compare a small repeatable opportunity with a larger but riskier opportunity using appropriate risk-adjusted measures.

Do not automatically choose the largest percentage return.

Avoid double-committing capital to simultaneous opportunities.

Preserve the ability to execute multiple independently qualified opportunities where sufficient capital and risk capacity exist.

Critical accounting rule:

Profit on deployed capital is not automatically the same as profit on total account equity.

For example, a 0.2% gain on 20% of total capital contributes approximately 0.04% to total account equity, before additional effects.

The system must calculate account-level net profitability correctly.

---

9. MULTIPLE SMALL-GAIN OPPORTUNITY CAPTURE

The platform must support accumulation of small, valid trading gains throughout a 24-hour period.

Examples include individual opportunities earning:

0.1%, 0.2%, 0.3%, 0.4%, and higher net returns.

Several independently profitable trades may collectively produce a larger daily return.

However:

- Never assume a fixed number of opportunities will appear.
- Never impose an arbitrary minimum trade count.
- Never generate trades merely to reach the daily target.
- Never assume every detected opportunity will fill successfully.
- Never ignore losses, failed orders, unused capital, or execution costs.
- Never sum returns from different capital allocations as though each used the full portfolio.
- Use mathematically correct realized P&L, capital-weighted returns, and compounding calculations.

The system should continuously pursue worthwhile opportunities even when achieving the preferred daily return appears unlikely.

A smaller achievable return is preferable to taking unjustified risk in pursuit of an unrealistic target.

---

10. MULTI-STRATEGY COORDINATION

Preserve the established strategy roadmap and deterministic execution architecture.

Review existing support for:

- Cross-exchange arbitrage.
- Triangular arbitrage.
- Statistical arbitrage.
- Funding-rate and basis strategies.
- Directional trading.
- Other approved strategies supported by evidence.

Evaluate additional strategies as research candidates, not automatically authorized production features.

Strategies should compete intelligently for available capital under the same portfolio-level risk authority.

Avoid duplicated market-data services, overlapping execution engines, redundant capital allocators, or conflicting risk systems.

A strategy must demonstrate a credible net edge through appropriate validation before receiving production capital.

---

11. AI INTELLIGENCE AND COST EFFICIENCY

Preserve the existing deterministic-first architecture.

The deterministic core retains authority over:

- Market-data validation.
- Mathematical calculations.
- Order sizing.
- Portfolio accounting.
- Risk controls.
- Trade authorization.
- Order execution.
- Reconciliation.
- Emergency shutdown.
- Recovery.

AI should contribute to:

- Market interpretation.
- Strategy research and analysis.
- Scenario evaluation.
- Performance reviews.
- Explanation of unusual market behavior.
- Detection and investigation of recurring execution problems.
- Recommendations for strategy improvements.

Keep existing specialized AI agents and previously approved conditional activation rules.

Do not create duplicate agents merely because this prompt uses different terminology.

Maintain event-driven AI usage, caching, appropriate model routing, and token/API cost controls.

AI recommendations must never bypass deterministic risk authorization.

---

12. ADAPTIVE DAILY PERFORMANCE MANAGEMENT

Maintain an aspirational daily return objective of 1.2% net or more without converting it into an execution requirement.

The platform must distinguish between:

- Desired daily return.
- Expected return from currently eligible opportunities.
- Realized account-level return.
- Unrealized P&L.
- Remaining capital and risk capacity.
- Current market opportunity quality.
- Forecast uncertainty.

If legitimate opportunities permit 1.5%, the system may capture them.

If conditions only permit smaller profitable outcomes, it should capture eligible opportunities without forcing additional trades.

If conditions do not support safe execution, it must wait.

Do not introduce a rule that increases trading intensity merely because the current daily return is below target.

Continue scanning and evaluating opportunities after achieving the target, but never bypass risk limits or encourage unnecessary turnover.

Evaluate performance over meaningful periods, not only individual successful days.

---

13. EXECUTION QUALITY AND FAILURE PROTECTION

Review and refine the existing execution engine.

Priority areas include:

- Maker-versus-taker execution decisions.
- Conservative slippage modeling.
- Order-book liquidity assessment.
- Opportunity expiration controls.
- Price deterioration checks.
- Partial-fill detection.
- Idempotent order submission.
- Duplicate-order prevention.
- Failed hedge handling.
- Exchange API timeouts.
- Order and balance reconciliation.
- Reliable transaction records.
- Emergency unwind logic.
- Exchange outage isolation.
- Controlled retry behavior.

Retries must never blindly create additional exposure.

Recovery must be based on reconciled exchange and portfolio state.

A process restart must not automatically authorize new trading before health, reconciliation, and risk gates pass.

---

14. PERFORMANCE MEASUREMENT AND EVIDENCE

Strengthen the existing performance analysis infrastructure.

Track:

- Total opportunities detected.
- Opportunities rejected and rejection reasons.
- Opportunities attempted.
- Orders partially and fully filled.
- Gross and net realized profits.
- Losses and transaction costs.
- Profitability by strategy and exchange.
- Profitability by opportunity-size tier.
- Expected versus actual slippage.
- Expected versus realized P&L.
- Capital utilization.
- Turnover and execution efficiency.
- Maximum drawdown.
- Worst trading day.
- Profit factor and risk-adjusted performance.
- Frequency of positive and negative days.
- Daily account-equity return.

Measure how frequently account-level net returns reach or exceed:

1.0%, 1.1%, 1.2%, 1.3%, 1.4%, and 1.5%.

Distinguish simulated, paper-trading, and actual live results.

Never present hypothetical results as verified real performance.

Use statistically meaningful sample sizes and uncertainty estimates.

A successful trading day does not prove a sustainable strategy.

---

15. CAPITAL PROTECTION — NON-NEGOTIABLE

All enhancements must remain subordinate to the canonical risk engine.

Preserve:

- Maximum portfolio exposure.
- Strategy-specific risk budgets.
- Exchange-specific capital limits.
- Concentration limits.
- Drawdown protection.
- Loss-streak safeguards.
- Slippage and liquidity limits.
- Leverage restrictions.
- Exchange health requirements.
- Emergency capital reserves.
- Circuit breakers and kill switches.
- Safe recovery and reauthorization.

The risk engine has final veto authority.

No daily profit target, AI suggestion, strategy, or opportunity ranking may override it.

Capital preservation → Risk authorization → Execution → Profit optimization.

---

16. THREE MANDATORY VERIFICATION GATES

Apply three independent verification gates to each affected implementation stage.

GATE 1 — Architecture and Consistency

Verify that:

- Changes respect existing requirements.
- No duplicate modules or conflicting responsibilities were introduced.
- Interfaces and dependencies are consistent.
- Existing working functionality is preserved.
- Security boundaries remain intact.
- Architectural decisions are traceable.

GATE 2 — Functional and Quantitative Correctness

Verify that:

- Relevant automated tests pass.
- Profit calculations are mathematically correct.
- Simulations include realistic trading costs.
- Capital allocation avoids double counting.
- Risk controls reject unsafe trades.
- Opportunity discovery behaves correctly.
- Failure and recovery scenarios are tested.
- Regressions are investigated and resolved.

GATE 3 — Operational Readiness

Verify that:

- Paper-trading evidence supports the expected behavior.
- Out-of-sample testing and stress tests are satisfactory.
- Monitoring and alerting work.
- Exchange and infrastructure failures are handled safely.
- Reconciliation and restart behavior are correct.
- Required security and deployment controls pass.
- Live-canary criteria are explicitly met before real-capital activation.

An unverified or failed gate must remain marked accordingly.

Never claim that passing source-code tests proves live profitability.

Do not expand live exposure without approved capital controls and evidence.

---

17. ROOT-CAUSE CORRECTION AND ANTI-LOOP RULE

When an issue is discovered:

1. Reproduce or establish evidence of the issue.
2. Trace its root cause.
3. Identify the affected dependencies.
4. Correct the underlying cause where safely possible.
5. Add appropriate regression coverage.
6. Verify that the correction does not introduce another conflict.
7. Update the canonical documentation.
8. Record the verification evidence.

Do not repeatedly patch symptoms.

Do not recreate features because the previous implementation is difficult to understand.

Do not rename components unnecessarily.

Do not introduce overlapping controllers, repeated business rules, or competing sources of truth.

If repeated approaches fail, stop repeating the same attempt and investigate the underlying assumption or dependency.

---

18. REPOSITORY CHANGE MANAGEMENT

Maintain professional traceability.

Before editing, establish the current repository state, relevant branch, active changes, and verified checkpoint.

For every implementation:

- Make coherent, scoped changes.
- Preserve unrelated working code.
- Keep configuration and secrets secure.
- Add or update necessary tests.
- Update existing canonical documentation instead of creating unnecessary parallel specifications.
- Record architectural decisions where appropriate.
- Keep commits focused and traceable.
- Document genuine blockers.
- Do not claim a commit, test, deployment, or verification happened unless evidence confirms it.

Never silently remove or weaken an existing requirement.

If a proposed improvement conflicts with a previous approved rule, identify the conflict and resolve it through the established decision process before implementation.

Use tools efficiently and avoid unnecessary repeated repository scans, AI calls, or token-heavy analysis.

---

19. REQUIRED WORKFLOW

Execute in this order:

Phase A — Inspect

Establish repository state, existing architecture, prior requirements, active work, and verified checkpoints.

Phase B — Compare

Map every requirement in this prompt to existing implementation and documentation.

Phase C — Decide

Classify each requirement as retain, refine, implement, consolidate, verify, reject as duplicate, or block pending a dependency.

Explain the reason and evidence.

Phase D — Implement

Make the smallest coherent set of changes that achieves the approved behavior.

Reuse functioning infrastructure.

Proceed autonomously where access and safety permit.

Phase E — Verify

Apply the three verification gates and run relevant tests, simulations, integration checks, and failure scenarios.

Phase F — Document

Update the canonical state, implementation evidence, remaining risks, and exact continuation checkpoint.

Phase G — Continue

Advance through eligible implementation work without resetting completed stages or repeatedly asking for information already available.

Stop only where a genuine safety, authorization, external-service, capital-allocation, or unresolved technical blocker prevents responsible continuation.

Never present unfinished work as complete.

---

20. FINAL DELIVERABLES AND REPORTING

Provide a precise implementation and verification report containing:

1. The verified starting checkpoint.
2. The requirements already satisfied.
3. Existing requirements that needed refinement.
4. Genuinely missing requirements implemented.
5. Duplicate or conflicting implementations prevented or consolidated.
6. Files and components changed.
7. Quantitative and functional tests performed.
8. Results for each of the three verification gates.
9. Outstanding blockers and risks.
10. Evidence-backed performance findings, if available.
11. The exact updated repository checkpoint.
12. The safest next implementation task.

Separate verified facts from assumptions and research hypotheses.

Do not fabricate tests, trading outcomes, repository changes, or production readiness.

---

FINAL NON-NEGOTIABLE DIRECTIVE

This project must remain a coherent, company-grade autonomous trading infrastructure platform.

Do not drift from the approved architecture.

Do not duplicate existing functionality.

Do not compromise capital preservation.

Do not force trades to meet a daily profitability target.

Do not treat positive theoretical spreads as guaranteed profits.

Do not confuse profitable individual trades with returns on total account equity.

Do not claim performance without verified evidence.

Discover opportunities aggressively. Evaluate them intelligently. Allocate capital efficiently. Execute selectively. Protect capital continuously. Measure results objectively.

The objective is to maximize the capture of legitimate, repeatable, risk-adjusted net trading opportunities—including small gains—while preserving the integrity, safety, consistency, and long-term reliability of the entire platform.

BEGIN WITH THE REPOSITORY AUDIT. PRESERVE THE EXISTING CHECKPOINT. IMPLEMENT ONLY WHAT IS GENUINELY NECESSARY.

```
