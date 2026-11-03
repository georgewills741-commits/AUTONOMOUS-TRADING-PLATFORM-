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

**Changed:** the generated [registry](../requirements/registry.md) and [handoff coverage](handoff-coverage.md); the roadmap's current position; the [drafts index](../drafts/README.md) and the draft's banner (its disposition); the project state (its status line and its bullet on owner decisions 8; the status table; the continuation contract's rows "Current task", "In progress, possibly partial", "Blocked", "Stage convergence", "Decisions in effect", "Other branches", "Known risks", and "Next safe action"; "Branches"; "Completed work"; "In-progress work"; "Blockers"; "Recent decisions"; "Recent changes"; "Next approved step"; the checkpoint log); the [stage record](stage-01-foundation.md) (its status line, its "Blockers" row, and the retirements listed for the certificate); the indexes ([documentation index](../README.md), [traceability README](README.md), [decision log](../decisions/README.md)).

**Requirements:** ten added, none removed or changed (check 3).

**Out of scope:** item 5 of "Next approved step"; any later stage's design, interfaces, or code (each new requirement is designed and tested when its stage is planned); the values V-42 and V-43, which are derived or set with their stages.

**The owner's messages after the last one the previous record names** (the [owner decisions 26 verification](owner-decisions-26-verification.md), whose list ends with the owner's "Continue" of 2026-11-02, 20:23 UTC), up to the copy that this record's last Gate 3 run reviews: none. The reports of that change's Gate 3 run 1 and of this change's as the client delivered them (2026-11-02, 20:43 and 21:31 UTC), the stop hook's feedback, the notices of background tasks and of the worker's restarts, and the summary the client wrote when it compacted the session (2026-11-03, 02:25 UTC) are the client's own.

## The status report the owner asked for first

The owner asked first for a repository-backed status of Stage 1. Each answer has its one canonical home, which this record cites rather than restates (DEC-057, decision 6):

| The owner's question | Where it is answered |
|---|---|
| 1. What has been implemented | The project state's "Completed work" and checkpoint log: checkpoints A to D (U1 to U7, with U8 ending at the exit) |
| 2. What has been verified | Each checkpoint's verification record, through its three gates; the [stage record](stage-01-foundation.md)'s X7 |
| 3. What is being worked on | The project state's "Current task": this audit until its commit, and item 5 from then on |
| 4. What remains in Stage 1 | The project state's "Next approved step" and "Stage convergence"; the stage record's exit checklist |
| 5. What is blocked or waiting for a decision | The project state's "Blocked" and "Decisions pending": nothing the work depends on; no owner decision pending |
| 6. What verification has passed | The stage record's exit checklist and each verification record |
| 7. The exact next step | The project state's "Next safe action" |

The status as of 2026-11-02, A to W, was reported to the owner the same day and is kept in the [owner decisions 26 verification](owner-decisions-26-verification.md) ("The status report").

## The draft reconciled

The audit started from the [draft](../drafts/draft-audit-of-owner-decisions-08.md) of 2026-10-07 and 2026-10-12, never reviewed (DEC-046, decision 5; DEC-047, decision 3), and compared it with what was decided since:

- **Kept:** its mapping of the twenty points, its contradiction search, its ten requirements with their owners and stages, its two values and two system rules, its readings, and its reason for adding lines rather than rewording the existing requirements, which now answers DEC-051's corrected reading (DEC-058, decision 3).
- **Renumbered:** DEC-042 and DEC-043, since used, are DEC-058, one record; V-41, since used for a configuration document's size ([DEC-054](../decisions/DEC-054-configuration-size-limit-and-retired-backup-branches.md)), and V-42 are V-42 and V-43. OPP-021 and OPP-022, TNP-027 to TNP-030, CAP-047 to CAP-049, PFC-019, SR-48, and SR-49 were still free.
- **Corrected:** CAP-047's further ranking considerations left out two the canonical requirements already list, strategy health (CAP-006) and opportunity expiration (CAP-006's opportunity duration, CAP-043's time sensitivity); OPP-022, TNP-028, TNP-029, and CAP-048 now open with the requirements they extend, as OPP-021, TNP-027, TNP-030, CAP-049, and PFC-019 did, and CAP-047 now opens with CAP-009 and adds CAP-006 and TNP-021 to those it names; PFC-019's "never detected" is qualified "where measurable"; the draft's citations of the drafting rules (a builder text under `docs/builder/`, DEC-042) now cite owner decisions 9 and DEC-051; PLT-027 joins the mapping of points 14 to 16.
- **Not carried:** the draft's two explanatory paragraphs for the Opportunity Detection Engine's specification (the directive's breadth, depth, and speed in existing requirements; the universe and its conditions): the first is this record's mapping, and the second is DEC-058's first reading, each stated once (DEC-057, decision 6); and its status snapshot of 2026-10-12, which the citations above replace.

## Method

1. Every principle of the directive, and each of its twenty numbered points, compared with the requirement lines of the specifications, the values register, the System Rules Register, the roadmap, and the handoffs they came from.
2. A contradiction search, by script over every requirement line outside the preserved texts, the drafts, and the records: percentages; "percent"; a minimum profit, edge, return, or expected value; "ceiling"; "quota"; "daily target"; "daily return"; "trade count"; "highest" or "largest"; forcing; chasing; "revenge"; "martingale"; "interrupt"; "unwind"; "hysteresis"; "anomal"; "outlier"; "impossible"; "suspicious"; stopping a scan or search. It gives 46 requirement lines besides the ten new ones, each read in context.
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
| 14 | No artificial percentage ceiling | Daily: TNP-012, TNP-013, TNP-026, PLT-027. Per opportunity: TNP-006, TNP-007, TNP-016 in general terms; made explicit: TNP-027, with TNP-028 for unusually large opportunities | Represented; per opportunity made explicit |
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
| TNP-016's configurable percentage threshold | Allowed only as a research or filter parameter that never becomes a universal hard rule; the directive forbids a built-in floor, not the operator's own explicit policy (DEC-058's second reading); at the upper end, a configured threshold may order the search or serve research, but never rejects an opportunity for its size (TNP-027, TNP-028) |
| RDY-011's "minimum expected edge" | A feature's or strategy's eligibility requirement derived from evidence (V-39), not a minimum for each opportunity (DEC-058's third reading) |
| TNP-019's uncertainty margin | Scaled by measured uncertainty; "must never be a fixed percentage or a universal minimum" |
| TNP-026's "unless an explicit risk/capital policy requires it" | Only the operator's explicit policy can stop operation for the day; the architecture has no ceiling |
| MKD-008's "impossible prices", MKD-013's "outlier corruption" | Quarantine of invalid data, not of extreme prices (DEC-058's fourth reading; TNP-028) |
| STR-015's canary allocation "within policy-defined limits" | A limit on the capital a new strategy version risks in canary, not on an opportunity's size or percentage; CAP-048 allocates subject to strategy limits |
| CAP-040's and RDY-025's thresholds and hysteresis | Rebalancing and capability transitions, other subjects; CAP-049's hysteresis concerns active trades |
| ARB-010's kill-switch triggers "unexpected spreads" and "market anomalies" | Possible triggers with policy thresholds (V-13): a risk control the directive keeps ("VALIDATE RISK"), acting on a venue's or market's state; an unusually large apparent opportunity is verified first and never rejected for its size alone (TNP-028) |
| The values register's examples (TNP-006, TNP-012, TNP-014) | Listed there as illustrations, never operating values |
| STR-011's "minimum period and trade count" | DEPRECATED / REPLACED ([DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md), [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)); STR-018 makes time and trade count evidence only |
| The other hits (for example "highest first" in RSK-004 and PERF-015, "forced" in RGM-003 and MIG-001, "interrupt" in the recovery requirements) | Other subjects: a precedence order, a classification, a hosting choice, recovery after an interruption |
| The roadmap | No stage, item, or feature sets a percentage, target, or quota |
| The code | No opportunity logic exists. Its only limits of this kind are V-41, the size of a configuration document (`atp.config`), and V-40, the precision of an amount (`atp.numeric`); the contract schemas constrain formats, not sizes; none caps an amount relative to anything |

## Duplicates

None created. The ten new requirements cite the requirements they extend ("In addition to …") instead of restating them. Two restatements were taken out between the draft's first and second versions (TNP-027's sentence that 5% is not a target, minimum, quota, or expected daily return, already TNP-014, TNP-005, and RSK-044; and CAP-049's opening sentence that a newer opportunity is never by itself a reason to intervene, already CAP-014), and two more now ("The draft reconciled"). The directive itself is kept as a HISTORICAL source, not a second set of rules.

## Classification and provenance of each drafted item

Each drafted item is classified (owner decisions 9, Rule 8), its origin stated (Rule 4), its owner and stage named (Rules 7 and 14), the existing requirements it strengthens named (Rule 16), and where it will be enforced and tested (Rule 17). The categories are the outcome of this reconciliation; each requirement keeps its ARCH-015 class in its specification line (DEC-051, decision 2).

| Item | Category (Rule 8) | Provenance (Rule 4): owner decisions 8, section | Strengthens (Rule 16) | Owner (Rule 7) | Stage (Rule 14) | Enforced and tested (Rule 17) |
|---|---|---|---|---|---|---|
| OPP-021 | NEW CONFIRMED REQUIREMENT | "Continuous whole-universe scanning" | OPP-001, OPP-018 | Opportunity Detection Engine (SYS-05) | 2 DATA FOUNDATION | The opportunity filter (OPP-005); test: scanning continues after a find of any size |
| OPP-022 | NEW CONFIRMED REQUIREMENT | "Opportunity search prioritization" | TNP-005, TNP-016; OPP-017 to OPP-020 | SYS-05 | 2 | The filter's search order; SR-48; test: no candidate below a priority level is dropped for its level |
| TNP-027 | NEW CONFIRMED REQUIREMENT | The opening reinforcement ("Only trade opportunities up to 1%") and "No artificial opportunity ceiling" | TNP-007, TNP-016; TNP-012, TNP-026 (a daily ceiling), TNP-006 | True Net-Profit Engine (SYS-06) | 3 CORE TRADING FOUNDATION | Economic eligibility (TNP-020); SR-48; test: a large positive-net opportunity is not rejected for its percentage |
| TNP-028 | NEW CONFIRMED REQUIREMENT | "No artificial opportunity ceiling" (the order of validation) | TNP-020; data validation stays MKD-008 and MKD-013 | SYS-06, with market data's validation | 3 | Eligibility; V-42; SR-48; test: an unusually large opportunity passes every check or is rejected for a named check, never for its size |
| TNP-029 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" (minimum efficient, optimal, and maximum efficient capital) | TNP-018, QNT-004; the final size stays RSK-011 | SYS-06; the Global Capital Authority allocates within it; the Risk Engine sets the final size | 3 | The economics calculation; test: the result across sizes, with the range's ends |
| TNP-030 | NEW CONFIRMED REQUIREMENT | "True net economics" (its list of costs, and "expected dollar profit") | TNP-018, TNP-021, TNP-023, TNP-025 | SYS-06 | 3 (the arbitrage terms with stage 5, as TNP-023) | The economics calculation; test: each term changes the result where it applies |
| CAP-047 | NEW CONFIRMED REQUIREMENT | "Opportunity competition" (not "Always choose the highest percentage"; its ranking list) | CAP-009, CAP-006, CAP-043, TNP-015, TNP-021 | Global Capital Authority (SYS-07) | 3 | Allocation ranking; SR-48; test: a higher percentage ranks below a better opportunity |
| CAP-048 | NEW CONFIRMED REQUIREMENT | "Capital efficiency" | CAP-007, CAP-036, CAP-016, RSK-011 | SYS-07 | 3 | Allocation; test: neither tiny artificial allocations nor full deployment because an opportunity appears |
| CAP-049 | NEW CONFIRMED REQUIREMENT | "Active trade protection" | CAP-014, CAP-015, DIR-004, RSK-013, RSK-017, RSK-026, RSK-045, STR-017 | SYS-07, with the position's owner and the controls CAP-049 names | 3 (the positions' owners in stages 4 and 5) | SR-49; V-43; test: an active trade and a better-looking new opportunity; hysteresis |
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
| 5 | Duplicates rejected | Four restatements taken out of the drafted lines ("Duplicates"); "persistent WebSocket connections" and "affected-route recalculation" (TEC-005, EXA-012, PERF-005); "expected dollar profit" as a new term (it is TNP-018's amount in quote currency; TNP-030 adds only the result relative to the capital used, and CAP-047 its use in ranking); a document restating every principle (DEC-058's alternatives) |
| 6 | Unnecessary items rejected | The draft's two explanatory paragraphs for the specification ("The draft reconciled") |
| 7 | Future capabilities identified | None new. The ten requirements belong to stages 2 to 4, whose features stay PROPOSED until each stage's plan is approved (DEC-040); nothing beyond Stage 1 is authorized (DEC-038) |
| 8 | Owner decisions required | None ("Owner decisions") |
| 9 | Conflicts discovered | None (the contradiction search above; each hit explained) |
| 10 | Conflicts resolved | None needed. Six phrases are read in DEC-058: two of the directive's, two of existing requirements that could be read against it, and two of its terms that existing requirements cover |
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
| A ceiling on a single opportunity was excluded only in general terms (TNP-007; TNP-016: no universal percentage threshold), not by name; TNP-012 and TNP-026 name only the daily ceiling | TNP-027 |
| No requirement said what to do with an unusually large opportunity | TNP-028, V-42 |
| No requirement gave an opportunity a capital range (minimum efficient, optimal, maximum efficient) | TNP-029 |
| Partial fills, failed or rejected orders, capital lock duration, venue reliability, and counterparty or custody exposure were not named as economic terms | TNP-030 |
| "Always choose the highest percentage" was excluded only implicitly (CAP-009) | CAP-047 |
| No requirement excluded tiny artificial allocations or full deployment because an opportunity appears | CAP-048 |
| Active trades were protected (CAP-014), but when an intervention is allowed and with what stability was not stated; who decides was stated only per control (DIR-004, RSK-013, RSK-017, RSK-026, RSK-045, STR-017) | CAP-049, V-43 |
| Expired, disappeared, latency-missed, and never-detected opportunities were not named categories | PFC-019 |
| No system rule indexed the per-opportunity floor and ceiling rules or active-trade protection | SR-48, SR-49 |

## Owner decisions

None required. Every point is either already canonical or stated by the owner in the directive, which asks for a missing rule to be corrected where the correct resolution is already established; each new requirement states what the directive says, or what an established requirement it cites determines, and each reading follows from existing requirements and the directive's own text. The readings are recorded in DEC-058 for the owner to see, and the owner can correct them.

## Reconciliation of the last change's temporary backup

The change that preserved owner decisions 26, committed as `a52e4ad`, was backed up on `claude/unverified-backup-owner-decisions-26` ([owner decisions 26 verification](owner-decisions-26-verification.md), "Identity"), in 8 commits, each on the one before and the first on `c2a6786`: `26ee405` (2026-11-02, 15:50 UTC), `d361546` (15:57), `32565ce` (16:01), `07af1be` (16:09), `f869703` (16:15), `a58896f` (20:23), `d1c63f7` (20:24), whose tree is that of the copy Gate 3 run 1 reviewed, and `081760e` (20:47). Each carries the seven labels, the emergency checkpoint record of §132 with its seven fields, and the session's trailer. On 2026-11-02, from 20:50 UTC, after `a52e4ad` was pushed and the machine checks passed on it, the builder compared the branch with `a52e4ad` by owner decisions 10's eight checks:

| # | Check (owner decisions 10) | Evidence | Result |
|---|---|---|---|
| 1 | Every intended valid change is preserved | `a52e4ad`'s tree is `081760e`'s (`git diff --name-status`: no difference): the last backup holds run 1's fixes and the record's final status | PASS |
| 2 | Corrections made during verification are preserved | The same tree: run 1's fixes in the wording it specified, and its result | PASS |
| 3 | No required work exists only on the temporary backup | No file of any of the 8 commits is missing from `a52e4ad` (`git diff --diff-filter=D`). Each differs from `c2a6786` only in `CLAUDE.md`, documents under `docs/`, the documentation tools' README, and the preserved-text manifest, so no code, test, tool's code, configuration, or workflow differs | PASS |
| 4 | No unverified or rejected implementation is accidentally promoted | `a52e4ad`'s parent is `c2a6786`; none of the 8 commits is in its history or in that of `main`, at `7172a5c` (`git merge-base --is-ancestor`) | PASS |
| 5 | The authoritative branch contains the correct final state | On a fresh clone of the designated branch from GitHub, at `a52e4ad` (20:50 to 20:51 UTC): the documentation checker and its self-test pass, and `compare_requirements.py c2a6786 --strict` reports 734 requirements before and after, none added, removed, or changed; the tests ran in the machine checks (check 7) | PASS |
| 6 | Required documentation and traceability are updated | `a52e4ad` holds the record's final status, PASS, the checkpoint log's row for the change, and the backup in the project state's "Branches", as active until reconciled | PASS |
| 7 | The official verified checkpoint has been successfully pushed | `a52e4ad` is on the remote branch (`git ls-remote`), pushed at 20:47 UTC, and the machine checks passed on it: [run 41522438377](https://github.com/georgewills741-commits/AUTONOMOUS-TRADING-PLATFORM-/actions/runs/41522438377), completed 20:49 UTC, every step, 1,108 tests passed | PASS |
| 8 | Repository status is clean and consistent | The working tree was clean at `a52e4ad`, the remote branch's commit (20:50 UTC) | PASS |

**Result: PASS.** The backup's work is VERIFIED AND INCORPORATED in `a52e4ad`. Its last commit, `081760e`, is kept under the archive branch `claude/archive/unverified-backup-owner-decisions-26`, pushed at 20:51 UTC and checked on GitHub at that commit (`git ls-remote`, and GitHub's branch list). The deletion of `claude/unverified-backup-owner-decisions-26`, a git push made only if the branch was still at `081760e`, was refused at 20:51 UTC with HTTP 403; the branch stays at `081760e`, and is retired as DEC-054 (decision 4) provides.

**The ten checks before "safe to delete"** ([owner decisions 22](../handoffs/owner-decisions-22-configuration-limit-and-branch-retirement.md)'s first rule set, §5), made on 2026-11-02 for the branch, at `081760e`:

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | All valid unique work is preserved elsewhere | Its commits are its archive branch's (check 3), and its work is in `a52e4ad` (the reconciliation above) | PASS |
| 2 | The canonical archive exists | GitHub's branch list (20:51 UTC): `claude/archive/unverified-backup-owner-decisions-26` at `081760e` | PASS |
| 3 | Commit and content parity | The branch is at the same commit as its archive branch, so its content is the same (GitHub's branch list; `git ls-remote`, 20:51 UTC) | PASS |
| 4 | No open work depends on it | The project state's work in progress and next steps name it only as done: reconciled, archived, and retired, with nothing left to do on it | PASS, in this change |
| 5 | No active pull request depends on it | GitHub's list of the repository's pull requests, in every state: none (20:51 UTC) | PASS |
| 6 | No required verification evidence exists only on it | A backup is evidence for no gate (DEC-052, decision 3); every record is on the designated branch; and the backup's commits are on its archive branch too | PASS |
| 7 | No unresolved owner decision depends on it | The [open-question register](../open-questions/register.md) and the project state: no decision on it is pending | PASS |
| 8 | No deployment or automation depends on it | The one workflow, `.github/workflows/checks.yml`, runs on every push and pull request and names no branch; nothing is deployed; outside `docs/`, the repository does not name the branch (`git grep`, 20:52 UTC) | PASS |
| 9 | Traceability is updated | The project state's "Branches", this record, and the stage record | PASS, in this change |
| 10 | A canonical rule permits retirement and deletion | DEC-052, decision 3: the backup branch is deleted once its archive is checked; DEC-054, decision 4: a later backup whose deletion is refused is retired the same way; owner decisions 10: "RETIRE / DELETE TEMPORARY BACKUP WHEN SAFE" | PASS |

So the branch is RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED. No deletion is tried again (§6): nothing shows that this environment's access has changed, and the owner has not asked. The branch is not protected on GitHub (its branch list).

**The report, A to L** (§14): A, `claude/unverified-backup-owner-decisions-26`; B, `081760e`; C, `claude/archive/unverified-backup-owner-decisions-26`, its work in `a52e4ad`; D, parity verified (the same commit as its archive branch; reconciled above); E, RETIRED — DELETION BLOCKED — SAFE TO DELETE WHEN PERMITTED; F, not authoritative; G, nothing depends on it (checks 4 to 8); H, safe to delete when permitted (the ten checks); I, HTTP 403 from this session's access to GitHub (2026-11-02, 20:51 UTC); J, no retry now: no evidence that the access has changed; K, kept, retired, until a deletion is permitted, its archive branch kept for audit; L, none now: when a deletion is permitted, or the owner deletes it on GitHub, re-check that it is still retired and at `081760e`, delete it, and record it as RETIRED — PHYSICALLY DELETED.

## Checks

The documentation tools, with the system Python 3.11, and git, on the working tree with this change. No code changed, so the [developer guide](../development.md)'s other commands run in the machine checks on this record's commit (check 4):

| # | Check | How | Result |
|---|---|---|---|
| 1 | The documentation checker | `python3 tools/docs/build_index.py --check-only`, after `python3 tools/docs/build_index.py` | PASS: exit 0; the regeneration writes the ten requirements into the registry and DEC-058's row into the handoff coverage, and nothing else |
| 2 | The documentation tools' self-test | `python3 tools/docs/selftest.py` | PASS: 61 cases and the control |
| 3 | The requirements added, and none removed or changed | `python3 tools/docs/compare_requirements.py a52e4ad --strict` | PASS: 734 requirements before, 744 after; added: CAP-047, CAP-048, CAP-049, OPP-021, OPP-022, PFC-019, TNP-027, TNP-028, TNP-029, TNP-030; none removed or changed |
| 4 | The code is unchanged | `git diff --name-only a52e4ad` and `git ls-files --others --exclude-standard`; the machine checks run the tests on this record's commit | PASS: the eighteen files this change adds or changes are all under `docs/`: this record, DEC-058, the four specifications, the values register, the System Rules Register, the generated registry and handoff coverage, the roadmap, the project state, the stage record, the draft and the drafts index, the documentation index, the traceability README, and the decision log |
| 5 | Hygiene of the change | `git diff --check a52e4ad`, its new files included; a scan of the lines this change adds, its new files included, for local paths, session or model identifiers, and the shapes of secrets | PASS: `git diff --check` reports nothing; the scan finds no local path, session or model identifier, or secret |
| 6 | The draft's content unchanged | `git diff -U0 a52e4ad -- docs/drafts/draft-audit-of-owner-decisions-08.md` | PASS: only its banner's two lines (its status and its disposition) change; its text blocks, the draft as it was, are untouched |

## Gates

**Verification 1 — the change works as intended:** PASS. Checks 1 to 6 pass, run again after this record's last edit before each Gate 3 run's copy was made, and every statement the change adds was read back against its evidence before each launch (DEC-057, decision 6): each cited requirement's text, the search's output, the code, git's output, GitHub's answers, and the session record, with their times. The read-backs found the statements corrected below ("Failures and fixes").

**Verification 2 — architecture and consistency:** PASS, by the builder's review of the whole diff. Each new requirement sits in the specification that owns its subject, names the requirements it extends, and states what none of them states, or states only in general terms, with the directive's words, or what an established requirement it cites determines, as its source (owner decisions 9, Rules 3 to 5, 16; DEC-051, decision 2, as corrected); no requirement, value, or system rule duplicates another (the requirement lines, the values register, and the System Rules Register searched for each); each requirement's stage is its specification's, and no later stage's work starts (DEC-038, DEC-040). The backup's reconciliation and retirement follow owner decisions 10 and 22 as for the earlier backups. Every current statement that item 4 was still to come, or that counted the retired backups, was searched (`git grep`) and updated; the dated records keep what they said at their date (DEC-037).

**Verification 3 — independent end-to-end and failure audit:** an independent reviewer, a separate agent started with a fresh context, on a push-disabled copy of the repository at `a52e4ad` with the change applied, made as the traceability README states and identified by the hash of its `git diff`. Findings are numbered E-01, E-02, and so on, across runs, with the severity DEC-045's decision 2 gives.

- **Run 1** (copy `b319ec8e95c4…`, made on 2026-11-02 at 21:05 UTC; its tree is that of the backup commit `16c24b1`): launched at 21:06 UTC; it reported at 21:31 UTC. **FAIL**: blocking E-01 to E-04, E-01 a new requirement whose wording excluded controls that existing requirements give authority over open positions, and E-02 to E-04 statements of the change shown false, each with the wording that fixes it; non-blocking E-05 to E-12; optional E-13 and E-14. Its report opens with the heading "Gate 3 run 1: item 4 (audit of owner decisions 8, DEC-058)" and the sentence "**Verdict: FAIL.** There are four blocking findings, E-01 to E-04." It found true: checks 1, 2, 3, and 5, run again in a fresh clone of the copy; the contradiction search, run again with its own script and further terms over the 744 requirement lines, with no new concern but E-05 and E-06; the code's limits; about 60 of the cited requirements, covering every one of the twenty points, apart from E-02; "The draft reconciled", compared by script with the draft's two versions; the last change's 8 backup commits and owner decisions 10's eight checks; the ten checks, apart from E-04's two times, and the report A to L; run 41522438377 and its 1,108 tests; the session record's times and the Scope's "none"; and the copy, unchanged at the end.
- **Baseline and severity** (DEC-045, decisions 1 and 2): the brief gave owner decisions 8 with its FINAL REQUIREMENT, owner decisions 9 as DEC-051 reads it, with its corrected reading of a refined requirement, the requirement conventions, the stages, the rules for drafts, the backup lifecycle, the record format and the owner's messages, and the current state; its severity was DEC-045's decision 2, with a new requirement that duplicates or contradicts one, states more than the directive or an established rule supports, or claims a gap an existing requirement closes among the blocking cases.
- **Blocking findings per run:** four in run 1, none reopened and none caused by a fix (the first run).
- **The stop after run 1:** the session's 5-hour usage limit stopped it at 21:31 UTC, as run 1's report arrived; the limit reset at 01:20 UTC on 2026-11-03, and the session resumed when its worker restarted at 02:20 UTC. Nothing was exposed: no edit was made after the backup `16c24b1` (21:05 UTC), whose tree the working tree had at 21:07 and at 02:20 UTC (DEC-057, decision 4).

| ID | Run | Finding and evidence | Class (owner decisions 13, §6) | Severity | Relation (§5) | Provenance | Fix | Status |
|---|---|---|---|---|---|---|---|---|
| E-01 | 1 | CAP-049 and V-43's note said that only the position's owning system or the Risk Engine's emergency handling (RSK-017) changes an active trade; existing requirements give other controls that power: RSK-013 (automatic de-risking before liquidation), RSK-026 and RSK-045 (the loss-streak responses), and STR-017 (the automatic canary stop). The directive does not say who decides | Blocking defect (a requirement's text) | Blocking | New | DEC-045, decision 2; owner decisions 9, Rules 7, 9, 12, and 13; DEC-051, decision 2 | CAP-049's second sentence, V-43's note, SR-49's "Enforced where", the gap row, and DEC-058's table row, in the words the review specified, with RSK-045 named in V-43's note and the gap row as in CAP-049 | Fixed; it changes a requirement's text, so run 2 reviews it (DEC-045, decision 5) |
| E-02 | 1 | The record said that no requirement forbade a ceiling on a single opportunity; TNP-007 and TNP-016, with TNP-006, exclude a universal one in general terms; the record's point 7 already called it "Represented; made explicit", and SR-48 indexes TNP-007 and TNP-016. DEC-058's decision 3 ("each stating only what no requirement states") was overstated for TNP-027 and for CAP-047's opening | Documentation issue (false claim) | Blocking | New | DEC-045, decision 2; owner decisions 9, Rules 5, 10, and 24; DEC-051's corrected reading | Point 14, the gap row, and TNP-027's classification row, in the words the review specified; and the optional part: TNP-027 opens with TNP-007 and TNP-016, DEC-058's "Extends" column the same, and its decision 3 says "or states only in general terms" | Fixed; the optional part changes a requirement and a decision, so run 2 reviews it |
| E-03 | 1 | The status report's question 3 cited the project state's "Current task" as "this audit"; in the change, that row names item 5 | Documentation issue (stale) | Blocking | New | DEC-045, decision 2; DEC-057, decision 6 | "this audit until its commit, and item 5 from then on" | Fixed (DEC-045, decision 5) |
| E-04 | 1 | The ten checks' 2 and 5 gave 20:52 UTC; the session record shows the branch list read at 20:51:49 to 20:51:50 and the pull requests at 20:51:50 to 20:51:51 | Documentation issue (false) | Blocking | New | DEC-045, decision 2; DEC-057, decision 6 | 20:51 UTC in both | Fixed (DEC-045, decision 5) |
| E-05 | 1 | TNP-016's configurable threshold was checked only as a floor; at the upper end, TNP-028 says that an unusually large opportunity is never rejected for its size | Documentation issue (incomplete) | Non-blocking | Related to E-02 | — | The contradictions table's TNP-016 row, in the words the review specified; DEC-058's second reading extended to the upper end: TNP-027 and TNP-028 bind the platform's own logic and defaults, not the operator's explicit hard constraints, which rank above them (RSK-004, RSK-049) | Fixed; DEC-058's text changes, so run 2 reviews it |
| E-06 | 1 | ARB-010's kill-switch triggers ("unexpected spreads", "market anomalies"), one of the 46 hits, were filed under "Other subjects" | Documentation issue (incomplete) | Non-blocking | New | — | A row of its own, in the words the review specified | Fixed |
| E-07 | 1 | "Failures and fixes" said that each of four lines (OPP-022, TNP-028, TNP-029, CAP-048) opens with the requirements it extends; OPP-022 and CAP-048 open with fewer than DEC-058's table names, as CAP-049 does | Documentation issue (overstated) | Non-blocking | New | — | "opens with requirements it extends; DEC-058's table names all of them" | Fixed |
| E-08 | 1 | "The draft reconciled" left out that CAP-047 adds TNP-021 to those it names | Documentation issue (incomplete) | Non-blocking | New | — | "adds CAP-006 and TNP-021 to those it names" | Fixed |
| E-09 | 1 | "Expected dollar profit" was called a rejected duplicate, though TNP-030 and CAP-047 use it | Documentation issue (inaccurate) | Non-blocking | New | — | The final report's item 5, in the words the review specified | Fixed |
| E-10 | 1 | V-43 might overlap V-14's position-protection rules (RSK-016, RSK-017) | Non-blocking improvement | Non-blocking | Related to E-01 | — | V-43's note: "Emergency handling keeps its own rules (V-14)" (E-01) | Fixed |
| E-11 | 1 | SR-48's name, "no percentage floor or ceiling", left out "artificial", which the requirements it indexes, the directive, and SR-19 keep | Documentation issue (overstated) | Non-blocking | Related to E-02 and E-05 | — | "no artificial percentage floor or ceiling", in SR-48 and in DEC-058's decision 5 | Fixed; DEC-058's text changes, so run 2 reviews it |
| E-12 | 1 | "Each new requirement states what the directive itself says" was overstated: some content comes from established requirements or is the builder's (CAP-049's deciders, TNP-029's placement and market impact, PFC-019's recorded market data, the values' classes and their behaviour until set) | Documentation issue (overstated) | Non-blocking | Related to E-01 | — | "or what an established requirement it cites determines", in this record and DEC-058's decision 7; DEC-058's "Decided by" and its decision-log row name the values' classes and their behaviour until set | Fixed; DEC-058's text changes, so run 2 reviews it |
| E-13 | 1 | TNP-029 did not say who supplies the sizes it evaluates (TNP-017; RSK-011) | Non-blocking improvement | Optional | New | — | "across the sizes at which it could be executed, which the trading system supplies (TNP-017)" | Fixed; it changes a requirement's text, so run 2 reviews it |
| E-14 | 1 | Three wording points: (a) DEC-058's decision 3 gave "would mix two sources in one line" as the reason not to reword, though owner decisions 5 reworded three requirements with no change of source; (b) the final report's item 10 said six phrases "could be read against the directive", two of which only map its terms; (c) DEC-058's decision 8 left out the draft's two explanatory paragraphs | Documentation issue (imprecise) | Optional | New | — | (a) "would mix the directive's source into the line or attribute its words to the earlier source", in decision 3 and the second alternative; (b) the words the review specified; (c) decision 8 names them | Fixed; (a) and (c) change DEC-058's text, so run 2 reviews them |

- **Run 2:** PENDING.

## Failures and fixes

| Failure | Cause | Fix | Re-run |
|---|---|---|---|
| Verification 2's duplicate search: CAP-047's further ranking considerations, as drafted, repeated strategy health (CAP-006) and opportunity expiration (CAP-006's opportunity duration, CAP-043's time sensitivity) | The draft listed the directive's ranking terms against CAP-043 and TNP-015 only | Both left out of CAP-047, which names CAP-006 among the requirements it extends ("The draft reconciled") | Checks 1 and 3 |
| Verification 1's read-back of DEC-058: decision 3 said that each new requirement names the requirements it extends; OPP-022, TNP-028, TNP-029, and CAP-048 did not | Written from the draft's other lines, not read against each | Each of the four now opens with requirements it extends; DEC-058's table names all of them | Checks 1 and 3 |
| Verification 2's sweep: the roadmap's current position still said that items 4 and 5 come next | A statement of what comes next, outside the project state | Item 4 done (DEC-058), item 5 next. Class sweep: "item 4" and "items 4 and 5" in the current documents (`git grep`); the others are the owner's order, true as stated, or dated records | Check 1 |
| Verification 1's read-back of this record: it said that five requirements of the draft (then six) already named what they extend, that the draft's two restatements were removed before its commit, that the code's only size limits were two values, and its Scope's list of the project state's changes was incomplete | Written from memory of the draft and of the code | Restated from the draft's text (five lines; the restatements removed between its first and second versions), from the code and its contract schemas, and from the diff | Checks 1 and 4 |
| Gate 3 run 1: four blocking findings (E-01 to E-04) | E-01: CAP-049's deciders were written from the directive's actions, DIR-004, and RSK-017, without a search for every requirement that gives a control authority over open positions; E-02: the gap was stated against the requirements that name a ceiling (TNP-012 and TNP-026, a daily one), not against those that exclude a universal percentage rule in general terms (TNP-007, TNP-016); E-03: the status table was written before the project state's "Current task" was changed to item 5; E-04: the time of the last check, check 8's search (20:52 UTC), was given to checks 2 and 5 | The wording run 1 specified, for E-05 to E-14 too, with RSK-045 named in V-43's note and the gap row as in CAP-049, and E-13's wording keeping "at which it could be executed". E-01, E-02's optional part, E-05, and E-11 to E-14 change requirements' text or DEC-058's, so run 2 reviews the fixes (DEC-045, decision 5). Class sweep for E-02: every statement that the ten requirements state what none stated, or only the directive's words (`git grep`, and `grep` in the two new files): six in the project state, one each in the decision log and the traceability README, and Verification 2's above, now corrected | Checks 1 to 6; run 2 |
| Verification 1's read-back of run 1's fixes: SR-49's related systems still named only the Risk Engine's emergency handling (RSK-017) among the controls over open positions, and DEC-058's second reading ranked the operator's hard constraints by RSK-004 alone, which RSK-049 refines | E-01's class swept only in the lines the review named | SR-49 names SYS-09 for the risk controls CAP-049 names and SYS-14 for the canary stop (STR-017); the reading cites RSK-004 and RSK-049 | Checks 1 and 3 |

## Final status and remaining issues

PENDING.

## Environment

System Python 3.11 (`python3`) for the documentation tools; git; GitHub's branch list, pull requests, and workflow runs, read through the session's GitHub tools.
