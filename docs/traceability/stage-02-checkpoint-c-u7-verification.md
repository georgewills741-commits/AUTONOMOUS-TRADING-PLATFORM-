# Stage 2, Checkpoint C, Unit U7 (the Quantitative Engine) — Verification Record

> **Status:** ACTIVE record of the first unit of Stage 2's checkpoint C, built before checkpoint B's venue adapters: U7, the Quantitative Engine with the Fee and Slippage Engines, in `atp.quant` (spread and depth, fees and funding, the walk of a taker order through a book, and indicators), with division in `atp.numeric` and the structure test's rule that the one module allowed floats builds no amount; the owner's message of 2026-11-21, 20:21 UTC, preserved as [owner decisions 47](../handoffs/owner-decisions-47-choice-of-the-next-work-delegated.md), with [DEC-080](../decisions/DEC-080-checkpoint-c-before-the-venue-adapters.md), which resolves OQ-36; and the reconciliation of the backup commits of the change that builds U4's parts that need no venue's data with its commit, `8116301` ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4). Its three gates: "Final status and remaining issues". The stage's status is in the [Stage 2 record](stage-02-data-foundation.md); the format follows the [traceability README](README.md).

## Identity

- **Date:** 2026-11-21 to 2026-11-22.
- **Stage:** Stage 2 (DATA FOUNDATION), checkpoint C, as the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) defines it (U6 and U7), authorized by [DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md) (decision 6) and built before checkpoint B's venue adapters by DEC-080; this change builds U7, U6 following as its own change ([Stage 2 record](stage-02-data-foundation.md), "Checkpoint C: U7, the Quantitative Engine with the Fee and Slippage Engines").
- **Starts from:** commit `8116301` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote: the change that builds U4's parts that need no venue's data ([checkpoint B (U4's venue-independent parts) verification](stage-02-checkpoint-b-u4-venue-independent-verification.md)), whose machine checks passed ([run 44941433386](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44941433386), triggered by its push: its jobs "checks" and "secrets" both passing). This record's own commit is entered in the project state's checkpoint log by the next change.
- **Temporary backup** ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 4; DEC-071): the reusable branch `claude/unverified-backup-reusable`, reused after the eight checks below. This change's first backup commit, `8f8f5dd`, has as its parent `953f2f6`, the last backup commit of the change that builds U4's parts that need no venue's data, and was pushed at 20:27:51 UTC, holding owner decisions 47, DEC-080, and the documents they change; U7's code, drafted first in a scratch clone of the repository in the builder's workspace, entered the repository with `509e587`, at 23:15:49 UTC, and its change to the time of use with `ac8d6ce`, at 23:20:28 UTC. Each later commit is a child of the branch's tip, pushed as a fast-forward and never forced, and each command that writes to the working tree runs the backup after its last write (CHECK-WRITES).
- **Interruptions:** the session's worker process was restarted at 21:25 UTC, while U7 was being designed. The working tree then equalled the tree of the backup commit `8f8f5dd`, compared file by file with the branch fetched from GitHub, so nothing was lost; nothing of U7 had yet been written outside the builder's workspace.

## Scope

**Added:** `src/atp/quant/`, a new package, SYS-03's: `_common.py` (refusals, the check of market data at the time of use, and results' evidence identifiers), `_contracts.py` (seven result contracts and three enums), `_spread.py` (spread and depth), `_fees.py` (the Fee Engine: fees and funding), `_slippage.py` (the Slippage Engine: the walk of a taker order), and `_indicators.py` (indicators, the one module allowed floats); its seven committed schemas, `contracts/atp.quant.*/1.0.schema.json`; `tests/quant/` (`test_exact.py`, `test_indicators.py`) and `tests/numeric/test_division.py`; owner decisions 47 and DEC-080; this record.

**Changed:** `atp.numeric` (`divide`, with `quantize` sharing its implementation of the directions); `atp.marketdata`'s exports (`item_time_ns` and `bar_end_ns`); the structure test (`FLOAT_ALLOWED`, the rule that a module allowed floats imports nothing from `atp.numeric`, with its planted samples, and `atp.quant`'s import rule); `tools/mutation/mutations.py` (74 entries for U7's rules, and the three N5 entries whose text moved into the shared implementation); the preserved-text manifest, `tools/docs/preserved-texts.sha256` (owner decisions 47's line); the [decision log](../decisions/README.md) (DEC-080's row); the [open-question register](../open-questions/register.md) (OQ-36 resolved); the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) (section 11: the order changed, DEC-080); the [Stage 2 record](stage-02-data-foundation.md); the [Quantitative Engine's specification](../systems/quantitative-engine.md); the [numerical policy](../architecture/numerical-policy.md); the [contract conventions](../architecture/contracts.md); the [architecture-to-repository map](../architecture/source-of-truth-map.md#architecture-to-repository) (`atp.quant`'s row); the [developer guide](../development.md)'s structure rules; the [roadmap](../roadmap/roadmap.md) (its current position, and U6's and U7's feature rows); the [project state](../project-state.md); the root README, the [documentation index](../README.md), and the [traceability README](README.md); the generated [verification matrix](verification-matrix.md).

**Requirements:** none added, removed, or changed (check 3).

**Out of scope:** U6, storage, the next change; checkpoint B's venue adapters, after each venue's verification and an approved server (OQ-34; DEC-080); incremental indicators, with U10, where measurement shows a gain (PERF-005); the account's own fee tier and rates (CORE TRADING FOUNDATION) and transfer costs (ARBITRAGE); volatility folded into slippage, which needs execution history (DIRECTIONAL TRADING and CORE TRADING FOUNDATION); drawdown, exposure, sizing, risk/reward, and arbitrage economics (the plan's section 3.2). No venue endpoint, credential, AI, or network access to a venue is used.

**The owner's messages after the last one the previous record names** (the [checkpoint B (U4's venue-independent parts) verification](stage-02-checkpoint-b-u4-venue-independent-verification.md) names none after 17:23 UTC at 19:31 UTC): the message of 2026-11-21, 20:21 UTC, preserved word for word as owner decisions 47 (DEC-080); OWNER-AFTER.

## Checks

The change's own checks, on the working tree with this change: the documentation tools with the system Python 3.11, the [developer guide](../development.md)'s checks through `uv run --locked`, the mutation runner on git clones, git, and GitHub's branch list and workflow runs.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | CHECK-1 |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | CHECK-2 |
| 3 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py 8116301 --strict` | CHECK-3 |
| 4 | The developer guide's checks, and the build | `uv run --locked` with `ruff check`, `ruff format --check`, `mypy`, `mypy --config-file tools/docs/mypy.ini`, and `pytest`; `uv build` | CHECK-4 |
| 5 | Hygiene of the change | `git diff --check 8116301`, its new files included; a scan of the lines it adds for local paths, session or model identifiers, and secrets | CHECK-5 |
| 6 | The preserved texts | The change's files against `8116301`, its new files included, under `docs/handoffs` and `docs/builder`; owner decisions 47's block against the owner's turn in the session record, byte for byte, and its manifest line | CHECK-6 |
| 7 | Quotations | The quotation script on the lines this change adds to the documents; each quotation of a source outside the repository found in it | CHECK-7 |
| 8 | Check 7, the mutation check ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6) | `tools/mutation/run.py` on git clones of the working tree, each with its remote removed, in four slices (`--slice K/4`), the runner's selection set by a wrapper around its functions: this change's entries (`S2-U7 `) with the entries of `atp.numeric._rounding`, whose code it changes; then the entries the change's documents and structure test may affect: those whose checks read the documents (by the repository test for secrets and by the documentation tools' self-test) and the structure test's from before this change | CHECK-8 |
| 9 | The reusable branch | `git rev-list --parents` on the branch fetched from GitHub; the labels, record, trailers, and marker of each commit after `953f2f6`; the workflow's runs on its pushes | CHECK-9 |
| 10 | Stale statements ([DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md), decision 4) | The stale-statement script on the active documents, and a search by subject for statements this change makes stale: OQ-36 as open, checkpoint C as not started or waiting, division not provided, no float in the code | CHECK-10 |
| 11 | U7's acceptance | The plan's U7 against the code and the tests | CHECK-11 |

## Reconciliation of the last change's temporary backup

Owner decisions 10's eight checks, on the backup commits of the change that builds U4's parts that need no venue's data, against its commit `8116301`, before the reusable branch was used again ([DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), decision 4), on 2026-11-21 from 20:22:59 to 20:24:48 UTC. The branch held 57 commits after `886884b`, the last commit the previous reconciliation checked: `96fbe3b` (2026-11-20, 21:46 UTC) to `953f2f6` (2026-11-21, 19:31 UTC), each with a single parent, the one before it, and each with the labels, the record, and the trailers, without a marker.

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `8116301`'s tree is `953f2f6`'s, `990ce9f3` (`git diff --name-only`: no difference) | PASS |
| 2 | Corrections made during verification are preserved | The same tree: the fixes of that change's Gate 3 runs 1 and 2, and its record's account of them | PASS |
| 3 | No required work exists only on the temporary backup | Each of the 34 files the commits change against `886884b`, whose tree is `395a657`'s, `f939ec4a`, is in `8116301` as in the last backup commit; the one file of an intermediate commit not in the last, DEC-079's first name, was renamed during that change | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `8116301`'s parent is `395a657`; none of the 57 commits is in its history or in `main`'s (`7172a5c`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch, at `8116301` (20:23:09 UTC): the documentation checker and its self-test pass, and 758 requirements, as at `395a657`, none added, removed, or changed | PASS |
| 6 | Required documentation and traceability are updated | `8116301` holds that change's record with its final status, PASS for its gates, and the project state, roadmap, and Stage 2 record that describe it | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `8116301` is the tip of the remote designated branch, and the machine checks passed on it ([run 44941433386](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44941433386), "checks" and "secrets") | PASS |
| 8 | Repository status is clean and consistent | `git status --porcelain` printed nothing at `8116301` (20:23:48 UTC); the branch is not protected, and the 57 runs on its pushes ran the secret test alone, each passing | PASS |

**Result: PASS.** The backup commits' work is VERIFIED AND INCORPORATED in `8116301`. The last backup commit checked is `953f2f6`. The branch is then reused by this change, its backup commits appended after `953f2f6`.

## Gates

GATES

## Findings

FINDINGS

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| The builder's review of the first draft found that its calculations checked only `eligible`, the assessment made when the data was validated, though the Stage 2 record carried to U7 the assessment at the time of use (MKD-012; U5's Gate 3, I-02) | The builder's drafting: the record's items carried to this unit read after the design, not before it | Each calculation on market data is given the time of use and the limits and assesses its data again; tests for data VALID when validated but not at the time of use, and for the arguments' types; entries `S2-U7 market data not VALID at the time of use used` and the two for the arguments | Checks 4 and 8: the mutation check on the first draft, 76 of its 79 entries killed and none surviving, stopped at 23:18 UTC and run again on the code that followed |
| The builder's review found that a sum beyond what a float holds raised `OverflowError` from `math.fsum`, and that a correlation computed in floats can come to 1.0000000000000002, which the result's contract refuses | The builder's drafting: the limits of floats not traced through the indicators | Sums taken through one helper that refuses such a sum (UNDEFINED); the correlation taken as the bound a float's rounding passes; tests with the series that gives 1.0000000000000002, found by a search, and entries | Checks 4 and 8 |
| mypy found the first draft's checks of types unreachable: `isinstance` on `Validated`, a final class, and on the types its signature already gives | The builder's drafting | Each written as `type(...) is not`, the value first bound to a name typed `object`, as code that is not typed can pass anything | Check 4 |
| The validator quarantined two of the first tests' items: a ticker with neither a bid nor an ask (MISSING_FIELD), and bars whose prices moved beyond the tests' outlier limit | The tests' data, not the code: validation refuses such items before a calculation sees them | The ticker's case removed, since validated data cannot hold it; the indicator tests' outlier limit raised | Check 4 |
| Two commands meant for the scratch clone ran in the repository, after a failed command skipped the change of directory: `ruff format` on `tests/quant` and the quant tests, at about 23:21 UTC | The builder's chaining of commands | The working tree compared with the branch at its last backup, `509e587`, file by file: equal, only ignored caches written; later commands check their directory first | Check 5 |
| The system Python 3.11, which runs the documentation tools, could not read the tests' generic functions (Python 3.12's syntax) when a script edited them | The builder's choice of interpreter | The script run with the project's Python 3.12, through `uv run --locked` | Check 4 |
| The roadmap's current position named checkpoint B's first increment only, not its second, built by the change before this one | That change's documents: its check 10 searched by subject and missed the sentence | Corrected with this change's | Check 10 |

## Final status and remaining issues

FINAL

## Environment

This cloud environment, in the United States. Python 3.12.3 for the platform, through uv 0.12.23 and `uv run --locked`; the system Python 3.11.18 for the documentation tools; git and GitHub's API for the branches and the machine checks' runs. No container, database, or network access to a venue was used.
