# Risk Engine, Risk Hierarchy and No-Trade Outcomes

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-09 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Risk") · **Sources:** §25–§27
>
> Canonical location for risk per §98 (`docs/risk/`).

Canonical definition of deterministic risk enforcement, the authority hierarchy, and the valid decision outcomes, including declining to trade.

## Deterministic risk enforcement

- **RSK-001** Deterministic enforcement · CONFIRMED ARCHITECTURAL PRINCIPLE · §25 — Risk enforcement must be deterministic.
- **RSK-002** Risk controls · SYSTEM REQUIREMENT · §25 — Controls may include: position limits; exposure limits; leverage limits; loss limits; position sizing; slippage limits; liquidity requirements; capital reserves; strategy limits; portfolio limits; exchange limits; correlation controls; trade authorization; emergency shutdown; kill switches.
- **RSK-003** AI cannot bypass risk · CONSTRAINT · §25 — AI cannot bypass these controls.

## Authority hierarchy

- **RSK-004** Risk decision hierarchy · CONFIRMED ARCHITECTURAL PRINCIPLE · §26 — Authority, highest first: system safety → user hard constraints → portfolio / risk policy → validated strategy rules → deterministic market conditions → AI analysis / proposal.
- **RSK-005** No override from below · CONSTRAINT · §26 — Lower layers cannot override higher layers.

The platform-level priority order (capital preservation first, opportunity targets last) is PLT-006 in the [platform overview](../product/platform-overview.md).

## No-trade and uncertainty outcomes

- **RSK-006** Valid outcomes · SYSTEM REQUIREMENT · §27 — Valid outcomes include: TRADE; WAIT; NO TRADE; REDUCE RISK; SUSPEND STRATEGY; SAFE MODE; ROLLBACK; UNCERTAIN; I DON'T KNOW.
- **RSK-007** No manufactured confidence · CONSTRAINT · §27 — The system must not manufacture confidence when evidence is insufficient.

Placing §27 in the Risk Engine document is PROPOSED. Part 1 calls it the "No-Trade / Uncertainty System" but does not name an owning system.

## Boundary (§92)

- **Owns:** deterministic risk decisions and the controls in RSK-002.
- **Consumes:** user hard constraints from the [Policy System](../systems/policy/policy-system.md); portfolio and exposure state from [Portfolio Management](../systems/portfolio-management.md); strategy output and AI proposals (validated first, AIV-004).
- **Must not:** be bypassed or overridden by AI (RSK-003, AIL-003), by research (STR-008), or by lower layers (RSK-005).
- **Not yet specified in Part 1:** limit values, what "system safety" at the top of the hierarchy contains, failure behavior, interfaces, tests.

## Findings

- DUP-04: kill switches, emergency shutdown, and safe mode also appear under Arbitrage Intelligence (ARB-010), System Health (HLT-001), and the §27 outcomes. §47 defers to a "global safety architecture" that Part 1 never defines. See OQ-06.
- DUP-09: arbitrage-specific and multi-leg risk are listed by Arbitrage Intelligence and Triangular Arbitrage.
- DUP-19: position sizing is also listed by the Quantitative Engine and Directional Trading.
- CF-01: the order of the capital-authority and risk checks differs between §19 and §94.
- CF-06: this engine enforces user hard constraints, but §95 maps no stage for the structured policy that holds them.
- OQ-20: the "system safety" rules at the top of RSK-004 are not enumerated.
