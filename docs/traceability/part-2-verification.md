# Part 2 Verification Record and Documentation Audit

> **Result: VERIFIED for the Part 2 documentation round (2026-09-30), with findings open for the owner.** Handoff Part 2 is preserved, reconciled with Part 1 and every earlier decision, and placed by ownership. Three verification passes were run on the actual files; the defects they found were fixed and re-checked. **Not verified:** any product behavior. Nothing is implemented, and implementation is not authorized (P2§330).
>
> Decisions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md), [DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md). Section-by-section trace: [Part 2 reconciliation](part-2-reconciliation.md).
>
> **Later changes:** this record is kept as written. The findings it lists as open, and the items it lists as awaiting confirmation, were answered by the owner the same day. See [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), DEC-026 to DEC-030, and the [verification of those decisions](owner-decisions-03-verification.md). The current mapping of every Part 2 section is the [Part 2 reconciliation](part-2-reconciliation.md).

## Summary

| Measure | Before Part 2 | After |
|---|---|---|
| Requirements | 394 | 588: 185 new from Part 2 sections, 9 new from DEC-024 |
| Existing requirements whose text, class, or location changed | — | **0** (script comparison against the previous commit) |
| Systems | 33 | 34 (SYS-34 Readiness System, formerly a component of SYS-14) |
| Requirement sets | 7 | 9 (MIG hosting, backup, and migration; VER verification) |
| Decision records | 23 | 25 |
| Findings | CF 13, DUP 22, OQ 23, TC 6, all resolved | CF 16 (CF-14 **open**), DUP 31, OQ 26 (OQ-24 to OQ-26 **open**), TC 7 (TC-07 **open**) |
| Values register | 29 entries | 33 entries |
| Part 2 sections accounted for | — | 350 of 350, plus the opening instruction and the final non-negotiables |

New requirements by class: SYSTEM REQUIREMENT 59; CONFIRMED REQUIREMENT 51; CONSTRAINT 46; CONFIRMED ARCHITECTURAL PRINCIPLE 33; PROPOSED 2 (OPS-009, ARCH-034); FUTURE 2 (REC-021, LED-008); PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION 1 (CAP-028).

## P2§331 required workflow

| Step (P2§331) | Done | Evidence |
|---|---|---|
| Read Part 1 | Yes | Re-read through its canonical specifications and the registry before reconciling |
| Read the complete Part 2 | Yes | All 350 sections, the opening instruction, and the final non-negotiables |
| Inspect the repository | Yes | Project state, registry, every specification touched, registers, maps |
| Identify existing documentation | Yes | Each Part 2 section mapped to existing requirements where they already cover it ([reconciliation](part-2-reconciliation.md), last column) |
| Identify duplicates | Yes | DUP-23 to DUP-31, including Part 2 restating itself (DUP-31) |
| Identify conflicting requirements | Yes | CF-14 (open), CF-15, CF-16; every earlier decision re-checked ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md), decision 5) |
| Identify missing systems | Yes | One: the Readiness System, registered as SYS-34. Every other name Part 2 uses was mapped to an existing owner ([system registry](../architecture/system-registry.md), last table) |
| Establish authoritative ownership | Yes | ARCH-027; [source-of-truth map](../architecture/source-of-truth-map.md), "Canonical authorities" |
| Create/update the requirements registry | Yes | [Registry](../requirements/registry.md): 588 entries, with an Approval column (ARCH-030) |
| Create/update the traceability matrix | Yes | [Part 2 reconciliation](part-2-reconciliation.md); [Part 1 coverage](handoff-coverage.md) |
| Create/update the dependency graph | Yes | [Dependency map](../architecture/dependency-map.md), D-54 to D-63 and the stage diagram |
| Create/update architecture documentation | Yes | [Architecture overview](../architecture/overview.md), ARCH-019 to ARCH-034 |
| Create/update the master roadmap | Yes | [Roadmap](../roadmap/roadmap.md), RMP-003 to RMP-011 and the Part 2 additions by stage |
| Create/update the Paper Trading architecture | Yes | [Paper trading](../systems/strategy/paper-trading.md), PAP-004 to PAP-012 |
| Create/update the Readiness System architecture | Yes | [Readiness System](../systems/readiness-system.md), RDY-001 to RDY-007 |
| Create/update the Daily System Intelligence Dashboard/Report specification | Yes | [Daily System Intelligence](../operations/daily-system-intelligence.md), DSI-001 to DSI-006 |
| Create/update the arbitrage architecture | Yes | [Arbitrage intelligence](../systems/arbitrage/arbitrage-intelligence.md), "Arbitrage architecture after Part 2"; XAR-005, TAR-003, TAR-004, ARB-015 |
| Create/update the deployment/migration architecture | Yes | [Hosting, backup, and migration](../operations/hosting-and-migration.md), MIG-001 to MIG-028; OPS-007 to OPS-013; REC-019 to REC-022 |
| Record open questions | Yes | OQ-24 to OQ-26, TC-07 ([open-question register](../open-questions/register.md)); CF-14 ([findings register](../conflicts/register.md)) |
| Produce a documentation audit | Yes | This record, "Documentation audit" below |
| Stop for human review/approval | Yes | [Project state](../project-state.md): implementation not authorized; owner decisions requested |

## Verification pass 1 — content: was it built correctly?

| Check | Method | Result |
|---|---|---|
| The historical copy of Part 2 is word-for-word | Converter round trip: Markdown stripped back to the received text | PASS: 2,774 content lines identical; sections 1 to 350 in order. Only the banner and the formatting were added |
| No existing requirement changed | Every requirement line compared with the previous commit | PASS: 0 changed, 0 moved, 0 removed; 194 added |
| New requirement wording follows the source | For each Part 2-sourced requirement, content words compared with the cited sections; lowest overlaps reviewed by hand | PASS after fixes. Low overlap came from connecting words ("in addition to X-NNN") and from the reconstructed table (ARCH-022). **Fixed:** PAP-012 had turned the final non-negotiable's "should" into a statement of fact; now "should", with the source named. DSI-005 had added "may"; now it follows the table's wording |
| Modal verbs kept (constitution Rule 56) | Each "must", "should", "may", "never", or "cannot" in a new requirement searched for in its cited sections | PASS after the DSI-005 fix |
| Conditional wording kept conditional (P2§181, ARCH-029) | Sources with "where approved", "if approved", "requires approval", or "remains a proposal" checked against the class given | PASS. OPS-009, ARCH-034: PROPOSED. REC-021, LED-008: FUTURE. CAP-028: REQUIRES CONFIRMATION. CUS-004 and CUS-005 are CONSTRAINTS that apply only "if custody is ever approved", like LED-001. PLT-017 and RMP-008 keep "failover where approved" as written |
| No duplicated requirement text | Pairwise word similarity across all 588 requirements | PASS after a fix. One near-pair: AGT-001 (replaced list of agents) and AGT-017 (roles kept). A note now says AGT-017 does not revive AGT-001 |
| Values classified (ARCH-018) | Every concrete value in a new requirement checked | PASS: V-30 to V-33 added. "1% per trade" and similar examples are marked non-operating |
| Every reconstructed table cell is a word from the source | ARCH-022's rows compared with §339 as received | PASS: boundaries restored only; the reading is disclosed in ARCH-022 and in the historical banner |

## Verification pass 2 — placement: is it in the right place?

| Check | Method | Result |
|---|---|---|
| Each requirement is in its owner's specification | Generator: prefix → owner; one ID per specification line | PASS |
| One owner per authority | ARCH-027 list compared with the system registry and the source-of-truth map | PASS: 12 of 12 have one owner |
| No new system without justification (constitution Rule 84) | Every Part 2 component name reviewed | PASS: one registration (SYS-34) with reasons in DEC-024; 22 other names mapped to existing owners |
| Duplicate authorities resolved | DUP-23 to DUP-31 | PASS: each resolved in DEC-024 and reflected in its specification |
| Terminology | Glossary checked for every Part 2 alias | PASS: 15 terms added and 2 updated (Readiness System, Opportunity Database); one term left open (global platform controller, OQ-24) |
| Registers, maps, roadmap, and index updated together | System registry, dependency map, source-of-truth map, glossary, roadmap, values register, decision log, documentation index | PASS |
| Stale statements | Searched for "not received", "expected from Part 2", "all resolved", and the old engine placement | PASS after fixes. "Part 2 not received" / "expected from Part 2" was corrected in 6 places, and "all resolved" in 4 specifications that now carry an open finding |
| Headers | Specifications that gained Part 2 requirements say "Handoff Parts 1 and 2" | PASS: 30 headers updated. The custody-and-ledger specification and the roadmap use a different header, which now names their Part 2 content |

## Verification pass 3 — whole system: does it fit with everything else?

| Check | Method | Result |
|---|---|---|
| All references and links resolve | `tools/docs/build_index.py --check-only` (every requirement, finding, decision, and system ID; every relative link) | PASS: no errors |
| Every Part 1 and Part 2 section is accounted for | Generator coverage checks | PASS: Part 1 104 of 104; Part 2 350 of 350 (279 with new requirements, the rest covered, restated, or process) |
| Build order respects dependencies (RMP-011) | Each new dependency (D-54 to D-63) compared with the stages | PASS after CF-16: the Readiness System and paper evidence (DIRECTIONAL) had needed the Performance Controller (ARBITRAGE); its core now moves to DIRECTIONAL. Everything else depends on the same or an earlier stage |
| Earlier decisions still hold | DEC-006 to DEC-023 re-checked (DEC-024, decision 5) | PASS except RSK-004 vs P2§101 → CF-14, left open; RSK-004 stays in force |
| Active requirements that cite a replaced requirement have a note | Script over all active requirements | PASS after fixes. CAP-021 (cites PERF-007) and RSK-010 (cites SEC-003) had no note; the gap predates Part 2. Notes added |
| No secrets committed (constitution Rules 110, 153) | Pattern search for keys, tokens, passwords, private keys | PASS: none |
| No product implementation | Repository inspected | PASS: only documentation and the documentation tooling (`tools/docs/`, DEC-025). No platform code, configuration, or infrastructure |
| Counts agree across documents | Registry, DEC-024, project state, this record | PASS |

## Documentation audit (P2§331)

### Where each area lives (P2§178)

| Area (P2§178) | Canonical document |
|---|---|
| Requirements | [requirements/](../requirements/README.md), [registry](../requirements/registry.md) |
| Architecture | [architecture/overview.md](../architecture/overview.md) |
| Market Data | [systems/market-data.md](../systems/market-data.md) |
| Quant | [systems/quantitative-engine.md](../systems/quantitative-engine.md) |
| Regime | [systems/market-regime-engine.md](../systems/market-regime-engine.md) |
| Opportunities | [systems/opportunity-detection.md](../systems/opportunity-detection.md) |
| Risk | [risk/risk-engine.md](../risk/risk-engine.md) |
| Capital | [systems/capital-management.md](../systems/capital-management.md) |
| Portfolio | [systems/portfolio-management.md](../systems/portfolio-management.md) |
| Execution | [systems/execution-engine.md](../systems/execution-engine.md) |
| Arbitrage | [systems/arbitrage/](../systems/arbitrage/arbitrage-intelligence.md) |
| AI | [ai/](../ai/ai-architecture.md) |
| Policy | [systems/policy/](../systems/policy/policy-system.md) |
| Strategies | [systems/strategy/strategy-management.md](../systems/strategy/strategy-management.md) |
| Security | [security/security-architecture.md](../security/security-architecture.md) |
| Paper Trading | [systems/strategy/paper-trading.md](../systems/strategy/paper-trading.md) |
| Readiness | [systems/readiness-system.md](../systems/readiness-system.md) |
| Monitoring | [operations/monitoring-and-observability.md](../operations/monitoring-and-observability.md), [daily-system-intelligence.md](../operations/daily-system-intelligence.md) |
| Performance | [architecture/performance-and-latency.md](../architecture/performance-and-latency.md) |
| Testing | [architecture/verification-architecture.md](../architecture/verification-architecture.md) |
| Deployment | [operations/deployment-and-operational-readiness.md](../operations/deployment-and-operational-readiness.md) |
| Migration | [operations/hosting-and-migration.md](../operations/hosting-and-migration.md) |
| Recovery | [systems/recovery-and-reconciliation.md](../systems/recovery-and-reconciliation.md) |
| Roadmap | [roadmap/roadmap.md](../roadmap/roadmap.md) |

### Documents created and changed

- **Created:**
  - the [historical Part 2 copy](../handoffs/part-2-consolidated-additional-systems.md);
  - [Readiness System](../systems/readiness-system.md), [Daily System Intelligence](../operations/daily-system-intelligence.md), [Incident Management](../operations/incident-management.md), [Hosting, Backup, and Migration](../operations/hosting-and-migration.md), [Verification Architecture](../architecture/verification-architecture.md);
  - [Part 2 reconciliation](part-2-reconciliation.md) and this record;
  - [DEC-024](../decisions/DEC-024-part-2-reconciliation.md), [DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md);
  - `tools/docs/build_index.py` and its README.
- **Changed:** 31 existing specifications and the roadmap (new requirement sections), the registers, the system registry, the dependency and source-of-truth maps, the glossary, the values register, the roadmap, the decision log, the documentation index, and the project state. The generated registry and coverage files were rebuilt.

### Duplicates, conflicts, and gaps found

- **Duplicates:** DUP-23 to DUP-31, all resolved (DEC-024).
- **Conflicts:** CF-14 is **open**; CF-15 and CF-16 are resolved.
- **Missing information (not invented, constitution Rule 32):** OQ-24 (global platform controller), OQ-25 (where PAPER-mode strategies run), OQ-26 (adaptive execution), TC-07 (split-brain across hosts).
- **Awaiting the owner's confirmation:** CAP-028 (extra capital categories), OPS-009 (infrastructure as code), ARCH-034 (domain command language), REC-021 (high availability and failover).

### Specification gaps left for stage planning

Part 2 did not supply these. Each is filled when its stage is planned, before that stage's implementation is approved (constitution Rules 75 and 140):

- interface contracts (ARCH-025);
- per-stage entry and exit criteria, and verification methods per requirement (ARCH-030);
- per-requirement dependencies;
- the walk-forward and Monte Carlo methodologies (BKT-007, BKT-009);
- the universe-selection details (OPP-013);
- readiness evidence thresholds (V-33);
- the migration package format and the backup and recovery objectives (MIG);
- the incident severity scale and lifecycle (INC);
- failure behavior per system (HLT-006).

### Anti-drift audit (constitution Part L)

| Question | Answer |
|---|---|
| Added something never approved? | No. Items Part 2 marks as needing approval are PROPOSED, FUTURE, or REQUIRES CONFIRMATION. The one builder addition, `tools/docs/`, is recorded in DEC-025 |
| Removed something approved? | No: 0 existing requirements changed or removed |
| Changed the meaning of a requirement? | No. CF-14 is recorded, not resolved |
| Did architecture change without being recognized? | Two placement changes, both recognized in DEC-024: SYS-34, and the Performance Controller's stage |
| Did responsibility move between systems? | Yes, deliberately and recorded: the Governance and Readiness Engine moved to SYS-34; the arbitrage opportunity database became the arbitrage view of SYS-05's database |
| Terminology drift? | No. Every alias is in the glossary |
| Stale documentation or memory? | Found and fixed (pass 2); the project state is updated |
| New source of truth? | No. The dashboard, Readiness System, and Opportunity Database read their owners; the registry is generated |
| Future work implemented early? | No |
| Does the repository match what we think we built? | Checked by script and by re-reading the generated files |

## The P2§349 checklist

Every concept Part 2 asks to check, with where it now lives. This is a reconciliation checklist, not a list of approved production requirements (P2§349): the class of each referenced requirement is in the [registry](../requirements/registry.md).

| Category | Concept | Canonical requirements |
|---|---|---|
| Core Architecture | Deterministic trading infrastructure | PLT-016, ARCH-019 |
| Core Architecture | AI intelligence layer | ARCH-019, AIL-001, AIL-002 |
| Core Architecture | Natural-language policy | NLP-001, NLP-004 |
| Core Architecture | Autonomous operation | PLT-013, PLT-015, PLT-020 |
| Core Architecture | Controlled self-improvement | STR-009, STR-010 |
| Core Architecture | Global controller | OQ-24 (open) |
| Core Architecture | Policy compiler | NLP-004, POL-012 |
| Core Architecture | Safe states | PLT-018, RSK-015 |
| Core Architecture | No-trade | RSK-006, RSK-031 |
| Core Architecture | Wait | RSK-006, RSK-032 |
| Core Architecture | Safe Mode | RSK-015, RSK-030 |
| Market Infrastructure | Market-data ingestion | MKD-001, MKD-003 |
| Market Infrastructure | WebSocket infrastructure | EXA-012, EXA-015 |
| Market Infrastructure | Data normalization | MKD-011, EXA-013 |
| Market Infrastructure | Data validation | MKD-003, MKD-008 |
| Market Infrastructure | Data quality | MKD-004, MKD-008 |
| Market Infrastructure | Data quarantine | MKD-009 |
| Market Infrastructure | Data lineage | MKD-010 |
| Market Infrastructure | Time synchronization | HLT-013 |
| Market Infrastructure | Whole-market scanning | OPP-001, OPP-013 |
| Market Infrastructure | Quantitative engine | QNT-001 to QNT-007 |
| Market Infrastructure | Regime engine | RGM-001, RGM-005, RGM-007 |
| Market Infrastructure | UNKNOWN REGIME | RGM-002, RGM-008 |
| Market Infrastructure | Opportunity Filter | OPP-005, OPP-008 |
| Market Infrastructure | Opportunity Database | OPP-014 to OPP-016 |
| Market Infrastructure | True Net Profit | TNP-001, TNP-018 |
| Market Infrastructure | Fee Engine | QNT-005 |
| Market Infrastructure | Slippage Engine | QNT-006 |
| Market Infrastructure | Liquidity protection | TNP-024 |
| Market Infrastructure | Funding costs | TNP-018, RSK-013 |
| Risk / Capital / Portfolio | Capital Authority | CAP-001, CAP-017 |
| Risk / Capital / Portfolio | Risk Authority | RSK-001, RSK-012 |
| Risk / Capital / Portfolio | Portfolio Authority | PRT-001, PRT-003 |
| Risk / Capital / Portfolio | Atomic capital reservation | CAP-027 |
| Risk / Capital / Portfolio | Capital allocation | CAP-006, CAP-017 |
| Risk / Capital / Portfolio | Capital utilization | CAP-006, CAP-007, DSI-002 |
| Risk / Capital / Portfolio | Loss-streak protection | RSK-026 |
| Risk / Capital / Portfolio | Excessive-trading protection | RSK-027 |
| Risk / Capital / Portfolio | Exposure control | RSK-002 |
| Risk / Capital / Portfolio | Drawdown control | RSK-002, QNT-002 |
| Risk / Capital / Portfolio | Strategy drift | PFC-009 |
| Risk / Capital / Portfolio | Kill switches | RSK-008, RSK-028 |
| Risk / Capital / Portfolio | No-new-position mode | RSK-029 |
| Execution | Exchange adapters | EXA-001, EXA-003, EXA-011 |
| Execution | Binance | EXA-005 |
| Execution | OKX | EXA-005 |
| Execution | Coinbase | EXA-005 |
| Execution | Exchange normalization | EXA-013 |
| Execution | Order management | EXE-002 |
| Execution | Fill management | EXE-002 |
| Execution | Rate limits | EXA-014 |
| Execution | Connection management | EXA-015 |
| Execution | Partial fills | EXE-002, CAP-005 |
| Execution | Order timeout handling | EXE-005, EXE-006 |
| Execution | Reconciliation | REC-008, EXE-007 |
| Execution | Execution latency | PERF-008, PERF-009 |
| Execution | Adaptive execution where approved | OQ-26 (open; not defined in either handoff) |
| Arbitrage | Cross-exchange arbitrage | XAR-001 to XAR-005 |
| Arbitrage | Triangular arbitrage | TAR-001 to TAR-004 |
| Arbitrage | Pre-positioned capital | XAR-005 |
| Arbitrage | Inventory management | CAP-002, CAP-023, XAR-005, PFC-014 |
| Arbitrage | Intelligent rebalancing | ARB-005, ARB-006, CAP-023, CAP-024 |
| Arbitrage | Arbitrage capital reserves | ARB-008, ARB-009, CAP-028 (awaits confirmation) |
| Arbitrage | Arbitrage risk | RSK-012, RSK-033 |
| Arbitrage | Arbitrage kill switch | RSK-008, ARB-010 |
| Arbitrage | Arbitrage performance controller | PFC-014 |
| Arbitrage | Arbitrage opportunity tiers | ARB-015 |
| Arbitrage | Expected-vs-actual arbitrage analysis | PFC-015 |
| Arbitrage | Multi-leg execution risk | TAR-004, RSK-033 |
| Strategy | Strategy Factory | STR-003, STR-012 |
| Strategy | Strategy Registry | STR-023 |
| Strategy | Strategy versioning | STR-005, STR-025 |
| Strategy | Strategy lifecycle | STR-001, STR-024 |
| Strategy | Backtesting | BKT-001, BKT-004 |
| Strategy | Out-of-sample testing | STR-001, BKT-006 |
| Strategy | Walk-forward testing | BKT-007 |
| Strategy | Stress testing | BKT-008 |
| Strategy | Monte Carlo/distribution analysis | BKT-009 |
| Strategy | Anti-overfitting | BKT-006 |
| Strategy | Paper trading | PAP-001, PAP-004 |
| Strategy | Canary | STR-013 to STR-020, OPS-011, OPS-013 |
| Strategy | Production | STR-001, OPS-007 |
| Strategy | Rollback | OPS-012, STR-017 |
| Strategy | Strategy health | PFC-003, PFC-005 |
| Strategy | Strategy drift | PFC-009 |
| Strategy | Controlled optimization | AGT-012, STR-009 |
| AI | AI Resource Governor | AIL-008, AIL-009 |
| AI | Model Router | RTR-001 to RTR-005 |
| AI | AI caching | AIL-010 |
| AI | AI failover | AIL-011 |
| AI | AI degradation | AIL-012 |
| AI | AI cost/value optimization | COST-001, COST-002 |
| AI | Market Analyst | AGT-008 |
| AI | Quant Research | AGT-010, AGT-017 |
| AI | Strategy Research | AGT-012, AGT-017 |
| AI | Trading Director | AGT-004, AGT-019, AGT-020 |
| AI | Devil's Advocate | AGT-006, AGT-007 |
| AI | Performance Analyst | AGT-014, AGT-021 |
| AI | Strategy Optimizer | AGT-012, AGT-017 |
| AI | Model Evaluation | MEV-001, MEV-003, MEV-004 |
| AI | AI Cost Manager | COST-001, COST-002 |
| AI | Hallucination Firewall | AIV-001 to AIV-003, AIV-017 |
| AI | Evidence/timestamp requirements | AIV-001, AIV-018, AIV-019 |
| AI | Multi-agent validation | AIV-007, AIV-008 |
| AI | AI disagreement | AIV-014, AIV-020 |
| AI | Tool-first architecture | AIL-013 |
| AI | AI permission scopes | AGT-022, SEC-008 |
| Paper / Readiness | Continuous real-time paper operation | PAP-004, PAP-005 |
| Paper / Readiness | Simulated capital | PAP-007 (where it runs: OQ-25) |
| Paper / Readiness | Paper execution | PAP-008 |
| Paper / Readiness | Paper/live architectural parity | PAP-006 |
| Paper / Readiness | Evidence accumulation | PAP-009 |
| Paper / Readiness | Expected-vs-observed analysis | PFC-010 |
| Paper / Readiness | Missed-opportunity analysis | PFC-012 |
| Paper / Readiness | False-opportunity analysis | PFC-013 |
| Paper / Readiness | Strategy-health analysis | PFC-003, AGT-014 |
| Paper / Readiness | Paper readiness | RDY-001, PAP-012 |
| Paper / Readiness | Canonical Readiness System | RDY-001, RDY-006 |
| Paper / Readiness | Readiness states | RDY-004, RDY-007 |
| Paper / Readiness | Readiness evidence | RDY-002 |
| Paper / Readiness | Readiness blockers | RDY-005 |
| Paper / Readiness | Paper → readiness → canary → production gate | STR-001, STR-019, RDY-006, PAP-012 |
| Intelligence / Observability | Daily System Intelligence Dashboard | DSI-001 |
| Intelligence / Observability | Daily System Intelligence Report | DSI-002 |
| Intelligence / Observability | Market summary | DSI-002 |
| Intelligence / Observability | Opportunity summary | DSI-002 |
| Intelligence / Observability | Execution summary | DSI-002 |
| Intelligence / Observability | Capital summary | DSI-002 |
| Intelligence / Observability | Risk summary | DSI-002 |
| Intelligence / Observability | AI summary | DSI-002 |
| Intelligence / Observability | Strategy health | DSI-002 |
| Intelligence / Observability | Incident summary | DSI-002 |
| Intelligence / Observability | Readiness summary | DSI-002, RDY-005 |
| Intelligence / Observability | UNKNOWN reporting | DSI-004 |
| Intelligence / Observability | Historical reports | DSI-003 |
| Intelligence / Observability | Performance trends | DSI-003 |
| Safety | No fixed return assumption | PLT-007, TNP-014 |
| Safety | No artificial daily profit ceiling | TNP-012, TNP-013 |
| Safety | Opportunity accumulation | TNP-008, TNP-010 |
| Safety | Capital compounding | CAP-011, CAP-026 |
| Safety | Safe states | PLT-018, RSK-015 |
| Safety | Kill switches | RSK-008 |
| Safety | Reconciliation | REC-008, LED-009 |
| Safety | Recovery | REC-010, REC-015 |
| Safety | Restart safety | REC-004, REC-015 |
| Safety | Unknown-state handling | RSK-014, REC-016, DSI-004 |
| Safety | External-state verification | REC-014, EXE-006 |
| Safety | Disaster recovery | MIG-028 |
| Safety | Backup/restore | MIG-022, MIG-028 |
| Data / Research Integrity | Look-ahead bias prevention | BKT-002 |
| Data / Research Integrity | Data leakage prevention | BKT-002, BKT-004, BKT-005 |
| Data / Research Integrity | Protected dataset separation | BKT-005 |
| Data / Research Integrity | Survivorship bias protection | BKT-002 |
| Data / Research Integrity | Data deduplication | MKD-004 |
| Data / Research Integrity | Data integrity | MKD-004, MKD-008 |
| Data / Research Integrity | Experiment reproducibility | STR-026 |
| Data / Research Integrity | Decision lineage | AUD-012 |
| Data / Research Integrity | Data lineage | MKD-010 |
| Data / Research Integrity | Version traceability | STR-025, POL-013, AUD-002 |
| Performance / Reliability | Performance testing | VER-001 |
| Performance / Reliability | Load testing | VER-002 |
| Performance / Reliability | Chaos testing | VER-003 |
| Performance / Reliability | Backpressure | PERF-014 |
| Performance / Reliability | Concurrency | PERF-013 |
| Performance / Reliability | Atomicity | PERF-013, CAP-027 |
| Performance / Reliability | Queue management | PERF-014, TEC-007 |
| Performance / Reliability | Resource isolation | PERF-005, PERF-016 |
| Performance / Reliability | Research compute isolation | PERF-016 |
| Performance / Reliability | Connection resilience | EXA-015 |
| Performance / Reliability | Rate-limit management | EXA-014 |
| Security | AI permissions | SEC-008, AGT-022 |
| Security | Tool permissions | AIL-013, SEC-009 |
| Security | Secret management | SEC-005, MIG-009 |
| Security | Environment separation | OPS-004, MODE-006, OPS-013 |
| Security | Production change control | OPS-007 |
| Security | Security monitoring | MON-010 |
| Security | Authentication | SEC-009 |
| Security | Authorization | SEC-009 |
| Security | Key-management boundary | SEC-001, CUS-004 |
| Security | Withdrawal separation | SEC-006 |
| Security | Custody isolation | CUS-003, CUS-005 |
| Security | Incident management | INC-001 to INC-003 |
| Deployment | Local hosting | MIG-001, MIG-002 |
| Deployment | Server/cloud hosting | MIG-001, MIG-003 |
| Deployment | Hosting abstraction | MIG-004 |
| Deployment | Local ↔ server migration | MIG-006, MIG-020 |
| Deployment | Portable platform state | MIG-008 |
| Deployment | Environment-specific configuration | MIG-010 |
| Deployment | Configuration compiler/environment adapter | MIG-011 |
| Deployment | Database migration | MIG-012 |
| Deployment | Migration validation | MIG-018, MIG-021 |
| Deployment | Migration dry-run | MIG-024 |
| Deployment | Active-instance protection | REC-013, REC-020 |
| Deployment | Split-brain prevention | REC-019 (TC-07 open) |
| Deployment | Failover | REC-021 (FUTURE) |
| Deployment | Standby | REC-022 |
| Deployment | Deployment reproducibility | OPS-008 |
| Deployment | Infrastructure-as-code where approved | OPS-009 (PROPOSED) |
| Deployment | Backup/restore | MIG-022 |
| Deployment | Disaster recovery | MIG-028 |
| Repository / Governance | Canonical repository knowledge base | ARCH-017 |
| Repository / Governance | Single master requirements registry | ARCH-030 |
| Repository / Governance | Single master roadmap | RMP-003 |
| Repository / Governance | Single traceability system | ARCH-031 |
| Repository / Governance | ADRs | ARCH-006 (decision records in docs/decisions) |
| Repository / Governance | Conflict register | ARCH-006 (findings register) |
| Repository / Governance | Duplicate-system prevention | ARCH-016, ARCH-027 |
| Repository / Governance | Canonical service ownership | ARCH-027 |
| Repository / Governance | Contract-first development | ARCH-025 |
| Repository / Governance | API/interface versioning | ARCH-026 |
| Repository / Governance | Deprecation | ARCH-015 (DEPRECATED / REPLACED class) |
| Repository / Governance | Documentation ownership | ARCH-017 |
| Repository / Governance | Consistency system | ARCH-032 |
| Repository / Governance | Requirement classification | ARCH-015 |
| Repository / Governance | No silent requirement promotion | ARCH-029 |

## Final state

```text
PART 2 DOCUMENTATION            = VERIFIED (this record)
OWNER DECISIONS NEEDED          = CF-14, OQ-24, OQ-25, OQ-26, TC-07;
                                  confirm or leave: CAP-028, OPS-009, ARCH-034, REC-021
COMPLETE DOCUMENTATION REVIEW   = NOT STARTED (handoff §101; P2§329)
PRODUCT IMPLEMENTATION          = NOT STARTED, NOT AUTHORIZED
USER APPROVAL                   = REQUIRED
```
