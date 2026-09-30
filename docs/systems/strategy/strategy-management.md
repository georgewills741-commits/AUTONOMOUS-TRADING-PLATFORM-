# Strategy Management (Lifecycle, Strategy Factory, Versioning)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-14 · **Category:** shared infrastructure ("Strategy lifecycle", §04) · **Roadmap stage:** DIRECTIONAL TRADING ("Strategy lifecycle"), although it serves all trading systems (CF-05) · **Sources:** §34–§38

Canonical definition of how strategies are researched, validated, promoted, versioned, improved, and retired, and of what research may and may not touch.

## Lifecycle and promotion

- **STR-001** Strategy lifecycle · CONFIRMED REQUIREMENT · §34 — Research → strategy specification → backtest → validation → out-of-sample / walk-forward → stress / robustness → paper → approval → canary → production.
- **STR-002** No AI shortcut through stages · CONSTRAINT · §34 — No strategy bypasses required stages because an AI recommends it.

## Strategy Factory

- **STR-003** Strategy Factory responsibilities · SYSTEM REQUIREMENT · §35 — Research; hypothesis generation; candidate creation; backtesting; validation; robustness; paper testing; comparison; versioning; promotion; retirement.
- **STR-004** Factory cannot touch live trading · CONSTRAINT · §35 — It must not directly modify live trading.

## Versioning

- **STR-005** Every meaningful change is a new version · CONFIRMED REQUIREMENT · §36 — Every meaningful strategy change creates a new version (examples: Directional Trend v1.0, v1.1, v2.0).
- **STR-006** No silent production changes · CONSTRAINT · §36 — Active production strategies must never be silently modified.

## Research / production separation

- **STR-007** What research may do · CONFIRMED ARCHITECTURAL PRINCIPLE · §37 — Research may: analyze history; generate hypotheses; create candidate strategies; backtest; stress-test; paper-test.
- **STR-008** What research must not touch · CONSTRAINT · §37 — Research must not directly modify: live strategies; production risk limits; exchange credentials; execution logic; user hard constraints; kill switches.

## Controlled improvement

- **STR-009** Improvement path · CONFIRMED REQUIREMENT · §38 — When a strategy deteriorates: performance deterioration → investigation → research → hypothesis → new strategy version → backtest → out-of-sample → robustness → paper → approval → canary → production.
- **STR-010** Forbidden reaction to losses · CONSTRAINT · §38 — Never: loss → AI changes live strategy → risk increases.

## Boundary (§92)

- **Owns:** strategy versions, lifecycle state, promotion, and retirement.
- **Uses:** [Backtesting](backtesting.md) and [Paper Trading](paper-trading.md) as lifecycle stages; AI research agents as assistants ([agents](../../ai/agents.md), AGT-012, AGT-013).
- **Must not:** modify live trading directly (STR-004), or let research change protected production controls (STR-008).
- **Not yet specified in Part 1:** validation and promotion criteria, who approves, what "canary" means (OQ-09), interfaces, tests.

## Findings

- DUP-18: research, hypothesis generation, and candidate creation are also AI agent responsibilities (AGT-010, AGT-012).
- DUP-20: the Directional Trading System lists strategy selection, backtesting, paper trading, and strategy improvement among its own responsibilities (DIR-002).
- OQ-09: "canary" appears in STR-001, STR-009, and §95 but is not defined.
- CF-05: strategy lifecycle is mapped to the DIRECTIONAL TRADING stage but also applies to arbitrage.
