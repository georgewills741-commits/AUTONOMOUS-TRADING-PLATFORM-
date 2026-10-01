# Owner Directive — Three-Level Verification and Platform Independence

> **Status:** ACTIVE — builder operating rule and platform principles set by the project owner on 2026-10-01, sent with the [master execution constitution](master-execution-constitution.md). Adopted by [DEC-034](../decisions/DEC-034-verification-and-platform-independence.md) and loaded into every Claude Code session through `CLAUDE.md`. The platform requirements it states are recorded in their owning specifications with DEC-034 as their source; this text is what they cite.
>
> **Formatting note:** converted from plain text to Markdown. The title above was added by the builder; everything below this note is the text as received, with no wording added, removed, or changed. The three "VERIFICATION n —" lines are shown in bold, and a blank line was added before each of the five lists that directly follow a line in the source, as Markdown needs. The lines of `=` that frame each title became Markdown headings, and the closing line of `=` was dropped. The two arrow flows are text blocks. History of this document is kept in git.

IMPORTANT:

From this point forward, EVERY development stage, feature, module, subsystem, or significant change MUST pass the following 3-level verification process before you consider it complete.

**VERIFICATION 1 — TECHNICAL / IMPLEMENTATION VERIFICATION**

- Confirm the implementation is complete.
- Confirm it is correctly integrated with the existing system.
- Run relevant tests.
- Run type checks.
- Run linting.
- Run builds.
- Verify interfaces, schemas, APIs, data contracts, and dependencies.
- Fix all failures before proceeding.

**VERIFICATION 2 — ARCHITECTURE / CONSISTENCY VERIFICATION**

- Confirm the implementation matches the approved project specification and architecture.
- Check against all existing project rules, decisions, requirements, and constraints.
- Check for duplicate systems.
- Check for conflicting requirements.
- Check for overlapping functionality.
- Check that naming, interfaces, data flows, responsibilities, and boundaries remain consistent.
- Ensure the new work does not silently change previously approved behavior.
- Fix any inconsistency before proceeding.

**VERIFICATION 3 — INDEPENDENT END-TO-END / FAILURE VERIFICATION**

- Test the completed stage as an actual working system component.
- Verify realistic end-to-end flows.
- Test important edge cases.
- Test invalid inputs and unexpected states.
- Test relevant dependency failures.
- Test recovery/error handling where applicable.
- Verify that safety, risk, state, logging, and failure controls behave as intended.
- Fix any failure and repeat the verification until it passes.

A stage is NOT COMPLETE unless it passes ALL THREE verification levels.

If any verification level fails:

1. Stop progression.
2. Identify the failure.
3. Fix it.
4. Re-run the failed verification.
5. Re-run any dependent verification that could have been affected.
6. Only then mark the stage complete.

Do NOT skip, weaken, combine, or bypass these verification gates for convenience.

For every completed stage, record the verification results and important evidence in the repository so there is a permanent audit trail.

Do not move to the next development stage until the current stage is:

- implemented,
- tested,
- architecturally consistent,
- independently verified,
- documented,
- and safely committed to Git.

## CRITICAL PLATFORM INDEPENDENCE PRINCIPLE

This project is a persistent, long-lived financial technology platform.

Claude Code is the engineering agent responsible for building,
maintaining, upgrading, extending, testing, documenting, and improving
the platform.

However, Claude Code is NOT the platform.

The production platform must exist independently of Claude Code.

The platform must be capable of:

- Operating without an active Claude Code session
- Operating without an active Claude conversation
- Continuing 24/7 operation within its authorized operating boundaries
- Maintaining persistent state
- Recovering from supported failures
- Enforcing deterministic risk and capital controls
- Executing authorized trading operations
- Monitoring itself
- Recording audit history
- Maintaining configuration and strategy versions
- Being deployed independently
- Being upgraded through controlled engineering processes
- Being restored after failure
- Being migrated between supported environments
- Receiving future features and improvements

Claude Code may return later and continue engineering the platform,
but the platform must never depend on Claude Code being continuously
active in order to operate.

## CLAUDE CODE AS LONG-TERM PLATFORM ENGINEER

Claude Code remains responsible for future engineering work after the
initial platform is released.

Future work may include:

- New features
- New strategies
- New arbitrage systems
- New exchanges
- New data sources
- New AI models
- New AI agents
- Performance improvements
- Security improvements
- Bug fixes
- Infrastructure improvements
- Database migrations
- API upgrades
- Exchange API changes
- Risk-system improvements
- Capital-management improvements
- Monitoring improvements
- Recovery improvements
- Deployment improvements
- User-requested capabilities
- Architectural improvements
- Technical-debt reduction

Every future change must follow the same governance and verification
requirements as the initial build.

## FUTURE DEVELOPMENT MUST CONTINUE FROM THE EXISTING PLATFORM

When Claude Code returns to the project after a previous development
session, it must NOT assume that the project should be rebuilt.

It must first inspect:

- Current repository state
- Current architecture
- Current implementation
- Current documentation
- Current roadmap
- Current requirements
- Current system rules
- Current deployed version where accessible
- Current database/schema state
- Current configuration
- Current strategy versions
- Current outstanding issues
- Current technical debt
- Current migration state
- Current release state

It must determine:

WHERE THE PLATFORM CURRENTLY IS

before determining:

WHAT SHOULD HAPPEN NEXT.

## CONTINUOUS ENGINEERING MODEL

The platform lifecycle is:

```text
BUILD
↓
VERIFY
↓
RELEASE
↓
DEPLOY
↓
OPERATE
↓
MONITOR
↓
MAINTAIN
↓
IDENTIFY IMPROVEMENT
↓
DESIGN
↓
IMPLEMENT
↓
VERIFY
↓
RELEASE
↓
DEPLOY
↓
OPERATE
↓
CONTINUE.
```

This cycle continues throughout the life of the platform.

## CLAUDE SESSION INTERRUPTION MUST NOT DAMAGE THE PROJECT

Claude Code sessions may end because of:

- Session limits
- Context limits
- Time limits
- Connection interruptions
- Environment restarts
- Tool failures
- User interruption
- Other operational reasons.

A session ending must NOT cause project state to exist only inside
Claude's memory.

Before ending a substantial work session, Claude must preserve the
necessary engineering state in the repository.

This includes, where applicable:

- Completed work
- Current stage
- Current task
- Remaining tasks
- Requirements changed
- Files changed
- Architecture decisions
- Tests performed
- Verification results
- Known failures
- Known blockers
- Open questions
- Migration state
- Deployment state
- Next required action

## RESUMABLE DEVELOPMENT

When Claude Code starts a new session, it must first recover project
context from the repository.

It should inspect the authoritative project-state and engineering
documentation before continuing.

It must not rely on:

"I remember what I was doing."

The repository must tell Claude what happened.

## NO RESTART-BASED KNOWLEDGE LOSS

A new Claude session must not:

- Rebuild completed systems
- Duplicate existing components
- Create conflicting documentation
- Reimplement existing functionality
- Forget previous architectural decisions
- Repeat completed stages
- Skip unresolved blockers
- Assume unfinished work is complete.

## CHECKPOINTED DEVELOPMENT

Long-running implementation work should use durable checkpoints.

A checkpoint should identify:

CURRENT STAGE

CURRENT OBJECTIVE

COMPLETED WORK

IN-PROGRESS WORK

REMAINING WORK

BLOCKERS

TEST STATUS

VERIFICATION STATUS

REPOSITORY STATUS

DOCUMENTATION STATUS

NEXT SAFE ACTION.

## COMMIT / PERSISTENCE PRINCIPLE

Completed coherent work must be persisted to version control according
to the repository's approved workflow.

Claude must avoid leaving substantial completed work existing only in an
uncommitted or undocumented session state.

Before moving between major stages, Claude must verify that the relevant
work is:

- Saved
- Consistent
- Tested
- Documented
- Version-controlled
- Recoverable.

## FUTURE UPGRADE PRINCIPLE

When the user requests a future feature, Claude Code should treat the
request as an upgrade to an existing production platform.

It must NOT automatically:

- Rebuild the platform
- Replace existing authorities
- Create duplicate systems
- Rewrite unrelated components
- Destroy compatibility
- Modify production directly
- Skip verification.

Instead:

```text
UNDERSTAND
↓
INSPECT CURRENT PLATFORM
↓
CLASSIFY REQUEST
↓
CHECK EXISTING CAPABILITY
↓
CHECK DUPLICATES
↓
CHECK CONFLICTS
↓
CHECK DEPENDENCIES
↓
DESIGN INTEGRATION
↓
ASSESS RISK
↓
IMPLEMENT
↓
VERIFY
↓
RELEASE
↓
DEPLOY SAFELY
↓
MONITOR
↓
DOCUMENT.
```

## THE PLATFORM MUST OUTLIVE THE BUILDER SESSION

The platform must remain understandable and operable even if:

- Claude Code is closed
- The current Claude session ends
- A future Claude session is started
- A different engineer takes over
- The original development environment changes.

The repository, documentation, deployment definitions, operational
procedures, tests, and version history must preserve the necessary
knowledge.

## FINAL PRINCIPLE

CLAUDE CODE BUILDS AND MAINTAINS THE PLATFORM.

THE PLATFORM DOES NOT DEPEND ON CLAUDE CODE TO OPERATE.

CLAUDE CODE MAY RETURN AT ANY TIME TO:

BUILD

FIX

UPGRADE

EXTEND

OPTIMIZE

MIGRATE

VERIFY

AND MAINTAIN

THE SAME EXISTING PLATFORM.

EVERY FUTURE CHANGE MUST PRESERVE THE PLATFORM'S ARCHITECTURAL
INTEGRITY, FINANCIAL STATE, SAFETY, SECURITY, PERFORMANCE,
RECONCILIATION, AND LONG-TERM MAINTAINABILITY.
