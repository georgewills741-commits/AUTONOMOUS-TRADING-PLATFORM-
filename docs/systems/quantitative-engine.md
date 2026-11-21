# Quantitative Engine

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — implemented for Stage 2's part, in `atp.quant` ("Stage 2's calculations", below; the [roadmap](../roadmap/roadmap.md)'s feature-status table) · **System:** SYS-03 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §12

Canonical definition of the platform's deterministic calculations.

## Requirements

- **QNT-001** Calculations without an LLM · CONFIRMED ARCHITECTURAL PRINCIPLE · §12 — The Quantitative Engine performs calculations without requiring an LLM.
- **QNT-002** Calculation scope · SYSTEM REQUIREMENT · §12 — Examples: RSI; MACD; ATR; moving averages; volatility; spread; returns; drawdown; exposure; position sizing; risk/reward; correlation; liquidity metrics; slippage; fees; arbitrage economics.
- **QNT-003** Deterministic-first rule · CONSTRAINT · §12 — If a calculation can be performed deterministically, the system should not ask an LLM to perform it.

Precision rules for all financial calculations are defined in the [architecture overview](../architecture/overview.md) (ARCH-010, ARCH-011).

## Decisions applied (2026-09-30)

- **QNT-004** Primitive metrics only · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine computes primitive metrics: fees, spread, slippage estimates, indicators, and sizing calculations. Combining costs into the true net expected result belongs only to the True Net-Profit Engine (TNP-017).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **QNT-005** Fee Engine · SYSTEM REQUIREMENT · P2§30 — Fees must be calculated deterministically. The Fee Engine should account for applicable: venue; instrument; maker/taker status; fee schedule; trading tier; funding; transfer costs where relevant. AI may interpret fee implications but cannot become the authoritative fee calculator.
- **QNT-006** Slippage Engine · SYSTEM REQUIREMENT · P2§31 — The Slippage Engine should model expected execution effects. Where data permits, it considers: order-book depth; order size; liquidity; volatility; spread; execution type; market impact; historical execution behavior.
- **QNT-007** Fee and Slippage Engines live here · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — The Fee Engine and the Slippage Engine are components of this engine, which already computes fees and slippage estimates as primitive metrics (QNT-004). There is one of each (ARCH-027). The True Net-Profit Engine combines their outputs (TNP-017), and fee metadata comes from the exchange adapters (EXA-012).

## Boundary (§92)

- **Owns:** deterministic calculation of the metrics in QNT-002.
- **Consumes:** validated, normalized [market data](market-data.md).
- **Must not be replaced by:** the Market Analyst (AGT-009) or the Quant Research Agent (AGT-011).
- **Not yet specified in Part 1:** calculation definitions, interfaces, tests. Specified since DATA FOUNDATION was planned ([Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md)): Stage 2's calculations, their interfaces, and their tests ("Stage 2's calculations", below; Stage 2's U7, in `atp.quant`; [Stage 2 record](../traceability/stage-02-data-foundation.md)); drawdown, exposure, sizing, and risk/reward come with CORE TRADING FOUNDATION, and arbitrage economics with the True Net-Profit Engine (the plan's section 3.2).

## Stage 2's calculations (U7)

Built at Stage 2's checkpoint C, before checkpoint B's venue adapters ([DEC-080](../decisions/DEC-080-checkpoint-c-before-the-venue-adapters.md)), in `atp.quant`. Each function's docstring states its definition in full, and the tests check each against values worked by hand from it (`tests/quant/`).

- **Inputs.** Market data reaches a calculation only as SYS-02's `Validated` (Consumes, above), and only if it was VALID when validated and is VALID again at the time of use, which the caller gives with the freshness limits (MKD-012; an item the [Stage 2 record](../traceability/stage-02-data-foundation.md) carried to this unit). A calculation without a result for its data (data not VALID, a missing price, side of a book, or fee schedule, too few bars, a gap between bars, or a definition that gives no value) is refused with its cause, so its consumer reads it as unknown, never as zero (master execution constitution §168).
- **Spread and liquidity** (QNT-002), exact: a ticker's or a book snapshot's mid, spread, and spread relative to the mid, rounded up; and the quantity and value of a book's levels within a band of the mid, each side marked complete when the snapshot shows a level beyond the band.
- **The Fee Engine** (QNT-005, QNT-007): a fee is the notional times the maker or taker rate of the venue's published schedule for the market's instrument type, at its base tier, as the venue's configuration holds it with its source and date (the plan's D8), exactly, and its result holds that schedule; a venue with no schedule for the type gives no fee, never zero. Funding is a perpetual position's notional times a published funding rate, paid by a long and received by a short when the rate is above zero. The account's own tier and rates come with CORE TRADING FOUNDATION, and transfer costs with ARBITRAGE (the plan's section 3.2).
- **The Slippage Engine** (QNT-006, QNT-007): a taker order of a size walked through one side of a book snapshot, best level first, up to a limit price where one is given (its execution type: a market order, or a limit order that takes liquidity). It gives the quantity filled, the levels reached, the best and worst prices, the value filled, the average price rounded against the taker, and, exactly, the slippage beyond the best price and the impact beyond the mid, the half spread included: depth, size, liquidity, spread, execution type, and market impact. Volatility is not folded into it in Stage 2: the estimate is exact, volatility is a float indicator, which may not reach an amount (the plan's D5), and a model joining them needs fitting to execution history, which comes with DIRECTIONAL TRADING and CORE TRADING FOUNDATION (QNT-006's "where data permits"; the plan's section 3.2). Both are given, each with its evidence identifier, to the consumer that combines costs (TNP-017).
- **Indicators** (QNT-002), in floats (TEC-003; the plan's D5), over a market's closed bars of one interval: the simple and exponential moving averages (the exponential started from the simple one), Wilder's RSI and average true range, Appel's MACD (its line, signal, and histogram), simple and logarithmic returns over a period, volatility as the sample standard deviation of one-bar logarithmic returns (per bar, not scaled to a year), and Pearson's correlation of two markets' one-bar logarithmic returns. Only `atp.quant._indicators` uses floats, and it imports nothing from `atp.numeric`, so no float becomes an amount (the structure test; [numerical policy](../architecture/numerical-policy.md), N4). Incremental indicators come where measurement shows a gain (PERF-005), with U10.
- **Results** (MKD-005, MKD-010): each is a contract that carries the time it describes, its inputs' evidence identifiers, its calculation's version, and its own evidence identifier, a SHA-256 digest of the form `atp.calculation/1`, the calculation's name and version, its parameters, and its inputs, so the same calculation of the same inputs gets the same identifier on any platform. No LLM or AI is asked (QNT-001, QNT-003), and no cost is combined into a net result (QNT-004).

## Findings (all resolved)

DUP-01 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (QNT-004). DUP-19 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (the strategy proposes a size from these calculations; the Risk Engine sets the final size, RSK-011).
