# True Net-Profit Engine (Opportunity Economics)

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — not implemented · **System:** SYS-06 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Opportunity economics"); ARBITRAGE adds transfer and multi-leg cost components ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §13–§17; Part 3: P3§394, P3§424, P3§440

Canonical definition of how every opportunity's economics are evaluated. It also holds the platform's rules on small positive opportunities, accumulation, and the absence of profit floors and ceilings. The handoff calls §14 "a critical requirement".

## Realistic executable economics

- **TNP-001** Realistic executable economics · CONFIRMED REQUIREMENT · §13 — Every opportunity must be evaluated using realistic executable economics.
- **TNP-002** Conceptual cost stack · CONFIRMED ARCHITECTURAL PRINCIPLE · §13 — Conceptually: gross opportunity − trading fees − spread − expected slippage − market impact − funding costs − rebalancing/transfer costs − other execution costs − safety/uncertainty margin = true net expected result.
- **TNP-003** Formal formula required · CONFIRMED REQUIREMENT · §13 — The exact formula must be formally defined.
- **TNP-004** Displayed differences are not profit · CONSTRAINT · §13 — The platform must never treat displayed percentage differences as guaranteed profit.

## Positive-net-profit opportunity principle (critical)

- **TNP-005** No universal minimum profit threshold · CONSTRAINT · §14 — The system must not impose an artificial universal minimum profit threshold that prevents it from taking a genuinely executable positive-net opportunity.
- **TNP-006** Positive-net opportunities are eligible · CONFIRMED REQUIREMENT · §14 — If a fully validated opportunity produces a positive true net expected profit (example: +0.1%) and all applicable conditions are satisfied — fees included; slippage included; liquidity sufficient; execution feasible; risk acceptable; capital available; no higher-priority conflict; expected value justifies execution; safety margin satisfied — then the system may execute it. The same applies to +0.2%, +0.3%, +0.5%, +1%, +2%, +5%, or any other positive result that genuinely survives the complete evaluation.
- **TNP-007** Economics, not labels · CONFIRMED REQUIREMENT · §14 — The system must evaluate economics, not an arbitrary percentage label.

## Small-profit accumulation

- **TNP-008** Small opportunities may accumulate · CONFIRMED REQUIREMENT · §15 — Small profitable opportunities may be valuable when they can be executed repeatedly and safely. The system may accumulate these results over time when each individual opportunity is independently valid.
- **TNP-009** No large-trades-only assumption · CONSTRAINT · §15 — The architecture must not assume "Only large trades matter."
- **TNP-010** Cumulative effect counts · CONFIRMED REQUIREMENT · §15 — The objective is to maximize risk-adjusted executable net profitability, including the cumulative effect of many smaller opportunities.
- **TNP-011** Small profit is not an automatic trade · CONSTRAINT · §15 — Small profit does not automatically mean trade. The opportunity must still pass: net-profit validation; risk controls; liquidity requirements; execution feasibility; capital allocation; cost analysis; strategy validity; safety requirements.

How realized results feed back into available capital (compounding) is defined in [Global Capital Authority](capital-management.md) (CAP-010 to CAP-013).

## No artificial profit ceiling

- **TNP-012** No conceptual ceiling · CONSTRAINT · §16 — The platform must not impose a conceptual ceiling such as "The system is only allowed to make 1% per day."
- **TNP-013** Cumulative daily results are not capped · CONFIRMED REQUIREMENT · §16 — If the market provides multiple valid opportunities and the system can safely execute them, cumulative daily profitability could theoretically exceed previously discussed target percentages.
- **TNP-014** No guaranteed daily return · CONSTRAINT · §16 — The system must not interpret this as a guaranteed 5% daily return. There is: no guaranteed daily return; no fixed daily target; no fixed daily ceiling; no assumption that opportunities will always exist. The actual result depends on market conditions, execution, liquidity, fees, risk, and available opportunities.

## Opportunity quality

- **TNP-015** Multi-dimensional quality · CONFIRMED REQUIREMENT · §17 — Opportunity quality should be evaluated using multiple dimensions rather than percentage alone. Possible dimensions: true net profitability; confidence in market data; liquidity; slippage; market impact; execution latency; capital requirement; risk; strategy validity; exchange health; competition with other opportunities; expected repeatability; rebalancing requirements; safety margin.
- **TNP-016** Percentage thresholds only as configurable filters · CONSTRAINT · §17 — A percentage threshold may be used as a configurable research/filter parameter, but it must not become a universal hard rule that conflicts with the positive-net-opportunity principle.

## Decisions applied (2026-09-30)

- **TNP-017** Sole owner of the true net expected result · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Only this engine produces the true net expected result. The Quantitative Engine supplies primitive metrics; trading systems supply legs, routes, and sizes, and consume the result.
- **TNP-018** Formula · CONFIRMED REQUIREMENT · DEC-014 — True net expected result, in quote currency at the intended size = gross edge at executable prices (walking the order book at the intended size) − trading fees at the account's actual fee tier − spread cost − expected slippage − expected market impact − funding and borrow costs over the expected holding period − attributed rebalancing/transfer costs − other execution costs − uncertainty margin. All terms use exact decimal arithmetic.
- **TNP-019** Uncertainty margin from measured uncertainty · CONSTRAINT · DEC-014 — The uncertainty margin is computed per opportunity as k × √(cost-estimate error² + latency price risk²). Cost-estimate error comes from expected-vs-actual history for that venue, market, and strategy, or a conservative prior when history is thin. Latency price risk is price volatility over the expected execution latency × size. k is an operator-configurable confidence multiplier. The margin must never be a fixed percentage or a universal minimum.
- **TNP-020** Economic eligibility · CONFIRMED REQUIREMENT · DEC-014 — An opportunity is economically eligible when its true net expected result, after the uncertainty margin, is greater than zero. It must still pass TNP-011.
- **TNP-021** Comparable quality measure · SYSTEM REQUIREMENT · DEC-011 — For each opportunity this engine also produces the TNP-015 quality dimensions and a risk-adjusted expected net return per unit of capital per unit of time, so opportunities from different trading systems can be compared for allocation.
- **TNP-022** Continuous calibration · CONFIRMED REQUIREMENT · DEC-014 — Cost estimates and the cost-estimate error are recalibrated continuously from expected-vs-actual results (PFC-001).

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **TNP-023** Latency decay in executable economics · CONFIRMED REQUIREMENT · DEC-019 — Executable net economics must incorporate realistic execution latency: expected opportunity value is weighed against expected latency decay and execution risk. An opportunity that theoretically produces positive net profit but is likely to disappear before execution should be rejected. This is part of each opportunity's economics, not a minimum-profit threshold (TNP-005).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **TNP-024** Liquidity protection · CONSTRAINT · P2§32 — A theoretical opportunity may be rejected if actual liquidity cannot support execution. Liquidity evaluation should be deterministic wherever possible.

Already covered: true executable net economics rather than headline spread, gross percentage, AI prediction, or a fixed return (P2§29, §345) is TNP-001, TNP-002, TNP-004, TNP-018, and PLT-007. Funding costs (P2§33) are a term of TNP-018. No guaranteed returns (P2§34) is PLT-007, PLT-008, and TNP-014. Opportunity accumulation (P2§35) is TNP-008 and TNP-010, with PLT-019. The percentages previously discussed are analytical categories or filters (TNP-016, ARB-015), never guarantees.

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **TNP-025** Execution probability and time · SYSTEM REQUIREMENT · P3§394, P3§424 — Opportunity discovery may be aggressive; execution must still require true executable net economics. In addition to the terms of TNP-018 and the latency decay of TNP-023, the system must account for: precision; execution probability. Time is a financial input: the system should account for data age; network latency; exchange latency; order-book changes; opportunity decay; transfer latency; AI latency; queue delay. A theoretically profitable opportunity may become unprofitable because of time.
- **TNP-026** No artificial daily profit ceiling unless policy requires it · CONSTRAINT · P3§440 — The platform must not artificially stop profitable operation simply because a daily percentage target has been reached unless an explicit risk/capital policy requires it. The system should continue evaluating opportunities subject to: risk; capital; policy; market conditions; execution quality.

P3§429 to P3§432 (fees, slippage, liquidity, funding and carry are real) are TNP-001, TNP-002, TNP-004, TNP-018, TNP-024, QNT-005, and QNT-006. P3§439 (no fixed daily profit requirement) is PLT-008 and TNP-014. TNP-026 keeps TNP-012 in force: the architecture has no built-in ceiling; only the operator's explicit risk or capital policy can stop operation for the day.

## Boundary (§92)

- **Owns:** the true net expected result of an opportunity (TNP-002), and the eligibility rules TNP-005 to TNP-016.
- **Consumes:** cost inputs (fees, spread, slippage estimates) and market data. See the [dependency map](../architecture/dependency-map.md).
- **Does not decide alone:** risk acceptance (Risk Engine), capital availability (Global Capital Authority), execution feasibility at submission time (Execution Engine).
- **Not yet specified:** the numerical methods for slippage and market impact (order-book walk, impact model), interfaces, tests. The formula is TNP-018, the margin TNP-019, and allocation ranking CAP-017.

## Findings (all resolved)

OQ-05 → [DEC-014](../decisions/DEC-014-net-profit-formula-and-uncertainty-margin.md) (TNP-018). TC-01 → [DEC-014](../decisions/DEC-014-net-profit-formula-and-uncertainty-margin.md) (TNP-019: the margin scales with measured uncertainty and can never be a universal minimum). TC-04 → [DEC-014](../decisions/DEC-014-net-profit-formula-and-uncertainty-margin.md) (TNP-022, PAP-003). DUP-01 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (TNP-017). DUP-10 and TC-03 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (TNP-021, CAP-017).
