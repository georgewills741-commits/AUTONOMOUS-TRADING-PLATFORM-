# Owner Decisions 4 — Verification Record

> **Status:** ACTIVE record of the checkpoint that applies the owner's answers of 2026-10-02 on the Part 3 findings and the Part 3 review ([DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)). Format: [traceability README](README.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md).

## Identity

- **Date:** 2026-10-02
- **Stage:** FOUNDATION — documentation initialization (before Stage 1)
- **Starts from:** commit `3b6f372`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope

| Change | Files |
|---|---|
| The owner's eight answers, kept verbatim (HISTORICAL) | [owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md) |
| Decision | DEC-035; [decision log](../decisions/README.md); DEC-031's status (confirmed by the owner) |
| CF-17: security above the user's hard policy | RSK-049 added and RSK-048 replaced (class only) in the [Risk Engine](../risk/risk-engine.md); SR-02 in the [System Rules Register](../requirements/system-rules-register.md); [architecture overview](../architecture/overview.md), [source-of-truth map](../architecture/source-of-truth-map.md), [roadmap](../roadmap/roadmap.md) references |
| CF-19: canonical feature lifecycle | GOV-024 added and GOV-018 replaced (class only) in [Architecture governance](../architecture/architecture-governance.md); [glossary](../glossary.md); roadmap |
| CF-18, DUP-34, DUP-35 confirmed; OQ-27 answered; TC-08 decided | [Findings register](../conflicts/register.md), [open-question register](../open-questions/register.md); TC-10 and the glossary note the names the feature and strategy lifecycles share |
| Part 3 approved | [Project state](../project-state.md) (gate table, continuation contract, open questions, next step, checkpoint log), [documentation index](../README.md) |
| Tooling | `compare_requirements.py --expect-changed=ID,ID` (a decided change passes only if exactly the listed requirements changed); three self-test cases for it; manifest line for the new verbatim record; tools README |
| Brought in line with the decisions (found by the Gate 3 reviews) | [Policy system](../systems/policy/policy-system.md), [capital management](../systems/capital-management.md), [readiness system](../systems/readiness-system.md), [security architecture](../security/security-architecture.md), [system registry](../architecture/system-registry.md), [platform overview](../product/platform-overview.md), [Part 3 reconciliation](part-3-reconciliation.md), DEC-033 (status and §107 row), the "Later changes" notes in the [Part 3](part-3-verification.md) and [governance adoption](governance-adoption-verification.md) records, the [traceability README](README.md) |
| Generated | `docs/requirements/registry.md`, `docs/traceability/handoff-coverage.md` |

Out of scope: TC-08's work (adding alternatives to DEC-001 to DEC-030), which is the next checkpoint; any platform code (none exists; implementation is not authorized).

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | The verbatim record matches what was asked and answered | Every label shown, question, option (label and description), and chosen answer in the record compared with the AskUserQuestion calls and results in the session transcript, by script | PASS: 8 of 8 labels, questions, all options, and all 8 answers identical; the owner added no notes |
| 2 | Generated files current; references, links, coverage, system rules, preserved texts, orphans | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 733 requirements, 47 prefixes, 95 findings, 35 decisions, 34 systems, 47 system rules |
| 3 | Only the decided requirement changes | `python3 tools/docs/compare_requirements.py 3b6f372 --strict --expect-changed=GOV-018:cls,RSK-048:cls` | PASS (exit 0): added GOV-024, RSK-049; changed GOV-018 and RSK-048 in their class only (to DEPRECATED / REPLACED), which the tool now checks per field; nothing removed; nothing else changed |
| 4 | The tools still fail on broken input | `python3 tools/docs/selftest.py` | PASS: 34 cases, including eight for `--expect-changed` (accepts the listed change and a listed class-only change and a listed removal; rejects an extra change, a missing one, a reworded text where only a class change is listed, a removal where only a change is listed, and a duplicated entry) |
| 5 | Code checks of the tools | `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS |
| 6 | No stale statements | Sweep of every active document, the Part 2 and Part 3 reconciliation maps included, for "awaiting", "awaits", "asked to confirm", "for the owner", "second only to system safety", GOV-018 described as proposed or current, and "in progress"; each hit judged historical or stale | PASS after the fixes of both reviews below. The first sweep wrongly left out the reconciliation maps as historical; they are active traceability maps and are now updated. Remaining hits are accurate statements, historical records (earlier verification records with "Later changes" notes; DEC-031's and DEC-033's bodies under updated status lines), the generated decision table of [handoff coverage](handoff-coverage.md) (DEC-031 → RSK-048, RDY-026), and the roadmap's FOUNDATION stage status, correctly in progress |
| 7 | Hygiene | `git diff --check`; `git status --short --ignored`; every removed line outside generated files reviewed | PASS: whitespace clean; only intended files; every removed line is a deliberate update |

Environment: Python 3.11, ruff 0.15.8, mypy 1.19.1, git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 to 7 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | PASS on the second re-run, after the first review (3 blocking) and the first re-run (1 blocking) failed and were fixed; see below |

### Gate 2 — architecture and consistency (builder)

- **Each answer applied once, where it belongs:** CF-17 in the Risk Engine (the owner of precedence) and SR-02; CF-19 in Architecture governance; confirmations and answers in the registers; nothing else changed meaning.
- **Replaced, never deleted:** RSK-048 and GOV-018 keep their wording with class DEPRECATED / REPLACED and name their replacements; SR-02 no longer rests on a replaced requirement (the checker enforces this).
- **Consistency:** RSK-004's layers keep their order inside RSK-049; GOV-024 states exactly the option the owner chose for CF-19 (the GOV-009 relation is a labelled builder reading); the shared lifecycle names are added to TC-10 rather than silently merged.
- **Roadmap:** RSK-049 stays in the single stage where RSK-048 was (FOUNDATION row of the Part 3 table); GOV-024 is in FOUNDATION.
- **Project memory:** the continuation contract, gate table, open questions (only TC-09 and TC-10, both deferred by design), next step (TC-08), and checkpoint log are current.

### Gate 3 — independent review

**First review: FAIL.** An independent reviewer (a separate agent that did not write the change; read-only; experiments on copies) confirmed the fidelity of the verbatim record, the tooling, and hygiene, but found active documents that contradicted DEC-035. Findings and fixes:

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | Active documents still said the owner's answers were pending: the roadmap header and FOUNDATION status, SR-20 and SR-26, the CF-18 note in capital management, the CF-17 and DUP-35 notes in the Risk Engine | BLOCKING | All updated to the owner's decisions |
| 2 | The policy system still said user hard constraints rank second only to system safety | BLOCKING | Now: below system safety and security (RSK-004, RSK-049) |
| 3 | GOV-018 was still described as proposed or current in the roadmap, the system registry, the readiness status table, and DUP-32 | BLOCKING | All point to GOV-024, which replaced it |
| 4 | This record claimed project memory was current, had no stale-statement check, and lacked "Failures and fixes" and "Final status" | Non-blocking | Check 6 added; this section and "Final status" added |
| 5 | GOV-024 carried two sentences the owner had not chosen (GOV-009's statuses inside DEPRECATED and RETIRED; every feature has a known status), and three places attributed them to the owner | Non-blocking | GOV-024 now states only the chosen option; the GOV-009 relation is a labelled builder reading; attributions corrected |
| 6 | A DEC-035 reading note compared a security change with RSK-039's procedure, which the owner had not said | Non-blocking | Reworded: the procedure is specified with the security and policy design |
| 7 | `--expect-changed` checked only which IDs changed, not how (a rewording or a removal of an expected ID passed) | Non-blocking | Per-field expectations (`ID:cls`, `ID:removed`); four more self-test cases |
| 8 | TC-08 was labelled "in progress" in some places and "nothing in progress" in others | Non-blocking | "Next — not started" everywhere |
| 9 | Earlier records had no pointer to the owner's later decisions | Non-blocking | DEC-033's status, and "Later changes" notes in the Part 3 and governance-adoption verification records |
| 10 | Minor: GOV ranges in the project state, the principles index without RSK-049, no pointer in the security architecture, and the verbatim record without the labels shown above each question | Non-blocking | All fixed; the labels were added and re-verified against the transcript (check 1) |

**First re-run: FAIL.** A new independent reviewer confirmed all ten fixes above, the fidelity of the verbatim record (labels, questions, options, answers), GOV-024 and RSK-049 against the chosen options, the tools (including attacks on the per-field `--expect-changed`), and hygiene. It found:

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | The Part 3 reconciliation map still called GOV-018 PROPOSED (P3§509), traced P3§471 only to the replaced RSK-048, and listed CF-17, CF-18, OQ-27, and TC-08 without "since decided"; check 6 was therefore untrue | BLOCKING | Rows for P3§358, P3§471, P3§474, P3§509 and the summary line updated, following the precedent of the Part 2 map; check 6 corrected |
| 2 | The "Later changes" notes named items those records do not list | Non-blocking | Each note now names only that record's open items, and says what was raised later |
| 3 | Banner metadata: Architecture governance's sources lacked DEC-035; the system registry's and source-of-truth map's dates were old | Non-blocking | Updated |
| 4 | DEC-031's "Resolves" line still said "awaiting the owner's confirmation" | Non-blocking | "then awaiting …; since decided, DEC-035" |
| 5 | `--expect-changed` silently kept the last of duplicated entries and read `ID:` as "any change" | Non-blocking | Duplicated or empty entries are refused; one more self-test case |
| 6 | The tools README's comparison section did not explain `--expect-changed` | Non-blocking | Explained there |

**Second re-run: PASS, no blocking finding.** A third independent reviewer confirmed all 16 earlier fixes in the files, swept all 97 active documents (both reconciliation maps included) and found nothing contradicting DEC-035, re-verified the verbatim record against the transcript, confirmed GOV-024 and RSK-049 state only the chosen options, ran every tool, and found the repository clean. Its 6 non-blocking findings, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| 1 | DEC-033's §107 row (and two body lines) still led only to GOV-018 and said "open for the owner" | "since decided: GOV-024 replaced GOV-018 (DEC-035)" added there and in DEC-033's consequences |
| 2 | DEC-031's status (and the decision log) mentioned only the CF-17 change, not that TC-08 was decided differently from DEC-031's recommendation | Both now say so |
| 3 | Architecture governance's scope sentence did not name GOV-024's source, and its ADR note did not mention the owner's TC-08 decision | Both added |
| 4 | This record's Scope table did not list every changed file | Completed (the row above) |
| 5 | The tools README omitted two self-test cases, and an empty item between commas (`A:cls,,B:cls`) was silently skipped | README completed; empty items are now refused too |
| 6 | Check 6 did not say which generated table it meant | Named: the decision table of handoff coverage |

**Builder's own separate pass** (after these fixes): re-ran checks 2 to 7; confirmed the refusal of duplicated, empty, and malformed `--expect-changed` entries by hand; re-read DEC-033's and DEC-031's changed lines and the governance note; `git status --short --ignored` shows only the intended files and ignored caches; `git diff --check` clean.

## Final status

**PASS.** All three gates passed. Gate 3 needed two re-runs; every finding of the three reviews (3 + 1 blocking, 21 non-blocking in total) is fixed. Remaining by design: TC-09 and TC-10 stay open until their stages are planned; TC-08's work is the next checkpoint (not started). No platform code exists; implementation is not authorized.
