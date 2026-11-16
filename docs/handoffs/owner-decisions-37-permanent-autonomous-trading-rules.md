# Owner Decisions 37 — Permanent autonomous trading rules of 2026-11-16: policy enforcement, intelligent opportunity discovery, and capital protection

> **Status:** HISTORICAL — source input: the owner's message of 2026-11-16, 18:54 UTC, delivered while the builder worked: a master directive that restates, for the platform's permanent operating policies, the trading rules of the owner's directive of 2026-11-06 ([owner decisions 29](owner-decisions-29-universal-opportunity-intelligence-and-profit-optimization.md)) and of the owner's answers of 2026-11-10 ([owner decisions 34](owner-decisions-34-approval-to-plan-stage-2-and-answers-on-the-directive.md)): aggressive opportunity discovery, intelligent evaluation, efficient capital allocation, selective execution, strict capital protection, and no forced trading; the daily figure of about 1.2% net as an objective, never a quota; and their integration into the existing application without duplication, under the three gates. It opens by asking whether the builder understands it; DEC-070 records the builder's answer: each of its points is already stated by the canonical requirements, with nothing to add and no conflict. This is **not** an active source of truth. It is preserved by [DEC-070](../decisions/DEC-070-permanent-trading-rules-mapped.md), which maps it to the canonical requirements that state its rules.
>
> **Formatting note:** the message is reproduced inside one text block exactly as received. Nothing was added, removed, or changed in it. The title, this banner, and the dated heading are the builder's.

## 2026-11-16, 18:54 UTC

```text
hope you understand what this is tell me if you understand you should be smart enough to know what to do here



PERMANENT AUTONOMOUS TRADING RULES
COMPANY-GRADE TRADING PLATFORM — POLICY ENFORCEMENT, INTELLIGENT OPPORTUNITY DISCOVERY, AND CAPITAL PROTECTION
MASTER DIRECTIVE FOR CLAUDE CODE
OPERATING MODE: SERIOUS MODE ALWAYS
This instruction applies to the autonomous trading company application currently under development.
THIS IS NOT A REQUEST TO BUILD A NEW TRADING PLATFORM, REDESIGN THE EXISTING SYSTEM, OR RESTART IMPLEMENTATION.
The application already has an established architecture, trading engines, operating policies, safety requirements, and development history.
Your responsibility is to ensure that the trading rules described below are correctly incorporated into the existing application's permanent operating policies.
Some or most of these requirements may already exist.
Therefore, your first responsibility is to identify what is already implemented, what needs stronger enforcement, what is incomplete, and what is genuinely new.
Do not blindly implement everything in this document.
The objective is to strengthen the existing application while preserving its architecture, consistency, reliability, and development progress.
1. MANDATORY AUDIT AND NON-DUPLICATION RULE
Before modifying any component, inspect the relevant existing implementation and canonical project documentation.
For each requirement below, determine whether it is:

* ALREADY IMPLEMENTED AND VERIFIED: Preserve it. Do not duplicate it.
* IMPLEMENTED BUT NOT ENFORCED: Strengthen enforcement within the existing component.
* PARTIALLY IMPLEMENTED: Complete the missing behavior without unnecessary restructuring.
* DOCUMENTED BUT NOT IMPLEMENTED: Integrate it into the appropriate existing component when necessary.
* GENUINELY NEW: Add it cleanly to the appropriate architecture.
* CONFLICTING: Identify and resolve conflicts using established project authority and decision rules.
* UNNECESSARY OR DUPLICATED: Do not introduce it again.

Do not create new engines, agents, services, controllers, or databases simply because this instruction uses different terminology.
Prefer updating existing components and canonical rules.
Do not confuse the absence of a particular feature name with the absence of its functionality.
Existing functionality must be assessed by its actual behavior.
2. PRIMARY TRADING PHILOSOPHY
The company's permanent trading philosophy shall be:
AGGRESSIVE OPPORTUNITY DISCOVERY.
INTELLIGENT OPPORTUNITY EVALUATION.
EFFICIENT CAPITAL ALLOCATION.
SELECTIVE EXECUTION.
STRICT CAPITAL PROTECTION.
NO FORCED TRADING.
The application must continuously seek legitimate profitable opportunities throughout its authorized trading universe.
However, aggressive opportunity discovery must never translate into reckless execution.
The system must distinguish between:

1. How aggressively it searches for opportunities.
2. How carefully it evaluates those opportunities.
3. How much capital it allocates.
4. Whether execution is justified.
5. Whether the opportunity complies with all existing risk policies.

Discovery should be broad and proactive.
Execution must remain selective and risk-controlled.
3. DAILY PROFITABILITY OBJECTIVE
The company's aspirational daily profitability objective is approximately:
1.2% NET RETURN OR HIGHER WHEN GENUINE MARKET OPPORTUNITIES SUPPORT IT.
This is a performance objective, not a guaranteed return or mandatory daily trading requirement.
The system must not interpret this target as an instruction to manufacture profits.
The following behavior is required:
Scenario A — Strong Opportunities
If valid opportunities can collectively produce returns exceeding 1.2%, the system may pursue those opportunities subject to all existing risk and execution requirements.
Do not artificially stop at 1.2% when additional profitable, independently justified opportunities remain available.
Scenario B — Moderate Opportunities
If the available opportunities support returns below 1.2%, the system must continue evaluating and capturing eligible profitable opportunities.
It must not reject worthwhile trades merely because the expected daily result is below the preferred target.
Scenario C — Small Opportunities
If the available opportunities have relatively small net returns, the system may execute them when they independently satisfy all profitability, risk, and capital-allocation requirements.
Scenario D — No Suitable Opportunities
If no available opportunity meets the system's requirements, it must select:
NO TRADE / WAIT.
Mandatory restrictions
Never:

* Force trades to achieve 1.2%.
* Increase leverage merely to pursue a daily target.
* Weaken risk limits to generate additional returns.
* Manufacture trading signals.
* Assume future profits are guaranteed.
* Execute trades with insufficient expected net profitability.
* Increase position sizes merely to recover losses.
* Override deterministic risk authorization.

The platform must accept that profitable days, losing days, and zero-return days are all possible.
4. UNIVERSAL OPPORTUNITY DISCOVERY RULE
The platform must not restrict opportunity discovery to a particular minimum return percentage.
It must continuously search the supported trading universe for potentially profitable opportunities.
This includes opportunities with estimated net returns such as:

* 0.1%
* 0.2%
* 0.3%
* 0.4%
* 0.5%
* 0.6%
* 0.7%
* 0.8%
* 0.9%
* 1.0%
* 1.2%
* 1.5%
* 2.0%
* 3.0%
* Higher legitimate opportunities.

These are examples, not a mandatory list of trading targets.
There must be no arbitrary universal percentage threshold that prevents economically worthwhile smaller opportunities from being evaluated.
However, a positive percentage alone does not authorize execution.
Every opportunity must satisfy the existing dynamic profitability threshold and risk controls.
The system should discover opportunities aggressively across its supported markets and strategies without duplicating the existing discovery engine.
5. MULTIPLE SMALL-GAIN PROFIT ACCUMULATION
The application must recognize that multiple smaller profitable opportunities may collectively generate meaningful daily returns.
For example, the system might identify valid opportunities offering:
Trade A: +0.10%
Trade B: +0.20%
Trade C: +0.30%
Trade D: +0.20%
Trade E: +0.40%
The application must be capable of evaluating and executing such opportunities when individually approved.
However, it must never assume these percentages can simply be added to calculate account-level returns.
The actual contribution depends on:

* Capital deployed.
* Trading costs.
* Whether trades occur sequentially or simultaneously.
* Actual realized returns.
* Capital availability.
* Compounding.
* Losses.
* Portfolio-level exposure.

Account-level daily performance must be calculated accurately.
Important enforcement
Do not require a fixed number of trades per day.
Do not impose a rule requiring three, five, or ten profitable trades.
The system should capture as many independently justified opportunities as market conditions and risk capacity permit.
Three profitable opportunities may be sufficient on one day.
More may be available on another.
No suitable opportunities may exist on some days.
Trade frequency must be opportunity-driven, not quota-driven.
6. AGGRESSIVE AND CONTINUOUS MARKET DISCOVERY
Enforce the existing universal opportunity-scanning architecture.
The system should continuously evaluate opportunities across authorized:

* Exchanges.
* Trading pairs.
* Markets.
* Strategy families.
* Arbitrage routes.
* Relevant time horizons.

Where supported, use multiple connected exchanges, with at least three as the initial intended multi-exchange coverage objective.
Do not create duplicate exchange integrations if the required connections or adapters already exist.
Improve discovery intelligently by prioritizing:

* Markets with meaningful liquidity.
* Markets exhibiting genuine price discrepancies.
* Opportunities with favorable expected net profitability.
* Reliable exchanges.
* Opportunities with sufficient executable order-book depth.
* Strategies demonstrating validated performance.

The system must be capable of considering multiple opportunities at the same time.
It should not unnecessarily wait for a large opportunity when a smaller independently profitable opportunity is available.
However, the system must not waste API calls, computing resources, or trading capital on meaningless activity.
Aggressive discovery must remain cost-aware and rate-limit compliant.
7. DYNAMIC PROFITABILITY AND EXECUTION RULE
Before executing any opportunity, the application must evaluate its realistic expected net profitability.
The evaluation must account for applicable:

* Exchange fees.
* Entry and exit costs.
* Bid/ask spreads.
* Slippage.
* Liquidity.
* Market impact.
* Funding or borrowing costs.
* Rebalancing costs.
* Execution uncertainty.
* Partial-fill exposure.
* Potential hedging costs.

Avoid double-counting costs already incorporated into executable prices.
Small opportunities must receive the same execution-quality checks as larger opportunities.
A 0.1% opportunity may qualify when its expected net economic value remains positive after appropriate uncertainty and risk buffers.
A 1.5% opportunity must still be rejected if its risks or execution costs make it unacceptable.
Higher quoted profits do not automatically mean better opportunities.
Use the existing dynamic profitability and risk-assessment components wherever available.
Do not introduce competing profitability engines.
8. INTELLIGENT CAPITAL ALLOCATION RULE
The existing capital-management system must allocate capital according to verified opportunity quality and portfolio constraints.
It must not automatically allocate capital solely to the opportunity with the highest quoted percentage return.
Consider:

* Expected net dollar profit.
* Capital efficiency.
* Execution probability.
* Capital requirements.
* Opportunity duration.
* Liquidity.
* Risk-adjusted expected return.
* Correlation between positions.
* Available reserves.
* Exchange reliability.
* Opportunity cost.

Where multiple opportunities qualify simultaneously, the system should determine the best feasible allocation within existing capital and risk limits.
Do not double-commit capital.
Do not spend emergency reserves without authorization under established policy.
Do not introduce duplicate capital-management logic.
The allocator must remain subordinate to the existing deterministic risk authority.
9. ADAPTIVE OPPORTUNITY PRIORITIZATION
Preserve the ability to pursue both smaller and larger profitable opportunities.
The system must intelligently rank opportunities according to expected net economic value, capital efficiency, execution feasibility, and risk.
Existing preferred return tiers may remain useful for classification and analysis.
However, return tiers must not become rigid execution barriers.
For example:
A 0.2% opportunity must not automatically be rejected because a 1.5% opportunity might appear later.
Likewise, a 1.5% opportunity must not automatically receive priority when a smaller opportunity offers substantially better risk-adjusted capital efficiency.
The platform should adapt to real market conditions rather than relying on rigid percentage-based decisions.
10. MULTI-STRATEGY COORDINATION
Preserve all previously approved strategy families and their existing validation requirements.
The trading application should coordinate eligible opportunities generated by different approved strategies.
Where supported, these may include:

* Cross-exchange arbitrage.
* Triangular arbitrage.
* Statistical arbitrage.
* Funding and basis strategies.
* Other validated trading strategies.

Do not activate unverified strategies merely to increase opportunity frequency.
Do not duplicate strategies that already exist.
All strategies must operate under shared portfolio-level capital and risk authority.
No individual strategy may bypass global safety controls.
11. AI AUTHORITY AND DETERMINISTIC CONTROL
Preserve the previously established deterministic-first architecture.
AI intelligence may assist with:

* Market interpretation.
* Strategy research.
* Opportunity analysis.
* Performance evaluation.
* Investigation of unusual conditions.
* Recommendations for strategy improvement.

However:
AI IS NOT THE FINAL AUTHORITY FOR TRADE EXECUTION.
Deterministic systems must retain authority over:

* Trading calculations.
* Capital allocation limits.
* Risk authorization.
* Order execution controls.
* Position accounting.
* Exposure management.
* Reconciliation.
* Emergency protection.

Existing AI specialists, model-routing systems, and AI cost-management policies must remain consistent with this rule.
Do not create unnecessary additional agents.
12. MARKET ADAPTATION AND NO-FORCED-TRADE ENFORCEMENT
The platform must continuously adjust its opportunity evaluation to actual market conditions.
Its objective is to capture the best feasible risk-adjusted opportunities, not to force a predetermined financial result.
If market opportunities support 1.5% or higher, the application may pursue them.
If available opportunities support only smaller returns, those opportunities must still receive proper consideration.
If expected net profitability is inadequate, the system must wait.
Daily profit objectives must not affect the authority of the risk engine.
The application must never compensate for a missed target through revenge trading, arbitrary leverage increases, unjustified capital concentration, or weakened validation.
A profitable opportunity must be worth executing independently of the daily profit objective.
13. CONTINUOUS PERFORMANCE INTELLIGENCE
Use the existing performance-monitoring, opportunity-history, and trading-memory infrastructure.
Ensure the application can measure:

* Opportunities discovered.
* Opportunities rejected.
* Reasons for rejection.
* Successfully executed opportunities.
* Failed and partial executions.
* Gross trading profit.
* Net realized profit.
* Trading losses.
* Account-level daily returns.
* Capital utilization.
* Execution quality.
* Strategy performance.
* Exchange performance.
* Maximum drawdown.
* Risk-adjusted profitability.

Track how frequently the system achieves daily net returns of at least:
1.0%, 1.1%, 1.2%, 1.3%, 1.4%, and 1.5%.
These statistics must come from actual verified performance data, clearly separating backtests, simulated trading, paper trading, and live execution.
Do not invent performance results.
Use actual results to evaluate whether strategy improvements produce measurable benefits.
Do not automatically promote new strategies based on short periods of favorable results.
14. PERMANENT CAPITAL-PROTECTION AUTHORITY
All trading rules must remain subordinate to the established deterministic risk engine.
Enforce existing controls for:

* Portfolio exposure.
* Position sizing.
* Capital limits.
* Maximum drawdown.
* Loss streaks.
* Exchange reliability.
* Liquidity requirements.
* Emergency protection.
* Recovery and reconciliation.
* Strategy activation.
* Deployment readiness.

Never weaken these controls to satisfy opportunity-discovery or profitability objectives.
NO TRADE is always an acceptable decision.
A trading opportunity is not approved merely because it is profitable on paper.
15. CLEAN INTEGRATION INTO THE EXISTING APPLICATION
This directive must be integrated professionally into the existing project.
Follow these rules:
RULE A — REUSE BEFORE ADDING
If existing functionality already satisfies a requirement, keep it unchanged unless evidence establishes a defect.
RULE B — STRENGTHEN BEFORE REPLACING
If functionality exists but is incomplete, improve it within the established architecture.
RULE C — NO PARALLEL SYSTEMS
Do not create duplicate scanners, execution engines, allocators, policy engines, or risk controllers.
RULE D — SINGLE SOURCE OF TRUTH
Trading policies must remain in their appropriate canonical locations.
Avoid multiple conflicting copies of the same rule.
RULE E — REQUIREMENT TRACEABILITY
Map every requirement to its corresponding existing policy, component, and verification evidence.
Reuse existing requirement identifiers where available.
RULE F — ROOT-CAUSE CORRECTION
When a rule is not functioning as intended, investigate and correct its root cause rather than introducing repeated workarounds.
RULE G — PRESERVE DEVELOPMENT STATE
Continue from the latest verified checkpoint.
Do not reset completed stages or unnecessarily modify unrelated functionality.
RULE H — MINIMAL NECESSARY CHANGES
Implement only the changes required to make the application comply with the approved rules.
Do not introduce unnecessary architecture or complexity.
16. THREE VERIFICATION GATES
Apply the existing three-gate verification process to relevant rule changes.
GATE 1 — POLICY AND ARCHITECTURE CONSISTENCY
Confirm:

* Rules are correctly incorporated.
* Existing approved requirements remain intact.
* No duplicate or conflicting functionality exists.
* Components have clear responsibilities.
* The architecture remains consistent.

GATE 2 — BEHAVIORAL ENFORCEMENT
Confirm:

* Small profitable opportunities are not rejected solely because they are below the daily target.
* Unprofitable or excessively risky opportunities are rejected.
* Trading remains independent of daily profit quotas.
* Capital allocation calculations are correct.
* Risk authorization cannot be bypassed.
* Multiple opportunities are coordinated safely.
* Relevant regression tests pass.

GATE 3 — OPERATIONAL RELIABILITY
Confirm:

* Existing trading workflows remain functional.
* Runtime enforcement works in the available test environment.
* Monitoring and audit records are accurate.
* No new execution or capital-management conflicts exist.
* Recovery and failure protections remain intact.
* Production readiness is not claimed without the necessary evidence.

A failed or unverified gate must not be reported as passed.
17. PERMANENT RULE ENFORCEMENT
These requirements are intended to govern the application throughout its development and future operation.
They must not remain merely as temporary instructions in a conversation.
Integrate them into the existing canonical policy and engineering documentation.
Where rules require executable safeguards, ensure the relevant existing components enforce them.
Add appropriate automated verification where needed.
Future changes must be checked against these approved trading rules.
Do not allow later feature development to silently override or contradict them.
Do not create multiple independent policy documents when an established canonical policy already exists.
Keep the enforcement system consistent, maintainable, and auditable.
18. EXECUTION AND REPORTING DIRECTIVE
Proceed in the following order:

1. Inspect the current repository and established trading policies.
2. Map these requirements to existing functionality.
3. Identify rules that are already correctly enforced.
4. Identify rules requiring stronger enforcement.
5. Identify genuinely new requirements.
6. Identify and resolve duplicate or conflicting requirements.
7. Integrate only necessary changes into existing components.
8. Apply the three verification gates.
9. Update the existing canonical documentation and traceability records.
10. Preserve the verified continuation checkpoint.

Provide a concise report showing:

* Already satisfied.
* Strengthened.
* Newly added.
* Duplicates avoided.
* Conflicts resolved.
* Tests completed.
* Verification results.
* Remaining issues.
* Exact development checkpoint.

Report facts supported by actual repository and test evidence.
Do not claim successful integration or verification without proof.
FINAL PERMANENT DIRECTIVE
The application must operate according to the following principles:
1. Search aggressively for legitimate profitable opportunities.
2. Accept both smaller and larger opportunities when independently justified.
3. Seek approximately 1.2% net daily or higher when market conditions genuinely permit.
4. Accept smaller achievable returns when the preferred target is unsupported.
5. Never force trades to satisfy daily targets.
6. Optimize capital allocation across qualified opportunities.
7. Preserve deterministic risk authority and capital protection.
8. Maintain accurate account-level profit calculations and performance evidence.
9. Preserve the existing company-grade application architecture.
10. Enforce existing rules, strengthen incomplete rules, and cleanly integrate only genuinely new requirements.
These rules must remain consistent throughout the platform's future development.
DO NOT REBUILD WHAT ALREADY EXISTS.
DO NOT DUPLICATE FUNCTIONALITY.
DO NOT INTRODUCE CONFLICTING RULES.
DO NOT WEAKEN THE EXISTING SYSTEM.
DO NOT FORCE PROFITABILITY.
INSPECT FIRST. ENFORCE EXISTING RULES. ADD ONLY WHAT IS MISSING. VERIFY EVERYTHING. PRESERVE CONTINUITY.
```
