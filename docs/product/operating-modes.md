# Operating Modes

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **Owner:** SYS-12 Policy System (POL-008, [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md)) · **Roadmap stage:** CORE TRADING FOUNDATION ([DEC-016](../decisions/DEC-016-roadmap-stage-placement.md)) · **Sources:** §31

Canonical definition of the platform's operating modes.

## Requirements

- **MODE-001** Four operating modes · CONFIRMED REQUIREMENT · §31 — The platform should support: RESEARCH (no real-money trading); PAPER (live/relevant market conditions with simulated capital); SUPERVISED (trade proposals require authorization according to configured policy); AUTONOMOUS LIVE (authorized trading executes automatically within policy and deterministic controls).
- **MODE-002** Controlled mode transitions · CONSTRAINT · §31 — Transitions must be controlled and auditable.

## Decisions applied (2026-09-30)

- **MODE-003** Per-strategy modes under a platform maximum · CONFIRMED REQUIREMENT · DEC-015 — Each strategy runs in its own operating mode, capped by a platform-wide maximum mode set in policy.
- **MODE-004** Mode transitions · DEPRECATED / REPLACED · DEC-015 — Moving to a more permissive mode requires the operator's confirmation and the strategy's lifecycle eligibility: PAPER needs the paper stage; SUPERVISED and AUTONOMOUS LIVE need approval, and a new version must pass canary (STR-011). Moving to a less permissive mode may happen automatically.
- **MODE-005** Supervised authorization · SYSTEM REQUIREMENT · DEC-015 — In SUPERVISED mode the operator approves or rejects each proposal. A proposal not approved before it expires is treated as NO TRADE, and an approved proposal is revalidated before execution (EXE-004).
- **MODE-006** Modes vs environments · CONSTRAINT · DEC-015 — Real orders can be sent only from the production environment, the only environment holding trading-enabled credentials. Development, testing, research, paper, and staging environments are technically unable to place real orders.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

MODE-004 is replaced by MODE-007: it required operator confirmation for every more permissive mode, which contradicts automatic canary entry (OC-1 item 17).

- **MODE-007** Autonomous mode progression within policy · CONFIRMED REQUIREMENT · DEC-019 — A strategy moves to a more permissive mode automatically when the deterministic readiness gates for that step pass (STR-013 to STR-016), within the platform-wide maximum mode set in policy. Raising the platform-wide maximum mode is an important policy change (POL-005). A step that policy designates human-controlled requires the operator (PLT-014). Moving to a less permissive mode may happen automatically.

## Related concepts that are not the same thing

The same words appear elsewhere with different meanings. They are kept distinct (see [glossary](../glossary.md)):

| Term | Here (platform operating mode) | Elsewhere |
|---|---|---|
| RESEARCH | Mode with no real-money trading | Strategy lifecycle stage (§34); research activity boundaries (§37); Research Agent (§54) |
| PAPER | Mode using simulated capital | Strategy lifecycle stage (§34); [Paper Trading](../systems/strategy/paper-trading.md) system (§32) |
| AUTONOMOUS LIVE | Mode in which authorized trading executes automatically | Strategy lifecycle stage PRODUCTION (§34); roadmap item "Live operation" (§95) |

## Resolved questions

OQ-08 is resolved by [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md): mode ownership (POL-008), granularity (MODE-003), transitions (MODE-004), supervised authorization (MODE-005), and separation from environments (MODE-006).
