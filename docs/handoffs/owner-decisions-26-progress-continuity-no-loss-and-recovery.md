# Owner Decisions 26 — Permanent project progress, long-term continuity, no-loss, anti-stagnation and recovery directive

> **Status:** HISTORICAL — source input: the owner's directive of 2026-11-02, 15:43 UTC, sent after the session resumed from a weekly usage limit and while the change reconciling Stage 1 checkpoint D's temporary backup was in its Gate 3 review. Marked mandatory, permanent, and project-wide, for all stages and all future Claude Code sessions, it sets thirty-six rules on measurable stage progress without lowering quality, on preserving all material work and knowledge durably in the repository, on recovering the exact project state after a long pause, and on investigating, recovering, and preventing any loss of work; and it asks for an immediate status report (A to W), with the builder continuing the authorized work while answering. This is **not** an active source of truth. It is preserved by [DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), which keeps its rules in force through the existing mechanisms and applies them ([owner decisions 17](owner-decisions-17-reuse-reinforce-and-enhance-existing-controls.md), Rule 0).
>
> **Formatting note:** the message is reproduced inside one text block exactly as received. Nothing was added, removed, or changed in it. The title, this banner, and the dated heading are the builder's.

## 2026-11-02, 15:43 UTC

```text
======================================================================
PERMANENT PROJECT PROGRESS, LONG-TERM CONTINUITY,
NO-LOSS, ANTI-STAGNATION & RECOVERY DIRECTIVE
STATUS:
MANDATORY
PERMANENT
PROJECT-WIDE
ALL STAGES
ALL FUTURE CLAUDE CODE SESSIONS
NON-OPTIONAL
SERIOUS MODE.
Continue the currently authorized work while answering this instruction.
Do NOT stop valid productive work merely to prepare a status response.
======================================================================
CONTEXT & OWNER EXPECTATION
A full previous working month was consumed while the project remained
in Stage 1 / Foundation.
A new working month has now started.
I do NOT want the same situation repeated without strong technical
justification supported by evidence.
This does NOT mean:

* rush;
* skip verification;
* weaken testing;
* bypass Gate 1, Gate 2, or Gate 3;
* lower security;
* ignore legitimate blockers;
* reduce company-grade quality;
* prematurely move stages.

It means the development process itself must now be managed so that:
QUALITY
+
CORRECTNESS
+
SAFETY
+
TRACEABILITY
+
CONTINUITY
+
MEASURABLE FORWARD PROGRESS
all exist together.
A company-grade process must be rigorous.
It must also CONVERGE.
======================================================================
RULE 1 — NO ANOTHER MONTH OF UNEXPLAINED STAGNATION
Do not allow another long period to pass in the same stage merely because
verification, remediation, or review keeps repeating.
If a stage remains open for an extended period:
determine WHY.
Classify the cause:
LEGITIMATE BLOCKING ENGINEERING WORK
ARCHITECTURAL DEFECT
SECURITY DEFECT
TESTING DEFECT
REPEATED REGRESSION
VERIFICATION LOOP
SCOPE CREEP
MOVING EXIT CRITERIA
DUPLICATE WORK
PROCESS FAILURE
TOOLING FAILURE
ENVIRONMENT FAILURE
MISSING OWNER DECISION
UNNECESSARY PERFECTIONISM
OTHER EVIDENCED CAUSE.
Do not continue indefinitely without identifying the cause.
======================================================================
RULE 2 — TIME SPENT DOES NOT LOWER QUALITY
Do NOT move to the next stage merely because significant time has passed.
One month of work does NOT automatically make a stage complete.
However:
TIME SPENT MUST PRODUCE EXPLAINABLE PROGRESS.
If substantial time is being consumed without measurable convergence:
perform a root-cause and process review.
Do NOT simply continue repeating the same procedure.
======================================================================
RULE 3 — MEASURE STAGE CONVERGENCE
For the current stage, maintain evidence of whether the stage is moving
toward completion.
Track where applicable:

* completed requirements;
* remaining requirements;
* blockers;
* blocker severity;
* resolved findings;
* reopened findings;
* regressions;
* verification status;
* Gate 1 status;
* Gate 2 status;
* Gate 3 status;
* independent-review status;
* mutation-testing status;
* repository-completeness status;
* traceability status;
* unresolved owner decisions;
* remaining exit criteria.

Classify progress:
STRONGLY CONVERGING
CONVERGING
SLOWLY CONVERGING
STALLED
REGRESSING
NON-CONVERGENT.
If STALLED, REGRESSING, or NON-CONVERGENT:
do not blindly continue the same process.
Investigate and fix the reason.
======================================================================
RULE 4 — FIX THE PROCESS IF THE PROCESS IS THE PROBLEM
If project quality controls themselves are causing unnecessary looping,
do NOT remove them.
Instead determine whether the actual problem is:

* duplicate verification;
* incorrectly invalidated evidence;
* unnecessary full reruns;
* unstable tests;
* inconsistent reviewers;
* changing completion criteria;
* new requirements entering the stage silently;
* incorrect mutation-test configuration;
* duplicated governance;
* poor traceability;
* excessive coupling;
* bad checkpoint discipline.

Fix the PROCESS DEFECT without weakening the QUALITY CONTROL.
======================================================================
RULE 5 — NOTHING IMPORTANT MAY BE LOST
This requirement is absolute:
NO MATERIAL PROJECT KNOWLEDGE OR VALID WORK SHOULD BE LOST BECAUSE:

* a Claude session ended;
* conversation context expired;
* a container disappeared;
* a local environment was deleted;
* development paused;
* a subscription month ended;
* the project was untouched for weeks or months;
* a future Claude session has no memory of the earlier conversation.

Important project state must be DURABLY PRESERVED.
======================================================================
RULE 6 — REPOSITORY IS THE LONG-TERM PROJECT MEMORY
The repository and approved durable project systems must contain enough
information to reconstruct the project without depending on Claude's
conversation memory.
Preserve where applicable:

* project purpose;
* current architecture;
* requirements;
* System Rules;
* Constitution;
* ADRs;
* owner decisions;
* stage definitions;
* stage status;
* roadmap;
* completed work;
* partially completed work;
* remaining work;
* blockers;
* open questions;
* technical debt;
* implementation;
* tests;
* verification results;
* review findings;
* mutation results;
* configuration rules;
* dependencies;
* traceability;
* recovery instructions;
* deployment state;
* migration state;
* known issues;
* temporary backup state;
* next authorized action.

Conversation memory is useful context.
It is NOT the durable source of project truth.
======================================================================
RULE 7 — LONG-PAUSE RECOVERY MUST BE POSSIBLE
Design project continuity so that the following situation is safe:
PROJECT STOPS TODAY
↓
NO WORK FOR 1 MONTH
OR
3 MONTHS
OR
6 MONTHS
OR LONGER
↓
A FUTURE CLAUDE CODE SESSION OPENS THE REPOSITORY
↓
IT RECOVERS THE EXACT PROJECT STATE
↓
IT CONTINUES CORRECTLY.
The future session must be able to determine:
WHAT IS THIS PROJECT?
WHAT RULES GOVERN IT?
WHAT STAGE IS ACTIVE?
WHY IS THAT STAGE ACTIVE?
WHAT HAS BEEN COMPLETED?
WHAT REMAINS?
WHAT HAS BEEN VERIFIED?
WHAT HAS NOT BEEN VERIFIED?
WHAT FAILED PREVIOUSLY?
WHAT WAS FIXED?
WHAT BLOCKERS REMAIN?
WHAT DECISIONS WERE MADE?
WHAT OWNER DECISIONS REMAIN?
WHAT MUST NOT BE REPEATED?
WHAT IS THE NEXT AUTHORIZED ACTION?
If the repository cannot answer these questions:
CONTINUITY IS INCOMPLETE.
Correct it.
======================================================================
RULE 8 — NO RECONSTRUCTION FROM MEMORY AFTER A LONG PAUSE
After any long pause:
DO NOT start coding immediately.
DO NOT guess where development stopped.
DO NOT redesign the project.
DO NOT recreate missing work from vague memory.
First perform:
REPOSITORY RECOVERY
→ CANONICAL STATE INSPECTION
→ CHECKPOINT IDENTIFICATION
→ STAGE RECOVERY
→ FINDING RECOVERY
→ VERIFICATION RECOVERY
→ WORKTREE INSPECTION
→ BACKUP INSPECTION
→ TRACEABILITY CHECK
→ NEXT-ACTION CONFIRMATION.
Then continue from the exact correct point.
======================================================================
RULE 9 — PRESERVE A CANONICAL CONTINUATION RECORD
Use the project's existing canonical continuation/checkpoint mechanism.
Do NOT create a competing system if one already exists.
At minimum, the durable continuation state must make clear:
CURRENT STAGE
CURRENT OBJECTIVE
LAST VERIFIED CHECKPOINT
LATEST DURABLE COMMIT
COMPLETED WORK
IN-PROGRESS WORK
REMAINING WORK
CURRENT BLOCKERS
OPEN FINDINGS
FAILED CHECKS
GATE STATUS
MUTATION STATUS
REVIEW STATUS
OWNER DECISIONS REQUIRED
TEMPORARY BACKUPS
KNOWN RISKS
NEXT AUTHORIZED ACTION.
This record must be updated whenever material project state changes.
======================================================================
RULE 10 — IMPORTANT WORK MUST NOT EXIST ONLY UNCOMMITTED
Material valid work must not remain indefinitely only in:

* an unstaged state;
* a staged-but-uncommitted state;
* untracked files;
* temporary container storage;
* local-only branches;
* Claude memory.

Follow the canonical commit/checkpoint rules.
Do NOT blindly commit everything.
But every material item must receive a deliberate disposition.
======================================================================
RULE 11 — PRESERVE UNVERIFIED WORK WITHOUT FALSELY VERIFYING IT
If important work exists but verification is incomplete:
preserve it through the approved temporary/candidate checkpoint mechanism
where canonical policy permits.
Clearly classify it as:
UNVERIFIED
NOT APPROVED
NOT PRODUCTION-READY
NOT AUTHORITATIVE.
Durability must NOT be confused with verification.
But incomplete verification must NOT be an excuse to leave substantial
work vulnerable to loss.
======================================================================
RULE 12 — VERIFIED CHECKPOINTS MUST BE DURABLE
When a stage or meaningful milestone passes its required verification:
create the appropriate durable verified checkpoint according to canonical
repository policy.
Confirm where applicable:
LOCAL COMMIT
→ EXPECTED COMMIT SHA
→ PUSH
→ REMOTE STATE
→ REQUIRED CI
→ TRACEABILITY
→ STAGE RECORD.
Do not merely assume preservation succeeded.
Verify it.
======================================================================
RULE 13 — DO NOT LOSE WORK DURING CLEANUP
Before:

* deleting branches;
* retiring backups;
* removing drafts;
* cleaning untracked files;
* resetting changes;
* rebasing;
* replacing files;
* consolidating documentation;

confirm that no valid unique work will be lost.
Cleanup must make the repository simpler.
It must not erase project knowledge.
======================================================================
RULE 14 — NO FORGOTTEN BACKUPS
Temporary backups/checkpoints must remain traceable until formally
resolved.
Possible states:
ACTIVE
UNVERIFIED
RECONCILED
ARCHIVED
RETIRED
DELETION BLOCKED
SUPERSEDED
SAFE TO DELETE
DELETED
RETAINED FOR AUDIT.
No backup may simply be forgotten.
No temporary branch may become accidental parallel project history.
======================================================================
RULE 15 — NOTHING IMPORTANT ONLY IN CHAT
Any owner decision, requirement, architecture rule, correction,
verification result, blocker, stage state, or other material project
knowledge established during conversation must be reconciled into the
appropriate canonical repository location when required.
Do not assume future Claude sessions will have this conversation.
======================================================================
RULE 16 — NO DUPLICATE STATE WHEN RECOVERING
After a pause, search before creating.
Do NOT recreate:

* requirements;
* files;
* services;
* agents;
* workflows;
* configuration;
* governance;
* tests;
* documentation;

merely because the new session does not immediately see them.
FIRST SEARCH.
THEN MAP.
THEN CONTINUE.
======================================================================
RULE 17 — CURRENT STAGE MUST HAVE FINITE EXIT CRITERIA
Every stage must have objective completion criteria.
A stage must not remain open simply because additional improvements can
still be imagined.
Distinguish:
BLOCKING REQUIREMENT
from
OPTIONAL IMPROVEMENT.
CURRENT-STAGE WORK
from
FUTURE-STAGE WORK.
CORRECTNESS
from
UNBOUNDED PERFECTION.
When approved blocking exit criteria are satisfied and required
verification passes:
EXIT THE STAGE.
Do not keep reopening it for non-blocking improvements.
======================================================================
RULE 18 — DO NOT MOVE FUTURE WORK INTO CURRENT STAGE
If a reviewer discovers useful work that belongs later:
CLASSIFY IT.
TRACE IT.
PLACE IT IN THE CORRECT ROADMAP STAGE.
Do not silently expand the current stage.
This is especially important because uncontrolled scope expansion can
consume entire development periods without genuine stage progression.
======================================================================
RULE 19 — NO QUALITY REDUCTION TO GAIN SPEED
Efficiency does NOT authorize:

* skipping tests;
* ignoring blockers;
* bypassing independent review;
* weakening security;
* reducing financial controls;
* weakening traceability;
* hiding known defects;
* forcing stage completion.

Progress must come from:
BETTER PROCESS
BETTER ROOT-CAUSE ANALYSIS
BETTER SCOPE CONTROL
BETTER REUSE OF VALID EVIDENCE
BETTER CHECKPOINTING
BETTER CONTINUITY
BETTER ENGINEERING.
Not lower standards.
======================================================================
RULE 20 — NO WASTED REPETITION
Do not repeatedly redo valid completed work.
Before rerunning substantial verification ask:
WHAT CHANGED?
WHAT DID THAT CHANGE INVALIDATE?
WHAT ACTUALLY NEEDS REVALIDATION?
Use impact-based revalidation.
TARGETED WHEN SAFE.
FULL REGRESSION WHEN NECESSARY.
Do not restart from zero without technical justification.
======================================================================
RULE 21 — ROOT CAUSE BEFORE REPEATED PATCHING
When the same class of problem keeps returning:
STOP PATCHING INDIVIDUAL SYMPTOMS.
Determine the shared root cause.
Check:

* architecture;
* dependencies;
* interfaces;
* configuration;
* ownership;
* tests;
* governance;
* stage scope;
* verification process;
* repository state.

Fix the root.
Then verify related areas.
======================================================================
RULE 22 — CURRENT MONTH MUST HAVE VISIBLE FORWARD PROGRESS
Do not optimize for an artificial number of stages completed.
However, this development period must show measurable progress.
Maintain evidence of:

* completed requirements;
* resolved blockers;
* stabilized systems;
* passed verification;
* reduced remaining work;
* stage transitions where legitimately achieved;
* durable commits/checkpoints;
* updated traceability.

If progress stops:
identify why immediately rather than allowing another long unexplained
period to pass.
======================================================================
RULE 23 — PROGRESS REVIEW WITHOUT CONSTANT INTERRUPTION
Do not waste development time producing repetitive status reports.
Use existing canonical project status mechanisms.
Update them as part of normal work.
The purpose of progress tracking is to detect stagnation early,
not create another administrative workload.
======================================================================
RULE 24 — STAGE AGE IS A SIGNAL, NOT AN AUTOMATIC FAILURE
A stage taking a long time may be legitimate.
But prolonged stage duration triggers analysis.
Ask:
WHY IS THIS STAGE STILL OPEN?
WHAT BLOCKERS REMAIN?
ARE THEY DECREASING?
HAS SCOPE CHANGED?
ARE EXIT CRITERIA STABLE?
ARE WE REPEATING WORK?
ARE WE DISCOVERING REAL DEFECTS?
IS THE PROCESS NON-CONVERGENT?
Then act on the evidence.
======================================================================
RULE 25 — IF WORK WAS PREVIOUSLY LOST, DETERMINE WHY
If any previous project work is now believed to be missing:
do NOT merely say:
"most of the work is gone."
Perform a loss/recovery audit.
Determine:

* exactly what is missing;
* what evidence proves it previously existed;
* whether it was ever committed;
* whether it exists in another branch;
* whether it exists in archive/checkpoint branches;
* whether it exists in Git history;
* whether it exists in unmerged commits;
* whether documentation preserved it;
* whether tests preserved expected behavior;
* whether recovery is possible;
* why the loss occurred;
* what control failed.

Do not declare work permanently lost until reasonable repository recovery
paths have actually been checked.
======================================================================
RULE 26 — RECOVER BEFORE REBUILD
If apparently missing work may still exist:
SEARCH AND RECOVER IT FIRST.
Check where applicable:

* Git history;
* branches;
* archive branches;
* temporary checkpoints;
* tags;
* reflog if available and appropriate;
* previous commits;
* PR history;
* repository reports;
* generated artifacts;
* canonical documentation.

Do NOT immediately rebuild missing work from scratch.
Rebuilding prematurely can create:

* duplicates;
* conflicting implementations;
* lost history;
* inconsistent behavior.

======================================================================
RULE 27 — AFTER ANY LOSS, FIX THE LOSS MECHANISM
If important work was genuinely lost:
the task is NOT complete after rebuilding it.
Identify the reason the loss was possible.
Strengthen the canonical continuity/persistence mechanism so the same
class of loss cannot easily happen again.
Potential areas include:

* checkpoint frequency;
* commit discipline;
* remote push;
* backup lifecycle;
* session handoff;
* branch retention;
* repository status tracking;
* durable verification evidence.

Fix the root cause.
======================================================================
RULE 28 — RECOVERY MUST PRESERVE QUALITY
Recovered work must not be blindly trusted simply because it was found.
Determine:

* what version it belongs to;
* whether it was verified;
* whether it was superseded;
* whether later fixes exist;
* whether requirements changed;
* whether tests still pass.

Recover history without accidentally restoring obsolete defects.
======================================================================
RULE 29 — CURRENT AUTHORITATIVE STATE MUST ALWAYS BE CLEAR
At all times there must be one clearly identifiable current project
truth.
Temporary branches, archives, backups, and historical checkpoints must
not compete with it.
Future sessions must know:
THIS IS CURRENT.
THIS IS ARCHIVED.
THIS IS UNVERIFIED.
THIS IS SUPERSEDED.
THIS IS RETIRED.
THIS IS FUTURE WORK.
======================================================================
RULE 30 — LONG-TERM COMPANY CONTINUITY
This project is intended to outlive:

* the current Claude session;
* the current subscription month;
* one computer;
* one container;
* one developer;
* one AI model;
* long periods of inactivity.

Therefore the project must be engineered so development can pause and
resume safely without loss of:

* architecture;
* intent;
* requirements;
* decisions;
* implementation;
* verification;
* state;
* history;
* quality.

======================================================================
RULE 31 — FUTURE SESSION STARTUP PROTOCOL
After any substantial pause, the future builder must:

1. Inspect repository instructions.
2. Identify canonical sources.
3. Identify current branch/checkpoint.
4. Read current stage status.
5. Read roadmap.
6. Recover unresolved findings.
7. Recover verification status.
8. Inspect worktree.
9. Inspect temporary backups.
10. Check recent decisions.
11. Confirm current authority.
12. Determine next authorized action.
13. Continue from there.

Do NOT redesign.
Do NOT reset.
Do NOT duplicate.
======================================================================
RULE 32 — COMPANY-GRADE HANDOFF TEST
Assume this project is untouched for six months.
Then a qualified engineer who has never seen the conversation receives
the repository.
Can they determine:

* project purpose;
* architecture;
* current stage;
* rules;
* requirements;
* decisions;
* completed work;
* remaining work;
* tests;
* verification;
* known defects;
* blockers;
* technical debt;
* current authoritative state;
* next authorized action?

If not:
the repository is not sufficiently durable.
Correct the deficiency.
======================================================================
RULE 33 — DO NOT CONFUSE ACTIVITY WITH PROGRESS
Running many tests,
creating many documents,
making many commits,
or performing many reviews
does NOT automatically equal progress.
Progress means:
REMAINING VALID WORK IS SHRINKING
AND
CONFIDENCE IN THE COMPLETED WORK IS INCREASING.
Measure that.
======================================================================
RULE 34 — ESCALATE STAGNATION EARLY
Do not wait another month before recognizing a loop.
If repeated cycles show little or no convergence:
perform an immediate convergence/root-cause review.
Determine whether to:

* correct implementation;
* correct tests;
* correct process;
* correct scope;
* correct traceability;
* stabilize dependencies;
* resolve owner decision;
* or otherwise remove the actual blocker.

======================================================================
RULE 35 — NO SILENT LOSS ACCEPTANCE
If project work is missing:
DO NOT simply accept the loss and move forward.
Investigate.
Recover where possible.
Document what happened.
Reconcile recovered state.
Verify it.
Fix the continuity weakness.
Then continue.
======================================================================
RULE 36 — KEEP WORKING WHILE ANSWERING
Do not stop valid current work merely to explain project status.
While preparing the requested answer:
CONTINUE THE AUTHORIZED WORK.
Do not interrupt:

* valid testing;
* verification;
* analysis;
* safe implementation;
* repository recovery;
* approved remediation.

Stop only when a genuine blocker, safety condition, or owner-level
decision requires it.
======================================================================
REQUIRED IMMEDIATE STATUS REPORT
Give me an evidence-based answer containing:
A. Current stage.
B. How long the current stage has been active according to available
repository evidence.
C. Why it has remained open.
D. Whether the stage is currently converging.
E. Exact remaining blockers.
F. Whether scope expanded during the stage.
G. Whether verification loops occurred.
H. Whether work was genuinely lost.
I. Exactly what work is believed missing.
J. What repository recovery paths have been checked.
K. What was recovered.
L. What could not be recovered.
M. Why any unrecoverable work was lost.
N. What control is being strengthened to prevent recurrence.
O. Current last verified checkpoint.
P. Current durable repository state.
Q. Material uncommitted/untracked work.
R. Current backup/archive state.
S. Current Gate 1 / Gate 2 / Gate 3 status.
T. Current independent-review status.
U. Current mutation-testing status where applicable.
V. Exact next authorized action.
W. Whether the project could safely resume after several months of
inactivity using only the repository.
Do not tell me:
"everything is fine"
unless it has been verified.
Do not tell me:
"the work is gone"
unless recovery paths have been checked.
======================================================================
FINAL PERMANENT PRINCIPLE
I DO NOT WANT ANOTHER MONTH CONSUMED BY A PREVENTABLE LOOP.
I ALSO DO NOT WANT QUALITY LOWERED JUST TO MOVE FASTER.
I WANT:
COMPANY-GRADE QUALITY
+
MEASURABLE PROGRESS
+
FINITE STAGES
+
ROOT-CAUSE CORRECTION
+
DURABLE REPOSITORY STATE
+
LONG-TERM RECOVERY
+
ZERO ACCEPTANCE OF PREVENTABLE PROJECT-KNOWLEDGE LOSS.
THE PROJECT MUST BE ABLE TO STOP TODAY,
REMAIN UNTOUCHED FOR MONTHS,
AND LATER CONTINUE FROM THE EXACT CORRECT STATE
WITHOUT RESETTING, REDESIGNING, DUPLICATING, OR LOSING IMPORTANT WORK.
NO IMPORTANT REQUIREMENT LOST.
NO IMPORTANT DECISION LOST.
NO IMPORTANT IMPLEMENTATION LOST.
NO IMPORTANT TEST LOST.
NO IMPORTANT VERIFICATION EVIDENCE LOST.
NO IMPORTANT TRACEABILITY LOST.
NO IMPORTANT STAGE STATE LOST.
NO IMPORTANT OWNER DECISION LOST.
NO VALID WORK LEFT ONLY IN CHAT OR AN EPHEMERAL ENVIRONMENT.
AND:
NO ENDLESS FOUNDATION LOOP.
NO MOVING GOALPOSTS.
NO UNCONTROLLED SCOPE EXPANSION.
NO BLIND REPETITION.
NO LOWERING QUALITY FOR SPEED.
NO CLAIM OF LOSS WITHOUT RECOVERY INVESTIGATION.
NO CLAIM OF COMPLETION WITHOUT EVIDENCE.
======================================================================
MANDATORY OPERATING FLOW
INSPECT
→ RECOVER CANONICAL STATE
→ CONFIRM CURRENT STAGE
→ CONFIRM LAST VERIFIED CHECKPOINT
→ INVENTORY CURRENT WORK
→ RECOVER ANY APPARENTLY MISSING WORK
→ IDENTIFY BLOCKERS
→ IDENTIFY ROOT CAUSES
→ CHECK CONVERGENCE
→ FIX REAL PROBLEMS
→ TEST
→ VERIFY
→ REVALIDATE AFFECTED AREAS
→ RECONCILE
→ UPDATE TRACEABILITY
→ PRESERVE EVERYTHING MATERIAL
→ COMMIT/CHECKPOINT ACCORDING TO POLICY
→ VERIFY DURABILITY
→ RECORD EXACT CONTINUATION STATE
→ CONTINUE FORWARD.
THE PROJECT MUST PROGRESS THROUGH CONTROLLED,
VERIFIED, DURABLE ENGINEERING — NOT THROUGH LOST WORK,
REPEATED RECONSTRUCTION, OR ENDLESS STAGE LOOPS.
```
