# Project State

The single record of where this project currently stands (Constitution Rules 50, 172). Update it after every major piece of work. If it disagrees with the repository, the repository wins and this file gets corrected (Rule 52).

**Last updated:** 2026-09-30

## Current stage

**FOUNDATION — documentation initialization.** Handoff Part 1 is documented and its open items are resolved. The owner's company-grade autonomous operating model ([OC-1](handoffs/owner-correction-01-autonomous-operating-defaults.md)) is applied. Three conflicts it raised await owner review. Part 2 has not been received.

| Gate | Status |
|---|---|
| Builder constitution | ADOPTED — [`builder/claude-code-builder-constitution.md`](builder/claude-code-builder-constitution.md) ([DEC-001](decisions/DEC-001-adopt-builder-constitution.md)) |
| Master handoff Part 1 (core platform features and systems) | RECEIVED and DOCUMENTED — [historical copy](handoffs/part-1-core-platform-features.md) · [coverage](traceability/handoff-coverage.md) · [verification](traceability/part-1-verification.md) |
| Part 1 open questions and findings (61) | **ALL RESOLVED** — [decision log](decisions/README.md) · [resolution verification](traceability/resolution-verification.md) |
| Technology stack | DECIDED — [technology stack](architecture/technology-stack.md) ([DEC-009](decisions/DEC-009-technology-stack.md)) |
| Owner correction 1: company-grade autonomous operating model | APPLIED — [DEC-019](decisions/DEC-019-company-grade-autonomous-operating-model.md), [DEC-020](decisions/DEC-020-value-classification.md) · [verification](traceability/owner-correction-01-verification.md) |
| Conflicts raised by the correction (CF-11 to CF-13) | **OPEN — awaiting owner review** ([findings register](conflicts/register.md)) |
| Master handoff Part 2 (detailed requirements, interfaces/contracts, dependency and stage mapping, verification architecture) | **NOT RECEIVED** |
| Complete documentation review (handoff §101) | NOT STARTED — after Part 2 |
| Human approval to implement | **NOT GIVEN** — required after the documentation review (handoff §101; constitution Part XXIII) |
| Product implementation | **NOT STARTED, NOT AUTHORIZED.** Nothing is deployed, and live trading is not active (handoff §00 items 22–25) |

## Current objective

Get the owner's decisions on CF-11 to CF-13, and receive Handoff Part 2. Fold Part 2 into the documentation, then re-check every decision (DEC-006 to DEC-020) against it, recording any conflict as a new finding rather than silently changing a decision.

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
- **Owner correction 1 (company-grade autonomous operating model):**
  - Directive kept word for word (HISTORICAL).
  - DEC-019: autonomous, policy-bounded rebalancing; graduated safety levels; automatic 24/7 recovery with an execution lease; readiness-driven canary; measured performance.
  - DEC-020: value classification, with a [values register](requirements/values-register.md) of 23 entries.
  - 41 new requirements. Nine earlier requirements marked DEPRECATED / REPLACED (CAP-022, SEC-003, HLT-007, HLT-008, HLT-009, REC-009, STR-011, MODE-004, PERF-007), class field only, wording kept. Ten TEC requirements reclassified to IMPLEMENTATION CHOICE.
  - The 5% / 14 days / 50 trades canary values are withdrawn; 50 ms / 500 ms are kept only as DESIGN TARGETS.

## In-progress work

None.

## Blockers

| Problem | Impact | Required resolution |
|---|---|---|
| Handoff Part 2 not received | Interfaces, contracts, per-stage entry/exit criteria, and verification architecture cannot be completed; the documentation review (§101) cannot start | Project owner supplies Part 2 |
| CF-11 to CF-13 open | Kill-switch reset rules, recovery ordering wording, and whether the lifecycle APPROVAL stage is human cannot be finalized | Owner decides; proposed resolutions are in the [findings register](conflicts/register.md) |

## Open questions

No open questions. Three open conflicts from the owner's correction:

- **CF-11 — kill-switch reset.** RSK-009 (operator-only reset) stays in force. Proposed: reset by cause — automatic reset for recoverable, measurable causes; operator reset for security, unknown financial state, and loss-based triggers.
- **CF-12 — recovery ordering.** Low impact. Proposed: no loaded state is relied on before the database is verified; internal checks are re-validated after reconciliation.
- **CF-13 — lifecycle APPROVAL stage.** Proposed: deterministic canary authorization by default, which the operator can make human-controlled in policy.

## Operating model now in force (replaces the earlier "defaults")

- **Rebalancing:** autonomous when policy-authorized and economically justified (expected benefit > transfer + risk + opportunity cost). Bounded by policy controls, using a separate transfer credential restricted to your own venue accounts. Never invents authorization (CAP-023 to CAP-025, SEC-006, SEC-007).
- **Emergencies:** graduated safety levels NORMAL → CAUTION → RESTRICTED → SAFE MODE → EMERGENCY → CRITICAL RECOVERY. Positions are handled per policy (hold, reduce, hedge, close, …), deterministically, with no AI, and idempotently (RSK-015 to RSK-020).
- **Restart:** automatic restart, reconciliation, and health checks, then automatic resumption when safe. Restricted operation when partly safe, SAFE MODE when uncertain. One active instance, enforced by an execution lease (REC-010 to REC-013).
- **Canary:** automatic when every readiness gate passes. Allocation is dynamic within policy limits, scales gradually, and stops and rolls back automatically (STR-013 to STR-018).
- **Performance:** measured, path-specific budgets and percentiles, with hard limits vs soft targets vs observed values. Latency enters the opportunity economics, and degradation is handled automatically (PERF-008 to PERF-012, TNP-023).
- **Before any of these can run autonomously:** you set its policy boundaries (POL-011; the unset values in the [values register](requirements/values-register.md)). An unset boundary means that action stays outside authorization.

## Recent decisions

[Decision log](decisions/README.md): DEC-001 to DEC-005 accepted (first recorded as proposed); DEC-006 to DEC-018 added on 2026-09-30; DEC-019 and DEC-020 (owner correction) added the same day.

## Recent changes

- 2026-09-30: adopted the builder constitution; created `CLAUDE.md` and this file.
- 2026-09-30: processed Handoff Part 1 into `docs/`.
- 2026-09-30: resolved all open items; added DEC-006 to DEC-018, [technology stack](architecture/technology-stack.md), and 109 decision-sourced requirements; updated registers, registry, roadmap, dependency map, glossary, and source-of-truth map. No code, configuration, or infrastructure created.
- 2026-09-30: applied owner correction 1 (DEC-019, DEC-020): 41 new requirements, 9 superseded, values register, CF-11 to CF-13 raised. No code, configuration, or infrastructure created.

## Next approved step

Owner decides **CF-11 to CF-13**, and supplies **Handoff Part 2**. Then integrate Part 2 (constitution handoff loop: read, extract, classify, map, organize, reconcile, persist, verify, report), re-check all decisions against it, and stop. After that comes the complete documentation review and human approval (§101). Only explicit approval such as "Begin Stage 1" authorizes implementation (constitution Rules 134–135).
