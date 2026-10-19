# Owner Decisions 14 — Company-grade project order, traceability, auditability, and engineering control rules

> **Status:** HISTORICAL — source input: the owner's message of 2026-10-14, sent during Stage 1 after the Foundation convergence audit was committed (`bec1680`) and reported. It sets mandatory, permanent, project-wide rules for the order of the repository and the project (its STATUS lines): everything material has a purpose, an owner, a canonical location, a status, a history, a dependency context, a verification path, and a traceability path; for important functionality, traceability runs end to end, from the owner's intent to operation, and back where appropriate (its §2); the existing traceability mechanism is reinforced, never duplicated (its §31); material state is preserved through the canonical repository, configuration, storage, or operational systems, not only in memory, private scratchpads, temporary scripts, or transient container state (its §27); and, before Foundation exits, a company-grade order audit is reported in 22 items (its §40). This is **not** an active source of truth. It is preserved by [DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md), which records how it is applied until its adoption as a builder text is decided.
>
> **Formatting note:** the message is reproduced inside one text block exactly as received, so that its lines, separator lines, lists, and arrows stay as they were sent. Nothing was added, removed, or changed in it. The title and this banner are the builder's.

```text
======================================================================
COMPANY-GRADE PROJECT ORDER, TRACEABILITY, AUDITABILITY
& ENGINEERING CONTROL RULES
======================================================================

STATUS:
MANDATORY
PERMANENT
PROJECT-WIDE
COMPANY-GRADE ENGINEERING STANDARD

PURPOSE:

The project must not merely contain files and code.

It must operate as a professionally governed engineering system where
important information can be traced, verified, reviewed, maintained,
recovered, audited, and understood by future qualified engineers.

Everything material must have:

A PURPOSE
AN OWNER
A CANONICAL LOCATION
A STATUS
A HISTORY
A DEPENDENCY CONTEXT
A VERIFICATION PATH
A TRACEABILITY PATH

The repository must remain orderly as the company and platform grow.

======================================================================
1 — COMPANY-GRADE ORDER
======================================================================

The repository must have a clear and intentional structure.

Every material artifact must belong somewhere for a reason.

Do not allow the repository to become a collection of unrelated files.

For each major artifact determine:

- what it is;
- why it exists;
- who owns it;
- where it belongs;
- whether it is authoritative;
- what depends on it;
- what it depends on;
- how it is verified;
- what lifecycle governs it.

Avoid:

- random files;
- unexplained folders;
- overlapping specifications;
- abandoned drafts;
- unclear naming;
- temporary artifacts becoming permanent accidentally;
- documentation scattered without ownership;
- implementation disconnected from specifications.

======================================================================
2 — TRACEABILITY MUST BE END-TO-END
======================================================================

For important functionality, traceability should support:

OWNER INTENT
→ DECISION
→ REQUIREMENT
→ ARCHITECTURE
→ SYSTEM / MODULE
→ IMPLEMENTATION
→ CONFIGURATION
→ TEST
→ VERIFICATION
→ RELEASE / CHECKPOINT
→ OPERATIONAL STATUS.

Where appropriate, reverse traceability must also be possible:

CODE
→ SYSTEM OWNER
→ REQUIREMENT
→ DECISION
→ TEST
→ VERIFICATION EVIDENCE.

A future engineer must be able to answer:

WHY DOES THIS EXIST?

WHO AUTHORIZED IT?

WHERE IS THE REQUIREMENT?

WHAT IMPLEMENTS IT?

WHAT TESTS IT?

WHAT VERIFIED IT?

WHAT VERSION INTRODUCED IT?

WHAT DEPENDS ON IT?

======================================================================
3 — EVERY MATERIAL REQUIREMENT MUST BE TRACEABLE
======================================================================

Each approved requirement should have, where applicable:

- stable ID;
- title;
- description;
- classification;
- status;
- provenance;
- owner;
- canonical source;
- dependencies;
- implementation mapping;
- test mapping;
- verification mapping;
- roadmap stage;
- related ADRs;
- supersession history where relevant.

Do not create IDs merely for appearance.

Use IDs where they provide durable traceability.

======================================================================
4 — EVERY MATERIAL DECISION MUST BE TRACEABLE
======================================================================

Important decisions must record:

- decision ID where applicable;
- problem;
- context;
- options considered;
- chosen decision;
- reason;
- owner / approver;
- consequences;
- affected systems;
- affected requirements;
- effective status;
- superseded decisions where relevant.

Do not rewrite history when a decision changes.

Record:

OLD DECISION
→ SUPERSEDED BY
→ NEW DECISION.

======================================================================
5 — CLEAR OWNERSHIP
======================================================================

Every major system must have clear ownership.

Examples:

- requirements ownership;
- architecture ownership;
- risk ownership;
- capital authority;
- execution ownership;
- security ownership;
- AI authority;
- data ownership;
- strategy ownership;
- testing ownership;
- operations ownership;
- recovery ownership;
- deployment ownership.

Avoid:

- shared authority with no final owner;
- two systems controlling the same responsibility;
- hidden authority inside utility code;
- reviewers becoming runtime authorities;
- AI becoming authority merely because it recommends something.

One responsibility should have one clear authoritative owner.

======================================================================
6 — AUTHORITATIVE VS REFERENCE DOCUMENTS
======================================================================

Every important document must clearly be one of:

AUTHORITATIVE
REFERENCE
GENERATED
HISTORICAL
SUPERSEDED
DRAFT
PROPOSAL
ARCHIVED.

Do not let future engineers guess which document is authoritative.

If one document is canonical:

other documents should reference it rather than restating its authority.

======================================================================
7 — STATUS MUST BE EXPLICIT
======================================================================

Important work must have explicit status.

Possible statuses may include:

PROPOSED
DRAFT
APPROVED
IMPLEMENTING
IMPLEMENTED
TESTING
VERIFICATION
BLOCKED
VERIFIED
RELEASED
ACTIVE
DEGRADED
SUSPENDED
DEPRECATED
SUPERSEDED
RETIRED.

Use the project's existing canonical lifecycle where one already exists.

Do not create a duplicate lifecycle.

Do not use ambiguous language such as:

"basically finished"
"almost ready"
"looks complete."

======================================================================
8 — CHANGE CONTROL
======================================================================

Every material change must answer:

WHAT CHANGED?
WHY?
WHO AUTHORIZED IT?
WHAT REQUIREMENT DOES IT AFFECT?
WHAT SYSTEM DOES IT AFFECT?
WHAT COULD BREAK?
WHAT MUST BE RETESTED?
WHAT DOCUMENTATION MUST CHANGE?
WHAT TRACEABILITY MUST CHANGE?
DOES MIGRATION APPLY?
DOES ROLLBACK APPLY?

No material change should appear mysteriously in the repository.

======================================================================
9 — CHANGE IMPACT ANALYSIS
======================================================================

Before material modifications, evaluate impact across:

- requirements;
- architecture;
- interfaces;
- schemas;
- APIs;
- dependencies;
- security;
- risk;
- capital;
- execution;
- AI;
- data;
- performance;
- testing;
- deployment;
- monitoring;
- recovery;
- operations;
- documentation;
- migration;
- backward compatibility.

Record significant impact where appropriate.

======================================================================
10 — VERSION AND HISTORY INTEGRITY
======================================================================

The repository must preserve meaningful evolution.

Do not silently overwrite architectural history.

Do not silently replace approved requirements.

Do not erase why major decisions changed.

Preserve meaningful relationships such as:

SUPERSEDES
SUPERSEDED BY
REPLACES
MIGRATED FROM
MIGRATED TO
DERIVED FROM
IMPLEMENTS
VERIFIES
DEPENDS ON.

======================================================================
11 — COMMIT QUALITY
======================================================================

Commits must represent understandable project changes.

Where the canonical workflow permits it:

- group logically related changes;
- avoid mixing unrelated work;
- use meaningful commit messages;
- reference relevant issue, requirement, decision, stage, or finding
  where useful;
- avoid committing accidental files;
- verify repository state before checkpointing.

Do not use commits as dumping grounds.

A future engineer should be able to understand why a meaningful commit
exists.

======================================================================
12 — ISSUE AND FINDING TRACEABILITY
======================================================================

Material issues and verification findings should be traceable through:

OPEN
→ INVESTIGATED
→ ROOT CAUSE IDENTIFIED
→ FIX PLANNED
→ FIX IMPLEMENTED
→ TESTED
→ REVERIFIED
→ CLOSED.

If reopened:

REOPENED
→ REASON
→ NEW EVIDENCE
→ NEW RESOLUTION.

Do not silently delete unresolved findings.

======================================================================
13 — ROOT-CAUSE DISCIPLINE
======================================================================

For recurring or serious defects, do not only patch symptoms.

Determine where appropriate:

SYMPTOM
→ ROOT CAUSE
→ CONTRIBUTING FACTORS
→ AFFECTED SYSTEMS
→ CORRECTIVE ACTION
→ PREVENTIVE ACTION
→ VERIFICATION.

Company-grade engineering should reduce recurrence, not repeatedly repair
the same class of defect.

======================================================================
14 — DEPENDENCY TRACEABILITY
======================================================================

Important dependencies must be understandable.

For major components preserve:

- upstream dependencies;
- downstream dependents;
- external services;
- internal APIs;
- data dependencies;
- configuration dependencies;
- runtime dependencies;
- deployment dependencies.

This should support safe change analysis.

======================================================================
15 — INTERFACE TRACEABILITY
======================================================================

Important interfaces should have:

- owner;
- purpose;
- contract;
- inputs;
- outputs;
- errors;
- version expectations;
- compatibility expectations;
- tests.

Do not allow undocumented contracts to become critical infrastructure.

======================================================================
16 — TEST TRACEABILITY
======================================================================

Important tests should answer:

WHAT REQUIREMENT OR BEHAVIOR DOES THIS TEST PROTECT?

Avoid large collections of tests whose purpose cannot be determined.

Where practical:

REQUIREMENT
→ TEST(S)
→ RESULT
→ VERIFICATION.

And:

CRITICAL IMPLEMENTATION
→ TEST COVERAGE
→ FAILURE BEHAVIOR.

======================================================================
17 — VERIFICATION TRACEABILITY
======================================================================

Verification must be traceable to the exact repository state tested.

Where appropriate record:

- commit/checkpoint;
- environment;
- configuration;
- test suite;
- gate;
- reviewer;
- timestamp;
- result;
- findings;
- exceptions;
- remediation;
- re-verification.

Do not claim a later modified repository state is verified based solely
on evidence produced against an older materially different state.

======================================================================
18 — RELEASE TRACEABILITY
======================================================================

Every production-capable release or significant deployment should be
traceable to:

RELEASE
→ SOURCE COMMIT
→ REQUIREMENTS
→ CHANGES
→ TESTS
→ VERIFICATION
→ MIGRATIONS
→ CONFIGURATION
→ DEPLOYMENT
→ MONITORING
→ ROLLBACK PLAN.

Do not allow unidentified builds or untraceable production versions.

======================================================================
19 — ENVIRONMENT ORDER
======================================================================

Clearly distinguish:

DEVELOPMENT
TEST
PAPER / SIMULATION
STAGING
CANARY
PRODUCTION

according to the canonical project lifecycle.

Do not mix:

- credentials;
- configuration;
- data;
- execution authority;
- deployment targets;
- operational state.

A development environment must not silently gain production authority.

======================================================================
20 — CONFIGURATION TRACEABILITY
======================================================================

Configuration changes must be controlled.

For important configuration determine:

- canonical source;
- owner;
- environment;
- default;
- allowed range;
- validation;
- security classification;
- change consequences;
- required tests.

Do not duplicate authoritative configuration.

======================================================================
21 — SECURITY TRACEABILITY
======================================================================

Security controls must be traceable to:

SECURITY REQUIREMENT
→ CONTROL
→ IMPLEMENTATION
→ TEST
→ VERIFICATION
→ MONITORING.

Important security exceptions must not exist informally.

Any exception must follow established governance and approval.

======================================================================
22 — FINANCIAL-CONTROL TRACEABILITY
======================================================================

Because this is a financial technology platform, critical financial
behavior must be especially traceable.

Examples include:

- capital authority;
- risk limits;
- exposure calculations;
- order validation;
- execution;
- balances;
- reconciliation;
- P&L;
- fees;
- slippage;
- partial fills;
- failure handling;
- recovery;
- custody state;
- rebalancing.

Critical financial calculations must be deterministic and auditable.

A future investigation should be able to reconstruct:

WHAT THE SYSTEM KNEW
→ WHAT RULES APPLIED
→ WHAT DECISION WAS MADE
→ WHAT ACTION OCCURRED
→ WHAT EXCHANGE REPORTED
→ HOW THE SYSTEM RECONCILED IT.

======================================================================
23 — AI DECISION TRACEABILITY
======================================================================

Where AI materially contributes to a proposal, analysis, or research
decision, preserve enough structured metadata where required to
understand:

- agent/model role;
- task;
- relevant inputs or evidence references;
- structured output;
- confidence where applicable;
- validation;
- whether deterministic systems accepted or rejected the proposal;
- final authoritative decision source.

AI reasoning must not become an opaque substitute for system authority.

======================================================================
24 — OPERATIONAL TRACEABILITY
======================================================================

Company-grade operation must support reconstruction of important events.

Where applicable record:

EVENT
→ SYSTEM
→ STATE BEFORE
→ ACTION
→ STATE AFTER
→ RESULT
→ ERROR / WARNING
→ RECOVERY ACTION.

Logs should be useful for:

- debugging;
- incident response;
- audit;
- reconciliation;
- performance;
- security;
- operational diagnosis.

Do not log secrets.

======================================================================
25 — INCIDENT TRACEABILITY
======================================================================

Significant incidents should follow a controlled lifecycle:

DETECTED
→ CLASSIFIED
→ CONTAINED
→ INVESTIGATED
→ ROOT CAUSE
→ REMEDIATED
→ VERIFIED
→ DOCUMENTED
→ PREVENTIVE ACTION.

Serious incidents must not disappear after the immediate problem is fixed.

======================================================================
26 — AUDITABILITY
======================================================================

A qualified reviewer should be able to reconstruct important project
history without relying on conversation memory.

For significant matters they should be able to determine:

- what existed;
- what changed;
- why it changed;
- who owned the change;
- what evidence supported it;
- what tests ran;
- what review occurred;
- what state resulted.

Auditability is not merely keeping logs.

It means preserving understandable, trustworthy evidence.

======================================================================
27 — NO HIDDEN STATE
======================================================================

Avoid important project state existing only in:

- someone's memory;
- Claude's memory;
- terminal history;
- local untracked files;
- temporary scripts;
- private scratchpads;
- transient container state;
- undocumented environment variables.

Material state must be preserved through the canonical repository,
configuration, storage, or operational systems.

======================================================================
28 — NO SHADOW PROCESSES
======================================================================

Do not allow unofficial processes to evolve beside canonical processes.

Examples:

- unofficial verification path;
- unofficial deployment mechanism;
- second requirements list;
- personal issue list replacing canonical tracking;
- manual configuration that bypasses canonical configuration;
- undocumented emergency workflow.

If a temporary process is necessary:

classify it;
document why;
define owner;
define lifecycle;
define retirement condition.

======================================================================
29 — NO SILENT EXCEPTIONS
======================================================================

Company-grade rules must not be bypassed silently.

If an exception is ever permitted by canonical governance, record:

- rule affected;
- reason;
- approver;
- scope;
- duration;
- risk;
- compensating controls;
- expiration;
- verification.

Temporary exceptions must not silently become permanent architecture.

======================================================================
30 — DOCUMENTATION ORDER
======================================================================

Documentation must remain:

CURRENT
CANONICAL
STRUCTURED
NON-DUPLICATIVE
TRACEABLE.

Do not create documentation merely to increase document count.

Every authoritative document should have a clear role.

Reference instead of copying.

Archive or supersede stale authority correctly.

======================================================================
31 — TRACEABILITY MATRIX / REGISTRY
======================================================================

Use the project's existing traceability mechanism.

If an existing traceability matrix, registry, or generated mapping
already exists:

REINFORCE IT.

Do not create a competing one.

It should support, where appropriate:

REQUIREMENT ID
→ DECISION
→ OWNER
→ SYSTEM
→ IMPLEMENTATION
→ TEST
→ VERIFICATION
→ ROADMAP STAGE
→ STATUS.

Important gaps should become visible.

======================================================================
32 — COMPANY-GRADE QUALITY GATES
======================================================================

Before a major stage exits, ensure required checks cover:

REQUIREMENTS
ARCHITECTURE
IMPLEMENTATION
TESTING
SECURITY
PERFORMANCE
TRACEABILITY
DOCUMENTATION
REPOSITORY INTEGRITY
OPERATIONS
RECOVERY
DEPLOYMENT READINESS
KNOWN ISSUES
OWNER DECISIONS.

Do not claim stage completion based only on passing code tests.

======================================================================
33 — CONTROLLED TECHNICAL DEBT
======================================================================

Technical debt must not be invisible.

Material debt should have:

- description;
- reason;
- impact;
- risk;
- owner;
- related system;
- priority;
- remediation stage;
- status.

Do not use technical debt as a dumping ground for unresolved blockers.

Blocking correctness or safety issues remain blockers.

======================================================================
34 — NO UNTRACKED TODO CULTURE
======================================================================

Do not scatter important TODO comments across the repository without
canonical tracking.

Material TODOs must map to:

- issue;
- requirement;
- technical debt item;
- roadmap item;
- documented deferred work.

Small implementation notes may remain local where appropriate.

Material project obligations may not.

======================================================================
35 — COMPANY-GRADE REVIEW DISCIPLINE
======================================================================

Reviews should verify against:

- approved requirements;
- architecture;
- system ownership;
- coding standards;
- security;
- tests;
- performance where applicable;
- documentation;
- traceability;
- scope.

Review must not silently rewrite approved project intent.

======================================================================
36 — REPOSITORY MUST TELL THE PROJECT STORY
======================================================================

A qualified future engineer should be able to determine:

WHAT WAS THE ORIGINAL OBJECTIVE?

WHAT IS THE CURRENT ARCHITECTURE?

WHAT DECISIONS SHAPED IT?

WHAT REQUIREMENTS EXIST?

WHAT SYSTEM OWNS EACH RESPONSIBILITY?

WHAT HAS BEEN IMPLEMENTED?

WHAT HAS BEEN TESTED?

WHAT HAS BEEN VERIFIED?

WHAT IS CURRENTLY ACTIVE?

WHAT REMAINS?

WHAT IS BLOCKED?

WHAT IS FUTURE WORK?

WHAT CHANGED RECENTLY?

WHY?

WHAT IS THE NEXT AUTHORIZED ACTION?

If the repository cannot answer these questions, improve repository
knowledge organization.

======================================================================
37 — NO FALSE ORDER
======================================================================

Do not make the repository appear organized while inconsistencies remain
underneath.

Examples of false order:

- perfect folder names but duplicate authorities;
- polished documents but outdated implementation;
- traceability table containing incorrect mappings;
- tests marked as passing against stale code;
- architecture diagrams disconnected from actual code;
- completed checklist with missing evidence.

Order must reflect reality.

======================================================================
38 — PERIODIC CONSISTENCY CHECK
======================================================================

At meaningful stage boundaries, inspect for drift between:

REQUIREMENTS
↔ DECISIONS
↔ ARCHITECTURE
↔ CODE
↔ CONFIGURATION
↔ TESTS
↔ VERIFICATION
↔ ROADMAP
↔ OPERATIONS.

Correct drift before it compounds.

======================================================================
39 — PROFESSIONAL HANDOFF STANDARD
======================================================================

Assume at any time the project may be handed to:

- another senior engineer;
- security engineer;
- QA engineer;
- DevOps engineer;
- auditor;
- future Claude Code session;
- operations team.

The repository must allow them to understand the project without needing
the original builder to explain undocumented knowledge.

======================================================================
40 — FINAL COMPANY-GRADE ORDER AUDIT
======================================================================

Before Foundation exits, report:

1. Canonical documents and locations.
2. Requirements traceability status.
3. Decision traceability status.
4. Architecture traceability status.
5. Implementation traceability status.
6. Test traceability status.
7. Verification evidence status.
8. Ownership coverage.
9. Dependency coverage.
10. Configuration coverage.
11. Security traceability.
12. Financial-control traceability.
13. Current stage status.
14. Outstanding blockers.
15. Deferred work.
16. Technical debt.
17. Open owner decisions.
18. Superseded material.
19. Temporary artifacts still present.
20. Repository inconsistencies discovered.
21. Corrections performed.
22. Remaining known gaps.

Do not claim company-grade order without performing this review.

======================================================================
41 — FINAL INTEGRITY PRINCIPLE
======================================================================

EVERY MATERIAL THING MUST BE:

KNOWN.
CLASSIFIED.
OWNED.
LOCATED.
TRACEABLE.
VERIFIABLE.
MAINTAINABLE.
AUDITABLE.
RECOVERABLE.

Nothing important should be:

MISSING.
ORPHANED.
UNOWNED.
UNTRACED.
DUPLICATED.
CONFLICTING.
HIDDEN.
AMBIGUOUS.
STALE.
ACCIDENTALLY PERMANENT.
FALSELY VERIFIED.

======================================================================
MANDATORY TRACEABILITY MODEL
======================================================================

OWNER INTENT
        ↓
DECISION
        ↓
REQUIREMENT
        ↓
ARCHITECTURE
        ↓
SYSTEM OWNER
        ↓
IMPLEMENTATION
        ↓
CONFIGURATION
        ↓
TEST
        ↓
VERIFICATION
        ↓
CHECKPOINT / RELEASE
        ↓
DEPLOYMENT
        ↓
OPERATION
        ↓
MONITORING
        ↓
MAINTENANCE / IMPROVEMENT

AND THE CHAIN MUST BE TRACEABLE BACKWARD WHEN NECESSARY.

======================================================================
FINAL COMMAND
======================================================================

MAKE THE PROJECT OPERATE LIKE A REAL ENGINEERING ORGANIZATION.

DO NOT MERELY STORE INFORMATION.

ORGANIZE IT.

DO NOT MERELY ORGANIZE IT.

TRACE IT.

DO NOT MERELY TRACE IT.

VERIFY IT.

DO NOT MERELY VERIFY IT.

PRESERVE THE EVIDENCE.

DO NOT CREATE DUPLICATE SOURCES OF TRUTH.

DO NOT ALLOW CONFLICTING AUTHORITIES.

DO NOT ALLOW IMPORTANT KNOWLEDGE TO EXIST ONLY IN CHAT.

DO NOT ALLOW IMPLEMENTATION WITHOUT TRACEABLE PURPOSE.

DO NOT ALLOW REQUIREMENTS WITHOUT OWNERSHIP.

DO NOT ALLOW TESTS WITHOUT UNDERSTANDABLE PURPOSE.

DO NOT ALLOW VERIFICATION WITHOUT EVIDENCE.

DO NOT ALLOW CHANGES WITHOUT IMPACT ANALYSIS WHERE MATERIAL.

DO NOT ALLOW HISTORY TO BE LOST.

DO NOT ALLOW THE REPOSITORY TO BECOME DISORDERED AS THE PLATFORM GROWS.

THE REQUIRED STANDARD IS:

ONE COHERENT PROJECT.
ONE CANONICAL SYSTEM OF RECORD.
CLEAR OWNERSHIP.
CONTROLLED CHANGE.
COMPLETE TRACEABILITY.
AUDITABLE EVIDENCE.
PROFESSIONAL ENGINEERING ORDER.
COMPANY-GRADE MAINTAINABILITY.
======================================================================
```
