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

## Decisions applied (2026-09-30)

- **STR-011** Canary · CONFIRMED REQUIREMENT · DEC-015 — In canary, a newly approved strategy version trades live with a capped capital allocation and tightened risk limits, for a minimum period and trade count. Promotion to production requires expected-vs-actual results within tolerance and no safety incidents. A breach suspends the version or rolls back to the previous one. Initial operator-configurable defaults: capital cap of 5% of the strategy's target allocation; minimum 14 days and 50 trades.
- **STR-012** The Strategy Factory owns the research process · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — The Strategy Factory owns and coordinates the research process, including "research coordination" (§51). AI agents assist inside it.

## Boundary (§92)

- **Owns:** strategy versions, lifecycle state, promotion, and retirement.
- **Uses:** [Backtesting](backtesting.md) and [Paper Trading](paper-trading.md) as lifecycle stages; AI research agents as assistants ([agents](../../ai/agents.md), AGT-012, AGT-013).
- **Must not:** modify live trading directly (STR-004), or let research change protected production controls (STR-008).
- **Not yet specified:** validation thresholds for each lifecycle stage (expected with Part 2 verification architecture), interfaces, tests. The operator approves promotions; canary is STR-011.

## Findings (all resolved)

DUP-18 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (STR-012). DUP-20 → [DEC-011](../../decisions/DEC-011-ownership-of-shared-responsibilities.md) (DIR-004). OQ-09 → [DEC-015](../../decisions/DEC-015-modes-canary-and-policy-governance.md) (STR-011). CF-05 → [DEC-016](../../decisions/DEC-016-roadmap-stage-placement.md) (built in DIRECTIONAL TRADING as shared infrastructure; ARBITRAGE depends on it).
