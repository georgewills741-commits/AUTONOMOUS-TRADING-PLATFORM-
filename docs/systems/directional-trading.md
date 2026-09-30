# Directional Trading System

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-17 · **Category:** trading system · **Roadmap stage:** DIRECTIONAL TRADING · **Sources:** §05 (also §03 A)
>
> Canonical location per §98 (`docs/systems/directional-trading.md`).

Canonical definition of the directional trading system: trading on expected market movement.

## Requirements

- **DIR-001** Purpose · CONFIRMED REQUIREMENT · §05 — The Directional Trading System identifies and manages opportunities where expected market movement creates a valid trading opportunity.
- **DIR-002** Responsibilities · SYSTEM REQUIREMENT · §05 — Responsibilities may include: trend analysis; momentum; signal generation; entry conditions; exit conditions; confirmation; market-condition filtering; regime compatibility; strategy selection; position sizing; stop-loss; take-profit; risk/reward; trade filtering; strategy monitoring; backtesting; paper trading; performance analysis; strategy improvement.
- **DIR-003** Cannot bypass platform controls · CONSTRAINT · §05 — It cannot bypass: capital controls; risk controls; execution validation; user restrictions; portfolio limits; exchange constraints.

## Decisions applied (2026-09-30)

- **DIR-004** Directional logic, shared infrastructure · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This system provides the directional-specific logic: signals, entry and exit, stops and targets, and selection among validated strategy versions. It uses the shared systems for backtesting, paper trading, performance analysis, strategy improvement, and monitoring.
- **DIR-005** Initial research candidates · SYSTEM REQUIREMENT · DEC-018 — The first directional strategies to research are trend following (moving-average and breakout entries with ATR-based stops) and momentum, on liquid markets, on 1-hour and 4-hour timeframes. Each must pass the full lifecycle (STR-001) before trading.

## Boundary (§92)

- **Owns:** directional trading behavior: signals, entry/exit logic, stop-loss and take-profit rules for directional strategies (ARCH-004).
- **Consumes:** opportunities from the [Opportunity Detection Engine](opportunity-detection.md); regime from the [Market Regime Engine](market-regime-engine.md); validated strategy versions from [Strategy Management](strategy/strategy-management.md).
- **Must pass through:** the [Global Capital Authority](capital-management.md), [Risk Engine](../risk/risk-engine.md), and [Execution Engine](execution-engine.md) (DIR-003).
- **Not yet specified:** interfaces, tests. Initial research candidates are DIR-005; instruments are PLT-011.

## Findings (all resolved)

DUP-20 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (DIR-004). DUP-19 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (RSK-011). DUP-08 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RGM-006). OQ-21 → [DEC-018](../decisions/DEC-018-initial-directional-research-candidates.md) (DIR-005).
