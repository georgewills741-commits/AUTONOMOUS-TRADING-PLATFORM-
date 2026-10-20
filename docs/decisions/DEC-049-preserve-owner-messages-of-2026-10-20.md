# DEC-049 — Preserve the owner's messages of 2026-10-20 (owner decisions 18); Gate 3 reviewers are launched as the rules require

- **Status:** ACCEPTED
- **Date:** 2026-10-20
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: each answer to the builder's questions is kept with its question and options). The messages and the answers are the owner's. How the second answer applies (decision 2) is the builder's reading of the rules it names, recorded so that the owner can correct it.

## Context

On 2026-10-20, while the change that preserves [owner decisions 17](../handoffs/owner-decisions-17-reuse-reinforce-and-enhance-existing-controls.md) was in its second Gate 3 run, the owner asked "how is things going was any rules changed". The question interrupted the builder's running step. The client reported that step as rejected, but its edit had already been written, on the builder's working copy of the next step, outside the repository; only the checks that followed it were cut off. The builder answered that no requirement, builder text, or code had changed, and listed what the change under review and the working copy change.

The interruption also cancelled that run's reviewer before it reported, and the environment then allowed a new reviewer only at the owner's explicit request. The owner said "go ahead with what you're doing", and the builder asked two questions:
- whether to launch a fresh reviewer for the cancelled run;
- whether to launch the reviewers of later Gate 3 runs without asking each time.

The owner chose "Launch a fresh reviewer (Recommended)" for the first. For the second, the owner chose neither option and wrote "follow the rules if it allows you".

## Decision

1. **The messages are preserved word for word**, as [owner decisions 18](../handoffs/owner-decisions-18-question-go-ahead-and-review-relaunch.md), a HISTORICAL source listed in the preserved-text manifest. It was composed by script from the session record: the two typed messages in text blocks, and the two questions with their labels, options, and answers as shown (DEC-047, decision 7).
2. **The reviewers of Gate 3.** The builder's environment lets the builder launch a reviewer, a separate agent, only at the owner's explicit request, and, after the owner has stopped one, another only when the owner asks again. The builder reads the owner's own rules as making that request standing for Gate 3: the owner's [checkpoint rule](../builder/checkpoint-and-verification-rule.md) asks, for Verification 3, "If possible, use an independent reviewer/checker or a separate verification pass rather than relying only on the same reasoning that produced the implementation" ([DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md); [DEC-033](DEC-033-adopt-master-execution-constitution.md)), and [owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md) says "Do NOT bypass DEC-032, DEC-033, Gate 3 …"; no rule asks for the owner's approval before each review. Read as the owner's answer asks, the rules therefore allow it: the builder launches a fresh-context reviewer for each Gate 3 run the procedure requires, without asking each time, and reports each result. The environment's exception stays: after the owner stops or interrupts a reviewer, the builder asks before launching another, as it did on 2026-10-20. This is the builder's reading, not the option the owner was offered and did not choose. It adds no rule and changes no gate, and the owner can stop a review or change the reading at any time.
3. **A launch that stops before it reports**, whether at a usage limit or because the owner interrupted it, is named in its change's verification record, as the [traceability README](../traceability/README.md)'s Gates bullet asks. It is resumed where it can be; otherwise its run is done again, by a new reviewer only as decision 2 allows.

## Alternatives considered

- **Read the second answer as "Ask me each time".** Not chosen: the owner did not choose that option, and the rules the answer names do not require it.
- **Read it as approval of the recommended option.** Not chosen: the owner wrote an answer of their own instead. The owner's quality directive (§11) forbids converting the builder's recommendation into the owner's approval, so the reading rests on the rules, as the answer asks.
- **Ask the owner again whether the checkpoint rule's request covers each review.** Not chosen: the owner's answer leaves it to the rules, and the rule's words ask, where possible, for an independent reviewer or a separate verification pass; a second question would ask the owner to repeat an answer already given. The owner can still change the reading.
- **Keep the question and the go-ahead out, as procedural.** Not chosen: [owner decisions 16](../handoffs/owner-decisions-16-short-instructions-approvals-and-questions.md) keeps a question on the state of the work and two go-aheads ("begin"). "Continue", "Try again", and notices of usage limits stay procedural (DEC-047, decision 7).

## Consequences

- Owner decisions 18 is listed in the preserved-text manifest and the documentation index.
- The verification record of the change that preserves it names the messages ([DEC-048](DEC-048-preserve-and-apply-rule-0.md), decision 3).
- The [traceability README](../traceability/README.md)'s Gates bullet names any launch that stopped before it reported (decision 3).
- No requirement, rule, gate, or code changes. Nothing here authorizes work beyond DEC-038's Stage 1.
