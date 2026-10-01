# DEC-033 — Adopt the master execution, consistency, verification and continuity constitution

- **Status:** ACCEPTED
- **Date:** 2026-10-01
- **Decided by:** project owner (constitution sent on 2026-10-01, marked "non-negotiable development governance"); the builder's: how the four builder texts combine, the reading notes, the placement of the platform-facing sections, and the wording of ARCH-041, ARCH-042, and PERF-023 taken from §139, §47, and §43
- **Text:** [`docs/builder/master-execution-constitution.md`](../builder/master-execution-constitution.md) (verbatim, ACTIVE)

## Context

On 2026-10-01 the owner sent the "Claude Code Master Execution, Consistency, Verification & Continuity Constitution" (§00 to §184), together with a request for a repository integrity check (done first: [integrity verification](../traceability/integrity-verification-2026-10-01.md)) and a directive on three-level verification and platform independence ([DEC-034](DEC-034-verification-and-platform-independence.md)). The constitution names Claude Code as builder and GPT as architect and specification author. It "supplements the project specification" and does not replace Parts 1 to 3, approved requirements, architecture, decision records, system rules, or the roadmap (§00).

Most of it is about how Claude works: session continuity, verification, Git, and repository hygiene. 61 of its 185 sections also state platform behavior, almost all of it already required by Parts 1 to 3 and earlier decisions.

## Decision

1. **Adopted as active builder rules,** loaded in every session by `CLAUDE.md`. Four builder texts now apply together: the [builder constitution](../builder/claude-code-builder-constitution.md) (DEC-001), the owner's [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md) (DEC-032), this constitution, and the owner's [directive](../builder/verification-and-platform-independence-directive.md) (DEC-034). All are kept verbatim; none is restated elsewhere. Where they differ, the stricter applies. They overlap heavily (DUP-39); what this constitution adds or makes stricter:
   - **Session continuity:** a durable checkpoint before a session ends (§04, §179), a resume protocol that stops when repository and checkpoint disagree (§05, §06), an emergency checkpoint (§132), a continuation contract (§87), and the fresh-session test (§88, §141). These live in the [project state](../project-state.md)'s "Continuation contract".
   - **Commits:** no dirty handoff (§52), the diff reviewed before the commit (§127, §128), and the commit itself verified after it is made (§53, §129).
   - **Evidence:** every verification leaves a repeatable record (§21, §22); the format is in the [traceability README](../traceability/README.md), with the stage record, completion certificate, transition checklist, and verification matrix that start at Stage 1 (§142 to §145, §152).
   - **Stop-the-line** (§153 to §155) and the **human review gate** (§156): "continue" in an unrelated instruction never approves an explicit gate. This matches constitution Rule 135.
   - **Generated files** have a policy (§70): the [tools README](../../tools/docs/README.md) and `.gitignore`, from the integrity checkpoint.

2. **One three-gate procedure (DUP-39).** Each gate covers everything the texts ask of it:

   | Gate | Builder constitution | Checkpoint rule (DEC-032) | This constitution | Directive (DEC-034) | What it means before code exists |
   |---|---|---|---|---|---|
   | 1 | Rule 119: code / implementation | Implementation / functional | §15: technical / implementation | Technical / implementation: tests, type checks, linting, builds | `tools/docs/build_index.py --check-only` (which also checks that preserved texts are unchanged and no document is orphaned); `tools/docs/compare_requirements.py <previous checkpoint> --strict`; `tools/docs/selftest.py` (negative tests of the tools); the round trip of any newly preserved text against the text as received; ruff, ruff format, and mypy on the tools ([tools README](../../tools/docs/README.md)) |
   | 2 | Rule 120: repository / architecture | Architecture / consistency | §16: architecture / consistency / requirements | Architecture / consistency | Review against requirements, decisions, registers, system rules, terminology, and ownership; search for duplicates, conflicts, drift, missing requirements, and broken traceability |
   | 3 | Rule 121: whole system / regression | Independent final audit / regression | §17: end-to-end / failure / operational | Independent end-to-end / failure | An independent reviewer (a separate agent that did not write the change) plus the builder's own separate pass; failure paths of the tools. From Stage 1 also end-to-end, failure, recovery, concurrency, and regression tests of the platform |

   The gates apply to everything built, modified, or approved, documentation included: DEC-032's scope, which is stricter than the directive's "every development stage, feature, module, subsystem, or significant change" and this constitution's "every major stage" (§14). They must be materially different checks (§18; Rule 122). A failed gate stops progression until fixed and re-run with every gate it could affect (§19).

3. **Project state stays where it is.** §03 suggests `docs/00-project/project-state.md` "or another explicitly designated authoritative location". [`docs/project-state.md`](../project-state.md) is that location (DEC-002's layout); moving it would break links and history for no gain. It now carries the fields of §03, §04, and §87.

4. **Platform-facing sections** are mapped to the requirements that already own them (table below). Three statements had no full home and become requirements, with DEC-033 as their source: ARCH-041 (§139, idempotent financial operations), ARCH-042 (§47, UNKNOWN is never SUCCESS), and PERF-023 (§43, no unsafe fast path). They are indexed as SR-46, SR-47, and in SR-09 of the [System Rules Register](../requirements/system-rules-register.md). No existing requirement changes.

5. **Terminology (§26, §35, §36).** The constitution's authority names are aliases of existing systems ([glossary](../glossary.md), [source-of-truth map](../architecture/source-of-truth-map.md)). State names used by more than one state machine are TC-10, decided when the state machines are specified.

6. **Feature lifecycle (§107).** It conflicts with Part 3's proposed feature statuses (GOV-018): CF-19, for the owner.

## Reading notes (builder)

| Section | Reading |
|---|---|
| §00 "ARCHITECT / SPECIFICATION AUTHOR: GPT" | Recorded as received. The text's authority here is the owner's sending it, recorded by this decision |
| §10 research/, experiments/, prototypes/ | Allowed only if the architecture permits them. None exists and none is created now (constitution Rule 12) |
| §20 exceptions to a blocker | Need the owner's explicit approval, recorded in a decision record |
| §41 "CANARY … remain correctly separated" | Canary is a production stage, separated by its own allocation and deterministic controls (OPS-013, STR-020), not a separate environment. No conflict |
| §85, §86 session limits | Stop starting new work, checkpoint the current unit, persist state; never rush completion. The integrity checkpoint was committed before this adoption began |
| §121 build order | Dependency order of the [roadmap](../roadmap/roadmap.md), never conversation order |
| §156 human review gate | The Part 3 human review (P3§541 items 29–30) and the implementation gate (handoff §101) stay; neither is passed by an unrelated "continue" |

## Platform-facing sections and their owners

Every other section is a builder rule: it governs Claude's work and needs no platform requirement.

| Section | Topic | Requirements that own it | Note |
|---|---|---|---|
| §26, §35 | One responsibility, one authority; one name per authority | ARCH-027, ARCH-037, ARCH-016 | Names mapped in the glossary and the source-of-truth map |
| §27, §28, §29 | No duplicate database, event bus, queue, or agent | GOV-014, GOV-020, AGT-002, ARCH-016 |  |
| §30 | One calculation authority for fees, slippage, sizing, capital, exposure, P&L, net profit | ARCH-003, QNT-005, QNT-006, TNP-018, LED-006 |  |
| §36 | One meaning per state name; documented boundaries between state machines | HLT-011, RSK-015, RDY-007, RDY-017, STR-024 | Names shared by several machines: TC-10 |
| §37 | No hidden behavior: no silent retries, capital movement, risk or strategy change, fallback, or AI authority | PLT-027, ARCH-029, PRT-003, ARB-009, EXA-014 | SR-45 |
| §38, §39 | Financial calculation integrity; no floating-point negligence | ARCH-010, ARCH-011, TEC-003, EXE-002 |  |
| §40, §42 | Security; production credentials never in code, Git, documents, unrestricted AI, logs, or fixtures | SEC-005, SEC-004, SEC-008, SEC-009, OPS-016 |  |
| §41 | Research, paper, staging, canary, production separated | OPS-004, OPS-013, MODE-006, PAP-011, PAP-013, SEC-004 | Canary is separated as a production stage with its own controls (OPS-013, STR-020), not as an environment |
| §43 | No unsafe fast path | PERF-023, RSK-034 | PERF-023 new (gap) |
| §44 | Measured performance (p50, p95, p99, throughput, latencies) | PERF-010, PERF-012, PERF-018, PERF-020, VER-001 |  |
| §45, §46 | Concurrency; atomic capital reservation | PERF-013, PERF-022, CAP-027 |  |
| §47 | SUCCESS, FAILURE, TIMEOUT, UNKNOWN; unknown is never success | ARCH-042, EXE-005, EXE-006, EXE-009 | ARCH-042 new (gap: balance, position, connectivity) |
| §48 | Reconcile before resuming after restart, failure, migration, failover, restore, deployment switch | REC-003, REC-015, REC-023, REC-028, MIG-018, REC-025 |  |
| §49 | One active execution instance; no local and server trading together | REC-013, REC-019, EXE-010, MIG-030 |  |
| §61 | Configuration changes to risk, capital, execution, strategy, security, production, AI budgets, or permissions are controlled | OPS-020, OPS-007, POL-005 |  |
| §76 | Each machine-enforceable rule names its owner, enforcement point, violation response, and verification | ARCH-038, ARCH-039 | The System Rules Register |
| §77, §171 | AI authority firewall; AI provides intelligence, deterministic infrastructure authority | PLT-016, ARCH-019, AIL-003 |  |
| §78 | AI failure keeps the system safe | AIL-011, AIL-012, AIL-018 |  |
| §79 | No live behavior change because an AI suggested it, a loss, a missed trade, or a new pattern | STR-002, STR-009, STR-027, HLT-016 |  |
| §80, §172 | Search broadly, filter strictly, validate rigorously, execute selectively | PLT-022, OPP-017, OPP-018 |  |
| §81 | No forced trading; NO TRADE is valid | RSK-044, RSK-031, RSK-032, CAP-036 |  |
| §82, §169 | Capital preservation first; financial correctness over convenience | PLT-006, PLT-009 |  |
| §83 | No guaranteed-return logic | PLT-005, PLT-007, CAP-013, TNP-014 |  |
| §84 | No daily profit ceiling unless policy requires it | TNP-026, TNP-012, TNP-013 |  |
| §96 | Performance work checked for races, staleness, lost events, risk bypass | PERF-022, PERF-021, PERF-023 |  |
| §97, §98, §99 | Regression; negative paths; recovery is tested | GOV-006, GOV-012, VER-003 |  |
| §100 | Backups restored in tests; reconcile after restore | RMP-010, MIG-024, MIG-022, MIG-028, REC-028 |  |
| §101 | Migration safety | MIG-012, MIG-018, MIG-023, MIG-024 |  |
| §102, §103 | Deployment safety; rollback | REC-013, MIG-011, MIG-027, SEC-004, GOV-006, OPS-012 |  |
| §104 | Canary eligibility is not permission to trade | RDY-015, RDY-016, STR-013, STR-020, STR-022, OPS-011 |  |
| §105 | Production safety gate | RMP-010, RDY-022 |  |
| §106, §173 | No self-authorized production expansion; capital enables capability, not authority | PLT-023, CAP-034, POL-005 |  |
| §107, §108, §109 | Feature lifecycle, completeness, known status | GOV-018, GOV-009, GOV-019, RDY-020 | CF-19, open for the owner |
| §115, §116, §117 | Resource, backpressure, and rate-limit safety | PERF-015, PERF-016, PERF-014, PERF-021, EXA-014 |  |
| §118, §119, §120 | Observability; auditability; reproducibility | MON-001, MON-002, MON-007, MON-009, MON-010, AUD-003, AUD-012, STR-026 |  |
| §122 | No user request overrides safety | RSK-034, RSK-039 |  |
| §139, §140 | Idempotent financial actions; no duplicate execution after resume | ARCH-041, EXE-008, CAP-027, EXE-009, REC-017 | ARCH-041 new (gap: cancellation, capital release) |
| §167 | Every critical state transition has a recovery story | REC-015, REC-016, REC-017, VER-003 |  |
| §168 | When unknown: do not guess | PLT-018, RGM-008, RSK-024 |  |
| §170 | Autonomy within defined authority | PLT-021, RSK-034, SEC-008, STR-002 |  |
| §174 | Readiness requires evidence | RDY-001, STR-018 |  |

## Alternatives considered

- **Merge the four builder texts into one.** Rejected: the owner's texts are kept verbatim (constitution Rule 27; DEC-032, "no silent dropping"), and `CLAUDE.md` forbids restating them. DEC-033 says how they combine instead.
- **One new requirement per platform-facing section.** Rejected: all but three would duplicate existing requirements (constitution Rule 30). Only the three statements without a full home became requirements.
- **Move the project state to `docs/00-project/`.** Rejected: §03 allows another designated location, and the move would break links for no gain.
- **Decide the feature lifecycle now (CF-19).** Rejected: the two models are both the owner's input and differ in substance; the choice is the owner's.

## Consequences

- `CLAUDE.md` loads all four builder texts in every session.
- Every checkpoint leaves a verification record in the format of the [traceability README](../traceability/README.md), and the project state's continuation contract is updated at every checkpoint and before a session ends.
- New: ARCH-041, ARCH-042, PERF-023; SR-46, SR-47; CF-19 (open), DUP-39 (resolved), TC-10 (open).
- Verification is repeatable from the repository (§22): the checker now also fails if a preserved text changes ([`preserved-texts.sha256`](../../tools/docs/preserved-texts.sha256)) or a document is orphaned (§71, §73), and `tools/docs/selftest.py` runs the negative tests that were only in the builder's scratch area before.
- Nothing here authorizes implementation (handoff §101; constitution Rules 134–135).
