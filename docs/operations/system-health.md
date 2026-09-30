# System Health, Failure Handling and Controlled Degradation

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-29 · **Category:** operations · **Roadmap stage:** **not mapped by §95** (CF-05) · **Sources:** §74, §90, §91

Canonical definition of the platform health states, the failures the platform must expect, and how it degrades safely.

## Health state machine

- **HLT-001** Health states · SYSTEM REQUIREMENT · §74 — Possible states: STARTING; HEALTHY; DEGRADED; WARNING; RECOVERING; SAFE MODE; TRADING HALTED; EXCHANGE DEGRADED; DATA DEGRADED; AI DEGRADED; EMERGENCY; STOPPED.
- **HLT-002** Formal state machine required · CONFIRMED REQUIREMENT · §74 — The final state machine must be formalized during architecture implementation.

## Failure is expected

- **HLT-003** Expected failures · CONFIRMED REQUIREMENT · §90 — Potential failures: market-data failure; exchange API failure; network failure; database failure; AI provider failure; model failure; execution timeout; partial fill; state inconsistency; resource exhaustion; process crash.
- **HLT-004** Fail safely · CONSTRAINT · §90 — The system must fail safely rather than fail creatively.

## Controlled degradation

- **HLT-005** Degradation examples · CONFIRMED ARCHITECTURAL PRINCIPLE · §91 — AI unavailable → deterministic capabilities continue where safe. Exchange unavailable → venue restricted → affected strategies restricted → other safe capabilities may continue.
- **HLT-006** Per-subsystem failure behavior · CONFIRMED REQUIREMENT · §91 — Failure behavior must be defined per subsystem.

HLT-006 is why every system specification has a "failure behavior" field. Part 1 leaves it unspecified for almost every system, so that field is expected from Part 2.

## Findings

- OQ-07: the final state machine. It needs transitions, the difference between DEGRADED and WARNING, and how the subsystem states combine.
- DUP-04: SAFE MODE, TRADING HALTED, and EMERGENCY overlap with the Risk Engine's kill switches and emergency shutdown (RSK-002), the arbitrage kill switch (ARB-010), and the §27 outcomes (RSK-006).
- CF-05: not mapped to any roadmap stage.
