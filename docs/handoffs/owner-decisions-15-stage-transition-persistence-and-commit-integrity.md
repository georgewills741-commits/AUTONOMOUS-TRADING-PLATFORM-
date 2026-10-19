# Owner Decisions 15 — Stage-transition repository persistence, commit integrity, and no unsaved work

> **Status:** HISTORICAL — source input: the owner's message of 2026-10-14, sent while the change that preserves owner decisions 14 was in its third gate. It sets mandatory, permanent, project-wide rules that block a stage transition (its STATUS lines): before a stage is complete, or work proceeds to the next authorized stage, all material work of the stage is identified, classified, reconciled, placed in its canonical location, preserved, traceable, version-controlled where appropriate, committed according to repository policy, pushed or durably preserved where required, and verified against the correct repository state; no important work is left only as uncommitted or untracked changes, temporary container state, forgotten drafts, temporary branches with unresolved status, conversation memory, or terminal history; and the objective is not to commit everything blindly but to classify and resolve every material item deliberately (its PURPOSE). A draft is a lifecycle status, not a repository state: an important draft may and often should be committed when repository policy permits, explicitly marked DRAFT, NOT APPROVED, NOT AUTHORITATIVE, NOT VERIFIED, and NOT PRODUCTION-READY, and committing it promotes nothing (its §1); every material draft has an explicit disposition (its §7) and creates no parallel authority (its §8); Gate 3 findings are persisted (its §13); and, before the next stage, a final report is made in items A to V (its §30). This is **not** an active source of truth. It is preserved by [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), which records how it is applied until its adoption as a builder text is decided.
>
> **Formatting note:** the message is reproduced inside one text block exactly as received, so that its lines, separator lines, lists, and arrows stay as they were sent. Nothing was added, removed, or changed in it. The title and this banner are the builder's.

```text
======================================================================
STAGE TRANSITION REPOSITORY PERSISTENCE, COMMIT INTEGRITY
& NO-UNSAVED-WORK RULE
======================================================================

STATUS:
MANDATORY
PERMANENT
PROJECT-WIDE
STAGE-TRANSITION BLOCKER
COMPANY-GRADE ENGINEERING CONTROL

PURPOSE:

Before Foundation or any future stage may be considered complete or
before work proceeds to the next authorized stage, confirm that all
material project work belonging to the completed stage has been:

- identified;
- classified;
- reconciled;
- placed in the correct canonical repository location;
- preserved;
- traceable;
- version-controlled where appropriate;
- committed according to repository policy;
- pushed / durably preserved where required;
- and verified against the correct repository state.

NO IMPORTANT PROJECT WORK MAY BE LEFT ONLY AS:

- uncommitted changes;
- untracked files;
- temporary container state;
- local-only modifications;
- forgotten drafts;
- unstaged edits;
- abandoned generated artifacts;
- temporary branches with unresolved status;
- Claude conversation memory;
- terminal history;
- hidden assumptions.

The objective is NOT to blindly commit everything.

The objective is to ensure that EVERY MATERIAL ITEM is deliberately
classified and resolved before stage transition.

======================================================================
1 — DRAFT DOES NOT MEAN UNSAVED
======================================================================

A DRAFT is a lifecycle/status classification.

UNCOMMITTED is a repository-state classification.

They are NOT the same thing.

An important draft may and often SHOULD be committed when repository
policy permits, provided it remains explicitly marked:

DRAFT
NOT APPROVED
NOT AUTHORITATIVE
NOT VERIFIED
NOT PRODUCTION-READY

Committing a draft does NOT promote it to approval.

Likewise:

COMMITTED
does NOT automatically mean
APPROVED.

COMMITTED
does NOT automatically mean
VERIFIED.

COMMITTED
does NOT automatically mean
AUTHORITATIVE.

COMMITTED
does NOT automatically mean
PRODUCTION-READY.

Preserve project work without falsifying its lifecycle status.

======================================================================
2 — COMPLETE UNCOMMITTED-WORK INVENTORY
======================================================================

Before stage transition, inspect the ENTIRE repository state.

At minimum inspect:

- current branch;
- git status;
- staged changes;
- unstaged changes;
- untracked files;
- ignored files relevant to project work;
- modified tracked files;
- deleted files;
- renamed files;
- new documents;
- draft documents;
- generated artifacts;
- test reports;
- verification reports;
- mutation reports;
- review findings;
- temporary files;
- local configuration changes;
- migration files;
- scripts;
- source code;
- tests;
- CI configuration;
- roadmap changes;
- traceability changes;
- ADRs;
- requirements;
- governance files;
- stage-status records.

Do not inspect only the obvious files.

Produce a complete material-change inventory.

======================================================================
3 — CLASSIFY EVERY UNCOMMITTED ITEM
======================================================================

Every material uncommitted or untracked item must be classified as one
of:

REQUIRED STAGE OUTPUT
VALID IMPLEMENTATION CHANGE
VALID DOCUMENTATION CHANGE
VALID TEST CHANGE
VALID CONFIGURATION CHANGE
VALID TRACEABILITY CHANGE
VALID REVIEW / VERIFICATION EVIDENCE
IMPORTANT DRAFT
FUTURE-STAGE WORK
TEMPORARY DEVELOPMENT ARTIFACT
GENERATED ARTIFACT
LOCAL-ONLY CONFIGURATION
SECRET / SENSITIVE MATERIAL
OBSOLETE FILE
DUPLICATE FILE
ACCIDENTAL CHANGE
UNKNOWN / REQUIRES INVESTIGATION

Do not leave items unclassified.

UNKNOWN material changes block stage transition until investigated.

======================================================================
4 — NOTHING MATERIAL MAY BE SILENTLY DISCARDED
======================================================================

Do not use:

git reset
git clean
checkout
restore
branch deletion
file deletion
or similar destructive actions

on material project work until its purpose and status are known.

Before discarding anything determine:

- origin;
- purpose;
- owner;
- relationship to current stage;
- whether equivalent work already exists;
- whether it contains valid unique work;
- whether it must be retained for traceability;
- whether it is superseded.

NO VALID WORK LOSS.

======================================================================
5 — NOTHING INAPPROPRIATE MAY BE COMMITTED
======================================================================

Repository completeness does NOT mean committing everything blindly.

Do NOT commit:

- secrets;
- API keys;
- passwords;
- tokens;
- private keys;
- production credentials;
- temporary caches;
- irrelevant generated files;
- local environment noise;
- build artifacts not intended for version control;
- editor state;
- accidental binaries;
- temporary logs unless required evidence;
- unrelated personal files.

Follow .gitignore and canonical repository policy.

If an important artifact should not be version-controlled, preserve its
metadata, generation process, or evidence through the correct canonical
mechanism instead.

======================================================================
6 — REQUIRED STAGE OUTPUTS MUST BE DURABLY PRESERVED
======================================================================

Every required output of the current stage must be present in the
repository or canonical durable project system before stage exit.

Examples may include:

- requirements;
- decisions;
- architecture;
- stage documentation;
- source code;
- tests;
- configuration schema;
- migration definitions;
- governance updates;
- traceability;
- verification reports;
- issue records;
- known limitations;
- open questions;
- current-stage status;
- next-stage handoff information.

If an important stage artifact exists only locally:

STAGE EXIT IS BLOCKED.

======================================================================
7 — MATERIAL DRAFTS MUST HAVE AN EXPLICIT DISPOSITION
======================================================================

Every material draft discovered before stage exit must have one explicit
disposition:

FINALIZED AND APPROVED
COMMITTED AS DRAFT
MAPPED TO EXISTING CANONICAL MATERIAL
SUPERSEDED
DEFERRED TO FUTURE STAGE
REQUIRES OWNER DECISION
REJECTED WITH TRACEABILITY
ARCHIVED ACCORDING TO POLICY

No important draft may simply remain forgotten in the working tree.

======================================================================
8 — DRAFTS MUST NOT CREATE PARALLEL AUTHORITY
======================================================================

If a draft duplicates or overlaps an existing canonical requirement,
architecture document, policy, or decision:

DO NOT commit it as a competing authoritative document.

Instead:

COMPARE
→ RECONCILE
→ MAP
→ MERGE USEFUL CONTENT
→ PRESERVE PROVENANCE
→ RETIRE OR CLASSIFY THE DUPLICATE.

Repository preservation must not create duplicate sources of truth.

======================================================================
9 — COMMIT BOUNDARY MUST BE INTENTIONAL
======================================================================

Before committing, review the exact diff.

Verify:

- every intended file belongs;
- no unrelated changes are included;
- no secrets are included;
- no accidental formatting explosion exists;
- no generated noise exists;
- no future-stage implementation slipped in;
- no duplicate system was created;
- no requirement was silently changed;
- no architecture drift occurred;
- no test was weakened merely to obtain a pass.

Commits must represent understandable engineering changes.

======================================================================
10 — USE THE EXISTING CANONICAL COMMIT POLICY
======================================================================

Do NOT invent a competing commit/checkpoint workflow.

Inspect existing rules such as:

- DEC-032;
- DEC-033;
- branch policy;
- review policy;
- checkpoint policy;
- Gate 3 requirements;
- temporary-backup policy;
- stage-exit policy.

If the project already defines how pre-verification work is preserved:

FOLLOW IT.

If official commits are prohibited before a certain verification gate,
do not bypass that rule.

Instead use the already authorized temporary/candidate checkpoint
mechanism if one exists.

If no compliant preservation mechanism exists and substantial work is
at risk:

identify the governance gap and request the exact owner decision needed.

======================================================================
11 — CANDIDATE CHECKPOINT VS VERIFIED CHECKPOINT
======================================================================

Where canonical policy permits, distinguish:

CANDIDATE / UNVERIFIED CHECKPOINT

from

VERIFIED / AUTHORITATIVE STAGE CHECKPOINT.

A candidate checkpoint may preserve work safely.

It must remain explicitly:

UNVERIFIED
NOT APPROVED
NOT FOR PRODUCTION
NOT A STAGE-COMPLETION CLAIM.

A verified checkpoint may only be created after the required verification
conditions are satisfied.

Do not confuse durability with verification.

======================================================================
12 — GATE 3 MUST REVIEW A KNOWN REPOSITORY STATE
======================================================================

Gate 3 should evaluate a clearly identifiable repository state.

Where possible, verification evidence must map to:

BRANCH
+
COMMIT / CHECKPOINT
+
CONFIGURATION
+
TEST STATE
+
REVIEW STATE.

Do not allow Gate 3 to review one state while substantial unrelated
uncommitted changes exist beside it.

If material changes are made after Gate 3 starts:

determine whether the reviewed state has changed materially.

If yes:

perform the required revalidation.

======================================================================
13 — GATE 3 FINDINGS MUST BE PERSISTED
======================================================================

A Gate 3 finding must not exist only inside Claude's response.

Material findings must be recorded in the canonical project mechanism.

For each finding preserve where appropriate:

- stable finding ID;
- description;
- classification;
- severity;
- affected requirement;
- affected component;
- evidence;
- root cause;
- remediation;
- verification;
- closure status.

Do not lose review knowledge between sessions.

======================================================================
14 — CORRECTIONS FOUND DURING GATE 3 MUST BE COMMITTED
======================================================================

If Gate 3 identifies legitimate defects and corrections are made:

do not leave those corrections only in the working tree.

Follow:

FINDING
→ FIX
→ TEST
→ IMPACT ANALYSIS
→ REQUIRED REVALIDATION
→ TRACEABILITY UPDATE
→ COMMIT / CHECKPOINT ACCORDING TO POLICY.

If the fix changes the repository state materially:

ensure verification evidence points to the new state.

======================================================================
15 — PRE-STAGE-EXIT CLEAN WORKTREE REQUIREMENT
======================================================================

Before transitioning to the next stage, the normal expected state is:

NO MATERIAL UNSTAGED CHANGES.
NO MATERIAL STAGED-BUT-UNCOMMITTED CHANGES.
NO MATERIAL UNTRACKED FILES.
NO UNKNOWN LOCAL MODIFICATIONS.
NO FORGOTTEN IMPORTANT DRAFTS.
NO UNRESOLVED TEMPORARY IMPLEMENTATIONS.
NO UNRECONCILED BACKUP WORK.
NO REQUIRED ARTIFACTS EXISTING ONLY LOCALLY.

Exceptions must be explicitly justified by canonical policy.

A clean worktree alone is NOT proof of completeness.

But a dirty worktree containing unexplained material work BLOCKS
stage transition.

======================================================================
16 — REMOTE DURABILITY CHECK
======================================================================

A local commit is not sufficient if canonical policy requires durable
remote preservation.

Before stage exit verify, where applicable:

LOCAL VERIFIED CHECKPOINT
→ PUSH
→ REMOTE BRANCH / CHECKPOINT EXISTS
→ EXPECTED COMMIT ID MATCHES
→ REQUIRED CI / REMOTE CHECKS RUN
→ REMOTE STATE CONFIRMED.

Do not assume a push succeeded.

Verify it.

======================================================================
17 — NO LOCAL-ONLY AUTHORITATIVE STATE
======================================================================

Authoritative stage completion must not depend on one:

- container;
- laptop;
- local clone;
- temporary workspace;
- Claude session.

The stage's durable state must be recoverable from approved persistent
systems.

This project must survive loss of the current development environment.

======================================================================
18 — COMMIT TRACEABILITY
======================================================================

Important commits/checkpoints should be traceable where practical to:

- stage;
- requirement;
- ADR;
- finding;
- issue;
- verification activity;
- migration;
- security correction;
- architecture change.

Do not overload commit messages with unnecessary data.

But meaningful project changes should not become historically opaque.

======================================================================
19 — REQUIREMENT-TO-COMMIT TRACEABILITY
======================================================================

Where appropriate support:

REQUIREMENT
→ IMPLEMENTATION
→ TEST
→ VERIFICATION
→ COMMIT / CHECKPOINT.

And reverse:

COMMIT
→ CHANGE PURPOSE
→ REQUIREMENT / FINDING
→ TEST
→ VERIFICATION.

This supports future audits and safe maintenance.

======================================================================
20 — DO NOT COMMIT UNAUTHORIZED SCOPE
======================================================================

A change being technically valid does not automatically mean it belongs
in the current stage.

Before including it in the Foundation checkpoint, determine whether it is:

FOUNDATION SCOPE
or
FUTURE-STAGE WORK.

Future-stage work must not silently enter Foundation.

Preserve it according to governance, but do not use stage completion as
an excuse for premature implementation.

======================================================================
21 — NO HIDDEN CHANGES INSIDE LARGE COMMITS
======================================================================

Large commits require additional review discipline.

Check for:

- unrelated refactors;
- changed thresholds;
- changed ownership;
- changed requirements;
- new dependencies;
- deleted safeguards;
- new external calls;
- configuration changes;
- schema changes;
- security changes;
- future-stage code.

Do not hide architectural changes inside a "Foundation fixes" commit.

======================================================================
22 — STAGE EXIT MUST REFERENCE EXACT VERIFIED STATE
======================================================================

The final Foundation completion record must identify the exact verified
repository state.

Record where canonical policy permits:

- branch;
- commit SHA / checkpoint ID;
- verification results;
- Gate 1 result;
- Gate 2 result;
- Gate 3 result;
- independent review result;
- mutation result where applicable;
- known non-blocking findings;
- deferred work;
- unresolved but non-blocking items;
- stage exit decision.

A future engineer must be able to identify exactly what was certified as
Foundation-complete.

======================================================================
23 — FINAL COMMIT COMPLETENESS AUDIT
======================================================================

Before Foundation exit, compare:

APPROVED FOUNDATION REQUIREMENTS

against

FINAL COMMITTED REPOSITORY STATE.

Confirm:

1. Every required Foundation artifact exists.
2. Every required implementation is committed.
3. Every required test is committed.
4. Every required document is committed.
5. Every required decision is preserved.
6. Every required traceability update is preserved.
7. Every Gate 3 correction is preserved.
8. Every required verification artifact is preserved or referenced.
9. No valid work remains only locally.
10. No duplicate authoritative material was introduced.
11. No conflicting material remains unresolved.
12. No important draft is forgotten.
13. No future-stage implementation was accidentally included.
14. No secret or inappropriate artifact was committed.
15. No required change is missing from the final checkpoint.

If ANY material item is missing:

DO NOT EXIT FOUNDATION.

======================================================================
24 — FINAL DRAFT AUDIT
======================================================================

Before stage transition, search specifically for draft indicators such as:

DRAFT
TODO
TBD
WIP
PLACEHOLDER
TEMP
PROVISIONAL
UNVERIFIED
PENDING
OPEN QUESTION
REQUIRES DECISION.

Do not automatically remove them.

Classify each occurrence.

Determine whether it is:

VALID INTENTIONAL DRAFT
BLOCKING INCOMPLETE WORK
FUTURE WORK
NON-BLOCKING DOCUMENTATION
TEMPORARY ARTIFACT
STALE TEXT
UNRESOLVED OWNER DECISION.

Every material draft must have a known disposition.

======================================================================
25 — NO PLACEHOLDER COMPLETION
======================================================================

Do not declare a stage complete if required implementation contains:

- placeholder logic;
- fake success responses;
- stubbed production behavior;
- unimplemented required methods;
- disabled mandatory checks;
- TODOs representing blocking functionality;
- incomplete migrations;
- incomplete required tests.

A placeholder may only remain if:

- it is intentionally outside current scope;
- correctly classified;
- cannot be mistaken for implemented behavior;
- tracked in the appropriate future stage.

======================================================================
26 — SESSION-END PERSISTENCE
======================================================================

Before ending a substantial session, determine whether material work is
still uncommitted.

If yes:

either preserve it according to the canonical safe-checkpoint policy

or

explicitly record why it remains uncommitted and how it will be recovered.

Do not allow substantial work to become dependent on an active Claude
session.

======================================================================
27 — RECOVERY TEST
======================================================================

Before Foundation exit, assume:

THE CURRENT CONTAINER IS DESTROYED NOW.

Then ask:

Can the complete intended Foundation state be recovered from the
repository and approved persistent systems?

If NO:

Foundation persistence is incomplete.

Fix it before transition.

======================================================================
28 — NEXT-STAGE TRANSITION GATE
======================================================================

The next stage may begin only when all applicable conditions are true:

FOUNDATION REQUIREMENTS SATISFIED
+
GATE 1 PASS
+
GATE 2 PASS
+
GATE 3 PASS
+
REQUIRED INDEPENDENT REVIEW PASS
+
REQUIRED MUTATION TESTING PASS
+
REPOSITORY COMPLETENESS PASS
+
TRACEABILITY PASS
+
DOCUMENTATION PASS
+
FINAL DIFF REVIEW PASS
+
COMMIT COMPLETENESS PASS
+
TEMPORARY BACKUPS RECONCILED
+
NO MATERIAL UNCOMMITTED WORK
+
NO MATERIAL UNTRACKED WORK
+
VERIFIED CHECKPOINT CREATED
+
REMOTE DURABILITY CONFIRMED WHERE REQUIRED
+
CURRENT STAGE STATUS RECORDED
+
NEXT AUTHORIZED STAGE IDENTIFIED.

Do NOT proceed merely because the code appears to work.

======================================================================
29 — BLOCK THE TRANSITION IF IMPORTANT WORK IS UNSAVED
======================================================================

The following are stage-transition blockers:

MATERIAL UNCOMMITTED SOURCE CODE
MATERIAL UNCOMMITTED TESTS
MATERIAL UNCOMMITTED REQUIREMENTS
MATERIAL UNCOMMITTED ADRs
MATERIAL UNCOMMITTED GOVERNANCE CHANGES
MATERIAL UNCOMMITTED TRACEABILITY
MATERIAL UNCOMMITTED GATE FIXES
MATERIAL UNTRACKED PROJECT FILES
UNKNOWN LOCAL MODIFICATIONS
FORGOTTEN DRAFTS WITH MATERIAL CONTENT
UNRECONCILED TEMPORARY BACKUPS
UNPRESERVED OWNER DECISIONS
UNPRESERVED VERIFICATION EVIDENCE
REQUIRED WORK EXISTING ONLY IN THE CONTAINER.

Resolve them before stage transition.

======================================================================
30 — FINAL REPORT REQUIRED
======================================================================

Before moving to the next stage provide an evidence-based report:

A. Current branch.

B. Final candidate/verified commit SHA.

C. Git working-tree status.

D. Staged changes remaining.

E. Unstaged changes remaining.

F. Material untracked files remaining.

G. Draft documents discovered.

H. Disposition of every material draft.

I. Temporary backups/checkpoints discovered.

J. Their final disposition.

K. Gate 3 changes made.

L. Confirmation that all Gate 3 fixes are preserved.

M. Required Foundation artifacts checked.

N. Missing artifacts discovered.

O. Duplicate/conflicting artifacts discovered.

P. Secrets / inappropriate files check.

Q. Traceability completeness.

R. Verification evidence mapping to exact commit.

S. Remote push/durability status where applicable.

T. Remaining blockers.

U. Remaining non-blocking future work.

V. Exact next authorized stage.

Do not state READY TO PROCEED unless the evidence supports it.

======================================================================
31 — ABSOLUTE FINAL RULE
======================================================================

NO IMPORTANT PROJECT WORK MAY BE LEFT BEHIND.

NO IMPORTANT PROJECT WORK MAY EXIST ONLY IN CLAUDE MEMORY.

NO IMPORTANT PROJECT WORK MAY EXIST ONLY IN THE CONTAINER.

NO IMPORTANT VALID WORK MAY REMAIN FORGOTTEN AS UNCOMMITTED.

NO IMPORTANT DRAFT MAY REMAIN WITHOUT A DISPOSITION.

NO VALID GATE-3 FIX MAY BE LOST.

NO MATERIAL FILE MAY REMAIN UNTRACKED WITHOUT EXPLANATION.

NO TEMPORARY BACKUP MAY REMAIN UNRECONCILED.

NO DUPLICATE SOURCE OF TRUTH MAY BE CREATED JUST TO SAVE WORK.

NO SECRET MAY BE COMMITTED.

NO FUTURE-STAGE WORK MAY BE SILENTLY PROMOTED.

NO COMMIT MAY BE TREATED AS APPROVAL BY ITSELF.

NO STAGE MAY BE TREATED AS VERIFIED ONLY BECAUSE IT WAS COMMITTED.

NO NEXT STAGE UNTIL THE CURRENT STAGE HAS A COMPLETE,
TRACEABLE, VERIFIED, DURABLY PRESERVED REPOSITORY STATE.

======================================================================
MANDATORY FINAL SEQUENCE
======================================================================

INSPECT REPOSITORY
→ INVENTORY ALL CHANGES
→ CLASSIFY EVERY MATERIAL CHANGE
→ INVESTIGATE UNKNOWN CHANGES
→ RECONCILE DRAFTS
→ RECONCILE DUPLICATES
→ RESOLVE CONFLICTS
→ PRESERVE VALID WORK
→ EXCLUDE SECRETS / NOISE
→ REVIEW DIFF
→ TEST
→ GATE 1
→ GATE 2
→ GATE 3
→ FIX REAL BLOCKERS
→ REVALIDATE
→ UPDATE TRACEABILITY
→ UPDATE DOCUMENTATION
→ FINAL REPOSITORY COMPLETENESS AUDIT
→ FINAL DRAFT AUDIT
→ FINAL DIFF AUDIT
→ COMMIT ACCORDING TO CANONICAL POLICY
→ VERIFY EXACT COMMIT
→ PUSH / DURABLY PRESERVE WHERE REQUIRED
→ VERIFY REMOTE STATE
→ RECONCILE TEMPORARY BACKUPS
→ CONFIRM CLEAN / EXPLAINED WORKTREE
→ RECORD STAGE EXIT
→ CHECKPOINT PROJECT STATE
→ ONLY THEN PROCEED TO THE NEXT AUTHORIZED STAGE.

======================================================================
FINAL PRINCIPLE
======================================================================

DO NOT RUSH TO THE NEXT STAGE.

DO NOT LEAVE VALID WORK BEHIND.

DO NOT BLINDLY COMMIT EVERYTHING.

DO NOT LOSE DRAFTS THAT MATTER.

DO NOT PROMOTE DRAFTS TO APPROVED BY ACCIDENT.

DO NOT CONFUSE VERSION CONTROL WITH VERIFICATION.

DO NOT CONFUSE VERIFICATION WITH APPROVAL.

THE REQUIRED COMPANY-GRADE STANDARD IS:

EVERY MATERIAL CHANGE
KNOWN
→ CLASSIFIED
→ RECONCILED
→ CORRECTLY LOCATED
→ TRACEABLE
→ TESTED WHERE REQUIRED
→ VERIFIED WHERE REQUIRED
→ COMMITTED ACCORDING TO POLICY
→ DURABLY PRESERVED
→ RECOVERABLE
→ ACCOUNTED FOR BEFORE STAGE TRANSITION.
======================================================================
```
