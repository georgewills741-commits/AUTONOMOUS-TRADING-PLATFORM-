# Integrity verification 2026-10-01 — Gate 3 Report

> **Status:** REFERENCE (evidence) — the report of the independent Gate 3 review of the change whose record is [Repository Integrity Verification — 2026-10-01](integrity-verification-2026-10-01.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). It is reproduced in a text block exactly as given, except that local paths are shown as placeholders (`<scratchpad>`, `<repository>`). The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the review. The headings use the record's names for the runs.

## Independent review

- **Reviewer:** a fresh-context subagent, launched 2026-10-01, 19:27 UTC; report given 2026-10-01, 19:33 UTC
- **sha256:** `c3449fbac2da0c1dbaaf9164ec5c86c6968d6d1fd94fb43d5bb3615ae3524555` as given; `272b3432b84ef0cafd889f14fd3b38f65a0f5f3a54a64636522e101f8f3a3ab2` as shown, with 7 local paths replaced

```text
**Verification 3: PASS.** I found nothing blocking. The script changes are formatting and types only, the checkers still catch broken input, and the numbers in the change set and the checker counts are correct. Five statements in the new record and README are wrong or contradict each other (findings 1–5). Each is a one-line fix, and I recommend fixing them in this same checkpoint. Gate 3 in the record still says PENDING (record line 92) and must be filled in before the commit.

I worked read-only. All experiments ran in a temporary worktree at `<scratchpad>/review3/wt`. I removed it afterwards (`git worktree remove --force` and `prune`), and `git worktree list` shows only the main tree. The real repository's `git status --porcelain` is the same before and after my review.

## Findings

1. **NON-BLOCKING: wrong cause given for `__pycache__`.** Three places say the bytecode is written when the scripts run: `.gitignore:1`, `tools/docs/README.md:55` and record line 66 (check 14).
   - Running the scripts directly writes no bytecode. I ran both tools in the worktree without `-B` and `tools/docs/` stayed clean; a test file run with `python3 t.py` produced no `__pycache__` either.
   - `python3 -m py_compile` does write it, and that is the builder's own check 5 (record line 57). Both `.pyc` files have the same timestamp, 19:16:55.657 and 19:16:55.658, which fits one `py_compile` run.
   - The `.gitignore` entry is still worth keeping. Only the stated cause should be corrected.

2. **NON-BLOCKING: a new README sentence contradicts the table above it.** `tools/docs/README.md:54` says the generated files are "never edited by hand". Lines 17–19 of the same README say `handoff-coverage.md` keeps hand-written tables and that every other column of the two reconciliations "is hand-written and kept". Only the generated parts are never hand-edited.

3. **NON-BLOCKING: the strict-mode mypy statement is wrong, and default mode checks less than the record implies.** Record line 76 says strict mode's 23 findings are "all functions without type annotations".
   - Running `mypy --strict` gives 13 untyped-call, 7 missing-annotation, 1 missing-return and **2 incompatible-assignment** findings. The last two are at `build_index.py:227` and `:230` (`nums` is a `range` in one branch and a `list` in another).
   - mypy's default mode skips the bodies of functions without annotations (`parse_src`, `approval`, `titles_of`, `md_files`, `strip_code`). So "Types PASS" (check 8) covers module-level code only.
   - With `--check-untyped-defs`, mypy reports the same 2 errors. They are harmless.

4. **NON-BLOCKING: the rename count is understated.** Record line 61 (check 9) says "only the two renamed loop variables". My comparison of the syntax trees (with annotations and the `typing` import removed) shows **three** loops renamed using two new names: `d`→`dec` twice and `d`→`extra` once, plus `d = dict(m.groupdict())`. `compare_requirements.py` is identical apart from formatting. Nothing reads the module-level `d` after these loops, and the new names clash with nothing.

5. **NON-BLOCKING: the new standing check isn't linked to where checks are defined.** `tools/docs/README.md:42` makes ruff and mypy a check "at every checkpoint".
   - DEC-032 line 22 lists the tests in use until code exists, and it names only `build_index.py`, `compare_requirements.py` and the round-trip checks.
   - The new README section cites neither DEC-009 nor TEC-009, which approved ruff and mypy as project tooling.
   - Nothing pins the tool versions; the README only records "Versions last used".
   - It agrees with DEC-009 rather than contradicting it, but a future session will find the rule only by reading the tools README.

6. **NON-BLOCKING: two owner governance texts exist only outside the repository.** `docs/project-state.md:133` and record lines 78–80 say the master execution constitution and the owner's directive are not committed yet.
   - Both exist only in the session scratchpad (`mec-raw.txt` and `dir2-raw.txt`, dated 2026-10-01).
   - The checkpoint rule says such knowledge must not exist only in chat or context. The note is accurate and safe ("ask the owner to send them again"), and the sequencing follows the owner's "Before doing anything else".
   - "Next approved step" (project-state lines 212–217) doesn't list this adoption. The adoption checkpoint should follow immediately.

7. **NON-BLOCKING: the record's Gate 3 section needs completing before the commit.** Record line 92 says PENDING. DEC-032 line 23 also asks for the builder's own separate pass alongside the independent reviewer; the record's Gate 3 row (line 88) mentions only the independent reviewer.

8. **NON-BLOCKING, already in the repository at HEAD (not part of this change):** `tools/docs/README.md:38` ("Run it after every documentation change…") sits under the "Requirement comparison" heading but means `build_index.py`, so it reads ambiguously.

## Claims I confirmed
- **Change set:** a2c8e92 against main has 113 files, +24,636/−1, 112 added and 1 modified. a9034ce against main has 103 files, +18,401/−1.
- **Area table:** every row matches. The "other docs/" row's 19 files are ai 5, operations 7, product 2 and one each for the other areas. Handoffs (12,834 lines) plus builder (3,190) make 16,024.
- **README.md "−1":** the old file was one line with no final newline, kept as line 1 of the new README.
- **Checker counts:** 723 requirements, 47 prefixes, 92 findings, 32 decisions, 34 systems, 45 system rules.
- **Comparisons:** against a9034ce, 111 added, 0 removed, 0 changed. Against HEAD, 0, 0 and 0.
- **Trailing spaces:** 92 lines of the Part 2 copy end in spaces, and so do exactly 92 lines of the received text (`handoff-part2-raw.txt`). No other tracked or new file has trailing blanks.
- **File types:** 111 Markdown and 2 Python files at HEAD. No binary, empty, over-1 MB or CR-ending files, no duplicate content, and every file ends with a newline.
- **Links:** every Markdown file except the root `README.md` is linked from another file (112 checked). The new record is linked from `docs/README.md`, `project-state.md` and `tools/docs/README.md`.
- **Secrets:** a scan of tracked and untracked files found no secrets, local paths or email addresses, and there is no `.env` file. There are no TODO/FIXME/HACK markers outside the verbatim sources.
- **Checkpoint log:** the hashes 16d317c through a2c8e92 match `git log`. The remote branch is at a2c8e92.
- **Before the fix:** the old scripts failed `ruff format --check` (2 files) and mypy (8 errors).
- **Commit contents:** `git diff --check` is clean. Every removed line in the documentation diffs is a replacement. The new `.gitignore` hides no tracked file (`git ls-files -ci` is empty). `git add -A` would add only `.gitignore` and the record; the caches stay ignored.

## Commands and key outputs
- `python3 -B tools/docs/build_index.py --check-only` → exit 0. File timestamps were the same before and after, so it wrote nothing.
- `git diff --quiet HEAD --` on the four generated files → identical. A full regeneration in the worktree gave byte-identical files.
- `python3 -B tools/docs/compare_requirements.py a9034ce --strict` → 612 to 723 requirements, 111 added, 0 removed, 0 changed, exit 0. Against `HEAD --strict`: 0/0/0, exit 0.
- Both tools on Python 3.10, 3.11, 3.12 and 3.13 → exit 0 on every version.
- `ruff check tools/docs` → "All checks passed!" `ruff format --check tools/docs` → "2 files already formatted". `mypy tools/docs` → "Success: no issues found in 2 source files". Versions: ruff 0.15.8, mypy 1.19.1, Python 3.11.15.
- In the worktree at HEAD: `ruff format --check` → "2 files would be reformatted". mypy → "Found 8 errors in 1 file".
- `mypy --strict tools/docs` → 23 errors (breakdown in finding 3). `mypy --check-untyped-defs tools/docs` → 2 errors.
- Syntax-tree comparison: `compare_requirements.py` IDENTICAL; `build_index.py` differs only by three loop renames and the `dict()` copy.
- Running old and new scripts on the same inputs gave identical output and exit codes: the control, bad references (link, SR, DEC, CF, SYS), an unknown class, an unlisted decision, and a reworded requirement in the comparison.
- Checker negative tests (all exit 1 with the matching message):
  - broken link
  - duplicate RSK-001
  - malformed requirement line
  - undefined SR-99 and XAR-999
  - stale `registry.md`
  - DEC-099 missing from the decision log
  - source §999
  - deleted RSK-047 ("prefix RSK not sequential")
  - The control after restoring all of these: exit 0.
- `compare_requirements.py HEAD --strict` negative tests:
  - RSK-001 text reworded → "changed (1)", exit 1
  - indented continuation line under RSK-015 edited → exit 1
  - RSK-002 class changed to PROPOSED → exit 1
  - RSK-048 removed → "removed (1)", exit 1
  - The same rewording without `--strict` → exit 0. After restoring → 0/0/0, exit 0.
- `git status --short --ignored` → 5 modified files, `.gitignore` and the record untracked, and `.mypy_cache/`, `.ruff_cache/` and `tools/docs/__pycache__/` ignored. The two caches are ignored by their own `.gitignore` files, `__pycache__` by the new root `.gitignore:3`.

## Files
- <repository>/docs/traceability/integrity-verification-2026-10-01.md (lines 57, 60–61, 66, 76, 78–80, 88, 92)
- <repository>/tools/docs/README.md (lines 17–19, 38, 42, 54–55)
- <repository>/.gitignore (line 1)
- <repository>/docs/project-state.md (lines 133, 212–217)
- <repository>/docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md (lines 22–23)
- <repository>/tools/docs/build_index.py (lines 227, 230, 341, 571, 589)
```

## Launches that stopped before reporting

None.
