# Backtesting

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-15 · **Category:** shared infrastructure · **Roadmap stage:** DIRECTIONAL TRADING, although arbitrage needs it too (CF-05) · **Sources:** §33

Canonical definition of what backtesting must support and protect against. It is a stage of the [strategy lifecycle](strategy-management.md) (STR-001).

## Requirements

- **BKT-001** Backtesting scope · SYSTEM REQUIREMENT · §33 — Backtesting must support: historical data; strategy execution; fees; slippage; liquidity; position management; risk; capital constraints; portfolio interaction; opportunity competition where applicable.
- **BKT-002** Bias and leakage protections · CONFIRMED REQUIREMENT · §33 — Protect against: look-ahead bias; data leakage; survivorship bias; training/test contamination; unrealistic execution assumptions.
- **BKT-003** A backtest is not authorization · CONSTRAINT · §33 — Backtesting alone does not authorize production.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../../decisions/DEC-024-part-2-reconciliation.md).

- **BKT-004** Additional integrity protections · CONFIRMED REQUIREMENT · P2§52 — In addition to BKT-002, backtests must prevent: future information leakage; incorrect fee assumptions; unrealistic liquidity; unrealistic slippage.
- **BKT-005** Protected dataset separation · CONSTRAINT · P2§53 — Where applicable, datasets are separated: training → validation → out-of-sample → paper → production. Data boundaries must prevent leakage.
- **BKT-006** Anti-overfitting validation · CONFIRMED REQUIREMENT · P2§54 — Strategy validation should consider: out-of-sample performance; walk-forward testing; parameter sensitivity; stress testing; market-regime diversity; Monte Carlo / distribution analysis; robustness testing. A strategy must not be approved merely because one historical backtest looks profitable.
- **BKT-007** Walk-forward testing · SYSTEM REQUIREMENT · P2§55 — Where applicable: train → test → roll forward → retrain / revalidate → test. The exact methodology must be documented.
- **BKT-008** Stress testing · SYSTEM REQUIREMENT · P2§56 — Strategies should be exposed to adverse conditions including, where relevant: volatility spikes; spread widening; liquidity deterioration; execution delays; exchange outages; slippage increases; partial fills; data interruptions.
- **BKT-009** Monte Carlo / distribution analysis · SYSTEM REQUIREMENT · P2§57 — Where appropriate, performance analysis should examine distributions rather than relying solely on average return. Potential outputs: drawdown distribution; losing streaks; return distribution; tail behavior; execution variance; risk-of-ruin-related measures. The exact methodology requires architectural specification.

The walk-forward (BKT-007) and Monte Carlo (BKT-009) methodologies are to be specified when DIRECTIONAL TRADING is planned; they are listed as specification gaps in the [Part 2 documentation audit](../../traceability/part-2-verification.md). Experiment reproducibility (P2§119) is STR-026.

## Boundary (§92)

- **Consumes:** historical [market data](../market-data.md) (MKD-004 applies the same bias protections at the data layer).
- **Used by:** [Strategy Management](strategy-management.md).
- **Not yet specified:** execution simulation model, interfaces, tests. Historical data comes from the platform's own permanent archives (TEC-012, [DEC-009](../../decisions/DEC-009-technology-stack.md)).
