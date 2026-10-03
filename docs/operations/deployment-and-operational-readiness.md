# Deployment and Operational Readiness

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — nothing is deployed and nothing may be (handoff §00 items 24–25) · **Owner:** operations (cross-cutting) · **Roadmap stage:** OPERATIONALIZATION ("Deployment", "Canary", "Live operation") · **Sources:** §80, §81 (also §01 "controlled deployment", "continuous development"); Part 3: P3§367, P3§490, P3§498

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
- **OPS-009** Infrastructure as code · DEPRECATED / REPLACED · P2§147, P2§256 — Where approved, infrastructure should be reproducible and version controlled, potentially covering: services; networks; storage; databases; monitoring; queues; environment variables; permissions; resource limits.
- **OPS-010** Single deployment source of truth · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§148, P2§257 — The repository must contain the authoritative deployment definition. Local and server environments may differ through explicit overrides.
- **OPS-011** Canary for production changes · CONFIRMED REQUIREMENT · P2§165 — Production strategy/system changes should use canary deployment where appropriate. Canary must have: limited exposure; defined success criteria; defined failure criteria; monitoring; a rollback path.
- **OPS-012** Deterministic, tested rollback · CONFIRMED REQUIREMENT · P2§166 — Rollback must be deterministic and tested. The system should know: what version was active; what changed; what prior version is valid; how to restore it; how to reconcile state afterward.
- **OPS-013** Canary is a production stage, not an environment · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — Canary runs in the production environment, the only one holding trading-enabled credentials (MODE-006), as a limited-exposure deployment stage with its own versions, limits, stop, and rollback (STR-013 to STR-020, OPS-011). The environments remain those of OPS-004, including research.

Notes:

- **OPS-008 and the technology stack.** [DEC-009](../decisions/DEC-009-technology-stack.md) is the architecture decision OPS-008 asks for: Docker images and Docker Compose (TEC-011). It was made deliberately, under the owner's delegation, not assumed.
- **OPS-009 is replaced** by OPS-014 to OPS-017. The owner made infrastructure as code mandatory ([DEC-029](../decisions/DEC-029-infrastructure-as-code.md)).
- **Environments (CF-15).** P2§161 and §236 list development, testing, staging, paper, canary, and production. OPS-004 lists development, testing, research, paper, staging, and production, the same list as constitution Rule 109. Canary cannot be a separate environment: it trades real money, and live credentials must never appear in a lower environment (P2§161). So it is a production stage (OPS-013). Research stays an environment because Part 2 does not remove it. Live credentials never reach lower environments (SEC-004, MODE-006), and paper never touches live accounts (PAP-011).
- **Live trading gate (P2§163, §235).** Live trading needs explicit authorization and activation. That is the operator raising the platform's maximum mode in policy (MODE-003, POL-005). Within that maximum, individual strategies progress through the readiness gates (STR-019 to STR-022).
- **Hosting, portability, backup, and migration** are in [Hosting, Backup, and Migration](hosting-and-migration.md) (MIG).

## Owner decisions applied (Part 2 findings, 2026-09-30)

From [DEC-029](../decisions/DEC-029-infrastructure-as-code.md) ([owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), Q7).

- **OPS-014** Infrastructure as code is mandatory · CONFIRMED REQUIREMENT · DEC-029 — Infrastructure as Code is a mandatory production requirement. All production infrastructure must be reproducible and version-controlled as code. This includes compute, containers, networking, databases, storage, monitoring, logging, alerting, deployment, scaling, failover, backup, and disaster-recovery configuration, and also the queues, environment variables, permissions, and resource limits carried forward from OPS-009.
- **OPS-015** Infrastructure separated from application code · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-029 — Infrastructure must be separated logically from application code and may be placed in a dedicated infrastructure repository when the project structure requires it. The system must not depend on undocumented manual server configuration.
- **OPS-016** Controlled infrastructure changes · CONSTRAINT · DEC-029 — Infrastructure changes must be validated, tested, reviewed, auditable, and safely deployable/rollbackable. Secrets must never be stored as plaintext in the repository.
- **OPS-017** Rebuild without the owner · CONFIRMED REQUIREMENT · DEC-029 — The architecture must support automated provisioning, recovery, migration between environments, and rebuilding production infrastructure without relying on the owner's physical availability.

Notes:

- **One source of truth.** If a dedicated infrastructure repository is created (OPS-015), it holds the authoritative deployment definition of OPS-010, and this repository links to it.
- **Tooling and hosts.** The infrastructure-as-code tool is chosen when OPERATIONALIZATION is planned (DEC-009 delegation). With high availability approved ([DEC-030](../decisions/DEC-030-high-availability-and-single-active-copy.md)), production runs on at least an active and a standby host (TEC-011 note).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **OPS-018** 24/7/365 operation and its limits · CONFIRMED REQUIREMENT · P3§367 — The production system is intended to operate continuously. It should be designed for 24/7/365 operation subject to: maintenance; planned deployment; emergency shutdown; venue availability; policy; infrastructure limitations; security events. The system should not require the user to manually restart the platform after every routine failure.
- **OPS-019** Availability targets from evidence · CONSTRAINT · P3§490 — The system should be designed toward continuous availability and autonomous operation. Availability targets must be established after architecture and infrastructure analysis. Claude must not invent an unsupported SLA such as 99.9999% without engineering evidence.
- **OPS-020** What a production change records · CONFIRMED REQUIREMENT · P3§498 — Changes to production must be controlled. Examples: strategy version; risk policy; capital policy; execution logic; exchange adapter; AI model; model router; infrastructure; database schema. Each significant change should have: version; approval; validation; rollback plan; audit record.

Notes:

- **OPS-018:** extends OPS-006. Automatic restart and resume follow REC-025 and REC-026.
- **OPS-019.** The availability target is value V-36, not set. Part 3's 99.9999% is an example of what must not be invented, not a target.
- **OPS-020:** adds the scope and the record to OPS-007's change process. Approval follows the owner of each change: policy changes through the Policy System (POL-005 to POL-007), strategy versions through the Readiness System (STR-019 to STR-022), infrastructure through OPS-016.

## Decisions applied (2026-10-01)

From the owner's directive on verification and platform independence ([DEC-034](../decisions/DEC-034-verification-and-platform-independence.md)).

- **OPS-021** Continuous engineering lifecycle · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-034 — The platform is a persistent, long-lived financial technology platform. Its lifecycle is: build → verify → release → deploy → operate → monitor → maintain → identify improvement → design → implement → verify → release → deploy → operate → continue. This cycle continues throughout the life of the platform.

For OPS-021, each step of the cycle already has its owner: verification (VER-001 to VER-003, GOV-012), release and deployment (OPS-007, OPS-011, OPS-012, OPS-020), monitoring (MON, HLT), improvement (STR-009 for strategies, GOV-002 for features). Every pass through the cycle follows the same governance as the first build (GOV-021).

## Production-readiness model (P3§541 item 23)

This section explains how production readiness is decided. It adds no requirement.

- **Per capability, not one flag.** Readiness is multi-dimensional (RDY-022): functional, security, data, risk, capital, execution, operational, monitoring, recovery, deployment, rollback, documentation, and testing readiness. The Readiness System keeps it per capability and shows it in the readiness matrix (RDY-023). A capability can go live while unrelated work continues (OPS-001, OPS-002).
- **Before any production trading:** the hardening list of RMP-010, the stage's three verification gates (VER; [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md)), and the operator raising the platform's maximum mode (MODE-003, POL-005).
- **"Production ready"** is claimed only when those criteria and their evidence are met (constitution Rule 214). The per-dimension criteria are set with each stage's completion criteria (constitution Rule 140) when OPERATIONALIZATION is planned.

## Findings

**Resolved:** CF-20 → [DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md): production never depends on any one machine; a machine of the owner's may host production only if it meets the same production-readiness criteria as any other production host (MIG-033; the model above) ([findings register](../conflicts/register.md); raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)).

## Not yet specified

What counts as an "approved operational milestone" (to come from each stage's exit criteria when that stage is planned), the per-dimension production-readiness criteria (constitution Rule 214; model above), the availability target (V-36), and hosting location. Canary is defined in STR-013 to STR-022 (which replaced STR-011) and OPS-011, OPS-013.
