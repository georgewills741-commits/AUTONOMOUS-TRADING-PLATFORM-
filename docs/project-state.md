# Project State

The single record of where this project currently stands (Constitution Rules 50, 172). Update it after every major piece of work. If it disagrees with the repository, the repository wins and this file gets corrected (Rule 52).

**Last updated:** 2026-09-30

## Current stage

**FOUNDATION — documentation initialization.** Handoff Part 1 is documented, and every open question and finding from it has been resolved. Part 2 has not been received.

| Gate | Status |
|---|---|
| Builder constitution | ADOPTED — [`builder/claude-code-builder-constitution.md`](builder/claude-code-builder-constitution.md) ([DEC-001](decisions/DEC-001-adopt-builder-constitution.md)) |
| Master handoff Part 1 (core platform features and systems) | RECEIVED and DOCUMENTED — [historical copy](handoffs/part-1-core-platform-features.md) · [coverage](traceability/handoff-coverage.md) · [verification](traceability/part-1-verification.md) |
| Part 1 open questions and findings (61) | **ALL RESOLVED** — [decision log](decisions/README.md) · [resolution verification](traceability/resolution-verification.md) |
| Technology stack | DECIDED — [technology stack](architecture/technology-stack.md) ([DEC-009](decisions/DEC-009-technology-stack.md)) |
| Master handoff Part 2 (detailed requirements, interfaces/contracts, dependency and stage mapping, verification architecture) | **NOT RECEIVED** |
| Complete documentation review (handoff §101) | NOT STARTED — after Part 2 |
| Human approval to implement | **NOT GIVEN** — required after the documentation review (handoff §101; constitution Part XXIII) |
| Product implementation | **NOT STARTED, NOT AUTHORIZED.** Nothing is deployed, and live trading is not active (handoff §00 items 22–25) |

## Current objective

Wait for Handoff Part 2 and fold it into the documentation. Then re-check every decision (DEC-006 to DEC-018) against it, recording any conflict as a new finding rather than silently changing a decision.

## Completed work

- **Constitution:** adopted and persisted; `CLAUDE.md` loads it every session.
- **Part 1 processing:**
  - Original handoff kept verbatim (HISTORICAL).
  - 33 systems registered.
  - 228 handoff requirements classified and placed in their owning specifications.
  - Dependency map, roadmap, glossary, source-of-truth map.
  - 61 findings and questions recorded.
  - Verified in three passes.
- **Resolution round (owner instruction: resolve every open item before Part 2):**
  - **Owner decisions:** single operator with no custody (DEC-006); spot, perpetual futures, and margin (DEC-007); venues Binance, OKX, Coinbase, Bybit, KuCoin, and extensible (DEC-008).
  - **Owner-delegated:** technology stack — Python 3.12 core, Rust only for measured hot paths, PostgreSQL + TimescaleDB, Parquet/DuckDB, NATS, CCXT (DEC-009).
  - **Decided under the owner's instruction:** DEC-010 to DEC-018 — pre-trade flow, ownership of every overlapping responsibility, safety architecture, AI organization (five agents plus three deterministic services), net-profit formula and uncertainty margin, modes/canary/policy governance, stage placement, reporting and performance targets, initial directional research candidates.
  - **Applied to the specifications:** 109 new requirements that cite their decision record. Five handoff requirements were reclassified (EXA-002, AGT-001, and LED-002 to DEPRECATED / REPLACED; CUS-001 and CUS-002 to FUTURE); no handoff requirement text was changed or removed.
  - All 10 conflicts, 22 duplicate responsibilities, 23 open questions, and 6 technical concerns are marked RESOLVED, with links, in the registers.

## In-progress work

None.

## Blockers

| Problem | Impact | Required resolution |
|---|---|---|
| Handoff Part 2 not received | Interfaces, contracts, per-stage entry/exit criteria, and verification architecture cannot be completed; the documentation review (§101) cannot start | Project owner supplies Part 2 |

## Open questions

None. All 23 open questions and 6 technical concerns are resolved ([register](open-questions/register.md)), and so are all 32 findings ([register](conflicts/register.md)).

## Decisions worth the owner's review

All decisions made under delegation can be overridden with a new decision record. These have the most operational effect:

- **Rebalancing transfers need your confirmation by default.** Trading keys never have withdrawal permission; automated transfers need an important policy change and a separate whitelisted key (CAP-022, SEC-003).
- **No automatic position closing in EMERGENCY** unless policy enables it (HLT-008).
- **No automatic resume after a restart** unless you enable it (REC-009).
- **Canary defaults:** 5% of target allocation, at least 14 days and 50 trades (STR-011).
- **Uncertainty margin confidence multiplier `k`:** operator-configured (TNP-019).
- **Latency design targets** of 50 ms / 500 ms (PERF-007), to be replaced by measurements.

## Recent decisions

[Decision log](decisions/README.md): DEC-001 to DEC-005 accepted (first recorded as proposed); DEC-006 to DEC-018 added on 2026-09-30.

## Recent changes

- 2026-09-30: adopted the builder constitution; created `CLAUDE.md` and this file.
- 2026-09-30: processed Handoff Part 1 into `docs/`.
- 2026-09-30: resolved all open items; added DEC-006 to DEC-018, [technology stack](architecture/technology-stack.md), and 109 decision-sourced requirements; updated registers, registry, roadmap, dependency map, glossary, and source-of-truth map. No code, configuration, or infrastructure created.

## Next approved step

Receive **Handoff Part 2**, then integrate it (constitution handoff loop: read, extract, classify, map, organize, reconcile, persist, verify, report), re-check all decisions against it, and stop. After that comes the complete documentation review and human approval (§101). Only explicit approval such as "Begin Stage 1" authorizes implementation (constitution Rules 134–135).
