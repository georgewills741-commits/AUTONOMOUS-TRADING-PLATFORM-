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

**Changed:** the stage record (the exit checklist's X2, X3, X4, and X5, and its date; its status line; its "Blockers"; the retirements listed for the certificate); the [roadmap](../roadmap/roadmap.md) (the evidence of Stage 1's features in the feature-status table, and its current position); the project state (its status line; the table under "Current stage"; the continuation contract's rows "Current stage and substage", "Current task", "In progress, possibly partial", "Blocked", "Stage convergence", "Pending verification", "Other branches", "Known risks", and "Next safe action"; "Branches"; "Completed work"; "In-progress work"; "Blockers"; "Recent changes"; "Next approved step"; the checkpoint log); the indexes ([documentation index](../README.md), [traceability README](README.md)).

**Requirements:** none added, removed, or changed (Gate 1).

**Out of scope:** X10, the certificate (X6), and the owner's approval (X8); any later stage's work.

**The owner's messages after the last one the previous record names** (the [company-grade order audit](company-grade-order-audit-2026-11-03.md), which names none after the owner's "Continue" of 2026-11-03, 13:33 UTC), up to the copy that this record's last Gate 3 run reviews: "Try again" of 19:13 UTC, after the usage limit had stopped the session: procedural ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7). Since that record's copy (14:21 UTC), the report of its run 1 as the client delivered it (14:37 UTC), the notices of background tasks, the stop hook's feedback, the usage limit's messages, the notices of the worker's restarts (15:47, 18:05, and 19:13 UTC), and the summary the client wrote when it compacted the session's context (19:32 UTC) are the client's own.

## Checks

The change's own checks: the documentation tools, with the system Python 3.11, and git, on the working tree with this change. The change is part of the final tree, so its three gates are the stage's below.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | PASS: exit 0; the regeneration changes no generated file |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | PASS: 61 cases and the control |
| 3 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py 1c6772c --strict` | PASS: 749 requirements before and after; none added, removed, or changed |
| 4 | The code is unchanged | `git diff --name-only 1c6772c` and `git ls-files --others --exclude-standard` | PASS: the six files this change adds or changes are documents: this record, the project state, the stage record, the roadmap, the documentation index, and the traceability README |
| 5 | Hygiene of the change | `git diff --check 1c6772c`, its new file included; a scan of the lines this change adds, its new file included, for local paths, session or model identifiers, and the shapes of secrets | PASS: `git diff --check` reports nothing; the scan finds no local path, session or model identifier, or secret |
| 6 | The preserved texts unchanged | `git diff --name-only 1c6772c -- docs/handoffs docs/builder` | PASS: no file under `docs/handoffs/` or `docs/builder/` changes |

## Gate 1 — technical (plan section 8)

From a clean clone of `1c6772c` (2026-11-03, 19:20 UTC), the commands of the stage record's "End to end from a clean clone", run by script, with uv 0.12.23, the version the project requires (`pyproject.toml`, `required-version`). This container's own uv, 0.11.32, refuses to run the project, so the required version was installed in a scratch environment outside the repository; the first attempt, with 0.11.32, stopped at that refusal ("Failures and fixes"). In the same clone, the requirement comparison over the whole stage ran at 19:38 UTC, and the tests ran again at 19:42 UTC to count them, since the script records each command's exit status and last line of output. The same commands were run again on the final tree with this change before Gate 3's copy was made (the last row).

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
| The same commands, and the requirement comparison over the whole stage, on a clean clone of `1c6772c` with this change applied, whose tree is that of the copy Gate 3 reviews | PASS: the same results, the 27 commands of the script, 1,108 tests, and the comparison's 734 and 749 requirements, the same 15 added |

The machine checks passed on `1c6772c` ([run 41656238442](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/41656238442), completed at 14:43 UTC, every step, 1,108 tests) and run on this record's commit. Check 7, the mutation check, killed all 461 mutations on checkpoint D's final tree ([checkpoint D verification](stage-01-checkpoint-d-verification.md)); the code and tests are unchanged since (the final tree, above), so its result stands for this tree.

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
| No future-stage work slipped in | `src/atp/` holds what the plan names: the `numeric`, `contracts`, and `config` modules and the `atp` command (`cli`). A search of `src/` for trading words finds the credential kind that only production may declare (MODE-006, SEC-004) and its refusal; `atp.contracts`' docstring, which says that no system contract, orders among them, is defined there; `atp.numeric`'s, which says that the exchange increments amounts are rounded to come in DATA FOUNDATION; and a dataclass's `order=True`: no exchange connection, order, or trading behavior | PASS |

## Gate 3 — independent end-to-end and failure audit

PENDING.

## The exit checklist after X2

X2: the three gates pass on the final tree, with no blocking finding open (this record). X3: every requirement of section 3.1 is traced to its implementation and test in the matrix, in the forms U7 accepts, checked on the final tree (Gate 2), and each requirement-marked test proves its requirement (Gate 3). X4: the repository test for secrets passes (Gate 1); a scan of all 288 files of the final tree with this change (19:38 UTC) finds no secret, local path, or model or session identifier, apart from the secret test's own planted samples (`tests/repository/test_no_secrets.py`); U1's dependency review is recorded, and the lockfile is unchanged since it ([company-grade order audit](company-grade-order-audit-2026-11-03.md), item 9). X5: each document the plan names exists and agrees with what was built (Gate 2). X1 stays IN PROGRESS: U8's acceptance, section 9 of the plan, is met at the exit, with the certificate and the owner's approval.

## Reconciliation of the last change's temporary backup

The company-grade order audit, committed as `1c6772c`, was backed up on `claude/unverified-backup-x9` ([company-grade order audit](company-grade-order-audit-2026-11-03.md), "Identity"), in six commits, each on the one before and the first on `0a9a8a5`, committed on 2026-11-03 from 14:13 UTC (`32f59a5`) to 14:41 UTC (`96cb67b`). `9807a6f` holds the tree of the copy given to its Gate 3 run 1. Each commit carries the seven labels, the emergency checkpoint record of §132 with its seven fields, and the session's trailer (a check of every commit's message). On 2026-11-03, from 19:15 UTC, after `1c6772c` was pushed and the machine checks passed on it, the builder compared the branch with `1c6772c` by owner decisions 10's eight checks:

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `1c6772c`'s tree is `96cb67b`'s (`git diff --name-status`: no difference): the last backup holds the fixes of Gate 3 run 1 and the record's final status | PASS |
| 2 | Corrections made during verification are preserved | The same tree: the fixes of run 1's findings, and their results | PASS |
| 3 | No required work exists only on the temporary backup | Each of the eight files that the six commits change is in `1c6772c`. Outside `docs/`, the commits change only `README.md` (the audit's correction O-02); no code, test, tool's code, configuration, or workflow | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `1c6772c`'s parent is `0a9a8a5`; none of the six commits is in its history or in that of `main`, at `7172a5c` (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch from GitHub, at `1c6772c` (19:16 UTC): the documentation checker and its self-test pass, and `compare_requirements.py 0a9a8a5 --strict` reports 749 requirements before and 749 after, none added, removed, or changed; the tests ran in the machine checks (check 7) | PASS |
| 6 | Required documentation and traceability are updated | `1c6772c` holds the record's final status, PASS, the checkpoint log's row for the change, and the backup in the project state's "Branches", as active until reconciled | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `1c6772c` is on the remote branch (`git ls-remote`), pushed at 14:41 UTC, and the machine checks passed on it (Gate 1, under its table) | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `1c6772c`, the remote branch's commit (19:15 UTC) | PASS |

**Result: PASS.** The backup's work is VERIFIED AND INCORPORATED in `1c6772c`. Its last commit, `96cb67b`, is kept under the archive branch `claude/archive/unverified-backup-x9`, pushed at 19:17 UTC and checked on GitHub at that commit (`git ls-remote`, and GitHub's branch list). The deletion of `claude/unverified-backup-x9`, a git push made only if the branch was still at `96cb67b`, was refused at 19:18 UTC with HTTP 403; the branch stays at `96cb67b`, and is retired as DEC-054 (decision 4) provides.

**The ten checks before "safe to delete"** ([owner decisions 22](../handoffs/owner-decisions-22-configuration-limit-and-branch-retirement.md)'s first rule set, §5), made on 2026-11-03 for the branch, at `96cb67b`:

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | All valid unique work is preserved elsewhere | Its commits are its archive branch's (check 3), and its work is in `1c6772c` (the reconciliation above) | PASS |
| 2 | The canonical archive exists | GitHub's branch list (19:17 UTC): `claude/archive/unverified-backup-x9` at `96cb67b` | PASS |
| 3 | Commit and content parity | The branch is at the same commit as its archive branch, so its content is the same (GitHub's branch list, 19:17 UTC; `git ls-remote`, 19:18 UTC) | PASS |
| 4 | No open work depends on it | The project state's work in progress and next steps name it only as done: reconciled, archived, and retired, with nothing left to do on it | PASS, in this change |
| 5 | No active pull request depends on it | GitHub's list of the repository's pull requests, in every state: none (19:17 UTC) | PASS |
| 6 | No required verification evidence exists only on it | A backup is evidence for no gate (DEC-052, decision 3); every record is on the designated branch; and the backup's commits are on its archive branch too | PASS |
| 7 | No unresolved owner decision depends on it | The open-question register and the project state: no decision on it is pending | PASS |
| 8 | No deployment or automation depends on it | The one workflow, `.github/workflows/checks.yml`, runs on every push and pull request and names no branch; nothing is deployed; outside `docs/`, the repository does not name the branch (`git grep`) | PASS |
| 9 | Traceability is updated | The project state's "Branches", this record, and the stage record | PASS, in this change |
| 10 | A canonical rule permits retirement and deletion | DEC-052, decision 3: the backup branch is deleted once its archive is checked; DEC-054, decision 4: a later backup whose deletion is refused is retired the same way; owner decisions 10: "RETIRE / DELETE TEMPORARY BACKUP WHEN SAFE" | PASS |

So the branch is RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED. No deletion is tried again (§6): nothing shows that this environment's access has changed, and the owner has not asked. The branch is not protected on GitHub (its branch list).

**The report, A to L** (§14): A, `claude/unverified-backup-x9`; B, `96cb67b`; C, `claude/archive/unverified-backup-x9`, its work in `1c6772c`; D, parity verified (the same commit as its archive branch; reconciled above); E, RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED; F, not authoritative; G, nothing depends on it (checks 4 to 8); H, safe to delete when permitted (the ten checks); I, HTTP 403 from this session's access to GitHub (2026-11-03, 19:18 UTC); J, no retry now: no evidence that the access has changed; K, kept, retired, until a deletion is permitted, its archive branch kept for audit; L, none now: when a deletion is permitted, or the owner deletes it on GitHub, re-check that it is still retired and at `96cb67b`, delete it, and record it as RETIRED — PHYSICALLY DELETED.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Gate 1's first run (19:19 UTC): every command stopped at uv's refusal, "Required uv version `==0.12.23` does not match the running version `0.11.32`"; one line read PASS, since the refusal's exit status, 2, was the one expected of the command used wrongly | This container's uv is not the version the project requires; the script took an exit status for its cause | The required uv installed in a scratch environment; the script fails a command whose output holds uv's refusal | Gate 1, 19:20 UTC |
| The read-back before Gate 3 (DEC-057, decision 6): the Scope did not list the stage record's "Blockers" or the project state's "Known risks", which the change edits; X3's status cited Gate 2 alone, though X3's method includes Gate 3's check of the marked tests; X4's scan had counted the files tracked at `1c6772c`, read from the working tree, and so missed this record; the Gate 2 row on future-stage work said that the credential kind and its refusal were `src/`'s only trading words; the comparison over the whole stage had been run without `--strict`, in the working repository; the record had no "Checks"; and the Scope's list of the client's entries left out the compaction summary | Statements written from the plan of the change and from earlier runs, not from the diff and the commands' output | Each statement corrected from its evidence: the diff's hunks, the plan's section 8, a scan of the final tree's 288 files, the search's every hit, the comparison run with `--strict` in the clean clone, the record format's "Checks", and the session record | Checks 1 to 6; Gate 1's last row |
| The builder's first check of the preserved texts, `sha256sum -c tools/docs/preserved-texts.sha256`, reported every text as failed | The manifest's hash of a Markdown text covers its title line and the text after its status banner, not the whole file, as its header says; the checker computes it that way | The texts checked by the checker (check 1) and by check 6, which shows that no file under `docs/handoffs/` or `docs/builder/` changes | Checks 1 and 6 |

## Final status and remaining issues

PENDING.

## Environment

System Python 3.11 (`python3`) for the documentation tools; uv 0.12.23 and the project's Python 3.12 for Gate 1; git; GitHub's branch list, pull requests, and workflow runs, read through the session's GitHub tools.
