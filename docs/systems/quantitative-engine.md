# Quantitative Engine

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-03 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION · **Sources:** §12

Canonical definition of the platform's deterministic calculations.

## Requirements

- **QNT-001** Calculations without an LLM · CONFIRMED ARCHITECTURAL PRINCIPLE · §12 — The Quantitative Engine performs calculations without requiring an LLM.
- **QNT-002** Calculation scope · SYSTEM REQUIREMENT · §12 — Examples: RSI; MACD; ATR; moving averages; volatility; spread; returns; drawdown; exposure; position sizing; risk/reward; correlation; liquidity metrics; slippage; fees; arbitrage economics.
- **QNT-003** Deterministic-first rule · CONSTRAINT · §12 — If a calculation can be performed deterministically, the system should not ask an LLM to perform it.

Precision rules for all financial calculations are defined in the [architecture overview](../architecture/overview.md) (ARCH-010, ARCH-011).

## Boundary (§92)

- **Owns:** deterministic calculation of the metrics in QNT-002.
- **Consumes:** validated, normalized [market data](market-data.md).
- **Must not be replaced by:** the Market Analyst (AGT-009) or the Quant Research Agent (AGT-011).
- **Not yet specified in Part 1:** calculation definitions, interfaces, tests.

## Findings

- DUP-01: QNT-002 includes "fees", "slippage" and "arbitrage economics", which the True Net-Profit Engine and both arbitrage systems also list.
- DUP-19: "position sizing" is also listed by the Risk Engine (RSK-002) and the Directional Trading System (DIR-002).
