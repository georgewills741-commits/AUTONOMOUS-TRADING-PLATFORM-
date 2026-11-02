# DEC-058 — The owner's opportunity-universe and economics directive applied: principles confirmed, gaps closed

- **Status:** ACCEPTED
- **Date:** 2026-11-02
- **Decided by:** project owner (the directive, [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), which also asks for a missing rule to be corrected where the correct resolution is already established, and for anything that needs the owner to be put to the owner); the builder's: the mapping to existing requirements, the placement and wording of the new requirements, which follow the directive's own words, and the readings below
- **Resolves:** the owner's request of 2026-10-07 to verify that the opportunity-universe and trading-economics principles are represented in the canonical requirements and that nothing contradicts them (the [project state](../project-state.md)'s "Next approved step", item 4)

## Context

On 2026-10-07, during Stage 1, the owner asked for a repository-backed status report and restated the platform's opportunity and economics principles "so that it is preserved in the canonical project knowledge and is not accidentally weakened during implementation": whole-universe discovery with aggressive breadth, depth, and speed; continuous scanning; competition between opportunities; no percentage floor or ceiling, with unusually large opportunities verified rather than rejected or trusted; small opportunities that accumulate; true net economics; dynamic capital allocation; no forced trading, quota, chasing, or revenge trading; active-trade protection; missed-opportunity analysis; strict risk and execution validation; no unsafe fast path. [DEC-041](DEC-041-preserve-opportunity-and-economics-directive.md) preserved the message word for word; the owner later placed the audit after checkpoint D ([DEC-052](DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 2).

The [opportunity and economics audit](../traceability/opportunity-economics-audit-2026-11-02.md) compared each principle with the specifications, the registers, the roadmap, and the code, starting from the [draft](../drafts/draft-audit-of-owner-decisions-08.md) the builder made on 2026-10-07 and 2026-10-12, reconciled with what was decided since: the owner's requirement drafting rules, a builder text since 2026-10-20, with [DEC-051](DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md)'s reading of them, as corrected on 2026-11-02 (its "Later changes"), and the numbers used since. Most principles were already canonical, from Handoff Part 1 (§08, §09, §13 to §17, §20, §21, §23), Part 2, Part 3 (§386 to §394, §416 to §420, §437 to §440), and DEC-014. No contradiction was found. Ten statements of the directive were made by no requirement, or only in part.

## Decision

1. **The directive is applied through the canonical requirements,** not through its text, which stays a HISTORICAL source.
2. **The principles already canonical stay where they are.** The audit maps each of the directive's twenty points to its requirements; none is restated.
3. **Ten requirements are added**, each to the specification that owns its subject, each naming the requirements it extends ("In addition to …"), and each stating only what no requirement states. None of the existing requirements is reworded: each keeps the source it was approved from (a handoff section or a decision), while the new requirement's source is the owner's directive, so a rewording would mix two sources in one line (owner decisions 9, Rule 4) and change what was approved (Rule 9); the new lines strengthen the existing ones without changing them, as DEC-051's corrected reading of Rule 16 provides.

| Requirement | What it adds | Extends | Owner |
|---|---|---|---|
| OPP-021 | Scanning does not stop at a found opportunity | OPP-001, OPP-018 | Opportunity Detection Engine (SYS-05) |
| OPP-022 | Search prioritization by value is a search order only, never a floor, quota, target, stopping condition, or universe restriction | OPP-017 to OPP-020, TNP-005, TNP-016 | SYS-05 |
| TNP-027 | No per-opportunity percentage ceiling | TNP-012, TNP-026 (a daily ceiling), TNP-006 | True Net-Profit Engine (SYS-06) |
| TNP-028 | An unusually large apparent opportunity gets additional validation; it is neither rejected nor executed for its size (V-42) | TNP-020; data validation stays MKD-008 and MKD-013 | SYS-06 |
| TNP-029 | Economics across sizes: minimum efficient, optimal, and maximum efficient capital | TNP-018, QNT-004; the final size stays RSK-011 | SYS-06 |
| TNP-030 | Further economic terms: partial fills, failed or rejected orders, capital lock duration, venue reliability, counterparty and custody exposure; the result in money and relative to capital | TNP-018, TNP-021, TNP-023, TNP-025 | SYS-06 |
| CAP-047 | No "highest percentage wins" rule; further ranking considerations | CAP-009, CAP-006, CAP-043, TNP-015, TNP-021 | Global Capital Authority (SYS-07) |
| CAP-048 | Allocation sized by the opportunity: no tiny allocations for artificial diversification, no full deployment because an opportunity appears | CAP-007, CAP-036, CAP-016, RSK-011 | SYS-07 |
| CAP-049 | Intervening in an active trade only on predefined material conditions, with hysteresis, by the position's owner or the Risk Engine's emergency handling (V-43) | CAP-014, CAP-015, DIR-004, RSK-017 | SYS-07 |
| PFC-019 | The outcome categories of missed- and false-opportunity analysis | PFC-012, PFC-016 | Performance Controller |

4. **Two values are registered** (ARCH-018): V-42, when an apparent opportunity counts as unusually large (OBSERVED, derived per market and strategy; until it is derived, every apparent opportunity gets TNP-028's checks); V-43, the materiality thresholds and hysteresis for intervening in an active trade (POLICY-CONTROLLED PARAMETER, validated with each strategy).
5. **Two system rules are indexed** (ARCH-038): SR-48, economics, not labels: no percentage floor or ceiling; SR-49, active trades are protected from ordinary opportunity competition.
6. **Each new requirement is mapped to its roadmap stage** (the roadmap's "Additions of 2026-11-02 by stage"): OPP-021 and OPP-022 to DATA FOUNDATION; TNP-027 to TNP-030, CAP-047 to CAP-049, SR-48, and SR-49 to CORE TRADING FOUNDATION; PFC-019 to DIRECTIONAL TRADING, with the Performance Controller's core.
7. **The owner's requirement drafting rules were applied** ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md), as DEC-051 reads them): each drafted item was classified, its provenance in the directive's words and its owner stated, and the existing requirements it strengthens named; no existing requirement's text changes. The classification and the final reconciliation report (Rule 23) are in the audit record. No owner decision is needed: each new requirement states what the directive itself says, which the directive asks to be corrected where missing.
8. **The draft is retired.** Its mapping, its requirement texts, its values and system rules, and its readings are incorporated, corrected where the audit found them out of date (the audit record, "The draft reconciled"); its numbers (DEC-042, DEC-043, V-41, V-42) and its status snapshot of 2026-10-12 are superseded.

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "'Universe' means … subject to: … capital availability …" | What is searched is the authorized universe of OPP-009, bounded by OPP-013. The directive's further conditions (execution capability, strategy eligibility, policy, risk controls, capital availability, operational health, instrument and exchange readiness) decide what may be executed (OPP-019, CAP-016, RSK-001, the Readiness System); an opportunity they block is still detected and recorded. The directive's own missed-opportunity categories ("detected but unavailable due to capital", "blocked by risk") require this reading |
| "Do not create an arbitrary rule such as 'Below 1% = ignore.'" | Constrains the architecture: no built-in floor. TNP-016 still allows a percentage threshold as a configurable research or filter parameter that never becomes a universal hard rule, and the operator's own explicit policy may restrict trading (PLT-020, RSK-049), as TNP-026 says for a daily ceiling |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement, derived from evidence per feature (V-39), not a minimum profit for each opportunity. Each opportunity's economic eligibility is TNP-020: a true net expected result above zero after the uncertainty margin, which is never a fixed percentage or universal minimum (TNP-019) |
| MKD-013's "outlier corruption" and MKD-008's "impossible prices" | Data is quarantined when validation shows it is invalid: impossible (a price no market can have, such as zero or negative), inconsistent across sources or sequence, or corrupt. A price that is only extreme, and consistent, is not corrupt; it reaches the opportunity engine, where TNP-028 verifies it. Quarantine is never a size limit on opportunities |
| "expected dollar profit" | The expected profit in the quote currency of the trade, which TNP-018 already computes as an amount; "dollar" is read as the account's quote currency |
| "persistent WebSocket connections", "affected-route recalculation" | Covered by TEC-005 and EXA-012 (WebSocket streams and their connections) and PERF-005 (event-driven processing, incremental calculation, connection reuse); no new requirement. They are designed when DATA FOUNDATION is planned |

## Alternatives considered

- **Record the directive without new requirements**, since most of it was already canonical. Not chosen: ten statements were made by no requirement or only in part, and the owner asked for missing rules to be corrected where the resolution is established.
- **Reword the existing requirements instead of adding lines** (owner decisions 9, Rule 16's default). Not chosen: each gap is new content, which a new line can state while naming the requirement it extends; a rewording would mix the directive's source with a handoff's or a decision's in one line and change what was approved (decision 3).
- **Restate every principle in one new document.** Not chosen: it would be a second copy of requirements that already have one canonical home each (constitution Rule 42; master execution constitution §33).
- **Put the unusual-opportunity rule in market data.** Not chosen: data validation stays with market data (MKD-004, MKD-008, MKD-013), but the rule concerns whether an opportunity is eligible, which the True Net-Profit Engine owns (TNP-017, TNP-020); TNP-028 names data validation as one of its steps.

## Consequences

- 734 requirements become 744; no existing requirement changes, so the requirement comparison shows ten added and nothing removed or changed.
- The new requirements belong to the stages of their specifications (DATA FOUNDATION for SYS-05; CORE TRADING FOUNDATION and the trading stages for the others). Like the rest of those stages, their features stay PROPOSED until each stage's plan is approved ([DEC-040](DEC-040-later-stage-features-proposed.md)), and nothing beyond Stage 1 is authorized ([DEC-038](DEC-038-stage-1-plan-approved.md)). No code is written for them now.
- When each stage is planned, its plan includes tests for these rules: filters and eligibility with small, large, and unusually large opportunities; ranking where the highest percentage is not the best; scanning that continues after a find; an active trade and a better-looking new opportunity; the outcome categories of PFC-019.
- The draft's disposition in the [drafts index](../drafts/README.md) becomes SUPERSEDED AND RETIRED by this record.
