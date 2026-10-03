# Master Knowledge-Base Integrity Audit — 2026-10-02

> **Status:** ACTIVE record of the pre-implementation audit the owner asked for on 2026-10-02 (the request is quoted in full in appendix B). It is the complete documentation review that handoff §101 and P2§329 require before implementation. Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md); format: [traceability README](README.md).
>
> **Verdict: B — READY WITH NON-BLOCKING FINDINGS** (for Stage 1 planning). No critical or high finding. Four items need the owner's decision (CF-20, CF-21, OQ-28, DUP-40); none blocks Stage 1 planning. Implementation is not authorized.

## Identity

- **Date:** 2026-10-02 (audit); fixes after Gate 3 and the commit 2026-10-03
- **Stage:** FOUNDATION — documentation initialization (before Stage 1)
- **Starts from:** commit `74928b4`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope and method

**Audited:** the whole repository as one knowledge system: Handoff Parts 1 to 3; the owner's correction, decisions, and directives; the four builder texts; 35 decision records; 733 requirements in 47 sets across 34 systems; the findings and open-question registers; the system registry, dependency map, source-of-truth map, glossary, values register, and System Rules Register; the roadmap; the traceability maps and verification records; the project state; the documentation tooling.

**How:** scripted checks over every active document (listed under "Checks"), then reading of the requirements, decisions, and notes each check pointed to. The seven decisions named in the request were traced through every active document. Seven handoff sections, chosen at random, were compared word by word with the requirements they map to. The sampled sections and the duplicate-scan script are given so the checks can be repeated (checks 3 and 11; appendix A).

**Changed by the audit:** only documentation that applies decisions already made, plus four new register entries for the owner (CF-20, CF-21, DUP-40, OQ-28). No requirement was added, removed, reworded, or reclassified (check 4). The changes are listed under "Changes made during the audit".

**Not verified here (UNVERIFIED in this audit):**

- that every sentence of Parts 1 to 3 is carried into a requirement. Each part was verified when it arrived (the [Part 1](part-1-verification.md), [Part 2](part-2-verification.md), and [Part 3](part-3-verification.md) records); this audit re-checked 7 sections by sample, all faithful, and confirmed that the preserved texts are unchanged since adoption (their hash check);
- anything about running software: no platform code, configuration, schema, test, deployment, or monitoring exists.

## Results by audit area

Numbers refer to the sections of the request.

**1. One knowledge system.** The repository is one connected set: every document is reachable from the indexes, every ID referenced anywhere is defined, every link resolves, and each requirement's text exists in exactly one specification (checks 1 and 3). The original handoffs and the owner's correction, decisions, and answers are kept verbatim as HISTORICAL sources under `docs/handoffs/`; the four builder texts, the owner's directive of 2026-10-01 among them, are kept verbatim as ACTIVE rules under `docs/builder/`; the specifications are the operating knowledge.

**2. Duplicates.** The registers hold 39 resolved duplicate findings (DUP-01 to DUP-39), each giving one owner. A fresh sweep found:

| Suspected duplicate | Class (A–F of the request) | Result |
|---|---|---|
| ARCH-031 and ARCH-040 (traceability chains) | C, parent/child | ARCH-040 extends ARCH-031 ("In addition to") |
| MODE-003 and POL-008 (operating modes) | D, specialization | MODE-003 defines per-strategy modes; POL-008 assigns their ownership to the Policy System |
| AUD-006 and MON-009 (logs vs audit trail) | B, two parts of one rule | Cross-referenced halves of one rule, each stating its part |
| HLT-001, HLT-007, and HLT-011 (three pairs); RSK-004 and RSK-048, RSK-048 and RSK-049; AGT-001 with AGT-016 and with AGT-017 | E, historical/replaced | The older one is DEPRECATED / REPLACED or mapped by the newer |
| CAP-003 and PLT-005; PERF-004 and PERF-019; PAP-012 and RDY-003 | A, genuinely separate | Similar words, different rules |
| RSK-004 and RSK-049 | D, refinement | RSK-049 places security above the user hard constraints that RSK-004 ranks; a pointer now links them (A-15) |
| MKD-007 and TEC-012 (market-data retention); MON-009 and TEC-012 (operational-log retention, found by the Gate 3 re-run; the scan cannot find it, V-19) | F, accidental | Same values stated twice with different classes: **DUP-40**, OPEN |
| The arbitrage opportunity database (ARB-003, ARB-014) vs the platform-wide Opportunity Database (OPP-016) | E, decided by DUP-26 | Arbitrage Intelligence's boundary still claimed to own the database (found by Gate 3): corrected to the arbitrage view (DEC-024) |
| Named components (Fee Engine, Slippage Engine, Rebalancing Engine, Eligibility Engine, AI Resource Governor, Governance and Readiness Engine, Opportunity Database) | C | Each is a recorded component or alias of one registered system |
| The constitution's authority names (Risk, Portfolio, Policy Authority; Audit System) | B | Same systems under other names; four were missing from the glossary although DEC-033 says they are there: added |
| State names used by several state machines and outcome vocabularies | B/D | TC-10 (open by design) listed some. Missing names added: RESEARCH, PAPER, VALIDATING; EMERGENCY, DEPRECATED (found by Gate 3); UNKNOWN, UNCERTAIN, ROLLBACK (found by the Gate 3 re-run). PRODUCTION and RETIRED were listed, but only as lifecycle states; their other uses were added |

No second system, authority, data store, or decision record for one responsibility was found. The stale statements of ownership of the arbitrage database are corrected: Arbitrage Intelligence's boundary (found by Gate 3), and the dependency map's D-31 row and the Performance Controller's inputs (found by the Gate 3 re-run).

**3. Conflicts.** All 19 recorded conflicts are resolved. A fresh sweep of the areas the request names (authority, security, user policy, risk, capital, execution, strategy, AI, safety, readiness, recovery, rebalancing, lifecycle, deployment, production, paper, canary, future features) found two new conflicts (CF-20; CF-21, found by Gate 3) and several wording issues:

| Conflict | Statements and sources | Canonical decision | Action | Owner needed |
|---|---|---|---|---|
| **CF-20** (new) | MIG-001, MIG-002, PLT-017 (local hosting must be supported, the user is not forced into one hosting architecture) vs the owner's audit request, §16 (production "must NOT depend on … the user's laptop"); related, and in line with the request: MIG-004, GOV-023 | None yet. Of three readings, existing requirements already meet two (DEC-030, OPS-017, MIG-004; GOV-023, PLT-029); it may be only an ambiguity | Recorded in the findings register with a recommended reading | **Yes** |
| **CF-21** (new, found by Gate 3): "withdrawal" in PLT-010 and Capital Management vs rebalancing transfers (SEC-006, SEC-007, CAP-023) | PLT-010 drops DEC-006's "for others"; DEC-019 | OC-1 item 4 and SEC-006: three separate authorities; the platform holds no *general* withdrawal or custody authority | Capital Management's note now quotes SEC-006; aligning PLT-010's wording changes a requirement, so it is recorded as CF-21 | **Yes** (or delegate) |
| Paper results vs automatic canary (PAP-012 vs STR-014, MODE-007) | P2§350 vs DEC-019 | Readiness decides, never paper results alone, within the operator's maximum mode (RDY system "Must not", MODE-007, POL-005) | None: consistent | No |
| Failover "FUTURE until approved" (platform overview note) vs DEC-030 | Builder note vs owner decision | DEC-030 approved high availability | Note corrected | No |

**4. The seven decisions.**

| Decision | Canonical requirement | Result |
|---|---|---|
| CF-17: non-bypassable security above user policy | RSK-049 (RSK-048 replaced); SR-02 | Consistent in every active document. A pointer from RSK-004 to RSK-049 was added where RSK-004 is defined |
| CF-18: growth reassesses capability; scales only within authorized policy after readiness; growth creates no authority; raising a bound needs the owner | CAP-034, PLT-023, RDY-013, POL-005 (the operator's explicit confirmation; reading the operator as the owner: PLT-010 names a single operator, DEC-006 speaks of "the operator's own accounts", and the project state tells the owner that widening a bound "still needs you (POL-005)"; no requirement says it in words); reading in Capital Management | Consistent. The confirmed reading lives in a note and in SR-20 and SR-26 rather than in one requirement; acceptable, since every element is a requirement |
| CF-19: the constitution's feature lifecycle is canonical | GOV-024 (GOV-018 replaced) | Consistent. Part 3's names are mapped, not kept as a second lifecycle |
| TC-08: alternatives backfilled only where sourced | DEC-001 to DEC-030 | Done in commit `74928b4`, with its [verification record](tc-08-alternatives-verification.md) |
| DUP-34: the Rebalancing Engine is a component of the Global Capital Authority | CAP-037 to CAP-042 (CAP-042: not a second capital authority) | Consistent in the registry, glossary, maps, and roadmap |
| DUP-35: one safety-level hierarchy; Part 3's names mapped onto it | RSK-015; the mapping note in the Risk Engine; glossary | Consistent |
| OQ-27: Parts 1 to 3 are the complete initial handoff; later additions remain possible | OQ-27, DEC-035; GOV-021, GOV-022 | Consistent; the second half was implicit. A note in Architecture governance now says it |

No active document still asserts the opposite of any of them. The remaining hits are historical text under status lines or "Later changes" notes.

**5. Completeness.** Every area in the request has a canonical home; see the consistency matrix below. Areas whose detail is deliberately left to stage planning are listed as finding A-05 (33 documents carry an explicit "Not yet specified" line: interfaces, schemas, tests, failure procedures).

**6. Classification.** The repository's classes map onto the request's categories as follows:

| Request's category | Repository's equivalent | Count or location |
|---|---|---|
| Confirmed requirement | CONFIRMED REQUIREMENT, SYSTEM REQUIREMENT | 221 + 150 |
| Principle | CONFIRMED ARCHITECTURAL PRINCIPLE | 140 |
| Hard constraint | CONSTRAINT; for values, HARD LIMIT in the values register | 187 |
| System rule | An entry of the System Rules Register (SR-01 to SR-47), which indexes requirements | 47 |
| User policy | The Policy System's runtime store (POL-009); not kept in the repository | — |
| Architectural decision | A decision record (DEC-001 to DEC-035) | 35 |
| Implementation decision | IMPLEMENTATION CHOICE | 11 |
| Proposal | PROPOSED (ARCH-034) | 1 |
| Recommendation | "RECOMMENDED — NOT YET APPROVED" in the registers | Proposed resolutions; CF-20, CF-21, DUP-40, OQ-28 open |
| Future capability | FUTURE (CUS-001, CUS-002, LED-008: custody; EXE-011: adaptive execution) | 4 |
| Open question | OQ entries and TC entries | OQ-28, TC-09, TC-10 open |
| Requires human confirmation | PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | 0 left; all were decided |
| Deprecated, superseded | DEPRECATED / REPLACED, each naming its replacement | 19 |
| Historical information | HISTORICAL banners (docs/handoffs/); "Later changes" notes on older records | 7 verbatim sources |

Checks: no requirement worded "where approved", "if approved", "remains a proposal", or "previously discussed" is classed as confirmed except where the condition is itself the rule (CUS-005, ARCH-029) or has since been decided (PLT-017, RMP-008: failover, approved by DEC-030). The roadmap places no PROPOSED or FUTURE entry in a build stage (its "Not in any stage" line); the registry's default stage is only the owning system's. 80 requirements rest on decisions the owner delegated to the builder (finding A-16).

**7. Authority and ownership.** One owner for each responsibility the request names:

| Responsibility | Canonical owner | Rule |
|---|---|---|
| System safety | The safety floor in the Risk Engine (SYS-09), with System Health (SYS-29) owning platform health state; together the "global safety architecture" | RSK-034, RSK-010, RSK-008, HLT-010, HLT-011 |
| Security | SYS-31 Security Architecture; ranks above user policy | SEC-001 to SEC-009, RSK-049 |
| User policy | SYS-12 Policy System (the natural-language interface is not the authority) | POL-002, POL-009, NLP-003 |
| Risk | SYS-09 Risk Engine | RSK-001, RSK-012 |
| Capital | SYS-07 Global Capital Authority | CAP-001, CAP-017 |
| Rebalancing | SYS-07 decides (its Rebalancing Engine); Arbitrage Intelligence (SYS-20) evaluates; the Execution Engine (SYS-10) executes transfers | CAP-018, CAP-023, CAP-042, ARB-006, EXE-009 |
| Execution | SYS-10 Execution Engine | EXE-001, ARCH-037 |
| Strategy | SYS-14 Strategy Management (Strategy Registry, lifecycle) | STR-001, STR-023 |
| Portfolio | SYS-08 Portfolio Management (capital read-only) | PRT-001, PRT-004 |
| Reconciliation | SYS-11 Recovery and Reconciliation | REC-008 |
| Readiness | SYS-34 Readiness System | RDY-001, RDY-006 |
| Recovery | SYS-11 (restart and service recovery, the execution lease); kill-switch recovery in SYS-09 | REC-013 to REC-018, REC-025, RSK-021 to RSK-025 |
| AI | No authority: AI provides intelligence, deterministic systems decide; the AI gateway (SYS-22) controls access | PLT-016, ARCH-019 to ARCH-022, AIL-006 |
| Governance and consistency | Architecture governance (GOV), the documentation checker | GOV-001 to GOV-024, ARCH-032, DEC-025 |

Specialized components analyse without deciding: Arbitrage Intelligence evaluates rebalancing but the Global Capital Authority decides (DUP-06); the Market Analyst interprets but never sets regime state (RGM-006); the Performance Controller detects but the Risk Engine restricts (PFC-008, PERF-011); AI agents propose but never authorize (AIL-003, AIV-009, RSK-039).

**8. Sources of truth.** The [source-of-truth map](../architecture/source-of-truth-map.md) answers every item the request names. Nine rows were missing and are added, each pointing to existing requirements: security; reconciliation; deployment definition and configuration; production version and change record; database schemas; AI gateway and routing; risk-limit values; feature lifecycle; platform lifecycle. (Gate 3 found that the first draft of the configuration row contradicted MIG-010 and that two rows repeated existing ones; both fixed.) Two of them are honestly incomplete and say so: database schemas (per system, with the interface contracts) and where the runtime release record is kept (OPERATIONALIZATION). No item has two competing canonical sources.

**9. Traceability.** Every requirement traces to its source (a handoff section or a decision record), its owning system and specification, and a build stage (or "platform-wide" / "None (FUTURE)"); every system rule traces to its enforcement point (System Rules Register). The chain stops there: no implementation, configuration, test, verification matrix, release, or monitoring exists yet. The verification matrix, stage record, and completion certificate start at Stage 1 (DEC-033; [traceability README](README.md)). The only code, `tools/docs/`, traces to DEC-025. One documentation claim was not supported by the repository (DEC-033: the glossary holds the constitution's authority names; four were missing) and is fixed.

**10. Deterministic vs AI boundary.** Deterministic systems own market data, calculations, capital, risk, order validation, execution, reconciliation, safety, and accounting (ARCH-019, ARCH-020, ARCH-021). AI is confined to analysis, research, interpretation, hypotheses, and proposals (ARCH-022, AIL-001). It cannot bypass risk, raise authorized risk, disable kill switches, override user restrictions, place unrestricted orders, deploy unvalidated strategies, or receive unrestricted secrets (AIL-003); arbitrage is deterministic end to end (ARB-013); invariants change only through a human-controlled change that AI may propose but never authorize (RSK-039); AI agreement cannot override deterministic safety (AIV-009, AIV-014). No contradiction found.

**11. Capital authority.** One authority and one capital state (CAP-001). Categories cover available, reserved, deployed (committed to positions), pending orders, pending release, partial fills, per exchange and per strategy (CAP-002), at risk, pending settlement, and unavailable (CAP-044); buckets and reserves (CAP-029 to CAP-033, CAP-045); reservation and release (CAP-004, CAP-016, CAP-021); productivity and competition for capital on a common basis (CAP-017, CAP-043, TNP-021); venue exposure (CAP-025, PRT-002, RSK-002). Portfolio reads capital (PRT-004); the arbitrage reserve lives inside it (ARB-009); the Rebalancing Engine is a component (CAP-042); paper trading's simulated capital is the same authority in the separate paper environment (PAP-007, PAP-013). No competing capital authority.

**12. Security.** Security ranks above user policy (RSK-049); least privilege for AI (SEC-008); AI credentials only in the AI gateway, separate from trading credentials (SEC-004, AIL-006); secrets never in the repository, logs, or AI prompts (SEC-005); trading, rebalancing-transfer, and withdrawal/custody authorities use separate credentials, and transfer credentials are allowlisted (SEC-006, SEC-007); only production holds trading credentials, so research and paper are technically unable to trade (MODE-006, SEC-004, PAP-013). The security set is complete for this stage; its implementation details are open (A-05).

**13. Safety, risk, health, readiness, recovery.** Kept apart: safety level (RSK-015), risk decisions (RSK), platform health (HLT-011, which separates health from the safety level), readiness (RDY-004, RDY-017), restart recovery (REC-014 to REC-018) and kill-switch recovery (RSK-021 to RSK-025). One safety hierarchy (RSK-015, DUP-35). Restart is not resume (REC-025); persisted state is untrusted until compared with external state (REC-014); unknown is never success (ARCH-042, EXE-008, EXE-009); recovery reconciles balances, positions, orders, reservations, and transfers and revalidates risk and capital (REC-015, REC-018); positions are never closed blindly (RSK-017) and safety actions are scoped (RSK-020, RSK-038); latched causes need explicit authorization (RSK-022). Gap: how a half-completed cross-exchange or triangular trade is handled is not yet specified (A-05).

**14. Performance.** First-class (PERF-002) with hot and cold paths (PERF-019), event-driven and incremental processing, caching, connection reuse (PERF-005), backpressure with bounded queues (PERF-014, PERF-021), persistent WebSockets (EXA-012, EXA-014), latency decomposition and path budgets (PERF-008, PERF-009), p50 to p99.9 measurement (PERF-010), throughput and load testing (VER-001, VER-002), resource isolation (PERF-016), concurrency safety (PERF-013, PERF-022), and no unsafe fast path (PERF-023, CAP-021). No values are invented (PERF-018).

**15. Feature extensibility.** The canonical process is GOV-002 with GOV-022, under GOV-021 and GOV-024. Every step of the request's sequence is one of their steps; the mapping is now written in [Architecture governance](../architecture/architecture-governance.md).

**16. Platform independent of Claude Code.** PLT-029, OPS-021, GOV-021 to GOV-023 (DEC-034); production rebuilt without the owner (OPS-017); 24/7 within limits (OPS-018). Session continuity: the [project state](../project-state.md) (its continuation contract, Recent decisions, Next approved step) covers stage, completed work, work in progress, remaining work, blockers, decisions, verification, repository and documentation state, and next action (a documentation-state row was added to the contract). Tests are covered by its "Verified" and "Not verified" rows: the only tests today are the tools' self-test, and platform tests start with Stage 1. The one open point is CF-20 (the owner's computer as a production host).

**17. Maintenance and upgrades.** GOV-021 lists bug fixes, features, strategies, exchanges, data sources, AI models and agents, performance, security, infrastructure, migrations, API upgrades, monitoring, recovery, deployment, architecture, and technical debt; GOV-022 makes each an upgrade of the existing platform, never a rebuild; GOV-006 governs schema and API versioning.

**18. Roadmap.** One roadmap (RMP-003), seven sequential stages (RMP-002), dependency order (RMP-011), production hardening before production (RMP-010), every requirement placed. No stage yet has its objective, scope, tests, verification, and completion criteria (constitution Rule 140): they are written when each stage is planned, so Stage 1's are the next deliverable (A-04).

**19. Three verification passes.** Defined once for all work (DEC-032, DEC-033; `CLAUDE.md`), with the record format in the [traceability README](README.md); since `b850eaa` every checkpoint has a verification record with three distinct passes, and since `a2c8e92`, when the owner's checkpoint rule was adopted (DEC-032), Gate 3 has had an independent reviewer. The builder's first commit, `16d317c`, predates the rule and has no record (the repository's first commit, `7172a5c`, is the owner's one-line README).

**20. Repository structure.** The actual tree matches DEC-002's derived structure plus `docs/builder/` (DEC-001) and `tools/docs/` (DEC-025). No misplaced, duplicate, orphaned, or stray file; the root holds only `README.md`, `CLAUDE.md`, and `.gitignore`. Stale forward references in older records (to Part 2 and OQ-15) now carry "Later changes" notes, and the roadmap's Stage 5 entry for CAP-028 names its replacements.

**21. Documentation quality.** Every specification states its status, owner, sources, stage, and gaps; the indexes are generated and checked. Fixed: the items in "Changes made during the audit". No history was rewritten: older records keep their text, with status lines or "Later changes" notes added.

**22. Implementation vs specification.** No platform implementation exists. The only code is the documentation tooling (`tools/docs/`: generator, comparison, self-test), which traces to DEC-025 and is checked by its self-test, ruff, and mypy. Nothing is called implemented, verified as software, or production-ready.

## Findings

| ID | Severity | Category | Issue | Affected | Why it matters | Evidence | Resolution | Owner decision | Blocks |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | MEDIUM | Conflict | Local hosting vs production independent of the owner's computer (**CF-20**) | MIG-001, MIG-002, PLT-017 vs the owner's audit request; related: MIG-004, GOV-023, DEC-030, OPS-017 | Decides whether production may run on the owner's machine | MIG-001's text; request §16 | Recommended reading in CF-20 | **HUMAN DECISION REQUIRED** | Not Stage 1; before OPERATIONALIZATION is planned |
| A-02 | MEDIUM | Ambiguity | Whether instrument scope includes derivatives beyond perpetual futures and margin (**OQ-28**) | DEC-007, PLT-011, OQ-04 | Defines the risk model of CORE | DEC-007 records "all three instrument types"; the question asked is not recorded | Confirm PLT-011, or name more types | **HUMAN DECISION REQUIRED** | Not Stage 1; before CORE is planned |
| A-03 | LOW | Duplicate | Retention values stated twice with different classes: market data in MKD-007 and TEC-012, and (found by the Gate 3 re-run) operational logs in MON-009 and TEC-012 (**DUP-40**) | MKD-007, MON-009, TEC-012 | Two places to keep in step | The requirement lines; V-18, V-19 | MKD-007 and MON-009 refer to TEC-012; MKD-007 takes its class; by decision record | **HUMAN DECISION REQUIRED** (or delegate) | No; before DATA FOUNDATION at the latest |
| A-04 | MEDIUM | Roadmap | No stage has its Rule 140 fields yet | Roadmap | Stage 1 cannot be implemented without them | Roadmap note above the stage table | The Stage 1 plan, for the owner's approval | Approval of the plan | Blocks Stage 1 implementation, not planning |
| A-05 | MEDIUM | Missing detail | Interfaces, schemas, tests, and failure procedures are not yet specified for any system (33 "Not yet specified" lines), including one-leg failure in cross-exchange arbitrage and partially completed triangular routes | All specifications | Later stages cannot be built without them | The "Not yet specified" lines | Specified when each stage is planned (ARCH-025, ARCH-030) | No | Each stage's implementation until specified |
| A-06 | MEDIUM | Open question | TC-09 (standby trading keys) and TC-10 (shared state names) stay open | Registers | Affect OPERATIONALIZATION and CORE design | The register rows | Decided when their stages are planned | Later | No |
| A-07 | LOW | Duplicate terms | TC-10's inventory missed RESEARCH, PAPER, VALIDATING; EMERGENCY and DEPRECATED (found by Gate 3); UNKNOWN, UNCERTAIN, ROLLBACK (found by the Gate 3 re-run); and the non-lifecycle uses of PRODUCTION and RETIRED | TC-10, glossary, project state | Incomplete input to the later decision | MODE-001, RDY-004, STR-024, MIG-014, OPS-004, GOV-009, RGM-002, RGM-005, RGM-007, ARCH-042, RSK-006, RSK-014, AIV-013 | Added; the inventory stays a working list until TC-10 is decided | No | Fixed |
| A-08 | LOW | Documentation claim | Four constitution authority names were missing from the glossary, though DEC-033 says they are there | Glossary | Unsupported claim | DEC-033 decision 5 | Added as aliases | No | Fixed |
| A-09 | LOW | Stale | The platform overview said failover stays FUTURE until approved | Platform overview | Contradicted DEC-030 | DEC-030 | Corrected | No | Fixed |
| A-10 | LOW | Terminology | "The platform itself withdraws nothing" was ambiguous next to rebalancing transfers | Capital Management | Could mislead the transfer design | SEC-006, OC-1 item 4, CAP-037 | Reworded, quoting SEC-006 ("no general withdrawal or custody authority"); CAP-030's constraints also cover venue restrictions (CAP-037); DEC-028's note marked as refined | No | Fixed |
| A-11 | LOW | Stale | Part 1 gap notes listed items since specified: Market Data, and (found by Gate 3) Arbitrage Intelligence's kill-switch reset | Market Data, Arbitrage Intelligence | Misstated what is open | MKD-007, MKD-012, HLT-011, PERF-008; RSK-008, RSK-021 to RSK-025 | Pointers added; still-open items named | No | Fixed |
| A-12 | LOW | Source of truth | Nine concepts had canonical requirements but no row in the source-of-truth map | Source-of-truth map | "Where is the source of truth?" unanswered for them | The added rows | Added | No | Fixed |
| A-13 | LOW | Stale | Older decision records still expected interface contracts from Part 2 or waited on OQ-15; the OC-1 verification record still showed CF-11 to CF-13 as open; the Part 1 record did not say Parts 2 and 3 had arrived; resolution notes for OQ-07, OQ-08, OQ-09, OQ-19 named requirements since replaced without saying so (found after Gate 3), and so did CF-09's status line (found by the Gate 3 re-run, which also widened the OQ-07 pointer to RSK-016, RSK-017, and RSK-020) and the system registry's SYS-29 and Canary entries (found by the builder's own pass after the re-run) | Findings register, open-question register, system registry, System Health, Operating modes, DEC-002, DEC-010, DEC-011, DEC-012, DEC-014; OC-1 and Part 1 verification records | Read as still pending | DEC-024's consequences; DEC-015; DEC-021 to DEC-023; DEC-024, DEC-031 | "Later changes" notes added | No | Fixed |
| A-14 | LOW | Clarity | The owner's feature sequence and the open-ended meaning of OQ-27 were not written down | Architecture governance | The request asks for both to be explicit | GOV-002, GOV-021, GOV-022 | Notes added | No | Fixed |
| A-15 | LOW | Clarity | RSK-004 had no pointer to RSK-049 where it is defined | Risk Engine | A reader could take user hard constraints as second only to safety | RSK-004, RSK-049 | Pointer added | No | Fixed |
| A-16 | INFO | Approval | 80 requirements rest on decisions the owner delegated to the builder (63 under the instruction to resolve every open item, DEC-010 to DEC-018; 17 under the stack delegation, DEC-009); 30 more are partly builder-decided (the delegated or placement parts of DEC-006, DEC-008, DEC-028, DEC-030, DEC-033, DEC-034) | Registry "Approval" column | The owner may override any of them | Registry | None required | Optional review | No |
| A-17 | INFO | Provenance | The owner's first-round answers (DEC-006 to DEC-009) and the options shown with CF-11 to CF-13 are not recorded verbatim | DEC-006 to DEC-009, DEC-021 to DEC-023 | History can only be reconstructed from the records | [TC-08 verification](tc-08-alternatives-verification.md) | OQ-28 covers the one material consequence; nothing is reconstructed | No | No |
| A-18 | INFO | Traceability | The chain ends at the specification: no implementation, tests, verification matrix, release, or monitoring yet | All | Expected before implementation | Registry; traceability README | Starts at Stage 1 | No | No |
| A-19 | INFO | Approval | 512 handoff requirements read "pending documentation review" in the registry | Registry | This audit is that review | The registry's Approval column | Changed to "reviewed" once the owner accepts this review | **Owner's acceptance** | No |
| A-20 | LOW | Conflict | PLT-010's wording drops DEC-006's "for others" and so reads as forbidding the rebalancing transfers DEC-019 approved (**CF-21**, found by Gate 3) | PLT-010, DEC-006, SEC-006 | Wording a builder could misread | DEC-006 decision 1; SEC-006; DEC-019's reconciliation note | Align PLT-010 with DEC-006 by decision record | **HUMAN DECISION REQUIRED** (or delegate) | No |
| A-21 | LOW | Stale ownership | Arbitrage Intelligence's boundary still said it owns the arbitrage opportunity database (found by Gate 3); the dependency map's D-31 row and the Performance Controller's inputs still named it as Arbitrage Intelligence's (found by the Gate 3 re-run) | Arbitrage Intelligence, dependency map, Performance Controller | Contradicted OPP-016 and DUP-26 | OPP-016; DEC-024; D-57 | Corrected to the arbitrage view of SYS-05's Opportunity Database | No | Fixed |
| A-22 | LOW | Stale | The roadmap's Stage 5 entry still read "arbitrage capital categories if confirmed (CAP-028)" (found by Gate 3) | Roadmap | CAP-028 was replaced by CAP-029 to CAP-033 (DEC-028) | DEC-028; the registry's stage column | Corrected, naming the replacements and their stages (CAP-029 to CAP-031 and CAP-033 in Stage 3, CAP-032 in Stage 4; the first correction misstated them, found by the Gate 3 re-run) | No | Fixed |
| A-23 | LOW | Cross-reference | OQ-28 was cross-referenced only from the platform overview, though DEC-005 asks every affected specification to name an open finding (found by Gate 3) | Exchange adapters, Risk Engine, Capital Management, Portfolio | Readers of those specifications would not see the open question | DEC-005; EXA-009, RSK-013, CAP-020, PRT-005 | Cross-references added; CF-20 and CF-21 also named in the platform overview | No | Fixed |

No CRITICAL or HIGH finding.

## Consistency matrix

| Area | Status | Canonical source | Owner | Conflicts | Duplicates | Missing items | Action |
|---|---|---|---|---|---|---|---|
| Requirements | Consistent with one open point | Owning specifications; [registry](../requirements/registry.md) | Each system | CF-21 (wording) | DUP-40 | — | Owner: CF-21, DUP-40; accept review (A-19) |
| Architecture | Consistent | [Overview](../architecture/overview.md), [system registry](../architecture/system-registry.md) | Platform architecture | None | None | Interface contracts (A-05) | At stage planning |
| Governance | Consistent | [Architecture governance](../architecture/architecture-governance.md); builder texts | GOV set; DEC-033 | None | None | — | Notes added (A-14) |
| Security | Consistent | [Security architecture](../security/security-architecture.md); RSK-049 | SYS-31 | None | None | Implementation detail (A-05) | — |
| Risk | Consistent | [Risk Engine](../risk/risk-engine.md) | SYS-09 | None | None | Limit values (policy), contracts | Pointer added (A-15) |
| Capital | Consistent with one open point | [Capital Management](../systems/capital-management.md) | SYS-07 | CF-21 (wording) | None | Reservation timeouts, failure behavior (A-05) | Note reworded (A-10); owner: CF-21 |
| Rebalancing | Consistent | CAP-018, CAP-023 to CAP-025, CAP-037 to CAP-042 | SYS-07 (decides), SYS-20 (evaluates), SYS-10 (executes) | None | None (DUP-34 confirmed) | — | — |
| Execution | Consistent | [Execution Engine](../systems/execution-engine.md) | SYS-10 | None | None | Order types, retry policy (A-05) | — |
| Strategies | Consistent | [Strategy Management](../systems/strategy/strategy-management.md), [Directional](../systems/directional-trading.md) | SYS-14, SYS-17 | None | None | Validation thresholds per stage (V-33) | At DIRECTIONAL planning |
| Arbitrage | Consistent with gaps | [Arbitrage documents](../systems/arbitrage/arbitrage-intelligence.md) | SYS-18 to SYS-20 | None | None (stale ownership notes corrected, A-21) | One-leg and partial-route handling (A-05) | At ARBITRAGE planning |
| Market Data | Consistent with one open point | [Market Data](../systems/market-data.md) | SYS-02 | None | DUP-40 | Schemas, per-stream failure behavior | Note fixed (A-11); owner: DUP-40 |
| Quant | Consistent | [Quantitative Engine](../systems/quantitative-engine.md) | SYS-03 | None | None | Calculation definitions | At DATA FOUNDATION planning |
| Regime | Consistent | [Market Regime Engine](../systems/market-regime-engine.md) | SYS-04 | None | None | Classification rules | At DATA FOUNDATION planning |
| AI | Consistent | [AI documents](../ai/ai-architecture.md) | SYS-22 to SYS-27 | None | None | Providers and models (by measurement) | — |
| Backtesting | Consistent | [Backtesting](../systems/strategy/backtesting.md) | SYS-15 | None | None | Execution simulation model | At DIRECTIONAL planning |
| Paper | Consistent | [Paper Trading](../systems/strategy/paper-trading.md) | SYS-16 | None | None | Fill and latency models | At DIRECTIONAL planning |
| Canary | Consistent | STR-013 to STR-022, OPS-013 | SYS-34, SYS-14 | None | None | Canary values (V-01 to V-05) | — |
| Production | Consistent with one open point | [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) | Deployment set | CF-20 | None | Release-record location | Owner: CF-20 |
| Recovery | Consistent | [Recovery and Reconciliation](../systems/recovery-and-reconciliation.md), [reliability model](../operations/reliability-and-recovery-model.md) | SYS-11 | None | None | Mismatch procedures; TC-09 | At CORE / OPERATIONALIZATION planning |
| Monitoring | Consistent with one open point | [Monitoring and Observability](../operations/monitoring-and-observability.md), [System Health](../operations/system-health.md) | SYS-28, SYS-29 | None | DUP-40 (MON-009) | Alert channels, dashboards | Owner: DUP-40 |
| Performance | Consistent | [Performance](../architecture/performance-and-latency.md), [verification architecture](../architecture/verification-architecture.md) | Platform architecture | None | None | Measured budgets (none yet) | — |
| Testing | Defined, not started | DEC-032, DEC-033, VER set, the traceability README | Builder process; VER | None | None | Test strategy per stage | In the Stage 1 plan |
| Deployment | Consistent with one open point | OPS set, MIG set | Deployment set | CF-20 | None | IaC tool choice (later) | Owner: CF-20 |
| Maintenance | Consistent | GOV-021, GOV-022 | Governance | None | None | — | — |
| Upgrade | Consistent | GOV-006, GOV-021, GOV-022, OPS-020 | Governance | None | None | — | — |
| Feature lifecycle | Consistent | GOV-024 | Governance | None | None (CF-19 decided) | Where statuses are kept (Stage 1) | In the Stage 1 plan |
| Roadmap | Consistent after one fix | [Roadmap](../roadmap/roadmap.md) | RMP | None | None | Rule 140 fields per stage (A-04) | Stale CAP-028 entry fixed (A-22); Stage 1 plan next |
| Traceability | Consistent to specification level | Registry, reconciliation maps, System Rules Register | ARCH-030, ARCH-031, ARCH-040 | None | None | Implementation-to-verification links (A-18) | From Stage 1 |
| Documentation | Consistent after fixes | [Documentation index](../README.md) | DEC-002 | None | None | — | Fixes A-07 to A-15, A-21 to A-23 |
| Session continuity | Consistent | [Project state](../project-state.md) | Builder process | None | None | — | Documentation-state row added |

## Changes made during the audit

All apply decisions already made; none adds, removes, rewords, or reclassifies a requirement (check 4).

| Change | File |
|---|---|
| CF-20, CF-21, and DUP-40 added (OPEN, for the owner); summary lines updated; "since replaced" pointer on CF-09 | [Findings register](../conflicts/register.md) |
| OQ-28 added (OPEN, for the owner); TC-10's inventory extended; status line; "since replaced" pointers on OQ-07, OQ-08, OQ-09, OQ-19 | [Open-question register](../open-questions/register.md) |
| "Since replaced" pointers in resolution notes and registry entries | [System Health](../operations/system-health.md), [Operating modes](../product/operating-modes.md), [system registry](../architecture/system-registry.md) (SYS-29, Canary) |
| Four authority aliases; shared state names extended | [Glossary](../glossary.md) |
| Nine rows of canonical sources | [Source-of-truth map](../architecture/source-of-truth-map.md) |
| The owner's feature sequence mapped; OQ-27 meaning | [Architecture governance](../architecture/architecture-governance.md) |
| Pointer from RSK-004 to RSK-049; OQ-28 named in Findings | [Risk Engine](../risk/risk-engine.md) |
| Failover note brought in line with DEC-030; OQ-28, CF-20, and CF-21 named in Findings | [Platform overview](../product/platform-overview.md) |
| Withdrawal note quoting SEC-006; OQ-28 named in Findings | [Capital Management](../systems/capital-management.md) |
| Part 1 gap note: what has since been specified; DUP-40 named in Findings | [Market Data](../systems/market-data.md) |
| Boundary: the arbitrage database is a view of the Opportunity Database; Part 1 gap note: kill-switch reset since specified | [Arbitrage Intelligence](../systems/arbitrage/arbitrage-intelligence.md) |
| OQ-28 named in Findings | [Exchange adapters](../systems/exchange-adapters.md), [Portfolio](../systems/portfolio-management.md) |
| DUP-40 named in a new Findings section | [Technology stack](../architecture/technology-stack.md), [Monitoring and observability](../operations/monitoring-and-observability.md) |
| CF-20 named in a new Findings section | [Hosting and migration](../operations/hosting-and-migration.md), [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) |
| CF-21 named in a new Findings section | [Security architecture](../security/security-architecture.md) |
| The arbitrage opportunity database named as the arbitrage view of SYS-05's Opportunity Database (DUP-26) | [Dependency map](../architecture/dependency-map.md) (D-31), [Performance Controller](../systems/performance-controller.md) |
| Stage 5 entry for CAP-028 names CAP-029 to CAP-033 and their stages; header: review done | [Roadmap](../roadmap/roadmap.md) |
| "Later changes" notes | DEC-002, DEC-010, DEC-011, DEC-012, DEC-014, DEC-028; the [Part 1](part-1-verification.md) and [owner correction 1](owner-correction-01-verification.md) verification records |
| Audit result, open decisions, next step, documentation-state row, TC-10 row, checkpoint log | [Project state](../project-state.md), [documentation index](../README.md), [traceability README](README.md) |
| This record | — |

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | References, links, coverage, system rules, preserved texts, orphans; generated files current | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 733 requirements, 47 prefixes, 99 findings, 35 decisions, 34 systems, 47 system rules |
| 2 | The tools still fail on broken input; code checks | `python3 tools/docs/selftest.py`; `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS: 34 cases; clean |
| 3 | Each requirement defined once; no near-duplicate text | Script: every requirement line in every active document, IDs counted. Duplicate scan: appendix A (words of four or more letters, lowercased, from each requirement's title and text; replaced requirements included; pairs whose word sets both have at least 6 words and whose Jaccard index is ≥ 0.42 or whose overlap is ≥ 0.8 of the smaller set) | PASS: each ID once (the only extra match is the made-up format example in the requirements README); 15 similar pairs, each classified in area 2 |
| 4 | No requirement changed by the audit | `python3 tools/docs/compare_requirements.py 74928b4 --strict` | PASS: 0 added, 0 removed, 0 changed |
| 5 | The seven decisions everywhere | Searches of every active document for each decision's terms (for example "outrank", "user hard policy", "RSK-048", "GOV-018", "IN DEVELOPMENT", "Rebalancing Engine", "PROTECTIVE", "OQ-27", "Part 4"); each hit read | PASS: no active statement of the opposite |
| 6 | Named systems and authorities | Script: every "… Engine / Authority / Manager / Registry / System / …" name in active documents checked against the system registry, glossary, and source-of-truth map | PASS after A-08: every name is a registered system, component, agent, or alias |
| 7 | State names shared across state machines | Script: upper-case state names in every requirement whose title or text defines states, levels, modes, statuses, environments, or lifecycles | PASS after A-07: the inventory was extended twice after Gate 3 found more names, and now covers outcome and result vocabularies too; it stays a working list until TC-10 is decided |
| 8 | Confirmed requirements with conditional wording | Script: "where approved", "if approved", "requires approval", "remains a proposal", "previously discussed", "future feature", "optional" in non-PROPOSED, non-FUTURE requirements | PASS after A-09: each hit is a rule about the condition, or decided since |
| 9 | Active requirements citing replaced ones | Script: references to DEPRECATED / REPLACED IDs in active requirement text, and a replacement note in the same document | PASS: 9 cases, each noted or a deliberate carry-forward (OPS-014) |
| 10 | Coverage of the request's areas | Keyword scan of all requirement texts for each area of sections 5 and 11 to 14, then reading of the hits | PASS: every area has requirements; gaps are A-05 |
| 11 | Sampled fidelity to the handoffs | P3§393, P3§398, P3§474, P3§527 and P2§96, P2§196, P2§244 (chosen at random) compared with their mapped requirements (PFC-013, PFC-016; PERF-014, PERF-021; GOV-016; RDY-016; ARB-015; ARCH-019; MIG-009) | PASS: 7 of 7 faithful |
| 12 | DUP proposals cited as first recorded | First four columns of DUP-01 to DUP-22 at `b850eaa` vs now | PASS: 22 of 22 identical |
| 13 | No platform code; root clean | `git ls-files` | PASS: only `.gitignore` and `tools/docs/` besides Markdown |
| 14 | Hygiene | `git diff --check`; `git status --short --ignored`; scan for secrets, local paths, model identifiers | PASS |
| 15 | The request kept verbatim | The appendix extracted by script from the session's message and compared byte for byte | PASS: 22,099 characters identical |

Environment: Python 3.11, ruff 0.15.8, mypy 1.19.1, git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 to 15 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | FAIL, then PASS on re-run: see below |

### Gate 2 — architecture and consistency (builder)

- **No decision changed.** Every fix applies a decision already recorded (DEC-006, DEC-015, DEC-019, DEC-024, DEC-030, DEC-033, DEC-035, OC-1 item 4). Where the audit found something that would change a requirement or needs the owner (CF-20, CF-21, DUP-40, OQ-28), it is recorded, not resolved.
- **One source of truth.** New rows and notes point to the owning requirements; nothing restates a requirement.
- **No history rewritten.** Older records keep their text; status lines and "Later changes" notes were added.
- **Project memory.** The project state records the verdict, the four open owner decisions, and the next step.

### Gate 3 — independent review

**First review: FAIL.** An independent reviewer (a separate agent that did not write the change; read-only on the repository, experiments on a copy; repository status unchanged afterwards) re-ran every check, confirmed every count in this record, checked the 230 or so requirement IDs it cites, sampled about 30 documents, and found:

| # | Finding | Severity | Fix |
|---|---|---|---|
| B1 | Area 19 said every checkpoint had an independent Gate 3 review; only those since `a2c8e92` did | BLOCKING | Area 19 corrected |
| B2 | "Changes made during the audit" listed the decision log (unchanged) and left out the technology stack, hosting and migration, and the new Findings lines | BLOCKING | Table rewritten from `git diff` |
| B3 | A new source-of-truth row said "runtime policy is not configuration", contradicting MIG-010 (policies are portable configuration) | BLOCKING | Row reworded: policy content is never in the repository; MIG-010 counts policies as portable configuration, moving with the platform state (MIG-008) |
| N1 | Arbitrage Intelligence still claimed to own the arbitrage opportunity database (DUP-26) | Non-blocking | A-21, fixed |
| N2 | Its Part 1 gap note still listed kill-switch reset rules | Non-blocking | In A-11, fixed |
| N3 | The roadmap still read "arbitrage capital categories if confirmed (CAP-028)" | Non-blocking | A-22, fixed |
| N4 | The withdrawal note dropped SEC-006's "general" and kept a narrow reading of CAP-030; PLT-010 drops DEC-006's "for others" | Non-blocking | Note quotes SEC-006 and includes CAP-037; DEC-028's note marked; PLT-010's wording is CF-21, for the owner |
| N5 | CF-20 left out MIG-004 and GOV-023, and a third reading (the builder's machine) | Non-blocking | CF-20 completed; "possibly only an ambiguity" |
| N6 | OQ-28 was not cross-referenced from all affected specifications | Non-blocking | A-23, fixed |
| N7 | Wrong IDs: REC-026 for "restart is not resume", SYS-21 among the arbitrage systems, V-02 for the first canary value; A-13 mixed different stale notes; area 1 called the 2026-10-01 directive HISTORICAL | Non-blocking | Corrected |
| N8 | Two new source-of-truth rows repeated existing rows; SEC-002 and GOV-007 were missing | Non-blocking | Rows merged or removed; IDs added |
| N9 | TC-10's inventory still missed PRODUCTION, EMERGENCY, DEPRECATED, RETIRED | Non-blocking | Added |
| N10 | Checks 3 and 11 could not be repeated from this record | Non-blocking | Method, script (appendix A), and sampled sections given; the defined scan finds 15 pairs, all classified |
| N11 | A-16 left out the 30 partly builder-decided requirements | Non-blocking | Added |
| N12 | The record did not say how tests are covered in the continuation contract | Non-blocking | Area 16 says so |
| N13 | The feature-sequence note should say the owner's list is mapped, not adopted | Non-blocking (optional) | Said |
| N14 | The open-question register's status line read ambiguously; DUP-40 lacked its "RECOMMENDED" label | Non-blocking | Fixed |

The reviewer confirmed: no requirement or decision changed; the counts; the decision checks; the fidelity of the CF-20, DUP-40, and OQ-28 entries; the appendix's integrity; the project-state update.

**Re-run 1:** the reviewer agent stopped on a usage limit before reporting. It changed nothing (repository status unchanged); its partial work was not used.

**Re-run 2: PASS.** A fresh independent reviewer (same conditions: read-only on the repository, experiments on a copy, `git status --short` identical before and after) confirmed all 17 findings of the first review fixed, re-ran every check and count, checked about 120 cited IDs against their text, and read 16 specifications the change did not touch. It found no blocking issue and 14 non-blocking ones, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| R1 | TC-10's inventory still missed UNKNOWN (RGM-007, ARCH-042), UNCERTAIN (RGM-005, RSK-006, RSK-014), ROLLBACK (MIG-014, RSK-006); area 2 and A-07 wrongly said PRODUCTION and RETIRED were missing; the glossary's term list left out APPROVED and CANARY and its "also" had no antecedent; the project state's TC-10 row named the old set | Names added in the register, glossary, and project state (with AIV-013 and RGM-002, found while fixing); wording corrected; check 7 says the inventory stays a working list |
| R2 | The dependency map's D-31 row and the Performance Controller's inputs still named the arbitrage database as Arbitrage Intelligence's (DUP-26) | Pointers added; area 2 and A-21 widened |
| R3 | MON-009 restates TEC-012's operational-log retention (V-19), the same pattern as DUP-40; the scan cannot find it | DUP-40 widened; named in Monitoring and observability; A-03 widened |
| R4 | CF-09's status line named REC-007 without "since replaced"; OQ-07's pointer left out RSK-016, RSK-017, RSK-020 | Pointer added; OQ-07 widened in the register and System Health; A-13 widened |
| R5 | CF-20 put MIG-004 and GOV-023, which agree with the request, on the conflicting side and left out PLT-017 | Sources reframed in CF-20, area 3, and A-01 |
| R6 | CF-20 and CF-21 were not cross-referenced from all affected specifications (DEC-005) | With CF-20's sources narrowed (R5), Architecture governance is no longer affected; Findings sections added to Deployment and operational readiness (CF-20) and Security architecture (CF-21) |
| R7 | The roadmap's corrected CAP-028 entry put CAP-032 in Stage 3, while the roadmap places it in Stage 4 | Corrected; A-22 |
| R8 | The N10 fix text named appendix B for the script | Appendix A |
| R9 | Area 16 said the continuation contract covers remaining work and decisions; other project-state sections do | Reworded |
| R10 | "The operator is the owner" was stated as fact | Marked as a reading, with its sources (area 4) |
| R11 | Three matrix rows said "Consistent" while listing an open finding | "Consistent with one open point" (also Market Data and Monitoring, for DUP-40) |
| R12 | RSK-004 with RSK-049 was class A though a refinement; AUD-006 with MON-009 read as B | Reclassified D and B |
| R13 | Area 19 called `16d317c` the first commit; the first is `7172a5c` | "The builder's first commit" |
| R14 | Architecture governance said the owner "restated" OQ-27's second half | "Stated" |

**Builder's own pass after re-run 2** (separate from the reviewer): the sweep of mentions of replaced requirements outside requirement lines was run again over every active document, this time listing every line without a pointer and reading each one. Decision records and resolved conflict entries keep their historical text under status lines or "Later changes" notes; two active entries had no pointer: the system registry's SYS-29 status (HLT-007 to HLT-009) and its Canary owner (STR-011). Both now point to their replacements (DEC-019; A-13). Checks 1 to 15 were then re-run on the final tree.

## Failures and fixes

| # | Failure | Cause | Fix | Re-run |
|---|---|---|---|---|
| 1 | The builder added a "Later changes" note to the Part 2 verification record that already had one | Only the first lines of the banner had been read | Duplicate removed; the Part 1 record's added note trimmed to what its existing note did not cover | Check 1 PASS |
| 2 | Three false or contradicting statements (Gate 3 B1 to B3) | Claims written from memory of the process (B1, B2) or from a summary of a requirement rather than its text (B3) | Each checked against `git diff`, the records, and MIG-010, and corrected | Gate 3 re-run |
| 3 | Fourteen smaller gaps (Gate 3 N1 to N14), among them three stale statements the audit's own sweeps did not catch | The sweeps searched for stale words and later decisions' IDs, not for every statement each later decision made untrue | Fixed as listed; CF-21 raised; one more sweep, of every mention of a replaced requirement outside requirement lines, added "since replaced" pointers to six resolution notes (A-13) | Gate 3 re-run |
| 4 | Fourteen further non-blocking gaps (Gate 3 re-run 2, R1 to R14), among them more shared state names, two more stale ownership statements, and one more stale pointer | The inventory and sweeps were checked against the names and statements already known, not re-derived from every requirement; the replaced-ID sweep skipped lines that held any pointer word | Fixed as listed; the replaced-ID sweep re-run line by line, which found two more entries (system registry) | Checks 1 to 15 re-run on the final tree |

## Final status

**PASS.** All three gates passed on the final tree; checks 1 to 15 pass. The audit's verdict is **B — READY WITH NON-BLOCKING FINDINGS** for Stage 1 planning. No requirement or decision was changed (check 4). Open for the owner: CF-20 and OQ-28 (decide), CF-21 and DUP-40 (decide or delegate), and acceptance of this review (A-19). TC-09 and TC-10 stay open until their stages are planned. Implementation is not authorized.

## Human review package

1. **Executive summary.** The knowledge base is coherent, traceable to specification level, and has one owner and one source of truth for every responsibility named in the request. The seven decisions of 2026-10-02 are applied consistently. The audit found no critical or high issue, two new conflicts (CF-20; CF-21, wording), one accidental duplicate (DUP-40), one scope question (OQ-28), and twelve documentation defects (A-07 to A-15, A-21 to A-23), all fixed.
2. **What was verified:** areas 1 to 22 above and checks 1 to 15.
3. **What was reconciled:** the documentation fixes in "Changes made during the audit".
4. **What was deduplicated:** nothing structural was needed; the duplicates found are recorded (DUP-40), were missing aliases and state names (A-07, A-08), or were a stale ownership statement (A-21).
5. **Conflicts resolved:** none was resolved by the builder; wording issues (withdrawal, failover, CAP-028) were brought in line with existing decisions, and CF-21 is left for the owner.
6. **Unresolved:** CF-20, CF-21, OQ-28, DUP-40 (owner); TC-09, TC-10 (by design, at their stages).
7. **Missing requirements:** none of the areas the request lists lacks a home. Missing detail is A-05 (interfaces, schemas, tests, failure procedures), by design produced at stage planning.
8. **Architecture issues:** CF-20 (hosting).
9. **Security issues:** none found.
10. **Capital, risk, execution issues:** none found; execution detail for multi-leg failure is open (A-05).
11. **AI governance issues:** none found.
12. **Repository issues:** none found.
13. **Documentation issues:** A-07 to A-15 and A-21 to A-23, all fixed; CF-21 (PLT-010's wording) for the owner.
14. **Traceability gaps:** the chain beyond specifications starts at Stage 1 (A-18).
15. **Roadmap issues:** Stage 1's plan with its Rule 140 fields is not written yet (A-04).
16. **Session continuity:** in place; the continuation contract gained a documentation-state row; tests are covered by its verification rows.
17. **Feature extensibility:** in place (GOV-001 to GOV-024).
18. **Exact changes:** "Changes made during the audit".
19. **Evidence:** each area and finding names its requirements; checks 1 to 15 are repeatable commands.
20. **Verdict:** B — READY WITH NON-BLOCKING FINDINGS.
21. **Next action from the owner:** accept this review (or ask for changes); decide CF-20 and OQ-28, and decide or delegate CF-21 and DUP-40 (none blocks Stage 1 planning); optionally confirm that GOV-002 with GOV-022 is the feature process meant; then authorize Stage 1 **planning**. Implementation still needs a separate, explicit "Begin Stage 1" after the plan is approved.

## Appendix A — check 3's duplicate scan

Run from the repository root with `python3`; it prints each similar pair and the total.

```python
# Near-duplicate scan used by the master knowledge-base audit, check 3.
import re, glob
req = {}
for f in glob.glob('docs/**/*.md', recursive=True):
    if f.startswith(('docs/handoffs', 'docs/builder', 'docs/traceability')) or f.endswith(('registry.md', 'requirements/README.md')):
        continue
    for l in open(f, encoding='utf-8'):
        m = re.match(r"- \*\*([A-Z]+-\d{3})\*\* (.+?) · ([A-Z /]+?) · \S.*? — (.*)", l)
        if m:
            req[m.group(1)] = set(re.findall(r"[a-z]{4,}", (m.group(2) + ' ' + m.group(4)).lower()))
ids = sorted(req)
n = 0
for i, a in enumerate(ids):
    for b in ids[i + 1:]:
        x, y = req[a], req[b]
        if min(len(x), len(y)) < 6:
            continue
        j = len(x & y) / len(x | y)
        c = len(x & y) / min(len(x), len(y))
        if j >= 0.42 or c >= 0.8:
            n += 1
            print(f"{a} {b} jaccard={j:.2f} containment={c:.2f}")
print(len(ids), 'requirements;', n, 'pairs')
```

## Appendix B — the request as received

The owner's message of 2026-10-02, reproduced exactly (extracted by script from the session; nothing added, removed, or changed):

```text
MASTER KNOWLEDGE-BASE INTEGRITY AUDIT — PRE-IMPLEMENTATION GATE

Before beginning any implementation work, perform a rigorous, repository-wide audit of EVERYTHING that has been provided, decided, reconciled, and established for this project so far.

This is not a request for a casual summary or a simple confirmation.

I need you to independently verify that the project knowledge is internally coherent, complete, traceable, correctly classified, correctly placed, and ready to serve as the authoritative foundation for a long-lived, company-grade production platform.

IMPORTANT:

Do NOT tell me that everything is correct merely because the documents exist.

Do NOT assume that because a requirement appears somewhere it has been correctly incorporated.

Do NOT silently invent missing requirements, reconstruct undocumented history, or silently change an architectural decision.

Where something is uncertain, conflicting, duplicated, missing, ambiguous, obsolete, superseded, or incorrectly classified, identify it explicitly.

Where the repository already contains the answer, use the repository as the source of truth.

Where a decision was explicitly made during the reconciliation process, verify that the resulting documentation reflects that decision.

==================================================
1. AUDIT THE COMPLETE KNOWLEDGE BASE
==================================================

Audit all available project knowledge, including:

- Parts 1–3
- all subsequent decisions and answers
- reconciliation decisions
- builder/constitution material
- architecture material
- requirements
- constraints
- principles
- policies
- decisions
- proposals
- future ideas
- open questions
- deprecated/replaced material
- roadmap
- repository documentation
- ADRs
- requirements registry
- traceability material
- system specifications
- AI specifications
- strategy specifications
- risk specifications
- capital specifications
- execution specifications
- arbitrage specifications
- operational/recovery specifications
- security specifications
- testing specifications
- deployment specifications
- platform lifecycle/maintenance/upgrade rules

Treat the complete result as ONE canonical knowledge system, not a collection of unrelated documents.

==================================================
2. DUPLICATE DETECTION
==================================================

Search systematically for duplicate or overlapping:

- requirements
- systems
- modules
- services
- components
- agents
- authorities
- state machines
- policies
- rules
- capabilities
- workflows
- data stores
- decision records
- documentation
- terminology
- lifecycle definitions
- governance mechanisms

For every suspected duplicate, determine whether it is:

A. genuinely separate,
B. the same capability described in multiple places,
C. a parent/child relationship,
D. an intentional specialization,
E. a historical/replaced definition,
F. an accidental duplicate.

Do not create a second system merely because the same responsibility was described under a different name.

Every responsibility must have a clear canonical owner.

==================================================
3. CONFLICT DETECTION
==================================================

Search for contradictions between:

- Part 1
- Part 2
- Part 3
- reconciliation decisions
- constitution rules
- ADRs
- requirements
- architecture
- implementation
- roadmap
- configuration
- repository documentation

Pay particular attention to conflicts involving:

- authority
- security
- user policy
- risk
- capital
- execution
- strategy
- AI
- safety
- readiness
- recovery
- rebalancing
- lifecycle
- deployment
- production
- paper trading
- canary
- future feature development

Do not silently resolve conflicts.

For every material conflict, record:

- conflicting statements
- source of each statement
- current canonical decision, if one exists
- why that decision is authoritative
- what must be updated elsewhere
- whether human approval is still required

==================================================
4. VERIFY THE RECONCILIATION DECISIONS
==================================================

Verify that the decisions just made during the reconciliation process are actually reflected consistently throughout the knowledge base.

At minimum verify the following decisions:

CF-17:
Non-bypassable security controls take precedence over user-configurable policy where applicable.

CF-18:
Capital growth automatically triggers capability reassessment and may automatically scale only within already-authorized policy boundaries and after readiness validation. Growth itself cannot create new authority. Increasing an authorization boundary requires owner approval.

CF-19:
The Constitution's canonical feature lifecycle is authoritative, with Part 3 terminology mapped into it rather than maintaining competing lifecycle systems.

TC-08:
Historical decision records may be backfilled now only where the repository provides evidence of alternatives actually considered. Do not invent historical alternatives.

DUP-34:
The Rebalancing Engine is a component of the canonical Global Capital Authority, not a second independent capital authority or competing capital-state owner.

DUP-35:
The adopted canonical safety-level system remains authoritative, with older Part 3 terminology mapped into it rather than creating a competing safety hierarchy.

OQ-27:
Parts 1–3 constitute the initial formal handoff/knowledge base. Later decisions and builder material are incorporated into the same canonical knowledge base. This does NOT prevent future features, upgrades, or requirements from being added later.

Verify that these decisions are reflected consistently and that no older document still silently asserts the opposite.

==================================================
5. REQUIREMENTS COMPLETENESS AUDIT
==================================================

Determine whether every substantive requirement we have established has a canonical location.

Check at minimum:

- deterministic trading infrastructure
- AI intelligence layer
- directional trading
- cross-exchange arbitrage
- triangular arbitrage
- future strategy extensibility
- market data
- exchange adapters
- quant engine
- regime engine
- opportunity engine
- global opportunity competition
- global capital authority
- dynamic capital allocation
- intelligent rebalancing
- portfolio
- risk
- execution
- reconciliation
- P&L/accounting
- strategy lifecycle
- backtesting
- anti-overfitting
- paper trading
- canary
- live trading
- AI agents
- model routing
- AI cost management
- hallucination controls
- AI permissions
- memory systems
- governance/consistency
- readiness
- safety states
- recovery
- disaster recovery
- failure handling
- security
- credentials
- least privilege
- monitoring
- observability
- auditability
- performance
- low-latency architecture
- testing
- deployment
- rollback
- migrations
- maintenance
- upgrades
- extensibility
- documentation
- roadmap
- traceability
- session continuity
- repository continuity
- future Claude Code maintenance

If a requirement has no canonical location, report it.

==================================================
6. REQUIREMENT CLASSIFICATION
==================================================

Verify that project knowledge is correctly classified as:

- CONFIRMED REQUIREMENT
- PRINCIPLE
- HARD CONSTRAINT
- SYSTEM RULE
- USER POLICY
- ARCHITECTURAL DECISION
- IMPLEMENTATION DECISION
- PROPOSAL
- RECOMMENDATION
- FUTURE CAPABILITY
- OPEN QUESTION
- REQUIRES HUMAN CONFIRMATION
- DEPRECATED
- SUPERSEDED
- HISTORICAL INFORMATION

Do not treat proposals as requirements.

Do not treat recommendations as approved architecture.

Do not treat historical information as current requirements.

Do not treat future capabilities as implemented capabilities.

==================================================
7. AUTHORITY AND OWNERSHIP AUDIT
==================================================

For every major responsibility, identify exactly ONE canonical authority.

Verify especially:

- System Safety
- Security
- User Policy
- Risk Authority
- Capital Authority
- Rebalancing
- Execution
- Strategy
- Portfolio
- Reconciliation
- Readiness
- Recovery
- AI
- Governance/Consistency

There must be no ambiguous competing authorities.

Verify that specialized components may make analyses/recommendations without accidentally becoming unauthorized authorities.

Example:

The Rebalancing Engine may determine whether rebalancing is economically justified, but the Global Capital Authority remains the canonical owner of capital state and capital movement authorization.

==================================================
8. SOURCE-OF-TRUTH AUDIT
==================================================

Identify the canonical source of truth for:

- requirements
- architecture
- system ownership
- system rules
- decisions
- roadmap
- strategy definitions
- risk limits
- capital state
- configuration
- deployment state
- production version
- database schema
- operational state
- audit history
- AI configuration
- model routing
- feature lifecycle
- platform lifecycle

If multiple sources claim authority over the same information, flag it.

No important information should have two competing canonical sources.

==================================================
9. TRACEABILITY AUDIT
==================================================

Verify traceability:

Requirement
→ architectural decision
→ system/component
→ implementation location
→ configuration where applicable
→ tests
→ verification
→ deployment/release
→ operational monitoring

Identify requirements that cannot currently be traced.

Identify implementation that cannot be traced back to an approved requirement or decision.

Identify documentation claims that cannot be supported by repository evidence.

==================================================
10. ARCHITECTURE BOUNDARY AUDIT
==================================================

Verify that responsibilities are properly separated.

In particular:

DETERMINISTIC SYSTEMS
must remain authoritative for:

- market data integrity
- calculations
- capital
- risk
- order validation
- execution
- reconciliation
- safety
- financial accounting

AI may provide:

- analysis
- research
- interpretation
- hypothesis generation
- strategy research
- controlled improvement proposals

AI must not become an uncontrolled authority over:

- capital
- risk limits
- security
- execution safety
- credentials
- reconciliation
- system safety

Verify that AI cannot bypass deterministic controls.

==================================================
11. CAPITAL AUTHORITY AUDIT
==================================================

Verify:

- one global capital authority
- one authoritative capital state
- dynamic capital allocation
- reservation/release
- deployed capital
- pending operations
- exchange balances
- strategy requests
- rebalancing
- reserves
- custody exposure
- capital productivity
- opportunity competition

Ensure no strategy, arbitrage module, or rebalancing module creates a competing capital authority.

==================================================
12. SECURITY AUDIT
==================================================

Verify that:

- non-bypassable security controls cannot be overridden by ordinary user policy
- least privilege is enforced
- AI permissions are bounded
- AI cannot access raw secrets unnecessarily
- withdrawal permissions are appropriately restricted
- credentials are isolated
- environments are separated
- research/paper systems cannot obtain production authority
- security controls cannot be bypassed through strategy, AI, capital, or execution logic

==================================================
13. SAFETY / RISK / RECOVERY AUDIT
==================================================

Verify separation between:

- safety state
- risk state
- system health
- readiness state
- recovery state

Verify there is only one canonical safety hierarchy.

Verify that:

- failures do not automatically cause unsafe resumption
- external exchange state is authoritative
- unknown order states are reconciled
- recovery verifies balances/orders/positions/fills
- capital and risk are revalidated before resume
- active trades are not casually interrupted
- emergency controls cannot be bypassed
- recovery cannot create unauthorized capital authority

==================================================
14. PERFORMANCE ARCHITECTURE AUDIT
==================================================

Verify that performance is a first-class architectural requirement.

Check for:

- hot path / cold path separation
- event-driven processing
- persistent WebSockets
- incremental calculations
- caching
- efficient data structures
- asynchronous processing where safe
- backpressure
- connection reuse
- latency measurement
- P50/P95/P99 where appropriate
- opportunity detection latency
- execution latency
- end-to-end latency
- throughput
- resource isolation

Also verify that performance optimization cannot bypass:

- risk
- validation
- capital reservation
- reconciliation
- auditability
- security

==================================================
15. FEATURE EXTENSIBILITY AUDIT
==================================================

Verify that the platform can accept future features without requiring a foundation rebuild.

Every new feature should pass:

UNDERSTAND
→ INSPECT
→ CLASSIFY
→ DUPLICATE CHECK
→ CONFLICT CHECK
→ DEPENDENCY CHECK
→ SECURITY CHECK
→ RISK CHECK
→ PERFORMANCE CHECK
→ DATA/API CHECK
→ DESIGN
→ APPROVAL
→ IMPLEMENT
→ VERIFY
→ PAPER/SAFE TEST
→ CANARY
→ PRODUCTION
→ MONITOR
→ DOCUMENT

Verify that this process is documented as the canonical future-feature process.

==================================================
16. PERSISTENT PLATFORM / CLAUDE CODE SEPARATION
==================================================

Verify that the repository explicitly establishes:

CLAUDE CODE = builder / maintainer / upgrader / tester / integrator

PRODUCTION PLATFORM = independent persistent financial technology platform

The production platform must NOT depend on:

- an active Claude session
- Claude conversation memory
- Claude availability
- the user's laptop
- the original builder being online

Verify that future Claude sessions can recover the project's state from the repository.

Verify session continuity documentation covers:

- current stage
- completed work
- work in progress
- remaining work
- blockers
- decisions
- tests
- verification
- repository state
- documentation state
- next action

==================================================
17. FUTURE MAINTENANCE AND UPGRADE AUDIT
==================================================

Verify that the platform explicitly supports:

- bug fixes
- new features
- new strategies
- new exchanges
- new data sources
- new AI capabilities
- security updates
- performance improvements
- infrastructure changes
- schema migrations
- API evolution
- monitoring improvements
- recovery improvements
- architecture evolution
- technical-debt reduction

Verify that future upgrades are controlled changes to the existing platform, not automatic rebuilds.

==================================================
18. ROADMAP AUDIT
==================================================

Verify that there is ONE canonical roadmap.

Check:

- dependencies
- sequencing
- prerequisites
- non-scope
- stage boundaries
- verification gates
- readiness gates
- production gates

Ensure Claude does not implement future stages prematurely.

Verify that every major stage has explicit completion criteria.

==================================================
19. THREE-PASS VERIFICATION AUDIT
==================================================

Verify that every major implementation stage uses three distinct verification passes:

PASS 1 — CODE VERIFICATION
Correctness, quality, tests, edge cases, failure paths.

PASS 2 — REPOSITORY / ARCHITECTURE VERIFICATION
Ownership, integration, boundaries, dependencies, documentation, duplication, consistency.

PASS 3 — FULL SYSTEM VERIFICATION
Regression, integration, security, performance, reliability, recovery, documentation, requirements traceability.

A stage must not be considered complete merely because code compiles or tests pass.

==================================================
20. REPOSITORY STRUCTURE AUDIT
==================================================

Inspect the actual repository.

Do not assume the proposed directory structure exists.

Compare the current repository against the canonical intended organization.

Identify:

- misplaced files
- duplicate documents
- obsolete documents
- conflicting documents
- undocumented systems
- undocumented modules
- orphaned requirements
- orphaned implementation
- stale references
- missing indexes
- missing cross-references

Preserve valid existing work.

Do not reorganize files merely for cosmetic reasons.

==================================================
21. DOCUMENTATION QUALITY AUDIT
==================================================

Verify that documentation is:

- internally consistent
- discoverable
- cross-linked
- versioned where appropriate
- authoritative
- non-duplicative
- explicit about status
- explicit about ownership
- explicit about dependencies
- explicit about unresolved questions

Historical decisions must not be rewritten as if they were always known.

Never fabricate missing history.

==================================================
22. IMPLEMENTATION VS SPECIFICATION AUDIT
==================================================

Determine whether the repository contains implementation already.

For every significant implementation:

- identify its corresponding requirement
- identify its architectural owner
- identify its status
- identify its tests
- identify its documentation
- identify whether it is actually complete

Do not call something implemented merely because files exist.

Do not call something production-ready without evidence.

Do not claim verification without actual verification evidence.

==================================================
23. MISSING / WEAK / AMBIGUOUS AREAS
==================================================

Create a dedicated findings section containing:

CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL

For every finding include:

- ID
- category
- exact issue
- affected source/document/system
- why it matters
- evidence
- recommended resolution
- whether human approval is required
- whether implementation is blocked

==================================================
24. FINAL CONSISTENCY MATRIX
==================================================

Produce a final matrix containing at minimum:

AREA | STATUS | CANONICAL SOURCE | OWNER | CONFLICTS | DUPLICATES | MISSING ITEMS | ACTION

Areas must include:

- Requirements
- Architecture
- Governance
- Security
- Risk
- Capital
- Rebalancing
- Execution
- Strategies
- Arbitrage
- Market Data
- Quant
- Regime
- AI
- Backtesting
- Paper
- Canary
- Production
- Recovery
- Monitoring
- Performance
- Testing
- Deployment
- Maintenance
- Upgrade
- Feature Lifecycle
- Roadmap
- Traceability
- Documentation
- Session Continuity

==================================================
25. DO NOT HIDE UNCERTAINTY
==================================================

If you cannot verify something, say:

UNVERIFIED

Do not say:

- confirmed
- complete
- production-ready
- consistent
- conflict-free

unless you have evidence.

If something requires my decision, clearly state:

HUMAN DECISION REQUIRED

and explain exactly what decision is needed and why.

==================================================
26. DO NOT IMPLEMENT DURING THIS AUDIT
==================================================

This audit is a pre-implementation governance and knowledge-integrity gate.

Do not begin building major production functionality while this audit is unresolved.

You may make documentation corrections that are explicitly required to reconcile the already-approved decisions, but do not silently change architecture or requirements.

If a change would alter an approved requirement or architectural decision, stop and flag it for human approval.

==================================================
27. FINAL VERDICT
==================================================

At the end, provide exactly one of:

A. READY FOR STAGE 1 PLANNING
   if the knowledge base and repository are sufficiently coherent and all material blockers are resolved.

B. READY WITH NON-BLOCKING FINDINGS
   if only minor issues remain and they do not compromise Stage 1 planning.

C. NOT READY
   if material conflicts, missing requirements, ownership ambiguity, architectural contradictions, security issues, or traceability failures remain.

Do not choose A merely because the documents look organized.

The verdict must be evidence-based.

==================================================
28. FINAL HUMAN REVIEW PACKAGE
==================================================

Before asking me to authorize Stage 1, provide:

1. Executive audit summary
2. What was verified
3. What was reconciled
4. What was deduplicated
5. What conflicts were resolved
6. What remains unresolved
7. Missing requirements
8. Architecture issues
9. Security issues
10. Capital/risk/execution issues
11. AI governance issues
12. Repository issues
13. Documentation issues
14. Traceability gaps
15. Roadmap issues
16. Session-continuity status
17. Future-feature extensibility status
18. Exact changes made during the audit
19. Evidence for each material conclusion
20. Final readiness verdict
21. Exact next action required from me

Do not start Stage 1 implementation until I explicitly authorize it.

The objective is not to make the project appear complete.

The objective is to establish a genuinely coherent, auditable, traceable, maintainable, extensible, secure, company-grade foundation that future engineers and future Claude Code sessions can continue from without reconstructing the project from memory.

END MASTER KNOWLEDGE-BASE INTEGRITY AUDIT
```
