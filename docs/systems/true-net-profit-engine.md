# True Net-Profit Engine (Opportunity Economics)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-06 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Opportunity economics"); §95 also lists "True net-profit calculation" under ARBITRAGE (CF-05) · **Sources:** §13–§17

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

## Boundary (§92)

- **Owns:** the true net expected result of an opportunity (TNP-002), and the eligibility rules TNP-005 to TNP-016.
- **Consumes:** cost inputs (fees, spread, slippage estimates) and market data. See the [dependency map](../architecture/dependency-map.md).
- **Does not decide alone:** risk acceptance (Risk Engine), capital availability (Global Capital Authority), execution feasibility at submission time (Execution Engine).
- **Not yet specified in Part 1:** the formula (TNP-003), how the safety/uncertainty margin is derived, who ranks opportunities by quality, interfaces, tests.

## Findings

- OQ-05: the formal formula required by TNP-003 has not been provided.
- TC-01: the safety/uncertainty margin could quietly become the universal minimum threshold forbidden by TNP-005 unless its derivation is defined per opportunity.
- TC-04: at small margins such as +0.1%, estimation error in fees or slippage of similar size can flip the sign. This is why expected-vs-actual comparison (PFC-001) matters.
- DUP-01: net-profit calculation is also listed by the Quantitative Engine, both arbitrage systems, and Arbitrage Intelligence.
- DUP-10: which system ranks opportunities by the quality dimensions in TNP-015 is unresolved.
