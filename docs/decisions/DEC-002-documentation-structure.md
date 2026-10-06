# DEC-002 — Documentation structure derived from Handoff Part 1

- **Status:** ACCEPTED (delegated, 2026-09-30: accepted under the owner's instruction to resolve all open items; first recorded as PROPOSED)
- **Date:** 2026-09-30
- **Affects:** everything under `docs/`
- **Resolves:** CF-07
- **Later changes:** OQ-15 is answered: `docs/product/trading-policy.md` is not created; runtime policy lives only in the Policy System ([DEC-015](DEC-015-modes-canary-and-policy-governance.md)). Splitting documents waits on content, not on Part 2 ([DEC-024](DEC-024-part-2-reconciliation.md), Consequences). The reason given below for not creating `implementation/` no longer holds: the stack is decided ([DEC-009](DEC-009-technology-stack.md)), and on 2026-10-05 the owner approved the Stage 1 plan and authorized Stage 1 implementation ([DEC-038](DEC-038-stage-1-plan-approved.md)). The plan's decision D2 places code and its artifacts in `src/`, `tests/`, `contracts/`, and `config/examples/`, so `implementation/` is still not created. The text below is kept as written.

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

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **§99's folder target as given** (`systems/directional/`, `systems/market-data/`, `systems/exchanges/`, `systems/recovery/`, `ai/agents/`, `implementation/`): not followed for these folders. The reason for each is in "Deviations from the §99 target" above: §98 gives a file path, one document is enough for now, or implementation is not authorized. CF-07 recorded the clash between §98's files and §99's folders.
- **Creating every possible folder up front:** ruled out by handoff §00 item 5 and §99, and by constitution Rules 9–16 (Context).

## Consequences

- Folders will be added when Part 2 or later stages introduce new responsibilities (Rule 12). The file paths used now are expected to stay stable.
- `docs/product/trading-policy.md` from §98 is not created until OQ-15 is answered.
