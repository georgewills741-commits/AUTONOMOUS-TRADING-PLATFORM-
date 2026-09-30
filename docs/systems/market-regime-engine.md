# Market Regime Engine

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-04 · **Category:** shared infrastructure · **Roadmap stage:** DATA FOUNDATION ("Regime engine") · **Sources:** §11

Canonical definition of market-regime awareness.

## Requirements

- **RGM-001** Explicit regime awareness · CONFIRMED REQUIREMENT · §11 — The system requires explicit market-regime awareness.
- **RGM-002** Regime states · SYSTEM REQUIREMENT · §11 — Possible states include: trending; ranging; high volatility; low volatility; panic/stress; uncertain; UNKNOWN REGIME.
- **RGM-003** No forced classification · CONSTRAINT · §11 — The system must not force uncertain conditions into an artificial classification.
- **RGM-004** Regime-based strategy rejection · SYSTEM REQUIREMENT · §11 — A strategy may be rejected when the current regime is incompatible.

## Decisions applied (2026-09-30)

- **RGM-005** Deterministic classification · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Regime classification is deterministic: rules or statistical models over Quantitative Engine features, versioned, with explicit thresholds for UNCERTAIN and UNKNOWN REGIME. No LLM is used.
- **RGM-006** Authority over regime state · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This engine is authoritative for regime state. The Market Analyst may add interpretation but never sets regime state.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **RGM-007** ABNORMAL state; evolving taxonomy · SYSTEM REQUIREMENT · P2§22, P2§212 — Potential states also include ABNORMAL. The taxonomy may evolve. UNKNOWN must remain a valid state.
- **RGM-008** No inference under UNKNOWN · CONSTRAINT · P2§23, P2§213 — If a strategy requires a known regime and the regime is UNKNOWN, the system must not infer a regime. UNKNOWN is not treated as safe and is not an invitation to guess. Possible responses: no trade; wait; reduced exposure; additional validation.

P2§22's state list (TRENDING, RANGING, HIGH_VOLATILITY, LOW_VOLATILITY, PANIC, ABNORMAL, UNKNOWN) does not repeat RGM-002's "stress" and "uncertain". Both lists are indicative ("possible", "potential"), so nothing is removed; the taxonomy is their union until it is finalized at DATA FOUNDATION.

## Boundary (§92)

- **Owns:** the current regime classification, including the uncertain and unknown states.
- **Used by:** the Directional Trading System ("regime compatibility", §05), the Opportunity Detection Engine (scans market regimes, §08), and the Trading Director (receives regime, §55).
- **Not yet specified:** the specific classification rules and their inputs (expected with Part 2 contracts), tests.

## Findings (all resolved)

OQ-10 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RGM-005). DUP-08 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RGM-006).
