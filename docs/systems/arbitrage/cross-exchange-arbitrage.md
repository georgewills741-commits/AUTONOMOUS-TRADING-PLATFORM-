# Cross-Exchange Arbitrage System

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-18 · **Category:** trading system · **Roadmap stage:** ARBITRAGE ("Cross-exchange") · **Sources:** §06 (also §03 B)
>
> Canonical location per §98 (`docs/systems/arbitrage/`).

Canonical definition of trading executable price discrepancies between venues. Capabilities shared by both arbitrage systems are in [Arbitrage Intelligence](arbitrage-intelligence.md).

## Requirements

- **XAR-001** Purpose · CONFIRMED REQUIREMENT · §06 — The Cross-Exchange Arbitrage System detects and evaluates executable price discrepancies between venues.
- **XAR-002** Real executable economics · CONSTRAINT · §06 — It must evaluate real executable economics, not merely displayed prices.
- **XAR-003** Responsibilities · SYSTEM REQUIREMENT · §06 — Exchange monitoring; price comparison; order-book evaluation; liquidity analysis; fee calculation; slippage estimation; market-impact analysis; latency analysis; capital availability; exchange health; position availability; true net-profit calculation; opportunity ranking; execution validation; opportunity tracking; expected-vs-actual analysis.
- **XAR-004** A price gap is not an opportunity · CONSTRAINT · §06 — A displayed price difference is not automatically an arbitrage opportunity.

## Boundary (§92)

- **Owns:** cross-exchange arbitrage behavior (ARCH-004).
- **Must use:** shared infrastructure for economics, capital, risk, execution, and portfolio (ARCH-003, ARB-002).
- **Not yet specified in Part 1:** how both legs are executed and hedged, handling of one-leg failure, interfaces, tests.

## Findings

Several XAR-003 responsibilities are also owned elsewhere:

| XAR-003 item | Also owned by | Finding |
|---|---|---|
| Fee calculation; slippage estimation; true net-profit calculation | Quantitative Engine; True Net-Profit Engine | DUP-01 |
| Opportunity ranking | Arbitrage Intelligence; Opportunity Detection | DUP-10 |
| Exchange monitoring; exchange health | Monitoring and Observability (exchanges); Exchange Adapter Layer | DUP-05 |
| Capital availability | Global Capital Authority | DUP-07 |
| Execution validation | Execution Engine | — (consumer of EXE-004) |
| Expected-vs-actual analysis | Performance Controller | DUP-03 |
