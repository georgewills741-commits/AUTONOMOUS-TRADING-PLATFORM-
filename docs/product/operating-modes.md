# Operating Modes

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **Owner:** not assigned in Part 1 (OQ-08) · **Roadmap stage:** not mapped by §95 (CF-05) · **Sources:** §31

Canonical definition of the platform's operating modes.

## Requirements

- **MODE-001** Four operating modes · CONFIRMED REQUIREMENT · §31 — The platform should support: RESEARCH (no real-money trading); PAPER (live/relevant market conditions with simulated capital); SUPERVISED (trade proposals require authorization according to configured policy); AUTONOMOUS LIVE (authorized trading executes automatically within policy and deterministic controls).
- **MODE-002** Controlled mode transitions · CONSTRAINT · §31 — Transitions must be controlled and auditable.

## Related concepts that are not the same thing

The same words appear elsewhere with different meanings. They are kept distinct (see [glossary](../glossary.md)):

| Term | Here (platform operating mode) | Elsewhere |
|---|---|---|
| RESEARCH | Mode with no real-money trading | Strategy lifecycle stage (§34); research activity boundaries (§37); Research Agent (§54) |
| PAPER | Mode using simulated capital | Strategy lifecycle stage (§34); [Paper Trading](../systems/strategy/paper-trading.md) system (§32) |
| AUTONOMOUS LIVE | Mode in which authorized trading executes automatically | Strategy lifecycle stage PRODUCTION (§34); roadmap item "Live operation" (§95) |

## Not specified in Part 1

Which system owns the current mode, who may change it, what approvals a transition needs, how SUPERVISED authorization works, and whether different strategies may run in different modes at the same time. Tracked as OQ-08 in the [open-question register](../open-questions/register.md).
