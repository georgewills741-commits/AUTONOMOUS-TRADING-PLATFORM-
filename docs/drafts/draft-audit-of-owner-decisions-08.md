# Draft — The Audit of Owner Decisions 8

> **Status:** DRAFT — NOT APPROVED, NOT AUTHORITATIVE, NOT VERIFIED, NOT PRODUCTION-READY. The builder's unverified work for item 4 of the [project state](../project-state.md)'s "Next approved step" (the audit the owner asked for on 2026-10-07, [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)), made on 2026-10-07 and 2026-10-12 in the builder's session workspace, never reviewed, and kept only there until DEC-047 (decision 3) had it committed as a draft. It drafts ten requirements, two system rules, and two values; none of them exists: their IDs are assigned nowhere, nothing in the draft is decided or in force, and it predates the adoption of owner decisions 9, whose drafting rules the audit must follow. It is committed as a draft under [owner decisions 15](../handoffs/owner-decisions-15-stage-transition-persistence-and-commit-integrity.md) (§1, §7, §8), as [DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md) (decision 3) decides; [DEC-046](../decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md) (decision 5) classifies it. Each file is kept in a text block, so nothing in it defines or changes a requirement, decision, rule, value, or record.
>
> **Disposition:** COMMITTED AS DRAFT, until item 4 reads it first, compares it with the canonical records, merges what remains valid under the rules then in force, keeps its provenance, and marks it superseded by the record that replaces it ([drafts index](README.md)).

## The draft audit record

The record of the audit, written as if for `docs/traceability/`; its checks, gates, failures, and final status were never filled in. Original: 20,072 bytes, sha256 `b4836bcdfc734f8286c83c0e0438480a6aa8bd71380f3f0ede3c186320b64ee0`.

```text
# Opportunity-Universe and Economics Audit — 2026-10-12

> **Status:** ACTIVE record of the audit the owner asked for on 2026-10-07 ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)): are the opportunity-universe and trading-economics principles represented in the canonical requirements, and does anything contradict them? Preserved by [DEC-041](../decisions/DEC-041-preserve-opportunity-and-economics-directive.md); applied by [DEC-043](../decisions/DEC-043-opportunity-universe-and-economics.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md); format: [traceability README](README.md).

## Identity

- **Date:** 2026-10-12
- **Stage:** 1 — FOUNDATION, between checkpoints B and C. This audit writes documentation only; it starts no later stage's work (DEC-038)
- **Starts from:** the commit of Stage 1's checkpoint B (the [project state](../project-state.md)'s checkpoint log). This record's own commit is entered there by the next checkpoint
- **Request:** the owner's message of 2026-10-07, preserved as owner decisions 8

## Stage 1 status at the time of the audit

The owner asked for this first. The canonical, current status is the [project state](../project-state.md) and the [stage record](stage-01-foundation.md); this is the snapshot the owner was given.

| Question | Answer, with evidence |
|---|---|
| Has Stage 1 started? | Yes. The owner approved the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) and authorized its implementation on 2026-10-05 ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md)) |
| Implemented | Checkpoint A (commit `f2e4046`): development environment, repository test for secrets, machine checks on GitHub (U1, U6). Checkpoint B: `atp.numeric` (exact amounts) and `atp.contracts` (contract kernel, outcomes, idempotency keys), committed schemas, U6's Hypothesis setting (U2, U3). No trading, exchange, configuration, or deployment code exists |
| Verified | Checkpoint A: three gates ([record](stage-01-checkpoint-a-verification.md)); the machine checks pass on GitHub and fail on a deliberately broken check. Checkpoint B: three gates ([record](stage-01-checkpoint-b-verification.md)). The stage as a whole is verified again at checkpoint D |
| Being worked on | This audit |
| Remaining in Stage 1 | Checkpoint C: configuration (U4) and the security foundation with the threat model (U5). Checkpoint D: the verification matrix (U7), the stage record's closure, the §152 checklist, and the completion certificate (U8). Then the owner's approval to proceed to Stage 2 planning |
| Blocked or waiting for a decision | Nothing blocked. No owner decision is pending |
| Next implementation step | Checkpoint C, starting with the items the stage record carries to it (TOML integers for amount settings; how a parsed TOML document reaches a contract; the secret scanner's unreported shapes) |

## Method

1. Every principle of the directive, and each of its twenty numbered points, compared with the requirement lines of the specifications (`docs/systems/`, `docs/risk/`, `docs/product/`, `docs/architecture/`, `docs/operations/`, `docs/ai/`), the [values register](../requirements/values-register.md), the [System Rules Register](../requirements/system-rules-register.md), the [roadmap](../roadmap/roadmap.md), and the handoffs they came from.
2. A contradiction search, by script over every requirement line: percentages; "minimum", "threshold", "ceiling", "cap", "limit", "maximum"; "highest" or "largest"; "forced", "quota", "trade count", "chase", "revenge", "martingale", "daily target"; "interrupt", "unwind", "hedge", "hysteresis"; "anomal", "outlier", "impossible", "suspicious". Each hit read in context.
3. The code checked for any limit on opportunity size (Stage 1's code has no opportunity logic; `atp.numeric` limits an amount's digits and exponent, not its size relative to anything).
4. Each gap closed in the specification that owns its subject, citing the existing requirements instead of restating them.

## The twenty points

| # | The directive's point | Canonical requirements | Result |
|---|---|---|---|
| 1 | Whole-universe opportunity discovery | OPP-001, OPP-003, OPP-009, OPP-013, OPP-018 | Represented |
| 2 | Aggressive breadth | OPP-017 ("breadth of search"), OPP-002, OPP-018, OPP-020, PLT-022 | Represented |
| 3 | Aggressive depth | OPP-017 ("depth of analysis"), TNP-018 (the order book walked at the intended size), TNP-024, TNP-025, TAR-002 to TAR-004, XAR-003, CAP-043; sizes and capacity added: TNP-029 | Represented; sizes added |
| 4 | Aggressive speed | OPP-017 ("speed of detection"), OPP-012, PERF-005, PERF-009, PERF-010, PERF-019, TEC-005, EXA-012 | Represented |
| 5 | Continuous scanning | OPP-017, OPP-018 ("continuously evaluate"), PLT-022; added: OPP-021 (a find does not stop the search), OPP-022 (prioritization is never a stopping condition) | Represented; made explicit |
| 6 | Cross-opportunity competition | CAP-008, CAP-009, CAP-017, CAP-043, TNP-015, TNP-021; added: CAP-047 (no "highest percentage wins" rule) | Represented; made explicit |
| 7 | 5%+ opportunities when genuinely valid | TNP-006 ("+5%, or any other positive result that genuinely survives the complete evaluation"); added: TNP-027 (no per-opportunity ceiling), TNP-028 | Represented; made explicit |
| 8 | 3%, 2%, 1.5%, 1%, 0.9% and other levels | TNP-006, TNP-007, TNP-020 | Represented |
| 9 | Smaller opportunities (0.1%, 0.2%, 0.4%, 0.5%) | TNP-005, TNP-006 (example +0.1%), TNP-008, TNP-009, TNP-011 | Represented |
| 10 | Accumulation of repeated smaller profitable opportunities | TNP-008, TNP-010, CAP-010, PLT-019 | Represented |
| 11 | True net economics after all relevant costs | TNP-001 to TNP-004, TNP-018, TNP-019, TNP-020, TNP-023, TNP-024, TNP-025, XAR-002, XAR-004; added: TNP-030 (partial fills, failed or rejected orders, capital lock duration, venue reliability, counterparty and custody exposure) | Represented; terms added |
| 12 | Dynamic capital allocation | CAP-006, CAP-007, CAP-030, CAP-035, CAP-036, CAP-043, CAP-045; added: CAP-048 (allocation sized by the opportunity) | Represented; sizing added |
| 13 | No artificial percentage floor | TNP-005, TNP-016, TNP-019, TNP-020, ARB-015; added: OPP-022 | Represented |
| 14 | No artificial percentage ceiling | Daily: TNP-012, TNP-013, TNP-026. Per opportunity: added TNP-027, with TNP-028 for unusually large opportunities | Daily represented; per opportunity added |
| 15 | No forced trading | RSK-031, RSK-032, RSK-044, PLT-018, PLT-019, PLT-025, CAP-036 | Represented |
| 16 | No daily profit quota | TNP-014, RSK-044 ("hit a daily target"), PLT-007, PLT-008, PLT-019 | Represented |
| 17 | No chasing or revenge trading | RSK-044 (chasing), RSK-047 (revenge trading, martingale) | Represented |
| 18 | Active-trade protection | CAP-014, CAP-015; added: CAP-049 (interventions only on predefined material conditions, with hysteresis) | Represented; interventions added |
| 19 | Missed-opportunity analysis | OPP-014, OPP-015, PFC-012, PFC-013, PFC-016, ARB-003; added: PFC-019 (outcome categories) | Represented; categories added |
| 20 | Strict risk and execution validation | OPP-019, TNP-011, CAP-004, CAP-016, RSK-001, EXE-004, PERF-023, DIR-003 | Represented |

The directive's other statements map the same way: the universe and its conditions (OPP-009, OPP-013; reading in DEC-043), the discovery flow (OPP-005, OPP-018, PLT-022), capital growth without reckless scaling (CAP-034, PLT-023, RDY-013, CAP-032), the objective (PLT-009, PLT-019, TNP-010), and the performance principle (PERF-005, PERF-014, PERF-016, PERF-021, PERF-010, PERF-023). The existing system rules SR-04, SR-05, SR-06, SR-07, SR-11, SR-15, SR-18, and SR-19 already index most of them; SR-48 and SR-49 are added.

## Contradictions

None found. Each hit of the search that could be read as a floor, a ceiling, a quota, or a size rule, and why it is consistent:

| Hit | Why it does not contradict the directive |
|---|---|
| ARB-015's tiers (about ≥1%, 0.5–1%, 0.2–0.5%, below 0.2%) | "Analytical categories only, not unconditional execution rules" |
| TNP-016's configurable percentage threshold | Allowed only as a research or filter parameter that never becomes a universal hard rule; the directive forbids a built-in floor, not the operator's own explicit policy (reading in DEC-043) |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement derived from evidence (V-39), not a minimum for each opportunity (reading in DEC-043) |
| TNP-019's uncertainty margin | Scaled by measured uncertainty; "must never be a fixed percentage or a universal minimum" |
| TNP-026's "unless an explicit risk/capital policy requires it" | Only the operator's explicit policy can stop operation for the day; the architecture has no ceiling |
| MKD-008's "impossible prices", MKD-013's "outlier corruption" | Quarantine of invalid data, not of extreme prices (reading in DEC-043; TNP-028) |
| The values register's examples (TNP-006, TNP-012, TNP-014) | Listed there as illustrations, never operating values |
| STR-011's "minimum period and trade count" | DEPRECATED / REPLACED (DEC-015, DEC-019); STR-018 makes time and trade count evidence only |
| The roadmap | No stage, item, or feature sets a percentage, target, or quota |
| The code | No opportunity logic exists; no amount is capped relative to anything |

## Duplicates

None created. The ten new requirements cite the requirements they extend ("In addition to …") instead of restating them. The directive itself is kept as a HISTORICAL source, not a second set of rules. Two restatements were taken out of the drafts before they were applied: TNP-027's sentence that 5% is not a target, minimum, quota, or expected daily return (already TNP-014, TNP-005, and RSK-044), and CAP-049's opening sentence that a newer opportunity is never by itself a reason to intervene (already CAP-014).

## Classification and provenance of each drafted item

The owner's [requirement drafting and anti-drift rules](../builder/requirement-drafting-and-anti-drift-rules.md) apply to this audit ([DEC-042](../decisions/DEC-042-adopt-requirement-drafting-and-anti-drift-rules.md)): each drafted item is classified (Rule 8), its origin stated (Rule 4), its owner and stage named (Rules 7 and 14), the existing requirement it strengthens named (Rule 16), and where it will be enforced and tested (Rule 17). The categories are the outcome of this reconciliation; each requirement keeps its ARCH-015 class in its specification line (DEC-042's reading notes).

| Item | Category (Rule 8) | Provenance (Rule 4): owner decisions 8, section | Strengthens (Rule 16) | Owner (Rule 7) | Stage (Rule 14) | Enforced and tested (Rule 17) |
|---|---|---|---|---|---|---|
| OPP-021 | NEW CONFIRMED REQUIREMENT | "Continuous whole-universe scanning" | OPP-001, OPP-018 | Opportunity Detection Engine (SYS-05) | 2 DATA FOUNDATION | The opportunity filter (OPP-005); test: scanning continues after a find of any size |
| OPP-022 | NEW CONFIRMED REQUIREMENT | "Opportunity search prioritization" | OPP-017 to OPP-020, TNP-005, TNP-016 | SYS-05 | 2 | The filter's search order; SR-48; test: no candidate below a priority level is dropped for its level |
| TNP-027 | NEW CONFIRMED REQUIREMENT | The opening reinforcement ("Only trade opportunities up to 1%") and "No artificial opportunity ceiling" | TNP-012, TNP-026 (the daily ceiling) | True Net-Profit Engine (SYS-06) | 3 CORE TRADING FOUNDATION | Economic eligibility (TNP-020); SR-48; test: a large positive-net opportunity is not rejected for its percentage |
| TNP-028 | NEW CONFIRMED REQUIREMENT | "No artificial opportunity ceiling" (the order of validation) | TNP-020; data validation stays MKD-008 and MKD-013 | SYS-06, with market data's validation | 3 | Eligibility; V-41; SR-48; test: an unusually large opportunity passes every check or is rejected for a named check, never for its size |
| TNP-029 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" (minimum efficient, optimal, and maximum efficient capital) | TNP-018, QNT-004; the final size stays RSK-011 | SYS-06; the Global Capital Authority allocates within it; the Risk Engine sets the final size | 3 | The economics calculation; test: the result across sizes, with the range's ends |
| TNP-030 | NEW CONFIRMED REQUIREMENT | "True net economics" (its list of costs, and "expected dollar profit") | TNP-018, TNP-021, TNP-023, TNP-025 | SYS-06 | 3 (the arbitrage terms with stage 5, as TNP-023) | The economics calculation; test: each term changes the result where it applies |
| CAP-047 | NEW CONFIRMED REQUIREMENT | "Cross-opportunity competition" (not "Always choose the highest percentage"; its ranking list) | CAP-043, TNP-015, TNP-021, CAP-009 | Global Capital Authority (SYS-07) | 3 | Allocation ranking; SR-48; test: a higher percentage ranks below a better opportunity |
| CAP-048 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" | CAP-043, CAP-016, RSK-011 | SYS-07 | 3 | Allocation; test: neither tiny artificial allocations nor full deployment because an opportunity appears |
| CAP-049 | NEW CONFIRMED REQUIREMENT | "Active trade protection" | CAP-014, CAP-015, DIR-004, RSK-017 | SYS-07, with the position's owner and the Risk Engine | 3 (the positions' owners in stages 4 and 5) | SR-49; V-42; test: an active trade and a better-looking new opportunity; hysteresis |
| PFC-019 | NEW CONFIRMED REQUIREMENT | "Missed opportunity analysis" | PFC-012, PFC-016 | Performance Controller | 4 DIRECTIONAL TRADING (its core) | The Opportunity Database's records (OPP-014 to OPP-016); test: each category recorded |
| V-41, V-42 | Part of TNP-028 and CAP-049: values to be derived or set (ARCH-018), not requirements | "Unusually large"; "materiality thresholds and hysteresis" | The values register | As their requirements | As their requirements | Recorded as not derived and not set, with their behaviour until then |
| SR-48, SR-49 | Index entries over existing and new requirements (ARCH-038); no new rule | The requirements they index | SR-04 to SR-07, SR-11 (alongside) | As named in the register | 3 | The enforcement points and tests named in the register |
| The six readings in DEC-043 | EXISTING REQUIREMENT (the reading of an existing requirement, or of the directive's wording, under it) | The requirements each names | — | — | — | — |
| The twenty points, where "Represented" | EXISTING REQUIREMENT | The requirements in the table above | — | — | — | — |

No item is a REFINED EXISTING REQUIREMENT: no existing requirement's text changes; each gap is closed by a new requirement in the same specification, with the same owner, that names the requirements it strengthens. Rewording an existing requirement would mix its source (a handoff section) with the directive's, while a new line keeps each requirement's provenance exact (Rule 4) and needs no change to what was already approved (Rule 9).

## Final reconciliation report

Rule 23 of the drafting rules, before the drafted requirements become authoritative:

| # | Item | Result |
|---|---|---|
| 1 | Existing requirements identified | Every one of the twenty points has canonical requirements (the table of the twenty points); the directive's other statements map to OPP-005, OPP-009, OPP-013, OPP-018, PLT-009, PLT-019, PLT-022, PLT-023, CAP-032, CAP-034, RDY-013, TNP-010, and PERF-005, PERF-010, PERF-014, PERF-016, PERF-021, PERF-023 |
| 2 | Requirements mapped | The twenty points and the other statements, as above; system rules SR-04, SR-05, SR-06, SR-07, SR-11, SR-15, SR-18, SR-19 already index most of them |
| 3 | Requirements refined | None: no existing requirement's text, class, or source changes (the requirement comparison shows nothing changed) |
| 4 | Genuine new requirements | Ten: OPP-021, OPP-022, TNP-027 to TNP-030, CAP-047 to CAP-049, PFC-019, each with the owner's directive as its source |
| 5 | Duplicates rejected | Two restatements taken out of the drafts (TNP-014's and CAP-014's content); "persistent WebSocket connections" and "affected-route recalculation" (TEC-005, EXA-012, PERF-005); "expected dollar profit" (TNP-018's amount in quote currency); a document restating every principle (DEC-043's alternatives) |
| 6 | Unnecessary items rejected | None beyond the duplicates of item 5 |
| 7 | Future capabilities identified | None new. The ten requirements belong to stages 2 to 4, whose features stay PROPOSED until each stage's plan is approved (DEC-040); nothing beyond Stage 1 is authorized (DEC-038) |
| 8 | Owner decisions required | None (below, "Owner decisions") |
| 9 | Conflicts discovered | None (the contradiction search above; each hit explained) |
| 10 | Conflicts resolved | None needed. Six phrases that could be read against the directive are read in DEC-043 under the requirements they belong to |
| 11 | Dependencies affected | The Opportunity Detection Engine, the True Net-Profit Engine (with the Quantitative Engine's calculations and market data's validation), the Global Capital Authority, the Risk Engine (final size, emergency handling), the positions' owners (directional and arbitrage systems), and the Performance Controller. No interface, schema, configuration, or code exists for them yet; each is designed with its stage's plan |
| 12 | Canonical sources updated | The four specifications (opportunity detection, true net profit, capital management, performance controller), the [values register](../requirements/values-register.md) (V-41, V-42), the [System Rules Register](../requirements/system-rules-register.md) (SR-48, SR-49), the [roadmap](../roadmap/roadmap.md) ("Additions of 2026-10-12 by stage"), the generated [registry](../requirements/registry.md), the [decision log](../decisions/README.md), and the [project state](../project-state.md) |
| 13 | Enforcement locations identified | Per requirement in the classification table; for the system rules, in the register's enforcement-point column |
| 14 | Tests added or updated | None in code: no opportunity, economics, or allocation code exists in Stage 1. The tests each stage's plan must include are listed in DEC-043's consequences and in the classification table |
| 15 | Three-pass verification performed | Below ("Gates") |
| 16 | Remaining unresolved items | V-41 is not derived and V-42 is not set (values register, with the behaviour until then); nothing else |

## Gaps closed

| Gap | Closed by |
|---|---|
| A found opportunity could, in a reading, end the search | OPP-021 |
| Search prioritization by value had no stated limits | OPP-022 |
| No requirement forbade a ceiling on a single opportunity (only on the daily total) | TNP-027 |
| No requirement said what to do with an unusually large opportunity | TNP-028, V-41 |
| No requirement gave an opportunity a size range (minimum efficient, optimal, maximum efficient) | TNP-029 |
| Partial fills, failed or rejected orders, capital lock duration, venue reliability, and counterparty or custody exposure were not named as economic terms | TNP-030 |
| "Always choose the highest percentage" was excluded only implicitly (CAP-009) | CAP-047 |
| No requirement excluded tiny artificial allocations or full deployment because an opportunity appears | CAP-048 |
| Active trades were protected (CAP-014), but when an intervention is allowed, by whom, and with what stability was not stated | CAP-049, V-42 |
| Expired, disappeared, latency-missed, and never-detected opportunities were not named categories | PFC-019 |
| No system rule indexed the floor and ceiling rules or active-trade protection | SR-48, SR-49 |

## Owner decisions

None required: every point is either already canonical or stated by the owner in the directive, and each reading follows from existing requirements and the directive's own text. The readings are recorded in DEC-043 for the owner to see.

## Checks

Pending.

## Gates

Pending.

## Failures and fixes

Pending.

## Final status

Pending.
```

## The first draft decision record

A decision record of 2026-10-07, numbered DEC-042 in the draft; that number has since been used for another decision. Original: 8,453 bytes, sha256 `2adca961ce45685d884b9cf9817e3e8eddc3afeeb05e82ac34ce61bbfa9fa54c`.

```text
# DEC-042 — The owner's opportunity-universe and economics directive applied: principles confirmed, gaps closed

- **Status:** ACCEPTED
- **Date:** 2026-10-07
- **Decided by:** project owner (the directive, [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)); the builder's: the mapping to existing requirements, the placement and wording of the new requirements, and the readings below
- **Resolves:** the owner's request of 2026-10-07 to verify that the opportunity-universe and trading-economics principles are represented in the canonical requirements and that nothing contradicts them

## Context

On 2026-10-07, during Stage 1, the owner asked for a repository-backed status report and restated the platform's opportunity and economics principles "so that it is preserved in the canonical project knowledge and is not accidentally weakened during implementation": whole-universe discovery with aggressive breadth, depth, and speed; continuous scanning; competition between opportunities; no percentage floor or ceiling, with unusually large opportunities verified rather than rejected or trusted; small opportunities that accumulate; true net economics; dynamic capital allocation; no forced trading, quota, chasing, or revenge trading; active-trade protection; missed-opportunity analysis; strict risk and execution validation; no unsafe fast path. The owner asked for contradictions, duplicates, and missing rules to be corrected where the resolution is already established, and for anything needing the owner to be put to the owner.

The [opportunity and economics audit](../traceability/opportunity-economics-audit-2026-10-07.md) compared each principle with the specifications, the registers, the roadmap, and the code. Most were already canonical, from Handoff Part 1 (§08, §09, §13 to §17, §20, §21, §23), Part 2, Part 3 (§386 to §394, §416 to §420, §437 to §440), and DEC-014. No contradiction was found. Ten statements of the directive were made by no requirement, or only in part (the audit's "Gaps").

## Decision

1. **The directive is applied through the canonical requirements,** not through its text, which [DEC-041](DEC-041-preserve-opportunity-and-economics-directive.md) preserved word for word as [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), a HISTORICAL source.
2. **The principles already canonical stay where they are.** The audit maps each of the directive's twenty points to its requirements; none is restated.
3. **Ten requirements are added**, each to the specification that owns its subject:

| Requirement | What it adds | Owner |
|---|---|---|
| OPP-021 | Scanning does not stop at a found opportunity | Opportunity Detection Engine (SYS-05) |
| OPP-022 | Search prioritization by value is a search order only, never a floor, quota, target, stopping condition, or universe restriction | SYS-05 |
| TNP-027 | No per-opportunity percentage ceiling (TNP-012 and TNP-026 cover the daily ceiling) | True Net-Profit Engine (SYS-06) |
| TNP-028 | An unusually large apparent opportunity gets additional validation; it is neither rejected nor executed for its size (V-41) | SYS-06 |
| TNP-029 | Economics across sizes: minimum efficient, optimal, and maximum efficient size | SYS-06 |
| TNP-030 | Further economic terms: partial fills, failed or rejected orders, capital lock duration, venue reliability, counterparty and custody exposure; the result in money and relative to capital | SYS-06 |
| CAP-047 | No "highest percentage wins" rule; further ranking considerations | Global Capital Authority (SYS-07) |
| CAP-048 | Allocation sized by the opportunity: no tiny allocations for artificial diversification, no full deployment because an opportunity appears | SYS-07 |
| CAP-049 | Intervening in an active trade only on predefined material conditions, with hysteresis, by the position's owner or the Risk Engine's emergency handling (V-42) | SYS-07 |
| PFC-019 | The outcome categories of missed- and false-opportunity analysis | Performance Controller |

4. **Two values are registered** (ARCH-018): V-41, when an apparent opportunity counts as unusually large (OBSERVED, derived per market and strategy; until it is derived, every apparent opportunity gets TNP-028's checks); V-42, the materiality thresholds and hysteresis for intervening in an active trade (POLICY-CONTROLLED PARAMETER, validated with each strategy).
5. **Two system rules are indexed** (ARCH-038): SR-48, economics, not labels: no percentage floor or ceiling; SR-49, active trades are protected from ordinary opportunity competition.

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "'Universe' means … subject to: … capital availability …" | What is searched is the authorized universe of OPP-009, bounded by OPP-013. The directive's further conditions (execution capability, strategy eligibility, policy, risk, capital, operational health, readiness) decide what may be executed; an opportunity they block is still detected and recorded. The directive's own missed-opportunity categories ("detected but unavailable due to capital", "blocked by risk") require this reading. Recorded in the Opportunity Detection Engine's specification |
| "Do not create an arbitrary rule such as 'Below 1% = ignore.'" | Constrains the architecture: no built-in floor. TNP-016 still allows a percentage threshold as a configurable research or filter parameter that never becomes a universal hard rule, and the operator's own explicit policy may restrict trading (PLT-020, RSK-049), as TNP-026 says for a daily ceiling |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement, derived from evidence per feature (V-39), not a minimum profit for each opportunity. Each opportunity's economic eligibility is TNP-020: a true net expected result above zero after the uncertainty margin, which is never a fixed percentage or universal minimum (TNP-019) |
| MKD-013's "outlier corruption" and MKD-008's "impossible prices" | Data is quarantined when validation shows it is invalid: impossible (a price no market can have, such as zero or negative), inconsistent across sources or sequence, or corrupt. A price that is only extreme, and consistent, is not corrupt; it reaches the opportunity engine, where TNP-028 verifies it. Quarantine is never a size limit on opportunities |
| "expected dollar profit" | The expected profit in the quote currency of the trade, which TNP-018 already computes as an amount; "dollar" is read as the account's quote currency |
| "persistent WebSocket connections", "affected-route recalculation" | Covered by TEC-005 and EXA-012 (WebSocket streams and their connections) and PERF-005 (event-driven processing, incremental calculation, connection reuse); no new requirement. They are designed when DATA FOUNDATION is planned |

## Alternatives considered

- **Record the directive without new requirements**, since most of it was already canonical. Not chosen: ten statements were made by no requirement or only in part, and the owner asked for missing rules to be added.
- **Restate every principle in one new document.** Not chosen: it would be a second copy of requirements that already have one canonical home each (constitution Rule 42; master execution constitution §33).
- **Put the unusual-opportunity rule in market data.** Not chosen: data validation stays with market data (MKD-004, MKD-008, MKD-013), but the rule concerns whether an opportunity is eligible, which the True Net-Profit Engine owns (TNP-017, TNP-020); TNP-028 names data validation as one of its steps.

## Consequences

- 734 requirements become 744; no existing requirement changes, so the requirement comparison shows ten added and nothing removed or changed.
- The new requirements belong to the stages of their specifications (DATA FOUNDATION for SYS-05; CORE TRADING FOUNDATION and the trading stages for the others). Like the rest of those stages, their features stay PROPOSED until each stage's plan is approved (DEC-040), and nothing beyond Stage 1 is authorized (DEC-038).
- When each stage is planned, its plan includes tests for these rules: filters and eligibility with small, large, and unusually large opportunities; ranking where the highest percentage is not the best; scanning that continues after a find; an active trade and a better-looking new opportunity; the outcome categories of PFC-019.
```

## The second draft decision record

A decision record of 2026-10-12, numbered DEC-043 in the draft; that number has since been used for another decision. Original: 9,338 bytes, sha256 `05d3c4a5f775aaa2a59b59eeb2a33b713f89a9cdb1c74bb53a39b4153f41af78`.

```text
# DEC-043 — The owner's opportunity-universe and economics directive applied: principles confirmed, gaps closed

- **Status:** ACCEPTED
- **Date:** 2026-10-12
- **Decided by:** project owner (the directive, [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), which also asks for missing rules to be added where the resolution is established); the builder's: the mapping to existing requirements, the placement and wording of the new requirements, which follow the directive's own words, and the readings below
- **Resolves:** the owner's request of 2026-10-07 to verify that the opportunity-universe and trading-economics principles are represented in the canonical requirements and that nothing contradicts them

## Context

On 2026-10-07, during Stage 1, the owner asked for a repository-backed status report and restated the platform's opportunity and economics principles "so that it is preserved in the canonical project knowledge and is not accidentally weakened during implementation": whole-universe discovery with aggressive breadth, depth, and speed; continuous scanning; competition between opportunities; no percentage floor or ceiling, with unusually large opportunities verified rather than rejected or trusted; small opportunities that accumulate; true net economics; dynamic capital allocation; no forced trading, quota, chasing, or revenge trading; active-trade protection; missed-opportunity analysis; strict risk and execution validation; no unsafe fast path. The owner asked for contradictions, duplicates, and missing rules to be corrected where the resolution is already established, and for anything needing the owner to be put to the owner.

The [opportunity and economics audit](../traceability/opportunity-economics-audit-2026-10-12.md) compared each principle with the specifications, the registers, the roadmap, and the code. Most were already canonical, from Handoff Part 1 (§08, §09, §13 to §17, §20, §21, §23), Part 2, Part 3 (§386 to §394, §416 to §420, §437 to §440), and DEC-014. No contradiction was found. Ten statements of the directive were made by no requirement, or only in part (the audit's "Gaps").

## Decision

1. **The directive is applied through the canonical requirements,** not through its text, which [DEC-041](DEC-041-preserve-opportunity-and-economics-directive.md) preserved word for word as [owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md), a HISTORICAL source.
2. **The principles already canonical stay where they are.** The audit maps each of the directive's twenty points to its requirements; none is restated.
3. **Ten requirements are added**, each to the specification that owns its subject:

| Requirement | What it adds | Owner |
|---|---|---|
| OPP-021 | Scanning does not stop at a found opportunity | Opportunity Detection Engine (SYS-05) |
| OPP-022 | Search prioritization by value is a search order only, never a floor, quota, target, stopping condition, or universe restriction | SYS-05 |
| TNP-027 | No per-opportunity percentage ceiling (TNP-012 and TNP-026 cover the daily ceiling) | True Net-Profit Engine (SYS-06) |
| TNP-028 | An unusually large apparent opportunity gets additional validation; it is neither rejected nor executed for its size (V-41) | SYS-06 |
| TNP-029 | Economics across sizes: minimum efficient, optimal, and maximum efficient size | SYS-06 |
| TNP-030 | Further economic terms: partial fills, failed or rejected orders, capital lock duration, venue reliability, counterparty and custody exposure; the result in money and relative to capital | SYS-06 |
| CAP-047 | No "highest percentage wins" rule; further ranking considerations | Global Capital Authority (SYS-07) |
| CAP-048 | Allocation sized by the opportunity: no tiny allocations for artificial diversification, no full deployment because an opportunity appears | SYS-07 |
| CAP-049 | Intervening in an active trade only on predefined material conditions, with hysteresis, by the position's owner or the Risk Engine's emergency handling (V-42) | SYS-07 |
| PFC-019 | The outcome categories of missed- and false-opportunity analysis | Performance Controller |

4. **Two values are registered** (ARCH-018): V-41, when an apparent opportunity counts as unusually large (OBSERVED, derived per market and strategy; until it is derived, every apparent opportunity gets TNP-028's checks); V-42, the materiality thresholds and hysteresis for intervening in an active trade (POLICY-CONTROLLED PARAMETER, validated with each strategy).
5. **Two system rules are indexed** (ARCH-038): SR-48, economics, not labels: no percentage floor or ceiling; SR-49, active trades are protected from ordinary opportunity competition.
6. **Each new requirement is mapped to its roadmap stage** (the roadmap's "Additions of 2026-10-12 by stage"): OPP-021 and OPP-022 to DATA FOUNDATION; TNP-027 to TNP-030, CAP-047 to CAP-049, SR-48, and SR-49 to CORE TRADING FOUNDATION; PFC-019 to DIRECTIONAL TRADING, with the Performance Controller's core.
7. **The owner's [requirement drafting and anti-drift rules](../builder/requirement-drafting-and-anti-drift-rules.md) were applied** ([DEC-042](DEC-042-adopt-requirement-drafting-and-anti-drift-rules.md)): each drafted item was classified, its provenance and owner stated, and the existing requirement it strengthens named; no existing requirement's text changes. The classification and the final reconciliation report (Rule 23) are in the audit record.

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "'Universe' means … subject to: … capital availability …" | What is searched is the authorized universe of OPP-009, bounded by OPP-013. The directive's further conditions (execution capability, strategy eligibility, policy, risk, capital, operational health, readiness) decide what may be executed; an opportunity they block is still detected and recorded. The directive's own missed-opportunity categories ("detected but unavailable due to capital", "blocked by risk") require this reading. Recorded in the Opportunity Detection Engine's specification |
| "Do not create an arbitrary rule such as 'Below 1% = ignore.'" | Constrains the architecture: no built-in floor. TNP-016 still allows a percentage threshold as a configurable research or filter parameter that never becomes a universal hard rule, and the operator's own explicit policy may restrict trading (PLT-020, RSK-049), as TNP-026 says for a daily ceiling |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement, derived from evidence per feature (V-39), not a minimum profit for each opportunity. Each opportunity's economic eligibility is TNP-020: a true net expected result above zero after the uncertainty margin, which is never a fixed percentage or universal minimum (TNP-019) |
| MKD-013's "outlier corruption" and MKD-008's "impossible prices" | Data is quarantined when validation shows it is invalid: impossible (a price no market can have, such as zero or negative), inconsistent across sources or sequence, or corrupt. A price that is only extreme, and consistent, is not corrupt; it reaches the opportunity engine, where TNP-028 verifies it. Quarantine is never a size limit on opportunities |
| "expected dollar profit" | The expected profit in the quote currency of the trade, which TNP-018 already computes as an amount; "dollar" is read as the account's quote currency |
| "persistent WebSocket connections", "affected-route recalculation" | Covered by TEC-005 and EXA-012 (WebSocket streams and their connections) and PERF-005 (event-driven processing, incremental calculation, connection reuse); no new requirement. They are designed when DATA FOUNDATION is planned |

## Alternatives considered

- **Record the directive without new requirements**, since most of it was already canonical. Not chosen: ten statements were made by no requirement or only in part, and the owner asked for missing rules to be added.
- **Restate every principle in one new document.** Not chosen: it would be a second copy of requirements that already have one canonical home each (constitution Rule 42; master execution constitution §33).
- **Put the unusual-opportunity rule in market data.** Not chosen: data validation stays with market data (MKD-004, MKD-008, MKD-013), but the rule concerns whether an opportunity is eligible, which the True Net-Profit Engine owns (TNP-017, TNP-020); TNP-028 names data validation as one of its steps.

## Consequences

- 734 requirements become 744; no existing requirement changes, so the requirement comparison shows ten added and nothing removed or changed.
- The new requirements belong to the stages of their specifications (DATA FOUNDATION for SYS-05; CORE TRADING FOUNDATION and the trading stages for the others). Like the rest of those stages, their features stay PROPOSED until each stage's plan is approved (DEC-040), and nothing beyond Stage 1 is authorized (DEC-038).
- When each stage is planned, its plan includes tests for these rules: filters and eligibility with small, large, and unusually large opportunities; ranking where the highest percentage is not the best; scanning that continues after a find; an active trade and a better-looking new opportunity; the outcome categories of PFC-019.
```

## The first draft script

The script that would have applied the first decision record's changes to the specifications; never run on the repository. Original: 12,775 bytes, sha256 `cbd5981e8d4a600ae92d7c5cb75b849e35dd26b9ef946d4b1197e5ffbfddc55f`. One line is redacted: the repository's local path in `ROOT = Path(...)` is shown as `<repository root>` (plan section 9, item 4: no local path in the repository); the sha256 of the text as shown is `5058d07e3b779f6c1aa33284cde01fe86ada50c4235ea1f426f8828251a566aa`.

```text
"""Apply DEC-042 (the owner's opportunity-universe and economics directive) to the specifications."""

from pathlib import Path

ROOT = Path("<repository root>")
INTRO = (
    "New requirements from the owner's directive of 2026-10-07 ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)), "
    "applied by [DEC-042](../decisions/DEC-042-opportunity-universe-and-economics.md). The directive restates principles that are already canonical; "
    "each is mapped to its existing requirements in the [opportunity and economics audit](../traceability/opportunity-economics-audit-2026-10-07.md). "
    "Only what was not yet stated anywhere is added here."
)


def insert_before(path: Path, marker: str, text: str) -> None:
    s = path.read_text(encoding="utf-8")
    assert s.count(marker) == 1, (path, marker)
    path.write_text(s.replace(marker, text + marker), encoding="utf-8")


# Opportunity Detection Engine
insert_before(
    ROOT / "docs/systems/opportunity-detection.md",
    "## Boundary (§92)",
    "## The owner's directive applied (2026-10-07)\n\n" + INTRO + "\n\n"
    "- **OPP-021** Scanning does not stop at a found opportunity · CONSTRAINT · DEC-042 — Opportunity discovery continues across the authorized universe whatever has already been found. Finding an opportunity of any size (5%, 3%, 1%, or less) is not a reason to stop searching or to ignore smaller opportunities. Computational resources are managed within the bounds of OPP-013 and the backpressure controls of PERF-014 and PERF-021.\n"
    "- **OPP-022** Search prioritization is not a floor · CONSTRAINT · DEC-042 — The system may search and evaluate higher-value candidates first (for example 5%, then 3%, 2%, 1.5%, 1%, 0.9%, 0.5%, 0.4%, 0.2%, 0.1%, and onward across the valid range). This order is a search priority only. It must never become: a minimum profit requirement; a trade quota; a daily target; a stopping condition; a universe restriction; a reason to ignore smaller opportunities.\n\n"
    "**Breadth, depth, and speed (the directive's terms; OPP-017).** Breadth is OPP-001, OPP-003, OPP-009, OPP-013, and OPP-018. Depth is evaluation beyond the headline price difference: the order book walked at the intended size (TNP-018) and across sizes (TNP-029); multi-leg, triangular, and cross-exchange routes (TAR-001 to TAR-004, XAR-001 to XAR-004); directional opportunities (DIR-001); liquidity (TNP-024); capital requirements and competing opportunities (CAP-043); net economics after costs (TNP-018); opportunity lifetime (TNP-023, TNP-025); capacity, capital reuse, and venue reliability (TNP-029, TNP-030, CAP-047). Speed is OPP-012, PERF-005 (event-driven, asynchronous, and parallel processing, efficient data structures, caching, precomputation, incremental calculation, connection reuse), TEC-005 and EXA-012 (WebSocket streams and connection management), PERF-014, PERF-016, PERF-021 (backpressure, resource isolation), and PERF-010 (measured latency), always within PERF-023 (no unsafe fast path). Recalculating only the routes an update affects is PERF-005's incremental calculation; it is designed with the opportunity filter when DATA FOUNDATION is planned.\n\n"
    "**The universe and its conditions.** The directive's universe is \"the complete set of opportunities the platform is currently authorized and technically capable of evaluating\". What is searched is OPP-009, bounded by OPP-013 (data quality, liquidity, venue availability, resource constraints, risk policy, market eligibility). The directive's further conditions (execution capability, strategy eligibility, policy, risk controls, capital availability, operational health, instrument and exchange readiness) decide what may be executed (OPP-019, CAP-016, RSK-001, the Readiness System); an opportunity they block is still detected and recorded, as the directive's own missed-opportunity categories require (\"detected but unavailable due to capital\", \"blocked by risk\"; PFC-012, PFC-016, PFC-019, OPP-015).\n\n",
)

# True Net-Profit Engine
insert_before(
    ROOT / "docs/systems/true-net-profit-engine.md",
    "## Boundary (§92)",
    "## The owner's directive applied (2026-10-07)\n\n" + INTRO + "\n\n"
    "- **TNP-027** No per-opportunity percentage ceiling · CONSTRAINT · DEC-042 — The platform must not impose an upper percentage ceiling on a single opportunity, such as \"only trade opportunities up to 1%\" or \"never consider anything above 5%\". An opportunity of 5%, 10%, 20%, or more that survives the complete evaluation is eligible like any other (TNP-006). 5% is not a target, a minimum, a quota, or an expected daily return (TNP-014).\n"
    "- **TNP-028** Unusually large opportunities are verified, neither rejected nor trusted for their size · CONFIRMED REQUIREMENT · DEC-042 — An apparent opportunity that is unusually large for its market triggers additional validation, because it may be a genuine market dislocation or a temporary liquidity imbalance, or it may come from stale or incorrect market data, an exchange malfunction, a symbol mismatch, a precision problem, a withdrawal or deposit restriction, an abnormal spread, insufficient liquidity, an execution impossibility, market manipulation, temporary venue degradation, or another data or execution anomaly. The order is: verify aggressively → validate the data → validate executability → validate true net economics → validate risk → execute only if every condition passes. It is never rejected merely because it is large, and never executed merely because it is large. What counts as unusually large is V-41.\n"
    "- **TNP-029** Economics across sizes · SYSTEM REQUIREMENT · DEC-042 — This engine evaluates an opportunity's true net expected result across the sizes at which it could be executed, so that each opportunity may have a minimum efficient size, an optimal size, and a maximum efficient size (its capacity), set by liquidity, slippage, market impact, and execution capacity. The Global Capital Authority allocates within that range (CAP-048), and the Risk Engine sets the final size (CAP-016, RSK-011).\n"
    "- **TNP-030** Additional terms of executable economics · SYSTEM REQUIREMENT · DEC-042 — In addition to the terms of TNP-018 and the time and probability terms of TNP-023 and TNP-025, executable economics account, where applicable, for: the expected effect of partial fills and of failed or rejected orders; capital lock duration; venue reliability; counterparty and custody exposure. The result is given as an amount in quote currency (TNP-018) as well as relative to the capital used, so that expected profit in money and in percentage can both be compared (TNP-021).\n\n",
)

# Global Capital Authority
insert_before(
    ROOT / "docs/systems/capital-management.md",
    "## Boundary (§92)",
    "## The owner's directive applied (2026-10-07)\n\n" + INTRO + "\n\n"
    "- **CAP-047** No \"highest percentage wins\" rule · CONSTRAINT · DEC-042 — Ranking competing opportunities must not reduce to choosing the highest percentage. A large headline opportunity may rank below a smaller one with better liquidity, slippage, execution probability, capital requirement, or risk, and several smaller high-quality opportunities may together be worth more than one large but unreliable opportunity. In addition to the dimensions of CAP-043 and TNP-015, ranking may consider: expected profit in quote currency; capture probability; capital lock duration; capital reuse; opportunity capacity; opportunity expiration; opportunity scarcity; historical reliability; strategy health.\n"
    "- **CAP-048** Opportunity-driven allocation size · CONSTRAINT · DEC-042 — When a strong opportunity appears, this system may allocate the capital the opportunity can usefully take, within its size range (TNP-029) and subject to: risk limits; liquidity; execution capacity; exposure limits; reserves; capital availability; opportunity capacity; strategy limits; exchange limits; portfolio constraints. It must neither divide capital into tiny allocations merely for artificial diversification nor deploy all capital merely because an opportunity appears.\n"
    "- **CAP-049** Intervening in an active trade · CONSTRAINT · DEC-042 — A newer opportunity is never by itself a reason to intervene in an active trade (CAP-014). An active trade is changed only when predefined material conditions justify an action such as CONTINUE, REDUCE, HEDGE, CANCEL, UNWIND, or EXIT. The action is decided by the system that owns the position (DIR-004 for directional positions; the arbitrage systems for their legs, TAR-004) and passes through this system, the Risk Engine, and the Execution Engine (DIR-003), or it is the Risk Engine's emergency handling (RSK-017). Materiality thresholds and hysteresis prevent unstable switching between actions (V-42).\n\n",
)

# Performance Controller
insert_before(
    ROOT / "docs/systems/performance-controller.md",
    "## Boundary (§92)",
    "## The owner's directive applied (2026-10-07)\n\n" + INTRO + "\n\n"
    "- **PFC-019** Opportunity outcome categories · SYSTEM REQUIREMENT · DEC-042 — In addition to the reasons of PFC-012 and PFC-016, missed- and false-opportunity analysis distinguishes, where measurable: detected and executed; detected and rejected, by reason (risk, liquidity, execution confidence, capital, and the others); detected but expired; disappeared before execution; missed because of system, data, or venue latency; never detected, found afterwards in recorded market data. The results are used to improve data quality, detection, filtering, execution, latency, capital allocation, strategy quality, and system performance, through the validated change processes and never by weakening safety controls (RSK-044, PFC-018).\n\n",
)

# Values register
path = ROOT / "docs/requirements/values-register.md"
s = path.read_text(encoding="utf-8")
anchor = "| V-40 | Decimal precision of financial calculations"
i = s.index(anchor)
j = s.index("\n", i)
rows = (
    "\n| V-41 | When an apparent opportunity counts as unusually large for its market and gets the additional validation of TNP-028 | TNP-028 | OBSERVED (derived per market and strategy from observed opportunity distributions) | Not derived yet | It only adds validation; it is never a rejection threshold or a ceiling (TNP-027). Until it is derived, every apparent opportunity gets TNP-028's additional checks |"
    "\n| V-42 | Materiality thresholds and hysteresis for intervening in an active trade | CAP-049 | POLICY-CONTROLLED PARAMETER (set with each strategy version and validated through its lifecycle, STR-001) | Not set | Until set for a strategy, its positions change only through its validated exit rules (DIR-004) and the Risk Engine's handling (RSK-017); a newer opportunity never interrupts them (CAP-014) |"
)
path.write_text(s[:j] + rows + s[j:], encoding="utf-8")
print("applied")

# System Rules Register
path = ROOT / "docs/requirements/system-rules-register.md"
s = path.read_text(encoding="utf-8")
anchor = "| SR-47 | No unsafe fast path |"
i = s.index(anchor)
j = s.index("\n", i)
rows = (
    "\n| SR-48 | Economics, not labels: no percentage floor or ceiling | TNP-005, TNP-007, TNP-016, TNP-027, TNP-028, OPP-022 | CONSTRAINT | §14, §17, DEC-042 | SYS-06 True Net-Profit Engine | SYS-05 (opportunity filter, search order), SYS-07 (ranking), SYS-12 (explicit operator policy only) | Economic eligibility (TNP-020); the opportunity filter (OPP-005); design review of every filter, ranking, and policy default | Block the design; a filter that rejects a positive-net opportunity, or a large one, for its percentage alone is a defect | Filter, eligibility, and ranking tests with small, ordinary, large, and unusually large opportunities | DOCUMENTED |"
    "\n| SR-49 | Active trades are protected from ordinary opportunity competition | CAP-014, CAP-049, CAP-015 | CONSTRAINT | §23, DEC-042 | SYS-07 Global Capital Authority | SYS-17, SYS-18, SYS-19 (the positions' owners), SYS-09 (emergency handling, RSK-017), SYS-10 | Capital allocation; intervention decisions by the position's owner through the Risk Engine | The intervention is refused; the new opportunity is rejected or waits (CAP-015) | Allocation tests with an active trade and a better-looking new opportunity; hysteresis tests | DOCUMENTED |"
)
s = s[:j] + rows + s[j:]
old = "SR-02 rests on RSK-049 since [DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)."
assert s.count(old) == 1
s = s.replace(old, old + " SR-48 and SR-49 added by [DEC-042](../decisions/DEC-042-opportunity-universe-and-economics.md) (2026-10-07).")
path.write_text(s, encoding="utf-8")
print("rules added")
```

## The second draft script

The script that would have applied the second decision record's changes, among them the drafted requirements, system rules, and values; never run on the repository. Original: 14,139 bytes, sha256 `6d1cdda26fa10549536b60559dca75255d4600670c9c48505473a688d3d7e445`. One line is redacted: the repository's local path in `ROOT = Path(...)` is shown as `<repository root>` (plan section 9, item 4: no local path in the repository); the sha256 of the text as shown is `5cba9ac2730c449f313cdbe7c1ba45554b37408465396b5b9d82af18697a947d`.

```text
"""Apply DEC-043 (the owner's opportunity-universe and economics directive) to the specifications."""

from pathlib import Path

ROOT = Path("<repository root>")
INTRO = (
    "New requirements from the owner's directive of 2026-10-07 ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)), "
    "applied by [DEC-043](../decisions/DEC-043-opportunity-universe-and-economics.md). The directive restates principles that are already canonical; "
    "each is mapped to its existing requirements in the [opportunity and economics audit](../traceability/opportunity-economics-audit-2026-10-12.md). "
    "Only what was not yet stated anywhere is added here."
)


def insert_before(path: Path, marker: str, text: str) -> None:
    s = path.read_text(encoding="utf-8")
    assert s.count(marker) == 1, (path, marker)
    path.write_text(s.replace(marker, text + marker), encoding="utf-8")


# Opportunity Detection Engine
insert_before(
    ROOT / "docs/systems/opportunity-detection.md",
    "## Boundary (§92)",
    "## The owner's directive of 2026-10-07 applied\n\n" + INTRO + "\n\n"
    "- **OPP-021** Scanning does not stop at a found opportunity · CONSTRAINT · DEC-043 — In addition to OPP-001 and OPP-018, opportunity discovery continues across the authorized universe whatever has already been found. Finding an opportunity of any size (5%, 3%, 1%, or less) is not a reason to stop searching or to ignore smaller opportunities. Computational resources are managed within the bounds of OPP-013 and the backpressure controls of PERF-014 and PERF-021.\n"
    "- **OPP-022** Search prioritization is not a floor · CONSTRAINT · DEC-043 — The system may search and evaluate higher-value candidates first (for example 5%, then 3%, 2%, 1.5%, 1%, 0.9%, 0.5%, 0.4%, 0.2%, 0.1%, and onward across the valid range). This order is a search priority only. It must never become: a minimum profit requirement; a trade quota; a daily target; a stopping condition; a universe restriction; a reason to ignore smaller opportunities.\n\n"
    "**Breadth, depth, and speed (the directive's terms; OPP-017).** Breadth is OPP-001, OPP-003, OPP-009, OPP-013, and OPP-018. Depth is evaluation beyond the headline price difference: the order book walked at the intended size (TNP-018) and across sizes (TNP-029); multi-leg, triangular, and cross-exchange routes (TAR-001 to TAR-004, XAR-001 to XAR-004); directional opportunities (DIR-001); liquidity (TNP-024); capital requirements and competing opportunities (CAP-043); net economics after costs (TNP-018); opportunity lifetime (TNP-023, TNP-025); capacity, capital reuse, and venue reliability (TNP-029, TNP-030, CAP-047). Speed is OPP-012, PERF-005 (event-driven, asynchronous, and parallel processing, efficient data structures, caching, precomputation, incremental calculation, connection reuse), TEC-005 and EXA-012 (WebSocket streams and connection management), PERF-014, PERF-016, PERF-021 (backpressure, resource isolation), and PERF-010 (measured latency), always within PERF-023 (no unsafe fast path). Recalculating only the routes an update affects is PERF-005's incremental calculation; it is designed with the opportunity filter when DATA FOUNDATION is planned.\n\n"
    "**The universe and its conditions.** The directive's universe is \"the complete set of opportunities the platform is currently authorized and technically capable of evaluating\". What is searched is OPP-009, bounded by OPP-013 (data quality, liquidity, venue availability, resource constraints, risk policy, market eligibility). The directive's further conditions (execution capability, strategy eligibility, policy, risk controls, capital availability, operational health, instrument and exchange readiness) decide what may be executed (OPP-019, CAP-016, RSK-001, the Readiness System); an opportunity they block is still detected and recorded, as the directive's own missed-opportunity categories require (\"detected but unavailable due to capital\", \"blocked by risk\"; PFC-012, PFC-016, PFC-019, OPP-015).\n\n",
)

# True Net-Profit Engine
insert_before(
    ROOT / "docs/systems/true-net-profit-engine.md",
    "## Boundary (§92)",
    "## The owner's directive of 2026-10-07 applied\n\n" + INTRO + "\n\n"
    "- **TNP-027** No per-opportunity percentage ceiling · CONSTRAINT · DEC-043 — In addition to TNP-012 and TNP-026, which concern a daily ceiling, the platform must not impose an upper percentage ceiling on a single opportunity, such as \"only trade opportunities up to 1%\" or \"never consider anything above 5%\". An opportunity of 5%, 10%, 20%, or more that survives the complete evaluation, including TNP-028's, is eligible like any other (TNP-006).\n"
    "- **TNP-028** Unusually large opportunities are verified, neither rejected nor trusted for their size · CONFIRMED REQUIREMENT · DEC-043 — An apparent opportunity that is unusually large for its market triggers additional validation, because it may be a genuine market dislocation or a temporary liquidity imbalance, or it may come from stale or incorrect market data, an exchange malfunction, a symbol mismatch, a precision problem, a withdrawal or deposit restriction, an abnormal spread, insufficient liquidity, an execution impossibility, market manipulation, temporary venue degradation, or another data or execution anomaly. The order is: verify aggressively → validate the data → validate executability → validate true net economics → validate risk → execute only if every condition passes. It is never rejected merely because it is large, and never executed merely because it is large. What counts as unusually large is V-41.\n"
    "- **TNP-029** Economics across sizes · SYSTEM REQUIREMENT · DEC-043 — This engine evaluates an opportunity's true net expected result across the sizes at which it could be executed, so that each opportunity may have a minimum efficient capital, an optimal capital, and a maximum efficient capital (its capacity), set by liquidity, slippage, market impact, and execution capacity, using the Quantitative Engine's slippage and sizing calculations (QNT-004). The Global Capital Authority allocates within that range (CAP-048), and the Risk Engine sets the final size (CAP-016, RSK-011).\n"
    "- **TNP-030** Additional terms of executable economics · SYSTEM REQUIREMENT · DEC-043 — In addition to the terms of TNP-018 and the time and probability terms of TNP-023 and TNP-025, executable economics account, where applicable, for: the expected effect of partial fills and of failed or rejected orders; capital lock duration; venue reliability; counterparty and custody exposure. The result is given as an amount in quote currency (TNP-018) as well as relative to the capital used, so that expected profit in money and in percentage can both be compared (TNP-021).\n\n",
)

# Global Capital Authority
insert_before(
    ROOT / "docs/systems/capital-management.md",
    "## Boundary (§92)",
    "## The owner's directive of 2026-10-07 applied\n\n" + INTRO + "\n\n"
    "- **CAP-047** No \"highest percentage wins\" rule · CONSTRAINT · DEC-043 — Ranking competing opportunities must not reduce to choosing the highest percentage. A large headline opportunity may rank below a smaller one with better liquidity, slippage, execution probability, capital requirement, or risk, and several smaller high-quality opportunities may together be worth more than one large but unreliable opportunity. In addition to the dimensions of CAP-043 and TNP-015, ranking may consider: expected profit in quote currency; capture probability; capital lock duration; capital reuse; opportunity capacity; opportunity expiration; opportunity scarcity; historical reliability; strategy health.\n"
    "- **CAP-048** Opportunity-driven allocation size · CONSTRAINT · DEC-043 — When a strong opportunity appears, this system may allocate the capital the opportunity can usefully take, within its capital range (TNP-029) and subject to: risk limits; liquidity; execution capacity; exposure limits; reserves; capital availability; opportunity capacity; strategy limits; exchange limits; portfolio constraints. It must neither divide capital into tiny allocations merely for artificial diversification nor deploy all capital merely because an opportunity appears.\n"
    "- **CAP-049** Intervening in an active trade · CONSTRAINT · DEC-043 — In addition to CAP-014, an active trade is changed only when predefined material conditions justify an action such as CONTINUE, REDUCE, HEDGE, CANCEL, UNWIND, or EXIT. The action is decided by the system that owns the position (DIR-004 for directional positions; the arbitrage systems for their legs, TAR-004) and passes through this system, the Risk Engine, and the Execution Engine (DIR-003), or it is the Risk Engine's emergency handling (RSK-017). Materiality thresholds and hysteresis prevent unstable switching between actions (V-42).\n\n",
)

# Performance Controller
insert_before(
    ROOT / "docs/systems/performance-controller.md",
    "## Boundary (§92)",
    "## The owner's directive of 2026-10-07 applied\n\n" + INTRO + "\n\n"
    "- **PFC-019** Opportunity outcome categories · SYSTEM REQUIREMENT · DEC-043 — In addition to the reasons of PFC-012 and PFC-016, missed- and false-opportunity analysis distinguishes, where measurable: detected and executed; detected and rejected, by reason (risk, liquidity, execution confidence, capital, and the others); detected but expired; disappeared before execution; missed because of system, data, or venue latency; never detected, found afterwards in recorded market data. The results are used to improve data quality, detection, filtering, execution, latency, capital allocation, strategy quality, and system performance, through the validated change processes and never by weakening safety controls (RSK-044, PFC-018).\n\n",
)

# Values register
path = ROOT / "docs/requirements/values-register.md"
s = path.read_text(encoding="utf-8")
anchor = "| V-40 | Decimal precision of financial calculations"
i = s.index(anchor)
j = s.index("\n", i)
rows = (
    "\n| V-41 | When an apparent opportunity counts as unusually large for its market and gets the additional validation of TNP-028 | TNP-028 | OBSERVED (derived per market and strategy from observed opportunity distributions) | Not derived yet | It only adds validation; it is never a rejection threshold or a ceiling (TNP-027). Until it is derived, every apparent opportunity gets TNP-028's additional checks |"
    "\n| V-42 | Materiality thresholds and hysteresis for intervening in an active trade | CAP-049 | POLICY-CONTROLLED PARAMETER (set with each strategy version and validated through its lifecycle, STR-001) | Not set | Until set for a strategy, its positions change only through its validated exit rules (DIR-004) and the Risk Engine's handling (RSK-017); a newer opportunity never interrupts them (CAP-014) |"
)
path.write_text(s[:j] + rows + s[j:], encoding="utf-8")
print("applied")

# System Rules Register
path = ROOT / "docs/requirements/system-rules-register.md"
s = path.read_text(encoding="utf-8")
anchor = "| SR-47 | No unsafe fast path |"
i = s.index(anchor)
j = s.index("\n", i)
rows = (
    "\n| SR-48 | Economics, not labels: no percentage floor or ceiling | TNP-005, TNP-007, TNP-016, TNP-027, TNP-028, OPP-022 | CONSTRAINT | §14, §17, DEC-043 | SYS-06 True Net-Profit Engine | SYS-05 (opportunity filter, search order), SYS-07 (ranking), SYS-12 (explicit operator policy only) | Economic eligibility (TNP-020); the opportunity filter (OPP-005); design review of every filter, ranking, and policy default | Block the design; a filter that rejects a positive-net opportunity, or a large one, for its percentage alone is a defect | Filter, eligibility, and ranking tests with small, ordinary, large, and unusually large opportunities | DOCUMENTED |"
    "\n| SR-49 | Active trades are protected from ordinary opportunity competition | CAP-014, CAP-049, CAP-015 | CONSTRAINT | §23, DEC-043 | SYS-07 Global Capital Authority | SYS-17, SYS-18, SYS-19 (the positions' owners), SYS-09 (emergency handling, RSK-017), SYS-10 | Capital allocation; intervention decisions by the position's owner through the Risk Engine | The intervention is refused; the new opportunity is rejected or waits (CAP-015) | Allocation tests with an active trade and a better-looking new opportunity; hysteresis tests | DOCUMENTED |"
)
s = s[:j] + rows + s[j:]
old = "SR-02 rests on RSK-049 since [DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)."
assert s.count(old) == 1
s = s.replace(old, old + " SR-48 and SR-49 added by [DEC-043](../decisions/DEC-043-opportunity-universe-and-economics.md) (2026-10-07).")
path.write_text(s, encoding="utf-8")
print("rules added")

# Roadmap: each new requirement mapped to its stage (Rule 14 of the drafting rules).
path = ROOT / "docs/roadmap/roadmap.md"
s = path.read_text(encoding="utf-8")
anchor = "PLT-029 (the platform operates without Claude Code) is platform-wide:"
assert s.count(anchor) == 1
section = (
    "### Additions of 2026-10-12 by stage ([DEC-043](../decisions/DEC-043-opportunity-universe-and-economics.md))\n\n"
    "| # | Stage | Added |\n"
    "|---|---|---|\n"
    "| 2 | DATA FOUNDATION | Scanning does not stop at a found opportunity; search prioritization is never a floor, quota, or stopping condition (OPP-021, OPP-022) |\n"
    "| 3 | CORE TRADING FOUNDATION | No percentage ceiling on a single opportunity; unusually large opportunities verified, neither rejected nor trusted for their size (V-41); economics across capital sizes; further economic terms (TNP-027 to TNP-030); no \"highest percentage wins\" rule; allocation sized by the opportunity; intervening in an active trade (V-42) (CAP-047 to CAP-049); SR-48, SR-49 |\n"
    "| 4 | DIRECTIONAL TRADING | Opportunity outcome categories in missed- and false-opportunity analysis (PFC-019), with the Performance Controller's core |\n\n"
)
path.write_text(s.replace(anchor, section + anchor), encoding="utf-8")
print("roadmap rows added")
```
