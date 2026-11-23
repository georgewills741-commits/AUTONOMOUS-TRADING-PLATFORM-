# DEC-081 — The owner's message of 2026-11-23, 20:27 UTC (owner decisions 49): OQ-37 left to the builder, who gives volatility beside the Slippage Engine's estimate in Stage 2

- **Status:** ACCEPTED
- **Date:** 2026-11-23
- **Decided by:** builder, under the owner's explicit delegation ("You choose the best option that suits my company", [owner decisions 49](../handoffs/owner-decisions-49-choice-on-volatility-delegated.md)), for QNT-006's volatility in Stage 2; under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept), for the preservation. The owner may override.
- **Resolves:** OQ-37.
- **Affects:** the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) (section 3.2's row for QNT-006, read with this decision), the [Quantitative Engine's specification](../systems/quantitative-engine.md), the [open-question register](../open-questions/register.md), the [Stage 2 record](../traceability/stage-02-data-foundation.md), the [project state](../project-state.md).

## Context

The change that builds U7, the first unit of Stage 2's checkpoint C, gives volatility beside the Slippage Engine's exact estimate, each with its evidence identifier, rather than folding it into the estimate. Its Gate 3's run 1 found that the plan's section 3.2 lists volatility among QNT-006's parts in Stage 2, so that the choice was the owner's ([checkpoint C (U7) verification](../traceability/stage-02-checkpoint-c-u7-verification.md), F-03). The builder raised OQ-37 and put it to the owner in its report of 19:58 UTC: option A, volatility given beside the estimate in Stage 2, a model that folds it in coming with DIRECTIONAL TRADING and CORE TRADING FOUNDATION, which bring the execution history such a model is fitted to, the builder recommending it; or option B, volatility folded into the estimate in Stage 2. At 20:27 UTC the owner answered: "You choose the best option that suits my company".

## Decision

1. **The message is preserved word for word**, as owner decisions 49, a HISTORICAL source listed in the preserved-text manifest, taken by script from its user turn in the session record and kept byte for byte, with the space that ends it, so `git diff --check` reports its line.
2. **The owner leaves OQ-37 to the builder, explicitly**, as the owner left OQ-36 ([DEC-080](DEC-080-checkpoint-c-before-the-venue-adapters.md)) and the technology stack ([DEC-009](DEC-009-technology-stack.md)). The builder decides it; the owner may override.
3. **Option A is chosen.** In Stage 2, QNT-006's volatility is met by giving volatility beside the Slippage Engine's exact estimate, each with its evidence identifier, to the consumer that combines costs (TNP-017); a model that folds volatility into the estimate comes with DIRECTIONAL TRADING and CORE TRADING FOUNDATION, with the historical execution behaviour that the plan's section 3.2 already gives them for QNT-006. The plan's row for QNT-006 is read with this decision.
4. **Why option A suits the company:** folding volatility into the exact estimate now would need either a float reaching an amount, which the plan's D5 forbids so that money is computed exactly, or a model of volatility's effect on execution with no execution history to fit it to, a guess presented as an estimate; giving both, each with its evidence, leaves nothing lost to the consumer that combines costs, and nothing built now is built again when the model comes.
5. **The message and this decision are recorded by the change that builds U7**, whose record names them.

## Alternatives considered

- **Option B, volatility folded into the estimate in Stage 2.** Not chosen: it needs an exception to D5, or a model with nothing to fit it to (decision 4).

## Consequences

- OQ-37 is RESOLVED.
- The plan's row for QNT-006, the Quantitative Engine's specification, the Stage 2 record, and the project state give the choice as this decision makes it.
- This decision changes no requirement, rule, gate, or code: U7's estimate stands as built.
