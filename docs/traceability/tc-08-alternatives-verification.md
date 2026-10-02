# TC-08 Alternatives — Verification Record

> **Status:** ACTIVE record of the checkpoint that adds an "Alternatives considered" section to the older decision records, as the owner decided for TC-08 on 2026-10-02 ([DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)). Format: [traceability README](README.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md).

## Identity

- **Date:** 2026-10-02
- **Stage:** FOUNDATION — documentation initialization (before Stage 1)
- **Starts from:** commit `0b3f97a`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope

The owner's choice (Q5 of [owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md)): "The builder goes through DEC-001 to DEC-030 now and adds Alternatives wherever the repository shows what was considered; records with no sourced alternatives say so."

**What counts as sourced.** An alternative is listed only if the repository records it in one of five ways:

- an option shown to the owner (owner decisions 3);
- a proposal, candidate, or "other option" in the [findings register](../conflicts/register.md) or the [open-question register](../open-questions/register.md);
- the side of a finding that the decision did not choose;
- an option the record itself names and rules out or defers (for example the builder's recommendation in DEC-007's Context, or "No new system is created" in DEC-017);
- an earlier version of a document, in the repository's git history (for example the roadmap at `b850eaa` for DEC-016).

A prohibition in the owner's own texts is a requirement and stays in its owning specification. It is also listed as an alternative only where the owner's text explicitly sets the unwanted approach against the wanted one ("you do not want", "rather than", "merely because", "nor"); those were found by searching the owner's texts for these forms.

Each bullet names its source. A reason is given only where a source states one; where the owner chose, the owner's choice is the reason. Nothing comes from memory or from conversation history outside the repository (constitution Rule 181).

| Change | Files |
|---|---|
| "Alternatives considered" added, placed before "Consequences" or at the end, each opening with a line that says when and why it was added | DEC-002, DEC-004, DEC-005, DEC-007, DEC-008, DEC-010 to DEC-013, DEC-015 to DEC-030 (25 records) |
| Records that already had the section, checked against the same sources | DEC-003 and DEC-009 gained one alternative each, under a line marking the addition; DEC-001, DEC-006, and DEC-014 unchanged |
| TC-08 resolved | [Open-question register](../open-questions/register.md) (status line and TC-08 row) |
| Notes brought in line | [Architecture governance](../architecture/architecture-governance.md) (ADR note); [decision log](../decisions/README.md); DEC-031's and DEC-035's status lines; the "Later changes" note of the [owner decisions 4 record](owner-decisions-04-verification.md); the P3§474 row of the [Part 3 reconciliation](part-3-reconciliation.md); [roadmap](../roadmap/roadmap.md) header; [documentation index](../README.md) |
| Project memory | [Project state](../project-state.md): gate table, current objective, continuation contract, completed work, recent decisions and changes, next approved step (with the observations below), checkpoint log (0b3f97a filled in) |
| Records | This record; the [traceability README](README.md) and the documentation index list it |

In all 30 records only lines were added; nothing in their earlier text changed (check 7).

Out of scope: any change to a decision, requirement, finding, or verbatim text; the complete documentation review (next); any platform code (none exists; implementation is not authorized).

### Where each record's alternatives come from

| Record | Sources of its alternatives |
|---|---|
| DEC-001 | Its own section, unchanged; nothing further recorded |
| DEC-002 | The record's "Deviations from the §99 target" table and Context; CF-07 |
| DEC-003 | Its own section; added: CF-10's other side |
| DEC-004 | The record's Context (handoff §00 item 7); constitution Rule 22 |
| DEC-005 | The record's title and Context (handoff §00 items 18–19; constitution Rules 56–58) |
| DEC-006 | Its own section, unchanged; it already covers OQ-01, OQ-02, and DUP-17 |
| DEC-007 | The record's Context (the builder recommended spot only); OQ-04 |
| DEC-008 | OQ-03 and EXA-002 (the three venues previously discussed); TC-05 |
| DEC-009 | Its own section; added: the record's "Retention" paragraph (external vendors FUTURE), OQ-22 |
| DEC-010 | CF-01, CF-02, CF-03, CF-09 (the conflicting readings and the proposals as first written); DUP-19 |
| DEC-011 | The claimants and proposals of DUP-01 to DUP-22 (unchanged since first recorded); DUP-10 and TC-03 (ranking owner left open); OQ-10 |
| DEC-012 | DUP-04's claimants and candidate; the record's Context; OQ-07 and HLT-001 (§74's states) |
| DEC-013 | DUP-11 to DUP-15 (the register's other options and claimants); TC-02; CF-04's proposal and OQ-12; AIV-008 (§66's policies); the record's own note on the premium threshold |
| DEC-014 | Its own section, unchanged; it already covers TC-01; TC-04's recommendation was adopted |
| DEC-015 | CF-08, OQ-15 (§98's two policy locations); OQ-08 |
| DEC-016 | CF-05, CF-06 (the §95 mapping as written); the roadmap and dependency map at `b850eaa` (the PROPOSED parallel trading stages) |
| DEC-017 | The record ("No new system is created") |
| DEC-018 | None recorded; the record says so |
| DEC-019 | The record's Context (the five operating defaults shown to the owner); OC-1's explicit contrasts (items 1, 9, 21, and its closing note) |
| DEC-020 | The record's Context ("rather than by redefining §96") |
| DEC-021 | CF-11 (the rule in force, the risk of fully automatic reset, the builder's proposal); the owner's answer ("merely because") |
| DEC-022 | CF-12 (the two orders and the builder's proposal); REC-014's wording |
| DEC-023 | CF-13's proposal (including "APPROVAL is always human"); the record's Placement paragraph |
| DEC-024 | The record's Decisions 1 to 4 (CF-15, CF-16, DUP-23 to DUP-31, naming) |
| DEC-025 | The record's Context; the [Part 1 verification record](part-1-verification.md) (why the checks were first kept out) |
| DEC-026 | Q1's options in owner decisions 3; CF-14 |
| DEC-027 | Q2, Q3, Q4, Q8, Q10's options in owner decisions 3 |
| DEC-028 | Q6's options and option text ("rather than fixed in code") in owner decisions 3; the owner's answer; the record's Placement paragraph |
| DEC-029 | Q7's options in owner decisions 3 |
| DEC-030 | Q5's and Q9's options in owner decisions 3; TC-07's candidates; the record's Notes (the builder's, labelled as such) |

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | Every record from DEC-001 to DEC-030 has exactly one "Alternatives considered" section | `grep -c '^## Alternatives considered$'` on each of the 30 files | PASS: 30 of 30 have exactly one |
| 2 | Each alternative matches its source | Each bullet read against the source named in it and in the table above | Builder's reading, then Gate 3 (below) |
| 3 | The DUP proposals cited for DEC-011 are as first recorded | Script comparing the first four columns of DUP-01 to DUP-22 at `b850eaa` with the current register | PASS: all 22 identical |
| 4 | No recorded alternative missed in git history | `git grep -n -i "RECOMMENDED\|recommend\|PROPOSED\|proposal\|candidate\|option" b850eaa -- docs` (outside the verbatim texts); the project state at each checkpoint commit from `9fdbc3f` to `a2c8e92`, searched for recommendations and options; `git log -p` of every decision record | PASS after the fixes below. The first pass had not searched history (failure 1 below). The sweep found DEC-016's PROPOSED parallel stages (also found by Gate 3) and the reason for DEC-025's earlier practice. Every other recommendation found matches the decision taken or is already listed: the proposed placements at `b850eaa` match DEC-016's table, the recommendations at `b6f005e` match the options shown in owner decisions 3, and the defaults at `9fdbc3f` are DEC-019's Context. No decision record ever lost a line other than status and header lines (Status, Resolves, Raises, Later changes) and DEC-003's sentence that OQ-23 awaited confirmation; none of them held an alternative |
| 5 | Generated files current; references, links, coverage, system rules, preserved texts, orphans | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 733 requirements, 47 prefixes, 95 findings, 35 decisions, 34 systems, 47 system rules |
| 6 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py 0b3f97a --strict` | PASS (exit 0): 0 added, 0 removed, 0 changed |
| 7 | The decision records only gained lines | `git diff --numstat -- docs/decisions/` | PASS: 0 lines removed from DEC-001 to DEC-030; DEC-031 and the decision log have one line each replaced by a longer one; DEC-035 one line added |
| 8 | The tools still fail on broken input | `python3 tools/docs/selftest.py` | PASS: 34 cases |
| 9 | Code checks of the tools (unchanged) | `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS |
| 10 | No stale statement about TC-08 | Sweep of every active document for "TC-08", "next checkpoint", and "alternatives"; each hit judged | PASS: remaining hits are accurate; or historical text under an updated status line or "Later changes" note (DEC-031's body, DEC-035's body, the Part 3 and owner decisions 4 verification records); or the TC-08 register row's Concern text, kept as raised, as the register does for every resolved item |
| 11 | Hygiene | `git diff --check`; `git status --short --ignored` | PASS: whitespace clean; only intended files; ignored caches only |

Environment: Python 3.11, ruff 0.15.8, mypy 1.19.1, git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 and 3 to 11 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | PASS on the re-run, after the first review failed (1 blocking) and was fixed; see below |

### Gate 2 — architecture and consistency (builder)

- **Applied as the owner chose:** every record from DEC-001 to DEC-030 states the alternatives the repository records; the one record with none (DEC-018) says so. No recommendation was turned into a decision, and no decision changed.
- **No invented history:** every alternative names its source. Where a source exists but is incomplete, the section says so (DEC-007 and DEC-008, whose questions are not recorded; DEC-021 to DEC-023, whose options are not recorded). A builder's reading is labelled as one (DEC-023, DEC-030).
- **One source of truth:** the sections cite the registers and the owner's recorded answers rather than restating them in full; the registers stay the record of each finding.
- **Project memory:** TC-08 is RESOLVED in the register; the project state, decision log, governance note, index, and roadmap say it is done; the next step is the complete documentation review.

### Gate 3 — independent review

**First review: FAIL.** An independent reviewer (a separate agent that did not write the change; read-only on the repository, experiments on copies; repository status unchanged afterwards) checked 75 bullets and DEC-018's line against their sources, the decision text, the tools, the stale-statement sweep, and hygiene. It found 66 bullets accurate, 8 with non-blocking issues, and 1 false:

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | DEC-016 said "No other stage order was recorded", but the roadmap and dependency map at `b850eaa` PROPOSED parallel trading stages; this record's check 2 and Gate 2 were therefore untrue | BLOCKING | Bullet replaced with the PROPOSED parallel stages, quoted, with "No reason is recorded"; git history added to the criterion; check 4 added |
| 2 | DEC-007 called the three types "this record's reading" of the owner's "all", while the record states them as fact; DEC-008 treated a similar answer as fact | Non-blocking | Both reworded neutrally: the decided scope, and that the question put to the owner is not recorded; the scope point is named in the project state's next step |
| 3 | DEC-011 cited §09 for ranking, which §09 does not mention, and left out the §17 quality dimensions DUP-10 lists | Non-blocking | Reworded to DUP-10's list, with "opportunity ranking" quoted from §43 and §06; the §17 dimensions noted as kept (TNP-021) |
| 4 | DEC-012 said no other owner was put forward, though DUP-04 lists claimants | Non-blocking | The claimants (§25, §27, §47, §74, and the undefined "global safety architecture") are now the alternative not taken |
| 5 | DEC-013 did not cover DUP-14, DUP-15, or OQ-12 | Non-blocking | DUP-14 bullet added; DUP-15 and OQ-12 named in their bullets; OQ-12 in the "no other alternatives" line |
| 6 | DEC-022 stated the owner's answer more strongly than REC-014 | Non-blocking | REC-014's wording quoted |
| 7 | DEC-023 cited "Consistency" for a claim that section does not make | Non-blocking | Labelled as the builder's reading |
| 8 | DEC-003's existing section missed CF-10's other side, though the owner's choice covers DEC-001 to DEC-030 | Non-blocking | Added under a line marking the addition; the builder then checked the other four existing sections and added DEC-009's deferred external data vendors the same way |
| 9 | This record lacked "Failures and fixes"; check 10 did not name the TC-08 Concern text; Gate 1 counted check 2; observation 2 was not in the project state | Non-blocking | All fixed |

**Re-run: PASS, no blocking finding.** A second independent reviewer (another separate agent, same read-only rules; an earlier attempt stopped on a usage limit before reporting and changed nothing) confirmed all nine fixes above with their sources, checked all 77 added bullets in the 27 changed records and DEC-018's line against their sources, re-swept the registers and project states in git history, verified every "none recorded" claim, re-ran every tool, and found the repository clean. Its 7 non-blocking findings, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| 1 | DEC-030 left out an option its own Notes defer: where the lease lives (a replicated database or an external coordinator) | Added as deferred |
| 2 | Check 4 said no decision record lost anything but status lines; header lines and DEC-003's OQ-23 sentence were also replaced | Check 4 reworded; none of those lines held an alternative |
| 3 | DEC-005 said the findings were resolved by DEC-006 to DEC-018; the register also names DEC-002 and DEC-003 | Now "as the registers show" |
| 4 | DEC-009's added line said its bullet was recorded elsewhere; the source is the record's own Retention paragraph | Line corrected |
| 5 | DEC-019 listed only the five defaults, though OC-1 explicitly sets other unwanted approaches against the ones it wants (the same holds for Q6's option text and DEC-028) | The owner's texts searched for explicit contrasts ("you do not want", "rather than", "merely because", "nor"); the hits were added to DEC-019, DEC-021, and DEC-028; the criterion above says how such prohibitions are treated |
| 6 | DEC-030's bullets resting on the builder's Notes were not labelled as builder readings; DEC-008 still credited the venue count to the owner's answer | Labelled "Builder's reading"; DEC-008 worded like DEC-007 |
| 7 | DEC-022 named REC-014 and REC-015 as the replacements; REC-016 also replaces REC-011 | Now REC-014 to REC-016 |

**Builder's own separate pass** (after these fixes): re-ran checks 1 and 3 to 11; re-read every changed bullet against its source (OC-1 items 1, 9, 21 and its closing note; owner decisions 2 and 3; RSK-017, RSK-023, STR-014, STR-018, CAP-023, CAP-029, REC-016); `git status --short --ignored` shows only the intended files and ignored caches.

## Failures and fixes

| # | Failure | Cause | Fix | Re-run |
|---|---|---|---|---|
| 1 | A sourced alternative was missed and a "none recorded" claim was false (DEC-016) | The first pass took its sources from the current registers and records only; earlier versions in git history were not searched | History sweep (check 4) over every earlier version; DEC-016 corrected; DEC-025 gained the recorded reason for its earlier practice | Check 4 PASS; Gate 3 re-run PASS |
| 2 | Eight bullets overstated, mis-cited, or left something out (Gate 3 findings 2 to 8) | Wording checked against the decision rather than against the cited source | Each bullet re-read against its source and fixed as listed above | Gate 3 re-run PASS |
| 3 | Seven smaller gaps found by the re-run (its table above), among them alternatives the owner's own texts set against the chosen approach | Owner prohibitions had been treated as requirements only | Explicit contrasts searched for and added; the criterion now states the rule; the rest fixed as listed | Checks 1 and 3 to 11 re-run, PASS |

## Observations for the documentation review

Found while doing this work; neither blocks this checkpoint:

1. **The owner's first-round answers are not recorded verbatim.** DEC-006 to DEC-009 hold the owner's answers only as short quotes or summaries, and the questions asked are not in the repository. Later rounds have verbatim records under `docs/handoffs/`. For DEC-007 this means the repository cannot show whether "all" covered OQ-04's "other derivatives"; the decided scope is the three types in PLT-011.
2. **The options listed with CF-11 to CF-13 are not recorded.** [Owner decisions 2](../handoffs/owner-decisions-02-cf-11-to-cf-13.md) keeps the questions and the owner's free-text answers, not the options shown; DEC-021 to DEC-023 say so.

Both are named in the project state's next step, the complete documentation review.

## Final status

**PASS.** All three gates passed. Gate 3 passed on its re-run; every finding of the two reviews (1 blocking, 15 non-blocking) is fixed. TC-08 is RESOLVED. Remaining: the two observations above, for the complete documentation review, which is next; TC-09 and TC-10 stay open until their stages are planned. No decision, requirement, or finding changed. No platform code exists; implementation is not authorized.
