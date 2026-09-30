# Deployment and Operational Readiness

> **Status:** DOCUMENTED (Handoff Part 1) — nothing is deployed and nothing may be (handoff §00 items 24–25) · **Owner:** operations (cross-cutting) · **Roadmap stage:** OPERATIONALIZATION ("Deployment", "Canary", "Live operation") · **Sources:** §80, §81 (also §01 "controlled deployment", "continuous development")

Canonical definition of what "operational" means and how development continues once part of the platform is live.

## Requirements

- **OPS-001** Operational readiness is not project completion · CONFIRMED ARCHITECTURAL PRINCIPLE · §80 — Operational readiness is not the same as total project completion.
- **OPS-002** Subsystems can go live independently · CONFIRMED REQUIREMENT · §80 — A completed subsystem can become operational while unrelated development continues, provided production boundaries remain protected.
- **OPS-003** Development while online · CONFIRMED REQUIREMENT · §81 — After an approved operational milestone: development may continue; production paths remain protected; new features remain isolated until verified; deployments are controlled; versioning is explicit; rollback exists; database changes are compatible; shared infrastructure changes are tested; new functionality passes required gates before activation.

## Decisions applied (2026-09-30)

- **OPS-004** Separate environments · CONFIRMED REQUIREMENT · DEC-015 — The environments are development, testing, research, paper, staging, and production, each with its own configuration, database, and credentials. Only production holds trading-enabled credentials (MODE-006).
- **OPS-005** Traceable, reversible deployments · CONFIRMED REQUIREMENT · DEC-009 — Every production deployment records the deployed version, can be rolled back to the previous version (TEC-011), and requires the stage's verification to have passed.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **OPS-006** 24/7 operation · CONFIRMED REQUIREMENT · DEC-019 — The platform is designed to operate 24/7. Services are supervised and restarted automatically (REC-010, TEC-013), and recovery and monitoring functions keep running during SAFE MODE and CRITICAL RECOVERY (REC-012).

## Not yet specified

What counts as an "approved operational milestone" (to come from the roadmap's stage exit criteria after Part 2), production-readiness criteria (constitution Rule 214), and hosting location. Canary is defined in STR-011.
