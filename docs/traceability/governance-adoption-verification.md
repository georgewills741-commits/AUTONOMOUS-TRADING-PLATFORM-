# Governance Adoption — Verification Record

> **Status:** ACTIVE record of the checkpoint that adopts the master execution constitution and the owner's directive on verification and platform independence ([DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md), [DEC-034](../decisions/DEC-034-verification-and-platform-independence.md)). Format: [traceability README](README.md). Made under the three-gate procedure of DEC-033.

## Identity

- **Date:** 2026-10-01
- **Stage:** FOUNDATION — documentation initialization (before Stage 1)
- **Starts from:** commit `5846675` (the integrity checkpoint). This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope

| Change | Files |
|---|---|
| Two texts received on 2026-10-01, kept verbatim as ACTIVE builder texts | [master execution constitution](../builder/master-execution-constitution.md), [directive](../builder/verification-and-platform-independence-directive.md) |
| `CLAUDE.md` loads all four builder texts | `CLAUDE.md` |
| Decisions | DEC-033, DEC-034; the [decision log](../decisions/README.md) |
| 8 new requirements, no existing one changed | PLT-029 ([platform overview](../product/platform-overview.md)); OPS-021 ([deployment and operational readiness](../operations/deployment-and-operational-readiness.md)); GOV-021 to GOV-023 ([architecture governance](../architecture/architecture-governance.md)); ARCH-041, ARCH-042 ([architecture overview](../architecture/overview.md)); PERF-023 ([performance](../architecture/performance-and-latency.md)) |
| System rules | SR-46, SR-47; ARCH-042 added to SR-09 ([System Rules Register](../requirements/system-rules-register.md)) |
| Findings | CF-19 (open, for the owner), DUP-39 (resolved) in the [findings register](../conflicts/register.md); TC-10 (open) in the [open-question register](../open-questions/register.md) |
| Terminology and authorities | [Glossary](../glossary.md) (constitution's authority names; shared state names); [source-of-truth map](../architecture/source-of-truth-map.md) |
| Records | Continuation contract in the [project state](../project-state.md); verification-record format in the [traceability README](README.md); roadmap additions of 2026-10-01 |
| Tooling | `build_index.py` also checks that preserved texts are unchanged (`tools/docs/preserved-texts.sha256`), status-banner links of preserved texts, and orphaned documents; `tools/docs/selftest.py` (negative tests); tools README |
| Generated | `docs/requirements/registry.md`, `docs/traceability/handoff-coverage.md` (rebuilt by `build_index.py`) |

Out of scope: any platform code, configuration, schema, or infrastructure (none exists; implementation is not authorized); CF-19's decision (the owner's).

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | Wording of the two new texts | Round trip of the repository copies against the texts as received (kept in the session's scratch area at receipt): word sequence and line by line; the constitution's sections §00 to §184 all present, in order | PASS: 7,083 and 1,283 words identical; every non-blank line identical (the constitution's two-line title is joined in its heading). Blank lines differ only as each banner's formatting note states |
| 2 | Generated files current; references, links, coverage, system rules, decisions; preserved texts unchanged; no orphans | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 731 requirements, 47 prefixes, 95 findings, 34 decisions, 34 systems, 47 system rules |
| 3 | No requirement lost, reworded, or reclassified | `python3 tools/docs/compare_requirements.py 5846675 --strict` | PASS (exit 0): 8 added (ARCH-041, ARCH-042, GOV-021, GOV-022, GOV-023, OPS-021, PERF-023, PLT-029), 0 removed, 0 changed |
| 4 | The tools still fail on broken input | `python3 tools/docs/selftest.py` | PASS: an unmodified copy passes; 20 broken copies rejected by the checker (among them the reviewer's attacks: a `>` line after a banner, a file in a subdirectory or of another type, CR LF line endings, two documents linking only to each other, a link only inside inline code); a banner-only change accepted; 3 broken copies rejected by the comparison |
| 5 | Preserved texts were unchanged before the manifest recorded them | Hash of each preserved text (as `build_index.py` defines it) at the commit that added it vs now; `git log` per file | PASS: each existing preserved text has been touched by exactly one commit, the one that added it, and its hash is unchanged |
| 6 | Code checks of the tools | `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS |
| 7 | Every link in every Markdown file, including `CLAUDE.md`, the root README, and the preserved texts' banners | Link resolution over all Markdown files | PASS: none broken |
| 8 | Coverage of the constitution's platform-facing sections | Every requirement ID in DEC-033's table checked to exist and to be approved (CF-19's row excepted, which names GOV-018 because it is the conflict) | PASS: 41 rows, 61 sections |
| 9 | Secrets, local paths, stray files | Pattern scan of tracked and new files; `git status --short --ignored`; `git diff --check` | PASS: no secret or local path; the only e-mail-like string is the dummy identity `selftest@localhost` that the self-test gives its temporary git repository; only intended files; whitespace clean. (The scan's "TODO" hit is the [integrity record](integrity-verification-2026-10-01.md)'s own description of that check.) |

Environment: Python 3.11, ruff 0.15.8, mypy 1.19.1, git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 to 9 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | PASS: an independent reviewer and the builder's own separate pass, below |

### Gate 2 — architecture and consistency (builder)

- **Ownership:** each new requirement sits in the specification that owns its prefix; no new system; the System Rules Register stays an index (DUP-38): SR-46 and SR-47 name canonical requirements and restate none.
- **Duplicates and conflicts:** DEC-033's table maps the constitution's other platform statements to existing owners instead of copying them (the requirements from decisions sit under "Decisions applied" headings, as the requirement conventions say); CF-19 and DUP-39 record the two overlaps found; GOV-022 refers to GOV-002's gate rather than repeating it.
- **Terminology:** the constitution's authority names are aliases in the glossary, and Capital Manager, Capital Controller, and Capital Engine are marked "do not use"; state names shared across state machines are tracked as TC-10.
- **Unchanged decisions:** no requirement, decision, or verbatim text changed; the SR-09 row only gained ARCH-042 and DEC-033.
- **Project memory:** the project state's continuation contract, gate table, open questions, recent changes, next step, and checkpoint log are current; `CLAUDE.md` loads all four builder texts; every new document is listed in the [documentation index](../README.md).

### Gate 3 — independent review

**Independent reviewer** (a separate review agent that did not write the change; read-only on the repository, experiments on copies; repository status unchanged afterwards): **PASS, no blocking finding.** It compared both texts with the texts as received using its own scripts, rendered them with a CommonMark parser to rule out accidental lists, headings, or emphasis, recomputed the manifest hashes, spot-checked 31 of DEC-033's then 36 coverage rows, re-ran every tool, and attacked the new checks. Its 10 non-blocking findings, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| 1 | `CLAUDE.md` and DEC-033 narrowed the gates to "every significant change", while DEC-032 says everything built, modified, or approved | Both now state DEC-032's scope |
| 2 | Five new requirements sat under "Handoff Part 3 applied" headings, against the requirement conventions; the governance document's lead-in still named two builder texts and Part 3 only | Moved under "Decisions applied (2026-10-01)" headings; GOV-021 to GOV-023 under their own DEC-034 heading; lead-in corrected |
| 3 | GOV-022 changed the source's modal verbs ("should treat", "must NOT assume") and left out the section's inspection list | GOV-022 rewritten with the source's verbs and the whole section, inspection list included; DEC-034 updated |
| 4 | The preserved-text check skipped a `>` line placed after the banner, files in subdirectories or of other types, and line-ending changes | Banner redefined as the first block of `>` lines; every file under the two directories is covered; files read byte-exact; self-test cases added for each |
| 5 | The orphan check accepted two documents linking only to each other, and links inside inline code | Now requires reachability from the entry points and ignores inline code; self-test cases added |
| 6 | The constitution's formatting note missed that §49's `+` flow lost its blank lines; the directive's note missed five added blank lines | Both notes corrected (banner-only edits, outside the preserved hash) |
| 7 | TC-10 cited REC-013 and STR-022, which do not define states, and missed RDY-011's DEGRADED | TC-10, the glossary entry, and the project state corrected |
| 8 | DEC-033's §118 row cited HLT-010 instead of the monitoring requirements; §100's row missed RMP-010 and MIG-024; §36, §37, §61, §76, and §167 had owners but no row | Rows corrected and added: 41 rows, 61 sections |
| 9 | The project state's open-question lead-in credited CF-19 and TC-10 to DEC-031 | Credits DEC-033 |
| 10 | This record said "no e-mail address" and "lines identical" without qualification | Checks 1 and 9 qualified |

**Builder's own separate pass** (after the fixes): re-ran checks 1 to 9 (all PASS; the self-test now runs 26 cases); confirmed that every line the diff removes outside generated files is a deliberate replacement; re-read DEC-033, DEC-034, the moved requirement sections, and the continuation contract; `git status --short --ignored` shows only the intended files and ignored caches.
