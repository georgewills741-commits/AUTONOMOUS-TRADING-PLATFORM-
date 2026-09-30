# Triangular Arbitrage System

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-19 · **Category:** trading system · **Roadmap stage:** ARBITRAGE ("Triangular") · **Sources:** §07 (also §03 C)

Canonical definition of trading executable multi-leg routes within a venue/market graph (example: Asset A → Asset B → Asset C → Asset A). Capabilities shared by both arbitrage systems are in [Arbitrage Intelligence](arbitrage-intelligence.md).

## Requirements

- **TAR-001** Purpose · CONFIRMED REQUIREMENT · §07 — The Triangular Arbitrage System identifies executable multi-leg routes.
- **TAR-002** Responsibilities · SYSTEM REQUIREMENT · §07 — Trading-pair graph construction; route discovery; route validation; profitability calculation; fees; slippage; liquidity; execution sequence; partial-fill handling; route invalidation; multi-leg risk; execution feasibility; expected-vs-actual analysis.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md).

- **TAR-003** Dynamic route discovery and calculation · SYSTEM REQUIREMENT · P2§88, P2§217 — The platform should dynamically discover routes such as asset A → asset B → asset C → asset A. It must calculate: prices; fees; precision; liquidity; slippage; capital requirement; execution sequence; true net result.
- **TAR-004** Triangular execution risk · SYSTEM REQUIREMENT · P2§89, P2§218 — The system must account for: leg failure; partial fills; price movement; liquidity deterioration; exchange rejection; precision constraints; rate limits; timing; residual assets. A mathematically profitable route may still be operationally invalid.

## Boundary (§92)

- **Owns:** the trading-pair graph, route discovery and validation, and the leg execution sequence (ARCH-004).
- **Must use:** shared infrastructure for economics, capital, risk, execution, and portfolio (ARCH-003).
- **Not yet specified in Part 1:** handling of a partially completed route, route latency limits, interfaces, tests.

## Findings (all resolved)

DUP-01 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (ARB-012, TNP-017). DUP-09 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RSK-012). DUP-03 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PFC-006). CF-04 → [DEC-013](../../decisions/DEC-013-ai-organization.md): arbitrage is deterministic end to end, and AI never proposes arbitrage trades (ARB-013).
