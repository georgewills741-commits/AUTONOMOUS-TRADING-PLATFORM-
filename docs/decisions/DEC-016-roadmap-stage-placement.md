# DEC-016 — Roadmap stage sequence and placement

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Later changes:** the Performance Controller's core moves to DIRECTIONAL TRADING ([DEC-024](DEC-024-part-2-reconciliation.md), CF-16); its arbitrage tracking stays in ARBITRAGE.
- **Date:** 2026-09-30
- **Resolves:** CF-05, CF-06

## Decision

Stages run **sequentially** in §95 order: FOUNDATION → DATA FOUNDATION → CORE TRADING FOUNDATION → DIRECTIONAL TRADING → ARBITRAGE → AI INTELLIGENCE → OPERATIONALIZATION (RMP-002). No live trading happens before OPERATIONALIZATION's canary and live-operation items.

| Item | Stage | Reason |
|---|---|---|
| Policy System (SYS-12), structured and versioned | CORE TRADING FOUNDATION | The Risk Engine enforces user hard constraints (CF-06). The NL interface stays in AI INTELLIGENCE (POL-010) |
| Operating modes | CORE | Paper and live separation must exist before any strategy runs |
| Audit and event history (SYS-30) | CORE | Core systems produce the events it records |
| System Health (SYS-29) | CORE; hardened in OPERATIONALIZATION | Kill switches and safe mode are needed as soon as trading logic exists |
| Trading ledger (SYS-33) | CORE | Capital derives from it (CAP-019) |
| Reconciliation | CORE (core logic); OPERATIONALIZATION (hardening) | Resolves the §95 double listing |
| True Net-Profit Engine | CORE; ARBITRAGE adds transfer and multi-leg cost components | One engine (DUP-01) |
| Strategy management, backtesting, paper trading | DIRECTIONAL, shared; ARBITRAGE depends on them | Resolves "mapped to a narrower stage" |
| Performance Controller | ARBITRAGE, platform-wide | Applies to directional strategies before any live operation |
| Model Evaluation, structured AI output, calibration | AI INTELLIGENCE | Needed before any AI output is used |
| Numerical precision, security | Every stage | Cross-cutting |
| Custody (SYS-32) | None (FUTURE) | DEC-006 |

The [roadmap](../roadmap/roadmap.md) and the [system registry](../architecture/system-registry.md) are updated to match.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **CF-06, the §95 mapping as written:** only the natural-language policy interface is mapped, to AI INTELLIGENCE, and the structured Policy System has no stage. Not taken: the Risk Engine, in CORE TRADING FOUNDATION, enforces user hard constraints, so the Policy System is built there (CF-06's proposal).
- **CF-05, the rest of the §95 mapping as written,** with some items in two stages, some shared items in one trading stage, and some in no stage: not kept. The table above places each item and, where an item spans stages, says which part goes where. §95 itself says exact sequencing is finalized after dependency analysis (CF-05).
- **Parallel trading stages:** the order the builder PROPOSED when Part 1 was first documented (the roadmap and the dependency map at commit `b850eaa`): "the two trading stages can run in parallel, and AI INTELLIGENCE follows CORE". Not taken: stages run sequentially in §95's order (RMP-002). No reason is recorded.
