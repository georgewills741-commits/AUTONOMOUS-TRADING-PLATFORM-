# DEC-070 — Preserve the owner's permanent trading rules of 2026-11-16 (owner decisions 37) and map them to the canonical requirements

- **Status:** ACCEPTED
- **Date:** 2026-11-16
- **Decided by:** builder: the preservation under [DEC-004](DEC-004-preserve-original-handoffs.md) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7), and the mapping under [owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)'s rules ([DEC-051](DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md)). The rules are the owner's.

## Context

On 2026-11-16, at 18:54 UTC, the owner sent a master directive of permanent trading rules and asked whether the builder understands it. It restates, for the platform's permanent operating policies, the trading rules of the owner's directive of 2026-11-06 ([owner decisions 29](../handoffs/owner-decisions-29-universal-opportunity-intelligence-and-profit-optimization.md)) and of the owner's answers of 2026-11-10 ([owner decisions 34](../handoffs/owner-decisions-34-approval-to-plan-stage-2-and-answers-on-the-directive.md)), which [DEC-068](DEC-068-universal-opportunity-directive-mapped.md) mapped to the canonical requirements the same day. It asks the builder to inspect first, map each rule to what already exists, strengthen or add only what is missing, and duplicate nothing. The builder answered that evening that it understands it, and that each of its points is already stated by the canonical requirements, with nothing to add and no conflict.

## Decision

1. **The message is preserved word for word**, as [owner decisions 37](../handoffs/owner-decisions-37-permanent-autonomous-trading-rules.md), a HISTORICAL source listed in the preserved-text manifest, taken by script from the session record and checked by its round trip.
2. **Each of its points is already canonical.** The [workflow and efficiency record](../traceability/workflow-and-efficiency-2026-11-16.md) maps each section to the requirements, values, system rules, and builder texts that state it, mostly through DEC-068's mapping. No requirement, value, or system rule is added, removed, or changed: none is missing, and none conflicts (owner decisions 9, Rules 5 and 10; the message's own Rules C and D).
3. **The daily figure stays a measurement** (V-44; PFC-021; SR-19), as the owner chose on 2026-11-10 and as the message itself says: "This is a performance objective, not a guaranteed return or mandatory daily trading requirement." Its "or higher" and its "Seek approximately 1.2% net daily or higher when market conditions genuinely permit" are read with its own restrictions: every independently justified opportunity is captured, with no ceiling at the figure (TNP-013, TNP-026) and nothing steered toward it.
4. **Emergency reserves** are used only as their policy permits: the message's "Do not spend emergency reserves without authorization under established policy" is CAP-029 (the emergency reserve, controlled by policy) with CAP-033 (no capital movement may violate the emergency reserve requirements).
5. **Its three gates** (its §16) are DEC-032's, named and ordered differently, as owner decisions 29's were (DEC-068's reading notes); nothing is renamed.
6. **Nothing is implemented.** No trading code exists yet: each requirement is built, with its tests, by the stage the [roadmap](../roadmap/roadmap.md) places it in, under that stage's approved plan ([DEC-038](DEC-038-stage-1-plan-approved.md); [DEC-040](DEC-040-later-stage-features-proposed.md)); Stage 2's planning is authorized and its implementation is not ([DEC-067](DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md), decision 2).

## Alternatives considered

- **Restate the rules as new requirements, or in a trading-policy document of their own.** Not chosen: each is stated already, and the message itself forbids parallel copies (its Rules C and D; owner decisions 9, Rules 3 and 19).
- **Read the daily figure as a target to steer toward.** Not chosen: the owner chose a measurement on 2026-11-10 (OQ-32), and the message's own restrictions rule steering out.

## Consequences

- Owner decisions 37 is listed in the preserved-text manifest and the documentation index; the workflow and efficiency record maps it.
- No requirement, rule, gate, value, or code changes (the record's requirement comparison).
