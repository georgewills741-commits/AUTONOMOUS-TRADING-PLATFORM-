# DEC-002 — Documentation structure derived from Handoff Part 1

- **Status:** ACCEPTED (delegated, 2026-09-30: accepted under the owner's instruction to resolve all open items; first recorded as PROPOSED)
- **Date:** 2026-09-30
- **Affects:** everything under `docs/`
- **Resolves:** CF-07

## Context

The handoff gives example canonical paths (§98) and a conceptual folder target (§99). It says not to create every folder blindly, and to derive the structure from the architecture (§00 item 5, §99). The constitution says the same (Rules 9–16).

## Decision

Create a directory only when it holds real content from Part 1, and follow §98 paths wherever §98 gives one:

| Directory | Why it exists now |
|---|---|
| `docs/product/` | Platform identity, objective, priorities (§01, §02, §82, §83), and operating modes (§31) |
| `docs/requirements/` | Requirement conventions and the requirement index (§00 item 10, §98) |
| `docs/architecture/` | Structural principles, system registry, dependency map, source-of-truth map, performance (§03, §04, §70, §92–§98) |
| `docs/systems/` | One specification per shared-infrastructure and trading system (§98 file paths) |
| `docs/systems/arbitrage/` | Three arbitrage documents (§98 names this folder) |
| `docs/systems/policy/` | Policy System and NL interface (§98 names this folder) |
| `docs/systems/strategy/` | Strategy management, backtesting, paper trading: three related documents |
| `docs/risk/` | Risk Engine (§98 names this folder) |
| `docs/ai/` | AI layer, output validation, model management, agents, memory (§98) |
| `docs/security/` | Security architecture (§89) |
| `docs/operations/` | Monitoring, system health, deployment and readiness (§74, §80, §81, §88, §90, §91) |
| `docs/roadmap/` | Stage classification and mapping (§95, §98) |
| `docs/decisions/` | Decision records (§98) |
| `docs/conflicts/` | Findings register (§99, constitution Rule 177) |
| `docs/open-questions/` | Open questions and technical concerns (§99, Rule 178) |
| `docs/traceability/` | Handoff coverage and verification records (§99, Rule 184) |
| `docs/handoffs/` | Original handoffs as HISTORICAL records (constitution Rule 27; not in §99; see DEC-004) |

## Deviations from the §99 target, and why

| §99 item | Not created | Reason |
|---|---|---|
| `systems/directional/` | single file `systems/directional-trading.md` | §98 gives that exact file path |
| `systems/market-data/`, `systems/exchanges/`, `systems/recovery/` | single files | One document each in Part 1; add a folder when content grows |
| `ai/agents/` | single file `ai/agents.md` | Six short agent definitions; split when Part 2 adds depth |
| `implementation/` | not created | Implementation is not authorized, and the technology stack is unknown (OQ-16, constitution Rule 104) |
| — | `docs/glossary.md` added | Needed for terminology normalization (constitution Rules 33, 59) |

## Consequences

- Folders will be added when Part 2 or later stages introduce new responsibilities (Rule 12). The file paths used now are expected to stay stable.
- `docs/product/trading-policy.md` from §98 is not created until OQ-15 is answered.
