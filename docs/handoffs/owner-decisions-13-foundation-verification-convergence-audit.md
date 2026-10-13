# Owner Decisions 13 — Foundation verification convergence audit

> **Status:** HISTORICAL — source input: the owner's message of 2026-10-13, sent during Stage 1 after checkpoint B's commit and the reconciliation of its temporary backup, while the record of the backup's archive-tag blocker was under its third gate. It orders a mandatory audit, before the gate cycle continues, of whether Stage 1 (FOUNDATION) verification converges, and states how that audit and any further remediation are conducted: a fixed baseline, stable finding identities, the provenance of every blocker, impact-based revalidation, and finite exit criteria. It authorizes no bypass of existing rules, no new feature, no scope expansion, and no lowering of quality (its STATUS lines). This is **not** an active source of truth. It is preserved by [DEC-044](../decisions/DEC-044-preserve-archive-tag-answers-and-convergence-audit.md), which records how it is applied.
>
> **Formatting note:** the message is reproduced inside one text block exactly as received, so that its lines, separator lines, lists, and arrows stay as they were sent. Nothing was added, removed, or changed in it. The title and this banner are the builder's.

```text
======================================================================
SERIOUS MODE — FOUNDATION VERIFICATION CONVERGENCE,
ANTI-LOOP, ANTI-DRIFT & GOVERNANCE INTEGRITY AUDIT
======================================================================

STATUS:
MANDATORY AUDIT
FOUNDATION-STAGE CONTROL
DOES NOT AUTHORIZE BYPASSING EXISTING RULES
DOES NOT AUTHORIZE NEW FEATURES
DOES NOT AUTHORIZE SCOPE EXPANSION
DOES NOT AUTHORIZE LOWERING QUALITY

PURPOSE:

Before continuing the current:

GATE 1
→ GATE 2
→ GATE 3
→ FINDING
→ FIX
→ REPEAT

cycle, determine from repository evidence whether Foundation is:

1. legitimately still failing;
2. converging normally;
3. repeatedly discovering regressions;
4. suffering verification-process problems;
5. suffering scope creep;
6. suffering moving completion criteria;
7. rerunning verification unnecessarily;
8. introducing new requirements during review;
9. reopening already resolved findings;
10. trapped in a non-convergent remediation loop.

DO NOT make Foundation pass artificially.

DO NOT weaken verification.

DO NOT bypass a legitimate blocker.

DO NOT remove existing quality controls.

DO NOT use this audit as permission to ignore defects.

The objective is:

HIGH QUALITY
+
FINITE EXIT CONDITIONS
+
FIXED AUTHORITY
+
TRACEABILITY
+
NO DUPLICATION
+
NO CONFLICT
+
NO SILENT DRIFT
+
NO UNBOUNDED PERFECTION LOOP.

======================================================================
0 — CANONICAL PROJECT AUTHORITY COMES FIRST
======================================================================

Before applying ANY instruction in this document, inspect the existing
canonical project governance.

Search all relevant authoritative sources, including where applicable:

- Global Trading Constitution;
- Requirements Registry;
- System Rules Register;
- Architecture;
- ADRs / Decision Records;
- Foundation specification;
- Foundation completion criteria;
- roadmap;
- stage plans;
- governance specifications;
- verification specifications;
- testing policies;
- mutation-testing policies;
- review procedures;
- security rules;
- risk rules;
- capital rules;
- execution rules;
- AI authority rules;
- repository rules;
- branch / checkpoint rules;
- traceability;
- issue registers;
- technical debt;
- audit reports;
- previous Gate reports;
- independent reviews;
- commits;
- test reports;
- CI evidence;
- session/checkpoint records.

DO NOT rely on conversation memory when repository evidence exists.

DO NOT assume this instruction overrides canonical project authority.

If an existing canonical mechanism already handles something described
here:

REUSE IT.
REINFORCE IT.
REFERENCE IT.
DO NOT DUPLICATE IT.

If this instruction conflicts with an approved canonical rule:

1. identify the conflict;
2. cite both sources internally in the project report;
3. determine whether existing governance establishes precedence;
4. follow established authority if the answer is unambiguous;
5. if an owner-level decision is required, STOP and ask the owner.

DO NOT silently override canonical rules.

======================================================================
1 — NO NEW GOVERNANCE SYSTEM FROM THIS AUDIT
======================================================================

This audit must NOT create an unnecessary:

- fourth verification gate;
- second review lifecycle;
- second requirements registry;
- second Foundation definition;
- duplicate governance process;
- duplicate test policy;
- duplicate issue tracker;
- duplicate completion checklist;
- duplicate source of truth;
- competing review authority;
- parallel architecture.

Before creating ANY new artifact, search the repository.

If an appropriate canonical artifact exists:

UPDATE OR REFERENCE THE EXISTING ONE.

Only create something new if:

- no suitable canonical home exists;
- creating it does not duplicate another authority;
- its ownership is clear;
- its purpose is justified;
- it is consistent with repository organization.

======================================================================
2 — FREEZE THE AUTHORITATIVE FOUNDATION BASELINE
======================================================================

Identify the exact approved Foundation baseline.

Do not invent it.

Create or identify a traceable baseline manifest showing:

- authoritative Foundation requirements;
- approved decisions;
- architecture relevant to Foundation;
- approved implementation scope;
- explicit non-scope;
- completion criteria;
- Gate requirements;
- testing requirements;
- independent-review requirements;
- documentation requirements;
- security requirements;
- repository requirements;
- known owner decisions;
- unresolved owner questions.

Where possible, associate the baseline with repository evidence such as:

- requirement IDs;
- ADR IDs;
- rule IDs;
- commit IDs;
- document paths;
- approved review records.

This baseline becomes the target against which Foundation is verified.

Gate 3 must NOT silently redefine Foundation during each review.

======================================================================
3 — SCOPE FREEZE DOES NOT MEAN DEFECT BLINDNESS
======================================================================

Foundation scope is frozen against uncontrolled expansion.

However, scope freeze MUST NOT be used to ignore a genuine defect.

A newly discovered issue may still block Foundation when it demonstrates:

- violation of an already approved requirement;
- architectural inconsistency;
- security weakness;
- integrity failure;
- data corruption risk;
- incorrect system behavior;
- broken test infrastructure;
- incorrect dependency behavior;
- repository inconsistency;
- financial correctness risk;
- violation of a non-bypassable system rule;
- missing evidence required by approved exit criteria.

But:

NEW FEATURE IDEAS,
OPTIONAL HARDENING,
FUTURE CAPABILITIES,
STYLE IMPROVEMENTS,
LATER-STAGE FUNCTIONALITY,
UNAPPROVED OPTIMIZATIONS

must NOT silently become Foundation blockers.

Classify them correctly and place them in their canonical future location.

======================================================================
4 — RECONSTRUCT THE COMPLETE VERIFICATION HISTORY
======================================================================

Inspect repository evidence and reconstruct the actual history of
Foundation verification.

Determine:

- when Foundation began;
- implementation milestones;
- every Gate 1 run;
- every Gate 2 run;
- every Gate 3 run;
- every independent review;
- mutation-test runs;
- failed checks;
- blocking findings;
- non-blocking findings;
- remediation changes;
- commits/checkpoints;
- reruns;
- regressions;
- scope changes;
- requirement changes;
- exit-criteria changes.

For each verification cycle record:

CYCLE ID
DATE / REPOSITORY STATE
BASELINE USED
GATE RESULT
FINDING IDs
SEVERITY
ROOT CAUSE
CHANGE MADE
AFFECTED FILES / SYSTEMS
AFFECTED REQUIREMENTS
REVALIDATION PERFORMED
FINAL DISPOSITION

Do not guess missing historical information.

If evidence is incomplete, mark it:

EVIDENCE INCOMPLETE.

======================================================================
5 — EVERY FINDING MUST HAVE A STABLE IDENTITY
======================================================================

Prevent the same problem from repeatedly reappearing under different wording.

Every material Gate finding must have a stable finding identifier or map
to an existing tracked finding.

Before recording a new finding:

SEARCH FOR AN EXISTING EQUIVALENT FINDING.

Possible classifications:

NEW FINDING
DUPLICATE FINDING
REOPENED FINDING
REGRESSION
RELATED FINDING
SUPERSEDED FINDING
INVALID FINDING
ALREADY RESOLVED

Different wording does NOT automatically make something a new issue.

If a previously resolved finding is reopened:

state WHY.

Do not repeatedly count the same defect as a new blocker.

======================================================================
6 — CLASSIFY EVERY FINDING CORRECTLY
======================================================================

Every finding must be classified as one of:

CRITICAL BLOCKER
BLOCKING DEFECT
MAJOR DEFECT
MINOR DEFECT
NON-BLOCKING IMPROVEMENT
FUTURE-STAGE WORK
TECHNICAL DEBT
DOCUMENTATION ISSUE
TEST-INFRASTRUCTURE ISSUE
FLAKY-TEST ISSUE
MUTATION-CONFIGURATION ISSUE
DUPLICATE FINDING
REGRESSION CAUSED BY A FIX
PRE-EXISTING UNRESOLVED FINDING
NEW REQUIREMENT
ARCHITECTURAL CONFLICT
GOVERNANCE CONFLICT
REQUIRES OWNER DECISION
INVALID / NOT APPLICABLE

Classification must be based on canonical project rules.

Do NOT upgrade severity merely because an improvement is desirable.

Do NOT downgrade severity merely because fixing the problem is inconvenient.

======================================================================
7 — REQUIREMENT PROVENANCE CHECK
======================================================================

When a reviewer says something "must" be changed, determine why.

Every blocking requirement must trace to:

- approved requirement;
- approved ADR;
- Constitution rule;
- System Rule;
- approved Foundation criterion;
- approved security requirement;
- approved testing requirement;
- approved architecture;
- another legitimate canonical authority.

If there is no authoritative basis:

DO NOT silently turn the reviewer's preference into a new requirement.

Instead classify it appropriately as:

PROPOSAL
RECOMMENDATION
FUTURE CAPABILITY
OPEN QUESTION
or
REQUIRES OWNER DECISION.

No reviewer, agent, test tool, or implementation process may silently
create owner-approved requirements.

======================================================================
8 — NO MOVING GOALPOSTS
======================================================================

Compare the exit criteria used by every Foundation verification cycle.

Determine whether:

- criteria were added;
- thresholds changed;
- new tests became mandatory;
- new architecture requirements appeared;
- new documentation requirements appeared;
- new security requirements appeared;
- scope expanded;
- review expectations changed.

For every change determine:

AUTHORIZED CHANGE
or
UNAUTHORIZED GOALPOST CHANGE.

If authorized:

record the provenance.

If unauthorized:

do not silently enforce it as a Foundation completion condition.

======================================================================
9 — IMPACT-BASED REVALIDATION
======================================================================

Do NOT automatically restart every expensive verification process after
every correction.

After every change perform:

CHANGE
→ IMPACT ANALYSIS
→ AFFECTED REQUIREMENTS
→ AFFECTED COMPONENTS
→ AFFECTED INTERFACES
→ AFFECTED DEPENDENCIES
→ AFFECTED SECURITY BOUNDARIES
→ AFFECTED TESTS
→ AFFECTED GATES
→ REQUIRED REVALIDATION.

Preserve valid previous evidence when technically justified.

Examples:

Documentation-only correction:

should not automatically invalidate unrelated mutation-testing evidence.

Localized implementation change:

rerun affected unit/integration/regression verification.

Shared-interface change:

may require broader integration and architectural verification.

Test-infrastructure change:

may invalidate previous test evidence.

Security-boundary change:

requires appropriate security revalidation.

Core financial/risk/capital/execution change:

requires appropriately broad verification.

The rule is:

REVALIDATE EVERYTHING THAT MAY HAVE BEEN MATERIALLY AFFECTED.

NOT:

RERUN EVERYTHING AUTOMATICALLY.

AND NOT:

RERUN TOO LITTLE TO SAVE TIME.

======================================================================
10 — VERIFICATION INVALIDATION MUST BE EXPLICIT
======================================================================

When previously passed evidence must be discarded, state exactly why.

For every invalidated verification result record:

- previous evidence;
- change that invalidated it;
- causal relationship;
- required replacement verification.

Do not discard valid evidence without reason.

Do not preserve invalid evidence merely because rerunning it is expensive.

======================================================================
11 — REVIEWERS MUST REVIEW, NOT REDESIGN FOUNDATION
======================================================================

Independent review must remain genuinely independent.

However, independent review is not permission to redesign the project.

Reviewer responsibilities:

- verify the approved baseline;
- identify genuine defects;
- identify inconsistencies;
- identify risks;
- identify missing required evidence;
- challenge unsupported claims.

Reviewer responsibilities do NOT automatically include:

- expanding Foundation;
- inventing features;
- rewriting owner decisions;
- changing authority;
- changing architecture without governance;
- adding arbitrary thresholds;
- converting preferences into blockers.

If a reviewer discovers a valuable future improvement:

TRACK IT.

Do not automatically block Foundation with it.

======================================================================
12 — MUTATION TESTING MUST HAVE CANONICAL PURPOSE
======================================================================

Inspect why mutation testing is required.

Determine:

- canonical source;
- covered code;
- intended confidence objective;
- approved threshold;
- exclusions;
- timeout policy;
- survivor handling;
- failure handling;
- relation to Foundation exit criteria.

Report:

TOTAL MUTATIONS
KILLED
SURVIVED
TIMED OUT
ERRORS
EXCLUDED
MUTATION SCORE
CANONICAL REQUIRED SCORE
RESULT

Do NOT invent:

- 100% requirements;
- arbitrary score requirements;
- arbitrary zero-survivor requirements;
- undocumented exclusions.

Do NOT weaken an existing approved threshold either.

Mutation testing should target code where mutation evidence provides
meaningful engineering value.

======================================================================
13 — DISTINGUISH DEFECTS FROM TEST DEFECTS
======================================================================

A failing test does not automatically prove production code is wrong.

Determine whether the root cause is:

PRODUCTION DEFECT
TEST DEFECT
OUTDATED TEST
FLAKY TEST
TEST ENVIRONMENT FAILURE
INCORRECT FIXTURE
MUTATION TOOL ISSUE
CONFIGURATION ISSUE
NONDETERMINISTIC BEHAVIOR
GENUINE REQUIREMENT VIOLATION.

Never modify correct production behavior merely to satisfy an incorrect test.

Never weaken a correct test merely to make production code pass.

Resolve the actual root cause.

======================================================================
14 — REGRESSION-CAUSED-BY-FIX ANALYSIS
======================================================================

If fixing Finding A creates Finding B:

record the relationship.

Do not treat B as unrelated noise.

Determine whether repeated remediation indicates:

- excessive coupling;
- poor abstraction;
- unstable interfaces;
- incomplete design;
- missing invariants;
- weak contracts;
- inadequate tests;
- architecture flaw.

Repeated fix-caused regressions require root-cause remediation.

Do not continue patching symptoms forever.

======================================================================
15 — CONVERGENCE METRICS
======================================================================

Measure whether Foundation is converging.

Track at minimum:

- remaining critical blockers;
- remaining blocking defects;
- reopened findings;
- duplicate findings;
- regressions introduced by fixes;
- newly discovered legitimate blockers;
- non-blocking findings;
- future-stage findings;
- verification reruns;
- unnecessary reruns if any;
- mutation survivors if relevant;
- unresolved owner decisions.

Compare cycles.

Determine whether the trend is:

STRONGLY CONVERGING
CONVERGING
SLOWLY CONVERGING
STALLED
REGRESSING
NON-CONVERGENT
INSUFFICIENT EVIDENCE.

Do not call something "converging" without evidence.

======================================================================
16 — REPEATED GATE-3 FAILURE ESCALATION
======================================================================

If Gate 3 repeatedly blocks Foundation without measurable convergence,
do NOT bypass Gate 3.

Perform a ROOT-CAUSE / VERIFICATION-CONVERGENCE REVIEW.

Investigate:

- genuine architecture problems;
- incomplete Foundation implementation;
- hidden dependency defects;
- test instability;
- incorrect tests;
- mutation configuration;
- reviewer inconsistency;
- requirement ambiguity;
- poor traceability;
- scope creep;
- changing exit criteria;
- newly introduced requirements;
- fix-induced regressions;
- repeated reopening;
- excessive coupling;
- unnecessary full-suite reruns;
- environmental instability;
- tooling failures;
- missing ownership;
- duplicated governance;
- contradictory canonical sources.

Fix the underlying cause.

Do not merely execute another identical cycle.

======================================================================
17 — NO PERFECTION LOOP
======================================================================

Foundation must satisfy approved completion criteria.

Foundation does NOT need to implement every theoretically desirable
improvement before progressing.

Distinguish:

CORRECTNESS
FROM
PERFECTION.

DISTINGUISH:

REQUIRED HARDENING
FROM
FUTURE HARDENING.

DISTINGUISH:

FOUNDATION DEFECT
FROM
FUTURE FEATURE.

DISTINGUISH:

BLOCKER
FROM
RECOMMENDATION.

A long-lived company-grade system will always have future improvement work.

The existence of future improvement does not automatically mean the
current stage is incomplete.

======================================================================
18 — NO TECHNICAL-DEBT HIDING
======================================================================

Do not misuse "future work" to hide legitimate Foundation defects.

If something is required for Foundation correctness:

FIX IT NOW.

If something is legitimately non-blocking:

classify it;
trace it;
assign it to the appropriate roadmap / debt register / future stage.

No silent deferral.

No silent deletion.

======================================================================
19 — FOUNDATION EXIT CHECKLIST MUST BE OBJECTIVE
======================================================================

Produce the authoritative Foundation exit checklist.

Every criterion must contain:

ID
DESCRIPTION
CANONICAL SOURCE
OWNER
REQUIRED EVIDENCE
VERIFICATION METHOD
PASS CONDITION
CURRENT STATUS
BLOCKING / NON-BLOCKING
DEPENDENCIES

Possible statuses:

NOT STARTED
IN PROGRESS
PASS
FAIL
BLOCKED
REQUIRES OWNER DECISION
NOT APPLICABLE

Do not use vague criteria such as:

"looks good"
"high quality"
"everything complete"
"professional enough."

Exit criteria must be objectively testable where practical.

======================================================================
20 — COMPLETION MUST HAVE A FINITE DEFINITION
======================================================================

Foundation exits when:

- all approved blocking requirements are satisfied;
- all required gates pass;
- required independent review passes;
- required tests pass;
- required mutation criteria pass if applicable;
- blocking security findings are resolved;
- blocking architecture findings are resolved;
- repository integrity requirements pass;
- traceability requirements pass;
- required documentation is current;
- no unresolved owner decision blocks exit;
- required evidence exists.

Foundation does NOT remain open solely because further improvements are
possible.

======================================================================
21 — NO BYPASS THROUGH RENAMING
======================================================================

Do not evade these controls by changing terminology.

Examples:

BLOCKER → "NOTE"
must not hide a blocker.

NEW REQUIREMENT → "REVIEW FINDING"
must not bypass approval.

FUTURE FEATURE → "FOUNDATION HARDENING"
must not silently expand scope.

UNVERIFIED → "CHECKPOINT"
must not imply verification.

RECOMMENDATION → "REQUIRED"
must not imply authority.

The substance determines classification, not the label.

======================================================================
22 — AUTHORITY MUST REMAIN SEPARATED
======================================================================

Do not allow verification work to create competing authorities.

Preserve existing responsibility boundaries.

Reviewers identify and validate.

Requirements define approved behavior.

Architecture defines system structure.

Security owns security controls where established.

Risk owns risk authority where established.

Capital Authority owns capital decisions where established.

Execution owns execution behavior where established.

AI remains within its authorized boundaries.

Verification does not become a new runtime authority.

Testing does not become a requirements authority.

Review tools do not become architecture owners.

======================================================================
23 — NO FOUNDATION IMPLEMENTATION EXPANSION
======================================================================

This audit does NOT authorize later roadmap implementation.

Do not begin:

- directional trading;
- arbitrage execution;
- exchange production integration;
- live capital deployment;
- autonomous production trading;
- future AI agents;
- later-stage infrastructure;

merely because Foundation code touches their interfaces or abstractions.

Respect roadmap stage boundaries.

Architecture may prepare for future stages without implementing them
prematurely.

======================================================================
24 — REPOSITORY INTEGRITY CHECK
======================================================================

During the audit inspect for:

- duplicate files;
- duplicate requirements;
- duplicate configuration;
- duplicate services;
- duplicate authorities;
- conflicting documentation;
- stale documents;
- broken references;
- abandoned temporary implementations;
- untracked generated files;
- unexpected binaries;
- accidental secrets;
- hidden configuration;
- dead code created during remediation;
- abandoned branches/checkpoints where relevant;
- inconsistent tests;
- unresolved merge artifacts;
- architectural drift.

Do not create new problems while fixing verification problems.

======================================================================
25 — TEMPORARY BACKUP / CHECKPOINT INTEGRITY
======================================================================

If unverified work has been preserved in a temporary backup/checkpoint,
do not forget it.

Its lifecycle must remain explicit:

UNVERIFIED WORK
→ TEMPORARY SAFE PRESERVATION
→ VERIFICATION
→ CORRECTIONS
→ VERIFIED AUTHORITATIVE CHECKPOINT
→ RECONCILIATION
→ RETIRE OR RETAIN ACCORDING TO CANONICAL POLICY.

Never:

- promote unverified backup as verified;
- abandon it indefinitely;
- delete it before confirming valid work is preserved;
- create parallel competing implementation history.

Follow existing repository policy.

Do not invent a second backup policy.

======================================================================
26 — EVIDENCE LEDGER
======================================================================

Maintain traceable evidence for significant verification claims.

Examples:

REQUIREMENT
→ IMPLEMENTATION
→ TEST
→ GATE RESULT
→ REVIEW RESULT
→ FINAL STATUS.

Claims such as:

PASS
VERIFIED
NO CONFLICTS
NO DUPLICATES
COMPLETE

must be supported by evidence.

Absence of detected evidence is NOT proof of absence unless the relevant
search/review was actually performed.

======================================================================
27 — OWNER DECISION GATE
======================================================================

Do not interrupt the owner for matters already resolved by canonical
project authority.

Reconcile those automatically.

STOP and ask the owner only when a genuine owner-level decision remains,
such as:

- conflicting authoritative requirements with no precedence;
- material scope change;
- material architecture change;
- authority reassignment;
- risk-policy change;
- security-policy change;
- Foundation exit-criteria change;
- unresolved product decision;
- approval of genuinely new requirement where approval is required.

When asking, provide:

ISSUE
EVIDENCE
CURRENT CANONICAL SOURCES
CONFLICT
OPTIONS
IMPACT OF EACH OPTION
RECOMMENDATION
EXACT DECISION REQUIRED.

Do not ask vague questions.

======================================================================
28 — CORRECTION PROTOCOL
======================================================================

When a legitimate blocker is discovered:

IDENTIFY
→ CLASSIFY
→ TRACE TO CANONICAL REQUIREMENT
→ IDENTIFY ROOT CAUSE
→ ANALYZE IMPACT
→ CHECK DEPENDENCIES
→ DESIGN MINIMAL CORRECT FIX
→ IMPLEMENT
→ RUN TARGETED TESTS
→ RUN REQUIRED BROADER REGRESSION
→ UPDATE DOCUMENTATION IF NECESSARY
→ UPDATE TRACEABILITY
→ REVERIFY
→ CLOSE FINDING WITH EVIDENCE.

Do not patch symptoms if root cause is understood and materially broader.

Do not perform unrelated refactoring during blocker remediation unless
required for correctness.

======================================================================
29 — CHANGE-SCOPE CONTROL
======================================================================

Every remediation change must be checked for:

INTENDED CHANGE
UNINTENDED CHANGE
OUT-OF-SCOPE CHANGE.

If unrelated changes appear in the diff:

investigate them before verification continues.

Avoid "while I am here" expansion.

Foundation remediation should be focused.

======================================================================
30 — THREE-PASS VERIFICATION REMAINS MANDATORY
======================================================================

Do NOT remove the established three-pass verification model.

PASS 1:
CONTENT / CODE / LOCAL CORRECTNESS

PASS 2:
REPOSITORY / ARCHITECTURE / INTEGRATION

PASS 3:
INDEPENDENT / SYSTEM / GOVERNANCE VERIFICATION

However:

each pass must evaluate against the fixed canonical baseline.

A pass must not silently enlarge that baseline.

======================================================================
31 — INDEPENDENT REVIEW MUST REMAIN INDEPENDENT
======================================================================

Do not weaken independent review by feeding it a desired conclusion.

Do not instruct it to "find nothing blocking."

Its objective is to evaluate evidence objectively.

However, ensure the reviewer receives:

- authoritative Foundation scope;
- completion criteria;
- non-scope;
- current repository state;
- applicable canonical rules.

This prevents a reviewer from evaluating against an invented or
unbounded target.

======================================================================
32 — NO AUTOMATIC PASS AFTER REPEATED FAILURE
======================================================================

Repeated failures do NOT earn an automatic pass.

Time spent does NOT earn an automatic pass.

One week spent in Foundation does NOT prove Foundation is ready.

Many passing tests do NOT cancel one legitimate blocker.

The solution to a genuine blocker is:

FIX IT.

The solution to a broken verification process is:

FIX THE PROCESS.

Do not confuse the two.

======================================================================
33 — NO AUTOMATIC FAILURE BECAUSE IMPROVEMENTS EXIST
======================================================================

Similarly:

Foundation does not automatically fail because reviewers can still think
of additional improvements.

The question is:

DOES THE APPROVED FOUNDATION BASELINE PASS?

Not:

CAN ANY POSSIBLE IMPROVEMENT STILL BE IMAGINED?

======================================================================
34 — CONVERGENCE STOP CONDITION
======================================================================

The remediation cycle terminates when:

- all canonical Foundation blockers are resolved;
- required verification evidence is current;
- all mandatory gates pass;
- independent review has no unresolved blocking finding;
- no owner-level decision remains that blocks completion;
- completion criteria are objectively satisfied.

At that point:

STOP REOPENING FOUNDATION FOR NON-BLOCKING IMPROVEMENTS.

Record later improvements in their proper lifecycle.

Create the verified Foundation checkpoint according to canonical rules.

Proceed to the next authorized roadmap stage.

======================================================================
35 — SESSION CONTINUITY
======================================================================

Before a substantial session ends or environment is at risk of loss,
preserve the current state according to repository policy.

Record:

- current Foundation status;
- active findings;
- resolved findings;
- remaining blockers;
- current verification evidence;
- current mutation-test state;
- current review state;
- unverified work state;
- checkpoint state;
- next safe action.

A future session must inspect repository state before repeating work.

Never blindly restart implementation.

======================================================================
36 — FINAL CONVERGENCE REPORT
======================================================================

Before continuing blindly, provide an evidence-based report containing:

A. Exact current Foundation status.

B. Authoritative Foundation baseline sources.

C. Exact Foundation exit criteria.

D. Number of Gate 1 cycles.

E. Number of Gate 2 cycles.

F. Number of Gate 3 cycles.

G. Number of independent reviews.

H. Findings from every Gate 3 cycle.

I. Genuine blockers found.

J. Regressions caused by fixes.

K. Reopened findings.

L. Duplicate findings.

M. Invalid / non-applicable findings.

N. Non-blocking improvements.

O. Future-stage work discovered.

P. New requirements proposed during verification.

Q. Whether any new requirement was improperly treated as approved.

R. Whether Foundation scope expanded.

S. Whether exit criteria changed.

T. Whether any goalpost movement occurred.

U. Why previous gates were rerun.

V. Whether each rerun was technically necessary.

W. Mutation-testing status and authoritative requirement.

X. Remaining genuine blockers.

Y. Outstanding owner decisions.

Z. Whether verification is:

   STRONGLY CONVERGING
   CONVERGING
   SLOWLY CONVERGING
   STALLED
   REGRESSING
   NON-CONVERGENT
   or
   INSUFFICIENT EVIDENCE.

AA. Root cause of any non-convergence.

AB. Exact next actions necessary to reach Foundation exit.

AC. Remaining engineering work based on evidence.

Do NOT invent a completion date.

======================================================================
37 — FINAL REPOSITORY CONSISTENCY CHECK
======================================================================

Before declaring Foundation verified, explicitly check:

NO DUPLICATE REQUIREMENTS.
NO DUPLICATE AUTHORITIES.
NO DUPLICATE GOVERNANCE.
NO COMPETING SOURCES OF TRUTH.
NO UNRESOLVED BLOCKING CONFLICTS.
NO SILENT SCOPE EXPANSION.
NO SILENT ARCHITECTURAL DRIFT.
NO UNAUTHORIZED REQUIREMENTS.
NO UNTRACKED BLOCKERS.
NO HIDDEN DEFERRALS.
NO TESTS SILENTLY WEAKENED TO FORCE PASSING.
NO SECURITY CONTROL BYPASSED.
NO FINANCIAL-SAFETY CONTROL BYPASSED.
NO REQUIRED EVIDENCE MISSING.
NO ABANDONED VALID WORK.
NO UNVERIFIED WORK PROMOTED AS VERIFIED.

Only state these as satisfied after actually performing the checks.

======================================================================
38 — FINAL OPERATING PRINCIPLE
======================================================================

DO NOT LOWER THE STANDARD TO ESCAPE FOUNDATION.

DO NOT KEEP FOUNDATION OPEN FOREVER TO PURSUE UNBOUNDED PERFECTION.

DO NOT FIX THE PROCESS BY REMOVING SAFETY.

DO NOT FIX SAFETY BY CREATING AN INFINITE PROCESS.

The system requires BOTH:

RIGOR
AND
CONVERGENCE.

PRESERVE:

- canonical requirements;
- Constitution;
- System Rules;
- ADRs;
- three-pass verification;
- independent review;
- architecture;
- security;
- financial correctness;
- testing;
- mutation testing where canonically required;
- traceability;
- evidence-based completion;
- owner authority;
- stage boundaries;
- repository integrity.

ENFORCE:

- fixed Foundation baseline;
- objective exit criteria;
- duplicate detection;
- conflict detection;
- provenance verification;
- finding classification;
- stable finding identity;
- scope control;
- impact-based revalidation;
- explicit verification invalidation;
- regression analysis;
- root-cause analysis;
- convergence measurement;
- finite completion conditions.

======================================================================
MANDATORY DESIRED FLOW
======================================================================

INSPECT CANONICAL PROJECT
→ IDENTIFY AUTHORITATIVE FOUNDATION BASELINE
→ CHECK FOR CONFLICTS
→ CHECK FOR DUPLICATES
→ FREEZE APPROVED SCOPE
→ RECONSTRUCT VERIFICATION HISTORY
→ IDENTIFY FINDINGS
→ DEDUPLICATE FINDINGS
→ CLASSIFY FINDINGS
→ TRACE BLOCKERS TO AUTHORITY
→ IDENTIFY ROOT CAUSE
→ FIX GENUINE BLOCKERS
→ ANALYZE CHANGE IMPACT
→ REVALIDATE AFFECTED EVIDENCE
→ RUN BROADER REGRESSION WHERE JUSTIFIED
→ GATE 1
→ GATE 2
→ INDEPENDENT GATE 3
→ EVALUATE CONVERGENCE
→ FIX ANY REMAINING REAL BLOCKER
→ REVERIFY
→ SATISFY OBJECTIVE EXIT CRITERIA
→ FINAL CONSISTENCY AUDIT
→ VERIFIED FOUNDATION CHECKPOINT
→ RECONCILE TEMPORARY BACKUPS
→ DOCUMENT FINAL STATE
→ PROCEED TO NEXT AUTHORIZED STAGE.

======================================================================
PROHIBITED FAILURE MODE
======================================================================

DO NOT ALLOW:

GATE 1
→ PASS
→ GATE 2
→ PASS
→ GATE 3
→ FIND OPTIONAL IMPROVEMENT
→ CALL IT A BLOCKER
→ EXPAND FOUNDATION
→ CHANGE CODE
→ INVALIDATE EVERYTHING
→ START FROM ZERO
→ GATE 1
→ GATE 2
→ GATE 3
→ INVENT ANOTHER REQUIREMENT
→ EXPAND FOUNDATION AGAIN
→ REPEAT INDEFINITELY.

AND ALSO DO NOT ALLOW:

GATE 3
→ FIND REAL BLOCKER
→ CALL IT "FUTURE WORK"
→ IGNORE IT
→ FORCE FOUNDATION TO PASS.

Both are incorrect.

======================================================================
FINAL COMMAND
======================================================================

BE STRICT ABOUT REAL DEFECTS.

BE EQUALLY STRICT ABOUT PROCESS DEFECTS.

REINFORCE EXISTING RULES.

DO NOT CREATE DUPLICATE RULES.

DO NOT CREATE COMPETING GOVERNANCE.

DO NOT CHANGE REQUIREMENTS SILENTLY.

DO NOT MOVE THE GOALPOSTS.

DO NOT EXPAND FOUNDATION SILENTLY.

DO NOT WEAKEN TESTS TO FORCE SUCCESS.

DO NOT RERUN EVERYTHING WITHOUT TECHNICAL JUSTIFICATION.

DO NOT PRESERVE INVALID EVIDENCE.

DO NOT DISCARD VALID EVIDENCE WITHOUT JUSTIFICATION.

DO NOT HIDE REAL BLOCKERS AS FUTURE WORK.

DO NOT PROMOTE FUTURE IMPROVEMENTS INTO BLOCKERS WITHOUT AUTHORITY.

DO NOT CLAIM VERIFIED WITHOUT EVIDENCE.

MAKE FOUNDATION:

CORRECT.
CONSISTENT.
TRACEABLE.
SECURE.
VERIFIABLE.
FINITE.
CONVERGENT.
AND READY TO SUPPORT THE NEXT AUTHORIZED STAGE.

The goal is not FAST PASSING.

The goal is not ENDLESS REVIEW.

The goal is a legitimately verified company-grade Foundation that can
exit its stage once its approved obligations are genuinely satisfied.
======================================================================
```
