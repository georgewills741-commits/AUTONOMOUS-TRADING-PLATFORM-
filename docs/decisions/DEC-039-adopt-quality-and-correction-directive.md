# DEC-039 — Adopt the owner's master quality, consistency, verification and correction directive

- **Status:** ACCEPTED
- **Date:** 2026-10-06
- **Decided by:** project owner (directive sent on 2026-10-06, after Stage 1's checkpoint A); the builder's: how it combines with the four other builder texts, the reading notes, what each gate covers now that code exists, and the mapping of its platform-facing sentences to existing requirements
- **Text:** [`docs/builder/quality-consistency-and-correction-directive.md`](../builder/quality-consistency-and-correction-directive.md) (verbatim, ACTIVE)

## Context

On 2026-10-06, after Stage 1's checkpoint A was committed and its machine checks had run on GitHub, the owner sent the "Master Quality, Consistency, Verification & Correction Directive" (sections 1 to 16 and a final rule). Before any further implementation, it asks for the project to be brought into a correct, consistent, verified, and maintainable state: inspect and reconcile everything; correct every mistake whose correct resolution the approved requirements, architecture, rules, or decisions already establish; stop and ask the owner only for decisions that are genuinely the owner's, consolidated into one batch; pass every significant change through three distinct verification passes; state status only with evidence; keep to the authorized stage; and persist the session's state in the repository.

The audit it asks for is recorded in the [quality audit of 2026-10-06](../traceability/quality-audit-2026-10-06.md). Most of the directive restates rules the four builder texts already impose; what it adds is listed below.

## Decision

1. **Adopted as an active builder rule,** loaded in every session by `CLAUDE.md`. Five builder texts now apply together: the [builder constitution](../builder/claude-code-builder-constitution.md) (DEC-001), the [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md) (DEC-032), the [master execution constitution](../builder/master-execution-constitution.md) ([DEC-033](DEC-033-adopt-master-execution-constitution.md)), the [directive on verification and platform independence](../builder/verification-and-platform-independence-directive.md) ([DEC-034](DEC-034-verification-and-platform-independence.md)), and this directive. All are kept verbatim; none is restated elsewhere; where they differ, the stricter applies. What this directive adds or makes stricter:
   - **Correction policy (§6, §16).** A defect whose correct resolution an approved requirement, rule, decision, or canonical source already establishes is corrected in the same piece of work, with its secondary effects checked, and the correction is recorded when it materially changes the repository. It is not left as a finding. This keeps [DEC-005](DEC-005-record-findings-without-resolving.md), which applies a resolution to the specifications only after the owner accepts it: for a resolution that an approved requirement, rule, decision, or canonical source already establishes, the owner's directive itself (§2, §6, §16) is that acceptance; every other resolution still goes to the owner.
   - **Owner decision gate (§2, §11).** Every question put to the owner gives the exact issue, why it matters, the existing requirements and decisions, any conflicting material, the options, their consequences, the builder's recommended interpretation, and the exact decision required; several questions go in one batch. Constitution Rules 32 and 183 and the master execution constitution's §92, §156, and §183 already forbade guessing and stopped at explicit review gates, and §92 already asked for the question, why it matters, the options, the dependencies, and the status. New are the existing requirements and decisions, the conflicting material, the consequences, the recommended interpretation, the exact decision required, and the batch.
   - **No promotion without authorization (§4).** PROPOSED never becomes APPROVED, RECOMMENDED never becomes OWNER-APPROVED, FUTURE never becomes CURRENT, RESEARCH never becomes PRODUCTION, and POSSIBLE never becomes SUPPORTED without the authorization each needs (as ARCH-029 and constitution Rules 180 and 181 already say for requirements).
   - **Precise status (§10).** No completion claim without evidence, stated in precise words such as those §10 lists; verification records give their final status that way ([traceability README](../traceability/README.md)).
   - **Session continuity (§14).** The project state's continuation contract also carries the decisions confirmed and pending, the non-blocking findings, the files changed and tests performed at the last checkpoint, the documentation status, and the migration and release status.
   - **Repository integrity (§13)** is checked item by item before a checkpoint commit (Gate 2 below).

2. **Its three passes are the three gates of DEC-033.** The table states what each gate covers now that code exists (since Stage 1's checkpoint A). It replaces the last column of DEC-033's gate table ("What it means before code exists") as the current statement; what that column says of Gate 2's review and of Gate 3's independent reviewer stays in force, as the table's "As DEC-033 states" cells say. The other columns of that table, and DEC-032's scope (everything built, modified, or approved, documentation included), are unchanged.

   | Gate | This directive | What the gate covers now |
   |---|---|---|
   | 1 | Pass 1: code / content | The documentation checks (`build_index.py --check-only`, `compare_requirements.py <previous checkpoint> --strict`, `selftest.py`, and the round trip of any newly preserved text, [tools README](../../tools/docs/README.md)) and the code checks of the [developer guide](../development.md) (ruff, ruff format, mypy on `src/` and `tests/`, mypy on the tools, pytest, and `uv build`), all through the locked environment; then a reading of the changed content for correctness, completeness, error handling, and security-sensitive behavior |
   | 2 | Pass 2: repository / architecture | As DEC-033 states, plus the migration impact (§9) and the repository integrity list (§13) |
   | 3 | Pass 3: system / governance | As DEC-033 states: an independent reviewer (a separate agent that did not write the change) and the builder's own separate pass; failure paths; the platform's end-to-end, failure, recovery, concurrency, and regression tests as far as the platform exists. Also, explicitly, §9's governance list: requirements, system rules, security, risk, capital controls, readiness, regression, performance where applicable, deployment and recovery implications, documentation, and the roadmap and stage authorization |

3. **Platform-facing sentences already have owners.** None becomes a new requirement:

   | Section | Topic | Requirements that own it |
   |---|---|---|
   | §5 | One canonical source and one authority per responsibility | ARCH-017, ARCH-027, ARCH-037, ARCH-016; the [source-of-truth map](../architecture/source-of-truth-map.md) |
   | §7 | No correction or optimization bypasses deterministic financial calculations, risk validation, capital authority, execution validation, reconciliation, security, auditability, data integrity, or recovery | PERF-023, RSK-034, ARCH-010, TEC-003, REC-003, REC-015, SEC-005, AUD-012, MKD-004 |
   | §7 | AI never becomes the financial source of truth | PLT-016, ARCH-019, AIL-002, AIL-003, LED-006 |
   | §7, §12 | No live trading, exchange connectivity, credentials, withdrawals, or production financial authority outside the authorized stage | The implementation gate (handoff §101; constitution Rules 134 to 136); [DEC-038](DEC-038-stage-1-plan-approved.md), which authorizes Stage 1 only; SEC-006, SEC-007 |
   | §8 | Performance never at the cost of correctness; measured, not claimed | PERF-023, PERF-022, PERF-006, PERF-010, PERF-012 |
   | §14 | The production platform operates without Claude Code | PLT-029, GOV-023 |
   | §15 | Future work extends the existing platform through the existing governance and feature lifecycle | GOV-021, GOV-022, GOV-002, GOV-024. Its sequence is mapped the way the owner's sequence of 2026-10-02 was ([architecture governance](../architecture/architecture-governance.md); confirmed by the owner, [DEC-036](DEC-036-owner-decisions-audit-findings.md)): checking existing capabilities, release, and deployment are steps of GOV-022; the security, risk, performance, and data/API checks and the authorization where required are steps of GOV-002 |

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "Before proceeding with any further implementation" | Checkpoint B of Stage 1 starts only after this directive's audit has passed its three gates and been committed |
| §10's status words; the document labels | Words for the builder's claims and reports and for documents, not platform states. Where the platform uses the same word it keeps its platform meaning there: BLOCKED and REQUIRES_REVIEW in component readiness (RDY-017, with its READY_FOR_ states; RDY-004 has READY_FOR_CANARY); APPROVED in GOV-024 and the strategy lifecycle (STR-024); ACTIVE in GOV-009; and the shared state names of TC-10 ([glossary](../glossary.md)) |
| §11 "STOP" | The stop applies to the matter that needs the owner's decision: nothing that depends on it proceeds, and the matter is put to the owner at once. Work that does not depend on it continues, and the question says so, so the owner can object |
| §9 "every major correction … and significant documentation change" | DEC-032's scope is wider and stays: everything built, modified, or approved |
| §1 "technical debt"; §14 "non-blocking findings" | Each item stays in the record that found it; the continuation contract lists them by pointer, so no second list of them appears |
| §14 "migration/release status" | Nothing is released or deployed, and no database, schema, or migration exists; the continuation contract says so until one does |
| §3 "duplicate feature lifecycles" | GOV-024 is the one feature lifecycle; GOV-009's statuses are related to it by D6 ([DEC-038](DEC-038-stage-1-plan-approved.md)); strategies keep their own lifecycle (STR-001, STR-024) |

## Alternatives considered

- **Treat the directive as a one-time instruction for this audit only.** Rejected: sections 2 to 6 and 9 to 16 state lasting rules, and owner instructions are not left in chat (master execution constitution §90; the checkpoint rule, "everything must be preserved in the repository").
- **Preserve it as historical input under `docs/handoffs/`, or in the audit record's appendix as the earlier audit requests were.** Rejected: rules that govern every session belong with the builder texts, loaded by `CLAUDE.md`, as DEC-032 to DEC-034 did.
- **Fold it into one of the existing builder texts.** Rejected: owner texts are kept verbatim and never restated (constitution Rule 27; `CLAUDE.md`).
- **Make its platform-facing sentences new requirements.** Rejected: each already has an owner (decision 3); a copy would be a second source (constitution Rule 30; ARCH-016).

## Consequences

- `CLAUDE.md` loads five builder texts; the manifest of preserved texts has a line for this one.
- Gate coverage is decision 2's table; DEC-032 and DEC-033 get "Later changes" lines pointing here.
- DUP-39 in the [findings register](../conflicts/register.md) covers this text too: its passes are the gates, and its continuity fields are in the one project state.
- The corrections of the audit, made under §6, are listed in its record. Two of them change status banners of preserved texts, which never changes the texts themselves: the master execution constitution's banner now names five builder texts, and the banner of owner correction 1 records the covering line the owner sent it with.
- The continuation contract in the [project state](../project-state.md) carries the fields of §14.
- No requirement changes. Nothing here authorizes implementation beyond DEC-038's Stage 1.
