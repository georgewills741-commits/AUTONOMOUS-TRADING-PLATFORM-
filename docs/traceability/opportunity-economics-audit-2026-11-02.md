# Opportunity-Universe and Economics Audit — 2026-11-02

> **Status:** ACTIVE record of the audit the owner asked for on 2026-10-07 ([owner decisions 8](../handoffs/owner-decisions-08-opportunity-universe-and-economics.md)), item 4 of the [project state](../project-state.md)'s "Next approved step": are the opportunity-universe and trading-economics principles represented in the canonical requirements, and does anything contradict them? Preserved by [DEC-041](../decisions/DEC-041-preserve-opportunity-and-economics-directive.md); applied by [DEC-058](../decisions/DEC-058-opportunity-universe-and-economics.md). The change also reconciles the last change's temporary backup with that change's commit, `a52e4ad`, and retires its branch ([DEC-057](../decisions/DEC-057-progress-continuity-no-loss-and-recovery.md), decision 6). Its three gates: "Final status and remaining issues". Format: [traceability README](README.md).

## Identity

- **Date:** 2026-11-02
- **Stage:** 1 — FOUNDATION, after checkpoint D, item 4 of "Next approved step". This audit writes documentation only; it starts no later stage's work ([DEC-038](../decisions/DEC-038-stage-1-plan-approved.md))
- **Starts from:** commit `a52e4ad` on branch `claude/code-builder-constitution-rrewgf`, equal to the remote. This record's own commit is entered in the project state's checkpoint log by the next change.
- **Request:** the owner's message of 2026-10-07, preserved as owner decisions 8; the order of work: [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md), decision 2
- **Rules:** the owner's requirement drafting rules ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)), as [DEC-051](../decisions/DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md) reads them, with its reading of a refined requirement corrected on 2026-11-02 (its "Later changes")
- **Temporary backup** (DEC-057, decision 4): the work was pushed to `claude/unverified-backup-item-4` from 2026-11-02, 20:55 UTC, as soon as it existed, and again as it changed. Each commit carries the seven labels of [DEC-042](../decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md) (decision 4) and the emergency checkpoint record of master execution constitution §132. Its reconciliation with this change's commit is recorded by the next change.

## Scope

**Added:** this record; DEC-058; ten requirements: OPP-021 and OPP-022 in the [Opportunity Detection Engine](../systems/opportunity-detection.md), TNP-027 to TNP-030 in the [True Net-Profit Engine](../systems/true-net-profit-engine.md), CAP-047 to CAP-049 in [capital management](../systems/capital-management.md), PFC-019 in the [Performance Controller](../systems/performance-controller.md); V-42 and V-43 in the [values register](../requirements/values-register.md); SR-48 and SR-49 in the [System Rules Register](../requirements/system-rules-register.md); the [roadmap](../roadmap/roadmap.md)'s "Additions of 2026-11-02 by stage".

**Changed:** the generated [registry](../requirements/registry.md); the [drafts index](../drafts/README.md) and the draft's disposition; the project state (the current task, the next action, the stage's convergence, the branches, the decisions, the recent changes, the checkpoint log); the [stage record](stage-01-foundation.md) (the retired backups); the indexes ([documentation index](../README.md), [traceability README](README.md), [decision log](../decisions/README.md)).

**Requirements:** ten added, none removed or changed (check 3).

**Out of scope:** item 5 of "Next approved step"; any later stage's design, interfaces, or code (each new requirement is designed and tested when its stage is planned); the values V-42 and V-43, which are derived or set with their stages.

**The owner's messages after the last one the previous record names** (the [owner decisions 26 verification](owner-decisions-26-verification.md), whose list ends with the owner's "Continue" of 2026-11-02, 20:23 UTC), up to the copy that this record's last Gate 3 run reviews: none. The report of that change's Gate 3 run 1 as the client delivered it (20:43 UTC), the stop hook's feedback, and the notices of background tasks are the client's own.

## The status report the owner asked for first

The owner asked first for a repository-backed status of Stage 1. Each answer has its one canonical home, which this record cites rather than restates (DEC-057, decision 6):

| The owner's question | Where it is answered |
|---|---|
| 1. What has been implemented | The project state's "Completed work" and checkpoint log: checkpoints A to D (U1 to U7, with U8 ending at the exit) |
| 2. What has been verified | Each checkpoint's verification record, through its three gates; the [stage record](stage-01-foundation.md)'s X7 |
| 3. What is being worked on | The project state's "Current task": this audit |
| 4. What remains in Stage 1 | The project state's "Next approved step" and "Stage convergence"; the stage record's exit checklist |
| 5. What is blocked or waiting for a decision | The project state's "Blocked" and "Decisions pending": nothing the work depends on; no owner decision pending |
| 6. What verification has passed | The stage record's exit checklist and each verification record |
| 7. The exact next step | The project state's "Next safe action" |

The status as of 2026-11-02, A to W, was reported to the owner the same day and is kept in the [owner decisions 26 verification](owner-decisions-26-verification.md) ("The status report").

## The draft reconciled

The audit started from the [draft](../drafts/draft-audit-of-owner-decisions-08.md) of 2026-10-07 and 2026-10-12, never reviewed (DEC-046, decision 5; DEC-047, decision 3), and compared it with what was decided since:

- **Kept:** its mapping of the twenty points, its contradiction search, its ten requirements with their owners and stages, its two values and two system rules, its readings, and its reason for adding lines rather than rewording the existing requirements, which now answers DEC-051's corrected reading (DEC-058, decision 3).
- **Renumbered:** DEC-042 and DEC-043, since used, are DEC-058, one record; V-41, since used for a configuration document's size ([DEC-054](../decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md)), and V-42 are V-42 and V-43. OPP-021 and OPP-022, TNP-027 to TNP-030, CAP-047 to CAP-049, PFC-019, SR-48, and SR-49 were still free.
- **Corrected:** CAP-047's further ranking considerations left out two the canonical requirements already list, strategy health (CAP-006) and opportunity expiration (CAP-006's opportunity duration, CAP-043's time sensitivity); CAP-047, CAP-048, OPP-022, TNP-028, and TNP-029 now name the requirements they extend, as the other five did; PFC-019's "never detected" is qualified "where measurable"; the draft's citations of the drafting rules (a builder text under `docs/builder/`, DEC-042) now cite owner decisions 9 and DEC-051; PLT-027 joins the mapping of points 14 to 16.
- **Not carried:** the draft's two explanatory paragraphs for the Opportunity Detection Engine's specification (the directive's breadth, depth, and speed in existing requirements; the universe and its conditions): the first is this record's mapping, and the second is DEC-058's first reading, each stated once (DEC-057, decision 6); and its status snapshot of 2026-10-12, which the citations above replace.

## Method

1. Every principle of the directive, and each of its twenty numbered points, compared with the requirement lines of the specifications, the values register, the System Rules Register, the roadmap, and the handoffs they came from.
2. A contradiction search, by script over every requirement line outside the preserved texts, the drafts, and the records: percentages; "percent"; a minimum profit, edge, return, or expected value; "ceiling"; "quota"; "daily target"; "daily return"; "trade count"; "highest" or "largest"; forcing; chasing; "revenge"; "martingale"; "interrupt"; "unwind"; "hysteresis"; "anomal"; "outlier"; "impossible"; "suspicious"; stopping a scan or search. It gives 46 requirement lines, each read in context.
3. The code checked for any limit on opportunity size.
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
| 14 | No artificial percentage ceiling | Daily: TNP-012, TNP-013, TNP-026, PLT-027. Per opportunity: added TNP-027, with TNP-028 for unusually large opportunities | Daily represented; per opportunity added |
| 15 | No forced trading | RSK-031, RSK-032, RSK-044, PLT-018, PLT-019, PLT-025, PLT-027, CAP-036 | Represented |
| 16 | No daily profit quota | TNP-014, RSK-044 ("hit a daily target"), PLT-007, PLT-008, PLT-019, PLT-027 | Represented |
| 17 | No chasing or revenge trading | RSK-044 (chasing), RSK-047 (revenge trading, martingale) | Represented |
| 18 | Active-trade protection | CAP-014, CAP-015; added: CAP-049 (interventions only on predefined material conditions, with hysteresis) | Represented; interventions added |
| 19 | Missed-opportunity analysis | OPP-014, OPP-015, PFC-012, PFC-013, PFC-016, ARB-003; added: PFC-019 (outcome categories) | Represented; categories added |
| 20 | Strict risk and execution validation | OPP-019, TNP-011, CAP-004, CAP-016, RSK-001, EXE-004, PERF-023, DIR-003 | Represented |

The directive's other statements map the same way: the universe and its conditions (OPP-009, OPP-013; DEC-058's first reading), the discovery flow (OPP-005, OPP-018, PLT-022), capital growth without reckless scaling (CAP-034, PLT-023, RDY-013, CAP-032), the objective (PLT-009, PLT-019, TNP-010), and the performance principle (PERF-005, PERF-014, PERF-016, PERF-021, PERF-010, PERF-023). The existing system rules SR-04, SR-05, SR-06, SR-07, SR-11, SR-15, SR-18, and SR-19 already index most of them; none indexes TNP-005, TNP-007, TNP-016, CAP-014, or CAP-015, which SR-48 and SR-49 now index, SR-48 per opportunity beside SR-19's daily ceiling.

## Contradictions

None found. The search's hits that could be read as a floor, a ceiling, a quota, or a size rule, and why each is consistent:

| Hit | Why it does not contradict the directive |
|---|---|
| ARB-015's tiers (about ≥1%, 0.5–1%, 0.2–0.5%, below 0.2%) | "Analytical categories only, not unconditional execution rules" |
| TNP-016's configurable percentage threshold | Allowed only as a research or filter parameter that never becomes a universal hard rule; the directive forbids a built-in floor, not the operator's own explicit policy (DEC-058's second reading) |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement derived from evidence (V-39), not a minimum for each opportunity (DEC-058's third reading) |
| TNP-019's uncertainty margin | Scaled by measured uncertainty; "must never be a fixed percentage or a universal minimum" |
| TNP-026's "unless an explicit risk/capital policy requires it" | Only the operator's explicit policy can stop operation for the day; the architecture has no ceiling |
| MKD-008's "impossible prices", MKD-013's "outlier corruption" | Quarantine of invalid data, not of extreme prices (DEC-058's fourth reading; TNP-028) |
| STR-015's canary allocation "within policy-defined limits" | A limit on the capital a new strategy version risks in canary, not on an opportunity's size or percentage; CAP-048 allocates subject to strategy limits |
| CAP-040's and RDY-025's thresholds and hysteresis | Rebalancing and capability transitions, other subjects; CAP-049's hysteresis concerns active trades |
| The values register's examples (TNP-006, TNP-012, TNP-014) | Listed there as illustrations, never operating values |
| STR-011's "minimum period and trade count" | DEPRECATED / REPLACED ([DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md), [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)); STR-018 makes time and trade count evidence only |
| The other hits (for example "highest first" in RSK-004 and PERF-015, "forced" in RGM-003 and MIG-001, "interrupt" in the recovery requirements) | Other subjects: a precedence order, a classification, a hosting choice, recovery after an interruption |
| The roadmap | No stage, item, or feature sets a percentage, target, or quota |
| The code | No opportunity logic exists. Its only size limits are V-41, a configuration document's bytes (`atp.config`), and V-40, the precision of an amount (`atp.numeric`); neither caps an amount relative to anything |

## Duplicates

None created. The ten new requirements cite the requirements they extend ("In addition to …") instead of restating them. Two restatements were taken out of the draft's lines before it was committed (TNP-027's sentence that 5% is not a target, minimum, quota, or expected daily return, already TNP-014, TNP-005, and RSK-044; and CAP-049's opening sentence that a newer opportunity is never by itself a reason to intervene, already CAP-014), and two more now ("The draft reconciled"). The directive itself is kept as a HISTORICAL source, not a second set of rules.

## Classification and provenance of each drafted item

Each drafted item is classified (owner decisions 9, Rule 8), its origin stated (Rule 4), its owner and stage named (Rules 7 and 14), the existing requirements it strengthens named (Rule 16), and where it will be enforced and tested (Rule 17). The categories are the outcome of this reconciliation; each requirement keeps its ARCH-015 class in its specification line (DEC-051, decision 2).

| Item | Category (Rule 8) | Provenance (Rule 4): owner decisions 8, section | Strengthens (Rule 16) | Owner (Rule 7) | Stage (Rule 14) | Enforced and tested (Rule 17) |
|---|---|---|---|---|---|---|
| OPP-021 | NEW CONFIRMED REQUIREMENT | "Continuous whole-universe scanning" | OPP-001, OPP-018 | Opportunity Detection Engine (SYS-05) | 2 DATA FOUNDATION | The opportunity filter (OPP-005); test: scanning continues after a find of any size |
| OPP-022 | NEW CONFIRMED REQUIREMENT | "Opportunity search prioritization" | TNP-005, TNP-016; OPP-017 to OPP-020 | SYS-05 | 2 | The filter's search order; SR-48; test: no candidate below a priority level is dropped for its level |
| TNP-027 | NEW CONFIRMED REQUIREMENT | The opening reinforcement ("Only trade opportunities up to 1%") and "No artificial opportunity ceiling" | TNP-012, TNP-026 (a daily ceiling), TNP-006 | True Net-Profit Engine (SYS-06) | 3 CORE TRADING FOUNDATION | Economic eligibility (TNP-020); SR-48; test: a large positive-net opportunity is not rejected for its percentage |
| TNP-028 | NEW CONFIRMED REQUIREMENT | "No artificial opportunity ceiling" (the order of validation) | TNP-020; data validation stays MKD-008 and MKD-013 | SYS-06, with market data's validation | 3 | Eligibility; V-42; SR-48; test: an unusually large opportunity passes every check or is rejected for a named check, never for its size |
| TNP-029 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" (minimum efficient, optimal, and maximum efficient capital) | TNP-018, QNT-004; the final size stays RSK-011 | SYS-06; the Global Capital Authority allocates within it; the Risk Engine sets the final size | 3 | The economics calculation; test: the result across sizes, with the range's ends |
| TNP-030 | NEW CONFIRMED REQUIREMENT | "True net economics" (its list of costs, and "expected dollar profit") | TNP-018, TNP-021, TNP-023, TNP-025 | SYS-06 | 3 (the arbitrage terms with stage 5, as TNP-023) | The economics calculation; test: each term changes the result where it applies |
| CAP-047 | NEW CONFIRMED REQUIREMENT | "Opportunity competition" (not "Always choose the highest percentage"; its ranking list) | CAP-009, CAP-006, CAP-043, TNP-015, TNP-021 | Global Capital Authority (SYS-07) | 3 | Allocation ranking; SR-48; test: a higher percentage ranks below a better opportunity |
| CAP-048 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" | CAP-007, CAP-036, CAP-016, RSK-011 | SYS-07 | 3 | Allocation; test: neither tiny artificial allocations nor full deployment because an opportunity appears |
| CAP-049 | NEW CONFIRMED REQUIREMENT | "Active trade protection" | CAP-014, CAP-015, DIR-004, RSK-017 | SYS-07, with the position's owner and the Risk Engine | 3 (the positions' owners in stages 4 and 5) | SR-49; V-43; test: an active trade and a better-looking new opportunity; hysteresis |
| PFC-019 | NEW CONFIRMED REQUIREMENT | "Missed opportunity analysis" | PFC-012, PFC-016 | Performance Controller | 4 DIRECTIONAL TRADING (its core) | The Opportunity Database's records (OPP-014 to OPP-016); test: each category recorded |
| V-42, V-43 | Part of TNP-028 and CAP-049: values to be derived or set (ARCH-018), not requirements | "Unusually large"; "materiality thresholds and hysteresis" | The values register | As their requirements | As their requirements | Recorded as not derived and not set, with their behaviour until then |
| SR-48, SR-49 | Index entries over existing and new requirements (ARCH-038); no new rule | The requirements they index | SR-19 and SR-04 to SR-07 (alongside) | As named in the register | 3 | The enforcement points and tests named in the register |
| The six readings in DEC-058 | EXISTING REQUIREMENT (the reading of an existing requirement, or of the directive's wording, under it) | The requirements each names | — | — | — | — |
| The twenty points, where "Represented" | EXISTING REQUIREMENT | The requirements in the table above | — | — | — | — |

No item is a REFINED EXISTING REQUIREMENT: no existing requirement's text changes, and DEC-058's decision 3 says why each gap is closed by a new line rather than by rewording the requirement it extends.

## Final reconciliation report

Rule 23 of the drafting rules, before the drafted requirements become authoritative:

| # | Item | Result |
|---|---|---|
| 1 | Existing requirements identified | Every one of the twenty points has canonical requirements (the table of the twenty points); the directive's other statements map to OPP-005, OPP-009, OPP-013, OPP-018, PLT-009, PLT-019, PLT-022, PLT-023, CAP-032, CAP-034, RDY-013, TNP-010, and PERF-005, PERF-010, PERF-014, PERF-016, PERF-021, PERF-023 |
| 2 | Requirements mapped | The twenty points and the other statements, as above; the system rules SR-04, SR-05, SR-06, SR-07, SR-11, SR-15, SR-18, and SR-19 already index most of them |
| 3 | Requirements refined | None: no existing requirement's text, class, or source changes (the requirement comparison shows nothing changed) |
| 4 | Genuine new requirements | Ten: OPP-021, OPP-022, TNP-027 to TNP-030, CAP-047 to CAP-049, PFC-019, each with the owner's directive as its source (DEC-058) |
| 5 | Duplicates rejected | Four restatements taken out of the drafted lines ("Duplicates"); "persistent WebSocket connections" and "affected-route recalculation" (TEC-005, EXA-012, PERF-005); "expected dollar profit" (TNP-018's amount in quote currency); a document restating every principle (DEC-058's alternatives) |
| 6 | Unnecessary items rejected | The draft's two explanatory paragraphs for the specification ("The draft reconciled") |
| 7 | Future capabilities identified | None new. The ten requirements belong to stages 2 to 4, whose features stay PROPOSED until each stage's plan is approved (DEC-040); nothing beyond Stage 1 is authorized (DEC-038) |
| 8 | Owner decisions required | None ("Owner decisions") |
| 9 | Conflicts discovered | None (the contradiction search above; each hit explained) |
| 10 | Conflicts resolved | None needed. Six phrases that could be read against the directive are read in DEC-058 under the requirements they belong to |
| 11 | Dependencies affected | The Opportunity Detection Engine, the True Net-Profit Engine (with the Quantitative Engine's calculations and market data's validation), the Global Capital Authority, the Risk Engine (final size, emergency handling), the positions' owners (the directional and arbitrage systems), and the Performance Controller. No interface, schema, configuration, or code exists for them yet; each is designed with its stage's plan |
| 12 | Canonical sources updated | The four specifications, the values register (V-42, V-43), the System Rules Register (SR-48, SR-49), the roadmap ("Additions of 2026-11-02 by stage"), the generated registry, the decision log, and the project state |
| 13 | Enforcement locations identified | Per requirement in the classification table; for the system rules, in the register's enforcement-point column |
| 14 | Tests added or updated | None in code: no opportunity, economics, or allocation code exists in Stage 1. The tests each stage's plan must include are listed in DEC-058's consequences and in the classification table |
| 15 | Three-pass verification performed | Below ("Gates") |
| 16 | Remaining unresolved items | V-42 is not derived and V-43 is not set (the values register, with the behaviour until then); nothing else |

## Gaps closed

| Gap | Closed by |
|---|---|
| A found opportunity could, in a reading, end the search | OPP-021 |
| Search prioritization by value had no stated limits | OPP-022 |
| No requirement forbade a ceiling on a single opportunity (only on the daily total) | TNP-027 |
| No requirement said what to do with an unusually large opportunity | TNP-028, V-42 |
| No requirement gave an opportunity a capital range (minimum efficient, optimal, maximum efficient) | TNP-029 |
| Partial fills, failed or rejected orders, capital lock duration, venue reliability, and counterparty or custody exposure were not named as economic terms | TNP-030 |
| "Always choose the highest percentage" was excluded only implicitly (CAP-009) | CAP-047 |
| No requirement excluded tiny artificial allocations or full deployment because an opportunity appears | CAP-048 |
| Active trades were protected (CAP-014), but when an intervention is allowed, by whom, and with what stability was not stated | CAP-049, V-43 |
| Expired, disappeared, latency-missed, and never-detected opportunities were not named categories | PFC-019 |
| No system rule indexed the per-opportunity floor and ceiling rules or active-trade protection | SR-48, SR-49 |

## Owner decisions

None required. Every point is either already canonical or stated by the owner in the directive, which asks for a missing rule to be corrected where the correct resolution is already established; each new requirement states what the directive says, and each reading follows from existing requirements and the directive's own text. The readings are recorded in DEC-058 for the owner to see, and the owner can correct them.

## Reconciliation of the last change's temporary backup

PENDING.

## Checks

PENDING.

## Gates

PENDING.

## Failures and fixes

PENDING.

## Final status and remaining issues

PENDING.

## Environment

System Python 3.11 (`python3`) for the documentation tools; git; GitHub's branch list, pull requests, and workflow runs, read through the session's GitHub tools.
