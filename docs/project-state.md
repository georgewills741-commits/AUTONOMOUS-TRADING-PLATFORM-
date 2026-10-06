# Project State

The single record of where this project currently stands (Constitution Rules 50, 172). Update it after every major piece of work. If it disagrees with the repository, the repository wins and this file gets corrected (Rule 52).

**Last updated:** 2026-10-06

## Current stage

**FOUNDATION — Stage 1 implementation in progress: checkpoint A done; checkpoint B is next.**

- Handoff Parts 1, 2, and 3 are documented and reconciled into one knowledge base ([DEC-024](decisions/DEC-024-part-2-reconciliation.md), [DEC-031](decisions/DEC-031-part-3-reconciliation.md)).
- The owner's company-grade autonomous operating model and the owner's decisions on CF-11 to CF-13 are applied.
- The owner answered every Part 2 finding (DEC-026 to DEC-030).
- The owner **approved the Part 3 reconciliation** and answered every open item on 2026-10-02 ([DEC-035](decisions/DEC-035-owner-decisions-part-3-findings.md)): security ranks above the user's hard policy (RSK-049), CF-18 confirmed, the constitution's feature lifecycle is canonical (GOV-024), no Part 4 is coming, older decision records get their alternatives now (TC-08; done, see below), and the DUP-34 and DUP-35 readings are confirmed.
- The owner's checkpoint and three-stage verification rule is adopted ([DEC-032](decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)).
- The owner's master execution constitution and directive on verification and platform independence (2026-10-01) are adopted ([DEC-033](decisions/DEC-033-adopt-master-execution-constitution.md), [DEC-034](decisions/DEC-034-verification-and-platform-independence.md)). The owner decided CF-19 from them (DEC-035).
- The **complete documentation review** was done on 2026-10-02 and 2026-10-03 as the owner's master knowledge-base audit ([record](traceability/master-knowledge-base-audit-2026-10-02.md)): verdict **B — ready with non-blocking findings** for Stage 1 planning. On 2026-10-03 the owner **accepted the review**, decided its four findings (CF-20, CF-21, OQ-28, DUP-40), confirmed the feature process, and **authorized Stage 1 planning** ([DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md)).
- On 2026-10-05 the owner's final decision checkpoint ([final decision checkpoint](traceability/final-decision-checkpoint-2026-10-05.md)) found two matters needing the owner. The owner **approved the [Stage 1 plan](roadmap/stage-01-foundation-plan.md)** with its decisions D1 to D11 as recommended and **authorized Stage 1 implementation** ("Begin Stage 1", [DEC-038](decisions/DEC-038-stage-1-plan-approved.md)). The owner's first-round answers of 2026-09-30 are now preserved verbatim ([DEC-037](decisions/DEC-037-final-decision-and-integrity-checkpoint.md)).
- Stage 1 is in progress. Checkpoint A built the development environment, the testing foundation, and the machine checks, and passed its three gates ([stage record](traceability/stage-01-foundation.md); [checkpoint A verification](traceability/stage-01-checkpoint-a-verification.md)). The platform has no trading capability. No later stage is authorized.

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
| Human review of the Part 3 reconciliation (P3§541 items 29–30), with CF-17, CF-18, CF-19, OQ-27, TC-08, and the DUP-34, DUP-35 readings | APPROVED and ANSWERED by the owner on 2026-10-02 — [DEC-035](decisions/DEC-035-owner-decisions-part-3-findings.md) · [answers](handoffs/owner-decisions-04-part-3-findings.md) |
| TC-08: alternatives in DEC-001 to DEC-030 (owner's choice: add now where sourced) | DONE — [TC-08 verification](traceability/tc-08-alternatives-verification.md) |
| Complete documentation review (handoff §101; P2§329) | DONE by the builder on 2026-10-02 and 2026-10-03, verdict B — [master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md); **ACCEPTED by the owner** on 2026-10-03 — [DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md) |
| Owner decisions raised by the audit: CF-20 (local hosting vs production independent of the owner's computer), CF-21 (PLT-010's wording on withdrawals), OQ-28 (instrument scope), DUP-40 (duplicated retention values) | DECIDED by the owner on 2026-10-03 — [DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md) · [answers](handoffs/owner-decisions-05-audit-findings.md) · [verification](traceability/owner-decisions-05-verification.md) |
| Stage 1 (FOUNDATION) planning | AUTHORIZED on 2026-10-03 ([DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md)); the [Stage 1 plan](roadmap/stage-01-foundation-plan.md) WRITTEN and verified ([verification](traceability/stage-01-plan-verification.md)); **APPROVED by the owner** on 2026-10-05, D1 to D11 as recommended — [DEC-038](decisions/DEC-038-stage-1-plan-approved.md) · [answers](handoffs/owner-decisions-06-stage-1-plan.md) |
| Final human-decision, knowledge-base, consistency, and repository checkpoint (owner request, 2026-10-05) | DONE — [final decision checkpoint](traceability/final-decision-checkpoint-2026-10-05.md); two owner decisions found and answered (DEC-038); first-round answers preserved ([DEC-037](decisions/DEC-037-final-decision-and-integrity-checkpoint.md)) |
| Human approval to implement | **GIVEN for Stage 1 only** — "Begin Stage 1", 2026-10-05 ([DEC-038](decisions/DEC-038-stage-1-plan-approved.md)). Every later stage needs its own approved plan and the owner's explicit approval (handoff §101; P2§330; P3§541; constitution Part XXIII, Rule 136) |
| Stage 1 checkpoint A: development environment (U1), testing foundation and machine checks (U6) | BUILT; three gates PASSED — [checkpoint A verification](traceability/stage-01-checkpoint-a-verification.md). The machine checks pass on GitHub and fail on a deliberately broken check ([stage record](traceability/stage-01-foundation.md), "Machine checks on GitHub") |
| Product implementation | **Stage 1 IN PROGRESS** (checkpoint A done; checkpoint B next). No trading capability exists; nothing is deployed; live trading is not active and is not part of Stage 1 (handoff §00 items 22–25; P2§330; Part 3 header) |

## Current objective

Stage 1 (FOUNDATION) as the approved [Stage 1 plan](roadmap/stage-01-foundation-plan.md) defines it ([DEC-038](decisions/DEC-038-stage-1-plan-approved.md)): a reproducible development environment, exact amounts, the contract kernel, configuration, the security foundation, machine checks, and the verification matrix, in checkpoints A to D, each through the three gates. No trading capability.

## Continuation contract

What the next session needs before it does anything (master execution constitution §03, §04, §87; DEC-033). Updated at every checkpoint and before a session ends. If this contract and the repository disagree, stop and reconcile first (§05).

| Field | Now |
|---|---|
| Current stage and substage | FOUNDATION — Stage 1 (DEC-038); checkpoint A done; checkpoint B (U2 exact amounts, U3 contract kernel) not yet started |
| Current task | None in progress at this checkpoint. Next: checkpoint B of the [Stage 1 plan](roadmap/stage-01-foundation-plan.md) (U2, U3), starting with the items the [stage record](traceability/stage-01-foundation.md) carries to it |
| Completed | See "Completed work" and the checkpoint log below |
| In progress, possibly partial | Nothing |
| Blocked | Nothing. The plan's risk that pushing the workflow might need further permission did not occur: the push was accepted and the workflow runs |
| Failed verification | None open |
| Pending verification | None |
| Verified | Every checkpoint in the checkpoint log, by its verification record |
| Not verified | Platform behavior: none exists yet; checkpoint A built the tooling, a repository test, and a package root that holds no code yet |
| Latest verified commit | The last row of the checkpoint log (a commit cannot record its own hash; the next checkpoint fills it in) |
| Uncommitted changes | None at a checkpoint. Changes found at the start of a session are unexplained until inspected (§07) |
| Repository integrity | Clean at the last checkpoint ([integrity verification](traceability/integrity-verification-2026-10-01.md); the record of each later checkpoint) |
| Known risks | TC-09 and TC-10 stay open until their stages are planned. Interfaces, schemas, tests, and failure procedures are specified only when each stage is planned (audit finding A-05). The plan's technical claims for U2 and U3 were tested on mypy 1.19.1; the locked mypy is 2.4.0, so checkpoint B re-tests them on the locked versions ([stage record](traceability/stage-01-foundation.md)) |
| Next safe action | "Next approved step", item 1: checkpoint B |
| Documentation state | Consistent and checked (`build_index.py --check-only`); the registry's Approval column reads "reviewed (DEC-036)" for the 512 handoff requirements, since the owner accepted the review |
| Do not change | The verbatim texts under `docs/handoffs/` and `docs/builder/` (only a status banner may change, by decision); any requirement's text or class without a decision record; the generated parts of generated files by hand; a dependency or a pinned version except as the [development guide](development.md) describes |
| Do not implement yet | Anything outside the approved Stage 1 plan: no later stage, no trading, no credentials, no deployment, no system contracts (they wait for their stages' plans); FUTURE and PROPOSED items stay unbuilt (handoff §101; constitution Rules 134–136) |

## Owner decisions on the Stage 1 plan (2026-10-05)

Both answered ([owner decisions 6](handoffs/owner-decisions-06-stage-1-plan.md)); applied by [DEC-038](decisions/DEC-038-stage-1-plan-approved.md):

| Item | Owner's decision | Applied |
|---|---|---|
| The Stage 1 plan's D1 to D11 | Approved, all as recommended | The [Stage 1 plan](roadmap/stage-01-foundation-plan.md) is APPROVED; D5 (feature-status table in the roadmap) and D6 (GOV-009's statuses next to GOV-024) in Architecture governance; D11's added dependencies in the technology stack |
| Stage 1 implementation | "Begin Stage 1" | Authorized for Stage 1 only; implementation started with checkpoint A on 2026-10-06 |

## Owner decisions on the audit findings (2026-10-03)

All answered ([owner decisions 5](handoffs/owner-decisions-05-audit-findings.md)); applied by [DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md):

| Item | Owner's decision | Applied |
|---|---|---|
| CF-20: hosting | Production never depends on any one machine, your computer included: an active host plus a standby, rebuilt without you. Your computer may be a production host only if it meets the same readiness bar as a server | MIG-033; local hosting stays supported (MIG-001, MIG-002) |
| OQ-28: instruments | Spot, perpetual futures, and margin; no other derivatives | PLT-011 confirmed |
| CF-21: withdrawal wording | PLT-010 matches DEC-006: "no deposit or withdrawal handling for others", naming SEC-006 for rebalancing transfers | PLT-010 reworded |
| DUP-40: retention values | Only in TEC-012; MKD-007 and MON-009 point to it | MKD-007, MON-009 reworded; V-18, V-19 |
| Feature process | GOV-002 with GOV-022, your sequence mapped onto it | Confirmed; no change |
| Documentation review | Accepted | Registry Approval column: "reviewed (DEC-036)" |
| Stage 1 planning | Authorized | The [Stage 1 plan](roadmap/stage-01-foundation-plan.md) was written and verified, and you approved it on 2026-10-05 (DEC-038) |

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
  - **Owner decisions:** single operator with no custody (DEC-006); spot, perpetual futures, and margin (DEC-007); venues Binance, OKX, Coinbase, Bybit, KuCoin, and extensible (DEC-008; Bybit and KuCoin as initial venues are the builder's reading of the owner's written answer, reported to the owner the same day).
  - **Owner-delegated:** technology stack — Python 3.12 core, Rust only for measured hot paths, PostgreSQL + TimescaleDB, Parquet/DuckDB, NATS, CCXT (DEC-009).
  - **Decided under the owner's instruction:** DEC-001 to DEC-005 accepted (first recorded as PROPOSED); DEC-010 to DEC-018 — pre-trade flow, ownership of every overlapping responsibility, safety architecture, AI organization (five agents plus three deterministic services), net-profit formula and uncertainty margin, modes/canary/policy governance, stage placement, reporting and performance targets, initial directional research candidates.
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
  - New documents: [Architecture governance](architecture/architecture-governance.md) (GOV-001 to GOV-020; GOV-018 since replaced by GOV-024, DEC-035); [System Rules Register](requirements/system-rules-register.md) (SR-01 to SR-45); [Reliability and recovery model](operations/reliability-and-recovery-model.md) (index). The [Readiness System](systems/readiness-system.md) now documents the capability and readiness model; [Deployment and operational readiness](operations/deployment-and-operational-readiness.md) the production-readiness model.
  - Registers: CF-17, CF-18, DUP-32 to DUP-38 (resolved by DEC-031; CF-17 and CF-18 then awaited confirmation, since decided by the owner, DEC-035); OQ-27, TC-08, TC-09 (then open; OQ-27 and TC-08 since decided, DEC-035); values V-36 to V-39.
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
  - New: the continuation contract; the verification-record format ([traceability README](traceability/README.md)); glossary aliases for the constitution's authority names; tooling that makes verification repeatable: a check that the preserved verbatim texts never change, an orphaned-document check, and a self-test of the tools ([tools README](../tools/docs/README.md)). Findings CF-19 (feature lifecycle; since decided by the owner, DEC-035), DUP-39 (resolved), TC-10 (shared state names, open until the state machines are specified).
- **Owner decisions 4 (Part 3 findings and review, 2026-10-02):**
  - Answers kept word for word ([owner decisions 4](handoffs/owner-decisions-04-part-3-findings.md)); applied by [DEC-035](decisions/DEC-035-owner-decisions-part-3-findings.md).
  - CF-17: security ranks above the user's hard policy, below the safety floor: RSK-049 replaces RSK-048. CF-18 confirmed. CF-19: the master execution constitution's feature lifecycle is canonical: GOV-024 replaces GOV-018. Both replaced requirements keep their wording; only their class changed.
  - OQ-27 answered (no Part 4). TC-08 decided (alternatives added now, where sourced). DUP-34 and DUP-35 confirmed. The Part 3 reconciliation is approved.
- **TC-08, alternatives in the older decision records (2026-10-02, the owner's choice):**
  - DEC-002, DEC-004, DEC-005, DEC-007, DEC-008, DEC-010 to DEC-013, and DEC-015 to DEC-030 now have an "Alternatives considered" section; DEC-001, DEC-003, DEC-006, DEC-009, and DEC-014 already had one. Each alternative names where the repository records it: an option shown to the owner, a proposal or candidate in the registers, the side of a finding not chosen, an option the record itself rules out, an earlier version of a document in git history, or an approach the owner's own text explicitly sets against the chosen one. DEC-003 and DEC-009 gained one such alternative each, under a line marking the addition. DEC-018 says none were recorded; nothing was reconstructed from memory.
  - No decision, requirement, or finding changed. TC-08 is RESOLVED. Record: [TC-08 verification](traceability/tc-08-alternatives-verification.md).
- **Master knowledge-base audit, the complete documentation review (2026-10-02, the owner's request):**
  - The whole repository audited as one knowledge system against the owner's 28-point request: decisions, duplicates, conflicts, classification, ownership, sources of truth, traceability, boundaries, capital, security, safety, performance, extensibility, platform independence, roadmap, verification, structure, documentation, implementation.
  - Verdict B, ready with non-blocking findings for Stage 1 planning; no critical or high finding. Raised for the owner: CF-20, CF-21, OQ-28, DUP-40 (decided on 2026-10-03, DEC-036). Fixed: the documentation defects listed in the record. No requirement changed.
  - Record, with the findings, the consistency matrix, the human review package, and the request verbatim: [master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md).
- **Owner decisions 5 (audit findings, review acceptance, Stage 1 planning, 2026-10-03):**
  - Answers kept word for word ([owner decisions 5](handoffs/owner-decisions-05-audit-findings.md)); applied by [DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md).
  - CF-20: MIG-033 added (production never depends on one machine). CF-21: PLT-010 reworded to match DEC-006. DUP-40: MKD-007 and MON-009 reworded to point to TEC-012. OQ-28: PLT-011 confirmed. The feature process (GOV-002 with GOV-022) confirmed.
  - The complete documentation review is accepted: the registry's Approval column for the 512 handoff requirements reads "reviewed (DEC-036)". Stage 1 planning is authorized.
- **Stage 1 plan (written 2026-10-03, revised after the independent reviews 2026-10-05; planning authorized by DEC-036):**
  - The [Stage 1 plan](roadmap/stage-01-foundation-plan.md) (approved on 2026-10-05, [DEC-038](decisions/DEC-038-stage-1-plan-approved.md)): objective, entry gate, the requirements Stage 1 covers, eight work units (development environment, testing and machine checks, exact amounts, contract kernel, configuration, security foundation, verification matrix, stage record) in four checkpoints, out of scope, outputs, tests, verification, completion criteria, and eleven decisions for the owner (D1 to D11).
  - No requirement or decision changed; no code written. Record: [Stage 1 plan verification](traceability/stage-01-plan-verification.md).
- **Final human-decision, knowledge-base, consistency, and repository checkpoint (2026-10-05, the owner's request):**
  - The open, deferred, conditional, recommended, and replaced items found by scripted sweeps of every active document classified; every decision the repository attributes to the owner checked against the owner's answers as given; conflict, duplicate, stale-statement, and canonical-source sweeps re-run. Record: [final decision checkpoint](traceability/final-decision-checkpoint-2026-10-05.md).
  - Two matters needed the owner: the Stage 1 plan's D1 to D11 and the authorization to implement. Both answered: approved as recommended, and "Begin Stage 1" ([DEC-038](decisions/DEC-038-stage-1-plan-approved.md); [owner decisions 6](handoffs/owner-decisions-06-stage-1-plan.md)).
  - The owner's first-round instruction and answers (OQ-01, OQ-03, OQ-04, OQ-16) preserved verbatim as [owner decisions 1](handoffs/owner-decisions-01-part-1-open-items.md), and the options shown with CF-11 to CF-13 as [owner decisions 2: options shown](handoffs/owner-decisions-02-options-shown.md); the edited quotations in DEC-006 to DEC-009 annotated, not rewritten; the CF-21 question's wording point recorded (finding F-02) ([DEC-037](decisions/DEC-037-final-decision-and-integrity-checkpoint.md)). No requirement changed.
- **Stage 1, checkpoint A (2026-10-06): development environment (U1), testing foundation and machine checks (U6):**
  - `pyproject.toml`, `uv.lock`, `.python-version`, the package root `src/atp/`; uv 0.12.23 required exactly; ruff, mypy (strict), pytest, Hypothesis, and Pydantic locked; the documentation tools keep their own check settings.
  - The repository test for secrets, the first real test (52 tests pass); `.gitignore` for local environment and secret files.
  - `.github/workflows/checks.yml`: the same checks on every push and pull request, read-only, no secret, actions pinned by commit hash, uv by version and checksum.
  - The dependency review (no published advisory) and the license check, the [development guide](development.md), the [stage record](traceability/stage-01-foundation.md), and the roadmap's feature-status table (D5). No requirement or decision changed. Record: [checkpoint A verification](traceability/stage-01-checkpoint-a-verification.md).

## In-progress work

None at this checkpoint. Next: checkpoint B (see "Next approved step").

## Blockers

| Problem | Impact | Required resolution |
|---|---|---|
| None open | — | — |

## Open questions

Nothing is waiting for the owner. CF-20, CF-21, OQ-28, and DUP-40, raised by the [master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md), were decided on 2026-10-03 ([DEC-036](decisions/DEC-036-owner-decisions-audit-findings.md)). The Stage 1 plan's D1 to D11 and the authorization to implement were decided on 2026-10-05 ([DEC-038](decisions/DEC-038-stage-1-plan-approved.md)).

Recorded now and decided when their stages are planned:

| Item | Question | Where |
|---|---|---|
| TC-09 | How a standby gets trading keys for automatic takeover without being able to trade before it holds the lease; decided when OPERATIONALIZATION is planned | [Open-question register](open-questions/register.md) |
| TC-10 | Shared state names (SUSPENDED, DEGRADED, ACTIVE, SAFE MODE, EMERGENCY, RESEARCH, PAPER, VALIDATING, APPROVED, CANARY, PRODUCTION, DEPRECATED, RETIRED, UNKNOWN, UNCERTAIN, ROLLBACK; the register lists where each is used) get one meaning each when the state machines are specified | [Open-question register](open-questions/register.md) |

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
- **Hosting.** The same platform runs locally or on a server, with migration only through a formal, reconciled process (MIG-001 to MIG-028). Production never depends on one machine, your computer included (MIG-033, from your answer on CF-20).
- **Canary.** Canary is a production stage (OPS-013).

**From your answers on the Part 2 findings:**

- **Safety floor.** Immutable safety invariants that nothing and nobody can bypass. Inside them, the platform adapts limits, allocation, and thresholds automatically, recovers by itself, and isolates problems instead of stopping everything (RSK-034 to RSK-039).
- **Capital.** Directional, emergency, and per-exchange buckets, sized dynamically and rebalanced automatically. Capital-intensive features switch on only as capital and proven safety allow (CAP-029 to CAP-033).
- **Infrastructure.** All production infrastructure is kept as code and rebuildable without you (OPS-014 to OPS-017).
- **High availability.** A standby takes over automatically after reconciling (REC-023). Only one copy ever trades, and a migration swaps exchange keys (MIG-029).

**From Part 3 (approved by the owner, DEC-035):**

- **Capability scales with the account, not with capital alone.** Small accounts are first-class; capabilities unlock automatically when economics, liquidity, risk, readiness, and policy allow, never because a balance crossed a fixed number; growth never raises exposure by itself (RDY-009 to RDY-026, CAP-034, PLT-023).
- **Search aggressively, act conservatively.** Broad, continuous discovery; a detected opportunity is only a candidate (PLT-022, OPP-017 to OPP-020).
- **Rebalancing** decides among NO ACTION, now, later, partial, pre-position, wait, or emergency, without churn, always through the capital authority (CAP-037 to CAP-042).
- **System rules** are indexed with owner, enforcement point, and violation handling in the [System Rules Register](requirements/system-rules-register.md).
- **Restart is not resume;** failures are isolated to the service that failed (REC-025, REC-026).
- **New features** pass the governance gate before approval (GOV-001 to GOV-024; GOV-018 replaced by GOV-024).

## Recent decisions

[Decision log](decisions/README.md):

- DEC-001 to DEC-005 accepted (first recorded as proposed).
- DEC-006 to DEC-018 added on 2026-09-30.
- DEC-019 and DEC-020 (owner correction) and DEC-021 to DEC-023 (owner decisions on CF-11 to CF-13) added the same day.
- DEC-024 (Part 2 reconciliation) and DEC-025 (documentation tooling in the repository) added the same day.
- DEC-026 to DEC-030 (owner decisions on the Part 2 findings) added the same day. DEC-024 confirmed by the owner.
- DEC-031 (Part 3 reconciliation; approved by the owner on 2026-10-02) and DEC-032 (the owner's checkpoint and verification rule) added the same day.
- DEC-033 (master execution constitution) and DEC-034 (owner's directive on verification and platform independence) added on 2026-10-01.
- DEC-035 (owner decisions on the Part 3 findings; Part 3 approved) added on 2026-10-02. DEC-031 confirmed by the owner, with CF-17 changed.
- DEC-001 to DEC-030 all have an "Alternatives considered" section since 2026-10-02 (TC-08, DEC-035). No decision changed.
- DEC-036 (owner decisions on the audit findings; documentation review accepted; Stage 1 planning authorized) added on 2026-10-03.
- DEC-037 (final decision and integrity checkpoint; first-round answers preserved) and DEC-038 (Stage 1 plan approved; Stage 1 implementation authorized) added on 2026-10-05.

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
- 2026-10-02: applied owner decisions 4 (DEC-035): RSK-049 and GOV-024 added; RSK-048 and GOV-018 replaced (class only); every conflict resolved; OQ-27 answered; Part 3 approved. The requirement comparison gained `--expect-changed` for decided changes. No platform code, configuration, or infrastructure created.
- 2026-10-02: TC-08: "Alternatives considered" sections added to the 25 older decision records that lacked one, each alternative with its source; TC-08 resolved. No requirement, decision, or finding changed.
- 2026-10-02: master knowledge-base audit (the complete documentation review), verdict B: CF-20, CF-21, DUP-40, OQ-28 raised for the owner; documentation defects fixed (glossary aliases, TC-10 inventory, source-of-truth rows, stale notes); no requirement changed ([record](traceability/master-knowledge-base-audit-2026-10-02.md)).
- 2026-10-03: applied owner decisions 5 (DEC-036): MIG-033 added; PLT-010, MKD-007, and MON-009 reworded; CF-20, CF-21, DUP-40, OQ-28 resolved; documentation review accepted (registry Approval column "reviewed"); Stage 1 planning authorized. No platform code, configuration, or infrastructure created.
- 2026-10-03 to 2026-10-05: wrote the [Stage 1 plan](roadmap/stage-01-foundation-plan.md) (PROPOSED), revised after two independent reviews: objective, entry gate, requirements, eight work units in four checkpoints, out of scope, outputs, tests, verification, completion criteria, and eleven decisions for the owner (D1 to D11). No requirement or decision changed; no code written.
- 2026-10-05: final human-decision, knowledge-base, consistency, and repository checkpoint: two owner decisions found and answered (DEC-038: Stage 1 plan approved, Stage 1 implementation authorized); first-round instruction and answers, and the options shown with CF-11 to CF-13, preserved verbatim (DEC-037); TC-10's GOV-009/GOV-024 part decided (D6); feature statuses to be kept in one roadmap table (D5). No requirement changed; no platform code written.
- 2026-10-06: Stage 1 checkpoint A: the development environment, the repository test for secrets, the machine checks, the development guide, the stage record, and the feature-status table. No requirement or decision changed; no trading capability.
- 2026-10-06: the machine checks ran on GitHub: they passed on checkpoint A's commit, failed on a deliberately broken check (`74ce426`), and passed on its revert (`bc6eca5`); recorded in the stage record.

## Next approved step

1. **The builder: checkpoint B of the [Stage 1 plan](roadmap/stage-01-foundation-plan.md).** First the items the [stage record](traceability/stage-01-foundation.md) carries to it: re-test the plan's technical claims for U2 and U3 on the locked versions (mypy 2.4.0 above all), enable ruff's SLF001, and write U6's Hypothesis setting with the first property tests. Then U2 (exact amounts) and U3 (contract kernel); three gates; commit; push.
2. **Then checkpoints C and D** in order (U4 and U5; U7 and U8), each through the three gates, and the stage's completion certificate, whose "approved to proceed" is the owner's.
3. **Authorization limits.** DEC-038 authorizes Stage 1 only (constitution Rules 134–136). Stage 2 needs its own plan and the owner's explicit approval.

## Memory check (constitution Rule 175)

A new session can reconstruct the project from the repository:

- this file for the state, starting with its continuation contract;
- [`docs/README.md`](README.md) for every document;
- the [development guide](development.md) to install, check, and test the code;
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
| 3b6f372 | Master execution constitution and owner directive adopted (DEC-033, DEC-034) | [Governance adoption verification](traceability/governance-adoption-verification.md) |
| 0b3f97a | Owner decisions on the Part 3 findings applied; Part 3 approved (DEC-035) | [Owner decisions 4 verification](traceability/owner-decisions-04-verification.md) |
| 74928b4 | TC-08: alternatives added to the older decision records | [TC-08 verification](traceability/tc-08-alternatives-verification.md) |
| 16df57f | Master knowledge-base audit (the complete documentation review), verdict B | [Master knowledge-base audit](traceability/master-knowledge-base-audit-2026-10-02.md) |
| bb19a60 | Owner decisions on the audit findings; documentation review accepted; Stage 1 planning authorized (DEC-036) | [Owner decisions 5 verification](traceability/owner-decisions-05-verification.md) |
| 47f5348 | Stage 1 plan written (PROPOSED), for the owner's approval | [Stage 1 plan verification](traceability/stage-01-plan-verification.md) |
| 69d3b86 | Final decision checkpoint; Stage 1 plan approved and Stage 1 implementation authorized (DEC-037, DEC-038) | [Final decision checkpoint](traceability/final-decision-checkpoint-2026-10-05.md) |
| f2e4046 | Stage 1 checkpoint A: development environment, testing foundation, and machine checks (U1, U6) | [Stage 1 checkpoint A verification](traceability/stage-01-checkpoint-a-verification.md) |
| The commit that adds this row | Checkpoint A's machine-check runs on GitHub recorded (after the negative test `74ce426` and its revert `bc6eca5`, which are not checkpoints) | [Stage 1 record](traceability/stage-01-foundation.md), "Machine checks on GitHub" |
