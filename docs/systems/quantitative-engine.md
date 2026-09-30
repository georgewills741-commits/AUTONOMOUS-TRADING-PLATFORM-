# Quantitative Engine

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-03 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §12

Canonical definition of the platform's deterministic calculations.

## Requirements

- **QNT-001** Calculations without an LLM · CONFIRMED ARCHITECTURAL PRINCIPLE · §12 — The Quantitative Engine performs calculations without requiring an LLM.
- **QNT-002** Calculation scope · SYSTEM REQUIREMENT · §12 — Examples: RSI; MACD; ATR; moving averages; volatility; spread; returns; drawdown; exposure; position sizing; risk/reward; correlation; liquidity metrics; slippage; fees; arbitrage economics.
- **QNT-003** Deterministic-first rule · CONSTRAINT · §12 — If a calculation can be performed deterministically, the system should not ask an LLM to perform it.

Precision rules for all financial calculations are defined in the [architecture overview](../architecture/overview.md) (ARCH-010, ARCH-011).

## Decisions applied (2026-09-30)

- **QNT-004** Primitive metrics only · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine computes primitive metrics: fees, spread, slippage estimates, indicators, and sizing calculations. Combining costs into the true net expected result belongs only to the True Net-Profit Engine (TNP-017).

## Boundary (§92)

- **Owns:** deterministic calculation of the metrics in QNT-002.
- **Consumes:** validated, normalized [market data](market-data.md).
- **Must not be replaced by:** the Market Analyst (AGT-009) or the Quant Research Agent (AGT-011).
- **Not yet specified in Part 1:** calculation definitions, interfaces, tests.

## Findings (all resolved)

DUP-01 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (QNT-004). DUP-19 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (the strategy proposes a size from these calculations; the Risk Engine sets the final size, RSK-011).
