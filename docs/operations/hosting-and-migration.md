# Hosting, Backup, and Migration

> **Status:** DOCUMENTED (Handoff Parts 2 and 3) — not implemented · **Owner:** cross-cutting requirement set (MIG); the modules that implement it are assigned when OPERATIONALIZATION is planned · **Roadmap stage:** OPERATIONALIZATION, except the design rules MIG-004 and MIG-010, which apply from the first implemented stage · **Sources:** P2§128–P2§145, P2§149–P2§154, P2§159, P2§167, P2§237–P2§263, P2§268, P2§318–P2§321, P2§340, P2§341; Part 3: P3§491, P3§497
>
> Canonical definition of where the platform can run and how its state is backed up and moved between hosts. Split-brain protection, the active execution authority, failover, and standby are defined in [Recovery and Reconciliation](../systems/recovery-and-reconciliation.md) (REC-019 to REC-022). The deployment package and change control are in [Deployment and Operational Readiness](deployment-and-operational-readiness.md) (OPS-007 to OPS-013). Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Principle

The deployment principle of Part 2 (P2§350): the same logical trading platform must be capable of running locally or on a server, with controlled migration between environments without corrupting financial, policy, strategy, or operational state.

## Hosting

- **MIG-001** Hosting choice · CONFIRMED REQUIREMENT · P2§128, P2§237 — The platform must support local hosting and remote server / cloud hosting. The user must not be forced into one hosting architecture.
- **MIG-002** Local hosting · SYSTEM REQUIREMENT · P2§129, P2§238 — Possible local components: trading services; database; monitoring; AI gateway; research; configuration; strategy registry; local execution. Required services are supported locally according to available resources. Minimum and recommended resources must eventually be documented.
- **MIG-003** Server hosting · CONFIRMED REQUIREMENT · P2§130, P2§239 — The same logical platform should be deployable remotely. Changing from local to server must not require rewriting trading logic.
- **MIG-004** Hosting abstraction; one platform · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§131, P2§240, P2§318, P2§340 — Trading / business logic is separated from the hosting environment. Trading components must not assume "this service always runs on the user's PC." Local or server hosting is an infrastructure/deployment decision; the trading logic remains the same, and the choice must not create two different trading platforms.
- **MIG-005** Resource differences · CONSTRAINT · P2§159, P2§268 — The system must account for different CPU, RAM, disk, network, and GPU. Trading correctness must not depend on a specific hardware configuration. Resource-dependent features should degrade explicitly.

## Portability and migration

- **MIG-006** Bidirectional portability · CONFIRMED REQUIREMENT · P2§132, P2§241, P2§341 — Required capability: local → export / backup → server → restore → validation → resume, and server → export / backup → local → restore → validation → resume, without rebuilding the trading architecture.
- **MIG-007** Migration is a formal process · CONSTRAINT · P2§133, P2§242 — Migration is a first-class capability. It must not mean randomly copying source files, database files, configuration, secrets, or cache. The platform should define a formal migration process.
- **MIG-008** Portable platform state · SYSTEM REQUIREMENT · P2§134, P2§243 — A potential migration package contains: database state; schema version; strategy registry; strategy versions; policy versions; user configuration; risk configuration; capital configuration; exchange configuration; venue metadata; opportunity records; experiment metadata; AI configuration; model routing; feature flags; audit metadata; deployment metadata; recovery state. Secrets must be handled separately and securely.
- **MIG-009** No plain-text secrets in migration packages · CONSTRAINT · P2§135, P2§244 — Migration packages must not contain plain-text: API keys; exchange secrets; wallet keys; passwords; authentication tokens. Secrets use secure migration mechanisms.
- **MIG-010** Portable vs environment-specific configuration · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§136, P2§245 — Configuration is split into portable configuration (strategies; policies; risk definitions; model-routing rules; market-universe rules) and environment-specific configuration (host paths; network addresses; runtime settings; hardware settings; storage paths; server credentials). Migration must resolve the target environment's values.
- **MIG-011** Configuration compiler / environment adapter · SYSTEM REQUIREMENT · P2§137, P2§246 — Conceptually: portable platform config → target environment → environment resolution → validation → deployable config. The target environment is resolved safely.
- **MIG-012** Database migration · CONSTRAINT · P2§138, P2§247 — Source state → schema version → migration plan → schema update → validation → restore. Financial records must never be silently corrupted; database migrations must preserve financial integrity.
- **MIG-013** Migration pre-flight · CONFIRMED REQUIREMENT · P2§139, P2§248 — Before migration: safely suspend new trading; determine positions; determine open orders; determine capital; determine exchange connectivity; verify the database; verify the backup; verify migration compatibility; verify the destination; verify dependencies; verify secrets; verify schema compatibility. Migration begins only after these state and environment checks.
- **MIG-014** Migration states · SYSTEM REQUIREMENT · P2§140, P2§249 — Migration has explicit deterministic states. Possible states: MIGRATION_PREPARING; MIGRATION_FROZEN; MIGRATION_IN_PROGRESS; VALIDATING; RECOVERY_READY; RESUMING; FAILED; ROLLBACK.
- **MIG-015** Open orders during migration · CONSTRAINT · P2§141, P2§250 — Internal orders must be reconciled against exchange orders. Copying database state does not transfer exchange state.
- **MIG-016** Open positions during migration · CONSTRAINT · P2§142, P2§251 — Internal positions must be reconciled against venue positions. If uncertain: NO NEW TRADE until reconciliation completes.
- **MIG-017** Capital during migration · CONSTRAINT · P2§143, P2§252 — Verify migrated internal state vs venue state vs ledger state. The migrated database alone is not authoritative; capital must be reconciled against authoritative external state.
- **MIG-018** Migration validation · CONFIRMED REQUIREMENT · P2§144, P2§253 — After restore: restore → schema → config → strategies → policy → capital → positions → orders → exchange health → system health → safe validation → resume authorization. Migration is incomplete until validation and reconciliation succeed.
- **MIG-019** Migration rollback · CONSTRAINT · P2§145, P2§254 — If validation fails, do not resume normal trading; a failed migration must not resume live trading. The platform should support: deployment rollback; prior-state restoration; previous-environment recovery; financial-state preservation; external-state reconciliation.
- **MIG-020** End-to-end migration sequence · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§319 — Local → safe trading state → backup → export portable state → verify → transfer → restore → environment configuration → schema validation → policy validation → strategy validation → capital reconciliation → position reconciliation → order reconciliation → exchange health → resume. Reverse migration must also be supported.
- **MIG-021** Migration completion criteria · CONSTRAINT · P2§320, P2§321 — Migration must preserve the project, not just code: it is successful only when the destination reproduces the relevant logical state, and "the application starts" is not sufficient. Migration is complete only when: the application starts; the database is valid; the schema is correct; configuration is valid; secrets are securely available; policies are intact; strategies are intact; active versions are correct; capital reconciles; positions reconcile; orders reconcile; exchanges are reachable; monitoring works; risk works; execution is configured correctly; active-instance ownership is established; safe operation is verified.
- **MIG-022** Backup and migration are distinct · CONFIRMED REQUIREMENT · P2§149, P2§258 — Backup answers "can we recover state?"; migration answers "can we intentionally move the platform?". Both are required.
- **MIG-023** Migration testing · CONFIRMED REQUIREMENT · P2§150, P2§259 — Eventually verify local → server, server → local, and server A → server B where relevant. Both migration directions must be tested.
- **MIG-024** Migration dry run · SYSTEM REQUIREMENT · P2§151, P2§260 — Where practical: source → export → package validation → simulated restore → dependency check → schema check → config check → report.
- **MIG-025** User-facing hosting experience · CONFIRMED REQUIREMENT · P2§152, P2§261 — The eventual product should abstract unnecessary infrastructure complexity; normal user experience may eventually be "run locally" or "run on server", with the platform handling the underlying deployment workflow. Normal users should not have to reconstruct the system manually.
- **MIG-026** Logical identity preservation · CONFIRMED REQUIREMENT · P2§153, P2§262 — Migration should preserve, where appropriate: user identity; policy history; strategy history; audit history; experiment history; configuration history; logical platform state; while updating environment-specific identifiers.
- **MIG-027** Environment identity · CONFIRMED REQUIREMENT · P2§154, P2§263 — Instances should remain distinguishable. Possible identifiers: platform ID; environment ID; deployment ID; version.

## Only one copy trades during a migration (owner decision)

From [DEC-030](../decisions/DEC-030-high-availability-and-single-active-copy.md) ([owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), Q5), resolving TC-07.

- **MIG-029** Freeze and new keys · CONSTRAINT · DEC-030 — During every move, freeze the old copy (MIG-013, MIG-014), then create new exchange API keys for the new location and delete the old ones, so the exchange itself refuses the old copy.
- **MIG-030** No trading before the old key is revoked · CONSTRAINT · DEC-030 — The destination does not trade on a venue until the old key for that venue is revoked. Where a venue offers no API for creating and revoking keys, the rotation is an operator step of the migration.

## Backup and disaster recovery

- **MIG-028** Disaster recovery · CONFIRMED REQUIREMENT · P2§167 — The project must eventually define: backup strategy; recovery points; recovery procedures; recovery validation; environment restoration; financial reconciliation; operational restart; incident procedures.

- **MIG-031** Disaster-recovery scope · CONFIRMED REQUIREMENT · P3§491 — The system must support recovery from: service failure; host failure; database failure; network failure; exchange outage; deployment failure; configuration corruption; security incident; infrastructure migration.
- **MIG-032** Migration and failover are distinct · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§497 — Migration is intentional movement; failover is an unexpected failure response. Both require reconciliation but have different operational workflows.

MIG-031 and MIG-032 come from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md) ([Part 3 reconciliation](../traceability/part-3-reconciliation.md), [DEC-031](../decisions/DEC-031-part-3-reconciliation.md)). MIG-031 lists what the disaster-recovery definition of MIG-028 must cover. A restore is followed by reconciliation, never trusted as it is (REC-028). Migration follows MIG-007 to MIG-021 and MIG-029, MIG-030; failover follows REC-021 to REC-024. The reliability and recovery model that ties these together is in [Reliability and recovery](reliability-and-recovery-model.md).

## How this fits the rest of the platform

- **Technology.** The initial deployment is Docker Compose on one host (TEC-011, [DEC-009](../decisions/DEC-009-technology-stack.md)). That host can be the operator's computer or a server, so MIG-001 holds without a second deployment. The Compose definition is the single deployment source of truth (OPS-010); local and server differ only through explicit overrides.
- **Reconciliation.** Every reconciliation step above is performed by Recovery and Reconciliation (REC-008), with the same rules as a restart (REC-014 to REC-018): the migrated database is recovery context, never authoritative financial state.
- **One active instance.** The source is frozen before the destination acts (MIG-013, MIG-014). Only one instance may trade an account (REC-019, REC-020). The execution lease (REC-013) protects instances that share a lease authority. Between two hosts with separate databases, the exchange keys are rotated instead (MIG-029, MIG-030). Automatic failover under high availability uses one shared lease authority (REC-023, REC-024).
- **Secrets** are never in a package (MIG-009, SEC-005). The destination receives newly issued keys (MIG-029) through the secret manager (SEC-005).
- **A migration failure** is a Safe Mode trigger (RSK-030) and an incident (INC-002).
- **Monitoring** covers migration and backup (MON-010). **Tests:** MIG-023 and MIG-024, and the [verification architecture](../architecture/verification-architecture.md).

## Findings

**Open:** CF-20: MIG-001 and MIG-002 (local hosting supported) vs the owner's statement that production must not depend on the owner's laptop ([findings register](../conflicts/register.md); raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)). MIG-001 and MIG-002 stand as written until the owner decides.

## Not yet specified

Package format, backup schedule and retention, recovery point and recovery time objectives (values to be added to the values register when set), minimum and recommended host resources (MIG-002), where the failover lease authority lives (REC-024), interfaces, tests. All infrastructure is kept as code (OPS-014), so the target environment is provisioned automatically (OPS-017).
