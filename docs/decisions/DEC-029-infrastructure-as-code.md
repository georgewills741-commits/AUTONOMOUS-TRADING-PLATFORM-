# DEC-029 — Infrastructure as code is a mandatory production requirement

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 3, Q7](../handoffs/owner-decisions-03-part-2-findings.md))
- **Supersedes:** OPS-009 (PROPOSED), now DEPRECATED / REPLACED by OPS-014 to OPS-017

## Decision

| Requirement | What it says |
|---|---|
| OPS-014 | All production infrastructure is reproducible and version-controlled as code: compute, containers, networking, databases, storage, monitoring, logging, alerting, deployment, scaling, failover, backup, and disaster-recovery configuration. OPS-009's queues, environment variables, permissions, and resource limits are carried forward |
| OPS-015 | Infrastructure is separated logically from application code, and may live in a dedicated infrastructure repository when the project structure requires it. Nothing depends on undocumented manual server configuration |
| OPS-016 | Infrastructure changes are validated, tested, reviewed, auditable, and safely deployable and rollbackable. Secrets are never stored as plaintext in the repository |
| OPS-017 | Provisioning, recovery, migration between environments, and rebuilding production are automated and do not rely on the owner's physical availability |

## How this fits (builder notes)

| Requirement | Relationship |
|---|---|
| OPS-010 (single deployment source of truth in "the repository") | Still one source of truth. If a dedicated infrastructure repository is created (OPS-015), it holds the authoritative deployment definition and this repository links to it |
| TEC-011 (Docker images, Docker Compose on one host) | The container definitions are part of the infrastructure code. With high availability approved ([DEC-030](DEC-030-high-availability-and-single-active-copy.md)), production needs at least an active and a standby host. The single-host Compose deployment remains for development and the early stages |
| Choice of infrastructure-as-code tool | An implementation choice made when OPERATIONALIZATION is planned, under the stack delegation of [DEC-009](DEC-009-technology-stack.md). No tool is chosen now (P2§146) |
| SEC-005, MIG-009 (secrets) | OPS-016 is consistent |
| MIG-011 (configuration compiler), MIG-006 (migration) | Infrastructure code is how the target environment is provisioned during a migration |

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

The options shown with Q7 in [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md):

- **Not separately** (recommended): no separate commitment for now, because the Docker setup file kept in the repository already covers it. Not chosen: the owner made infrastructure as code a mandatory production requirement.
- **Yes, approve now:** the owner wrote an answer instead, which approves it and adds the scope and conditions of OPS-014 to OPS-017.
