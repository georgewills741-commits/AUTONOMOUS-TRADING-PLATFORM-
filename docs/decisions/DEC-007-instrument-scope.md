# DEC-007 — Instrument scope: spot, perpetual futures, and margin

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ("all, because the control risks are there")
- **Resolves:** OQ-04
- **Affects:** [platform overview](../product/platform-overview.md), [exchange adapters](../systems/exchange-adapters.md), [risk engine](../risk/risk-engine.md), [Global Capital Authority](../systems/capital-management.md), [portfolio](../systems/portfolio-management.md)

## Context

Part 1 mentions funding rates, funding costs, leverage limits, and positions, but never states the instrument scope. The builder recommended spot only. The owner chose all three instrument types, relying on the risk controls.

## Decision

1. The platform trades **spot, perpetual futures, and margin** products (PLT-011).
2. Because leverage and liquidation add risk to every core system, **no instrument type is enabled for live trading until its specific risk controls are implemented and verified** (PLT-012). This follows from the safety priority (PLT-006): capital preservation and risk control rank above opportunity. It does not narrow the owner's scope; it orders how each type is switched on.
3. Required controls for derivatives and margin (RSK-013): maximum leverage; minimum distance to liquidation; margin-ratio limits with automatic de-risking before liquidation; funding and borrow cost limits; limits on total derivatives notional.
4. The capital state tracks collateral, borrowed funds, and required margin (CAP-020). The portfolio tracks leverage, notional, margin, liquidation prices, and funding and borrow accruals (PRT-005). Adapters expose each venue's supported instrument types and settings (EXA-009).

## Consequences

The CORE TRADING FOUNDATION risk model must be designed for leveraged positions from the start. Each venue supports a different subset of instrument types, so availability is per venue.
