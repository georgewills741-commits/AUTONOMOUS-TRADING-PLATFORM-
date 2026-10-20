# Foundation convergence audit 2026-10-13 — Gate 3 Reports

> **Status:** REFERENCE (evidence) — the reports of the independent Gate 3 reviews of the change whose record is [Foundation Verification Convergence Audit — 2026-10-13](foundation-convergence-audit-2026-10-13.md), committed so that what the record says of each run can be checked against what the reviewer reported ([DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), decision 5; [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 3). Each is reproduced in a text block exactly as given, except that local paths are shown as placeholders (`<repository>`, `<home>/`). `<home>/` stands for the path of the home directory of the account the reviews ran under, which is replaced wherever it appears, also where a reviewer named it among the paths searched for; each such replacement is counted as a local path replaced. The sha256 of each report is stated as given and, where anything was replaced, as shown; the text it covers is the block's lines joined by line breaks, with a final line break where the entry says the report ends with one. It defines nothing; the record is the account of the reviews. The headings use the record's names for the runs.

## Run 1

- **Reviewer:** a fresh-context subagent, launched 2026-10-13, 18:43 UTC; report given 2026-10-13, 18:59 UTC
- **sha256:** `fc6dd969b87bd98ff16707c5d28f04cb9e3b1c3428fc2ae5503785848ec3c5fa` as given; `995d99f79376908f9e2c901e94ea144cf64e3508cce0d2e3bdee4621e02e603a` as shown, with 1 local path replaced

```text
## Gate 3 review: Foundation convergence audit (record and DEC-045), on cb3cca1 plus the uncommitted change

**Verdict: FAIL.** Six findings are blocking. Five are false statements in the record; one is an analysis DEC-044 assigns to this audit that is missing. All six fix quickly. Most of the record checks out: the per-run counts, the 29 finding identities and their classes, the line counts, the mutation history, the requirement comparison, the test-function check, and the exit checklist's mapping to plan §9.

### Commands and results
- **Tool runs** (system python3 3.11.15, in the review copy):
  - `build_index.py --check-only`: exit 0 (734 requirements, 45 decisions).
  - `selftest.py`: exit 0, PASS.
  - `compare_requirements.py cb3cca1 --strict`: exit 0, with 0 added, removed or changed.
  - `compare_requirements.py 69d3b86 --strict`: exit 0, with 0 added, removed or changed.
- **Duplicate files** (sha256 of every tracked file): none. Decision files: 45, each number once.
- **Test functions:**
  - f2e4046 has 6; 4816059 and cb3cca1 have 230 each; none of A's 6 is missing.
  - Present only in backup commits: three enum/flag tests in `test_model.py`. This matches section 11.
- **Recounted from the records:**
  - Checkpoint A blocking findings: 2, 1, 0.
  - Checkpoint B blocking findings: 7, 3, 4, 2, 2, 2, 2, 1, 1, 2, 0.
  - Checkpoint B non-blocking plus optional: 11, 13, 5, 8, 11, 7, 6, 8, 6, 8, 5, which sums to 88.
  - All 29 FA/FB rows map to their run's table (I checked all of them, including FA-03, FB-17, FB-18, FB-21 and FB-26). Class tallies 12+4+7+1+4+1 = 29.
- **Quality audit:** 2, 1, 2, 2 blocking findings, plus run 3's stopped first attempt. The single PASS runs of 5ac6799, f0de09c and 813fa90, and cb3cca1's FAIL-then-PASS, all match their commit messages.
- **Section 5 line counts:** `_model.py` 660 (ab78d52, 540fe4a, ca43693) to 792 (4816059, ee84f26). `test_model.py` 1,673 to 2,232. The backup has 11 commits, ab78d52 to ee84f26.
- **Plan:** unchanged since 69d3b86 except the one "Later changes" note (in f2e4046), so §9 is unchanged.
- **Mutation testing:**
  - No plan or decision mentions mutation testing.
  - The history 47 … 329 is all in the record.
  - `mutate3.py` holds 329 mutations: 190 in `atp.contracts`, 34 in `atp.numeric`, 105 in `test_structure.py`.
  - Timeout claim true: `timeout=600` sits in a `try/finally` with no `except`, so the first timeout stops the script before its summary.
  - Mutations that do not parse are reported INVALID. Both "Failures and fixes" rows exist (two mutations that never compiled; FB-17's hidden ruff failure).
- **Remote and GitHub:** f2e4046, 4816059, 813fa90 and cb3cca1 are on origin. GitHub GET requests show machine checks succeeded on 4816059 (run 38394631060), 813fa90 (38397859451) and cb3cca1 (38447719517).
- **Hygiene:** the 329 added or new lines contain no `/home/`, `/tmp/`, `<home>/`, model identifiers or secret patterns; `git diff --check` exits 0.
- **Consistency:**
  - Project state: items renumbered 1 to 5 consistently (references at lines 67, 70, 82, 85, 254, 354); the cb3cca1 log row is filled in; DEC-045 is in "Decisions in effect" and in the log.
  - The stage record's "Blockers" row now matches the project state.
  - No active document still says the audit is next.

### Findings
| # | Finding and evidence | Severity | Suggested fix |
|---|---|---|---|
| 1 | **Usage-limit relaunches are miscounted.** The audit names B's runs 8, 10 and 11 (line 55) and gives a total of five (lines 124, 188 item F, 203 item U). The checkpoint B record also has stopped first launches at runs 5, 6 and 7 (lines 190, 212, 230), so B had six and the total is eight. The fifth one the audit lists, the blocker record's first review, is not in the repository: cb3cca1's message records no stopped launch, and `git log --grep='usage limit' 69d3b86..cb3cca1` finds nothing. This is false against owner decisions 13 §4, §15 and §36 U. | BLOCKING | Name runs 5, 6, 7, 8, 10 and 11. Correct the totals (7 recorded, plus the cb3cca1 one marked EVIDENCE INCOMPLETE). |
| 2 | **Not every brief gave the reviewer the plan.** Line 109 says each brief of runs 4 to 11 "also gave the plan's U2, U3, sections 7 and 8, D2, D7, and D8 to read". Briefs 4 to 9 do (e.g. review4-prompt.txt line 13). review10-prompt.txt (23 lines) and review11-prompt.txt (60 lines) never mention the plan, U2, U3, D2, D7, D8 or sections 7 and 8. So the last two briefs gave no baseline, which bears on §31 and DEC-045 decision 1. The severity sentence itself is the same in all eight. | BLOCKING | State that briefs 4 to 9 gave the plan's sections and 10 and 11 did not. Use this as evidence in section 9. |
| 3 | **An analysis DEC-044 assigns to the audit is missing.** DEC-044 decision 4 says "the audit first finds which of [owner decisions 13's] rules the existing builder texts already state". Neither the audit nor DEC-045 does this; grep finds only the sources list (line 11) and the next-step pointers (line 210; DEC-045 decision 9). Yet the record says "COMPLETE" (line 221), and the project state's next step decides whether owner decisions 13 joins the builder texts without this input. | BLOCKING | Add a short mapping: each lasting rule of owner decisions 13, the builder text that already states it, and which ones only DEC-045 states. Or move the task explicitly with a "Later changes" line on DEC-044. |
| 4 | **FB-18's note contradicts DEC-045.** Line 87 says "under DEC-045 such a finding is non-blocking unless the baseline requires the rule". DEC-045 decision 2 (line 15) keeps blocking any finding that "shows a statement in the records that is false or overstated". FB-18 was exactly that: at ab78d52, the records said private modules are refused (checkpoint B record line 24; development guide line 74), and run 5 found `from atp.numeric import _context` unscanned. So FB-18 is the same kind as FB-09, FB-12 and FB-23, which the audit counts as legitimate. That undermines "28 of 29 legitimate" (I) and M. A fresh session would find two opposite rules. | BLOCKING | Class FB-18 as a documentation issue (false claim, Rule 129) and recount I. Or amend DEC-045 to say what the note says. |
| 5 | **Two classes recurred after their design changed.** Line 99 says "Each class came back by another path until its design changed", but the audit's own rows contradict it. The float class recurred at run 7 (FB-21), after run 3's change. The input-in-errors class recurred at run 8 (FB-23), after run 4's change. This overstates the root-cause analysis (§14, §16). | BLOCKING | Say that two of the four classes recurred after their design change, and what that implies. |
| 6 | **Checkpoint A non-blocking count is off by one.** Line 103 gives "Non-blocking and optional … 11, 6, and 5" for A. Run 2 had N1 to N6 plus one Optional row, so 7; run 1's 11 includes its optional N11, and every B count includes optionals. N (line 196) should be 23, not 22. | BLOCKING (minor; mechanical) | Change to 7 and 23. |
| 7 | **§76 is quoted more broadly than it reads.** Section 6 (line 114) and DEC-045 decision 6 and its Alternatives ("§76 requires a test for every enforced rule") cite §76. §76, titled "SYSTEM RULE ENFORCEMENT", says "Approved machine-enforceable rules must identify … TEST". The builder's added rules are not approved (section 5 says so). The per-rule standard is still traceable, through §148 ("What enforcement has no test?"), Rule 129 and DEC-032 Verification 3. Nothing is invented or weakened: no score is set and the standard is unchanged. | NON-BLOCKING | Quote §76 exactly and cite §148 in DEC-045. |
| 8 | **Check 7 does not cover the secret scanner.** "Covered code … and the secret scanner" (line 115) is not true of check 7: none of its 329 mutations touch `test_no_secrets.py`, and check 7 runs without the secrets test. The scanner was mutation-tested by checkpoint A's check 11 (20 of 20) and is unchanged since f2e4046, so that evidence is valid but the attribution is wrong. A's mutation runs are also missing from the history. At checkpoint C, U5 changes the scanner. | NON-BLOCKING | Attribute the scanner to A's check 11, add A's runs to the history, and note that checkpoint C's list needs scanner mutations. |
| 9 | **Reopened vs regression is classed inconsistently.** FA-03 (a fix only partly done) is "Reopened", but FB-14 (FB-10's fix incomplete for a path FB-10 itself named) and FB-21 are "Regression caused by a fix". On FA-03's standard, "No finding was reopened" (line 139) is doubtful. The relation column is open about it, so this is a judgment call. | NON-BLOCKING | Apply one rule to all three, or state the distinction. |
| 10 | **Two distinctions are left unstated.** The split between "Blocking defect" and "Major defect" (12 and 4) is never defined; each run's table had them all as Blocking. Section 6 of owner decisions 13 also asks to separate production defects from test defects; the record does not say that FA-01, FB-14, FB-18, FB-20 and parts of FB-09, FB-10, FB-12 and FB-13 were in the repository tests (scanners), not `src/`. | NON-BLOCKING | Define the split, and give the src/scanner breakdown. |
| 11 | **Two labels are inexact.** Item I calls the 7 documentation issues "7 false or overstated claims", but FB-07 is a continuity gap. The quality-audit row (line 53) says every blocking finding was "in the wording of one question"; R2 was the question's missing registration. | NON-BLOCKING | Adjust the wording. |
| 12 | **Two exit-checklist details.** The checklist restates plan §9's eight criteria and adds none, and all 27 §152 items are covered. Two details: X7's pass condition adds "passing machine checks", which is defensible via U6 and Gate 1 but should be sourced. The "Integration tests: NOT APPLICABLE" reading is weak, since its own evidence says the contract tests and end-to-end commands check how the modules work together (plan §7). The performance, recovery and capability/readiness N/A readings are supported (plan §5; the Readiness System is Stage 4). | NON-BLOCKING | Source X7's condition; map the integration item to that evidence instead of N/A. |
| 13 | **DEC-045's no-re-run exception now reaches code checkpoints.** Decision 5 says a reviewer-specified wording fix needs no further independent run. That extends the precedent of documentation-only records to checkpoints C and D. It is consistent with DEC-032's "where appropriate" and §9, but the record must then report a failed run, not PASS. | NON-BLOCKING | Require the record to state "FAIL on run n; wording applied without a further run". |
| 14 | **Smaller wording points.** The decision-log row, the project state (line 323) and the audit (line 148) say the whole brief "is kept in the record"; DEC-045 decision 1 and the traceability README keep only its baseline and severity. DEC-045 decision 2's "canonical record" is broad enough to readmit the builder's own conventions as provenance. The audit's Gate 3 bullet and "COMPLETE" were written before this review. | OPTIONAL | Align the wording, and revise the status lines after the fixes. |

### Integrity
- The review copy is as found: the `git diff` sha256 begins 8b671a1135f0, the two new files' hashes are unchanged, and no new or ignored files were left.
- My outputs are in `scratchpad/gate3audit13/`. One output file first went to the scratchpad root by mistake and was moved there at once; no existing file was touched.
- No push, tag or branch was created; GitHub was used through three GET requests only; the main repository was not touched.
```

## Run 2

- **Reviewer:** the subagent of run 1, asked by message on 2026-10-13, 19:10 UTC, for a focused re-review of the corrections; it stopped at the session usage limit and was asked to resume on 2026-10-14, 00:18 UTC; report given 2026-10-14, 00:25 UTC
- **sha256:** `44058042e89767470009067428b95a37ab03ac312afd0e3c02b98c50bfa367c9` as given; `3006ec112006c29a4952b398eb1ca8ec6f9a907ec47a7dbbfcc102a0b872b149` as shown, with 2 local paths replaced

```text
## Gate 3, run 2 (focused re-review): Foundation convergence audit corrections

**Verdict: PASS.** All six blocking findings and the eight non-blocking ones from run 1 are corrected and hold up against the repository. No correction introduced a blocking issue. Six minor findings remain (one non-blocking classification point, one non-blocking mapping point, four optional wording points), listed below.

### Commands and results
- **State:** HEAD cb3cca1; push disabled; `git diff` sha256 begins 362fbaa97df7 (the two new files are intent-to-add).
- **What changed since run 1:** I diffed the changed text against my run 1 extract (`gate3audit13/added.txt`). Only four tracked lines changed: the decision-log row, the project state's DEC-045 line, and the stage record's X7 and integration rows. I re-read the audit record (249 lines) and DEC-045 in full.
- **Tool runs (system python3 3.11):**
  - `build_index.py --check-only`: exit 0 (734 requirements, 45 decisions).
  - `selftest.py`: exit 0, PASS.
  - `compare_requirements.py cb3cca1 --strict`: exit 0, with 0 added, removed or changed.
- **The new mapping subsection:** I printed the title of every builder-text rule it cites (38 constitution rules, 45 master execution constitution sections, 11 quality directive sections). Each exists and fits its row. DEC-033 line 30 does name the independent reviewer.
- **Stale counts:** none of "22 at checkpoint A", "five launches", "4 regressions", "4 of 26", "28 of the 29" or "blocking only by a record" remains anywhere in `docs/`.
- **Secret scanner:** `test_no_secrets.py` is unchanged from f2e4046 to cb3cca1.
- **SLF001 probe:** ruff 0.15.8 at `<home>/.local/bin`, on stdin, no cache. It flags none of `from atp.contracts._outcome import _Kind`, `from atp.contracts import _outcome` or `from atp.numeric import _context`. It does flag the attribute access `_outcome._to_envelope`.
- **Hygiene:** the 351 added lines contain no local paths, model identifiers or secret patterns; `git diff --check` exits 0.

### Run 1 findings, each checked
1. **Stopped launches:** line 55 names runs 5, 6, 7, 8, 10 and 11; line 57 marks the cb3cca1 launch "recorded here", and the "Evidence incomplete" paragraph (line 59) lists it. Line 126 and items F and U (lines 216, 231) say eight, of which seven are recorded.
2. **Briefs:** lines 22, 111 and 150 now say runs 10 and 11 named no part of the plan, which matches the brief files.
3. **Mapping:** lines 159–183 now map the directive's rules to the builder texts. The citations check out (see finding 3 below for one gap).
4. **FB-18:** the contradicting note is gone. DEC-045 decision 2 is consistent with the record, and item I reads "all 29". The new provenance is supported by plan §7, U3 and my probe.
5. **Recurrence:** line 101 now says FB-21 and FB-23 recurred after their design changes.
6. **Counts:** checkpoint A's runs read 11, 7, 5, and N reads 23.
7. **§76:** §6 (lines 116, 118), FB-06, item W, and DEC-045 decision 6 and its Alternatives cite §148, with §76 limited to approved rules.
8. **Secret scanner:** credited to checkpoint A's check 11 (twenty mutations, each caught). The 34/190/105 split matches my count.
9. **Reopened vs regression:** FB-14 is reopened, with definitions given; J is 3, K is 2; §8's row is 0,0,1,0,1,0,1,0,0,1,0; line 141 is consistent.
10. **Where each was:** 14 + 6 + 9 = 29, identical to the breakdown I derived myself in run 1.
11. **Item I and the quality-audit row:** both now worded correctly.
12. **Stage record:** X7 is sourced and the integration item now cites its evidence.
13. **DEC-045 decision 5:** now requires the record to state the failed run.
14. **Wording:** the decision log, the project state, line 150 and DEC-045 decision 2's new sentence all agree; the Gate 3 bullet records run 1.

**Counts agree everywhere:** across §1, §3, §4, §7, §8 and §12, the stage record, the project state, and DEC-045 ("26" at B). §3's blocking findings sum to 3 + 26 = 29; "By class" sums to 12+4+1+7+2+3 = 29.

### Findings
| # | Finding and evidence | Severity | Suggested fix |
|---|---|---|---|
| 1 | **FB-18 is classed differently from findings of the same kind.** Line 87 calls it a "Test-infrastructure issue". FA-01 and FB-20 are the same kind (a rule-enforcing test missing a spelling the plan requires it to catch; all three are under "repository tests" at line 99), yet they are "Blocking defect". The counts are unaffected. | NON-BLOCKING | Class FB-18 like FB-20, or class all six repository-test findings the same way. |
| 2 | **FB-18's link to the outcome is left implicit.** The record's example is `atp.numeric._context`. The link holds because the same escaped form, `from atp.<package> import _module`, reaches `atp.contracts._outcome`, and SLF001 cannot catch imports (probe above). | OPTIONAL | Add "the same form reached `atp.contracts._outcome`". |
| 3 | **The §24/§25 mapping row leans on a text that is not a builder text.** It cites owner decisions 10 (DEC-042 to DEC-044), which is not one of the five builder texts; whether it joins one is itself decided with owner decisions 9 (DEC-044 decision 4). The builder texts reach §25 only through master execution constitution §132–§136, which the row does not cite. | NON-BLOCKING | Say so, and cite §132–§136. |
| 4 | **The root-cause trigger is paraphrased too narrowly.** Lines 101 and 174 say a root-cause review starts when a regression "recurs". DEC-045 decision 7 (and the audit's own §9 row) start one at the first blocking regression caused by a fix. | OPTIONAL | Use decision 7's words. |
| 5 | **Two senses of "code" in one cell.** Item I (line 219) gives "16 defects in the code" beside "14 were in the platform's code": four of the 16 were in repository tests. Line 99's "never as Gate 3 blocking findings" also passes over FB-06, whose substance was eleven untested rules. | OPTIONAL | Write "16 defects (12 blocking, 4 major)"; mention FB-06 at line 99. |
| 6 | **Two small wording points.** Run 6's record (line 212) says "the account's usage limit", not "the session's" (line 55). Line 245 says this review used "DEC-045's severity rule"; run 1's brief carried its own, close but not identical. | OPTIONAL | Write "a usage limit"; write "a severity rule like DEC-045's". |

### Integrity
- The review copy is as I found it: HEAD cb3cca1, the same eight status lines, `git diff` sha256 362fbaa97df7bd02, no ignored or new files.
- My files are only in `gate3audit13/`; the ruff probe ran on stdin with no cache and wrote nothing.
- No push, tag or branch; no GitHub requests in this run; nothing touched in `<repository>`.
```

## Launches that stopped before reporting

None.
