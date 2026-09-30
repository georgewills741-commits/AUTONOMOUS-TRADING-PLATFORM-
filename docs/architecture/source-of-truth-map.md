# Source-of-Truth Map

> **Status:** ACTIVE — 2026-09-30. Answers "where is the source of truth?" for every major concept (constitution Rule 43, handoff §98, ARCH-017).
>
> If two documents seem to disagree, the one listed here wins, and the disagreement is recorded in the [findings register](../conflicts/register.md).

## Project control

| Concept | Canonical location |
|---|---|
| Builder operating rules | [docs/builder/claude-code-builder-constitution.md](../builder/claude-code-builder-constitution.md) |
| Current project state and next step | [docs/project-state.md](../project-state.md) |
| Documentation index | [docs/README.md](../README.md) |
| Requirement text | The specification that owns the requirement (each requirement ID appears in exactly one specification) |
| Requirement index (ID → owner, class, source, stage) | [docs/requirements/registry.md](../requirements/registry.md) |
| Requirement conventions and classification | [docs/requirements/README.md](../requirements/README.md) |
| Handoff section → canonical location | [docs/traceability/handoff-coverage.md](../traceability/handoff-coverage.md) |
| Systems and ownership | [docs/architecture/system-registry.md](system-registry.md) |
| Dependencies | [docs/architecture/dependency-map.md](dependency-map.md) |
| Roadmap and stage mapping | [docs/roadmap/roadmap.md](../roadmap/roadmap.md) |
| Decisions | [docs/decisions/](../decisions/README.md) |
| Conflicts and duplicate responsibilities | [docs/conflicts/register.md](../conflicts/register.md) |
| Open questions and technical concerns | [docs/open-questions/register.md](../open-questions/register.md) |
| Terminology | [docs/glossary.md](../glossary.md) |
| Technology stack | [docs/architecture/technology-stack.md](technology-stack.md) |
| Operating values and their classification | [docs/requirements/values-register.md](../requirements/values-register.md) |
| Original handoffs (HISTORICAL, not active) | [docs/handoffs/](../handoffs/part-1-core-platform-features.md) |

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
| Canary readiness, approval, and scaling | SYS-14 Strategy Management (Governance and Readiness Engine) | STR-013 to STR-022 — [strategy-management.md](../systems/strategy/strategy-management.md) |
| Autonomy boundaries | SYS-12 Policy System | POL-011 — [policy-system.md](../systems/policy/policy-system.md) |
| Realized financial history (P&L, fees, transfers, balances) | SYS-33 Trading Ledger | LED-004, LED-006 — [custody-and-ledger.md](../systems/custody-and-ledger.md) |
| Operating mode | SYS-12 Policy System | POL-008 — [policy-system.md](../systems/policy/policy-system.md) |
| Trading universe | SYS-05 with SYS-12 exclusions | OPP-009 — [opportunity-detection.md](../systems/opportunity-detection.md) |
| Allocation ranking | SYS-07 Global Capital Authority | CAP-017 — [capital-management.md](../systems/capital-management.md) |
| Regime state | SYS-04 Market Regime Engine | RGM-006 — [market-regime-engine.md](../systems/market-regime-engine.md) |
