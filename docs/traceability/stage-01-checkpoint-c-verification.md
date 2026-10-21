# Stage 1, Checkpoint C — Verification Record

> **Status:** ACTIVE record of Stage 1's checkpoint C: the configuration (U4) and the security foundation (U5) of the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), with check 7 as maintained tooling and the items carried to checkpoint C ([stage record](stage-01-foundation.md), "Checkpoint C: the carried items"). Format: [traceability README](README.md). **IN VERIFICATION** until its last Gate 3 run reports.

## Identity

- **Date:** 2026-10-21
- **Stage:** 1 — FOUNDATION, checkpoint C (the plan, section 11)
- **Starts from:** commit `b9d635f` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.
- **Authorization:** [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md) (Stage 1 only); the order of work of [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md) (decision 2): checkpoints C and D after item 3 of "Next approved step".
- **Temporary backup** (DEC-052, decision 3): the work was pushed to `claude/unverified-backup-checkpoint-c` while it was being built, since a session could end with it uncommitted, first as commit `b1cca22` (2026-10-21, 04:38 UTC), and again as it changed; each commit is labelled TEMPORARY, UNVERIFIED, PENDING VERIFICATION, NOT FOR MERGE, NOT PRODUCTION-READY, NOT APPROVED, and NOT A VERIFIED CHECKPOINT, with the emergency checkpoint record of master execution constitution §132. Its reconciliation with this checkpoint's commit, its archive branch, and the deletion are recorded by the next change.

## Scope

**Added:**

| File | Unit | What it is |
|---|---|---|
| `src/atp/config/` (`__init__.py`, `_settings.py`, `_secrets.py`, `_load.py`) | U4 | The configuration: its two parts as contracts, the secret kinds, `Secret` and `SecretSource`, reading TOML in its JSON form, loading a configuration directory, the summary |
| `src/atp/cli/__init__.py` | U4 | The `atp` command, `atp config check` (D1) |
| `config/examples/` (`platform.toml`, `environments/<environment>.toml` for the six environments) | U4 | The example configuration, placeholders only (D2, GOV-017) |
| `contracts/atp.config.portable/1.0.schema.json`, `contracts/atp.config.environment/1.0.schema.json`, `contracts/atp.config.secret-declaration/1.0.schema.json` | U4 | The committed schemas of the configuration's contracts |
| `tests/config/` (`test_settings.py`, `test_load.py`, `test_secrets.py`), `tests/cli/test_cli.py` | U4 | Their tests |
| `docs/security/threat-model.md` | U5 (D2) | The threat model |
| `tools/mutation/` (`README.md`, `mutations.py`, `run.py`) | — | Check 7 as maintained tooling ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) |
| This record | — | Checkpoint C's verification record |

**Changed:** `pyproject.toml` (the `atp` script; mypy also checks `tools/mutation/`); `tests/repository/test_structure.py` (the import rules of `atp.config` and `atp.cli`, with planted samples); `tests/repository/test_no_secrets.py` (U5's extension: secret declarations in TOML files, and the shapes decided at this checkpoint); the [developer guide](../development.md) ("Configuration", the layout, the checks); the [contract conventions](../architecture/contracts.md) (the questions decided at this checkpoint); the [numerical policy](../architecture/numerical-policy.md) (N7: amounts in a configuration file are strings); the [source-of-truth map](../architecture/source-of-truth-map.md) (the two modules' rows; the configuration source; the threat model); the [security architecture](../security/security-architecture.md) (its status and its "Not yet specified" line); the [roadmap](../roadmap/roadmap.md)'s feature-status rows of U4 and U5; the [stage record](stage-01-foundation.md); [Stage 1 mutation checks as run](stage-01-mutation-checks.md) (a "Later changes" line); `docs/README.md` and this directory's index; the [project state](../project-state.md).

**Requirements:** none added, removed, or changed (check 4). Delivered by this checkpoint (the plan, section 3.1): MIG-004, MIG-010, and SEC-005 by U4, which introduces no operating value (ARCH-018); SEC-001 by U5's threat model. Prepared (section 3.2): OPS-004's six environment names and MIG-027's platform and environment identifiers as validated values; MODE-006 and SEC-004 as defence in depth only.

**Out of scope:** U7 and U8 (checkpoint D); any credential, trading capability, service, deployment, or system contract; items 4 and 5 of "Next approved step", which follow checkpoint D (DEC-052, decision 2).

**The owner's messages after the last one the previous record names** (the [owner decisions 9 adoption verification](owner-decisions-09-adoption-verification.md), whose list ends with the answers of 2026-10-20, 22:28 UTC), up to the copy that this record's last Gate 3 run reviews: none.

## Checks

The commands are those of the [developer guide](../development.md), run with uv 0.12.23 from the repository root.

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | The lockfile installs exactly | `uv sync --locked`; `uv lock --check` | PENDING |
| 2 | Lint, formatting, types | `uv run --locked ruff check`; `uv run --locked ruff format --check`; `uv run --locked mypy`; `uv run --locked mypy --config-file tools/docs/mypy.ini` | PENDING |
| 3 | Tests | `uv run --locked pytest` | PENDING |
| 4 | Documentation and requirements | `python3 tools/docs/build_index.py --check-only`; `python3 tools/docs/selftest.py`; `python3 tools/docs/compare_requirements.py b9d635f --strict` | PENDING |
| 5 | The package builds | `uv build`, archives listed | PENDING |
| 6 | U4's acceptance | The negative-path tests of `tests/config/` and `tests/cli/`, one or more for each rule of U4; `atp config check --env <name>` on the example configuration for each environment; the deliberately broken configurations of `tests/cli/test_cli.py`; and from a clean clone: `uv sync --locked`, the checks, `uv build`, and the installed command on every example environment, good and broken | PENDING |
| 7 | U5's acceptance | The repository test for secrets on the real repository, and on planted secrets in copies of the example configuration | PENDING |
| 8 | Check 7: each rule's test fails when the rule is removed | The [mutation tooling](../../tools/mutation/README.md) on clones of the working tree: checkpoint C's mutations while the work was built, then the whole list on the final tree | PENDING |
| 9 | The schema-writing command | The developer guide's command, run on the committed `contracts/` | PENDING |
| 10 | Hygiene | `git diff --check` with new files included; `git status --short --ignored`; a scan of the added lines for secrets, local and system paths, and model or session identifiers; no float literal in `src/`; no TODO, FIXME, XXX, or HACK marker in the code | PENDING |
| 11 | Dependencies | `uv.lock` compared with `b9d635f` | PENDING |

## Gates

**Verification 1 — technical:** checks 1 to 11.

**Verification 2 — architecture and consistency:** PENDING.

**Verification 3 — independent end-to-end and failure audit:** PENDING.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Check 7, checkpoint C's mutations as first run: "U4 arrays not checked" survived | No test put a refused value (a date, a time, a number with a fraction) inside a TOML array | A test of such values inside an array and inside an array of tables (`tests/config/test_load.py`) | Killed on re-run |

## Reconciliation of item 3's temporary backup

Item 3's change, commit `b9d635f`, was backed up on `claude/unverified-backup-item-3` (DEC-052, decision 3; its [verification record](owner-decisions-09-adoption-verification.md)), in two commits: `1f5bdb7`, pushed on 2026-10-20 at 23:03 UTC, after Gate 3 run 1 reported, holds the copy that run reviewed; `499dd7e`, pushed at 23:13 UTC on `1f5bdb7`, holds the tree committed after that run's fixes. Both carry the backup's labels and the emergency checkpoint record. On 2026-10-20 the builder compared the branch with `b9d635f` by [owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md)'s eight checks:

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `499dd7e`'s tree, `3b1562e`, is `b9d635f`'s | PASS |
| 2 | Corrections made during verification are preserved | `1f5bdb7` differs from `b9d635f` in six files only, those of run 1's fixes and of the record's Gate 3 result: DEC-048, DEC-052, the project state, item 3's verification record, the owner rule sets reconciliation, and the stage record | PASS |
| 3 | No required work exists only on the temporary backup | No file of `1f5bdb7` is missing from `b9d635f`, and `499dd7e` has `b9d635f`'s tree | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | Neither backup commit is in the history of `b9d635f` or of `main` (`7172a5c`) (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch, at `b9d635f`: the documentation checker and its self-test pass, and `compare_requirements.py af177dd --strict` reports no requirement added, removed, or changed; the tests ran in the machine checks (check 7 below) | PASS |
| 6 | Required documentation and traceability are updated | `b9d635f` holds item 3's record with its final status, the project state's checkpoint log row, and the backup in its "Other branches" | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `b9d635f` is on the remote branch (`git ls-remote`), and the machine checks passed on it: [run 39513605246](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/39513605246) | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `b9d635f`, the remote branch's commit | PASS |

**Result: PASS.** The backup's work is VERIFIED AND INCORPORATED in `b9d635f`. Its last commit, `499dd7e`, is kept under the archive branch `claude/archive/unverified-backup-item-3`, pushed at 23:14 UTC and checked on GitHub at that commit (`git ls-remote`; the GitHub API's reference). The deletion of `claude/unverified-backup-item-3`, a `git push` made only if the branch was still at `499dd7e`, was refused at 23:15 UTC with HTTP 403, as the deletion of checkpoint B's backup branch was (DEC-052, decision 4); the branch stays at `499dd7e`, the commit its archive keeps.

## Final status and remaining issues

**IN VERIFICATION** until the last Gate 3 run reports.

Remaining, each in its canonical place: checkpoint D, then items 4 and 5 of "Next approved step" (DEC-052); A4 of the [owner decisions 9 adoption verification](owner-decisions-09-adoption-verification.md), open, settled before any requirement is drafted under DEC-051's reading (this checkpoint drafts none); the deletion of the backup branches of checkpoint B and item 3, which this environment refuses (the project state's "Blockers").

## Environment

Python 3.12 in the project's environment (uv 0.12.23, the versions in `uv.lock`); the system Python 3.11 for the documentation tools; git.
