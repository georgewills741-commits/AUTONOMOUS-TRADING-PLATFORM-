# Quantitative Engine

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-03 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §12

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
- **Not yet specified in Part 1:** calculation definitions, interfaces, tests.

## Findings (all resolved)

DUP-01 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (QNT-004). DUP-19 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (the strategy proposes a size from these calculations; the Risk Engine sets the final size, RSK-011).
