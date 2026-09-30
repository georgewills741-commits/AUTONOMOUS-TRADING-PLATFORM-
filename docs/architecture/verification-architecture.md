# Verification Architecture

> **Status:** DOCUMENTED (Handoff Part 2) — not implemented · **Owner:** cross-cutting requirement set (VER) · **Roadmap stage:** every stage; load and chaos testing are part of production hardening (RMP-010) · **Sources:** P2§168–P2§170, P2§194, P2§333
>
> Where each kind of platform verification is defined. This is about testing the **platform**. How Claude verifies its own work in three passes at every stage is defined by the [builder constitution](../builder/claude-code-builder-constitution.md) (Part XX) and is not repeated here. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Requirements

- **VER-001** Performance testing · CONFIRMED REQUIREMENT · P2§168 — The system should measure: latency; throughput; CPU; memory; database performance; queue latency; network latency; execution path latency; AI latency.
- **VER-002** Load testing · CONFIRMED REQUIREMENT · P2§169 — Test behavior under: high market event rates; many opportunities; multiple venues; concurrent strategies; large historical datasets; AI bursts; reconciliation load.
- **VER-003** Chaos testing · CONFIRMED REQUIREMENT · P2§170 — Where appropriate, test: exchange disconnect; WebSocket failure; database failure; AI provider failure; queue failure; network degradation; slow responses; partial services; process restart; host failure. The system should enter safe states rather than undefined behavior.

## Map of verification requirements

Each kind of verification is defined once, in the document that owns the behavior. This table only points to them.

| What is verified | Where it is defined |
|---|---|
| Performance, load, chaos | VER-001 to VER-003 (this document); measured budgets PERF-008 to PERF-012 |
| Strategy validity: backtest integrity, dataset separation, anti-overfitting, walk-forward, stress, Monte Carlo | BKT-002 to BKT-009 |
| Paper evidence and paper-vs-expected | PAP-004 to PAP-012, PFC-010 |
| Readiness before canary and production | RDY-001 to RDY-007, STR-019 to STR-022 |
| Canary and rollback | STR-013 to STR-020, OPS-011, OPS-012 (rollback must be tested) |
| Recovery and reconciliation | REC-014 to REC-018; recovery must be tested (constitution Rule 159) |
| Migration, dry run, and both directions | MIG-018, MIG-021, MIG-023, MIG-024 |
| Security boundaries | SEC-009; security boundaries must be tested (constitution Rule 154) |
| AI outputs | AIV-004, AIV-016 to AIV-020 |
| Environment protection (tests never touch production) | MODE-006, SEC-004, PAP-011; constitution Rule 117 |

## Per-stage verification

Each roadmap stage gets its objective, scope, tests, verification, and completion criteria when it is planned (constitution Rule 140). Verification methods are then assigned per requirement (ARCH-030). Nothing is verified yet: every requirement is DOCUMENTED.
