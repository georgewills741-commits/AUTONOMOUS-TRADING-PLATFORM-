# Owner Decisions 22 — The limits on record: a question, the instruction to fix them, and two rule sets on retiring temporary branches and on the configuration's resource safety

> **Status:** HISTORICAL — source input: two messages of the owner of 2026-10-27, sent after Stage 1's checkpoint C was committed (`b11abe7`) and reported. The first, at 07:29 UTC, asks what the builder meant by the first of the report's "Limits on record", that a configuration file larger than available memory stops the load with a Python error instead of a clean refusal, and asks the builder to continue while answering. The second, at 07:59 UTC, after the builder had answered and offered to add a limit on a file's size, says that these limits are under item 8 of the report, asks the builder to start fixing all of these problems if it can, making sure everything is safe, and to treat that as a rule. It then sets two rule sets. The first is for temporary branches whose deletion the environment refuses (HTTP 403): their lifecycle status, where they are recorded and with which fields, the checks before one is called safe to delete, and the report. The second is for the configuration's resource safety, clean failure, and memory exhaustion: look for an existing control first, classify the current behaviour, fail cleanly and closed with a limit that has an engineering reason, test, review the denial-of-service risk, document, classify, trace, and report. The client's own "Continue from where you left off." prompts, sent while the session was stopped at its usage limit, and the owner's "Continue" messages, the first at 10:37 UTC, are procedural and not kept ([owner decisions 16](owner-decisions-16-short-instructions-approvals-and-questions.md)). This is **not** an active source of truth. It is preserved by [DEC-054](../decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md), which keeps its two rule sets in force and applies them.
>
> **Formatting note:** each message is reproduced inside one text block exactly as received, including the spaces that end three of their lines and the two line breaks that end the first. Nothing was added, removed, or changed in them. The title, this banner, and the dated headings are the builder's.

## 2026-10-27, 07:29 UTC

```text
What do you mean by Limits on record:
A configuration file larger than available memory stops the load with a Python error, not a clean refusal. Nothing is loaded or shown, and the developer guide states this limit.

Continue doing what you're doing while answering this question 


```

## 2026-10-27, 07:59 UTC

```text
All this are under number 8 Limits on record:

Good now you can now start fixing all this problems if you can fix them because I will not want any problem because we have gone so far that I will not want errors or problems you can treat this as a rule you have to know but make sure everything is safe and no problem 😊 

Then concerning about this 

======================================================================
TEMPORARY BRANCH RETIREMENT, DELETION-BLOCKED
& ANTI-CONFUSION CONTROL

SERIOUS MODE.

The environment has returned HTTP 403 when attempting to delete certain
temporary backup branches.

Do NOT repeatedly retry deletion without evidence that permissions or
repository policy have changed.

Do NOT create duplicate branches merely to work around the 403.

Do NOT falsely mark a branch as physically DELETED while the Git reference
still exists.

The objective is to make these branches operationally equivalent to
retired/deleted work WITHOUT creating confusion, duplicate authority,
false repository state, or future accidental reuse.

Follow DEC-052 and all existing canonical repository/branch-retention
rules first.

======================================================================
1 — USE A CLEAR LIFECYCLE STATUS

For any temporary backup branch whose valid contents have already been
reconciled into the canonical retained archive/checkpoint and whose
physical deletion is blocked by permissions, classify it as:

RETIRED
DELETION BLOCKED
NON-AUTHORITATIVE
DO NOT USE
DO NOT MERGE
DO NOT DEVELOP FROM
RETAINED ONLY BECAUSE PHYSICAL DELETION IS CURRENTLY UNAVAILABLE

Preferred combined state:

RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED

Do NOT use only:

DELETED

because that would be factually incorrect while the branch still exists.

======================================================================
2 — CANONICAL ARCHIVE REMAINS THE REFERENCE

Where DEC-052 establishes:

claude/archive/unverified-backup-checkpoint-c

as the retained archive/reference branch, preserve that decision.

If another temporary branch contains identical content and has already
served its purpose:

it must NOT remain a competing active branch.

Record that it is:

SUPERSEDED / RECONCILED BY:
claude/archive/unverified-backup-checkpoint-c

where this is factually correct.

Apply the same principle to checkpoint B and item 3 temporary backup
branches according to their actual canonical archive/reconciliation state.

======================================================================
3 — DO NOT CREATE ANOTHER BRANCH JUST TO MARK IT RETIRED

Do NOT solve this by creating additional branches such as:

deleted-copy
old-copy
final-copy
backup-of-backup
retired-copy

unless an existing canonical repository rule explicitly requires such a
branch.

That would increase duplication rather than solve it.

Prefer updating the existing canonical branch lifecycle / repository
state record.

======================================================================
4 — RECORD THE RETIREMENT IN THE CANONICAL REPOSITORY

Use the project's existing canonical branch/checkpoint/backup registry or
repository-state mechanism.

If one already exists:

UPDATE IT.

Do NOT create a competing registry.

For each affected branch record, where appropriate:

BRANCH NAME
PURPOSE
ORIGINAL STATUS
CURRENT STATUS
CANONICAL REPLACEMENT / ARCHIVE
CONTENT PARITY STATUS
LAST VERIFIED COMMIT SHA
DELETION ATTEMPT RESULT
DELETION FAILURE REASON
DECISION / POLICY REFERENCE
SAFE-TO-DELETE STATUS
DEPENDENCIES
FINAL DISPOSITION

Example status:

Branch:
<temporary branch>

Status:
RETIRED — DELETION BLOCKED

Authority:
NONE

Canonical retained branch:
claude/archive/unverified-backup-checkpoint-c

Content:
VERIFIED IDENTICAL, if actually verified

Use:
PROHIBITED FOR NEW DEVELOPMENT

Merge:
PROHIBITED UNLESS EXPLICITLY REACTIVATED THROUGH GOVERNANCE

Deletion:
SAFE TO DELETE WHEN PERMISSIONS ALLOW, if verified safe

Reason still present:
REMOTE DELETE RETURNED HTTP 403

Decision:
DEC-052

======================================================================
5 — VERIFY BEFORE MARKING SAFE TO DELETE

Before assigning:

SAFE TO DELETE WHEN PERMITTED

verify that:

1. All valid unique work has been preserved elsewhere.
2. The canonical archive/checkpoint exists.
3. Commit/content parity is confirmed where claimed.
4. No open work depends on the temporary branch.
5. No active PR depends on it.
6. No required verification evidence exists only on it.
7. No unresolved owner decision depends on it.
8. No deployment or automation depends on it.
9. Traceability has been updated.
10. DEC-052 or another canonical rule permits retirement/deletion.

If any of these checks fail:

DO NOT mark the branch safe to delete.

Classify it accurately and investigate.

======================================================================
6 — DO NOT CONTINUALLY RETRY A KNOWN 403

Once deletion has been attempted and HTTP 403 has been confirmed:

record the failure.

Do not waste development cycles repeatedly issuing the same deletion
command.

Retry only when there is evidence that:

- permissions changed;
- authentication changed;
- repository protection changed;
- environment capabilities changed;
- the owner explicitly requests another attempt;
- or canonical maintenance work calls for another cleanup attempt.

This prevents another unnecessary operational loop.

======================================================================
7 — IF RENAMING IS POSSIBLE, DO NOT DO IT AUTOMATICALLY

Do not rename branches merely to make them "look deleted."

Git branch renaming may internally require creating another reference and
deleting the old one, which could:

- fail under the same permission restriction;
- temporarily create duplicate refs;
- break links;
- break PR references;
- damage traceability;
- create unnecessary repository noise.

Only rename a retired branch if:

- canonical branch policy allows it;
- the rename is technically supported;
- dependencies are checked;
- it improves clarity;
- it does not create duplicate references;
- traceability is preserved.

If renaming is justified, prefer terminology such as:

retired
superseded
deletion-blocked

NOT:

deleted

while the branch still physically exists.

======================================================================
8 — LOGICAL RETIREMENT MUST BE ENFORCED

Once a branch is classified:

RETIRED — DELETION BLOCKED

Claude Code must treat it as logically removed from active engineering.

That means:

DO NOT base new development on it.

DO NOT merge from it automatically.

DO NOT use it as the latest project truth.

DO NOT compare it as a competing canonical implementation unless needed
for audit/recovery.

DO NOT reopen it simply because it remains visible remotely.

The canonical repository state determines authority, not mere branch
existence.

======================================================================
9 — PHYSICAL DELETION MAY HAPPEN LATER

If permissions later allow branch deletion:

first re-check that the branch is still:

RETIRED
NON-AUTHORITATIVE
RECONCILED
DEPENDENCY-FREE
SAFE TO DELETE.

Then delete it according to canonical repository policy.

After successful deletion:

update the lifecycle record from:

RETIRED — DELETION BLOCKED

to:

RETIRED — PHYSICALLY DELETED

or the existing canonical equivalent.

Record the deletion evidence where appropriate.

Do not leave the registry claiming deletion is blocked after deletion
actually succeeds.

======================================================================
10 — IF DELETION IS NEVER NECESSARY

If DEC-052 or repository policy determines that retaining the branch is
useful for audit/history and it causes no technical or governance problem:

it may remain.

But its status must still be unambiguous:

ARCHIVED / RETIRED
NON-AUTHORITATIVE
NOT ACTIVE
NOT FOR DEVELOPMENT

Do not delete merely for cosmetic cleanliness when retention has a valid
audit purpose.

======================================================================
11 — APPLY THIS TO ALL AFFECTED TEMPORARY BRANCHES

Inspect:

- checkpoint C temporary backup branch;
- checkpoint B temporary backup branch;
- item 3 backup branch;
- any other temporary/unverified backup branch subject to the same issue.

For each one independently determine:

ACTIVE
ARCHIVED
RECONCILED
RETIRED
SUPERSEDED
DELETION BLOCKED
SAFE TO DELETE
MUST RETAIN
REQUIRES INVESTIGATION.

Do not assume identical disposition merely because their names are similar.

======================================================================
12 — NO DUPLICATE AUTHORITY

A physically existing retired branch must NOT be treated as another
source of truth.

There must still be:

ONE AUTHORITATIVE PROJECT STATE.

If the archive branch is the canonical retained copy under DEC-052:

reference it.

Do not let the temporary branch compete with it.

======================================================================
13 — FINAL VERIFICATION

After applying retirement status, verify:

- no active workflow references the retired branch;
- no current stage uses it;
- no valid work exists only there;
- canonical archive/checkpoint is intact;
- traceability is intact;
- repository documentation reflects reality;
- no duplicate authority was introduced;
- no misleading "deleted" status exists;
- the 403 deletion limitation is documented;
- future deletion conditions are clear.

======================================================================
14 — REQUIRED REPORT

Report for each affected branch:

A. Exact branch name.

B. Current commit SHA.

C. Canonical archive/replacement.

D. Whether content parity was actually verified.

E. Current lifecycle status.

F. Whether it is authoritative.

G. Whether anything still depends on it.

H. Whether it is safe to delete.

I. Why deletion failed.

J. Whether deletion should be retried now.

K. Whether it should remain retained.

L. Exact next action.

Do not say "identical" unless that comparison was actually performed.

Do not say "safe to delete" without checking dependencies.

======================================================================
FINAL RULE

A BRANCH THAT STILL EXISTS IS NOT PHYSICALLY DELETED.

DO NOT FALSIFY REPOSITORY STATE.

Instead use:

RETIRED
+
DELETION BLOCKED
+
NON-AUTHORITATIVE
+
SAFE TO DELETE WHEN PERMITTED

when those statements are supported by evidence.

The desired lifecycle is:

TEMPORARY BACKUP
→ RECONCILED
→ CANONICAL CONTENT PRESERVED
→ RETIRED
→ DELETION ATTEMPT
→ HTTP 403
→ RETIRED / DELETION BLOCKED
→ NO LONGER USED
→ PERIODIC OR EVENT-DRIVEN CLEANUP
→ DELETE IF LATER PERMITTED AND STILL APPROPRIATE
→ UPDATE TRACEABILITY.

NOT:

DELETE FAILS
→ CREATE ANOTHER BRANCH
→ CREATE MORE DUPLICATES
→ FORGET WHICH ONE IS AUTHORITATIVE.

AND NOT:

DELETE FAILS
→ CALL IT DELETED ANYWAY
→ MISLEAD FUTURE ENGINEERS.

Keep the repository truthful, clean, traceable, non-duplicative, and
company-grade.


And about this also ======================================================================
CONFIGURATION RESOURCE-SAFETY, CLEAN-FAILURE
& MEMORY-EXHAUSTION HARDENING RULE

SERIOUS MODE.

You reported:

"A configuration file larger than available memory stops the load with
a Python error, not a clean refusal. Nothing is loaded or shown, and the
developer guide states this limit."

Treat this as a KNOWN ROBUSTNESS GAP that must be evaluated against the
canonical Foundation requirements, security rules, configuration rules,
reliability requirements, and stage exit criteria.

Do NOT hide the issue merely because it is documented.

Documentation of a limitation does NOT automatically mean the
implementation is sufficiently robust.

======================================================================
1 — FIRST DETERMINE WHETHER THIS IS ALREADY COVERED

Before creating any new rule, component, validation layer, exception
handler, configuration subsystem, or governance entry:

SEARCH THE REPOSITORY.

Determine whether the project already defines:

- configuration size limits;
- configuration resource limits;
- memory-safety behavior;
- input-size validation;
- failure-mode requirements;
- fail-closed behavior;
- configuration parsing limits;
- resource-exhaustion handling;
- denial-of-service protections;
- startup/load error handling;
- structured configuration errors.

If an existing canonical mechanism already covers this:

REINFORCE AND FIX THAT MECHANISM.

Do NOT create a duplicate solution.

======================================================================
2 — CLASSIFY THE CURRENT BEHAVIOR PRECISELY

Determine the exact current behavior from evidence.

Verify:

- what function loads the configuration;
- whether the full file is read into memory;
- which parser is used;
- what exception actually occurs;
- whether the exception is deterministic;
- whether memory exhaustion can affect the process or host;
- whether partial state is created;
- whether previous configuration remains intact;
- whether secrets or configuration values can leak in error output;
- whether logs expose sensitive contents;
- whether the process crashes;
- whether startup fails safely;
- whether recovery is deterministic.

Do not describe it generically as "Python error" if the actual exception
can be identified.

======================================================================
3 — FAIL CLEANLY AND FAIL CLOSED

An oversized or resource-unsafe configuration must NOT result in an
uncontrolled failure path where avoidable.

The desired behavior is:

CONFIGURATION REQUEST
→ PRE-VALIDATION
→ SIZE / RESOURCE SAFETY CHECK
→ SAFE PARSING
→ SCHEMA VALIDATION
→ ATOMIC ACCEPTANCE
or
→ CONTROLLED REJECTION.

A rejected configuration must NOT become partially active.

If loading fails:

- preserve the last known valid configuration where canonical design
  requires it;
- do not expose partial configuration;
- do not silently continue with partially parsed state;
- do not expose sensitive values;
- return/record a structured failure;
- provide a deterministic reason where possible.

======================================================================
4 — DO NOT RELY ONLY ON AVAILABLE RAM

Do not use:

"the machine will run out of memory first"

as the effective configuration-size control.

Define or reuse a deliberate safe limit or resource policy according to
canonical project architecture.

The limit must be based on justified engineering constraints, not an
arbitrary number invented merely to make the test pass.

Consider where applicable:

- maximum accepted configuration size;
- parser behavior;
- expected configuration scale;
- memory amplification during parsing;
- concurrent loads;
- host minimum resources;
- deployment environments;
- denial-of-service risk;
- recovery behavior.

If the canonical project already defines such a limit:

use it.

If no limit exists and defining one materially requires an owner or
architecture decision:

report the gap rather than inventing policy.

======================================================================
5 — VALIDATE BEFORE EXPENSIVE ALLOCATION WHERE PRACTICAL

Where technically appropriate, reject an obviously oversized input
before attempting to fully materialize or parse it.

Possible safe controls may include, depending on architecture:

- file-size check before loading;
- bounded reads;
- streaming where supported and justified;
- parser limits;
- explicit maximum byte size;
- controlled resource budget;
- validated decompression limits if compressed input exists.

Do not implement complexity that the system does not need.

Use the simplest correct mechanism that satisfies the canonical
requirements.

======================================================================
6 — HANDLE MEMORY / RESOURCE EXCEPTIONS DEFENSIVELY

Even with pre-validation, defensive handling may still be required.

Inspect whether relevant allocation, parser, or resource exceptions can
occur.

If so, handle them at the correct boundary.

The application should convert expected resource-limit failures into a
controlled project-defined error rather than exposing an uncontrolled
stack trace or ambiguous crash where avoidable.

Do NOT catch broad exceptions merely to suppress real defects.

Catch only what is technically justified.

======================================================================
7 — ATOMIC CONFIGURATION ACTIVATION

A new configuration must not become authoritative until the complete
configuration has successfully passed all required validation.

Preferred model:

READ / LOAD
→ PARSE
→ VALIDATE
→ CROSS-CHECK
→ ACCEPT
→ ATOMICALLY ACTIVATE.

If any step fails:

REJECT THE CANDIDATE CONFIGURATION.

Do not mutate active state incrementally before validation completes
unless the canonical architecture explicitly requires and safely
supports that behavior.

======================================================================
8 — PRESERVE LAST KNOWN GOOD STATE

Where the platform supports runtime configuration reloads, inspect
whether failure should preserve the last known good configuration.

If canonical design requires this:

FAILED NEW CONFIG
→ CURRENT VALID CONFIG REMAINS ACTIVE
→ FAILURE RECORDED
→ NO PARTIAL STATE.

Do not invent runtime fallback behavior if the current architecture does
not support configuration reloads.

Follow the existing lifecycle.

======================================================================
9 — STRUCTURED ERROR BEHAVIOR

Where applicable, produce a controlled error such as:

CONFIGURATION_REJECTED
RESOURCE_LIMIT_EXCEEDED
CONFIGURATION_TOO_LARGE

or the project's existing canonical equivalent.

The error should identify:

- failure category;
- safe user/developer message;
- whether active configuration changed;
- remediation guidance where appropriate.

Do not include:

- secrets;
- raw credentials;
- entire configuration contents;
- unnecessary sensitive paths or values.

======================================================================
10 — TEST THE FAILURE MODE

Add or strengthen tests according to the existing canonical testing
framework.

Where applicable test:

1. configuration below limit loads successfully;
2. configuration at the accepted boundary behaves correctly;
3. configuration above the accepted boundary is rejected cleanly;
4. malformed configuration is rejected separately from oversized input;
5. no partial state is activated;
6. last known valid state remains correct where applicable;
7. error output contains no secrets;
8. recovery after rejection works;
9. repeated invalid requests do not corrupt state;
10. resource failure does not silently bypass validation.

Do not create unrealistic tests that require actually exhausting the
host's entire memory when the behavior can be tested safely through
bounded conditions, mocks, controlled limits, or equivalent mechanisms.

======================================================================
11 — SECURITY / DENIAL-OF-SERVICE REVIEW

Evaluate whether an attacker or malformed input could deliberately force
excessive memory allocation.

Determine whether this configuration-loading path is:

- local only;
- administrator controlled;
- authenticated;
- remotely reachable;
- indirectly reachable through automation.

The more exposed the path, the stronger the resource-control requirement.

Do not overstate the threat if the path is strictly local and trusted.

But do not ignore a reachable resource-exhaustion vector.

======================================================================
12 — DOCUMENTATION MUST MATCH IMPLEMENTATION

After fixing or classifying the behavior:

update the developer documentation so it describes the actual enforced
behavior.

The documentation should not merely say:

"large files may crash Python."

If the implementation now provides a controlled limit, document the
canonical limit/policy and expected error behavior where appropriate.

Do not duplicate numeric configuration limits across multiple
authoritative documents.

Reference the canonical configuration source.

======================================================================
13 — FOUNDATION BLOCKER CLASSIFICATION

Determine whether this issue is:

CRITICAL BLOCKER
BLOCKING DEFECT
MAJOR DEFECT
MINOR DEFECT
NON-BLOCKING HARDENING
FUTURE-STAGE WORK

using the canonical Foundation exit criteria.

Do NOT downgrade it merely because documentation exists.

Do NOT upgrade it merely because a cleaner error would be preferable.

The classification must be evidence-based.

If Foundation requires controlled invalid-input/resource-limit handling,
this may be a real blocker.

If Foundation only requires documented safe failure with no partial state
and the current behavior satisfies canonical requirements, classify it
accordingly.

======================================================================
14 — NO TEST-PASS HACK

Do not solve this by:

- artificially lowering test input size;
- catching every exception;
- suppressing the traceback without fixing behavior;
- removing the test;
- weakening the requirement;
- documenting the crash as "expected" simply to pass verification.

Fix the actual failure boundary where required.

======================================================================
15 — TRACEABILITY

If this issue is corrected, preserve traceability:

FINDING
→ ROOT CAUSE
→ REQUIREMENT / RULE
→ IMPLEMENTATION CHANGE
→ TEST
→ VERIFICATION
→ FINAL STATUS.

If it is intentionally accepted as a documented limitation:

record the authoritative reason and classification.

Do not leave the decision only in conversation.

======================================================================
16 — VERIFY NO DUPLICATE RESOURCE-LIMIT SYSTEM

Before implementing any new configuration-size control, inspect whether
resource-limit enforcement already exists elsewhere.

If a canonical resource-policy mechanism exists:

use it.

Do not hard-code another independent limit that can later drift.

ONE CANONICAL RESOURCE POLICY WHERE APPROPRIATE.

======================================================================
17 — FINAL REQUIRED RESULT

Report:

A. Exact root cause.

B. Exact current exception/failure path.

C. Whether any partial state is created.

D. Whether active configuration can be corrupted.

E. Whether secrets can leak.

F. Whether the process crashes or only the load operation fails.

G. Existing canonical requirement covering this behavior.

H. Current severity/classification.

I. Whether a fix is required before Foundation exit.

J. Correct remediation if required.

K. Tests added/updated.

L. Verification result.

M. Canonical documentation updated.

N. Whether the limitation remains after remediation.

======================================================================
FINAL PRINCIPLE

A COMPANY-GRADE PLATFORM SHOULD NOT DEPEND ON RANDOM MEMORY EXHAUSTION
AS ITS INPUT-SIZE CONTROL.

KNOWN RESOURCE LIMITS SHOULD BE:

DEFINED,
ENFORCED,
TESTED,
TRACEABLE,
AND FAILED SAFELY WHERE PRACTICAL.

DOCUMENTATION DOES NOT SUBSTITUTE FOR ROBUST IMPLEMENTATION.

AT THE SAME TIME:

DO NOT CREATE UNNECESSARY COMPLEXITY,
DO NOT INVENT ARBITRARY LIMITS,
DO NOT DUPLICATE EXISTING CONTROLS,
AND DO NOT TURN OPTIONAL HARDENING INTO A FALSE BLOCKER.

INSPECT
→ CLASSIFY
→ TRACE
→ FIX THE ROOT CAUSE IF REQUIRED
→ TEST
→ VERIFY
→ DOCUMENT
→ PRESERVE.
```
