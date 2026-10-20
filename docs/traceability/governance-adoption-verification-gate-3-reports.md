# Governance adoption verification — Gate 3 Report

> **Status:** REFERENCE (evidence) — the report of the independent Gate 3 review of the change whose record is [Governance Adoption — Verification Record](governance-adoption-verification.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). It is reproduced in a text block exactly as given; nothing in it was replaced. The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the review. The headings use the record's names for the runs.

## Independent review

- **Reviewer:** a fresh-context subagent, launched 2026-10-01, 23:24 UTC; report given 2026-10-01, 23:37 UTC
- **sha256:** `d5777b1512f7583c91bea3cda8b9162580dae84b4bdccd329d2372ecf24c0d37`, as given and as shown

```text
**Gate 3 verdict: PASS. There are no blocking findings and 10 non-blocking ones.** I recommend fixing findings 1 to 3 before the commit. Each is a small wording or placement fix.

The two texts are word-for-word faithful to what was received. The 8 new requirements match their sources. The registers and counts are consistent, and every tool check passes. The new preserved-text and orphan checks have gaps, but nothing in the repository currently falls into them.

I made no change to the repository. `git status --porcelain` matches the snapshot I took at the start, HEAD is still 5846675, there is no extra worktree, and no stash. All my experiments ran on copies under `.../scratchpad/review4/`, using my own scripts: `fidelity.py`, `render_check.py`, `attack.py`.

## Findings

**1. NON-BLOCKING (fix first): the gate scope is now narrower than DEC-032, without saying so.**
- `CLAUDE.md:7` now says "Every **significant** change … passes the one three-gate verification procedure". The old line said "Every change passes all three verification gates".
- `DEC-033:31` says "The gates apply to every significant change … (DEC-032 is stricter than §14's 'every major stage')".
- DEC-032 itself (line 12) and the rule (`checkpoint-and-verification-rule.md:28`) say "EVERYTHING you build, modify, or approve".
- So the new canonical procedure (the source-of-truth map points to DEC-033) states a narrower scope and credits it to DEC-032. The "stricter applies" clause softens this, but the wording should say "everything built, modified, or approved (DEC-032)".

**2. NON-BLOCKING: the 8 new requirements sit under Part 3 headings.**
- ARCH-041 and ARCH-042 (`overview.md:165-166`), PERF-023 (`performance-and-latency.md:51`), PLT-029 (`platform-overview.md:117`) and OPS-021 (`deployment-and-operational-readiness.md:63`) are under "## Handoff Part 3 applied (2026-09-30)".
- That heading's lead-in says "New requirements from Handoff Part 3, cited as P3§N".
- This breaks `docs/requirements/README.md`: "Requirements from a decision sit under a 'Decisions applied' heading".
- `architecture-governance.md:9` is also stale. It names only two builder texts and says its requirements "are project requirements from Handoff Part 3", but GOV-021 to GOV-023 come from DEC-034.

**3. NON-BLOCKING: GOV-022 changes the source's modal verbs and drops part of its section.**
- `architecture-governance.md:50`: "should treat the request as an upgrade" became "is treated as an upgrade", and "it must NOT assume … rebuilt" became "does not assume". The conventions say modal verbs are kept.
- The directive's "Future development must continue…" section also has a 15-item inspection list and "where the platform currently is before what should happen next". GOV-022 drops both.
- DEC-034 maps that whole section to GOV-022 and does not list the omitted part among the builder rules in its item 3.
- PLT-029, OPS-021, GOV-021, GOV-023, ARCH-041 (§139), ARCH-042 (§47) and PERF-023 (§43) are faithful: same items, order and modal verbs. Classes and owning documents are appropriate.

**4. NON-BLOCKING: the preserved-text check has gaps.** I tried each case on a copy of the working tree.
- **Correctly caught:** a changed body word, a changed title line, a broken banner link, an unlinked new doc, a link that exists only inside a code block, a deleted preserved file, and a malformed manifest line. A banner-only change and extra blank lines after the banner pass, as intended.
- **Not caught (F, F2):** a `>` line inserted between the banner and the body, such as "> NOTE: §52 no longer applies.", or a `>` quote placed before the body. `preserved_body()` skips every `>` or blank line after line 1. No current text has a body starting with `>`, so this cannot hide anything today.
- **Not caught (H, H2):** `docs/builder/extra/override.md` or `docs/builder/override.txt`. Files in a subdirectory, or non-.md files, are skipped by both `md_files()` and `preserved_paths()`. The tools README (line 36) claims "every file under docs/handoffs/ and docs/builder/ is listed".
- **Not caught (K):** converting a preserved text to CRLF. Files are read with universal newlines.

**5. NON-BLOCKING: the orphan check has two smaller gaps.**
- Two docs that link only to each other both pass. The check is "linked from some document", not "reachable from the index".
- A link inside inline code still counts as a link.
- §71 and §73 actually ask for purpose and ownership, so a link check is only a proxy for them.

**6. NON-BLOCKING: the master constitution's formatting note is inaccurate in one place.**
- The note (`master-execution-constitution.md:5`) says blank lines were removed only inside the arrow flows, and that blank-separated lines stay separate paragraphs.
- But §49's blank-separated "LOCAL ACTIVE / + / SERVER ACTIVE" was stacked into a text block (lines 1171-1175). Putting it in a text block was right, since a bare "+" would otherwise render as a list item.
- The directive's formatting note does not mention 5 inserted blank lines, after the three bold VERIFICATION lines and before the two lists. No wording is affected.

**7. NON-BLOCKING: TC-10 is partly inaccurate.**
- REC-013 uses "active" only as an adjective, not as a state named ACTIVE.
- STR-022 says "a blocked / readiness-failed state", lowercase and with the readiness meaning, so it is not really a second state machine.
- TC-10 misses that RDY-011's capability states (ENABLED; LIMITED; DEGRADED; …) are a third use of DEGRADED.
- The other citations are correct: SUSPENDED in RDY-004, RDY-017 and STR-024; DEGRADED in HLT-011 and RDY-017; SAFE MODE in RSK-015 and HLT-001; ACTIVE in GOV-009.
- `project-state.md:184` lists TC-10 without SAFE MODE, while the glossary includes it.
- READY is named in §36 but appears in only one machine (readiness), so leaving it out is defensible.

**8. NON-BLOCKING: two DEC-033 coverage rows are weak.**
- The §118 (observability) row cites HLT-010, which is about who owns platform state. The MON-001 to MON-011 monitoring requirements are not cited.
- §100 says "Backups must be tested for restoration". The row cites REC-028, MIG-022 and MIG-028, but the closer owners are RMP-010 (restore before production) and MIG-024 (simulated restore), which are not cited.
- I spot-checked 31 of the 36 rows. The others map correctly.
- Sections with platform content that are not in the table: §36 (handled by TC-10), §37 (PLT-027, STR-006, SR-45), §61 (OPS-020), §76 (ARCH-038, ARCH-039), §167. All have existing owners, so no requirement is missing.

**9. NON-BLOCKING: CF-19 and DUP-39 are accurate; one heading is mis-attributed.**
- CF-19's state lists match §107, P3§509 (GOV-018) and GOV-009 exactly. It is correctly marked RECOMMENDED — NOT YET APPROVED.
- DUP-39's references are correct.
- The project-state "Open questions" lead-in (`project-state.md:174`) credits every item to DEC-031, but CF-19 and TC-10 come from DEC-033.

**10. NON-BLOCKING: two small inaccuracies in the verification record.**
- Check 9 says there is no e-mail address. `selftest.py:229` contains `selftest@localhost`, a harmless dummy identity for the temporary git repository.
- Check 1's "lines identical" is true for non-blank lines only. Blank lines differ as described in finding 6.
- Every other claim in the record I re-checked and found true: the 7,083 and 1,283 word counts, the counts in checks 2 to 4, 36 rows and 56 sections, and the tool versions.

## Key evidence (commands and outputs)

**Fidelity** (my scripts, comparing the raw texts minus the `=` lines against the repo copies minus the banner and Markdown markers):

| Text | Words | Non-blank lines | Notes |
|---|---|---|---|
| Directive | 1283 = 1283 | 297 = 297, identical | |
| Master constitution | 7083 = 7083 | 2006 = 2006, identical | Title join correct |

- I rendered both copies with CommonMark (markdown-it-py 4.2.0, installed only in scratch). The visible text equals the raw text minus list markers.
  - Each raw `- ` or `N. ` line becomes exactly one `<li>`: 258 in the master constitution, 137 in the directive.
  - Every numbered list in the raw text runs 1, 2, 3… with no gaps, so Markdown's renumbering changes nothing.
  - No list item swallows the next line, and no accidental headings, links or emphasis appear. There is exactly 1 horizontal rule (intended) and 185 section headings. The `[ ]` checklist lines render literally as paragraphs.
- The 10 manifest hashes match my own recomputation. Each existing preserved text is byte-identical to the one commit that added it (16d317c, b850eaa, 419b8da, 03716bf, a9034ce, b6f005e, a2c8e92 ×2).

**Tools:**

| Command | Result |
|---|---|
| `build_index.py --check-only` | exit 0: 731 requirements; 47 prefixes; 95 findings (19 CF + 39 DUP + 27 OQ + 10 TC); 34 decisions; 47 system rules |
| `compare_requirements.py 5846675 --strict` | exit 0: added 8 (ARCH-041, ARCH-042, GOV-021, GOV-022, GOV-023, OPS-021, PERF-023, PLT-029); removed 0; changed 0 |
| `selftest.py` | PASS, 19 lines, in 5.4 s; `/tmp` entry count 67 before and after; repo status unchanged |
| `ruff check` / `ruff format --check` | clean (run with `--no-cache`) |
| `mypy --check-untyped-defs` | clean (cache in scratch) |

**Consistency:**
- My own link and anchor check across 118 Markdown files and 2,660 links found nothing broken.
- All 4 `@` imports in `CLAUDE.md` resolve.
- Every checkpoint-log hash exists in `git log`, and 5846675 is HEAD.
- The registry class deltas add up: +2 CONFIRMED REQUIREMENT, +2 CONFIRMED ARCHITECTURAL PRINCIPLE, +4 CONSTRAINT.
- SR-46 and SR-47 sources match their requirements, and all 47 system-rule rows have consistent columns.
- `docs/README.md` links every document.
- The only stale "723 / SR-45 / 92 findings" numbers are in dated historical records, which is correct.

**Hygiene:**
- `git diff --check` is clean. No trailing whitespace, missing final newline or CR in the 8 new files.
- No secrets or local paths (`/home/`, `/tmp/`, `scratchpad`) in any changed or new file.
- No deletions. Every removed line has an updated replacement.
- Ignored entries: `.mypy_cache/` and `.ruff_cache/` (each ignores itself, as the tools README documents) and `tools/docs/__pycache__/` (in `.gitignore`). All date from 19:16, before this review.
- The 8 untracked files are all intended for this checkpoint.
```

## Launches that stopped before reporting

None.
