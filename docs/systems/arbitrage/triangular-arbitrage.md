# Triangular Arbitrage System

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-19 · **Category:** trading system · **Roadmap stage:** ARBITRAGE ("Triangular") · **Sources:** §07 (also §03 C)

Canonical definition of trading executable multi-leg routes within a venue/market graph (example: Asset A → Asset B → Asset C → Asset A). Capabilities shared by both arbitrage systems are in [Arbitrage Intelligence](arbitrage-intelligence.md).

## Requirements

- **TAR-001** Purpose · CONFIRMED REQUIREMENT · §07 — The Triangular Arbitrage System identifies executable multi-leg routes.
- **TAR-002** Responsibilities · SYSTEM REQUIREMENT · §07 — Trading-pair graph construction; route discovery; route validation; profitability calculation; fees; slippage; liquidity; execution sequence; partial-fill handling; route invalidation; multi-leg risk; execution feasibility; expected-vs-actual analysis.

## Boundary (§92)

- **Owns:** the trading-pair graph, route discovery and validation, and the leg execution sequence (ARCH-004).
- **Must use:** shared infrastructure for economics, capital, risk, execution, and portfolio (ARCH-003).
- **Not yet specified in Part 1:** handling of a partially completed route, route latency limits, interfaces, tests.

## Findings

- DUP-01: profitability, fees, and slippage calculation overlap with the True Net-Profit Engine and the Quantitative Engine.
- DUP-09: multi-leg risk overlaps with the shared Risk Engine.
- DUP-03: expected-vs-actual analysis overlaps with the Performance Controller.
- CF-04: the AI output contract's BUY / SELL / HOLD / NO_TRADE decision does not describe multi-leg routes.
