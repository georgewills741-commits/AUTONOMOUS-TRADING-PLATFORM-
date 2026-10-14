# Foundation Verification Convergence Audit — 2026-10-13

> **Status:** record of the audit the owner ordered on 2026-10-13 ([owner decisions 13](../handoffs/owner-decisions-13-foundation-verification-convergence-audit.md)), made before any further gate cycle ([DEC-044](../decisions/DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), decision 3). It reconstructs Stage 1's verification from the repository, classifies every blocking finding, and measures convergence. Its process corrections are applied by [DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md); its exit checklist is kept in the [stage record](stage-01-foundation.md). It changes no code, requirement, decision, or approved completion criterion.

## Identity

- **Date:** 2026-10-13
- **Stage:** 1 — FOUNDATION, after checkpoint B and before checkpoint C
- **Starts from:** commit `cb3cca1`, which preserved the owner's directive
- **Authorization:** owner decisions 13 (the audit); [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md) authorizes Stage 1 only, and nothing here goes beyond it (owner decisions 13, §23)
- **Sources inspected (its §0):** the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md); DEC-032, DEC-033, DEC-038, DEC-039, DEC-041 to DEC-044; the builder texts; the [requirements README](../requirements/README.md), the registry and the requirement comparison; the [traceability README](README.md); the verification records of [checkpoint A](stage-01-checkpoint-a-verification.md) and [checkpoint B](stage-01-checkpoint-b-verification.md), the [quality audit](quality-audit-2026-10-06.md), and the [owner decisions 7 verification](owner-decisions-07-verification.md); the [stage record](stage-01-foundation.md); the [project state](../project-state.md) and its checkpoint log; the commits from `69d3b86` to `cb3cca1`, and the eleven commits of checkpoint B's temporary backup, the only commits of checkpoint B's runs; the machine-check runs on GitHub. The briefs the builder gave the Gate 3 reviewers are not in the repository; the builder's copies of those of checkpoint B's runs 4 to 11 were read, and what they say is recorded here.

## 1. The answer in brief

Stage 1 is **in progress, not failing**. Checkpoints A and B passed their three gates and are committed and pushed (`f2e4046`, `4816059`); checkpoints C and D have not started; no blocking finding is open. One step is blocked: the archive tag of checkpoint B's temporary backup ("Blockers" in the project state), which does not block checkpoint C.

Verification **converged** at both code checkpoints. Checkpoint A needed three Gate 3 runs (2, 1, then 0 blocking findings). Checkpoint B needed eleven, over seven days, with 7, 3, 4, 2, 2, 2, 2, 1, 1, 2, and 0 blocking findings: **slowly converging**, with a long tail, and then converged. It was not a non-convergent loop: no blocking finding was invalid or a duplicate, most were genuine defects against the approved baseline, and the exit criteria never moved.

The tail had process causes, which DEC-045 corrects (section 9):

1. The records claimed more than the code enforced and more than the baseline required, and every false claim was rightly blocking.
2. The reviewer briefs made "a rule not enforced as claimed" blocking, so every rule the builder added became new blocking surface. The briefs were not kept in the repository, and the last two named no part of the plan.
3. Optional findings were fixed by adding rules, and those rules produced later blocking findings.
4. Some fixes caused new blocking findings.

## 2. The Foundation baseline (its §2)

The baseline is the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), approved by the owner on 2026-10-05 ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md); [owner decisions 6](../handoffs/owner-decisions-06-stage-1-plan.md)). It has not changed since, apart from one recorded "Later changes" note that moved U6's Hypothesis setting to checkpoint B, where it was delivered. No second Foundation definition exists or is created here.

| Part of the baseline | Canonical source |
|---|---|
| Objective; systems affected | Plan §1 |
| Entry gate | Plan §2; re-checked in the stage record on 2026-10-06 |
| Requirements and their disposition | Plan §3: §3.1 delivered by Stage 1 code; §3.2 started; §3.3 design rules verified in Gate 2; §3.4 later stages; §3.5 not built. The 734 requirements of the [registry](../requirements/registry.md) are unchanged since `69d3b86` (`compare_requirements.py` at each checkpoint: 0 added, removed, or changed) |
| Approved implementation scope | Plan §4: U1 to U8, each with its acceptance criteria; decisions D1 to D11 (plan §10, DEC-038) |
| Non-scope | Plan §5 |
| Outputs and their locations | Plan §6; D2 |
| Testing requirements | Plan §7. It invents no coverage target and adds no coverage tool; it names no mutation testing |
| Gates and independent review | DEC-032, DEC-033 (one three-gate procedure), [DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md) (what each gate covers now that code exists); plan §8, which defines Gate 3 for Stage 1 |
| Documentation, security, and repository requirements | Plan §9 items 4 and 5; U5 (SEC-001, SEC-005); D2 |
| Completion criteria | Plan §9, items 1 to 8; the §152 transition checklist and the §143 certificate of the master execution constitution |
| Decisions in force | DEC-001 to DEC-044; the owner's for Stage 1: owner decisions 6 and 7 (DEC-038, DEC-040), and owner decisions 8 to 13 (DEC-041 to DEC-044) |
| Unresolved owner questions | None ([open-question register](../open-questions/register.md)). TC-09 and TC-10 are decided when their stages are planned |

## 3. Verification history (its §4)

Stage 1 began on 2026-10-06 (`69d3b86`, the plan approved). Each change passed Gate 1 (the builder's checks), Gate 2 (the builder's architecture and consistency review), and Gate 3 (an independent fresh-context reviewer and the builder's own pass).

| Cycle | Dates and commit | Baseline | Gate 3 runs: verdict and blocking findings | Disposition |
|---|---|---|---|---|
| Checkpoint A (U1, U6) | 2026-10-06, `f2e4046` | Plan, U1 and U6 | 3: FAIL (2), FAIL (1, a finding of run 1 only partly fixed), PASS (0) | Committed and pushed; the machine checks passed on GitHub and failed on a deliberate negative test (`74ce426`, reverted by `bc6eca5`), recorded by `5ac6799` |
| Record of the machine-check runs | 2026-10-06, `5ac6799` | The records | 1: PASS (its three wording fixes applied) | Committed |
| Quality audit (DEC-039) | 2026-10-06 to 07, `a6cca83` | The owner's quality directive | 4: 2, 1, 2, and 2 blocking findings, every one in the question to the owner or its registration (run 3 found run 2's rewrite had undone part of run 1's fix); run 4's fixes, phrase-level wording the review specified, were applied without a fifth run. A first launch of run 3 stopped at the usage limit before reporting | Committed |
| OQ-29 applied (DEC-040) | 2026-10-07, `f0de09c` | The owner's answer | 1: PASS | Committed |
| Checkpoint B (U2, U3) | 2026-10-07 to 13, `4816059` | Plan, U2 and U3 | 11: FAIL (7), FAIL (3), FAIL (4), FAIL (2), FAIL (2), FAIL (2), FAIL (2, one borderline), FAIL (1, borderline), FAIL (1), FAIL (2), PASS (0). The first launches of runs 5, 6, 7, 8, 10, and 11 stopped at a usage limit before reporting | Committed and pushed; machine checks passed |
| Reconciliation of checkpoint B's backup | 2026-10-13, `813fa90` | Owner decisions 10's eight checks | 1: PASS (non-blocking and optional findings applied) | Committed |
| Archive-tag blocker; owner decisions 12 and 13 preserved | 2026-10-13, `cb3cca1` | The records; DEC-043 | 2: FAIL (1: the "Blockers" table said "None open"), then PASS on a focused re-review. A first launch stopped at the usage limit before reporting (observed by the builder and recorded here; `cb3cca1`'s message does not mention it) | Committed |

**Evidence incomplete:** the records give each gate's result on the final tree and every failure found on the way ("Failures and fixes"), but not each intermediate Gate 1 and Gate 2 run one by one; checkpoint B's runs 1 to 7 are not dated one by one and have no commit, since the temporary backup started before run 8 (2026-10-12); the stopped first launch of `cb3cca1`'s review is recorded only here; and the Gate 3 briefs are not in the repository. DEC-045 makes each brief's baseline part of the verification record from now on.

## 4. The blocking findings (its §5 to §7, §13, §14)

Every blocking finding of Stage 1's code checkpoints gets a stable identity here: FA- for checkpoint A, FB- for checkpoint B, numbered in order. The finding's own words, its fix, and its tests are in its verification record, under the run named. "Provenance" is the canonical source the finding shows violated (its §7). "Relation" says how it stands to earlier findings (its §5).

| ID | Run | Finding, in short | Class (its §6) | Provenance | Relation |
|---|---|---|---|---|---|
| FA-01 | A, run 1, B1 | The secret scanner missed credential names with a prefix | Blocking defect | U1 and U5 (the repository test for secrets); constitution Rule 110 | New |
| FA-02 | A, run 1, B2 | The records said U6's Hypothesis setting "cannot be met", which was false | Documentation issue (false claim) | Constitution Rules 129, 173 | New |
| FA-03 | A, run 2, F1 | FA-02 only partly fixed | Reopened finding | As FA-02 | Reopens FA-02: the fix corrected one sentence of two |
| FB-01 | B, run 1, 1 | An outcome instance given to a contract skipped validation, so a float reached an amount | Blocking defect | U2 and U3 acceptance (floats refused); ARCH-025; TEC-003 | New; first of the float-into-amount class |
| FB-02 | B, run 1, 2 | An exponent too large escaped as `InvalidOperation` | Blocking defect | U2 (the constructor refuses invalid values); U3 (one refusal type) | New |
| FB-03 | B, run 1, 3 | The immutability check let mutable types through | Blocking defect | U3 acceptance (mutation, including of nested values, refused); D8 | New |
| FB-04 | B, run 1, 4 | `__context__` still held the input after `from None` | Blocking defect (security) | U3 (validation errors never carry input values) | New; first of the input-in-errors class |
| FB-05 | B, run 1, 5 | The numerical policy said rounding is never silent; `round()` and others round | Documentation issue (false claim) | Rule 129; D7 (rounding only on request) | New; first of the silent-rounding class |
| FB-06 | B, run 1, 6 | Check 7 said every rule had a catching test; eleven had none | Documentation issue (false claim) | Rule 129; master execution constitution §148; DEC-032, Verification 3 | New |
| FB-07 | B, run 1, 7 | The next step depended on an owner message not in the repository | Documentation issue (continuity) | Master execution constitution §01, §90 | New |
| FB-08 | B, run 2, 1 | A contract could switch the base's settings off | Blocking defect | D8 (strict, unknown fields refused, immutable) as a guarantee of every contract; U3's purpose | New |
| FB-09 | B, run 2, 2 | `float()`, `math.floor`, and others converted or rounded unscanned; the record said "no float conversion" | Documentation issue (false claim); the fix extended the scanner beyond the plan | Rule 129; TEC-003 | Related to FB-05 |
| FB-10 | B, run 2, 3 | Floats reached amounts through Pydantic models that are not contracts, Pydantic dataclasses, `validate_call`; `Decimal` used in ways the scanner missed | Major defect; part of the fix extended the scanner beyond the plan | U2's purpose (no float reaches an amount); TEC-003 | Related to FB-01 |
| FB-11 | B, run 3, 1 | A float or a JSON number reached an `Amount` field through a default or a validator | Blocking defect | U3 acceptance (float or JSON-number amounts refused); U2 | Related to FB-01: the same class by another path. Its fix replaced lists of what to refuse with lists of what is allowed |
| FB-12 | B, run 3, 2 | A float became an amount through its text; the records said it could not | Documentation issue (false claim); the fix extended the scanner | Rule 129; TEC-003 | Related to FB-09 |
| FB-13 | B, run 3, 3 | `//`, `divmod`, and `%` truncate without a signal; `math` and `statistics` convert to float | Major defect | D7 (rounding only through functions that name the direction) | Related to FB-05 |
| FB-14 | B, run 3, 4 | The Pydantic scanner added for FB-10 missed `pydantic.dataclasses` and `create_model` | Reopened finding | U2's purpose; FB-10 | Reopens FB-10: its fix missed Pydantic dataclasses, a path FB-10 itself named |
| FB-15 | B, run 4, 1 | A constraint written as a field's default (`Field(gt=0)`) was silently dropped; -5 was accepted | Blocking defect (financial correctness) | U3 (contracts validated); ARCH-010 | New |
| FB-16 | B, run 4, 2 | Another exception raised in a validator escaped with the input in its text | Blocking defect (security) | U3 (errors never carry input values) | Related to FB-04 |
| FB-17 | B, run 4's fix, found by run 5 | `ruff check` failed on FB-16's fix, while the records said the checks passed | Regression caused by a fix | Plan §8, Gate 1; Rule 129 | Caused by FB-16's fix; checks run in one command had hidden it |
| FB-18 | B, run 5, 2 | A private module of another package could be imported unscanned | Blocking defect | U3 and plan §7 (the structure test refuses access to the outcome's private members outside `atp.contracts`; the same form reached `atp.contracts._outcome`, and ruff's SLF001 does not check imports); Rule 129 (the records said private modules were refused) | New |
| FB-19 | B, run 6, 1 | `Amount` could be called and subclassed, building a `Decimal` outside `atp.numeric` without the constructor's checks | Blocking defect | U2 (one amount constructor; no `Decimal(...)` outside `atp.numeric`) | New |
| FB-20 | B, run 6, 2 | The import scanner skipped imports from the package root | Blocking defect | Plan §8, Gate 2 (one-way imports, enforced by the structure test) | New |
| FB-21 | B, run 7, 1 | The amount's union rule missed an amount with metadata of its own | Regression caused by a fix | U2 and U3 (floats refused) | The union rule came from run 4's optional finding 7 (`Amount \| float`) and missed a spelling that finding did not name. Related to FB-01 |
| FB-22 | B, run 7, 2 | An enum's own `_missing_` read any JSON value as a member; `IntFlag` kept unknown bits | Major defect (borderline) | D8 (strict) | New |
| FB-23 | B, run 8, 1 | The conventions said a constructor's error text hides input; it shows input three ways | Documentation issue (false claim) | Rule 129; U3 | Related to FB-04 |
| FB-24 | B, run 9, 1 | A validator that converts its value is applied again whenever the contract is validated again | Major defect (data integrity), fixed as a rule caught in review | ARCH-025; U3 | New |
| FB-25 | B, run 10, B1 | A union whose members are written alike read a contract's own JSON back as another member | Blocking defect (data integrity) | U3 (contracts and their written form) | New |
| FB-26 | B, run 10, B2 | The rule written for FB-24 named a normalization that escapes the constraints written before it | Regression caused by a fix | Rule 129; U3 | Caused by FB-24's fix |

**By class:** 13 blocking defects (FA-01, FB-01, FB-02, FB-03, FB-04, FB-08, FB-11, FB-15, FB-16, FB-18, FB-19, FB-20, FB-25); 4 major defects (FB-10, FB-13, FB-22, FB-24); 7 documentation issues (FA-02, FB-05, FB-06, FB-07, FB-09, FB-12, FB-23: six false or overstated claims and one continuity gap, FB-07); 2 reopened findings (FA-03, FB-14); 3 regressions caused by fixes (FB-17, FB-21, FB-26). Every run's table rated all of them blocking; this audit's split between blocking and major defects is its own: a major defect is a genuine one that the reviewer called borderline (FB-22), whose fix went partly beyond the plan's listed checks (FB-10, FB-13), or that was resolved as a rule caught in review rather than in code (FB-24). A finding is reopened when its fix left open a path the finding itself named, and a regression caused by a fix when the fix brought a new defect or a new rule that missed another path. A gap in a test that enforces rules (the secret scanner of U1, the structure test of plan §7) is classed like the others, as a defect of a Stage 1 deliverable; where each finding was is given next. None was invalid, a duplicate, flaky, a test-environment failure, or a new requirement.

**Where each was (its §13):** 14 in the platform's code under `src/` (FB-01, FB-02, FB-03, FB-04, FB-08, FB-11, FB-15, FB-16, FB-17, FB-19, FB-21, FB-22, FB-24, FB-25); 6 in the repository tests that enforce rules on the code, the secret scanner and the structure test (FA-01, FB-10, FB-13, FB-14, FB-18, FB-20), where the code itself did nothing wrong but the test missed a way future code could; and 9 in the records (FA-02, FA-03, FB-05, FB-06, FB-07, FB-09, FB-12, FB-23, FB-26). Test defects of other kinds were found by the builder while fixing ("Failures and fixes"); among the Gate 3 blocking findings, the eleven rules that had no catching test (FB-06) are classed by the record's false claim that each had one.

**Recurring classes (related findings):** a float reaching an amount (FB-01, FB-10, FB-11, FB-21), input in error text (FB-04, FB-16, FB-23), silent rounding or float conversion (FB-05, FB-09, FB-12, FB-13), and validators (FB-24, FB-26). Each design change closed the paths known then: lists of what is allowed after run 3 (FB-11), every refusal raised after its handler after run 4 (FB-16), and "a validator only checks" after run 10 (FB-26). Two classes still recurred after their change, by paths through what the new design allowed: a float through the union rule (FB-21, run 7) and input through a constructor's error text (FB-23, run 8). A design change closes a class only for the paths it covers, which is why DEC-045 asks every fix to cover its class and starts a root-cause review when a fix causes a blocking regression or a run does not lower the blocking count.

**Regressions caused by fixes, and reopened findings (its §14):** 3 regressions caused by fixes (FB-17, FB-21, FB-26) and 1 reopened finding (FB-14) at checkpoint B, and 1 reopened finding at A (FA-03). Two more chains started from optional or non-blocking findings fixed by adding a rule: run 4's optional finding 7 gave the union rule that FB-21 found incomplete; run 10's non-blocking N2 gave a key-default rule, in which run 11's first launch found three defects ("Failures and fixes"). They point to a large, coupled surface (Pydantic's validation features), fixes made for the reported path rather than the class (as checkpoint A's run 3 also noted), and rules added beyond the baseline that each became something to verify.

**Non-blocking and optional findings:** checkpoint A's three runs found 11, 7, and 5. Checkpoint B's found 11, 13, 5, 8, 11, 7, 6, 8, 6, 8, and 5. Their number did not fall from run to run, as expected (its §17, §33): a fresh reviewer can always name improvements. Each is fixed or recorded in its verification record; those left are in the stage record ("Checkpoint B: non-blocking findings", "Carried to checkpoint C"), each with its handling. None is hidden (its §18): the ones carried to checkpoint C are decisions for U4 and U5, inside Stage 1.

## 5. Goalposts (its §8)

- **The exit criteria did not move.** Plan §9 reads as approved; the one "Later changes" note moved a U6 item to checkpoint B, where it was delivered.
- **The requirements did not move.** No requirement was added, removed, or changed at any checkpoint (`compare_requirements.py --strict`, recorded in each record).
- **The reviewers' severity did not move.** The briefs of runs 4 to 11 define BLOCKING in the same words: "wrong behaviour, a rule not enforced as claimed, a false or materially overstated record claim, a security leak, or a continuity gap", on a realistic path a future developer's ordinary code could take. The briefs of runs 4 to 9 also gave the plan's U2, U3, sections 7 and 8, D2, D7, and D8 to read; those of runs 10 and 11, which focused on the previous run's findings, named no part of the plan, so those reviewers had no stated baseline beyond the records.
- **What moved was the verified surface, through the builder's own records.** The kernel and the scanners grew beyond the checks the plan lists: refusals of every float conversion and rounding function the reviewers found, of Pydantic outside `atp.contracts`, of private imports across packages, and the list of what a contract may add (settings, field types, metadata, validators, unions, literals, enums, defaults). Each is recorded in the numerical policy or the contract conventions as the builder's design under D7 and D8. None is an owner-approved criterion or a requirement, and none was presented as one; but each became something "claimed", so each could be blocking. Between run 8 and the final tree alone, `src/atp/contracts/_model.py` grew from 660 to 792 lines and its test module from 1,673 to 2,232 (the backup's commits). This is not an unauthorized change of the exit criteria; it is uncontrolled growth of what Gate 3 verified, which DEC-045 stops (decisions 2 and 4).

## 6. Mutation testing: check 7 (its §12)

- **Canonical source:** no plan or decision requires mutation testing. Check 7 is the builder's method for the evidence that the tests can fail: "each rule tried has a test that catches its removal". That standard is canonical: the master execution constitution asks "What enforcement has no test?" (§148), and asks every approved machine-enforceable rule to name its test (§76); DEC-032's Verification 3 looks for "tests that pass without actually proving the required behavior"; constitution Rule 129 forbids claiming what is not shown; and the plan's U7 and §8 ask Gate 3 to check that each marked test proves its requirement. §76 itself speaks of approved rules, so for the builder's own design rules the anchors are §148, Verification 3, and Rule 129.
- **Covered code:** the rules of `atp.numeric` (34 mutations), `atp.contracts` (190), and the structure test (105). The secret scanner is not in check 7: checkpoint A's check 11 covered it, with twenty mutations, each caught ([checkpoint A verification](stage-01-checkpoint-a-verification.md)), and it has not changed since; checkpoint C, whose U5 extends it, adds mutations for it.
- **Threshold:** none is set by any canonical source, and none is invented here. The standard is per rule: each mutation removes one enforced rule, and it must be caught. A surviving mutation is analysed: a rule without a test gets its test (FB-06 and the "Failures and fixes" rows on check 7), and a mutation without effect is recorded (checkpoint B's run 3, finding 8). This is §148 applied (and §76, for approved rules), not an arbitrary 100% score.
- **Final run, on the tree of `4816059`:** 329 mutations; 329 caught; 0 survived; none timed out (the builder's script gives each mutation 600 seconds and stops at the first that exceeds them; every run completed); 0 invalid (a mutation that does not compile is reported as invalid, never as caught; two such were found and fixed earlier, "Failures and fixes"); no exclusions (the list is the selection). The canonical requirement, one catching test per enforced rule, is met.
- **Repeatability:** the list of mutations and the script that applies them are in the builder's session workspace, not in the repository, so check 7 cannot be repeated from the repository alone (master execution constitution §22). They are committed with checkpoint C's work, where check 7 next runs ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md), decision 6).
- **History:** 47, 79, 107, 179, 198, 225, 260, 284, 293, 294, 323, and 329 mutations (check 7 and "Failures and fixes"), growing with the rules. As the record says, mutation testing shows that the rules tried are tested, not that no untested rule remains; Gate 3 runs found such rules. The full runs after each round were justified where the mutated modules had changed, but heavy (their durations are not recorded). DEC-045 runs the affected mutations during a checkpoint's rounds and the full list once on its final tree.

## 7. Reruns (its §9, §10)

- **Gate 3 runs** each followed a failed run, as DEC-032's gate rule requires: fix, then run the affected verification again. Each was necessary. Checkpoint B's runs 2 to 9 reviewed the whole change set; runs 10 and 11 reviewed the fixes and compared the tree with the previous run's copy. Full reviews of an unchanged area let each fresh reviewer find new paths there; focused re-reviews, as DEC-045 sets them, check the fixes and what they touch.
- **Eight launches stopped at a usage limit** before reporting: seven recorded (the quality audit's run 3; checkpoint B's runs 5, 6, 7, 8, 10, and 11) and one recorded here only (the blocker record's first review). They were run again; the environment, not a finding, caused them.
- **Gate 1** ran again after every fix; it is cheap, and run 5 showed why each check runs as its own command (FB-17).
- **Evidence invalidated** was named each time, in "Failures and fixes": run 5 invalidated check 2's earlier PASS (FB-17); two mutations that never compiled invalidated their earlier "caught"; mutations whose code a fix rewrote were rewritten. The quality audit's run 4 and the final decision checkpoint closed reviewer-specified wording fixes without another independent run, as DEC-045 now states generally.

## 8. Convergence (its §15)

| Checkpoint B run | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Blocking findings | 7 | 3 | 4 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 0 |
| Of which reopened or caused by a fix | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| Non-blocking and optional | 11 | 13 | 5 | 8 | 11 | 7 | 6 | 8 | 6 | 8 | 5 |

FB-17 was found by run 5 in run 4's fix, so it is counted in run 5's column.

- **Checkpoint A:** 2, 1, 0: converging.
- **Checkpoint B:** a fall from 7 to 2 by run 4, then six runs at 1 or 2, then 0: slowly converging, then converged. One finding was reopened (FB-14, at run 3) and none repeated; after run 7, each blocking finding was new, a new path of an earlier class (FB-23), or a regression of a fix.
- **Documentation-only changes:** the quality audit's question oscillated (2, 1, 2, 2) until it was closed with the review's own wording.
- **Stage 1 as a whole: CONVERGING.** No blocking finding is open, and no owner decision blocks the next checkpoint. The long tail at B came from the process causes of section 9, which, left as they were, would recur at C and D.

## 9. Root causes and their corrections (its §16, §32)

| Cause | Evidence | Correction (DEC-045) |
|---|---|---|
| The records claimed more than the code enforced and more than the baseline required | FA-02, FB-05, FB-06, FB-09, FB-12, FB-23, FB-26 | Decision 4: state what the code enforces, list the limits; a false claim is corrected to the truth; enforcement beyond the baseline needs a canonical source |
| "A rule not enforced as claimed" was blocking, so every added rule was new blocking surface; the briefs were not in the repository | Section 5; FB-21; the briefs of runs 10 and 11, which named no part of the plan | Decisions 1 and 2: each brief gives the approved baseline, and its baseline and severity are kept in the record; a blocking finding names the canonical source it violates |
| Optional findings fixed by adding rules | Run 4's optional finding 7 leading to FB-21; run 10's N2 leading to the defects of run 11's first launch | Decision 4: a non-blocking or optional finding whose fix adds a rule is recorded for later, not fixed in the same round |
| Fixes made for the reported path, not the class; checks run together hid a failure | FA-03, FB-14, FB-17, FB-21, FB-26; FB-21 and FB-23 after their classes' design changes; checkpoint A's run 3 | Decisions 4, 5, and 7: a fix is checked against the finding's class; each check runs on its own; a regression caused by a fix triggers a root-cause review |
| Full re-runs | Section 7 | Decisions 5 and 6: impact-based revalidation; the full mutation list once per checkpoint |

**Gaps this audit found, and their handling:** the Gate 3 briefs are not in the repository (DEC-045, decision 1); check 7's list and script are not either (section 6; DEC-045, decision 6); intermediate Gate 1 and Gate 2 runs are not recorded one by one (DEC-045, decision 7 counts each Gate 3 run instead); and the stage record's "Blockers" row said "None" while the project state recorded the blocked tag (corrected in this change).

None of these lowers the standard: the three gates, the independent reviewer, the requirements, the plan's acceptance criteria, check 7's per-rule standard, and the rule that every false claim is fixed all stay.

### Which of the directive's rules the builder texts already state

DEC-044 (decision 4) asks this audit which of owner decisions 13's lasting rules the five builder texts already state. Most do; what is new is what DEC-045 decides.

| Owner decisions 13 | Already stated in | New, applied by DEC-045 |
|---|---|---|
| §0, §1: canonical authority first; reuse, never duplicate governance | Constitution Rules 30, 37, 41 to 44; master execution constitution §25 to §29, §33, §164; quality directive §3, §5 | — |
| §2, §19, §20, §34: a fixed baseline; objective, finite exit criteria | Constitution Rules 137 to 140, 213; master execution constitution §12, §13, §143, §152; the plan's §9 | The exit checklist's fields, kept in the stage record (decision 8); each Gate 3 pass judged against the baseline (decisions 1, 2) |
| §3, §17, §18, §32, §33: no scope creep, no defect blindness, no perfection loop, no hidden debt | Constitution Rules 78, 79, 127, 209, 210; master execution constitution §20, §65 to §68; the quality directive's opening and §16 | A non-blocking finding whose fix adds a rule is recorded for later, not fixed in the round (decision 4) |
| §4, §26: the verification history; evidence for every claim | Constitution Rules 124, 128, 129; master execution constitution §21, §145; quality directive §10 | Per-run counts of blocking, reopened, and fix-caused findings (decision 7) |
| §5: one identity per finding | — | Decision 3 |
| §6, §7, §11, §31: classification; the provenance of a blocker; the reviewer's scope and brief | Constitution Rules 180 to 183, 208; master execution constitution §93, §94; quality directive §4; DEC-033 (an independent reviewer) | Decisions 1 and 2 |
| §8: no moving goalposts | Constitution Rule 56; master execution constitution §64; quality directive §2 | Comparing the criteria across cycles (this audit, section 5) |
| §9, §10: revalidation by impact; invalidated evidence named | Constitution Rule 126; master execution constitution §19; the checkpoint and verification rule ("rerun the complete three-stage gate where appropriate") | Decision 5 |
| §12: mutation testing's purpose | Master execution constitution §76, §148; DEC-032, Verification 3 | Decision 6 |
| §13, §14, §16, §28: test defects; regressions caused by fixes; root causes; correction | Constitution Rules 115, 116, 125, 191 to 193, 208; master execution constitution §19, §162; quality directive §6 | Fixes cover their class (decision 5); a blocking regression caused by a fix, or a run that does not lower the blocking count, starts a root-cause review (decision 7) |
| §15: convergence measured | — | Decision 7 |
| §21, §22, §23: no bypass by renaming; separated authority; no implementation expansion | Constitution Rules 80, 81, 92, 134 to 139; master execution constitution §26, §65, §77; quality directive §4, §12 | — |
| §24, §25, §29, §35, §37: repository integrity; temporary backups; change scope; continuity; the final consistency check | Master execution constitution §02 to §07, §69 to §73, §110, §124 to §128, §132 to §136, §152; quality directive §13, §14. Outside the builder texts: owner decisions 10 (DEC-042 to DEC-044), whose adoption is decided with owner decisions 9's | — |
| §27: the owner decision gate | Quality directive §11; master execution constitution §92, §156 | — |
| §30: three passes | DEC-032, DEC-033, DEC-039 | Each pass against the fixed baseline (decisions 1, 2) |
| §36: the report | Asked once, of this audit (section 12) | — |
| §38: rigor and convergence together | The rows above, which it sums up | — |

Whether the directive's text joins the builder texts that `CLAUDE.md` loads stays with owner decisions 9's adoption (DEC-044, decision 4); until then its new rules apply through DEC-045, which every session reaches from the project state.

## 10. Exit checklist (its §19, §20)

The objective exit checklist is kept where the plan puts the stage's closure, in the [stage record](stage-01-foundation.md), "Transition checklist and completion certificate": the eight completion criteria of plan §9, each with its source, owner, evidence, method, pass condition, status, and dependencies, and the §152 items under the sixth. It restates the approved criteria; it adds none. Foundation exits when they hold (plan §9; owner decisions 13, §20, §34), not when no improvement can be imagined.

## 11. Integrity and consistency checks performed (its §24, §37)

On `cb3cca1` (2026-10-13):

| Check | How | Result |
|---|---|---|
| Duplicate requirements; unauthorized requirements | `build_index.py --check-only` (IDs unique and defined); `compare_requirements.py 69d3b86 --strict` | None: 734 requirements, none added, removed, or changed since Stage 1 began |
| Duplicate files | The sha256 hash of every tracked file | None |
| Duplicate decisions or preserved texts | Decision numbers in `docs/decisions/`; the preserved-text manifest | None: DEC-001 to DEC-044 once each; every preserved text listed once and unchanged |
| Competing sources of truth; duplicate authorities or governance | The [source-of-truth map](../architecture/source-of-truth-map.md) and the system registry against the modules; Gate 2's scans at checkpoint B | One owner per module; no second configuration source, contract base, amount constructor, or gate procedure |
| Unresolved blocking conflicts | The [findings register](../conflicts/register.md) | None open |
| Tests weakened or deleted | Test functions of `f2e4046` and of every backup commit against `4816059` | Every checkpoint A test is still present (6 then, 230 now); the three test functions removed during checkpoint B were replaced by the recorded correction of enum values and flags |
| Untracked blockers; hidden deferrals | The project state's "Blockers"; the stage record's non-blocking and carried items | The archive tag is tracked; every deferral is recorded with its handling |
| Security and financial-safety controls | The secrets test, the structure test, and the machine checks on `4816059`, `813fa90`, and `cb3cca1` (passed); no credential, exchange connection, or trading path exists | None bypassed |
| Unverified work promoted; abandoned valid work | The backup's eleven commits against `4816059` (the reconciliation) | None promoted; none abandoned: the branch is kept until its tag exists |
| Architectural drift | The structure test's import directions; Gate 2 at checkpoint B | None found. The growth of the kernel's rules is recorded in section 5 |
| Scope | Stage 1's commits against plan §5 | No later-stage work: no exchange, market data, storage, trading, AI, or deployment |

## 12. The report the directive asks for (its §36)

| Item | Answer |
|---|---|
| A. Current status | IN PROGRESS: checkpoints A and B complete (three gates passed, committed, pushed); C and D not started; no open blocking finding; the archive tag of checkpoint B's backup blocked |
| B. Baseline sources | Section 2 |
| C. Exit criteria | Plan §9, items 1 to 8, with the §152 checklist; their statuses in the stage record (section 10) |
| D. Gate 1 cycles | One before each Gate 3 run and on each final tree: at least 3 for checkpoint A and 11 for B, and one for each documentation change; intermediate runs are not recorded one by one (evidence incomplete) |
| E. Gate 2 cycles | One per change on its final tree (recorded); intermediate reviews not recorded one by one (evidence incomplete) |
| F. Gate 3 cycles | 23 runs with a verdict since Stage 1 began: 3 for checkpoint A, 11 for B, and 9 for documentation changes (1, 4, 1, 1, and 2); eight more launches stopped at usage limits before reporting (section 7) |
| G. Independent reviews | One per Gate 3 run with a verdict: 23 |
| H. Findings of every Gate 3 cycle | Section 3 and the verification records; the blocking ones in section 4 |
| I. Genuine blockers | All 29 blocking findings were legitimate under the rules in force: 17 defects (13 blocking, 4 major), 7 documentation issues (6 false or overstated claims, 1 continuity gap), 2 reopened findings, and 3 regressions caused by fixes (section 4). 14 were in the platform's code, 6 in the repository tests that enforce rules, and 9 in the records |
| J. Regressions caused by fixes | 3 (FB-17, FB-21, FB-26) |
| K. Reopened findings | 2 (FA-03, FB-14) |
| L. Duplicate findings | None; 4 recurring classes of related findings (section 4) |
| M. Invalid findings | None |
| N. Non-blocking improvements | 23 at checkpoint A and 88 at B (sections 4 and 8); each fixed or recorded |
| O. Future-stage work | None found as a blocker; frame variables in tracebacks are recorded for the observability stage |
| P. New requirements proposed | None in the registry. Kernel design rules were added under D7 and D8 and recorded in the conventions (section 5) |
| Q. A new requirement treated as approved | No |
| R. Scope expansion | No later-stage work. The verified surface grew beyond the plan's listed checks through the builder's design rules (section 5) |
| S. Exit criteria changed | No |
| T. Goalpost movement | Not of the criteria or the reviewers' severity; the verified surface moved with the records' claims (section 5) |
| U. Why gates were re-run | Each Gate 3 re-run followed a failed run (DEC-032); eight more followed launches stopped at usage limits |
| V. Whether each re-run was necessary | Yes in substance, since each failed run had a real blocking finding; full reviews where focused ones would do, and full mutation runs during rounds, were heavier than needed (section 7) |
| W. Mutation testing | Section 6: 329 of 329 caught on the final tree; the canonical requirement is one catching test per enforced rule (§148; §76 for approved rules); no score is canonical |
| X. Remaining genuine blockers | None for checkpoints A and B. The archive tag blocks only the backup's retirement |
| Y. Outstanding owner decisions | None. The owner decides at Stage 1's end whether to proceed (plan §9, item 8) and, if the tag is still missing then, whether its step may be carried past Stage 1 (DEC-044) |
| Z. Convergence | CONVERGING: A converged; B slowly converging, then converged; no open blocker |
| AA. Root cause of the slow tail | Section 9 |
| AB. Next actions to reach the exit | The project state's "Next approved step": the adoption of owner decisions 9, which also decides whether owner decisions 13 joins the builder texts; the audit of owner decisions 8; checkpoint C (U4, U5, with the carried items) and checkpoint D (U7, U8), under DEC-045; then the owner's approval to proceed |
| AC. Remaining engineering work | U4 configuration and U5 security foundation (checkpoint C); U7 verification matrix and U8 closure (checkpoint D); the items carried to C; the stage's own three gates. No completion date is given (its §36) |

## Gates

- **Gate 1:** the documentation checks pass, and no requirement changed (`compare_requirements.py cb3cca1 --strict`); the commands of section 11 as recorded there.
- **Gate 2:** by the builder: no second Foundation definition, checklist, gate, review lifecycle, or issue tracker is created (owner decisions 13, §1): the baseline is the plan, the exit checklist lives in the stage record, the corrections are one decision record applying existing rules, and the finding identities above number the existing findings; no code, requirement, approved criterion, or decision changed.
- **Gate 3:** an independent fresh-context reviewer, briefed with this audit's baseline (owner decisions 13 and the canonical sources above) and a severity rule like DEC-045's, recounted the record's facts against the repository. Run 1: FAIL, six blocking findings (counts and statements it recounted differently, and the missing mapping of the directive's rules to the builder texts), all corrected; its non-blocking findings applied where they made the record more exact. Run 2, focused on the corrections (DEC-045, decision 5), its first launch stopped at a usage limit and resumed: PASS, no blocking finding; its two non-blocking and four optional points, wording and one classification (FB-18, classed like FB-20) that the review specified, applied without a further run.

## Final status

**COMPLETE.** Stage 1 is in progress and converging; no blocking finding is open; the process corrections are in DEC-045, and the exit checklist is in the stage record.
