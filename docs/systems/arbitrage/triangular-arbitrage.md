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

## Findings (all resolved)

DUP-01 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (ARB-012, TNP-017). DUP-09 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RSK-012). DUP-03 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PFC-006). CF-04 → [DEC-013](../../decisions/DEC-013-ai-organization.md): arbitrage is deterministic end to end, and AI never proposes arbitrage trades (ARB-013).
