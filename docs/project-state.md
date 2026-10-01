# Project State

The single record of where this project currently stands (Constitution Rules 50, 172). Update it after every major piece of work. If it disagrees with the repository, the repository wins and this file gets corrected (Rule 52).

**Last updated:** 2026-10-01

## Current stage

**FOUNDATION — documentation initialization.**

- Handoff Parts 1, 2, and 3 are documented and reconciled into one knowledge base ([DEC-024](decisions/DEC-024-part-2-reconciliation.md), [DEC-031](decisions/DEC-031-part-3-reconciliation.md)).
- The owner's company-grade autonomous operating model and the owner's decisions on CF-11 to CF-13 are applied.
- The owner answered every Part 2 finding (DEC-026 to DEC-030).
- The Part 3 reconciliation **awaits human review** (P3§541 items 29–30). Items for the owner: confirm CF-17 and CF-18, answer OQ-27, accept or change TC-08's recommendation, and check two builder readings (DUP-34, DUP-35). TC-09 is decided when OPERATIONALIZATION is planned.
- The owner's checkpoint and three-stage verification rule is adopted ([DEC-032](decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)).
- The owner's master execution constitution and directive on verification and platform independence (2026-10-01) are adopted ([DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md), [DEC-034](decisions/DEC-034-verification-and-platform-independence.md)). CF-19 from them is for the owner.
- Implementation is not authorized.

| Gate | Status |
|---|---|
| Builder constitution | ADOPTED — [`builder/claude-code-builder-constitution.md`](builder/claude-code-builder-constitution.md) ([DEC-001](decisions/DEC-001-adopt-builder-constitution.md)) |
| Master handoff Part 1 (core platform features and systems) | RECEIVED and DOCUMENTED — [historical copy](handoffs/part-1-core-platform-features.md) · [coverage](traceability/handoff-coverage.md) · [verification](traceability/part-1-verification.md) |
| Part 1 open questions and findings (61) | ALL RESOLVED — [decision log](decisions/README.md) · [resolution verification](traceability/resolution-verification.md) |
| Technology stack | DECIDED — [technology stack](architecture/technology-stack.md) ([DEC-009](decisions/DEC-009-technology-stack.md)) |
| Owner correction 1: company-grade autonomous operating model | APPLIED — [DEC-019](decisions/DEC-019-company-grade-autonomous-operating-model.md), [DEC-020](decisions/DEC-020-value-classification.md) · [verification](traceability/owner-correction-01-verification.md) |
| Conflicts raised by the correction (CF-11 to CF-13) | DECIDED by the owner — [DEC-021](decisions/DEC-021-kill-switch-recovery.md), [DEC-022](decisions/DEC-022-restart-recovery-sequence.md), [DEC-023](decisions/DEC-023-autonomous-canary-approval.md) · [answers](handoffs/owner-decisions-02-cf-11-to-cf-13.md) · [verification](traceability/owner-decisions-02-verification.md) |
| Master handoff Part 2 (consolidated additional systems, paper operation, readiness, arbitrage, deployment portability) | RECEIVED, DOCUMENTED, and RECONCILED — [historical copy](handoffs/part-2-consolidated-additional-systems.md) · [reconciliation](traceability/part-2-reconciliation.md) · [verification and documentation audit](traceability/part-2-verification.md) · [DEC-024](decisions/DEC-024-part-2-reconciliation.md) |
| Part 2 findings (CF-14, OQ-24 to OQ-26, TC-07, and four items to confirm) | DECIDED by the owner — [DEC-026](decisions/DEC-026-safety-floor-and-layered-control.md) to [DEC-030](decisions/DEC-030-high-availability-and-single-active-copy.md) · [answers](handoffs/owner-decisions-03-part-2-findings.md) · [verification](traceability/owner-decisions-03-verification.md) |
| Owner's checkpoint, version-control, and three-stage verification rule | ADOPTED — [`builder/checkpoint-and-verification-rule.md`](builder/checkpoint-and-verification-rule.md) ([DEC-032](decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)) |
| Repository integrity verification (owner request, 2026-10-01) | DONE — [record](traceability/integrity-verification-2026-10-01.md) |
| Master execution, consistency, verification and continuity constitution | ADOPTED — [`builder/master-execution-constitution.md`](builder/master-execution-constitution.md) ([DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md)) |
| Owner's directive on three-level verification and platform independence | ADOPTED — [`builder/verification-and-platform-independence-directive.md`](builder/verification-and-platform-independence-directive.md) ([DEC-034](decisions/DEC-034-verification-and-platform-independence.md)) |
| Master handoff Part 3 (autonomy, capital scaling, system rules, extensibility, 24/7 operations, rebalancing, readiness) | RECEIVED, DOCUMENTED, and RECONCILED — [historical copy](handoffs/part-3-consolidated-autonomy-capital-scaling.md) · [reconciliation](traceability/part-3-reconciliation.md) · [verification and documentation audit](traceability/part-3-verification.md) · [DEC-031](decisions/DEC-031-part-3-reconciliation.md) |
| Human review of the Part 3 reconciliation (P3§541 items 29–30), with CF-17, CF-18, OQ-27, TC-08, and the DUP-34, DUP-35 readings; and CF-19 | **AWAITING THE OWNER — next step** |
| Complete documentation review (handoff §101; P2§329) | NOT STARTED — after the Part 3 review |
| Human approval to implement | **NOT GIVEN** — required after the documentation review (handoff §101; P2§330; P3§541; constitution Part XXIII) |
| Product implementation | **NOT STARTED, NOT AUTHORIZED.** Nothing is deployed, and live trading is not active (handoff §00 items 22–25; P2§330; Part 3 header) |

## Current objective

The owner reviews the Part 3 reconciliation (P3§541 item 29) and answers the items listed under "Open questions" below, CF-19 included (TC-09 is recorded now and decided when OPERATIONALIZATION is planned). Then the complete documentation review (§101, P2§329) and the plan for Stage 1 (FOUNDATION) with its objective, scope, tests, and completion criteria. After that the owner decides whether to approve implementation of Stage 1.

## Continuation contract

What the next session needs before it does anything (master execution constitution §03, §04, §87; DEC-033). Updated at every checkpoint and before a session ends. If this contract and the repository disagree, stop and reconcile first (§05).

| Field | Now |
|---|---|
| Current stage and substage | FOUNDATION — documentation initialization; the governance texts of 2026-10-01 are adopted; waiting for the owner's review |
| Current task | None in progress. The next task is the owner's (see "Next approved step") |
| Completed | See "Completed work" and the checkpoint log below |
| In progress, possibly partial | Nothing |
| Blocked | The documentation review and Stage 1 planning wait for the owner's Part 3 review and answers ("Blockers") |
| Failed verification | None open |
| Pending verification | None |
| Verified | Every checkpoint in the checkpoint log, by its verification record |
| Not verified | Platform behavior: nothing is implemented |
| Latest verified commit | The last row of the checkpoint log (a commit cannot record its own hash; the next checkpoint fills it in) |
| Uncommitted changes | None at a checkpoint. Changes found at the start of a session are unexplained until inspected (§07) |
| Repository integrity | Clean at the last checkpoint ([integrity verification](traceability/integrity-verification-2026-10-01.md); the record of each later checkpoint) |
| Known risks | Owner answers still due (CF-17, CF-18, CF-19, OQ-27, TC-08) may change requirements; nothing is built on them. The tools' check versions are not pinned until Stage 1 ([tools README](../tools/docs/README.md)) |
| Next safe action | The owner's review ("Next approved step", item 1). The builder makes no further change until then, unless the owner asks |
| Do not change | The verbatim texts under `docs/handoffs/` and `docs/builder/` (only a status banner may change, by decision); any requirement's text or class without a decision record; the generated parts of generated files by hand |
| Do not implement yet | Anything. Implementation is not authorized (handoff §101; constitution Rules 134–135); FUTURE and PROPOSED items stay unbuilt even then |

## Owner decisions on the Part 2 findings (2026-09-30)

All answered ([owner decisions 3](handoffs/owner-decisions-03-part-2-findings.md)):

| Item | Owner's decision | Record |
|---|---|---|
| CF-14: top of the rules | An immutable **safety floor**: nobody (AI, strategy, policy, administrator, automatic process) can bypass the safety invariants; changing one needs a formal human-controlled change. Everything operational adapts automatically inside that envelope, recovers by itself, and never deadlocks the healthy parts. RSK-004 unchanged | [DEC-026](decisions/DEC-026-safety-floor-and-layered-control.md): RSK-034 to RSK-039, PLT-021 |
| OQ-24: global platform controller | Existing parts working together; no new system | [DEC-027](decisions/DEC-027-part-2-open-questions.md): ARCH-035 |
| OQ-25: where PAPER mode runs | The separate paper environment, no real exchange keys | DEC-027: PAP-013 |
| OQ-26: adaptive execution | A FUTURE feature, not built until approved | DEC-027: EXE-011 |
| ARCH-034: command language | Kept as an idea | DEC-027 |
| DEC-024's five choices | All kept | DEC-027 |
| CAP-028: capital categories | Added (directional capital, emergency reserve, per-exchange reserve), policy-set and dynamic, rebalanced automatically, with progressive capability activation | [DEC-028](decisions/DEC-028-capital-buckets-and-progressive-activation.md): CAP-029 to CAP-033, RDY-008 |
| OPS-009: infrastructure as code | Mandatory for production | [DEC-029](decisions/DEC-029-infrastructure-as-code.md): OPS-014 to OPS-017 |
| TC-07: one copy during migration | Freeze the old copy, then new exchange keys for the new location, old ones deleted | [DEC-030](decisions/DEC-030-high-availability-and-single-active-copy.md): MIG-029, MIG-030 |
| REC-021: high availability | Planned now: a standby copy takes over automatically after checking and reconciling state | DEC-030: REC-021, REC-023, REC-024 |

Builder readings you may want to check, all stated in the decision records:

- The safety floor is RSK-034 together with the existing system safety rules (RSK-010). HARD LIMIT values are part of it.
- Automatic adjustments happen inside the bounds you set in policy. Widening a bound or an authorization still needs you (POL-005).
- The "Capital Allocation & Treasury Engine" is the existing Global Capital Authority. Capability eligibility is decided by the Readiness System.
- The standby's "explicit activation" is acquiring the execution lease under a policy authorization, not a human action.
- Where a venue cannot create or revoke keys through its API, the migration's key swap is an operator step.

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
- **Owner decisions 2 (CF-11 to CF-13):**
  - Answers kept word for word.
  - DEC-021: cause-based, risk-aware kill-switch recovery.
  - DEC-022: staged restart recovery; persisted state untrusted until reconciled.
  - DEC-023: autonomous approval by the Governance and Readiness Engine.
  - 16 new requirements. RSK-009, REC-007, and REC-011 replaced (class field only); their activation, AI-limit, and restricted-operation clauses carried forward.
  - Values register now has 29 entries.
- **Handoff Part 2 (2026-09-30):**
  - Kept word for word (HISTORICAL; round-trip verified). Every section §1 to §350 is traced.
  - 194 new requirements: 185 from Part 2 sections, 9 from DEC-024. No existing requirement changed.
  - New specifications:
    - [Readiness System](systems/readiness-system.md) (SYS-34);
    - [Daily System Intelligence Dashboard and Report](operations/daily-system-intelligence.md);
    - [Incident Management](operations/incident-management.md);
    - [Hosting, Backup, and Migration](operations/hosting-and-migration.md);
    - [Verification Architecture](architecture/verification-architecture.md).
  - Extended: the [paper trading](systems/strategy/paper-trading.md) architecture and the [arbitrage](systems/arbitrage/arbitrage-intelligence.md) architecture.
  - Registers:
    - findings CF-14 to CF-16 and DUP-23 to DUP-31;
    - open questions OQ-24 to OQ-26 and TC-07;
    - values V-30 to V-33.
  - Updated: roadmap RMP-003 to RMP-011; dependency map D-54 to D-63; source-of-truth map; glossary.
  - Verified in three passes; defects found were fixed and re-checked.
  - The documentation generator and checker now live in the repository: [`tools/docs/`](../tools/docs/README.md) ([DEC-025](decisions/DEC-025-documentation-tooling-in-repository.md)).
- **Owner decisions 3 (Part 2 findings, 2026-09-30):**
  - Answers kept word for word.
  - DEC-026 to DEC-030: 24 new requirements.
  - Class-only changes: CAP-028 and OPS-009 replaced; REC-021 reclassified from FUTURE to CONFIRMED REQUIREMENT. No requirement wording changed.
  - Values register now has 35 entries.

- **Handoff Part 3 and the checkpoint rule (2026-09-30):**
  - Both kept word for word: Part 3 as HISTORICAL (round-trip verified, sections §351 to §550), the rule as an ACTIVE builder rule loaded by `CLAUDE.md` (DEC-032).
  - Every section §351 to §550 is traced in the [Part 3 reconciliation](traceability/part-3-reconciliation.md).
  - 111 new requirements: 109 from Part 3 sections, 2 from DEC-031 (RDY-026, RSK-048). New prefix GOV. No existing requirement changed, was reclassified, or was removed (checked with `tools/docs/compare_requirements.py`).
  - New documents: [Architecture governance](architecture/architecture-governance.md) (GOV-001 to GOV-020); [System Rules Register](requirements/system-rules-register.md) (SR-01 to SR-45); [Reliability and recovery model](operations/reliability-and-recovery-model.md) (index). The [Readiness System](systems/readiness-system.md) now documents the capability and readiness model; [Deployment and operational readiness](operations/deployment-and-operational-readiness.md) the production-readiness model.
  - Registers: CF-17, CF-18, DUP-32 to DUP-38 (resolved by DEC-031; CF-17 and CF-18 await confirmation); OQ-27, TC-08, TC-09 (open); values V-36 to V-39.
  - Updated: roadmap (RMP-012 and "Part 3 additions by stage"), dependency map (D-66 to D-71), system registry, source-of-truth map, glossary, indexes. Six stale notes from earlier rounds corrected.
  - Tooling: the checker reads P3 sources and checks the System Rules Register; `compare_requirements.py` added.
  - Verified in three gates: [Part 3 verification record](traceability/part-3-verification.md). Gate 3, by an independent reviewer, failed first (2 blocking, 14 non-blocking defects, all fixed, including two missing requirements now PERF-022 and AIL-021) and passed on an independent re-run.
- **Repository integrity verification (2026-10-01, owner request):**
  - Every piece of work from the earlier rounds is in the repository; the branch change set was reviewed area by area; no secrets, stray, binary, or duplicate files.
  - Two tooling defects found and fixed: formatting (`ruff format`) and type errors (`mypy`) in `tools/docs/`, with no change in behavior. Generated Python bytecode is now excluded by `.gitignore`.
  - Record: [integrity verification](traceability/integrity-verification-2026-10-01.md).
- **Master execution constitution and owner directive (2026-10-01):**
  - Both kept word for word as ACTIVE builder texts (round-trip verified), loaded by `CLAUDE.md` with the two earlier ones. Where the four differ, the stricter applies; they share one three-gate procedure (DEC-033, DUP-39).
  - 8 new requirements: PLT-029, OPS-021, GOV-021 to GOV-023 (DEC-034: the platform runs without Claude Code; continuous lifecycle; future changes are upgrades under the same governance); ARCH-041, ARCH-042, PERF-023 (DEC-033: idempotent financial operations; UNKNOWN is never SUCCESS; no unsafe fast path). No existing requirement changed.
  - The constitution's other 58 platform-facing sections map onto existing requirements (DEC-033's table). System rules SR-46, SR-47, and ARCH-042 in SR-09.
  - New: this continuation contract; the verification-record format ([traceability README](traceability/README.md)); glossary aliases for the constitution's authority names; tooling that makes verification repeatable: a check that the preserved verbatim texts never change, an orphaned-document check, and a self-test of the tools ([tools README](../tools/docs/README.md)). Findings CF-19 (feature lifecycle, open for the owner), DUP-39 (resolved), TC-10 (shared state names, open until the state machines are specified).

## In-progress work

None. The Part 3 reconciliation is complete and awaits human review.

## Blockers

| Problem | Impact | Required resolution |
|---|---|---|
| Human review of the Part 3 reconciliation (P3§541 items 29–30) | Normal implementation cannot begin, as intended | The owner reviews DEC-031 and answers the items below |

## Open questions

For the owner ([DEC-031](decisions/DEC-031-part-3-reconciliation.md), "Left for the owner"; CF-19 and TC-10 from [DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md)):

| Item | Question | Where |
|---|---|---|
| CF-17 | Confirm rule precedence: the safety floor first (your DEC-026 decision), then user hard constraints, security, risk, capital, execution, strategy, market conditions, AI (RSK-048). In particular, security controls outside the floor (transfer restrictions, AI least privilege) then rank below your hard policy: is that what you want? | [Findings register](conflicts/register.md) |
| CF-18 | Confirm: capital growth raises limits or authorized capital only where your policy already authorizes that scaling and readiness validates it; otherwise it is a policy change needing you | [Findings register](conflicts/register.md) |
| OQ-27 | Is a separate Part 4 coming? | [Open-question register](open-questions/register.md) |
| TC-08 | Older decision records mostly lack "Alternatives": add them only when a record is next amended and only where they can be sourced | [Open-question register](open-questions/register.md) |
| Readings | Check the mapping of the rebalancing decisions (DUP-34) and of Part 3's emergency state names (DUP-35) | [Findings register](conflicts/register.md) |
| CF-19 | Which feature lifecycle is canonical: the master execution constitution's (§107: IDEA … RETIRED, "must") or Part 3's proposed statuses (GOV-018)? The builder recommends §107's, with Part 3's names mapped onto it | [Findings register](conflicts/register.md) |
| TC-10 | Shared state names (SUSPENDED, DEGRADED, ACTIVE, and SAFE MODE as Part 1 listed it) get one meaning each when the state machines are specified; no answer needed now | [Open-question register](open-questions/register.md) |
| TC-09 | How a standby gets trading keys for automatic takeover without being able to trade before it holds the lease; decided when OPERATIONALIZATION is planned | [Open-question register](open-questions/register.md) |

What stays unapproved by design (proposals, future items) is shown in the [registry](requirements/registry.md)'s Approval column.

## Operating model now in force (replaces the earlier "defaults")

- **Rebalancing:** autonomous when policy-authorized and economically justified (expected benefit > transfer + risk + opportunity cost). Bounded by policy controls, using a separate transfer credential restricted to your own venue accounts. Never invents authorization (CAP-023 to CAP-025, SEC-006, SEC-007).
- **Emergencies:** graduated safety levels NORMAL → CAUTION → RESTRICTED → SAFE MODE → EMERGENCY → CRITICAL RECOVERY. Positions are handled per policy (hold, reduce, hedge, close, …), deterministically, with no AI, and idempotently (RSK-015 to RSK-020).
- **Restart:** automatic restart. Persisted state is treated as untrusted until reconciled against the exchanges, through the owner's staged sequence (database, schema, configuration, connectivity, balances, positions, orders, reservations, transfers, risk, strategy, data freshness, execution state, safety checks). Resumption is automatic when verified, restricted when partly verified, and NO-TRADE / SAFE MODE with escalation when uncertain. Recovery is idempotent and one active instance is enforced by an execution lease (REC-010 to REC-018).
- **Kill switches:** transient infrastructure trips (exchange/API instability, connectivity, stale data, rate limits, temporary slowness) recover automatically and progressively once cleared and verified. Security, unknown financial state, abnormal losses, data integrity, suspected duplicates, reconciliation failures, custody issues, repeated abnormal behavior, and anything uncertain stay latched until you authorize a reset. Repeated trips escalate to you (RSK-021 to RSK-025).
- **Canary:** the Governance and Readiness Engine approves automatically when every mandatory gate passes. You are asked only for deployments policy marks as human-controlled (e.g. a brand-new strategy class). Nobody — AI or human — can bypass the gates. Allocation is dynamic, scales gradually, and stops and rolls back automatically (STR-013 to STR-022).
- **Performance:** measured, path-specific budgets and percentiles, with hard limits vs soft targets vs observed values. Latency enters the opportunity economics, and degradation is handled automatically (PERF-008 to PERF-012, TNP-023).
- **Before any of these can run autonomously:** you set its policy boundaries (POL-011; the unset values in the [values register](requirements/values-register.md)). An unset boundary means that action stays outside authorization.

**Also from Part 2:**

- **Deterministic first.** AI provides intelligence and deterministic infrastructure provides authority (PLT-016, ARCH-019 to ARCH-022).
- **Paper and readiness.** Paper trading is a continuous evidence source (PAP-004 to PAP-012). Progression is decided by one Readiness System, never by a single number (RDY-001 to RDY-007).
- **Hosting.** The same platform runs locally or on a server, with migration only through a formal, reconciled process (MIG-001 to MIG-028).
- **Canary.** Canary is a production stage (OPS-013).

**From your answers on the Part 2 findings:**

- **Safety floor.** Immutable safety invariants that nothing and nobody can bypass. Inside them, the platform adapts limits, allocation, and thresholds automatically, recovers by itself, and isolates problems instead of stopping everything (RSK-034 to RSK-039).
- **Capital.** Directional, emergency, and per-exchange buckets, sized dynamically and rebalanced automatically. Capital-intensive features switch on only as capital and proven safety allow (CAP-029 to CAP-033).
- **Infrastructure.** All production infrastructure is kept as code and rebuildable without you (OPS-014 to OPS-017).
- **High availability.** A standby takes over automatically after reconciling (REC-023). Only one copy ever trades, and a migration swaps exchange keys (MIG-029).

**From Part 3 (awaiting your review):**

- **Capability scales with the account, not with capital alone.** Small accounts are first-class; capabilities unlock automatically when economics, liquidity, risk, readiness, and policy allow, never because a balance crossed a fixed number; growth never raises exposure by itself (RDY-009 to RDY-026, CAP-034, PLT-023).
- **Search aggressively, act conservatively.** Broad, continuous discovery; a detected opportunity is only a candidate (PLT-022, OPP-017 to OPP-020).
- **Rebalancing** decides among NO ACTION, now, later, partial, pre-position, wait, or emergency, without churn, always through the capital authority (CAP-037 to CAP-042).
- **System rules** are indexed with owner, enforcement point, and violation handling in the [System Rules Register](requirements/system-rules-register.md).
- **Restart is not resume;** failures are isolated to the service that failed (REC-025, REC-026).
- **New features** pass the governance gate before approval (GOV-001 to GOV-020).

## Recent decisions

[Decision log](decisions/README.md):

- DEC-001 to DEC-005 accepted (first recorded as proposed).
- DEC-006 to DEC-018 added on 2026-09-30.
- DEC-019 and DEC-020 (owner correction) and DEC-021 to DEC-023 (owner decisions on CF-11 to CF-13) added the same day.
- DEC-024 (Part 2 reconciliation) and DEC-025 (documentation tooling in the repository) added the same day.
- DEC-026 to DEC-030 (owner decisions on the Part 2 findings) added the same day. DEC-024 confirmed by the owner.
- DEC-031 (Part 3 reconciliation; awaiting review) and DEC-032 (the owner's checkpoint and verification rule) added the same day.
- DEC-033 (master execution constitution) and DEC-034 (owner's directive on verification and platform independence) added on 2026-10-01.

## Recent changes

- 2026-09-30: adopted the builder constitution; created `CLAUDE.md` and this file.
- 2026-09-30: processed Handoff Part 1 into `docs/`.
- 2026-09-30: resolved all open items; added DEC-006 to DEC-018, [technology stack](architecture/technology-stack.md), and 109 decision-sourced requirements; updated registers, registry, roadmap, dependency map, glossary, and source-of-truth map. No code, configuration, or infrastructure created.
- 2026-09-30: applied owner correction 1 (DEC-019, DEC-020): 41 new requirements, 9 superseded, values register, CF-11 to CF-13 raised. No code, configuration, or infrastructure created.
- 2026-09-30: applied owner decisions on CF-11 to CF-13 (DEC-021 to DEC-023): 16 new requirements, 3 superseded. No code, configuration, or infrastructure created.
- 2026-09-30: integrated Handoff Part 2 (DEC-024, DEC-025): 194 new requirements, SYS-34, five new specifications, findings CF-14 to CF-16, DUP-23 to DUP-31, OQ-24 to OQ-26, TC-07. No existing requirement changed. No platform code, configuration, or infrastructure created; the only code is the documentation checker in `tools/docs/`.
- 2026-09-30: applied owner decisions 3 on the Part 2 findings (DEC-026 to DEC-030): 24 new requirements; CAP-028 and OPS-009 replaced; REC-021 reclassified. No code, configuration, or infrastructure created.
- 2026-09-30: integrated Handoff Part 3 (DEC-031) and adopted the checkpoint and verification rule (DEC-032): 111 new requirements, GOV set, System Rules Register, reliability and production-readiness models, findings CF-17, CF-18, DUP-32 to DUP-38, OQ-27, TC-08, TC-09. No existing requirement changed. No platform code, configuration, or infrastructure created.
- 2026-10-01: repository integrity verification at the owner's request: tooling lint and type fixes, `.gitignore` for generated bytecode, code checks documented in the tools README. No requirement or decision changed.
- 2026-10-01: adopted the master execution constitution and the owner's directive (DEC-033, DEC-034): 8 new requirements, SR-46, SR-47, CF-19, DUP-39, TC-10, continuation contract, verification-record format. No existing requirement changed. No platform code, configuration, or infrastructure created.

## Next approved step

1. The owner's review of the Part 3 reconciliation and answers to CF-17, CF-18, CF-19, OQ-27, TC-08, and the DUP-34, DUP-35 readings (P3§541 items 29–30). TC-09 is decided when OPERATIONALIZATION is planned.
2. The complete documentation review (§101, P2§329): read the whole documentation set as one, looking for gaps, contradictions, and anything not ready for Stage 1.
3. Plan Stage 1 (FOUNDATION) with its objective, scope, tests, verification, and completion criteria (constitution Rule 140).
4. Only explicit approval such as "Begin Stage 1" authorizes implementation (constitution Rules 134–135). Approval to implement does not approve later architecture changes (Rule 136).

## Memory check (constitution Rule 175)

A new session can reconstruct the project from the repository:

- this file for the state, starting with its continuation contract;
- [`docs/README.md`](README.md) for every document;
- the [registry](requirements/registry.md) for every requirement;
- the registers for everything open;
- [`tools/docs/`](../tools/docs/README.md) to rebuild and check the indexes and to compare requirements with any earlier commit.

No conversation history is needed.

## Checkpoint log ([DEC-032](decisions/DEC-032-adopt-checkpoint-and-verification-rule.md))

Each checkpoint commit and its verification record. Hashes are those on branch `claude/code-builder-constitution-rrewgf`; a commit cannot contain its own hash, so each checkpoint's hash is recorded by the next one.

| Commit | Contents | Verification record |
|---|---|---|
| 16d317c | Constitution adopted; project state created | — (before the rule) |
| b850eaa | Handoff Part 1 documented | [Part 1 verification](traceability/part-1-verification.md) |
| 9fdbc3f | Part 1 open items resolved (DEC-006 to DEC-018) | [Resolution verification](traceability/resolution-verification.md) |
| 419b8da | Owner correction 1 (DEC-019, DEC-020) | [Owner correction 1 verification](traceability/owner-correction-01-verification.md) |
| 03716bf | Owner decisions on CF-11 to CF-13 (DEC-021 to DEC-023) | [Owner decisions 2 verification](traceability/owner-decisions-02-verification.md) |
| b6f005e | Handoff Part 2 integrated (DEC-024, DEC-025) | [Part 2 verification](traceability/part-2-verification.md) |
| a9034ce | Owner decisions on the Part 2 findings (DEC-026 to DEC-030) | [Owner decisions 3 verification](traceability/owner-decisions-03-verification.md) |
| a2c8e92 | Handoff Part 3 integrated; checkpoint rule adopted (DEC-031, DEC-032) | [Part 3 verification](traceability/part-3-verification.md) |
| 5846675 | Repository integrity verification; tooling lint and type fixes | [Integrity verification 2026-10-01](traceability/integrity-verification-2026-10-01.md) |
| The commit that adds this row | Master execution constitution and owner directive adopted (DEC-033, DEC-034) | [Governance adoption verification](traceability/governance-adoption-verification.md) |
