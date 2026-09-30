# Documentation Index

The canonical project knowledge base for the Autonomous Trading Platform: a production-grade autonomous cryptocurrency trading platform ([platform overview](product/platform-overview.md)). The conversation is not the source of truth; this repository is (handoff §00).

**Current state:** Handoff Parts 1 and 2 are documented and reconciled into one knowledge base ([DEC-024](decisions/DEC-024-part-2-reconciliation.md)). The owner's operating model and decisions are applied. Part 2 raised findings that wait for the owner (CF-14, OQ-24 to OQ-26, TC-07). Implementation is not authorized; see [project state](project-state.md).

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
| [architecture/](architecture/overview.md) | [Overview](architecture/overview.md) · [System registry](architecture/system-registry.md) · [Dependency map](architecture/dependency-map.md) · [Source-of-truth map](architecture/source-of-truth-map.md) · [Technology stack](architecture/technology-stack.md) · [Performance, latency and continuous operation](architecture/performance-and-latency.md) · [Verification architecture](architecture/verification-architecture.md) |
| [systems/](systems/) (data foundation) | [Exchange adapters](systems/exchange-adapters.md) · [Market data](systems/market-data.md) · [Quantitative engine](systems/quantitative-engine.md) · [Market regime engine](systems/market-regime-engine.md) · [Opportunity detection](systems/opportunity-detection.md) |
| [systems/](systems/) (core trading) | [True net-profit engine](systems/true-net-profit-engine.md) · [Global Capital Authority](systems/capital-management.md) · [Portfolio](systems/portfolio-management.md) · [Execution engine](systems/execution-engine.md) · [Recovery and reconciliation](systems/recovery-and-reconciliation.md) · [Audit and event history](systems/audit-and-event-history.md) |
| [systems/policy/](systems/policy/policy-system.md) | [Policy system](systems/policy/policy-system.md) · [Natural Language Policy Interface](systems/policy/natural-language-policy-interface.md) |
| [systems/strategy/](systems/strategy/strategy-management.md) | [Strategy management](systems/strategy/strategy-management.md) · [Backtesting](systems/strategy/backtesting.md) · [Paper trading](systems/strategy/paper-trading.md) · [Readiness System](systems/readiness-system.md) |
| Trading systems | [Directional trading](systems/directional-trading.md) · [Cross-exchange arbitrage](systems/arbitrage/cross-exchange-arbitrage.md) · [Triangular arbitrage](systems/arbitrage/triangular-arbitrage.md) · [Arbitrage intelligence](systems/arbitrage/arbitrage-intelligence.md) · [Performance controller](systems/performance-controller.md) |
| Ledger (custody FUTURE) | [Platform account, custody and ledger](systems/custody-and-ledger.md) |
| [risk/](risk/risk-engine.md) | [Risk engine, hierarchy and no-trade outcomes](risk/risk-engine.md) |
| [ai/](ai/ai-architecture.md) | [AI architecture](ai/ai-architecture.md) · [AI output validation](ai/ai-output-validation.md) · [Model management](ai/model-management.md) · [Agents](ai/agents.md) · [AI memory](ai/ai-memory.md) |
| [security/](security/security-architecture.md) | [Security architecture](security/security-architecture.md) |
| [operations/](operations/system-health.md) | [Monitoring and observability](operations/monitoring-and-observability.md) · [System health](operations/system-health.md) · [Deployment and operational readiness](operations/deployment-and-operational-readiness.md) · [Daily System Intelligence](operations/daily-system-intelligence.md) · [Incident management](operations/incident-management.md) · [Hosting, backup, and migration](operations/hosting-and-migration.md) |
| [requirements/](requirements/README.md) | [Conventions](requirements/README.md) · [Registry (index)](requirements/registry.md) · [Values register](requirements/values-register.md) |
| [roadmap/](roadmap/roadmap.md) | [Master roadmap](roadmap/roadmap.md) |
| [decisions/](decisions/README.md) | [Decision log](decisions/README.md) |
| [conflicts/](conflicts/register.md) | [Findings register](conflicts/register.md): conflicts and duplicate responsibilities (CF-14 open) |
| [open-questions/](open-questions/register.md) | [Open questions and technical concerns](open-questions/register.md) (OQ-24 to OQ-26 and TC-07 open) |
| [traceability/](traceability/handoff-coverage.md) | [Handoff coverage (Part 1)](traceability/handoff-coverage.md) · [Part 2 reconciliation](traceability/part-2-reconciliation.md) · [Part 2 verification record](traceability/part-2-verification.md) · [Part 1 verification record](traceability/part-1-verification.md) · [Resolution verification record](traceability/resolution-verification.md) · [Owner correction 1 verification record](traceability/owner-correction-01-verification.md) · [Owner decisions 2 verification record](traceability/owner-decisions-02-verification.md) |
| [glossary.md](glossary.md) | Canonical terminology |
| [handoffs/](handoffs/part-1-core-platform-features.md) | [Part 1](handoffs/part-1-core-platform-features.md) · [Part 2](handoffs/part-2-consolidated-additional-systems.md) · [Owner correction 1: autonomous operating defaults](handoffs/owner-correction-01-autonomous-operating-defaults.md) · [Owner decisions 2: CF-11 to CF-13](handoffs/owner-decisions-02-cf-11-to-cf-13.md) (all HISTORICAL) |
| [builder/](builder/claude-code-builder-constitution.md) | [Claude Code Builder Constitution](builder/claude-code-builder-constitution.md): how the repository is built and maintained |
| [../tools/docs/](../tools/docs/README.md) | Documentation generator and checker ([DEC-025](decisions/DEC-025-documentation-tooling-in-repository.md)); run it after every documentation change |
