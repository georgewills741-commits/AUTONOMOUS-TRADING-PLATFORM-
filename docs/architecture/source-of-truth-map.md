# Source-of-Truth Map

> **Status:** ACTIVE — 2026-09-30, updated 2026-10-01 and 2026-10-02. Answers "where is the source of truth?" for every major concept (constitution Rule 43, handoff §98, ARCH-017).
>
> If two documents seem to disagree, the one listed here wins, and the disagreement is recorded in the [findings register](../conflicts/register.md).

## Project control

| Concept | Canonical location |
|---|---|
| Builder operating rules | [docs/builder/claude-code-builder-constitution.md](../builder/claude-code-builder-constitution.md) |
| Owner's checkpoint, version-control, and three-stage verification rule | [docs/builder/checkpoint-and-verification-rule.md](../builder/checkpoint-and-verification-rule.md) ([DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)) |
| Master execution, consistency, verification and continuity constitution (builder rules) | [docs/builder/master-execution-constitution.md](../builder/master-execution-constitution.md) ([DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md)) |
| Owner's directive on three-level verification and platform independence | [docs/builder/verification-and-platform-independence-directive.md](../builder/verification-and-platform-independence-directive.md) ([DEC-034](../decisions/DEC-034-verification-and-platform-independence.md)) |
| How the builder texts combine; the one three-gate procedure | [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md) (DUP-39) |
| Current project state, next step, and continuation contract | [docs/project-state.md](../project-state.md) |
| Verification records and their format | [docs/traceability/README.md](../traceability/README.md) |
| Documentation index | [docs/README.md](../README.md) |
| Requirement text | The specification that owns the requirement (each requirement ID appears in exactly one specification) |
| Requirement index (ID → owner, class, source, stage) | [docs/requirements/registry.md](../requirements/registry.md) |
| Requirement conventions and classification | [docs/requirements/README.md](../requirements/README.md) |
| Handoff section → canonical location | Part 1: [docs/traceability/handoff-coverage.md](../traceability/handoff-coverage.md); Part 2: [docs/traceability/part-2-reconciliation.md](../traceability/part-2-reconciliation.md); Part 3: [docs/traceability/part-3-reconciliation.md](../traceability/part-3-reconciliation.md) |
| Systems and ownership | [docs/architecture/system-registry.md](system-registry.md) |
| Dependencies | [docs/architecture/dependency-map.md](dependency-map.md) |
| Roadmap and stage mapping | [docs/roadmap/roadmap.md](../roadmap/roadmap.md) |
| Decisions | [docs/decisions/](../decisions/README.md) |
| Conflicts and duplicate responsibilities | [docs/conflicts/register.md](../conflicts/register.md) |
| Open questions and technical concerns | [docs/open-questions/register.md](../open-questions/register.md) |
| Terminology | [docs/glossary.md](../glossary.md) |
| Technology stack | [docs/architecture/technology-stack.md](technology-stack.md) |
| Operating values and their classification | [docs/requirements/values-register.md](../requirements/values-register.md) |
| Original handoffs (HISTORICAL, not active) | [Part 1](../handoffs/part-1-core-platform-features.md), [Part 2](../handoffs/part-2-consolidated-additional-systems.md), [Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), and the owner's directives and answers in [docs/handoffs/](../handoffs/owner-correction-01-autonomous-operating-defaults.md) (latest: [owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md)) |
| Non-negotiable platform principles (index) | [docs/product/platform-overview.md](../product/platform-overview.md) (ARCH-028) |
| System rules (index of enforceable behavioral rules) | [docs/requirements/system-rules-register.md](../requirements/system-rules-register.md) (ARCH-038) |
| Feature-extensibility governance | [docs/architecture/architecture-governance.md](architecture-governance.md) (GOV) |
| Reliability and recovery model (index) | [docs/operations/reliability-and-recovery-model.md](../operations/reliability-and-recovery-model.md) |
| Documentation generator and checker | [tools/docs/](../../tools/docs/README.md) ([DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md)) |

## Product domains

Every system's canonical document is listed in the [system registry](system-registry.md). The handoff's own §98 examples map as follows:

| §98 domain | §98 location | Canonical location used | Note |
|---|---|---|---|
| Risk | `docs/risk/` | [docs/risk/risk-engine.md](../risk/risk-engine.md) | Followed |
| Directional Trading | `docs/systems/directional-trading.md` | [same](../systems/directional-trading.md) | Followed (§99's `systems/directional/` not used, CF-07) |
| Arbitrage | `docs/systems/arbitrage/` | [docs/systems/arbitrage/](../systems/arbitrage/arbitrage-intelligence.md) | Followed |
| AI | `docs/ai/` | [docs/ai/](../ai/ai-architecture.md) | Followed |
| Execution | `docs/systems/execution-engine.md` | [same](../systems/execution-engine.md) | Followed |
| Capital | `docs/systems/capital-management.md` | [same](../systems/capital-management.md) | Followed; the system is named Global Capital Authority |
| Policy | `docs/product/trading-policy.md` and `docs/systems/policy/` | [docs/systems/policy/](../systems/policy/policy-system.md) only | The product file is deliberately not created: runtime policy lives only in the Policy System (POL-009, [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md)) |
| Roadmap | `docs/roadmap/` | [docs/roadmap/roadmap.md](../roadmap/roadmap.md) | Followed |
| Requirements | `docs/requirements/` | [docs/requirements/](../requirements/README.md) | Followed |
| Architecture Decisions | `docs/decisions/` | [docs/decisions/](../decisions/README.md) | Followed |

## Key authorities

Direct answers to §100's "where does … authority live?":

| Authority | Owner | Canonical rule |
|---|---|---|
| Capital | SYS-07 Global Capital Authority | CAP-001 — [capital-management.md](../systems/capital-management.md) |
| Risk | SYS-09 Deterministic Risk Engine | RSK-001, RSK-004 — [risk-engine.md](../risk/risk-engine.md) |
| Execution | SYS-10 Execution Engine | EXE-001 — [execution-engine.md](../systems/execution-engine.md) |
| User policy | SYS-12 Policy System (NL interface is not the authority) | POL-002, NLP-003 — [policy-system.md](../systems/policy/policy-system.md) |
| Portfolio state | SYS-08 Portfolio Management | PRT-001, PRT-003 — [portfolio-management.md](../systems/portfolio-management.md) |
| Strategy versions and promotion | SYS-14 Strategy Management | STR-001, STR-005 — [strategy-management.md](../systems/strategy/strategy-management.md) |
| Kill switches, trading authorization, kill-switch recovery | SYS-09 Risk Engine | RSK-008, RSK-021 to RSK-025 — [risk-engine.md](../risk/risk-engine.md) ([DEC-012](../decisions/DEC-012-safety-architecture.md)) |
| Platform health state | SYS-29 System Health | HLT-011, HLT-012 — [system-health.md](../operations/system-health.md) |
| Safety level (NORMAL … CRITICAL RECOVERY) and emergency handling | SYS-09 Risk Engine (emergency controller) | RSK-015 to RSK-020 — [risk-engine.md](../risk/risk-engine.md) ([DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)) |
| Rebalancing decision | SYS-07 Global Capital Authority | CAP-023 to CAP-025 — [capital-management.md](../systems/capital-management.md) |
| Transfer execution | SYS-10 Execution Engine | EXE-009 — [execution-engine.md](../systems/execution-engine.md) |
| Restart recovery sequence | SYS-11 Recovery and Reconciliation | REC-014 to REC-018 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Active execution instance (lease) | SYS-11 Recovery and Reconciliation | REC-013, EXE-010 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Canary readiness, approval, and scaling | SYS-34 Readiness System (the Governance and Readiness Engine) for readiness and approval; SYS-14 for the lifecycle stage | STR-013 to STR-022 — [strategy-management.md](../systems/strategy/strategy-management.md) |
| Autonomy boundaries | SYS-12 Policy System | POL-011 — [policy-system.md](../systems/policy/policy-system.md) |
| Realized financial history (P&L, fees, transfers, balances) | SYS-33 Trading Ledger | LED-004, LED-006 — [custody-and-ledger.md](../systems/custody-and-ledger.md) |
| Operating mode | SYS-12 Policy System | POL-008 — [policy-system.md](../systems/policy/policy-system.md) |
| Trading universe | SYS-05 with SYS-12 exclusions | OPP-009 — [opportunity-detection.md](../systems/opportunity-detection.md) |
| Allocation ranking | SYS-07 Global Capital Authority | CAP-017 — [capital-management.md](../systems/capital-management.md) |
| Regime state | SYS-04 Market Regime Engine | RGM-006 — [market-regime-engine.md](../systems/market-regime-engine.md) |

## Canonical authorities (ARCH-027)

Part 2 requires exactly one of each fundamental authority (P2§184). Each has one owner:

| Authority (P2§184) | Owner | Canonical rule |
|---|---|---|
| Capital Authority | SYS-07 Global Capital Authority | CAP-001, CAP-017 — [capital-management.md](../systems/capital-management.md) |
| Risk Authority | SYS-09 Risk Engine | RSK-001, RSK-012 — [risk-engine.md](../risk/risk-engine.md) |
| Portfolio Authority | SYS-08 Portfolio Management | PRT-001, PRT-003 — [portfolio-management.md](../systems/portfolio-management.md) |
| Policy Authority | SYS-12 Policy System | POL-002, POL-009, NLP-003 — [policy-system.md](../systems/policy/policy-system.md) |
| Fee Engine | SYS-03 Quantitative Engine | QNT-005, QNT-007 — [quantitative-engine.md](../systems/quantitative-engine.md) |
| Slippage Engine | SYS-03 Quantitative Engine | QNT-006, QNT-007 — [quantitative-engine.md](../systems/quantitative-engine.md) |
| Exchange abstraction | SYS-01 Exchange Adapter Layer | EXA-004, EXA-011 — [exchange-adapters.md](../systems/exchange-adapters.md) |
| Audit system | SYS-30 Auditability / Event and Decision History | AUD-005, AUD-012 — [audit-and-event-history.md](../systems/audit-and-event-history.md) |
| Market-data normalization layer | SYS-02 Market-Data Infrastructure | MKD-011 — [market-data.md](../systems/market-data.md) |
| Strategy Registry | SYS-14 Strategy Management | STR-023 — [strategy-management.md](../systems/strategy/strategy-management.md) |
| Readiness System | SYS-34 Readiness System | RDY-001, RDY-006 — [readiness-system.md](../systems/readiness-system.md) |
| Opportunity Registry (Opportunity Database) | SYS-05 Opportunity Detection Engine | OPP-016 — [opportunity-detection.md](../systems/opportunity-detection.md) |
| Execution state (P3§467) | SYS-10 Execution Engine | EXE-002, ARCH-037 — [execution-engine.md](../systems/execution-engine.md) |
| Financial ledger (P3§467) | SYS-33 Trading Ledger | LED-004, LED-006, ARCH-037 — [custody-and-ledger.md](../systems/custody-and-ledger.md) |

The master execution constitution (§26) names the same authorities in its own words: Execution Authority is execution state, Market Data Authority the market-data normalization layer, Canonical Financial Ledger the financial ledger, and Audit System the audit system ([glossary](../glossary.md); [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md)).

Other Part 2 concepts and where they are defined:

| Concept | Owner | Canonical rule |
|---|---|---|
| Deterministic core vs AI layer, responsibility table | Platform architecture | ARCH-019 to ARCH-022 — [overview.md](overview.md) |
| AI Resource & Decision Governor | SYS-22 (AI gateway) | AIL-008, AIL-009 — [ai-architecture.md](../ai/ai-architecture.md) |
| Paper trading architecture, simulated capital | SYS-16 Paper Trading (capital state in SYS-07) | PAP-004 to PAP-012 — [paper-trading.md](../systems/strategy/paper-trading.md) |
| Readiness states, evidence, blockers | SYS-34 Readiness System | RDY-002 to RDY-005 — [readiness-system.md](../systems/readiness-system.md) |
| Daily System Intelligence Dashboard and Report | SYS-28 Monitoring and Observability | DSI-001 to DSI-006 — [daily-system-intelligence.md](../operations/daily-system-intelligence.md) |
| Incident records | SYS-28 Monitoring and Observability | INC-001 to INC-003 — [incident-management.md](../operations/incident-management.md) |
| Hosting, portability, migration, backup, disaster recovery | Hosting, backup, and migration set | MIG-001 to MIG-028; MIG-029 to MIG-033 (owner decisions DEC-030 and DEC-036; Part 3) — [hosting-and-migration.md](../operations/hosting-and-migration.md) |
| Active execution authority across hosts, split-brain, standby, failover | SYS-11 Recovery and Reconciliation | REC-019 to REC-022 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Environments (canary is a production stage) | Deployment and operational readiness | OPS-004, OPS-013 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |
| Platform verification (performance, load, chaos) | Verification set | VER-001 to VER-003 — [verification-architecture.md](verification-architecture.md) |
| Data quality, quarantine, lineage | SYS-02 Market-Data Infrastructure | MKD-008 to MKD-010 — [market-data.md](../systems/market-data.md) |
| Decision lineage | SYS-30 | AUD-012 — [audit-and-event-history.md](../systems/audit-and-event-history.md) |
| Strategy drift, missed and false opportunities | SYS-21 Performance Controller | PFC-009, PFC-012, PFC-013 — [performance-controller.md](../systems/performance-controller.md) |
| Loss-streak and excessive-trading protection, NO NEW POSITIONS | SYS-09 Risk Engine | RSK-026 to RSK-029 — [risk-engine.md](../risk/risk-engine.md) |
| Safety floor (immutable safety invariants) and the layered control model | SYS-09 Risk Engine | RSK-034 to RSK-039 with RSK-004 and RSK-010 — [risk-engine.md](../risk/risk-engine.md) ([DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)) |
| Capital buckets and progressive capability activation | SYS-07 (buckets), SYS-34 (eligibility) | CAP-029 to CAP-033, RDY-008 — [capital-management.md](../systems/capital-management.md) |
| High availability and failover | SYS-11 Recovery and Reconciliation | REC-021, REC-023, REC-024 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Infrastructure as code | Deployment and operational readiness | OPS-014 to OPS-017 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |
| Capability registry, capability availability, blockers, readiness matrix | SYS-34 Readiness System | RDY-009 to RDY-026 — [readiness-system.md](../systems/readiness-system.md) |
| Rebalancing Engine (decision model, anti-churn, emergency rebalancing) | SYS-07 Global Capital Authority | CAP-037 to CAP-042 — [capital-management.md](../systems/capital-management.md) |
| Capital change events and capital states | SYS-07 Global Capital Authority | CAP-044, CAP-046 — [capital-management.md](../systems/capital-management.md) |
| Rule precedence including Part 3's layers | SYS-09 Risk Engine | RSK-004, RSK-049 (RSK-048 replaced, DEC-035) — [risk-engine.md](../risk/risk-engine.md) |
| Safe Mode permissions, emergency priority | SYS-09 Risk Engine | RSK-041 to RSK-043 — [risk-engine.md](../risk/risk-engine.md) |
| Service-level recovery; restart is not resume | SYS-11 Recovery and Reconciliation | REC-025, REC-026 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Operational intelligence | SYS-29 System Health | HLT-015 — [system-health.md](../operations/system-health.md) |
| Production-readiness model | Deployment and operational readiness, with SYS-34 | RDY-022, RMP-010 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |

## Further canonical sources (master knowledge-base audit, 2026-10-02)

Added by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md), which found these had canonical requirements but no row here. Nothing new is decided; where a source is not yet specified, the row says so.

| Concept | Owner | Canonical rule |
|---|---|---|
| Security controls, credentials, secrets | SYS-31 Security Architecture; precedence above the user's hard policy is RSK-049 | SEC-001, SEC-002, SEC-004 to SEC-009 — [security-architecture.md](../security/security-architecture.md) |
| Reconciliation logic (orders, balances, positions, ledger) | SYS-11 Recovery and Reconciliation; other systems invoke it | REC-008 — [recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Deployment definition and configuration | The repository's deployment definition (OPS-010); portable vs environment-specific configuration (MIG-010, MIG-011). Policy content is never kept in the repository: it lives in the Policy System's versioned store (POL-009). MIG-010 counts policies as portable configuration, which moves with the platform state (MIG-008), not with the deployment definition. Secrets are never in the repository (SEC-005) | OPS-010 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md); MIG-010, MIG-011 — [hosting-and-migration.md](../operations/hosting-and-migration.md) |
| Production version and change record | Production change control | OPS-012, OPS-020 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md). Where the runtime release record is kept is not yet specified (OPERATIONALIZATION) |
| Database schemas | Each owning system, through its contracts (ARCH-025; data schemas are a contract type, GOV-007) | GOV-006 (versioned or migrated), OPS-020 (a schema change is a recorded production change), MIG-008 (schema version in the platform state). Not yet specified per system |
| AI gateway, model routing, AI budgets | SYS-22 (gateway), SYS-24 Model Router, SYS-25 AI Cost Manager | AIL-006, AIL-007, RTR-003, COST-002 — [ai-architecture.md](../ai/ai-architecture.md), [model-management.md](../ai/model-management.md) |
| Risk-limit values (runtime) | SYS-12 Policy System, versioned runtime store (autonomy bounds: the "Autonomy boundaries" row above); how each value is classified is the [values register](../requirements/values-register.md) | POL-009 — [policy-system.md](../systems/policy/policy-system.md) |
| Feature lifecycle | Architecture governance | GOV-024 — [architecture-governance.md](architecture-governance.md) |
| Platform lifecycle; the platform is independent of Claude Code | Platform overview and deployment | PLT-029 — [platform-overview.md](../product/platform-overview.md); OPS-021 — [deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md); GOV-021 to GOV-023 — [architecture-governance.md](architecture-governance.md) |
