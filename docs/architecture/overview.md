# Architecture Overview

> **Status:** DOCUMENTED (Handoff Part 1) — conceptual architecture; no implementation exists · **Owner:** platform architecture (cross-cutting) · **Sources:** §03, §04, §08, §69, §70, §79, §92–§94, §96–§98
>
> Canonical home for the structural principles that apply to every system. System-specific rules live in each system's own specification; this document links to them rather than restating them.

## Shape of the platform

The platform has three trading systems on top of shared infrastructure (§03):

```text
                 AUTONOMOUS TRADING PLATFORM
                           |
          +----------------+----------------+
          |                |                |
     DIRECTIONAL     CROSS-EXCHANGE    TRIANGULAR
       TRADING        ARBITRAGE         ARBITRAGE
          |                |                |
          +----------------+----------------+
                           |
                  SHARED INFRASTRUCTURE
                           |
 DATA / QUANT / STRATEGY / CAPITAL / RISK /
 PORTFOLIO / EXECUTION / AI / STORAGE /
 MONITORING / RECOVERY / SECURITY
```

Every system and capability named in Part 1, with its category, owner, and canonical document, is listed in the [system registry](system-registry.md). How they depend on each other is in the [dependency map](dependency-map.md).

- **ARCH-001** Multiple trading systems · CONFIRMED ARCHITECTURAL PRINCIPLE · §03 — The platform contains multiple trading systems: A. Directional Trading (trades based on validated directional opportunities); B. Cross-Exchange Arbitrage (trades executable discrepancies between venues); C. Triangular Arbitrage (trades executable multi-leg opportunities within a venue/market graph).
- **ARCH-002** One platform, not three applications · CONSTRAINT · §03 — These systems share infrastructure. They must not become three unrelated applications.
- **ARCH-003** Reuse of common infrastructure · CONFIRMED ARCHITECTURAL PRINCIPLE · §04 — Trading systems must reuse common infrastructure. They must not independently recreate: market-data ingestion; data normalization; quantitative calculations; risk enforcement; capital accounting; portfolio accounting; exchange connectivity; execution; logging; monitoring; storage; recovery; reconciliation; security; strategy lifecycle; AI infrastructure.
- **ARCH-004** Ownership split · CONFIRMED ARCHITECTURAL PRINCIPLE · §04 — A trading system owns its trading behavior. Shared infrastructure owns common platform capabilities.
- **ARCH-016** Duplication control · CONFIRMED ARCHITECTURAL PRINCIPLE · §97 — Shared capability must be implemented once where appropriate. Directional Trading and Arbitrage both consume the shared Risk Engine. Likewise capital; execution; portfolio; market data; quantitative calculations; monitoring; storage; recovery must not be unnecessarily duplicated.

## Layer separation

- **ARCH-008** Canonical conceptual flow · CONFIRMED ARCHITECTURAL PRINCIPLE · §70 — Data → quantitative computation → opportunity → strategy → AI reasoning → capital / risk → execution → external venue → reconciliation → portfolio state.
- **ARCH-009** Explicit layer authority · CONSTRAINT · §70 — Each layer must have explicit responsibility. No layer silently assumes another layer's authority.

Part 1 describes this flow in five places, and they do not fully agree on where AI sits or on whether capital or risk is checked first. See CF-01, CF-02 and CF-03 in the [findings register](../conflicts/register.md).

## What is deterministic and what belongs to AI

This summarizes rules defined in the linked documents. It adds no new rules.

| Deterministic (no LLM required) | AI (proposes and analyses; never enforces) |
|---|---|
| Market data pipeline — [market-data](../systems/market-data.md) | Market interpretation, research, hypothesis generation, news/sentiment — [AI architecture](../ai/ai-architecture.md) |
| Quantitative calculations — [quantitative engine](../systems/quantitative-engine.md) (QNT-003: if deterministic is possible, do not ask an LLM) | Trade proposals (Trading Director) and challenges (Devil's Advocate) — [agents](../ai/agents.md) |
| High-volume opportunity screening — [opportunity detection](../systems/opportunity-detection.md) | Strategy research and improvement proposals, always through the formal lifecycle — [strategy management](../systems/strategy/strategy-management.md) |
| Risk enforcement — [risk engine](../risk/risk-engine.md) | Interpreting natural-language instructions into proposed policy — [NL policy interface](../systems/policy/natural-language-policy-interface.md) |
| Execution — [execution engine](../systems/execution-engine.md) | Performance interpretation — [agents](../ai/agents.md) |
| Policy enforcement — [policy system](../systems/policy/policy-system.md) | |

AI output crosses into the deterministic side only through validated, structured contracts ([AI output validation](../ai/ai-output-validation.md)), and the deterministic Risk Engine keeps final authority ([risk hierarchy](../risk/risk-engine.md)). Whether the Market Regime Engine is deterministic is not stated (OQ-10).

## Market monitoring vs operational monitoring

- **ARCH-005** Two kinds of monitoring · CONFIRMED ARCHITECTURAL PRINCIPLE · §08 — The system must distinguish Market Monitoring ("What is happening across the trading universe?") from Operational Monitoring ("Is the platform itself functioning correctly?"). These must remain separate.

Market monitoring is owned by the [Opportunity Detection Engine](../systems/opportunity-detection.md). Operational monitoring is owned by [Monitoring and Observability](../operations/monitoring-and-observability.md) and [System Health](../operations/system-health.md).

## Cross-cutting engineering rules

- **ARCH-010** Numerical precision · CONFIRMED REQUIREMENT · §79 — Financial calculations must be deterministic and precise. Includes: prices; quantities; fees; slippage; P&L; position sizing; exposure; leverage; risk; reservations; arbitrage economics; portfolio accounting.
- **ARCH-011** Exchange-specific precision · CONSTRAINT · §79 — Exchange-specific precision must be respected.
- **ARCH-006** Consistency and anti-drift · CONFIRMED REQUIREMENT · §69 — The platform must preserve consistency as the project grows. The architecture should maintain: canonical definitions; versioned requirements; explicit ownership; traceability; dependency mapping; conflict detection; decision records; strategy versions; policy versions; model versions; interface contracts.
- **ARCH-007** Changes checked against architecture · CONSTRAINT · §69 — Changes must be checked against existing architecture before acceptance.

Failure handling and controlled degradation are defined in [System Health](../operations/system-health.md). Performance and latency are defined in [Performance, Latency and Continuous Operation](performance-and-latency.md). Security is defined in [Security Architecture](../security/security-architecture.md).

## Ownership and traceability rules

- **ARCH-012** System boundary definition · CONFIRMED ARCHITECTURAL PRINCIPLE · §92 — Every system must define: purpose; responsibility; inputs; outputs; dependencies; interfaces; data owned; data consumed; data produced; allowed actions; forbidden actions; failure behavior; tests; roadmap stage.
- **ARCH-013** Feature ownership chain · CONFIRMED ARCHITECTURAL PRINCIPLE · §93 — For every feature: what responsibility → which system owns it → which document defines it → which module implements it → which requirement tracks it → which roadmap stage → which test verifies it. This prevents duplicate implementation.
- **ARCH-014** Dependencies respected · CONFIRMED ARCHITECTURAL PRINCIPLE · §94 — Dependencies must be respected.
- **ARCH-015** Feature classification · CONFIRMED REQUIREMENT · §96 — Every feature must be classified as one of: CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE; CONSTRAINT; SYSTEM REQUIREMENT; PROPOSED; FUTURE; PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION; OPEN QUESTION; TECHNICAL CONCERN; DEPRECATED / REPLACED. No silent classification changes.
- **ARCH-017** Canonical source of truth · CONFIRMED ARCHITECTURAL PRINCIPLE · §98 — Major domains require authoritative locations. Other documents should reference the authoritative source.

Where these are applied: the §94 example chain and every recorded dependency are in the [dependency map](dependency-map.md) (ARCH-014); classification rules are in the [requirements README](../requirements/README.md) (ARCH-015); the canonical location of every concept is in the [source-of-truth map](source-of-truth-map.md) (ARCH-017).

Every system specification in `docs/systems/`, `docs/risk/`, `docs/ai/`, `docs/security/` and `docs/operations/` records the §92 fields that Part 1 supplies and lists the rest as not yet specified. Part 2 is expected to provide interfaces and contracts (§103 closing note).
