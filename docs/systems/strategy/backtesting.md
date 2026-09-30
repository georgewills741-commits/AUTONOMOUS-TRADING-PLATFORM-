# Backtesting

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-15 · **Category:** shared infrastructure · **Roadmap stage:** DIRECTIONAL TRADING, although arbitrage needs it too (CF-05) · **Sources:** §33

Canonical definition of what backtesting must support and protect against. It is a stage of the [strategy lifecycle](strategy-management.md) (STR-001).

## Requirements

- **BKT-001** Backtesting scope · SYSTEM REQUIREMENT · §33 — Backtesting must support: historical data; strategy execution; fees; slippage; liquidity; position management; risk; capital constraints; portfolio interaction; opportunity competition where applicable.
- **BKT-002** Bias and leakage protections · CONFIRMED REQUIREMENT · §33 — Protect against: look-ahead bias; data leakage; survivorship bias; training/test contamination; unrealistic execution assumptions.
- **BKT-003** A backtest is not authorization · CONSTRAINT · §33 — Backtesting alone does not authorize production.

## Boundary (§92)

- **Consumes:** historical [market data](../market-data.md) (MKD-004 applies the same bias protections at the data layer).
- **Used by:** [Strategy Management](strategy-management.md).
- **Not yet specified in Part 1:** historical data sources and depth (OQ-22), execution simulation model, interfaces, tests.
