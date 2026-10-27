# Owner Decisions 22 — Verification Record

> **Status:** ACTIVE record of the change that preserves [owner decisions 22](../handoffs/owner-decisions-22-configuration-limit-and-branch-retirement.md) and applies it ([DEC-054](../decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md)): the limit on a configuration document's size (V-41), the retirement of the three temporary backup branches, and the reconciliation of checkpoint C's temporary backup with its commit. Format: [traceability README](README.md).

## Identity

- **Date:** 2026-10-27
- **Stage:** 1 — FOUNDATION, after checkpoint C and before checkpoint D: a correction of checkpoint C's U4, and the retirement of the backup branches, at the owner's instruction
- **Starts from:** commit `b11abe7` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next change.
- **Authorization:** [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md) (Stage 1 only); the owner's instruction of 2026-10-27, 07:59 UTC, to fix the limits on record (owner decisions 22), applied by DEC-054 (decision 2).
- **Temporary backup** ([DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3): the work was pushed to `claude/unverified-backup-owner-decisions-22` while its gates ran, since a session could end with it uncommitted, first on 2026-10-27 at 11:43 UTC, and again as it changed; each commit is labelled TEMPORARY, UNVERIFIED, PENDING VERIFICATION, NOT FOR MERGE, NOT PRODUCTION-READY, NOT APPROVED, and NOT A VERIFIED CHECKPOINT, with the emergency checkpoint record of master execution constitution §132. Its reconciliation with this change's commit, its archive branch, and the attempt to delete it are recorded by the next change.

## Scope

**Added:**

| File | What it is |
|---|---|
| `docs/handoffs/owner-decisions-22-configuration-limit-and-branch-retirement.md` | The owner's two messages of 2026-10-27, preserved word for word |
| `docs/decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md` | Their decision record |
| This record | The change's verification record |

**Changed:**

- **Code:** `src/atp/config/_load.py`: the constant `MAXIMUM_DOCUMENT_SIZE`; `_read_file` reads at most one byte more than it and refuses a larger file; `_read_toml` refuses a longer text before parsing it; the module's and the functions' docstrings. `src/atp/config/__init__.py` exports the constant.
- **Tests:** `tests/config/test_load.py` and `tests/cli/test_cli.py` ("The limit on a configuration document's size", below).
- **Tooling:** `tools/mutation/mutations.py`, eight entries for the new rules; `tools/docs/preserved-texts.sha256`, owner decisions 22.
- **Documents:** the [values register](../requirements/values-register.md) (V-41); the [developer guide](../development.md) ("Fail closed" and "What the rules do not catch"); the [threat model](../security/threat-model.md) (administrative operations, and a row of its traceability table); the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md)'s "Later changes"; the [roadmap](../roadmap/roadmap.md)'s current position and its row of U4; the [source-of-truth map](../architecture/source-of-truth-map.md) (its status and the row of `atp.config`); the [stage record](stage-01-foundation.md) (its status, fields, checkpoint C's row, and the certificate's note on the backups); the [checkpoint C verification](stage-01-checkpoint-c-verification.md)'s "Later changes"; the project state; the [owner rule sets reconciliation](owner-rule-sets-reconciliation.md) (the two rule sets); `CLAUDE.md` (the two rule sets named); the [glossary](../glossary.md) (a temporary backup's statuses among the builder status words); the [architecture overview](../architecture/overview.md)'s status (ARCH-018); the documentation index, the decision log, and the traceability README.

**Requirements:** none added, removed, or changed (check 4). V-41 is a value in the values register, as ARCH-018 requires, not a requirement.

**Out of scope:** checkpoint D; items 4 and 5 of "Next approved step"; any other change to the rules of U4 or U5; the deletion of the backup branches, which this environment refuses.

**The owner's messages after the last one the previous record names** (the [checkpoint C verification](stage-01-checkpoint-c-verification.md), whose list ends with the owner's instruction of 2026-10-27, 04:05 UTC), up to the copy that this record's last Gate 3 run reviews: the owner's question of 2026-10-27, 07:29 UTC, and the owner's instruction and two rule sets of 07:59 UTC, preserved word for word as owner decisions 22 by DEC-054; the owner's "Continue" of 10:37 UTC, procedural ([owner decisions 16](../handoffs/owner-decisions-16-short-instructions-approvals-and-questions.md)). The "Continue from where you left off." prompts of 07:40, 07:50, 07:58, and 10:37 UTC are the client's own (isMeta), not the owner's, as are the stop hook's feedback and the notices of finished background tasks.

## The limit on a configuration document's size

### Before this change

At `b11abe7`, `load_configuration` read each file whole (`Path.read_bytes`), decoded it, and parsed it with Python's TOML reader, then took its JSON form and validated it. Nothing bounded the size. The reader's memory and time grow with the square of a dotted key's parts: for each prefix of such a key it keeps a tuple as long as that prefix until the end of the section. Measured on `read_toml`, the same reading, each document read as the portable part in a fresh process (its peak resident memory, `ru_maxrss`; the process alone takes about 29 MiB):

| Document | Size | Peak resident memory | Time | Result |
|---|---|---|---|---|
| One dotted key of 8,191 parts | 16,382 bytes | 287 MiB | 0.9 s | Refused: nested too deeply to read |
| One dotted key of 16,383 parts | 32,766 bytes | 1,058 MiB | 7.8 s | The same |
| One dotted key of 32,767 parts | 65,534 bytes | 4,136 MiB | 35.7 s | The same |

The installed command, before and after this change, each run in a process whose address space was capped at 1 GiB (`RLIMIT_AS`), so that no case could exhaust the container's memory (the paper environment's file valid; `platform.toml` as below):

| `platform.toml` | Before (`b11abe7`) | After |
|---|---|---|
| 3 GiB, sparse | Exit 1, with a traceback: `MemoryError`, raised in `Path.read_bytes`, called by `_read_file` | Exit 1: "platform.toml: larger than 8192 bytes, the most a configuration file may hold" |
| 65,532 bytes: one dotted key of 32,765 parts | Exit 1, with a traceback: `MemoryError`, raised in the TOML reader (`Flags.is_`, called by `key_value_rule`) | Exit 1: the same refusal |
| 8,190 bytes: one dotted key of 4,094 parts | Exit 1: "platform.toml: nested too deeply to read" | The same |
| 8,192 bytes: a valid file | Exit 0: the summary | The same |
| 8,193 bytes: a valid file | Exit 0: the summary | Exit 1: the refusal |

Without an address-space cap, Linux can let the allocations succeed until its out-of-memory killer stops a process, possibly another one, with no Python error at all. That is inferred from Linux's documented behaviour and not reproduced, since it could stop other processes in this container. Either way the load stopped closed: `load_configuration` returns a whole configuration or raises, keeps no state, and nothing reloads a configuration at run time, so no partial or corrupted configuration could result; a traceback shows code, not the file's content, so no secret or setting was printed.

### The limit (V-41)

Its value and reason are V-41 in the values register, enforced by `MAXIMUM_DOCUMENT_SIZE` (DEC-054, decision 3). Measured at the limit, each document of exactly 8,192 characters read as the portable part (Python's traced peak, `tracemalloc`; times under tracing; and, for the four shapes that took most, the peak resident memory of a fresh process):

| Document of 8,192 characters | Traced peak | Time | Fresh process's peak resident memory | Result |
|---|---|---|---|---|
| One dotted key of 4,094 parts | 65.2 MiB | 0.27 s | 94.1 MiB | Refused: nested too deeply to read |
| A header of 2,000 parts, then 477 two-part keys | 9.4 MiB | 0.40 s | 38.3 MiB | The same |
| A header of 1,000 parts, then 700 two-part keys | 6.5 MiB | 0.30 s | 35.8 MiB | The same |
| A header of 500 parts, then 811 two-part keys | 3.8 MiB | 0.18 s | 32.7 MiB | Refused by the contract |
| A header of 4,094 parts | 3.9 MiB | 0.10 s | 33.0 MiB | Refused: nested too deeply to read |
| One dotted key of 4,080 parts in an inline table | 1.0 MiB | 0.05 s | 30.1 MiB | The same |
| 1,000 tables | 0.95 MiB | 0.05 s | 30.6 MiB | Refused by the contract |
| 900 keys | 0.65 MiB | 0.05 s | — | The same |
| 2,700 empty inline tables in an array | 0.57 MiB | 0.02 s | — | The same |
| 2,700 empty arrays in an array | 0.51 MiB | 0.02 s | — | The same |
| Inline tables 1,600 deep | 0.47 MiB | 0.02 s | — | Refused: nested too deeply to read |
| Arrays 2,700 deep | 0.32 MiB | 0.02 s | — | The same |
| 1,360 array-of-tables headers | 0.29 MiB | 0.02 s | — | Refused by the contract |

The single dotted key is the worst shape found: a key of k parts keeps tuples of about 4k² bytes, and a document of n characters holds a key of at most n/2 parts. A header followed by many keys keeps less, about n²/8 bytes. These are measurements and the reader's code, not a proof that no worse document exists; V-41's notes say so ("the worst document found").

### Tests and check 7

Added or changed in `tests/config/test_load.py`:

- `test_the_limit_on_a_document_is_v_41`: the constant is V-41's value.
- `test_a_document_at_the_limit_is_read`, and `test_a_document_longer_than_the_limit_is_refused_unread` for a longer document that is valid TOML and one that is not, both refused for their length.
- `test_the_reading_of_the_worst_document_within_the_limit_is_bounded`: the longest dotted key a document within the limit holds is refused, and its reading's traced peak stays under 80 MiB.
- `test_a_file_that_cannot_be_read_is_refused`, now for a file that cannot be opened and one whose reading fails, both inside the reading's boundary; the test it replaces made `Path.read_bytes` fail, which the reading no longer calls.
- `test_a_file_at_the_limit_loads_and_a_larger_one_is_refused`, for each of the two files: one at the limit, ending with a character of two bytes, loads; one larger by such a character, which the bounded read cuts, is refused for its size and not reported as text that is not UTF-8.
- `test_a_file_larger_than_the_limit_is_refused_before_anything_else`: a file that is too large, is not TOML, and holds a declared secret's value is refused for its size alone, with nothing from the file in the refusal.
- `test_a_file_larger_than_the_limit_is_not_read_in_full`: a sparse file of 64 MiB is refused with a traced peak under 1 MiB (13,397 bytes when measured), where a full read would take 64 MiB.
- `test_a_refused_load_leaves_nothing_behind`: after three refused loads (too large, not TOML, not UTF-8), the valid directory loads with the same summary as before them.
- Documents longer than the limit in earlier tests: the binary integer of 15,000 digits is now refused for its length (a binary integer that the JSON form cannot convert has more than 14,000 digits, so it no longer fits in a document); the header 10,000 deep is now 4,000 deep, still refused as nested too deeply. In the property test of the reading, the inline tables 3,000 deep are now 1,000 deep and the header 10,000 deep is 3,000 deep, both still deeper than the reading goes while Hypothesis raises the recursion limit to about 2,000 (measured: 2,017); the length is a step of its statistics.

In `tests/cli/test_cli.py`, one broken configuration more: a `platform.toml` larger than the limit, holding a secret's value, is refused with exit 1, the refusal on standard error, and no secret.

Check 7's list has eight new entries, each removing one part of the limit: "U4 the limit on a document changed", "U4 a file read in full", "U4 a file read only to the limit", "U4 a file larger than the limit accepted", "U4 a file at the limit refused", "U4 a file opened and read outside the boundary", "U4 a document longer than the limit parsed", and "U4 a document at the limit refused".

### The owner's report, A to N (owner decisions 22, the second rule set, §17)

| Item | Answer |
|---|---|
| A. Exact root cause | `_read_file` read each file whole, and the TOML reader's memory grows with the square of a dotted key's parts; no limit bounded either, since U4 introduced no operating value (the Stage 1 plan, U4) |
| B. Exact failure path | `MemoryError`, raised in `Path.read_bytes` for a file too large to read, or in the TOML reader for a document too large to parse (`Flags.is_`, from `key_value_rule`), and not caught, so the command ended with a traceback and exit 1. Without an address-space limit, the kernel's out-of-memory killer may stop the process instead (inferred) |
| C. Partial state | None: `load_configuration` returns a whole configuration or raises, and keeps no state |
| D. Corruption of the active configuration | Not possible: nothing reloads a configuration; a process loads it once, at start |
| E. Secrets in the output | None: the traceback shows code, not the file's content; the refusals hold nothing from the file (tested) |
| F. Process or load | Before: the process ended with an uncaught `MemoryError`, or was killed (inferred), and loading the configuration is the start of the process. After: the load is refused with `ConfigurationError`, and the command exits 1 with the refusal |
| G. Canonical requirement | Constitution Rules 108 (configuration validated before use) and 150 (no uncontrolled memory growth); the master execution constitution, §115; the Stage 1 plan's U4, "Fail closed"; MIG-010 for the configuration; ARCH-018 for the value |
| H. Classification | MINOR DEFECT. Against Rule 150 and U4's clean refusal, a file of tens of kilobytes could exhaust the process's memory. But the path is local and its files are the administrator's, the load still failed closed, no partial state or leak was possible, and Stage 1 runs no service. Checkpoint C's Gate 3 run 3 classified it as non-blocking (C-18), and the measurements here show a smaller file suffices, not a new exposure |
| I. A fix required before Foundation exits | Not by the exit criteria, under that classification; fixed now at the owner's instruction (DEC-054, decision 2) |
| J. Remediation | V-41: a bounded read that refuses a larger file without reading it in full, and a length check before parsing (DEC-054, decision 3) |
| K. Tests | "Tests and check 7" above |
| L. Verification | "Gates" below |
| M. Documentation | V-41 in the values register; the developer guide; the threat model; the Stage 1 plan's later changes; the roadmap; the source-of-truth map; the stage record; checkpoint C's record; the docstrings of `atp.config` |
| N. What remains | The bound is measured, not proven (V-41's notes). A host with less memory free than the worst case found needs fails as at any allocation, with `MemoryError`, a failure of the host. No last known good configuration is kept, since nothing reloads one (DEC-054, decision 3) |

## The temporary backup branches

### The ten checks before "safe to delete" (owner decisions 22, the first rule set, §5)

Made on 2026-10-27 for each of `claude/unverified-backup-checkpoint-b` (at `ee84f26`), `claude/unverified-backup-item-3` (at `499dd7e`), and `claude/unverified-backup-checkpoint-c` (at `5ef914e`):

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | All valid unique work is preserved elsewhere | Each branch's commits are its archive branch's (check 3). Its work is in the designated branch's commit: no file of its last commit is missing from that commit (`git diff --name-status`). Item 3's last tree is `b9d635f`'s; checkpoint B's differs from `4816059` in four documents, and checkpoint C's from `b11abe7` in five, each later corrected or updated there (the reconciliations of checkpoint B and below) | PASS for each |
| 2 | The canonical archive exists | GitHub's branch list: `claude/archive/unverified-backup-checkpoint-b` at `ee84f26`, `claude/archive/unverified-backup-item-3` at `499dd7e`, `claude/archive/unverified-backup-checkpoint-c` at `5ef914e` | PASS for each |
| 3 | Commit and content parity | Each temporary branch is at the same commit as its archive branch, so its content is the same (GitHub's branch list; `git ls-remote`) | PASS for each |
| 4 | No open work depends on it | The project state's work in progress and next steps name none of them; the work goes on on the designated branch | PASS for each |
| 5 | No active pull request depends on it | GitHub's list of the repository's pull requests, in every state: none | PASS for each |
| 6 | No required verification evidence exists only on it | A backup is evidence for no gate (DEC-052, decision 3); every record is on the designated branch; and the backup's commits are on its archive branch too | PASS for each |
| 7 | No unresolved owner decision depends on it | The [open-question register](../open-questions/register.md) and the project state: no decision is pending | PASS for each |
| 8 | No deployment or automation depends on it | The one workflow, `.github/workflows/checks.yml`, runs on every push and pull request and names no branch; nothing is deployed; outside `docs/`, the repository names none of these branches (`git grep`) | PASS for each |
| 9 | Traceability is updated | The project state's "Branches", this record, the stage record, and DEC-054 | PASS for each, in this change |
| 10 | A canonical rule permits retirement and deletion | [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3: the backup branch is deleted once its archive is checked; [owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md): "RETIRE / DELETE TEMPORARY BACKUP WHEN SAFE" | PASS for each |

So each branch is SAFE TO DELETE WHEN PERMITTED. No deletion was tried again (§6): nothing shows that this environment's access has changed, and the owner has not asked. The branches are not protected on GitHub (its branch list), so the refusal comes from this session's access, which accepts pushes that create branches but refuses deletions.

### The final verification (§13)

| Check | Result |
|---|---|
| No active workflow references a retired branch | PASS: check 8 |
| No current stage uses one | PASS: check 4 |
| No valid work exists only on one | PASS: check 1 |
| The canonical archives and checkpoints are intact | PASS: the archive branches (check 2); `4816059`, `b9d635f`, and `b11abe7` on the designated branch, whose head is `b11abe7` on GitHub |
| Traceability is intact | PASS: check 9 |
| The documentation reflects reality | PASS: no document calls a branch deleted; the project state, the stage record, and DEC-054 state each branch's status |
| No duplicate authority was introduced | PASS: no branch, register, or rename added; the designated branch is the one authoritative state |
| No misleading "deleted" status exists | PASS: each branch is RETIRED — DELETION BLOCKED |
| The 403 limitation is documented | PASS: the project state's "Branches" and "Blockers" |
| Future deletion conditions are clear | PASS: DEC-054, decision 4, and the project state's "Final disposition" |

### The report, A to L, for each branch (§14)

| Item | `claude/unverified-backup-checkpoint-b` | `claude/unverified-backup-item-3` | `claude/unverified-backup-checkpoint-c` |
|---|---|---|---|
| A. Branch name | As headed | As headed | As headed |
| B. Current commit | `ee84f26` | `499dd7e` | `5ef914e` |
| C. Canonical archive and replacement | `claude/archive/unverified-backup-checkpoint-b`; its work in `4816059` | `claude/archive/unverified-backup-item-3`; `b9d635f` | `claude/archive/unverified-backup-checkpoint-c`; `b11abe7` |
| D. Parity actually verified | Yes: the same commit as its archive branch, compared on GitHub on 2026-10-27; its work reconciled by owner decisions 10's eight checks on 2026-10-13 | Yes: the same; reconciled on 2026-10-20 | Yes: the same; reconciled on 2026-10-27 (below) |
| E. Lifecycle status | RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED | The same | The same |
| F. Authoritative | No | No | No |
| G. Anything depending on it | Nothing (checks 4 to 8) | Nothing | Nothing |
| H. Safe to delete | Yes, when permitted (the ten checks) | Yes, when permitted | Yes, when permitted |
| I. Why deletion failed | HTTP 403 from this session's access to GitHub; a git push of the deletion was also cut off five times on 2026-10-20 | HTTP 403 (2026-10-20, 23:15 UTC) | HTTP 403 (2026-10-27, 06:15 UTC) |
| J. Retry now | No: no evidence that the access has changed (§6) | No | No |
| K. Keep it | Kept, retired, until a deletion is permitted; its archive branch is kept for audit | The same | The same |
| L. Next action | None now. When a deletion is permitted, or the owner deletes it on GitHub: re-check that it is still retired and at `ee84f26`, delete it, and record it as RETIRED — PHYSICALLY DELETED | The same, at `499dd7e` | The same, at `5ef914e` |

## Reconciliation of checkpoint C's temporary backup

Checkpoint C, commit `b11abe7`, was backed up on `claude/unverified-backup-checkpoint-c` while it was built and verified (DEC-052, decision 3; its [verification record](stage-01-checkpoint-c-verification.md), "Identity"), in 13 commits, `b1cca22` (2026-10-21, 04:38 UTC) to `5ef914e` (2026-10-27, 05:18 UTC), the last holding the tree Gate 3 run 4 reviewed. Each carries the backup's labels and the emergency checkpoint record. On 2026-10-27, from 06:13 UTC, the builder compared the branch with `b11abe7` by [owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md)'s eight checks:

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `b11abe7` differs from `5ef914e` in five documents only, those of Gate 3 run 4's wording fixes and of the record's result: the project state, the roadmap, the threat model, checkpoint C's record, and the stage record (`git diff --name-status`) | PASS |
| 2 | Corrections made during verification are preserved | Those five documents hold run 4's fixes (C-21 to C-25) and the record's final status; no code, test, tool, configuration, or lockfile differs | PASS |
| 3 | No required work exists only on the temporary backup | No file of `5ef914e` is missing from `b11abe7` | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | None of the 13 backup commits is in the history of `b11abe7` or of `main` (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch from GitHub, at `b11abe7`: the documentation checker and its self-test pass, and `compare_requirements.py b9d635f --strict` reports no requirement added, removed, or changed; the tests ran in the machine checks (check 7 below) | PASS |
| 6 | Required documentation and traceability are updated | `b11abe7` holds checkpoint C's record with its final status, the project state's checkpoint log row, and the backup in its "Other branches" | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `b11abe7` is on the remote branch (`git ls-remote`), and the machine checks passed on it: [run 40459753026](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/40459753026), completed 06:14 UTC | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `b11abe7`, the remote branch's commit | PASS |

**Result: PASS.** The backup's work is VERIFIED AND INCORPORATED in `b11abe7`. Its last commit, `5ef914e`, is kept under the archive branch `claude/archive/unverified-backup-checkpoint-c`, pushed at 06:15 UTC and checked on GitHub at that commit (`git ls-remote`; the GitHub API's reference). The deletion of `claude/unverified-backup-checkpoint-c`, a git push made only if the branch was still at `5ef914e`, was refused at 06:15 UTC with HTTP 403; the branch stays at `5ef914e`, retired ("The temporary backup branches" above).

## Checks

The commands are those of the [developer guide](../development.md), run with uv 0.12.23 from the repository root.

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | The lockfile installs exactly | `uv sync --locked`; `uv lock --check` | PASS; `uv.lock` and `pyproject.toml` are unchanged from `b11abe7` |
| 2 | Lint, formatting, types | `uv run --locked ruff check`; `uv run --locked ruff format --check`; `uv run --locked mypy`; `uv run --locked mypy --config-file tools/docs/mypy.ini` | PASS: 41 files formatted; 37 source files under strict mypy (`src/`, `tests/`, `tools/mutation/`); the documentation tools' 4. Each command run on its own and its exit status read |
| 3 | Tests | `uv run --locked pytest` | CHECK3_RESULT |
| 4 | Documentation and requirements | `python3 tools/docs/build_index.py --check-only`; `python3 tools/docs/selftest.py`; `python3 tools/docs/compare_requirements.py b11abe7 --strict` | PASS: the generated files current; the self-test passes; 734 requirements before and after, 0 added, removed, or changed |
| 5 | The package builds | `uv build`, the wheel listed | PASS: the wheel holds `atp/config/_load.py` with `MAXIMUM_DOCUMENT_SIZE` and no tests, documentation, tools, examples, or schemas |
| 6 | The limit's acceptance | The tests of "The limit on a configuration document's size" above; the installed command, before and after this change, on the oversized files of the table above, with the process's address space capped at 1 GiB; the measurements at the limit | PASS: each file larger than the limit is refused with the size refusal and no traceback; files at the limit load; the worst document found at the limit is refused within the measured bounds |
| 7 | The property tests' reach | `--hypothesis-show-statistics` on the property test of the reading; and C-16's acceptance: each of the seven mutations that remove a class of failure from the two reading boundaries, run against the two property tests alone, on a clone of the working tree | PASS: the 100 examples reach every step: the reader's refusal 26.7%, the JSON form 21.9%, the length 16.2%, validation 10.5%, nested too deeply 6.7%, the amount constructor 6.7%, an integer too long 5.7%, read 1.0% (the rest invalid examples); all seven mutations killed by the property tests alone, which pass unmutated |
| 8 | Check 7: each rule's test fails when the rule is removed | The [mutation tooling](../../tools/mutation/README.md): the whole list, 437 mutations (checkpoints A and B's 349, checkpoint C's 80, and this change's 8), in four slices on four clones of the working tree (`--slice K/4`) | CHECK8_RESULT |
| 9 | The preserved text | The round trip of owner decisions 22 against the session record: each text block equal to the owner's message of its minute, found as a plain user turn that is not the client's own (isMeta); the manifest's hash computed independently | PASS: both blocks equal, byte for byte (282 and 23,337 characters); the manifest line's hash, `6b287f32dcdb…`, equals the one computed from the title line and everything after the banner |
| 10 | Hygiene | `git diff --check` with the new files included; `git status --short --ignored`; a scan of the added lines for secrets, local and system paths, and model or session identifiers; no float literal in `src/` (by `ast`, with Python 3.12); no TODO, FIXME, XXX, or HACK marker in `src/`, `tests/`, `tools/`, `contracts/`, `config/`, `pyproject.toml`, or `.github/` | PASS: whitespace clean, except three lines of the owner's messages in owner decisions 22, which end with the owner's own spaces and are kept as received (DEC-054, decision 1); only intended files and ignored caches; nothing found |
| 11 | Dependencies | `uv.lock` compared with `b11abe7` | PASS: unchanged; the bounded read uses the standard library |
| 12 | The branches on GitHub | GitHub's branch list and pull request list, and `git ls-remote origin` (reads) | PASS: the eight branches and their commits as "The temporary backup branches" above states; no pull request in any state |

## Gates

**Gate 1 (Verification 1, technical): GATE1_RESULT**

**Gate 2 (Verification 2, architecture and consistency), the builder's pass: PASS**, after the corrections in "Failures and fixes".

- **The baseline:** owner decisions 22 and DEC-054; the Stage 1 plan's U4 ("Fail closed") and ARCH-018; DEC-020's value classes and the values register's rule for adding a value; DEC-052 (decisions 3 and 4) and owner decisions 10's lifecycle and eight checks; DEC-045 (decisions 1 to 7); DEC-047 (decision 7) and DEC-048 (decision 3), for the owner's messages; DEC-051 (decision 3), for rule sets kept in force through their decision records.
- **No duplicate control and one source:** no limit on a configuration's size, an input's size, or a resource existed (searched in the requirements, the system rules, the values register, the code, and the tests); one value, V-41, in the values register; one constant, which the pinned test ties to it. The developer guide, the threat model, the plan, the roadmap, the source-of-truth map, and the stage record name V-41 without repeating its value; the decision record states the alternatives' sizes, not V-41's value.
- **Claims only what is enforced** (DEC-045, decision 4): "refused without being read in full" is enforced by the bounded read and tested by the traced peak of a sparse file of 64 MiB; "before it is parsed" by the length check, tested; "bounds the memory and time" is stated as a measurement, not a proof, with the worst document found.
- **The sweep for statements of the corrected fact** through `src/`, `tests/`, `tools/`, and the documents: the developer guide, the threat model, `_read_toml`'s docstring, and the property test's comment stated the memory limit, and are corrected; checkpoint C's record states it as found then and gets a "Later changes" line. The comment of the repository test for secrets' property test, "short of exhausting the process's memory", stays true: that test reads the repository's own files without the limit, and must, since `uv.lock` is larger than it.
- **The branches:** no branch, register, or rename added; no document calls a branch deleted; the project state's "Other branches" points to its new "Branches" section, where every earlier reference to "Other branches" still leads.
- **The owner's messages:** both kept byte for byte (check 9); the record names every owner message since checkpoint C's record's last.

**Gate 3 (Verification 3, independent review): GATE3_RESULT**

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Check 2: ruff reported two implicit string concatenations inside collections (ISC004) and an `__enter__` that does not return `Self` (PYI034) in the new tests; the formatter would have reformatted two files | Written without running the checks first | Parentheses around the concatenations; `Self`; the formatter applied | Check 2 passes |
| Gate 2, the builder's review of the new tests before their first run: the test of a document longer than the limit built a text two characters longer, and its "valid" case ended with a bare key, which is not TOML | The text's length and content were not checked | The text is exactly one character longer, asserted; the valid case ends with a comment | Check 3 |
| Gate 2, the builder's sweep: statements of the memory limit in the developer guide, the threat model, `_read_toml`'s docstring, and the property test's comment | The fact is stated in several places | Each states the enforced behaviour, as "Gate 2" above says | Check 4 |
| Gate 2, the builder's sweep of the project state: checkpoint C was missing from its status table and from "Completed work", which stopped at 2026-10-07; "Decisions in effect" read DEC-001 to DEC-052, though DEC-053 existed; "Not verified" said that no configuration or command exists yet | Earlier changes updated the continuation contract's other fields and "Recent changes", not these | The rows and entries added, the decisions in effect DEC-001 to DEC-054, and "Not verified" naming what checkpoints B and C and this change verify | Check 4 |
| The builder's answer to the owner's question of 07:29 UTC said that reaching the limit takes a multi-gigabyte file, and named a limit of 1 MB as an example | Stated before the reading was measured | DEC-054's context corrects it from the measurements; the report to the owner says so | — |
| Check 8's first fingerprint of the working tree differed from its clones' | The working tree holds the documentation tools' ignored ruff cache, which a clone does not | The fingerprint without ignored caches, `2df73b85142546c5`, equals each clone's | — |

## Final status and remaining issues

FINAL_STATUS

## Environment

Python 3.12 in the project's environment (uv 0.12.23, the versions in `uv.lock`); the system Python 3.11 for the documentation tools; git.
