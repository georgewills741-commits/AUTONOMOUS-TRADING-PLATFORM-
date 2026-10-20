# Owner Decisions 17 — Rule 0: reuse, reinforce, and enhance existing canonical controls; continuing until the work is done

> **Status:** HISTORICAL — source input: two messages of the owner of 2026-10-19, sent during Stage 1 while the change that preserves owner decisions 14 to 16 was in its Gate 3 runs. The first sets "RULE 0": before any rule, mechanism, process, document, workflow, checkpoint, verification control, recovery or continuation process, anti-loop control, or root-cause procedure is created "from this instruction", the canonical repository is inspected; where an equivalent or overlapping canonical mechanism exists, no other is created: the existing one is inspected, its authority verified, compared with the requirement and its real gaps identified, then reinforced, and enhanced where justified. Its sections cover the existing rule first; remembered knowledge, which is not authority: before it is relied on, it is verified against the repository, the authoritative evidence; enhancement without drift; no expansion of scope "while I am here"; the root, not only the symptom; evidence; not weakening existing controls; the whole related mechanism, from rule to operational behavior; no duplicate enhancements; provenance; when the owner is asked and when not; and continuous improvement without continuous drift. Its final principle states "THE OBJECTIVE IS NOT MORE RULES." and "THE OBJECTIVE IS A STRONGER EXISTING SYSTEM.", and closes with "NEVER DUPLICATE. NEVER SILENTLY OVERRIDE. NEVER DRIFT." The second, sent while the sixth Gate 3 run of that change was pending, asks the builder to continue and not to stop until everything is done or the usage limits run out, and says the builder can ask questions when needed or necessary. This is **not** an active source of truth. It is preserved by [DEC-048](../decisions/DEC-048-preserve-and-apply-rule-0.md), which applies it.
>
> **Formatting note:** each message is reproduced inside one text block exactly as received, so that its lines, separator lines, lists, and arrows stay as they were sent. Nothing was added, removed, or changed in them. The title, this banner, and the two headings are the builder's.

## The owner's message of 2026-10-19, 19:28 UTC

```text
======================================================================
RULE 0 — REUSE, REINFORCE & ENHANCE EXISTING CANONICAL CONTROLS
======================================================================

Before creating, adding, or introducing ANY rule, mechanism, process,
document, workflow, checkpoint, verification control, recovery process,
continuation process, anti-loop control, or root-cause procedure from
this instruction:

FIRST INSPECT THE CANONICAL REPOSITORY.

Determine whether the project already contains the same or substantially
equivalent capability.

The project may already have:

- continuation rules;
- session-recovery rules;
- checkpoint rules;
- state-recovery mechanisms;
- root-cause procedures;
- anti-loop controls;
- convergence rules;
- verification rules;
- issue/finding lifecycle rules;
- stage-transition rules;
- repository-integrity rules;
- traceability rules;
- backup/recovery rules;
- governance processes;
- testing procedures;
- change-impact rules;
- remediation procedures;
- consistency controls.

IF AN EQUIVALENT OR OVERLAPPING CANONICAL MECHANISM ALREADY EXISTS:

DO NOT CREATE ANOTHER ONE.

Instead:

INSPECT IT
→ VERIFY ITS AUTHORITY
→ COMPARE IT WITH THIS REQUIREMENT
→ IDENTIFY ANY REAL GAPS
→ REINFORCE THE EXISTING MECHANISM
→ ENHANCE IT WHERE JUSTIFIED
→ IMPROVE ITS IMPLEMENTATION WHERE NECESSARY
→ IMPROVE ITS TESTING WHERE NECESSARY
→ IMPROVE ITS TRACEABILITY WHERE NECESSARY
→ IMPROVE ITS DOCUMENTATION WHERE NECESSARY
→ VERIFY THE ENHANCED RESULT.

The goal is NOT to create more rules.

The goal is to make the existing canonical system stronger.

======================================================================
EXISTING RULE FIRST
======================================================================

When an existing rule already correctly covers the requirement:

APPLY IT.

Do not rewrite it merely to make it look new.

When an existing rule is correct but weakly enforced:

STRENGTHEN ITS ENFORCEMENT.

When an existing rule is correct but poorly tested:

STRENGTHEN ITS TEST COVERAGE.

When an existing rule is correct but poorly documented:

IMPROVE THE CANONICAL DOCUMENTATION.

When an existing rule is correct but poorly traceable:

IMPROVE TRACEABILITY.

When an existing rule is partially complete:

REFINE THE EXISTING CANONICAL RULE.

When an existing implementation is incomplete:

COMPLETE OR CORRECT THE EXISTING IMPLEMENTATION.

When multiple overlapping rules exist:

RECONCILE THEM INTO THE PROPER CANONICAL SOURCE.

DO NOT CREATE A THIRD VERSION.

======================================================================
KNOWLEDGE IS NOT AUTHORITY
======================================================================

If Claude Code already "knows" or remembers a rule from:

- a previous session;
- conversation context;
- prior reasoning;
- previous implementation work;
- earlier instructions;

that knowledge may help locate the relevant repository evidence.

However:

CLAUDE MEMORY IS NOT THE CANONICAL SOURCE OF TRUTH.

Before relying on remembered project knowledge:

VERIFY IT AGAINST THE REPOSITORY.

Use:

REPOSITORY
→ REQUIREMENTS
→ ADRs
→ SYSTEM RULES
→ GOVERNANCE
→ ARCHITECTURE
→ TRACEABILITY
→ CURRENT IMPLEMENTATION

as the authoritative evidence.

If Claude's memory conflicts with repository truth:

DO NOT silently trust memory.

Investigate the discrepancy.

======================================================================
ENHANCEMENT IS ENCOURAGED — DRIFT IS NOT
======================================================================

Claude Code is encouraged to improve existing mechanisms when objective
evidence shows that they can be made:

- clearer;
- safer;
- more reliable;
- more maintainable;
- more testable;
- more traceable;
- more deterministic;
- more efficient;
- more recoverable;
- less repetitive;
- less error-prone;
- more robust against future sessions and failures.

However, enhancement must NOT become an excuse for architectural drift.

Every enhancement must preserve:

- approved project intent;
- canonical ownership;
- authority boundaries;
- stage boundaries;
- security requirements;
- risk requirements;
- capital authority;
- execution authority;
- AI boundaries;
- verification requirements;
- traceability;
- repository organization;
- approved lifecycle rules.

======================================================================
NO "WHILE I AM HERE" EXPANSION
======================================================================

Do not turn a legitimate enhancement into uncontrolled scope expansion.

For every proposed enhancement determine:

IS IT REQUIRED TO FIX THE CURRENT PROBLEM?

IS IT REQUIRED TO PREVENT THE PROBLEM FROM RECURRING?

IS IT A SAFE REFINEMENT OF AN EXISTING APPROVED MECHANISM?

OR

IS IT ACTUALLY A NEW FEATURE / ARCHITECTURAL CHANGE / FUTURE CAPABILITY?

If it is genuinely new or materially changes approved architecture,
authority, requirements, risk, security, scope, or lifecycle:

DO NOT silently implement it.

Classify it according to canonical governance and obtain owner approval
when required.

======================================================================
ENHANCE THE ROOT, NOT ONLY THE SYMPTOM
======================================================================

When a recurring problem reveals weakness in an existing canonical
mechanism, Claude Code should not merely repair the latest occurrence.

Where justified:

IMPROVE THE ROOT MECHANISM.

For example:

weak session continuity
→ strengthen canonical continuity mechanism;

recurring duplicate findings
→ strengthen finding identity/deduplication;

repeated unnecessary verification reruns
→ strengthen impact-based revalidation;

lost or forgotten work
→ strengthen checkpoint/persistence controls;

repeated configuration inconsistency
→ strengthen canonical configuration ownership/validation;

repeated traceability gaps
→ strengthen existing traceability mechanism.

The improvement should prevent the entire CLASS of problem from recurring
where technically practical.

======================================================================
ENHANCEMENT MUST BE EVIDENCE-BASED
======================================================================

Do not enhance systems merely because a different design is personally
preferred.

An enhancement should have a justified reason such as:

- recurring defect;
- demonstrated gap;
- insufficient enforcement;
- missing validation;
- weak test coverage;
- incomplete traceability;
- recovery weakness;
- maintainability problem;
- performance evidence;
- security evidence;
- architectural inconsistency;
- verified operational risk.

Record material reasons where appropriate.

======================================================================
DO NOT WEAKEN EXISTING CONTROLS DURING ENHANCEMENT
======================================================================

An enhancement must not silently:

- remove verification;
- weaken tests;
- reduce security;
- reduce auditability;
- reduce traceability;
- bypass governance;
- change authority;
- change owner decisions;
- relax risk controls;
- weaken deterministic safeguards;
- introduce hidden state;
- introduce duplicate sources of truth.

"Improvement" must genuinely improve the system.

======================================================================
CHECK THE WHOLE RELATED MECHANISM
======================================================================

When strengthening an existing control, inspect its related chain:

RULE
→ OWNER
→ ARCHITECTURE
→ IMPLEMENTATION
→ CONFIGURATION
→ TEST
→ VERIFICATION
→ TRACEABILITY
→ DOCUMENTATION
→ OPERATIONAL BEHAVIOR.

Do not improve one layer while leaving the other layers inconsistent.

Example:

If documentation is strengthened but implementation still behaves
differently:

THE WORK IS NOT COMPLETE.

If implementation is corrected but tests still encode the old behavior:

THE WORK IS NOT COMPLETE.

If tests are corrected but canonical requirements remain inconsistent:

THE WORK IS NOT COMPLETE.

======================================================================
NO DUPLICATE ENHANCEMENTS
======================================================================

Before adding a proposed enhancement:

SEARCH THE REPOSITORY.

Determine whether:

- it already exists;
- it is already being implemented;
- another system already owns it;
- an open issue already tracks it;
- a future roadmap stage already contains it;
- an ADR already decided it.

If yes:

MAP TO THE EXISTING ITEM.

Do not create another one.

======================================================================
PRESERVE PROVENANCE
======================================================================

If an existing mechanism is enhanced, preserve traceability showing:

ORIGINAL CANONICAL MECHANISM
→ IDENTIFIED GAP
→ REASON FOR ENHANCEMENT
→ CHANGE
→ AFFECTED COMPONENTS
→ TESTS
→ VERIFICATION
→ RESULT.

Do not make significant improvements historically invisible.

======================================================================
NO UNNECESSARY OWNER INTERRUPTION
======================================================================

If an enhancement:

- preserves approved intent;
- stays within existing authority;
- does not change material scope;
- does not change system ownership;
- does not change risk/security policy;
- does not alter approved architecture materially;
- and is clearly authorized by existing engineering rules;

Claude Code may perform the engineering improvement autonomously.

Do not repeatedly ask the owner for routine engineering corrections.

However, if enhancement requires:

- new requirement;
- material architecture change;
- authority reassignment;
- material security-policy change;
- risk-policy change;
- scope expansion;
- roadmap change requiring approval;
- new production capability;
- unresolved conflict between canonical authorities;

STOP AND REQUEST THE REQUIRED OWNER DECISION.

======================================================================
CONTINUOUS IMPROVEMENT WITHOUT CONTINUOUS DRIFT
======================================================================

The project is expected to improve over time.

Claude Code is not required to preserve weak implementation merely
because it already exists.

But improvement must happen through controlled evolution.

The required model is:

EXISTING CANONICAL SYSTEM
→ INSPECT
→ VERIFY
→ IDENTIFY REAL WEAKNESS
→ TRACE TO ROOT CAUSE
→ DESIGN COMPATIBLE IMPROVEMENT
→ CHECK DUPLICATES
→ CHECK CONFLICTS
→ CHECK AUTHORITY
→ CHECK SCOPE
→ IMPLEMENT
→ TEST
→ VERIFY
→ UPDATE TRACEABILITY
→ PRESERVE RESULT.

NOT:

EXISTING SYSTEM
→ CLAUDE PREFERS ANOTHER DESIGN
→ CREATE PARALLEL SYSTEM
→ LEAVE BOTH
→ CREATE FUTURE CONFLICT.

======================================================================
FINAL REINFORCEMENT PRINCIPLE
======================================================================

IF THE PROJECT ALREADY HAS THE RULE:

FOLLOW IT.

IF THE PROJECT ALREADY HAS THE CONTROL:

USE IT.

IF IT IS WEAK:

STRENGTHEN IT.

IF IT IS INCOMPLETE:

COMPLETE IT.

IF IT IS CORRECT BUT POORLY TESTED:

TEST IT BETTER.

IF IT IS CORRECT BUT POORLY ENFORCED:

ENFORCE IT BETTER.

IF IT IS CORRECT BUT POORLY TRACEABLE:

IMPROVE TRACEABILITY.

IF IT IS DUPLICATED:

RECONCILE IT.

IF IT CONFLICTS:

RESOLVE IT THROUGH CANONICAL AUTHORITY.

IF IT IS OBSOLETE:

FOLLOW THE PROPER SUPERSESSION PROCESS.

IF IT IS GENUINELY MISSING:

ADD IT THROUGH THE EXISTING GOVERNANCE PROCESS.

IF CLAUDE ONLY REMEMBERS IT:

VERIFY IT IN THE REPOSITORY FIRST.

IF AN IMPROVEMENT REQUIRES OWNER AUTHORITY:

STOP AND ASK.

THE OBJECTIVE IS NOT MORE RULES.

THE OBJECTIVE IS A STRONGER EXISTING SYSTEM.

REUSE.
REINFORCE.
ENHANCE.
VERIFY.
PRESERVE.

NEVER DUPLICATE.
NEVER SILENTLY OVERRIDE.
NEVER DRIFT.
======================================================================
```

## The owner's message of 2026-10-19, 19:49 UTC

```text
Continue from where you left off.and dont stop until everything is done or you run out limits you can ask questions when is needed or necessary
```
