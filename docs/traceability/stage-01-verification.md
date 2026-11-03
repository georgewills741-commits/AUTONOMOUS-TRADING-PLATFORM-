# Stage 1 Verification — the Whole Stage's Three Gates (X2)

> **Status:** ACTIVE record of X2 of the [stage record](stage-01-foundation.md)'s exit checklist: the three gates of the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) (section 8), applied to the whole stage on its final tree, after X9's corrections (plan section 9, item 2: "after every fix"; [DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md); [DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md)). The change also reconciles the last change's temporary backup with that change's commit, `1c6772c`, and retires its branch ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 6). Its three gates: "Final status and remaining issues". Format: [traceability README](README.md).

## Identity

- **Date:** 2026-11-03
- **Stage:** 1 — FOUNDATION; X2 of the exit checklist, after X9 and before X10 ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 6). This change writes documentation only; it starts no later stage's work ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md))
- **Starts from:** commit `1c6772c` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote. This record's own commit is entered in the project state's checkpoint log by the next change.
- **The final tree:** since checkpoint D's commit, `fd750c3`, no code, test, tool's code, example configuration, contract, lockfile, project definition, or workflow has changed: outside `docs/`, only `CLAUDE.md`, the README, the documentation tools' README, and the manifest of preserved texts (`git diff --stat fd750c3 1c6772c`). The stage's code and tests are those its four checkpoints verified; this change adds documents only.
- **Temporary backup** (DEC-057, decision 4): the work was pushed to `claude/unverified-backup-x2` as soon as it existed, and again as it changed. Each commit carries the seven labels of [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4) and the emergency checkpoint record of master execution constitution §132. Its reconciliation with this change's commit is recorded by the next change.

## Scope

**Added:** this record.

**Changed:** the stage record (the exit checklist's X2, X3, X4, and X5, and its date; its status line; the retirements listed for the certificate); the [roadmap](../roadmap/roadmap.md) (the evidence of Stage 1's features in the feature-status table, and its current position); the project state (its status line; the table under "Current stage"; the continuation contract's rows "Current stage and substage", "Current task", "In progress, possibly partial", "Blocked", "Stage convergence", "Pending verification", "Other branches", and "Next safe action"; "Branches"; "Completed work"; "In-progress work"; "Blockers"; "Recent changes"; "Next approved step"; the checkpoint log); the indexes ([documentation index](../README.md), [traceability README](README.md)).

**Requirements:** none added, removed, or changed (Gate 1).

**Out of scope:** X10, the certificate (X6), and the owner's approval (X8); any later stage's work.

**The owner's messages after the last one the previous record names** (the [company-grade order audit](company-grade-order-audit-2026-11-03.md), which names none after the owner's "Continue" of 2026-11-03, 13:33 UTC), up to the copy that this record's last Gate 3 run reviews: "Try again" of 19:13 UTC, after the usage limit had stopped the session: procedural ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7). Since that record's copy (14:21 UTC), the report of its run 1 as the client delivered it (14:37 UTC), the notices of background tasks, the stop hook's feedback, the usage limit's messages, and the notices of the worker's restarts (15:47, 18:05, and 19:13 UTC) are the client's own.

## Gate 1 — technical (plan section 8)

From a clean clone of `1c6772c` (2026-11-03, 19:20 UTC), the commands of the stage record's "End to end from a clean clone", run by script, with uv 0.12.23, the version the project requires (`pyproject.toml`, `required-version`). This container's own uv, 0.11.32, refuses to run the project, so the required version was installed in a scratch environment outside the repository; the first attempt, with 0.11.32, stopped at that refusal ("Failures and fixes"). The same commands were run again on the final tree with this change before Gate 3's copy was made (the last row).

| Check | Result |
|---|---|
| `uv sync --locked`; `uv lock --check` | PASS: the locked packages installed; the lockfile is current (20 packages) |
| `uv run --locked ruff check`; `uv run --locked ruff format --check` | PASS |
| `uv run --locked mypy`, strict; `uv run --locked mypy --config-file tools/docs/mypy.ini` | PASS |
| The documentation checker (`--check-only`) and its self-test | PASS: the checker regenerates nothing and finds no error, so the matrix is current; the self-test's 61 cases and the control |
| `uv run --locked pytest` | PASS: 1,108 tests |
| `uv build` | PASS: `atp-0.1.0-py3-none-any.whl` and `atp-0.1.0.tar.gz` |
| `atp config check` on the example configuration of each of the six environments, the secret set | PASS: exit 0 for each, the secret shown only as `<redacted>` |
| The secret not set; an unknown environment | PASS: exit 1 for each |
| The broken copies of checkpoint D's run: a trading-enabled credential declared for staging; the secret's value in a comment of `platform.toml`; a TOML integer too long to read, in decimal and in hexadecimal; a configuration directory whose name is too long; a document nested too deeply to read; the secret's value written with a TOML escape; a `platform.toml` larger than V-41 | PASS: exit 1 for each, with its refusal and no traceback, and the secret's value never shown |
| The command used wrongly | PASS: exit 2 |
| The requirement comparison over the whole stage: `compare_requirements.py 69d3b86 --strict`, against the commit that authorized Stage 1 | PASS: 734 requirements before, 749 now; the 15 of items 4 and 5 added (DEC-058, DEC-059), none removed or changed |
| The same commands on the final tree with this change | PENDING |

The machine checks passed on `1c6772c` ([run 41656238442](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/41656238442), every step, 1,108 tests) and run on this record's commit. Check 7, the mutation check, killed all 461 mutations on checkpoint D's final tree ([checkpoint D verification](stage-01-checkpoint-d-verification.md)); the code and tests are unchanged since (the final tree, above), so its result stands for this tree.

## Gate 2 — architecture and consistency (plan section 8)

| Plan section 8's Gate 2 | Evidence | Result |
|---|---|---|
| Each module has one owner and one responsibility (constitution Rule 83) | The source-of-truth map's "Architecture to repository": five rows, `atp`, `atp.numeric`, `atp.contracts`, `atp.config`, and `atp.cli`, each with one owner and its responsibility ([company-grade order audit](company-grade-order-audit-2026-11-03.md), items 4 and 8) | PASS |
| Dependencies point one way, enforced by the structure test | The imports between platform modules, read from the code's syntax trees: `atp.numeric` imports none; `atp.contracts` only `atp.numeric`; `atp.config` only `atp.contracts` and `atp.numeric`; `atp.cli` only `atp.config`, and no module imports `atp.cli`. `tests/repository/test_structure.py` enforces them and passes (Gate 1) | PASS |
| The command-line module receives errors from `atp.config` already rendered | `atp.cli` imports only `atp.config`; each refusal of Gate 1's broken copies reaches the command as a rendered line, with no traceback | PASS |
| No second configuration source (GOV-014) | The code reads the process environment only for secrets (`atp.config`'s `_secrets.py`) and files only for the configuration (`atp.config`'s `_load.py`) and to compare the committed contract schemas (`atp.contracts`' `_schemas.py`) (a search of `src/`) | PASS |
| No float in an amount (TEC-003) | `atp.numeric`'s amounts refuse a float, and a TOML float is read as an exact amount (`parse_float`); the other mentions of `float` in `src/` are refusals or `atp.contracts`' rule for where a finite float is allowed, all tested | PASS |
| No host-specific value in code (MIG-004) | No host, address, or local path in `src/` (a search); its one URL is JSON Schema's dialect identifier | PASS |
| Every requirement of section 3.1 traced in the matrix | 24 of 24, each with its implementation and its tests, which the checker enforces (the [verification matrix](verification-matrix.md)) | PASS |
| Every public function of the three modules has at least one test | Each name in the `__all__` of `atp.numeric` (12), `atp.contracts` (17), and `atp.config` (19) is named in a test, apart from `atp.config`'s two file-name constants, `PORTABLE_FILE` and `ENVIRONMENTS_DIRECTORY`, which are not functions (a script over the packages and `tests/`) | PASS |
| The documentation, the roadmap, the feature-status table, and the project state agree with what was built | The developer guide's commands are Gate 1's, and they pass; the threat model's controls, the architecture-to-repository map, and the matrix were read against the code (the [company-grade order audit](company-grade-order-audit-2026-11-03.md), items 4 to 6 and 11); the feature-status table's Stage 1 rows, their states, and the project state, read against the stage record. The feature-status table's evidence said that the stage's own gates run before its exit; this change says they passed | PASS |
| No future-stage work slipped in | `src/atp/` holds the four packages of the plan; its only trading words are the credential kind that only production may declare (MODE-006, SEC-004) and its refusal | PASS |

## Gate 3 — independent end-to-end and failure audit

PENDING.

## The exit checklist after X2

X2: the three gates pass on the final tree, with no blocking finding open (this record). X3: every requirement of section 3.1 is traced to its implementation and test in the matrix, in the forms U7 accepts, checked on the final tree (Gate 2). X4: the repository test for secrets passes (Gate 1); a scan of all 287 tracked files of `1c6772c` finds no secret, local path, or model or session identifier, apart from the secret test's own planted samples (`tests/repository/test_no_secrets.py`); U1's dependency review is recorded, and the lockfile is unchanged since it ([company-grade order audit](company-grade-order-audit-2026-11-03.md), item 9). X5: each document the plan names exists and agrees with what was built (Gate 2). X1 stays IN PROGRESS: U8's acceptance, section 9 of the plan, is met at the exit, with the certificate and the owner's approval.

## Reconciliation of the last change's temporary backup

PENDING.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Gate 1's first run (19:19 UTC): every command stopped at uv's refusal, "Required uv version `==0.12.23` does not match the running version `0.11.32`"; one line read PASS, since the refusal's exit status, 2, was the one expected of the command used wrongly | This container's uv is not the version the project requires; the script took an exit status for its cause | The required uv installed in a scratch environment; the script fails a command whose output holds uv's refusal | Gate 1, 19:20 UTC |

## Final status and remaining issues

PENDING.

## Environment

System Python 3.11 (`python3`) for the documentation tools; uv 0.12.23 and the project's Python 3.12 for Gate 1; git; GitHub's branch list, pull requests, and workflow runs, read through the session's GitHub tools.
