# Deployment and Operational Readiness

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — nothing is deployed and nothing may be (handoff §00 items 24–25) · **Owner:** operations (cross-cutting) · **Roadmap stage:** OPERATIONALIZATION ("Deployment", "Canary", "Live operation") · **Sources:** §80, §81 (also §01 "controlled deployment", "continuous development")

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

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **OPS-007** Production change control · CONFIRMED REQUIREMENT · P2§164, P2§111 — Production changes should follow: proposal → review → test → approval → deploy → monitor → rollback if required.
- **OPS-008** Reproducible deployment package · CONFIRMED REQUIREMENT · P2§146, P2§255 — The project should define a reproducible deployment package. The exact technology is an architecture decision; possible approaches include containers, infrastructure configuration, deployment manifests, and environment templates. No implementation technology should be assumed prematurely.
- **OPS-009** Infrastructure as code · PROPOSED · P2§147, P2§256 — Where approved, infrastructure should be reproducible and version controlled, potentially covering: services; networks; storage; databases; monitoring; queues; environment variables; permissions; resource limits.
- **OPS-010** Single deployment source of truth · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§148, P2§257 — The repository must contain the authoritative deployment definition. Local and server environments may differ through explicit overrides.
- **OPS-011** Canary for production changes · CONFIRMED REQUIREMENT · P2§165 — Production strategy/system changes should use canary deployment where appropriate. Canary must have: limited exposure; defined success criteria; defined failure criteria; monitoring; a rollback path.
- **OPS-012** Deterministic, tested rollback · CONFIRMED REQUIREMENT · P2§166 — Rollback must be deterministic and tested. The system should know: what version was active; what changed; what prior version is valid; how to restore it; how to reconcile state afterward.
- **OPS-013** Canary is a production stage, not an environment · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — Canary runs in the production environment, the only one holding trading-enabled credentials (MODE-006), as a limited-exposure deployment stage with its own versions, limits, stop, and rollback (STR-013 to STR-020, OPS-011). The environments remain those of OPS-004, including research.

Notes:

- **OPS-008 and the technology stack.** [DEC-009](../decisions/DEC-009-technology-stack.md) is the architecture decision OPS-008 asks for: Docker images and Docker Compose (TEC-011). It was made deliberately, under the owner's delegation, not assumed.
- **OPS-009 stays PROPOSED** until the owner approves infrastructure as code. The Compose definition (TEC-011) already keeps services, networks, storage, environment variables, and resource limits under version control.
- **Environments (CF-15).** P2§161 and §236 list development, testing, staging, paper, canary, and production. OPS-004 lists development, testing, research, paper, staging, and production, the same list as constitution Rule 109. Canary cannot be a separate environment: it trades real money, and live credentials must never appear in a lower environment (P2§161). So it is a production stage (OPS-013). Research stays an environment because Part 2 does not remove it. Live credentials never reach lower environments (SEC-004, MODE-006), and paper never touches live accounts (PAP-011).
- **Live trading gate (P2§163, §235).** Live trading needs explicit authorization and activation. That is the operator raising the platform's maximum mode in policy (MODE-003, POL-005). Within that maximum, individual strategies progress through the readiness gates (STR-019 to STR-022).
- **Hosting, portability, backup, and migration** are in [Hosting, Backup, and Migration](hosting-and-migration.md) (MIG).

## Not yet specified

What counts as an "approved operational milestone" (to come from each stage's exit criteria when that stage is planned), production-readiness criteria (constitution Rule 214), and hosting location. Canary is defined in STR-011.
