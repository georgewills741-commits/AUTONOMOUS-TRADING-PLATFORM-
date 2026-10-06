# Stage 1, Checkpoint A — Verification Record

> **Status:** ACTIVE record of Stage 1's checkpoint A: the development environment and repository layout (U1) and the testing foundation and machine checks (U6) of the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md); format: [traceability README](README.md). The stage as a whole is tracked in the [stage record](stage-01-foundation.md).

## Identity

- **Date:** 2026-10-06
- **Stage:** 1 — FOUNDATION, checkpoint A (the plan, section 11)
- **Starts from:** commit `69d3b86`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.
- **Authorization:** [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md) (Stage 1 only)

## Scope

**Added:**

| File | Unit | What it is |
|---|---|---|
| `pyproject.toml` | U1, U6 | Project definition: Python 3.12 or later; Pydantic as the only runtime dependency; pytest, Hypothesis, ruff, mypy as development dependencies; build backend `uv_build` 0.12.23; uv 0.12.23 required; pytest, mypy, and ruff settings |
| `uv.lock` | U1 | The locked versions of every dependency |
| `.python-version` | U1 | Python 3.12 |
| `src/atp/__init__.py`, `src/atp/py.typed` | U1 | The package root (D1), with no code yet; the marker that the package has type information |
| `tests/repository/test_no_secrets.py` | U1 (U5's repository test) | The repository test for secrets, and tests of its scanner on planted samples |
| `.github/workflows/checks.yml` | U6 | The machine checks (D4) |
| `tools/docs/ruff.toml`, `tools/docs/mypy.ini` | U1 | The documentation tools' own check settings, unchanged in effect |
| `docs/development.md` | U1 | The development guide (D2) |
| `docs/traceability/stage-01-foundation.md` | U8 | The stage record |
| This record | — | Checkpoint A's verification record |

**Changed:** `.gitignore` (local environment and secret files); the root `README.md` (status; link to the development guide); `docs/README.md` (index); the [roadmap](../roadmap/roadmap.md) (feature-status table of D5; Stage 1 status); the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) (banner: link to the stage record, the Hypothesis wording note); [architecture governance](../architecture/architecture-governance.md) (the table exists); the [technology stack](../architecture/technology-stack.md) (where versions are fixed; status); the [source-of-truth map](../architecture/source-of-truth-map.md) (versions, the development procedure, feature states, stage evidence); the [requirements README](../requirements/README.md) (requirement status during Stage 1); the [tools README](../../tools/docs/README.md) (code checks with pinned versions); the [traceability README](README.md) (records); the [project state](../project-state.md).

**Requirements:** none added, removed, or changed (check 4). Delivered in part by this checkpoint (the plan, section 3.1): TEC-001, TEC-008, TEC-009 (testcontainers excepted) by U1; GOV-012 and GOV-023 by U6; SEC-005 is applied by the repository test for secrets, ahead of U5.

**Out of scope:** U2 to U5 and U7 (checkpoints B to D); any platform behavior, contract, configuration, trading capability, credential, or deployment.

## Checks

The commands are those of the [development guide](../development.md), run with uv 0.12.23 from the repository root.

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | The lockfile installs exactly | `uv sync --locked` | PASS |
| 2 | Lint, formatting, types | `uv run --locked ruff check`; `uv run --locked ruff format --check`; `uv run --locked mypy`; `uv run --locked mypy --config-file tools/docs/mypy.ini` | PASS |
| 3 | Tests | `uv run --locked pytest` | PASS: 52 tests |
| 4 | Documentation and requirements | `uv run --locked python tools/docs/build_index.py --check-only`; `uv run --locked python tools/docs/selftest.py`; `python3 tools/docs/compare_requirements.py 69d3b86 --strict` | PASS: 734 requirements; self-test 34 cases; 0 added, 0 removed, 0 changed |
| 5 | The package builds | `uv build` | PASS: the wheel holds `atp/__init__.py`, `atp/py.typed`, and its metadata; the source archive holds `src/atp/`, `README.md`, `PKG-INFO`, and `pyproject.toml` (uv_build's copy, without comments, with the original kept as `pyproject.toml.orig`). Neither holds tests, anything from `docs/`, or secrets |
| 6 | Another uv version is refused | uv 0.8.17: `uv sync --locked` | PASS: refused ("Required uv version `==0.12.23` does not match") |
| 7 | The workflow runs what the guide says | Every `run:` line of the workflow extracted and run locally, with `CI=true` | PASS: all ten commands |
| 8 | The workflow file is valid | actionlint 1.7.12, run once with `uvx` | PASS: no error |
| 9 | Clean clone | A fresh clone of `69d3b86` with this checkpoint's changes applied and nothing else (no `.venv/`, no caches): `uv sync --locked`, then checks 2 to 5 | PASS. In the same throwaway clone, a credential-like value planted in an untracked file, and a force-added `.env`, each made the repository test fail, naming the file and never the value; it passed again once they were removed |
| 10 | Each config applies where meant | `ruff check --show-files`; `ruff check --show-settings` on a tool file and on a test file | PASS: documentation not linted; 59 rules for the tools (their former set), 468 for `src/` and `tests/` |
| 11 | The scanner finds what it must, passes what it must, and its tests can fail | The scanner's tests: each of the 18 value patterns, through 36 planted samples (prefixed names such as `BINANCE_API_SECRET`, names such as `AWS_SECRET_ACCESS_KEY`, `b"…"`, `r'…'`, and triple-quoted strings, a URL with an empty user, CRLF line endings, every alternative of the AWS and GitHub patterns, the bare `token` name), and 12 secret-like file names, planted in a temporary directory, is reported; every report names one of the 18 kinds exactly, so none can carry a value; ordinary text that resembles a credential is not reported (placeholders; templates and variable references, in settings and URLs; type names, file paths, numbers, enum values, masked values, and environment-variable names given as values, quoted or not; a public key); the repository test covers the repository root; the file listing, run on a temporary git repository, returns exactly the tracked, the untracked but not ignored, and the force-added files. Twenty mutations, each run against these tests, undo one rule at a time (every rule above, and the mutants that survived Gate 3 runs 2 and 3) | PASS: every sample and name reported, no ordinary line reported; each of the twenty mutations makes a test fail |
| 12 | Dependency review and licenses | PyPI's record of each locked release, its published advisories and license | PASS: no advisory; licenses in the [stage record](stage-01-foundation.md) |
| 13 | Hygiene | `git diff --check`; `git status --short --ignored`; scan of the added lines for secrets, local and system paths, and model or session identifiers | PASS |

## Gates

**Verification 1 — technical: PASS.** Checks 1 to 13 above.

**Verification 2 — architecture and consistency: PASS.** Reviewed by the builder against the plan, the decisions, and the requirements:

- **Placement (D1, D2, D4):** the package at `src/atp/`, tests under `tests/`, the development guide at `docs/development.md`, the workflow at `.github/workflows/checks.yml`; no directory created for a later checkpoint (`contracts/`, `config/examples/` wait for their first artifact).
- **Dependencies (D3, D11; constitution Rules 99–102):** only the approved set and their transitive dependencies, with uv and the build backend pinned exactly and the actions by commit hash; actionlint and the advisory lookups were run once and not added.
- **No second source:** versions are fixed in one place each, now named in the [source-of-truth map](../architecture/source-of-truth-map.md); the tools' own check settings configure checks of the tools only, not the platform (GOV-014); the feature-status table is the one record of feature states (D5).
- **Scope (RMP-011, GOV-017):** no platform behavior, contract, configuration, Hypothesis profile, or command written ahead of its checkpoint.
- **Requirements:** none changed (check 4); in the strict sense of constitution Rule 211 none is yet implemented in full, which the [requirements README](../requirements/README.md) now says; the registry's generated status line therefore stays true.
- **Consistency:** the roadmap, project state, stage record, feature-status table, plan banner, architecture governance, technology stack, source-of-truth map, tools README, and indexes agree with what was built; a sweep for stale statements about checkpoint A, pinning, and "no code" found one active line, in the project state, now corrected (the others are approved plan text, dated records, or a decision's conditional rule).
- **Security:** the workflow is read-only, keeps no credentials, uses no repository secret, and pins every action; the repository test covers every file git would commit.

**Verification 3 — independent end-to-end and failure audit.** A fresh-context reviewer, not the builder, worked from a clean clone with the change set applied, ran every command of the development guide and the workflow, tried to break the checks, and verified the pins, the checksum, the dependency review, and the records.

- **Run 1: FAIL**, two blocking findings and eleven non-blocking ones, all fixed:

| # | Finding | Severity | Fix |
|---|---|---|---|
| B1 | The secret scanner missed credential names with a prefix (`BINANCE_API_SECRET`, `DB_PASSWORD`, `exchange_api_key`): its pattern began with a word boundary, and an underscore is a word character | Blocking | The name may follow any character but a letter or digit; planted samples with prefixed names added; a mutation back to the word boundary fails those samples and the no-value test's count (check 11) |
| B2 | The plan's banner and the stage record said U6's Hypothesis configuration "cannot be met", which is false: Hypothesis's pytest plugin options can be set in `pyproject.toml` | Blocking | Both corrected: the setting is deferred to checkpoint B, which writes the first property tests; the development guide says the same |
| N1 | Other secret formats and file names were not detected (unquoted dotenv and YAML values, bare `secret` and `token` keys, credentials in URLs, several issuers' tokens, `*.env` and other credential files) | Non-blocking | Detected now: 18 value patterns and a longer list of file names; `*.env` ignored by `.gitignore` |
| N2 | The file listing had no automated test | Non-blocking | Test added on a temporary git repository; two mutations of the listing each fail it |
| N3 | The scanner reads the working tree, not the staged content | Non-blocking | Said in the test's docstring and the development guide; the machine checks scan the pushed commit |
| N4 | The source archive's contents were described inexactly | Non-blocking | Check 5 lists them exactly |
| N5 | A machine path appeared in the stage record | Non-blocking | Removed; the hygiene scan now looks for system paths too |
| N6 | The development guide did not say how to get uv 0.12.23 | Non-blocking | Added; the command was run and its uv synced the project |
| N7 | Two builder readings in the feature-status table were not recorded | Non-blocking | Recorded in the stage record's "builder details and plan wording" |
| N8 | Architecture governance still described the time before implementation as the present | Non-blocking | Reworded |
| N9 | U3 needs ruff's SLF001, which is not enabled yet | Non-blocking | Carried to checkpoint B in the stage record |
| N10 | The records said the three gates had passed while Gate 3 had not | Non-blocking | The commit waits for a passing Gate 3 run |
| N11 | The negative test could run on a temporary branch | Optional | Kept on this branch: the builder pushes only to its designated branch; recorded in the stage record |

- **Run 2: FAIL**, one blocking finding and six non-blocking ones, all fixed. A new fresh-context reviewer confirmed every other run-1 fix, the clean clone, every planted break (13 scanner and listing mutants killed, one surviving), the pins, the checksum, and the dependency review:

| # | Finding | Severity | Fix |
|---|---|---|---|
| F1 | B2 only partly fixed: the sentence introducing the stage record's "builder details and plan wording" still said a plan point "cannot be met" | Blocking | Reworded: "one plan item deferred to checkpoint B (U6's Hypothesis setting)" |
| N1 | Credential shapes still missed: `b"…"`, `r'…'`, and triple-quoted strings; names such as `AWS_SECRET_ACCESS_KEY`, `ENCRYPTION_KEY`, `SIGNING_KEY`; a URL with an empty user | Non-blocking | Detected now, each with a planted sample; the shapes still not reported are carried to checkpoint C in the stage record |
| N2 | Ordinary text reported as secrets (DSN templates and variable references, type names, file paths, numbers, environment-variable names given as values) | Non-blocking | Not reported now; each added to the ordinary-text test |
| N3 | The no-value test survived a mutant that added a report carrying part of a value | Non-blocking | Every report must have the exact form "file:line: secret-like value (kind)"; that mutant now fails |
| N4 | "If any" wording could let U6's Hypothesis item close with nothing written | Non-blocking | Checkpoint B writes the setting; if none is needed, it records a deviation from U6 for the owner |
| N5 | Record wording: the B1 row's "exactly those samples"; check 5's "documents"; the guide's "the same commands" | Non-blocking | Corrected |
| N6 | The record format asks for the builder's own separate pass | Non-blocking | Added below |
| Optional | Git run by the test could act on another repository if repository variables were set | Optional | The test removes `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` before running git |

- **Run 3: PASS**, no blocking finding. A third fresh-context reviewer confirmed every run-2 fix, the clean clone, every planted break (35 mutations run, 27 killed), the pins, the checksum, the dependency review, the records' counts, and the fresh-session test. Its five non-blocking findings, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| N1 | The no-value test still accepted any text in a report's parentheses, so a report could carry part of a value there (as run 2's N3, fixed for one sample rather than the class) | Every report must name one of the 18 kinds exactly; that mutant now fails |
| N2 | CRLF line endings slipped past both unquoted patterns | Both accept CRLF; two CRLF samples planted |
| N3 | Quoted values that are not credentials were still reported (templates, type names, paths, numbers, enum values, masked values, and name-to-kind lines such as U4's configuration will hold), and the records claimed more than the code did (as run 2's N2, fixed for samples rather than the class) | One rule for every setting: a value, quoted or not, is reported only if it contains both a letter and a digit; templates and variable references are excluded explicitly; each case added to the ordinary-text test; the records state the rule as the code applies it |
| N4 | Missed shapes not in the list carried to checkpoint C | Added to the stage record's "Carried to checkpoint C", with what the letter-and-digit rule gives up (a letters-only passphrase) |
| N5 | Mutants that survived: the unquoted setting's letter rule alone, a mis-set repository root, the bare `token` name, the `ghs_` and `ASIA` alternatives | A digits-only ordinary sample, an assertion that the scan covers `pyproject.toml`, and a planted sample for each alternative; each mutant now fails |

**Builder's own separate pass**, apart from the reviewers: after each run's fixes, checks 1 to 13 re-run on the working tree and on a clean clone; check 11's mutations run by the builder against its own changes (the first attempts misfired twice, see "Failures and fixes"); the records re-read against each finding, and swept for the claims the findings named ("cannot be met", "if any", counts, file lists). After run 3's fixes the builder's mutation run found two more rules untested, because the new letter-and-digit rule already covered their samples (the template exclusion and the environment-name exception); a sample only each of them excludes was added, and all twenty mutations then failed a test. Run 3's fixes change the test of the repository only, not its scope or any record's claim beyond what they correct, so no fourth independent run was made; checks 1 to 13 were re-run on the final tree.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| ruff reported 34 findings in the documentation tools | ruff 0.16 replaced its four default rule families with 413 curated rules; the tools were written to the old defaults | `tools/docs/ruff.toml` keeps the tools at their former rule set; their code is unchanged (U1: the tools run unchanged) | Check 2: PASS |
| `ruff format --check` wanted to rewrite a Python example inside the master audit record | ruff 0.16 also formats Python code blocks in Markdown files | ruff limited to Python files (`include` in `pyproject.toml`) | Check 2: PASS; check 10 |
| mypy reported 23 errors in the documentation tools | The project's strict settings applied to the tools when they were named on the command line | `tools/docs/mypy.ini` keeps the tools at the level they were written to | Check 2: PASS |
| The new test file failed `ruff format --check` | Lines longer than the formatter's 88 columns | Formatted with `ruff format` | Check 2: PASS |
| The documentation checker failed on the name of the checksum algorithm, written in capitals with a hyphen, reporting it as an undefined requirement | The checker reads any word shaped like a requirement ID (two to four capitals, a hyphen, three digits) as one | Written as "sha256" in the two documents | Check 4: PASS |
| The self-test failed | This record did not exist yet, so the stage record's link to it was broken in the self-test's copy too | This record written | Check 4: PASS, 34 cases |
| A first run of the checks reported exit code 0 for commands that had failed | The builder's helper read the exit status of the wrong command | Every check re-run with its own exit code captured; all results above come from that run | Checks 1 to 5: PASS |
| Gate 3 run 1: two blocking findings (B1, B2) | B1: a regular-expression boundary that treats the underscore as part of a word, and a test whose only sample was the one shape the pattern caught; B2: a claim about Hypothesis written from its core library without checking its pytest plugin | See "Verification 3" | Gate 3 run 2 |
| After run 3's fixes, two scanner rules were untested | The new letter-and-digit rule excluded every ordinary sample those rules were meant to cover | A sample only each rule excludes added | Check 11: all twenty mutations fail a test |
| Gate 3 run 2: one blocking finding (F1) | The run-1 fix corrected the table row but not the sentence above it that made the same claim; the fix was not re-read against the whole section | Sentence reworded; the record searched for every remaining "cannot be met" | Gate 3 run 3 |
| A second mutation check skipped two mutations | The script's search strings were escaped wrongly, so they were not found | Re-run with exact raw strings; both mutations then made a test fail | Check 11 |
| The first mutation check reported failures that did not come from the mutation | Shell quoting doubled the backslash, and the mutant ran outside the repository, so the repository-wide test failed on its own | Re-run with a script that applies each mutation exactly and leaves out the repository-wide test | Check 11 |
| Wording ahead of the facts: the roadmap first called checkpoint A "done"; the technology stack's status left out TEC-003; the stage record's version note was inexact | Written before the evidence was complete, or from memory | Corrected: checkpoint A is "built and verified", its GitHub runs pending; TEC-003 added; the note gives each version exactly | Re-read |

## Final status

**PASS.** Verification 1 and 2 passed; Verification 3 passed on run 3, after runs 1 and 2 failed and every finding of the three runs was fixed; checks 1 to 13 pass on the final tree and on a clean clone. No requirement or decision changed; no platform behavior was written.

**Pending, recorded in the [stage record](stage-01-foundation.md):** U6's acceptance on GitHub (the machine checks' first run on this checkpoint's commit, and the negative test), which needs this commit's push and is recorded by the next commit; U6's Hypothesis setting, deferred to checkpoint B; the items carried to checkpoints B and C.

## Environment

Python 3.12.3 (the project; the system interpreter) and Python 3.11.15 (`python3`, for `compare_requirements.py`); uv 0.12.23; ruff 0.16.10; mypy 2.4.0; pytest 9.1.1; Hypothesis 6.168.5; Pydantic 2.13.5; git 2.43.0; Linux.
