# Documentation Index

The canonical project knowledge base for the Autonomous Trading Platform: a production-grade autonomous cryptocurrency trading platform ([platform overview](product/platform-overview.md)). The conversation is not the source of truth; this repository is (handoff §00).

**Current state:** Handoff Parts 1, 2, and 3 are documented and reconciled into one knowledge base ([DEC-024](decisions/DEC-024-part-2-reconciliation.md), [DEC-031](decisions/DEC-031-part-3-reconciliation.md)). The owner has answered the Part 2 findings ([DEC-026](decisions/DEC-026-safety-floor-and-layered-control.md) to [DEC-030](decisions/DEC-030-high-availability-and-single-active-copy.md)). On 2026-10-01 the owner's master execution constitution and directive on verification and platform independence were adopted ([DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md), [DEC-034](decisions/DEC-034-verification-and-platform-independence.md)). On 2026-10-02 the owner approved the Part 3 reconciliation and answered every open item ([DEC-035](decisions/DEC-035-owner-decisions-part-3-findings.md)); TC-09 and TC-10 are decided when their stages are planned. The older decision records now state their alternatives (TC-08). The complete documentation review is done ([master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md), verdict B). On 2026-10-03 the owner accepted it, decided its four findings (CF-20, CF-21, OQ-28, DUP-40), and authorized Stage 1 planning ([DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md)). Implementation is not authorized; see [project state](project-state.md).

## Start here

1. [Project state](project-state.md): where the project stands and the next approved step.
2. [Platform overview](product/platform-overview.md): what the platform is and must do.
3. [Architecture overview](architecture/overview.md): structural principles, and what is deterministic vs AI.
4. [System registry](architecture/system-registry.md): every system, its owner document, and its stage.
5. [Decision log](decisions/README.md): every decision, and who made it.
6. [Technology stack](architecture/technology-stack.md): what the platform will be built with.

## Status labels used throughout

| Label | Meaning |
|---|---|
| DOCUMENTED | Recorded from a handoff; not implemented, not verified |
| FUTURE | Recorded but deliberately not built now (e.g. custody) |
| DEPRECATED / REPLACED | Superseded; the replacement is named |
| ACCEPTED (delegated) | A decision the builder made under an explicit owner instruction; the owner may override it |
| HISTORICAL | Source input kept for traceability; not an active source of truth |

## Layout

| Area | Contents |
|---|---|
| [product/](product/platform-overview.md) | [Platform overview](product/platform-overview.md) · [Operating modes](product/operating-modes.md) · platform principles index (in the overview) |
| [architecture/](architecture/overview.md) | [Overview](architecture/overview.md) · [System registry](architecture/system-registry.md) · [Dependency map](architecture/dependency-map.md) · [Source-of-truth map](architecture/source-of-truth-map.md) · [Technology stack](architecture/technology-stack.md) · [Performance, latency and continuous operation](architecture/performance-and-latency.md) · [Verification architecture](architecture/verification-architecture.md) · [Architecture governance](architecture/architecture-governance.md) |
| [systems/](systems/) (data foundation) | [Exchange adapters](systems/exchange-adapters.md) · [Market data](systems/market-data.md) · [Quantitative engine](systems/quantitative-engine.md) · [Market regime engine](systems/market-regime-engine.md) · [Opportunity detection](systems/opportunity-detection.md) |
| [systems/](systems/) (core trading) | [True net-profit engine](systems/true-net-profit-engine.md) · [Global Capital Authority](systems/capital-management.md) · [Portfolio](systems/portfolio-management.md) · [Execution engine](systems/execution-engine.md) · [Recovery and reconciliation](systems/recovery-and-reconciliation.md) · [Audit and event history](systems/audit-and-event-history.md) |
| [systems/policy/](systems/policy/policy-system.md) | [Policy system](systems/policy/policy-system.md) · [Natural Language Policy Interface](systems/policy/natural-language-policy-interface.md) |
| [systems/strategy/](systems/strategy/strategy-management.md) | [Strategy management](systems/strategy/strategy-management.md) · [Backtesting](systems/strategy/backtesting.md) · [Paper trading](systems/strategy/paper-trading.md) · [Readiness System](systems/readiness-system.md) |
| Trading systems | [Directional trading](systems/directional-trading.md) · [Cross-exchange arbitrage](systems/arbitrage/cross-exchange-arbitrage.md) · [Triangular arbitrage](systems/arbitrage/triangular-arbitrage.md) · [Arbitrage intelligence](systems/arbitrage/arbitrage-intelligence.md) · [Performance controller](systems/performance-controller.md) |
| Ledger (custody FUTURE) | [Platform account, custody and ledger](systems/custody-and-ledger.md) |
| [risk/](risk/risk-engine.md) | [Risk engine, hierarchy and no-trade outcomes](risk/risk-engine.md) |
| [ai/](ai/ai-architecture.md) | [AI architecture](ai/ai-architecture.md) · [AI output validation](ai/ai-output-validation.md) · [Model management](ai/model-management.md) · [Agents](ai/agents.md) · [AI memory](ai/ai-memory.md) |
| [security/](security/security-architecture.md) | [Security architecture](security/security-architecture.md) |
| [operations/](operations/system-health.md) | [Monitoring and observability](operations/monitoring-and-observability.md) · [System health](operations/system-health.md) · [Deployment and operational readiness](operations/deployment-and-operational-readiness.md) · [Daily System Intelligence](operations/daily-system-intelligence.md) · [Incident management](operations/incident-management.md) · [Hosting, backup, and migration](operations/hosting-and-migration.md) · [Reliability and recovery model](operations/reliability-and-recovery-model.md) |
| [requirements/](requirements/README.md) | [Conventions](requirements/README.md) · [Registry (index)](requirements/registry.md) · [Values register](requirements/values-register.md) · [System Rules Register](requirements/system-rules-register.md) |
| [roadmap/](roadmap/roadmap.md) | [Master roadmap](roadmap/roadmap.md) |
| [decisions/](decisions/README.md) | [Decision log](decisions/README.md) |
| [conflicts/](conflicts/register.md) | [Findings register](conflicts/register.md): conflicts and duplicate responsibilities (all resolved) |
| [open-questions/](open-questions/register.md) | [Open questions and technical concerns](open-questions/register.md) (TC-09 and TC-10 open until their stages; all others resolved) |
| [traceability/](traceability/README.md) | [Records and their format](traceability/README.md) · [Handoff coverage (Part 1)](traceability/handoff-coverage.md) · [Part 2 reconciliation](traceability/part-2-reconciliation.md) · [Part 2 verification record](traceability/part-2-verification.md) · [Part 3 reconciliation](traceability/part-3-reconciliation.md) · [Part 3 verification record](traceability/part-3-verification.md) · [Owner decisions 3 verification](traceability/owner-decisions-03-verification.md) · [Part 1 verification record](traceability/part-1-verification.md) · [Resolution verification record](traceability/resolution-verification.md) · [Owner correction 1 verification record](traceability/owner-correction-01-verification.md) · [Owner decisions 2 verification record](traceability/owner-decisions-02-verification.md) · [Integrity verification 2026-10-01](traceability/integrity-verification-2026-10-01.md) · [Governance adoption verification](traceability/governance-adoption-verification.md) · [Owner decisions 4 verification](traceability/owner-decisions-04-verification.md) · [TC-08 verification](traceability/tc-08-alternatives-verification.md) · [Master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md) · [Owner decisions 5 verification](traceability/owner-decisions-05-verification.md) |
| [glossary.md](glossary.md) | Canonical terminology |
| [handoffs/](handoffs/part-1-core-platform-features.md) | [Part 1](handoffs/part-1-core-platform-features.md) · [Part 2](handoffs/part-2-consolidated-additional-systems.md) · [Part 3](handoffs/part-3-consolidated-autonomy-capital-scaling.md) · [Owner decisions 5: audit findings, review acceptance, Stage 1 planning](handoffs/owner-decisions-05-audit-findings.md) · [Owner decisions 4: Part 3 findings and review](handoffs/owner-decisions-04-part-3-findings.md) · [Owner decisions 3: Part 2 findings](handoffs/owner-decisions-03-part-2-findings.md) · [Owner correction 1: autonomous operating defaults](handoffs/owner-correction-01-autonomous-operating-defaults.md) · [Owner decisions 2: CF-11 to CF-13](handoffs/owner-decisions-02-cf-11-to-cf-13.md) (all HISTORICAL) |
| [builder/](builder/claude-code-builder-constitution.md) | [Claude Code Builder Constitution](builder/claude-code-builder-constitution.md): how the repository is built and maintained · [Checkpoint and verification rule](builder/checkpoint-and-verification-rule.md): the owner's three-gate verification and checkpoint-commit rule ([DEC-032](decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)) · [Master execution constitution](builder/master-execution-constitution.md): execution, consistency, verification, and continuity rules ([DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md)) · [Verification and platform-independence directive](builder/verification-and-platform-independence-directive.md): the owner's three-level verification and platform independence ([DEC-034](decisions/DEC-034-verification-and-platform-independence.md)). All four are ACTIVE and loaded by `CLAUDE.md` |
| [../tools/docs/](../tools/docs/README.md) | Documentation generator and checker ([DEC-025](decisions/DEC-025-documentation-tooling-in-repository.md)); run it after every documentation change |
