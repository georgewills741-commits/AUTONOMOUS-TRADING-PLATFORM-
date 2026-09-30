# Market Regime Engine

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-04 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Regime engine") · **Sources:** §11

Canonical definition of market-regime awareness.

## Requirements

- **RGM-001** Explicit regime awareness · CONFIRMED REQUIREMENT · §11 — The system requires explicit market-regime awareness.
- **RGM-002** Regime states · SYSTEM REQUIREMENT · §11 — Possible states include: trending; ranging; high volatility; low volatility; panic/stress; uncertain; UNKNOWN REGIME.
- **RGM-003** No forced classification · CONSTRAINT · §11 — The system must not force uncertain conditions into an artificial classification.
- **RGM-004** Regime-based strategy rejection · SYSTEM REQUIREMENT · §11 — A strategy may be rejected when the current regime is incompatible.

## Decisions applied (2026-09-30)

- **RGM-005** Deterministic classification · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Regime classification is deterministic: rules or statistical models over Quantitative Engine features, versioned, with explicit thresholds for UNCERTAIN and UNKNOWN REGIME. No LLM is used.
- **RGM-006** Authority over regime state · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine is authoritative for regime state. The Market Analyst may add interpretation but never sets regime state.

## Boundary (§92)

- **Owns:** the current regime classification, including the uncertain and unknown states.
- **Used by:** the Directional Trading System ("regime compatibility", §05), the Opportunity Detection Engine (scans market regimes, §08), and the Trading Director (receives regime, §55).
- **Not yet specified:** the specific classification rules and their inputs (expected with Part 2 contracts), tests.

## Findings (all resolved)

OQ-10 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RGM-005). DUP-08 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RGM-006).
