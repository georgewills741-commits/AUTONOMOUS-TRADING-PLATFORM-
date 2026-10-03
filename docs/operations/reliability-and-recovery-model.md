# Reliability and Recovery Model

> **Status:** DOCUMENTED (Handoff Part 3, P3§367–P3§377, P3§487–P3§500, P3§520, P3§549) — not implemented · **Owner:** cross-cutting; each step is owned by the system named below · **Roadmap stage:** CORE TRADING FOUNDATION (recovery, safety levels) and OPERATIONALIZATION (24/7 hardening, failover, disaster recovery)
>
> Part 3 asks for a reliability/recovery model (P3§541 item 25) with reliability documented under "Reliability/Operations" (P3§537). **This document is an index, not a specification.** It defines no requirement: it shows how the requirements that already own each piece fit together, so a reader can follow a failure from detection to resume. Placement: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

## Principles

- **24/7, but never blind.** The platform is designed to run 24/7/365 within stated limits (OPS-006, OPS-018) and recovers routine failures automatically (REC-010, RSK-021). A restart never authorizes trading by itself (REC-003, REC-025; SR-27 in the [System Rules Register](../requirements/system-rules-register.md)).
- **Isolate, do not stop everything.** A failure is contained to the affected service, venue, strategy, or instrument type (REC-026, RSK-038, RSK-020).
- **Safety first, then state, then resume.** Emergency priority is RSK-042; emergencies never cause uncontrolled simultaneous actions (RSK-041).
- **Known safe failures recover automatically; dangerous ones do not self-repair** (HLT-016, RSK-022).
- **Targets from evidence.** No availability or latency target is invented (OPS-019, PERF-018; values V-36 and V-06 to V-08).

## Failure → detection → response → resume

| Step | What happens | Owner | Requirements |
|---|---|---|---|
| 1. Detect | Health and operational intelligence across service, data, exchange, AI, capital, strategy, deployment, storage, network | SYS-29 System Health; SYS-28 Monitoring | HLT-010, HLT-011, HLT-015, MON-001 to MON-011 |
| 2. Classify | Transient vs latched cause; emergency type → safety level | SYS-09 Risk Engine (emergency controller) | RSK-016, RSK-021, RSK-022, V-27 |
| 3. Contain | Set the safety level, scoped to what is affected; kill switches; NO NEW POSITIONS; Safe Mode | SYS-09 Risk Engine | RSK-008, RSK-015, RSK-020, RSK-028 to RSK-030, RSK-040, RSK-043 |
| 4. Protect positions | Policy-driven, deterministic position handling | SYS-09 Risk Engine | RSK-017, RSK-018, RSK-019 |
| 5. Restart what failed | Supervised restart of the service, not the platform | Infrastructure (TEC-013) under SYS-29 | REC-025, REC-026, OPS-006 |
| 6. Recover state | Persisted state is untrusted context; verify database and configuration | SYS-11 Recovery and Reconciliation | REC-014, REC-015 |
| 7. Reconcile | External state is authoritative: balances, positions, orders, reservations, transfers | SYS-11 | REC-005, REC-015, REC-017, EXE-009 |
| 8. Verify authority | Hold the execution lease; recovery never bypasses auth, security, or active-instance protection | SYS-11, SYS-10 | REC-013, REC-018, REC-027, EXE-010 |
| 9. Readiness check | Recovery decision; readiness of affected capabilities reassessed | SYS-11; SYS-34 Readiness System | REC-016, RDY-024 |
| 10. Resume or stay safe | Progressive, scoped recovery; escalate if certainty cannot be restored | SYS-09, SYS-11 | RSK-023, RSK-024, REC-012, HLT-012 |
| 11. Learn | Incident lifecycle and structured lessons; no automatic behavior change | SYS-28 Incident Management | INC-001 to INC-005, STR-027 |

Every step is recorded in the audit trail (AUD-008, AUD-009).

## Emergency and health states

The safety level (RSK-015) and the health state (HLT-011) are two different things. Part 3's emergency state names (P3§372) map onto the safety levels and health states without merging their meanings; the mapping is in the [Risk Engine](../risk/risk-engine.md) (DUP-35). The final state machines are fixed when CORE TRADING FOUNDATION is planned (HLT-002).

## Standby, failover, migration, backup

| Situation | Model | Requirements |
|---|---|---|
| Main copy fails (high availability, approved) | Standby takes over automatically after ownership check and reconciliation; one lease authority, so at most one copy trades | REC-021 to REC-024, REC-029 |
| Standby while main is healthy | Monitors, validates, receives replicated state, prepares recovery; cannot trade without the lease | REC-020, REC-022, REC-029 |
| Intentional move local ↔ server | Formal migration; freeze the source; new keys; no trading before the old key is revoked | MIG-007 to MIG-021, MIG-029, MIG-030, MIG-032 |
| Restore from backup | Restored state is reconciled against external state before any trading | REC-028, MIG-022, MIG-028, MIG-031 |
| Disaster | Recovery from service, host, database, network, exchange, deployment, configuration, security, and migration failures; production never depends on one machine | MIG-028, MIG-031, MIG-033, OPS-014 to OPS-017 |

No distributed execution architecture is designed or approved, so P3§494's exception does not apply (see [Recovery and Reconciliation](../systems/recovery-and-reconciliation.md)).

## Change control and verification

Production changes are versioned, approved, validated, reversible, and audited (OPS-007, OPS-020, OPS-012). Recovery must be tested, not only documented (constitution Rule 159): chaos and failure testing (VER-003), migration testing (MIG-023, MIG-024), and load testing (VER-002) are in the [verification architecture](../architecture/verification-architecture.md).

## Not yet specified

The final safety-level and health state machines (HLT-002), the Safe Mode permission table (RSK-043), recovery point and recovery time objectives, the availability target (V-36), where the failover lease authority lives (REC-024) and how a standby obtains trading keys (TC-09), and interfaces and tests. All are produced when the owning stage is planned.
