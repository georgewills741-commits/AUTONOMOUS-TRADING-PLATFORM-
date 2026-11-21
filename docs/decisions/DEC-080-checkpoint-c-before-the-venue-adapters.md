# DEC-080 — The owner's message of 2026-11-21, 20:21 UTC (owner decisions 47): OQ-36 left to the builder, who builds checkpoint C before checkpoint B's venue adapters

- **Status:** ACCEPTED
- **Date:** 2026-11-21
- **Decided by:** builder, under the owner's explicit delegation ("So choose the best option that suits my company project", [owner decisions 47](../handoffs/owner-decisions-47-choice-of-the-next-work-delegated.md)), for the order of the next work; under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept), for the preservation. The owner may override.
- **Resolves:** OQ-36.
- **Affects:** the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) (section 11's order, read with this decision), the [roadmap](../roadmap/roadmap.md), the [open-question register](../open-questions/register.md), the [Stage 2 record](../traceability/stage-02-data-foundation.md), the [project state](../project-state.md).

## Context

The change that builds U4's parts that need no venue's data was committed as `8116301` after its three gates, and the machine checks passed on it ([run 44941433386](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/44941433386)). Its report, at 19:38 UTC, answered the owner's question of 17:23 UTC and put OQ-36 to the owner ([DEC-079](DEC-079-owner-messages-on-open-venue-items-and-other-venues.md), decision 5): whether checkpoint C, U7 the Quantitative Engine with the Fee and Slippage Engines and U6 storage, which need no venue's data, is built before checkpoint B's venue adapters, which wait for a verified venue and an approved server (OQ-34), the builder recommending it (option A), or the plan's order is kept (option B). At 20:21 UTC the owner answered: "So choose the best option that suits my company project".

## Decision

1. **The message is preserved word for word**, as owner decisions 47, a HISTORICAL source listed in the preserved-text manifest, taken by script from its user turn in the session record and kept byte for byte, with the two spaces that end it, so `git diff --check` reports its line.
2. **The owner leaves OQ-36 to the builder, explicitly**, as the owner left the technology stack ([DEC-009](DEC-009-technology-stack.md): "choose the best combination that suits my system"). The builder decides it; the owner may override.
3. **Option A is chosen.** Checkpoint C is built now, U7 first, then U6, each as its own change through the three gates; checkpoint B's venue adapters follow once a venue is verified and a server approved (OQ-34), and checkpoint B stays open until they pass their gates. As the master execution constitution's §64 asks:
   - **Old order** (the plan's section 11): A; B (U4's adapters and U5); C (U6, U7), after B; D; E.
   - **New order:** A (done); B's parts that need no venue's data (U5 and U4's venue-independent parts, done); C (U7, then U6); B's venue adapters, when a venue is verified and a server approved; D; E.
   - **Reason:** B's remaining work needs a verified venue and an approved server, which wait for the owner (OQ-34) and which the builder cannot provide; C's units need neither, so building them now keeps the work going without contacting any venue or relaxing any rule. U7 comes first because it needs no infrastructure; U6 after it, on the environment that U1's readiness check provides (D2).
   - **Dependency:** C depends on B (section 11) for the canonical market data that the adapters supply; its contracts (U2) and its validation (U5) are built. U7 and U6 are built and verified on canonical items that their tests make; each adapter, when it comes, supplies the same items, and its acceptance includes them, so neither unit is built again. Each venue's fee schedule comes with that venue's configuration (D8; EXA-012), carried to its adapter.
   - **Impact:** no requirement, rule, gate, or venue's status changes. Stage 2's E (U10's runs and U11's closure) still needs B's adapters (section 11: E depends on A to D). Checkpoint D's place is not changed by this decision.
4. **Why option A suits the project:** the units it brings forward are needed in any order, cost nothing more, and contact no venue; waiting would stop the work for as long as OQ-34 stays open; and nothing built now is built again when the adapters come.
5. **The message and this decision are recorded by the change that builds U7**, whose record names them.

## Alternatives considered

- **Option B, the plan's order kept.** Not chosen: it stops the work until the owner's open items are settled, for no gain in safety or quality.
- **Checkpoint D too, before B's adapters.** Not decided now: D (U8 regime, U9 opportunity detection) depends on C, and whether its units need a venue's data is assessed when C is done; a change of its place would be recorded then.

## Consequences

- OQ-36 is RESOLVED.
- The Stage 2 plan's section 11 notes the change of order; the roadmap, the Stage 2 record, and the project state show checkpoint C as the next work, U7 first, and checkpoint B open until its adapters pass.
- This decision changes no requirement, rule, gate, or code; no venue is enabled, added, or researched, and no server is approved.
