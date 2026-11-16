# Workflow and Efficiency — the Workflow's Change, and the Owner's Messages of 2026-11-11 and 2026-11-16

> **Status:** ACTIVE record of the change that makes the workflow's change of [DEC-064](../decisions/DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md) (decision 2); preserves the owner's questions of 2026-11-11 and messages of 2026-11-16 word for word, keeps the directive on efficiency in force through the existing rules ([DEC-069](../decisions/DEC-069-owner-questions-and-efficiency-directive.md)), and maps the permanent trading rules to the canonical requirements ([DEC-070](../decisions/DEC-070-permanent-trading-rules-mapped.md)); and reconciles the last change's temporary backup with its commit and retires its branch ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 6). Its three gates: "Final status and remaining issues". Format: [traceability README](README.md).

## Identity

- **Date:** 2026-11-16
- **Stage:** between Stage 1, COMPLETE, and Stage 2 (DATA FOUNDATION), whose planning is authorized and whose implementation is not ([DEC-067](../decisions/DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md), decision 2): the workflow's change that DEC-067 places after the mapping of owner decisions 29 and before Stage 2's entry gate and plan. It changes the workflow, one sentence the documentation tools generate, and documentation; it starts no stage's work.
- **Starts from:** commit `2618740` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote: the mapping's commit ([universal opportunity mapping](universal-opportunity-mapping-2026-11-11.md)), whose machine checks passed ([run 43932077424](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/43932077424), from 18:44 to 18:46 UTC, every step passing, "Tests" included; the only run for that commit). This record's own commit is entered in the project state's checkpoint log by the next change.
- **Temporary backup** (DEC-057, decision 4): `claude/unverified-backup-workflow`, pushed as the work changed, each command that writes to the working tree ending with the backup. Each commit carries the seven labels of [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4), the emergency checkpoint record of master execution constitution §132, and `[skip ci]` in its subject, but one (check 7), and the repository test for secrets runs on its snapshot before its push (DEC-064, decision 2). Its reconciliation with this change's commit is recorded by the next change.

## Scope

**Added:** this record; owner decisions 35, 36, and 37, each taken by script from the session record and equal to it (check 6); DEC-069 and DEC-070.

**Changed:** the workflow (`.github/workflows/checks.yml`: two jobs, "secrets" and "checks", and its header comment); the sentence on tests that `tools/docs/build_index.py` writes into the [verification matrix](verification-matrix.md), and the matrix; the [documentation tools' README](../../tools/docs/README.md) (the machine checks' sentence); the manifest of preserved texts (`tools/docs/preserved-texts.sha256`, three lines); the [developer guide](../development.md) (its three statements on the machine checks); the [threat model](../security/threat-model.md) (SEC-005's row); the [architecture governance](../architecture/architecture-governance.md) (its status line); DEC-064 (a "Later changes" line); the [owner rule sets reconciliation](owner-rule-sets-reconciliation.md) (its status line; a section for owner decisions 36; its seventh gap; a line of its result); `CLAUDE.md` (the owner's rule sets in force: owner decisions 36); the [decision log](../decisions/README.md); the [documentation index](../README.md) (its links); the [traceability README](README.md) (a row for this record); the [roadmap](../roadmap/roadmap.md) (its current position; the stages table's row for DATA FOUNDATION); the [stage record](stage-01-foundation.md) (its status line; its "Stage" table's rows "Security status" and "Next stage"; the certificate's "Remaining future work"); and the project state (its "Last updated"; its status line; under "Current stage", three entries, added; under "Current objective", where the work is now; the continuation contract's rows "Current task", "In progress, possibly partial", "Blocked", "Stage convergence", "Decisions in effect", "Other branches", "Known risks", and "Next safe action"; "Branches": a fifteenth branch, the archive branches, and the active backup; "In-progress work"; "Recent decisions"; "Recent changes"; "Next approved step"; the checkpoint log).

**Requirements:** none added, removed, or changed (check 3).

**Out of scope:** Stage 2's entry gate and plan, the next change; any implementation of a requirement.

**The owner's messages after the last one the previous record names** ([universal opportunity mapping](universal-opportunity-mapping-2026-11-11.md): none after the owner's "Continue" of 2026-11-11, 04:16 UTC; its final status names the later ones), up to the copy that this record's last Gate 3 run reviews: the owner's "Okay" of 2026-11-11, 11:50 UTC, procedural ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7); three questions of 11:52, 12:00, and 12:04 UTC, preserved as owner decisions 35 (DEC-069); the owner's "Try again" of 2026-11-16, 18:21 UTC, procedural; a permanent directive of 18:34 UTC, delivered while the builder worked, preserved as owner decisions 36 (DEC-069); and permanent trading rules of 18:54 UTC, delivered while the builder worked, preserved as owner decisions 37 (DEC-070). Since that record's copy (2026-11-11, 05:19 UTC), the stop hook's feedback, the client's notices of a stopped run (05:27 UTC) and of the worker's restarts (05:38, 12:20, and 17:56 UTC), the report of that record's Gate 3 run 1 as the client delivered it (12:07 UTC), the summary the client wrote when it compacted the conversation (12:11 UTC), the reports of two read-only agents of this session as the client delivered them (2026-11-16, 18:40 and 18:57 UTC), and the notices of background tasks are the client's own.

## Checks

The change's own checks, on the working tree with this change: the documentation tools with the system Python 3.11, git, and, since the workflow and a tool change, the [developer guide](../development.md)'s checks through `uv run --locked`.

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | PASS: exit 0; against `2618740`, the regeneration changes one generated file, the verification matrix, whose sentence on tests now states the workflow's rule and whose SEC-005 row now names the workflow, which its `Requirements:` comment now lists |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | PASS: 61 cases and the control |
| 3 | No requirement added, removed, or changed | `python3 tools/docs/compare_requirements.py 2618740 --strict` | PASS: 757 requirements before and after; none added, removed, or changed |
| 4 | The developer guide's checks | `uv run --locked` with `ruff check`, `ruff format --check`, `mypy`, `mypy --config-file tools/docs/mypy.ini`, and `pytest` | PASS: each exits 0; 1,108 tests pass |
| 5 | Hygiene of the change | `git diff --check 2618740`, its new files included; a scan of the lines it adds for local paths, session or model identifiers, and the shapes of secrets | PASS: `git diff --check` reports only the four lines of owner decisions 35 that end with the owner's spaces (DEC-069, decision 1); the scan finds none |
| 6 | The preserved texts unchanged, and the new ones as received | `git diff --name-only 2618740 -- docs/handoffs docs/builder`; the round trip of owner decisions 35, 36, and 37 against their messages in the session record, by the documentation tools' rule for preserved texts; their manifest lines (check 1) | PASS: no existing file there changes; the three new texts equal their messages byte for byte (18, 104, and 43 characters; 8,131; and 20,958), and their manifest lines hold |
| 7 | The workflow on GitHub | One backup commit, `01efb7e`, pushed without the marker, so that GitHub runs the new workflow from its snapshot on a temporary backup branch | PASS: [run 43933628611](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/43933628611) succeeded: the job "secrets" ran and passed, its step "Repository test for secrets" included, and the job "checks" was skipped. A push to the designated branch runs both jobs, as this change's commit will show; a pull request runs both by the job's first condition, and none is made, no pull request having been asked for |
| 8 | Quotations | A script: every quoted string in the lines this change adds, looked for in the owner's texts under `docs/handoffs/`; the quotations of the builder's answers of 2026-11-11, looked for in the session record | PASS: each quotation of the owner is in the owner's texts; each quotation of the builder's answers is in the session record; the other quoted strings name rows, sections, or values |
| 9 | The trading rules' mapping cites what exists | A script: each of the 57 identifiers the mapping below cites, looked up in the registry or the System Rules Register, and V-44 in the values register, with its title | PASS: each exists, and its title names the point it is cited for |
| 10 | Stale statements (DEC-069, decision 4) | `git grep -n -E "workflow's change\|the next change\|fourteen\|unverified-backup-owner-decisions-29\|skip ci\|Last updated" -- docs CLAUDE.md README.md tools/docs/README.md`, every line read | PASS: each current statement of the facts this change changes is updated (Scope); dated statements, decision texts, and the Stage 1 record's count of its own backups stay as written |

## The workflow's change

[DEC-064](../decisions/DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md) (decision 2) set it, for after Stage 1's exit: the machine checks monitor SEC-005 on every push, whatever their other checks find, and a temporary backup commit no longer needs a marker in its message. The workflow now has two jobs, each with read-only permissions, no repository secret, and the same pinned actions and uv version:

- **secrets:** the repository test for secrets, `tests/repository/test_no_secrets.py`, on every push and every pull request;
- **checks:** every check of the developer guide but `uv build`, on every pull request and on every push but one to a temporary backup branch (`claude/unverified-backup-*`) or an archive branch (`claude/archive/*`), whose snapshots are evidence for no gate ([DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 3).

A backup push therefore runs only the secret test, which passes unless a secret is committed, so it sends no failure email. The builder still runs the same test on each backup snapshot before its push. From this change's commit on, backup commits carry no marker; the designated branch's pushes and every pull request run every check, as before. The developer guide, the threat model, the documentation tools' README, and the matrix's generated sentence say so.

## The report on efficiency, A to H (owner decisions 36, §12)

The builder gave it in the session on 2026-11-16 at 18:40 UTC. Its evidence, measured from the session record's usage fields, the client's notices, and the repository:

- **A. Stage and task:** Stage 1 is COMPLETE; Stage 2's planning is authorized, and its implementation is not (DEC-067). The task then: completing the mapping of owner decisions 29.
- **B. Where tokens and time go:**
  1. The main session: 2,081 calls from 2026-10-28 to 2026-11-16, 18:38 UTC, each carrying the conversation, 463,113 tokens of context on average, 947,239,363 cached tokens in all (the report said 2,120 calls and about 455,000 tokens, having counted the client's 39 notices of a usage limit, which call no model).
  2. Gate 3: 18 runs from 2026-11-02 to 2026-11-11, from 315,902 to 456,505 tokens each as the client reported them, 7,012,455 in all: about two runs a change, and six for the certificate's.
  3. What the runs found: of the 158 findings in the nine records written since 2026-11-02 (the checkpoint D backup record, begun 2026-10-29, adds 7, all documentation issues), 148 are documentation issues; the others are 6 non-blocking improvements, 2 blocking defects, a regression caused by a fix, and a test-infrastructure issue (the report said 108 of about 110, and no code defect, having counted six of the nine records; corrected here). Many are statements a change left stale, because the same facts are restated in many active documents and each change must update each statement of them: the project state alone is 188,309 bytes, with a line of 7,113 characters.
  4. Seventeen committed decision records are titled as preserving the owner's messages; nine of them keep questions or short messages and change nothing (the report said eighteen, counting a draft of DEC-069, and that each only preserves a message; corrected here).
  5. Fixed context: `CLAUDE.md` and the six builder texts it loads, 174,337 bytes on every call (174,511 with this change), an estimated 44,000 tokens at about four bytes a token.
  6. The usage limits' stops: from 2026-10-29 to 2026-11-02, from 2026-11-06 to 2026-11-09, and from 2026-11-11 to 2026-11-16 (the project state's "Stage convergence").
  Not measured: how cached tokens count toward the owner's plan's limits.
- **C. The existing mechanisms:** the owner rule sets reconciliation's section for owner decisions 36.
- **D. Applied within existing authority:** the mapping committed after its one Gate 3 run, whose fixes it had specified and judged to need no further run (DEC-045, decision 5); the next pieces, this change, in one change with one Gate 3 cycle; the model, the tools, and the context matched to each task, with two read-only checks given to a smaller model, each finding checked by the builder; the scan for stale statements (check 10); records that reference the canonical place instead of restating it; reviews kept on the strongest model, scoped to what changed (DEC-069, decision 4).
- **E. Changes needing the owner's approval:** none; loading the builder texts on demand and lighter reviews were considered and not recommended (DEC-069's alternatives).
- **F. Controls kept:** the three gates, the backups, the secret test, the machine checks, and every requirement and decision.
- **G. Measurement:** each change's record states its Gate 3 runs with their tokens, its blocking findings per run, and the main session's calls and average context (DEC-069, decision 4); the baseline is above.
- **H. Next action:** the mapping's commit, then this change, then Stage 2's entry gate and plan.

The two read-only checks: the mapping's line-by-line coverage check, 167,216 tokens; and the trading rules' mapping below, 173,480 tokens, each as the client reported it.

## The trading rules of 2026-11-16 mapped (DEC-070)

Each section of [owner decisions 37](../handoffs/owner-decisions-37-permanent-autonomous-trading-rules.md) against the requirements, values, system rules, and builder texts that state it, mostly through the [universal opportunity mapping](universal-opportunity-mapping-2026-11-11.md)'s rows, named by owner decisions 29's sections. Status in owner decisions 9's classes (Rule 8); none is implemented, each being built by the stage the roadmap places it in.

| Section | Already stated by | Status |
|---|---|---|
| Preamble, §1, §15, §17, §18: inspect first; classify; no duplicate engines, agents, services, or policy documents; reuse, strengthen, one source of truth, traceability, root cause, continuity, minimal change; permanent enforcement; the order of work and the report | The mapping's rows for §1, §2, and §17 to §20; constitution Rules 35 to 41, 66, and 191 to 193; owner decisions 9, Rules 0 to 5, 10, 16, 17, 19, and 23; owner decisions 17, Rule 0 | EXISTING (builder) |
| §2: the philosophy; discovery kept apart from evaluation, allocation, execution, and risk | The §3 rows: PLT-006, PLT-022, OPP-017, SR-02 | EXISTING REQUIREMENT |
| §3: the daily objective of about 1.2% net or higher, its four scenarios, and its restrictions | The §3 and §12 rows: V-44 and PFC-021, a measurement only, as the owner chose on 2026-11-10; SR-19, PLT-007, PLT-008, TNP-013, TNP-014, TNP-026, RSK-044, RSK-047, CAP-034 | EXISTING REQUIREMENT |
| §4, §9: discovery with no minimum percentage; tiers, not barriers; the dynamic threshold | The §4 rows: OPP-018, OPP-022, OPP-023, TNP-019, TNP-022, CAP-043 | EXISTING REQUIREMENT |
| §5: small gains; returns never summed; no trade quota | The §8 and §9 rows: PFC-020, TNP-008, TNP-013, PLT-008 | EXISTING REQUIREMENT |
| §6: continuous, cost-aware discovery within rate limits; several opportunities at once; at least three exchanges | The §5 and §6 rows: OPP-001, OPP-017, OPP-023, OPP-024, PERF-017, EXA-005 (five initial venues), EXA-007, EXA-013 | EXISTING REQUIREMENT |
| §7: net profitability after every cost, each counted once; the same checks for small opportunities; no competing engine | The §7 rows: TNP-017 to TNP-020, TNP-022, TNP-031 | EXISTING REQUIREMENT |
| §8: allocation by risk-adjusted value; no double commitment; emergency reserves only as policy permits; under the risk authority | The §8 row: CAP-006, CAP-008, CAP-017, CAP-029, CAP-033, CAP-043, CAP-045, RSK-002 | EXISTING REQUIREMENT |
| §10: strategies coordinated under one authority; no unverified strategy activated | The §10 rows: STR-001, STR-016, STR-024, PAP-012, RDY-002, CAP-008; STR-029, FUTURE | EXISTING REQUIREMENT |
| §11: deterministic authority over AI | The §11 row: SR-03, ARCH-019, ARCH-020, EXE-001, AGT-016, COST-001 | EXISTING REQUIREMENT |
| §12, §14: adaptation to the market; no revenge trading; capital protection above every objective; no trade always acceptable | The §12 and §15 rows: RSK-044, RSK-047, SR-18, SR-19, SR-02, PLT-006 | EXISTING REQUIREMENT |
| §13: the measures; days at 1.0% to 1.5%; results kept apart by origin; nothing invented; no promotion on short periods | The §14 rows: DSI-002, OPP-014, PFC-012, PFC-015, PFC-020, PFC-021, PFC-022, PAP-012, STR-016, V-44 | EXISTING REQUIREMENT |
| §16: three gates | DEC-032's three, named and ordered differently, as in the §16 row (DEC-068's reading notes) | EXISTING (builder) |
| The closing directive: its ten principles | The rows above: 1, §2/§6; 2 and 4, §3/§4/§9; 3, §3; 5, §3/§12; 6, §8; 7, §11/§14; 8, §5/§13; 9–10, §15 | EXISTING REQUIREMENT; 9–10, EXISTING (builder) |

## Reconciliation of the last change's temporary backup

The mapping, committed as `2618740`, was backed up on `claude/unverified-backup-owner-decisions-29` in 19 commits, each on the one before and the first on `ad60e54`, committed from 2026-11-11, 05:00 UTC (`213786d`), to 2026-11-16, 18:43 UTC (`5490f7f`). Each commit carries the seven labels, the emergency checkpoint record of §132 with its seven fields, both trailers, and `[skip ci]` (checked by script on 2026-11-16, 18:54 UTC).

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `2618740`'s tree is `5490f7f`'s (`git diff --name-only`: no difference) | PASS |
| 2 | Corrections made during verification are preserved | The same tree: Gate 3 run 1's fixes and the record's account of them | PASS |
| 3 | No required work exists only on the temporary backup | Each of the 25 files the commits change against `ad60e54` is in `2618740`; outside `docs/`, only `CLAUDE.md`. Three commits of 2026-11-16, from 18:31 to 18:33 UTC, also held owner decisions 35, and the last of them a first draft of DEC-069, written for the mapping and moved to this change, which carries them; the message of one later commit, `6e33ea1`, still named that preservation, and the next, `5490f7f`, corrected it | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `2618740`'s parent is `ad60e54`; none of the 19 commits is in its history or in that of `main`, at `7172a5c` (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch from GitHub, at `2618740` (18:54 UTC): the documentation checker and its self-test pass, and `compare_requirements.py ad60e54 --strict` reports 749 requirements before and 757 after, the eight added; the tests ran in the machine checks | PASS |
| 6 | Required documentation and traceability are updated | `2618740` holds the record's final status, PASS for its gates, the checkpoint log's row, and the backup in the project state's "Branches", as active until reconciled | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `2618740` is on the remote branch (`git ls-remote`), pushed at 18:44 UTC, and the machine checks passed on it ([run 43932077424](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/43932077424)) | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `2618740` after the commit and its push | PASS |

**Result: PASS.** The backup's work is VERIFIED AND INCORPORATED in `2618740`. Its last commit, `5490f7f`, is kept under the archive branch `claude/archive/unverified-backup-owner-decisions-29`, pushed at 18:55 UTC after a check that no archive branch for it existed, and checked on GitHub at that commit. Its commit carries the marker, so the push started no run. One deletion of the branch was then attempted (18:55 UTC), with a lease on `5490f7f`, and refused: git reported "the remote end hung up unexpectedly", as for the earlier backups, whose output also showed HTTP 403 (this output kept only its last three lines); the branch stays at `5490f7f`.

**The ten checks before "safe to delete"** ([owner decisions 22](../handoffs/owner-decisions-22-configuration-limit-and-branch-retirement.md)'s first rule set, §5), made on 2026-11-16 for the branch, at `5490f7f`:

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | All valid unique work is preserved elsewhere | Its commits are its archive branch's, and its work is in `2618740` and, for owner decisions 35, in this change | PASS |
| 2 | The canonical archive exists | GitHub's branch list (2026-11-16): `claude/archive/unverified-backup-owner-decisions-29` at `5490f7f` | PASS |
| 3 | Commit and content parity | The branch is at its archive branch's commit (GitHub's branch list and `git ls-remote`) | PASS |
| 4 | No open work depends on it | The project state names it only as reconciled, archived, and retired | PASS, in this change |
| 5 | No active pull request depends on it | GitHub's list of the repository's pull requests, in every state: none | PASS |
| 6 | No required verification evidence exists only on it | A backup is evidence for no gate (DEC-052, decision 3); every record is on the designated branch, and its commits are on its archive branch too | PASS |
| 7 | No unresolved owner decision depends on it | None: a later backup branch whose deletion is refused is retired and kept without a new question to the owner (DEC-067, decision 5) | PASS |
| 8 | No deployment or automation depends on it | The workflow names no single branch: its branch patterns cover every temporary backup and archive branch alike; nothing is deployed; outside `docs/`, the repository does not name the branch (`git grep`) | PASS |
| 9 | Traceability is updated | The project state's "Branches" and this record | PASS, in this change |
| 10 | A canonical rule permits retirement and deletion | DEC-052, decision 3; DEC-054, decision 4; DEC-067, decision 5; owner decisions 10: "RETIRE / DELETE TEMPORARY BACKUP WHEN SAFE" | PASS |

So the branch is RETIRED — DELETION BLOCKED — NON-AUTHORITATIVE — SAFE TO DELETE WHEN PERMITTED (DEC-067, decision 5). No deletion is tried again; it is not protected on GitHub. **The report, A to L** (§14): A, `claude/unverified-backup-owner-decisions-29`; B, `5490f7f`; C, `claude/archive/unverified-backup-owner-decisions-29`, its work in `2618740`; D, parity verified; E, RETIRED — DELETION BLOCKED — NON-AUTHORITATIVE — SAFE TO DELETE WHEN PERMITTED; F, not authoritative; G, nothing depends on it (checks 4 to 8); H, safe to delete when permitted; I, refused by this session's access to GitHub, as before (2026-11-16, 18:55 UTC; the HTTP status not captured); J, no retry: the owner keeps the retired branches until the owner removes them or asks for their deletion from this environment (DEC-064; DEC-067); K, kept, retired, its archive branch kept for audit; L, none now: when the owner deletes it, check that its archive branch is still at `5490f7f` and record it as RETIRED — PHYSICALLY DELETED.

## Gates

**Verification 1 — the change works as intended:** PASS. Checks 1 to 10 pass, run again after this record's last edit before Gate 3's copy was made. The workflow ran on GitHub as intended on a backup branch (check 7); its other two paths follow from the job's condition, the designated branch's on this change's commit.

**Verification 2 — architecture and consistency:** PASS, by the builder's review of the whole diff. The workflow's change is the one DEC-064 (decision 2) set, in the existing workflow, with no new tool, permission, secret, or action; each statement of the machine checks' rule says the same (check 10). The owner's messages are preserved as the earlier ones were, and the directive on efficiency and the trading rules add no rule set, requirement, component, or source of truth: each of their points is mapped to what states it (the owner rule sets reconciliation; the table above), as owner decisions 17's Rule 0 and owner decisions 9's Rules 3, 5, 10, and 16 ask. The backup's reconciliation follows owner decisions 10 and 22, as for the earlier backups.

**Verification 3 — independent end-to-end and failure audit:** PENDING.

## Failures and fixes

None before Gate 3's copy: the change's checks failed only while it was being written, before owner decisions 35 to 37 were linked and listed, and passed once they were.

## Final status and remaining issues

PENDING.

## Environment

System Python 3.11 (`python3`) for the documentation tools and the change's scripts; uv 0.12.23 with the locked tools of `uv.lock` for the developer guide's checks; git; GitHub's branch list, pull requests, and workflow runs, read through the session's GitHub tools.
