# DEC-059 — The owner's platform traceability rules of 2026-10-14 applied: rules mapped, gaps closed

- **Status:** ACCEPTED
- **Date:** 2026-11-03
- **Decided by:** project owner (the rules, [owner decisions 14](../handoffs/owner-decisions-14-company-grade-order-and-traceability.md), its §18 to §25, which [DEC-046](DEC-046-preserve-company-grade-order-and-traceability-rules.md) (decision 3) has reconciled with the requirements under the owner's requirement drafting rules, a gap drafted under them, and anything that needs the owner put to the owner); the builder's: the mapping to existing requirements, the placement and wording of the new requirements, which follow the owner's words and the established requirements they cite, their stages, and the readings below
- **Resolves:** item 5 of the [project state](../project-state.md)'s "Next approved step"

## Context

On 2026-10-14 the owner sent permanent rules for the project's order, traceability, and auditability (owner decisions 14), in force through DEC-046. Its §18 to §25 concern the platform itself: the traceability of releases, the order and separation of environments, the traceability of configuration, of security controls, of financial controls, of AI decisions, of operations, and of incidents. DEC-046 (decision 3) placed their reconciliation with the requirements after the owner's requirement drafting rules were adopted ([DEC-051](DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md), as corrected on 2026-11-02 in its "Later changes"), and the owner placed it after checkpoint D ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 2). At checkpoint C, Stage 1's own settings and security controls were checked against §20 and §21 (DEC-052, decision 2).

The [platform traceability reconciliation](../traceability/platform-traceability-reconciliation-2026-11-03.md) compared each rule, element by element, with the requirement lines of the specifications, by reading and by a search for each element's terms. Most of the rules were already canonical: §22, §23, and §25 in full, and §18 to §21 and §24 in part. No contradiction was found. Six elements were named by no requirement, or only in general terms: a release's source commit and its links; the deployment targets and operational state of environments; most of the attributes recorded for a setting; security exceptions, and monitoring in a security control's trace; an operational event's state before and after.

## Decision

1. **The rules are applied through the canonical requirements,** not through their text, which stays where DEC-046 keeps it.
2. **What is already canonical stays where it is.** The reconciliation maps each rule to its requirements; none is restated.
3. **Five requirements are added**, each to the specification that owns its subject, each naming the requirements it extends ("In addition to …"), and each stating what no requirement states, or states only in general terms. None of the existing requirements is reworded: each keeps the source it was approved from (a handoff section or a decision), while the new requirement's source is the owner's rules, so a rewording would mix the rules' source into the line or attribute their words to the earlier source (owner decisions 9, Rule 4), and change what was approved (Rule 9); the new lines strengthen the existing ones without changing them, as DEC-051's corrected reading of Rule 16 provides.

| Requirement | What it adds | Extends | Owner |
|---|---|---|---|
| OPS-022 | A release traceable to its source commit, and from it to its requirements, changes, tests, verification, migrations, configuration, deployment, monitoring, and rollback plan; no unidentified build or untraceable production version (§18) | OPS-005, OPS-012, OPS-020 | Deployment and operational readiness |
| OPS-023 | Environments share no deployment target or operational state (§19) | OPS-004, MODE-006, SEC-004 | Deployment and operational readiness |
| MIG-034 | The attributes each important setting records (§20) | MIG-010, MIG-011, ARCH-018, GOV-014 | Hosting, backup, and migration |
| SEC-010 | Each security control traceable through to its monitoring; no informal security exception (§21) | ARCH-040, RSK-049, GOV-016 | SYS-31 Security Architecture |
| MON-012 | An operational event's record, from the event to the recovery action, and what logs serve (§24) | MON-009, AUD-002, SEC-005 | SYS-28 Monitoring and Observability |

4. **One system rule is extended** (ARCH-038): SR-43, no undocumented production changes, also lists OPS-022. No system rule is added.
5. **Each new requirement is mapped to its roadmap stage** (the roadmap's "Additions of 2026-11-03 by stage"): OPS-022, OPS-023, and MON-012 to OPERATIONALIZATION, with their specifications; MIG-034 and SEC-010 to DATA FOUNDATION and each later stage, for the settings and security controls each stage adds. Stage 1's exit criteria are fixed ([DEC-057](DEC-057-progress-continuity-no-loss-and-recovery.md), decision 5), and its own settings and controls were checked against §20 and §21 at checkpoint C.
6. **The owner's requirement drafting rules were applied** ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md), as DEC-051 reads them): each drafted item was classified, its provenance in the owner's words and its owner stated, and the existing requirements it strengthens named; no existing requirement's text changes. The classification and the final reconciliation report (Rule 23) are in the reconciliation record. No owner decision is needed: each new requirement states what the owner's rules say, which DEC-046 has drafted where no requirement states it, and each reading follows from existing requirements and the rules' own text.

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| §19's "DEVELOPMENT, TEST, PAPER / SIMULATION, STAGING, CANARY, PRODUCTION according to the canonical project lifecycle" | The environments of OPS-004: development, testing, research, paper, staging, and production. TEST is testing; PAPER / SIMULATION is paper, with its simulated capital (PAP-013); research stays an environment of its own; CANARY is a stage of production, not an environment (OPS-013) |
| §18's "production-capable release or significant deployment" | A release that can be deployed to production, or a deployment that changes production as OPS-020's significant changes do |
| §20's "important configuration" | Each setting of the platform's configuration, in its two parts (MIG-010). An operating value keeps its record in the values register (ARCH-018) and is recorded as a setting where it becomes one |
| §21's "security exceptions" | A security control not applied, or applied in part, where its requirement says it applies. The "established governance and approval" is RSK-049's formal, audited security change, recorded as GOV-016 asks for a choice that affects security |
| §25's lifecycle | The stages of INC-004 and the fields of INC-002: DETECTED, CLASSIFIED, CONTAINED, INVESTIGATED, and VERIFIED are INC-004's detect, classify, contain, investigate, and verify; ROOT CAUSE is INC-002's root cause; REMEDIATED is INC-004's recover, with INC-002's actions; DOCUMENTED is INC-002's record; PREVENTIVE ACTION is INC-005's structured lessons, which INC-004's learn produces. An incident INC-004 closes still goes on to learn, so a serious incident does not disappear once the immediate problem is fixed |

## Alternatives considered

- **Record the rules without new requirements**, since most were already canonical. Not chosen: six elements were named by no requirement, or only in general terms, and DEC-046 has a gap drafted.
- **Reword the existing requirements instead of adding lines** (owner decisions 9, Rule 16's default). Not chosen: each gap is new content, which a new line can state while naming the requirement it extends; a rewording would mix the rules' source into the line or attribute their words to the earlier source, and change what was approved (decision 3).
- **A line for every rule, §22, §23, and §25 included.** Not chosen: their every element is already named by a requirement (the reconciliation's mapping); another line would restate them (constitution Rule 42; owner decisions 9, Rules 3 and 5).
- **Place MIG-034 and SEC-010 in FOUNDATION**, beside the governance rules placed there for every later feature. Not chosen: Stage 1's plan and exit criteria are fixed (DEC-038; DEC-057, decision 5), and its settings and controls already meet them.

## Consequences

- 744 requirements become 749; no existing requirement changes, so the requirement comparison shows five added and nothing removed or changed.
- The new requirements belong to the stages above. Like the rest of those stages, their features stay PROPOSED until each stage's plan is approved ([DEC-040](DEC-040-later-stage-features-proposed.md)), and nothing beyond Stage 1 is authorized ([DEC-038](DEC-038-stage-1-plan-approved.md)). No code is written for them now.
- When each stage is planned, its plan names how these rules are met and tested: the release record and the deployment check that refuses an unidentified build; separate deployment targets and state per environment; the record of each new setting; each new security control's trace, and the absence of informal exceptions; the operational event records.
