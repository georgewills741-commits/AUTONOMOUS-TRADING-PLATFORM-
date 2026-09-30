# Documentation Index

The canonical project knowledge base for the Autonomous Trading Platform: a production-grade autonomous cryptocurrency trading platform ([platform overview](product/platform-overview.md)). The conversation is not the source of truth; this repository is (handoff §00).

**Current state:** documentation of Handoff Part 1 is complete. Part 2 has not been received. **No product implementation exists or is authorized.** Details: [project state](project-state.md).

## Start here

1. [Project state](project-state.md): where the project stands and the next approved step.
2. [Platform overview](product/platform-overview.md): what the platform is and must do.
3. [Architecture overview](architecture/overview.md): structural principles, and what is deterministic vs AI.
4. [System registry](architecture/system-registry.md): every system, its owner document, and its stage.
5. [Open questions](open-questions/register.md) and [findings](conflicts/register.md): what is unresolved.

## Status labels used throughout

| Label | Meaning |
|---|---|
| DOCUMENTED | Recorded from a handoff; not implemented, not verified |
| PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | Not a production requirement until the owner confirms it |
| PROPOSED | A decision or placement in effect provisionally, awaiting owner review |
| RECOMMENDED — NOT YET APPROVED | The builder's recommendation; not a requirement |
| HISTORICAL | Source input kept for traceability; not an active source of truth |

## Layout

| Area | Contents |
|---|---|
| [product/](product/platform-overview.md) | [Platform overview](product/platform-overview.md) · [Operating modes](product/operating-modes.md) |
| [architecture/](architecture/overview.md) | [Overview](architecture/overview.md) · [System registry](architecture/system-registry.md) · [Dependency map](architecture/dependency-map.md) · [Source-of-truth map](architecture/source-of-truth-map.md) · [Performance, latency and continuous operation](architecture/performance-and-latency.md) |
| [systems/](systems/) (data foundation) | [Exchange adapters](systems/exchange-adapters.md) · [Market data](systems/market-data.md) · [Quantitative engine](systems/quantitative-engine.md) · [Market regime engine](systems/market-regime-engine.md) · [Opportunity detection](systems/opportunity-detection.md) |
| [systems/](systems/) (core trading) | [True net-profit engine](systems/true-net-profit-engine.md) · [Global Capital Authority](systems/capital-management.md) · [Portfolio](systems/portfolio-management.md) · [Execution engine](systems/execution-engine.md) · [Recovery and reconciliation](systems/recovery-and-reconciliation.md) · [Audit and event history](systems/audit-and-event-history.md) |
| [systems/policy/](systems/policy/policy-system.md) | [Policy system](systems/policy/policy-system.md) · [Natural Language Policy Interface](systems/policy/natural-language-policy-interface.md) |
| [systems/strategy/](systems/strategy/strategy-management.md) | [Strategy management](systems/strategy/strategy-management.md) · [Backtesting](systems/strategy/backtesting.md) · [Paper trading](systems/strategy/paper-trading.md) |
| Trading systems | [Directional trading](systems/directional-trading.md) · [Cross-exchange arbitrage](systems/arbitrage/cross-exchange-arbitrage.md) · [Triangular arbitrage](systems/arbitrage/triangular-arbitrage.md) · [Arbitrage intelligence](systems/arbitrage/arbitrage-intelligence.md) · [Performance controller](systems/performance-controller.md) |
| Unconfirmed | [Platform account, custody and ledger](systems/custody-and-ledger.md) (PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION) |
| [risk/](risk/risk-engine.md) | [Risk engine, hierarchy and no-trade outcomes](risk/risk-engine.md) |
| [ai/](ai/ai-architecture.md) | [AI architecture](ai/ai-architecture.md) · [AI output validation](ai/ai-output-validation.md) · [Model management](ai/model-management.md) · [Agents](ai/agents.md) · [AI memory](ai/ai-memory.md) |
| [security/](security/security-architecture.md) | [Security architecture](security/security-architecture.md) |
| [operations/](operations/system-health.md) | [Monitoring and observability](operations/monitoring-and-observability.md) · [System health](operations/system-health.md) · [Deployment and operational readiness](operations/deployment-and-operational-readiness.md) |
| [requirements/](requirements/README.md) | [Conventions](requirements/README.md) · [Registry (index)](requirements/registry.md) |
| [roadmap/](roadmap/roadmap.md) | [Master roadmap](roadmap/roadmap.md) |
| [decisions/](decisions/README.md) | [Decision log](decisions/README.md) |
| [conflicts/](conflicts/register.md) | [Findings register](conflicts/register.md): conflicts and duplicate responsibilities |
| [open-questions/](open-questions/register.md) | [Open questions and technical concerns](open-questions/register.md) |
| [traceability/](traceability/handoff-coverage.md) | [Handoff coverage](traceability/handoff-coverage.md) · [Part 1 verification record](traceability/part-1-verification.md) |
| [glossary.md](glossary.md) | Canonical terminology |
| [handoffs/](handoffs/part-1-core-platform-features.md) | [Part 1](handoffs/part-1-core-platform-features.md) (HISTORICAL) |
| [builder/](builder/claude-code-builder-constitution.md) | [Claude Code Builder Constitution](builder/claude-code-builder-constitution.md): how the repository is built and maintained |
