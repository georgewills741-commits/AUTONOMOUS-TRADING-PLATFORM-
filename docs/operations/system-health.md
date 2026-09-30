# System Health, Failure Handling and Controlled Degradation

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-29 · **Category:** operations · **Roadmap stage:** CORE TRADING FOUNDATION; hardened in OPERATIONALIZATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §74, §90, §91

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

HLT-006 is why every system specification has a "failure behavior" field. Part 1 leaves it unspecified for almost every system, Part 2 did not supply it either, so each system's failure behavior is specified when its stage is planned (constitution Rule 140).

## Decisions applied (2026-09-30)

- **HLT-007** Formal states · DEPRECATED / REPLACED · DEC-012 — The overall platform state is one of STARTING, RECOVERING, HEALTHY, DEGRADED, SAFE MODE, TRADING HALTED, EMERGENCY, or STOPPED. EXCHANGE DEGRADED (per venue), DATA DEGRADED, and AI DEGRADED are component conditions that make the overall state DEGRADED. WARNING is an alert severity (MON-007), not a trading state.
- **HLT-008** Trading allowed per state · DEPRECATED / REPLACED · DEC-012 — HEALTHY: trading allowed. DEGRADED: only strategies that do not depend on a degraded component. SAFE MODE: no new positions; reduce and close only. TRADING HALTED: no orders except those the operator approves. EMERGENCY: cancel all open orders, no new orders, and alert the operator; positions are closed automatically only if policy explicitly enables it. STARTING, RECOVERING, STOPPED: no trading.
- **HLT-009** Transitions · DEPRECATED / REPLACED · DEC-012 — Any state can move automatically to SAFE MODE, TRADING HALTED, or EMERGENCY when a deterministic rule or kill switch fires. Leaving those states requires operator action and the safe-resume checks (REC-004). STARTING moves to RECOVERING, and RECOVERING to HEALTHY only after reconciliation succeeds.
- **HLT-010** Ownership of platform state · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-012 — System Health owns the platform state, fed by operational monitoring. The Risk Engine reads it before authorizing any trade (RSK-010).

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

HLT-007 is replaced by HLT-011 and RSK-015. HLT-008 is replaced by RSK-015 to RSK-017. HLT-009 is replaced by HLT-012 and RSK-020.

- **HLT-011** Health state separate from safety level · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — System Health tracks the platform's health: STARTING, RECOVERING, HEALTHY, DEGRADED, or STOPPED, plus the component conditions EXCHANGE DEGRADED (per venue), DATA DEGRADED, and AI DEGRADED. WARNING is an alert severity. What the platform may do is governed by the Risk Engine's safety level (RSK-015). Of the §74 names, SAFE MODE and EMERGENCY are safety levels, and TRADING HALTED is the condition in which the global kill switch is active. Health conditions feed the deterministic rules that set the safety level.
- **HLT-012** Automatic progression to healthy · CONFIRMED REQUIREMENT · DEC-019 — The platform moves from STARTING through RECOVERING to HEALTHY automatically when the recovery checks pass (REC-011), without operator action. While they do not pass, it stays in RECOVERING, at safety level SAFE MODE or CRITICAL RECOVERY.

References to REC-011 in HLT-012 now resolve to REC-015 and REC-016 ([DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **HLT-013** Clock-drift detection · SYSTEM REQUIREMENT · P2§51 — Time is critical to market data, orders, fills, funding, arbitrage, latency, reconciliation, and backtesting. The system should detect meaningful clock drift.

What the platform does when drift is detected (for example marking data degraded) is specified when DATA FOUNDATION is planned; P2§51 requires detection only.

## Findings (all resolved)

OQ-07 → [DEC-012](../decisions/DEC-012-safety-architecture.md) (HLT-007 to HLT-010). DUP-04 → [DEC-012](../decisions/DEC-012-safety-architecture.md) (RSK-008). CF-05 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (CORE TRADING FOUNDATION).
