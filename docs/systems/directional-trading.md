# Directional Trading System

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-17 · **Category:** trading system · **Roadmap stage:** DIRECTIONAL TRADING · **Sources:** §05 (also §03 A)
>
> Canonical location per §98 (`docs/systems/directional-trading.md`).

Canonical definition of the directional trading system: trading on expected market movement.

## Requirements

- **DIR-001** Purpose · CONFIRMED REQUIREMENT · §05 — The Directional Trading System identifies and manages opportunities where expected market movement creates a valid trading opportunity.
- **DIR-002** Responsibilities · SYSTEM REQUIREMENT · §05 — Responsibilities may include: trend analysis; momentum; signal generation; entry conditions; exit conditions; confirmation; market-condition filtering; regime compatibility; strategy selection; position sizing; stop-loss; take-profit; risk/reward; trade filtering; strategy monitoring; backtesting; paper trading; performance analysis; strategy improvement.
- **DIR-003** Cannot bypass platform controls · CONSTRAINT · §05 — It cannot bypass: capital controls; risk controls; execution validation; user restrictions; portfolio limits; exchange constraints.

## Boundary (§92)

- **Owns:** directional trading behavior: signals, entry/exit logic, stop-loss and take-profit rules for directional strategies (ARCH-004).
- **Consumes:** opportunities from the [Opportunity Detection Engine](opportunity-detection.md); regime from the [Market Regime Engine](market-regime-engine.md); validated strategy versions from [Strategy Management](strategy/strategy-management.md).
- **Must pass through:** the [Global Capital Authority](capital-management.md), [Risk Engine](../risk/risk-engine.md), and [Execution Engine](execution-engine.md) (DIR-003).
- **Not yet specified in Part 1:** initial strategies, timeframes and instruments (OQ-21, OQ-04), interfaces, tests.

## Findings

- DUP-20: several DIR-002 items (backtesting, paper trading, performance analysis, strategy improvement, strategy monitoring, strategy selection) are also shared-infrastructure capabilities (ARCH-003 includes "strategy lifecycle"). The PROPOSED reading is that this system provides the directional-specific parts and uses the shared systems for the rest.
- DUP-19: position sizing is also listed by the Quantitative Engine and the Risk Engine.
- DUP-08: regime compatibility depends on which system is authoritative for regime state.
