# Market Regime Engine

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-04 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Regime engine") · **Sources:** §11

Canonical definition of market-regime awareness.

## Requirements

- **RGM-001** Explicit regime awareness · CONFIRMED REQUIREMENT · §11 — The system requires explicit market-regime awareness.
- **RGM-002** Regime states · SYSTEM REQUIREMENT · §11 — Possible states include: trending; ranging; high volatility; low volatility; panic/stress; uncertain; UNKNOWN REGIME.
- **RGM-003** No forced classification · CONSTRAINT · §11 — The system must not force uncertain conditions into an artificial classification.
- **RGM-004** Regime-based strategy rejection · SYSTEM REQUIREMENT · §11 — A strategy may be rejected when the current regime is incompatible.

## Boundary (§92)

- **Owns:** the current regime classification, including the uncertain and unknown states.
- **Used by:** the Directional Trading System ("regime compatibility", §05), the Opportunity Detection Engine (scans market regimes, §08), and the Trading Director (receives regime, §55).
- **Not yet specified in Part 1:** classification method, inputs, whether it is deterministic, tests.

## Findings

- OQ-10: Part 1 does not say whether regime classification is deterministic. §95 groups it with the deterministic data-foundation systems.
- DUP-08: the Market Analyst agent lists "regime interpretation" (AGT-008). Which one is authoritative for regime state is unresolved.
