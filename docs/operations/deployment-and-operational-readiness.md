# Deployment and Operational Readiness

> **Status:** DOCUMENTED (Handoff Part 1) — nothing is deployed and nothing may be (handoff §00 items 24–25) · **Owner:** operations (cross-cutting) · **Roadmap stage:** OPERATIONALIZATION ("Deployment", "Canary", "Live operation") · **Sources:** §80, §81 (also §01 "controlled deployment", "continuous development")

Canonical definition of what "operational" means and how development continues once part of the platform is live.

## Requirements

- **OPS-001** Operational readiness is not project completion · CONFIRMED ARCHITECTURAL PRINCIPLE · §80 — Operational readiness is not the same as total project completion.
- **OPS-002** Subsystems can go live independently · CONFIRMED REQUIREMENT · §80 — A completed subsystem can become operational while unrelated development continues, provided production boundaries remain protected.
- **OPS-003** Development while online · CONFIRMED REQUIREMENT · §81 — After an approved operational milestone: development may continue; production paths remain protected; new features remain isolated until verified; deployments are controlled; versioning is explicit; rollback exists; database changes are compatible; shared infrastructure changes are tested; new functionality passes required gates before activation.

## Not yet specified in Part 1

Deployment targets and environments (constitution Rule 109 lists development, testing, research, paper, staging, production), the definition of "canary" (OQ-09), what counts as an "approved operational milestone", rollback mechanics, and production-readiness criteria (constitution Rule 214).
