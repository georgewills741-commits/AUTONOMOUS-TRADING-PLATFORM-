# Handoff Part 3 — Verification Record

> **Status:** ACTIVE record of the Part 3 checkpoint (2026-09-30), made under the owner's [checkpoint and three-stage verification rule](../builder/checkpoint-and-verification-rule.md) ([DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)). What was reconciled: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md) and the [Part 3 reconciliation](part-3-reconciliation.md).
>
> **Later changes:** the owner decided the items this record lists as open on 2026-10-02 ([DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)): CF-17 changed (RSK-049 replaces RSK-048), CF-18 confirmed, OQ-27 answered, TC-08 decided, DUP-34 and DUP-35 confirmed, and the Part 3 reconciliation approved. CF-19, raised after this record (DEC-033), was decided at the same time (GOV-024 replaces GOV-018). TC-09 stays open until OPERATIONALIZATION is planned. This record is kept as written.

## Scope

Documentation and project tooling only. No platform code, configuration, schema, or infrastructure exists or was created. "Tests" for this checkpoint are therefore the documentation checks the rule's reading allows (DEC-032): the generator and checker, the requirement comparison, the round-trip checks of the preserved sources, the wording-fidelity checks, and negative tests of the checker itself.

## What changed

| Measure | Before (a9034ce) | After |
|---|---|---|
| Requirements | 612 (Part 1: 228, Part 2: 185, decisions: 199) | 723 (Part 1: 228, Part 2: 185, Part 3: 109, decisions: 201) |
| Requirement prefixes | 46 | 47 (GOV added) |
| Existing requirements changed, reclassified, removed | — | 0, 0, 0 (`compare_requirements.py a9034ce --strict`) |
| Systems | 34 | 34 (no new system) |
| Decisions | DEC-001 to DEC-030 | DEC-001 to DEC-032 |
| Findings | CF 16, DUP 31, OQ 26, TC 7, all resolved | CF 18 (CF-17 and CF-18 resolved by the builder, awaiting owner confirmation), DUP 38 (all resolved), OQ 27 (OQ-27 open), TC 9 (TC-08 and TC-09 open) |
| Values | V-01 to V-35 | V-01 to V-39 |
| System rules | — | SR-01 to SR-45 |
| Dependency edges | D-01 to D-65 | D-01 to D-71 |

## P3§541 workflow — where each step was done

| # | Step | Where |
|---|---|---|
| 1–3 | Read Parts 1, 2, and 3 | Parts 1 and 2 were read when received; their canonical requirements were re-read for this reconciliation. Part 3 read in full; preserved verbatim ([historical copy](../handoffs/part-3-consolidated-autonomy-capital-scaling.md)) |
| 4–6 | Inspect the repository; existing documentation; existing implementation | Repository inspected (Gate 3). Documentation: every specification listed in [docs/README](../README.md). Implementation: none exists; the only code is the documentation tooling in `tools/docs/` |
| 7 | Duplicate systems | DUP-32 to DUP-38; no new system |
| 8 | Conflicting requirements | CF-17, CF-18 |
| 9 | Missing systems | None missing: every Part 3 name maps to an existing owner ([system registry](../architecture/system-registry.md), "Named in Part 3") |
| 10 | Undocumented assumptions | Builder readings are written into DEC-031 (CF-17, CF-18, DUP-34's outcome mapping, DUP-35's mapping of the emergency state names) and listed for the owner |
| 11 | Master requirements registry | [Registry](../requirements/registry.md), generated, now with Part 3 sources |
| 12 | System Rules Register | [System Rules Register](../requirements/system-rules-register.md) |
| 13 | Capability/readiness model | [Readiness System](../systems/readiness-system.md), "Capability and readiness model" |
| 14 | Canonical architecture | [Architecture overview](../architecture/overview.md) (ARCH-036 to ARCH-040) |
| 15 | Service ownership | [System registry](../architecture/system-registry.md) |
| 16 | Authority boundaries | [Source-of-truth map](../architecture/source-of-truth-map.md) (ARCH-027, ARCH-037) and each system's boundary section |
| 17 | Dependency graph | [Dependency map](../architecture/dependency-map.md), D-66 to D-71 |
| 18 | Conflict register | [Findings register](../conflicts/register.md) |
| 19 | Duplication audit | Findings register DUP-32 to DUP-38; near-duplicate text check (Gate 1) |
| 20 | Master traceability matrix | [Part 3 reconciliation](part-3-reconciliation.md) with the Part 1 and Part 2 coverage; registry; System Rules Register |
| 21 | Master roadmap | [Roadmap](../roadmap/roadmap.md): RMP-012 and "Part 3 additions by stage" |
| 22 | Verification strategy | [Verification architecture](../architecture/verification-architecture.md) (VER), GOV-012, the planned verification column of the System Rules Register, and this record |
| 23 | Production-readiness model | [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md), "Production-readiness model" |
| 24 | Deployment/migration model | [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) and [Hosting and migration](../operations/hosting-and-migration.md) (MIG-031, MIG-032) |
| 25 | Reliability/recovery model | [Reliability and recovery model](../operations/reliability-and-recovery-model.md) |
| 26 | Feature-extensibility governance model | [Architecture governance](../architecture/architecture-governance.md) |
| 27 | Documentation audit | Below |
| 28 | Unresolved questions | For the owner: OQ-27, TC-08, the confirmations of CF-17 and CF-18, and the DUP-34 and DUP-35 readings. Recorded now and decided when OPERATIONALIZATION is planned: TC-09 ([project state](../project-state.md)) |
| 29 | Present for human review | The checkpoint report to the owner; [project state](../project-state.md) |
| 30 | STOP | No implementation started; the project waits for the owner |

## P3§535 checklist — every item traced

P3§536: the checklist is not approval of its items. Each item below is traced to the requirements that own it, with their current classes. None rests on a PROPOSED, FUTURE, REQUIRES CONFIRMATION, or DEPRECATED requirement; the one conditional item ("infrastructure-as-code where approved") was approved by the owner (DEC-029).

| P3§535 item | Canonical requirements | Classes | Note |
|---|---|---|---|
| Deterministic trading core | PLT-016, ARCH-019, ARCH-021 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| AI intelligence layer | ARCH-019, AIL-001, AIL-002 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT |  |
| Natural-language policy | NLP-001, NLP-004 | CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Policy compiler | NLP-004, POL-012 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT | Two steps: NL → structured (AI INTELLIGENCE), structured → rules (CORE) |
| Autonomous operation | PLT-013, PLT-015, PLT-024 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Capital-scaled capabilities | RDY-009, RDY-013, CAP-032 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Capital authority | CAP-001, ARCH-027 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Risk authority | RSK-001, ARCH-027 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Portfolio authority | PRT-001, ARCH-027 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Whole-market opportunity discovery | OPP-001, OPP-013, OPP-018 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Aggressive opportunity search | OPP-017, PLT-022 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Opportunity filter | OPP-005, OPP-008 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Opportunity database | OPP-014, OPP-016 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Rejected opportunity analysis | OPP-015 | CONFIRMED REQUIREMENT |  |
| Missed opportunity analysis | PFC-012, PFC-016 | SYSTEM REQUIREMENT |  |
| False opportunity analysis | PFC-013, PFC-016 | SYSTEM REQUIREMENT |  |
| True net profitability | TNP-001, TNP-018, TNP-020 | CONFIRMED REQUIREMENT |  |
| Fee engine | QNT-005 | SYSTEM REQUIREMENT |  |
| Slippage engine | QNT-006 | SYSTEM REQUIREMENT |  |
| Liquidity | TNP-024 | CONSTRAINT |  |
| Funding | TNP-018, RSK-013 | CONFIRMED REQUIREMENT |  |
| Market regime | RGM-001, RGM-002 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| UNKNOWN REGIME | RGM-002, RGM-008 | SYSTEM REQUIREMENT; CONSTRAINT |  |
| Arbitrage | ARB-001 | SYSTEM REQUIREMENT |  |
| Cross-exchange arbitrage | XAR-001 | CONFIRMED REQUIREMENT |  |
| Triangular arbitrage | TAR-001, TAR-003 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Pre-positioned capital | XAR-005, CAP-039 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Intelligent rebalancing | CAP-023, CAP-037, CAP-038 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT | Rebalancing Engine is part of SYS-07 (DUP-34) |
| Anti-rebalancing churn | CAP-040 | CONSTRAINT |  |
| Capital reserves | CAP-029, CAP-045, ARB-008 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Capital scaling | CAP-030, CAP-035 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Capital growth detection | CAP-046 | CONFIRMED REQUIREMENT |  |
| Capital reduction detection | CAP-046 | CONFIRMED REQUIREMENT |  |
| Feature eligibility | RDY-011, RDY-008 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Readiness states | RDY-004, RDY-017 | SYSTEM REQUIREMENT |  |
| Blockers | RDY-018 | CONFIRMED REQUIREMENT |  |
| Automatic readiness reassessment | RDY-024 | CONFIRMED REQUIREMENT |  |
| Canary readiness | STR-013, RDY-015 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Canary deployment | STR-014, STR-016, OPS-011 | CONFIRMED REQUIREMENT; CONSTRAINT | Canary is a production stage, not an environment (OPS-013) |
| Rollback | OPS-012, STR-017 | CONFIRMED REQUIREMENT |  |
| Safe Mode | RSK-015, RSK-030, RSK-043 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| No-new-position mode | RSK-029 | CONFIRMED REQUIREMENT |  |
| Kill switches | RSK-008, RSK-028 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT |  |
| 24/7 operation | OPS-006, OPS-018 | CONFIRMED REQUIREMENT |  |
| Automatic restart | REC-010, REC-025 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Recovery | REC-015, REC-026 | CONFIRMED REQUIREMENT |  |
| Reconciliation after restart | REC-015, REC-016 | CONFIRMED REQUIREMENT |  |
| Failover | REC-021, REC-023 | CONFIRMED REQUIREMENT | High availability approved (DEC-030) |
| Standby | REC-022, REC-029 | CONSTRAINT |  |
| Split-brain protection | REC-019, REC-024 | CONSTRAINT |  |
| Active-instance authority | REC-013, REC-020 | CONSTRAINT |  |
| AI Resource Governor | AIL-008, AIL-009 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Model Router | RTR-001, RTR-003 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| AI caching | AIL-010 | SYSTEM REQUIREMENT |  |
| AI failover | AIL-011, AIL-019 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| AI degradation | AIL-012, AIL-018 | SYSTEM REQUIREMENT |  |
| AI cost/value optimization | COST-001, AIL-008, AIL-021 | SYSTEM REQUIREMENT |  |
| Market Analyst | AGT-008, AGT-016 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Quant Research Agent | AGT-010, AGT-017 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT | Role kept; performed by the Research Agent (DEC-013) |
| Strategy Research Agent | AGT-012, AGT-017 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT | Role kept; performed by the Research Agent (DEC-013) |
| Trading Director | AGT-004, AGT-019 | SYSTEM REQUIREMENT |  |
| Devil's Advocate | AGT-006, AGT-007 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Performance Analyst | AGT-014, AGT-015 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Strategy Optimizer | AGT-017, AGT-016 | CONFIRMED REQUIREMENT | Role kept; performed by the Research Agent (DEC-013) |
| Model Evaluation Agent | AGT-017, MEV-003 | CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE | Role kept; a deterministic service, not an AI agent (DEC-013) |
| AI Cost Manager | COST-001, COST-002 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE | Deterministic service (DEC-013) |
| Hallucination Firewall | AIV-001, AIV-017 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Evidence | AIV-001, AIV-019 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Timestamp requirements | AIV-001, MKD-005 | CONFIRMED REQUIREMENT |  |
| Multi-agent validation | AIV-007, AIV-014 | CONFIRMED ARCHITECTURAL PRINCIPLE; CONFIRMED REQUIREMENT |  |
| Strategy Factory | STR-003, STR-012 | SYSTEM REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Strategy Registry | STR-023 | SYSTEM REQUIREMENT |  |
| Paper trading | PAP-004, PAP-006 | CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Live trading | MODE-001, MODE-006 | CONFIRMED REQUIREMENT; CONSTRAINT | Only after OPERATIONALIZATION's canary and live items and the operator's maximum mode (RMP-002, MODE-003) |
| Strategy drift | PFC-009, PFC-018 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Loss-streak protection | RSK-026, RSK-045 | SYSTEM REQUIREMENT |  |
| Excessive-trading protection | RSK-027, RSK-046 | SYSTEM REQUIREMENT |  |
| Anti-overfitting | BKT-006 | CONFIRMED REQUIREMENT |  |
| Walk-forward testing | BKT-007 | SYSTEM REQUIREMENT |  |
| Stress testing | BKT-008 | SYSTEM REQUIREMENT |  |
| Monte Carlo/distribution analysis | BKT-009 | SYSTEM REQUIREMENT |  |
| Performance testing | VER-001 | CONFIRMED REQUIREMENT |  |
| Load testing | VER-002 | CONFIRMED REQUIREMENT |  |
| Chaos testing | VER-003 | CONFIRMED REQUIREMENT |  |
| Backpressure | PERF-014, PERF-021 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Concurrency | PERF-013, PERF-022 | CONSTRAINT |  |
| Atomic capital reservation | CAP-027 | CONSTRAINT |  |
| Rate-limit management | EXA-014 | SYSTEM REQUIREMENT |  |
| Connection management | EXA-015 | SYSTEM REQUIREMENT |  |
| Data quarantine | MKD-009, MKD-013 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Time synchronization | HLT-013, HLT-014 | SYSTEM REQUIREMENT; CONFIRMED REQUIREMENT |  |
| Data lineage | MKD-010 | CONFIRMED REQUIREMENT |  |
| Decision lineage | AUD-012 | CONFIRMED REQUIREMENT |  |
| Experiment reproducibility | STR-026 | CONFIRMED REQUIREMENT |  |
| Reconciliation | REC-008, LED-009 | CONFIRMED ARCHITECTURAL PRINCIPLE; CONSTRAINT |  |
| Disaster recovery | MIG-028, MIG-031 | CONFIRMED REQUIREMENT |  |
| Backup/restore | MIG-022, REC-028 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Security monitoring | SEC-009, MON-010 | SYSTEM REQUIREMENT |  |
| AI permissions | SEC-008, AGT-022 | CONSTRAINT; SYSTEM REQUIREMENT |  |
| Tool permissions | AIL-013, AGT-022 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT |  |
| Secret management | SEC-005, OPS-016 | CONSTRAINT |  |
| Environment separation | OPS-004, MODE-006 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Production change control | OPS-007, OPS-020 | CONFIRMED REQUIREMENT |  |
| Incident management | INC-001, INC-004 | CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Requirement traceability | ARCH-031, ARCH-040 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| ADRs | GOV-016 | CONFIRMED REQUIREMENT |  |
| Deprecation | GOV-009, GOV-008 | SYSTEM REQUIREMENT; CONSTRAINT |  |
| Duplicate-system prevention | ARCH-016, GOV-003, GOV-014 | CONFIRMED ARCHITECTURAL PRINCIPLE; CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Contract-first development | ARCH-025, GOV-007 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT |  |
| API/interface versioning | ARCH-026, GOV-006 | CONSTRAINT |  |
| Local hosting | MIG-002 | SYSTEM REQUIREMENT |  |
| Server/cloud hosting | MIG-003 | CONFIRMED REQUIREMENT |  |
| Local/server migration | MIG-006, MIG-007 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Portable platform state | MIG-008 | SYSTEM REQUIREMENT |  |
| Environment-specific configuration | MIG-010, MIG-011 | CONFIRMED ARCHITECTURAL PRINCIPLE; SYSTEM REQUIREMENT |  |
| Migration validation | MIG-018 | CONFIRMED REQUIREMENT |  |
| Active-instance protection | REC-013, EXE-010 | CONSTRAINT |  |
| Split-brain prevention | REC-019, REC-024 | CONSTRAINT |  |
| Failover/standby | REC-021, REC-023, REC-029 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Deployment reproducibility | OPS-008, OPS-014 | CONFIRMED REQUIREMENT |  |
| Infrastructure-as-code where approved | OPS-014, OPS-015 | CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE | Approved and mandatory since DEC-029 (OPS-009 replaced) |
| Canonical repository knowledge base | ARCH-017, MEM-004 | CONFIRMED ARCHITECTURAL PRINCIPLE; CONSTRAINT |  |
| Single master requirements registry | ARCH-030 | CONFIRMED REQUIREMENT |  |
| Single master roadmap | RMP-003 | CONFIRMED REQUIREMENT |  |
| Single traceability system | ARCH-031, ARCH-040 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Feature extensibility | GOV-001 | CONFIRMED ARCHITECTURAL PRINCIPLE |  |
| Feature conflict detection | GOV-004 | CONSTRAINT |  |
| Feature dependency analysis | GOV-005 | CONSTRAINT |  |
| Feature security review | GOV-010, GOV-002 | CONFIRMED REQUIREMENT |  |
| Feature performance review | GOV-002 | CONFIRMED REQUIREMENT |  |
| Feature migration impact | GOV-002, GOV-013 | CONFIRMED REQUIREMENT |  |
| Feature rollback | GOV-019, GOV-008 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Capability registry | RDY-020 | SYSTEM REQUIREMENT | Component of SYS-34 (DUP-33) |
| System Rules Register | ARCH-038 | CONFIRMED REQUIREMENT |  |
| Readiness matrix | RDY-023 | SYSTEM REQUIREMENT | Component of SYS-34 (DUP-33) |
| Blocker explanations | RDY-018, RDY-019 | CONFIRMED REQUIREMENT |  |
| Capital-aware capability scaling | RDY-009, RDY-013 | CONFIRMED REQUIREMENT; CONSTRAINT |  |
| Autonomous capability unlocking | RDY-012 | CONFIRMED REQUIREMENT |  |
| Safe degradation | HLT-005, PERF-011, AIL-012 | CONFIRMED ARCHITECTURAL PRINCIPLE; CONFIRMED REQUIREMENT; SYSTEM REQUIREMENT |  |
| Controlled self-improvement | STR-009, STR-002 | CONFIRMED REQUIREMENT; CONSTRAINT |  |

## Documentation audit (P3§541 item 27)

| Check | Result |
|---|---|
| Stale statements | Searched for statements still describing the state before Part 3 ("Parts 1 and 2 are documented", "No open questions", "Part 2 findings await", old counts and ranges) and for notes expecting content from an earlier handoff ("expected with Part 2 contracts" and variants). Six active stale notes from earlier rounds were found and corrected: roadmap FOUNDATION status; Strategy Management boundary (replaced STR-011, "Part 2 verification architecture"); Recovery and Reconciliation boundary (replaced REC-009, "Part 2 contracts"); Market Regime Engine boundary ("Part 2 contracts"); Deployment and Operational Readiness ("Canary is defined in STR-011", found by the independent review); the Performance Controller's status line (ARBITRAGE only, before DEC-024). The status lines of the 16 specifications that gained Part 3 requirements now name Part 3 and its sections Dated decision records keep their wording as history; DEC-024 already annotates their "expected in Part 2" statements |
| Duplicates | DUP-32 to DUP-38 recorded and resolved. Near-duplicate text check over all 723 requirements: one pair above the threshold, ARCH-031 / ARCH-040; reviewed and kept, because ARCH-040 must restate the chain to show where the rule and the interface links go, and it says "in addition to ARCH-031" |
| Contradictions | CF-17 and CF-18 recorded, reconciled in DEC-031, and listed for the owner. No other contradiction found between Part 3 and the existing requirements or decisions (DEC-031, decision 5) |
| Missing documents | P3§537's homes and P3§541's artifacts all exist (DEC-031, decision 2; the workflow table above). No giant miscellaneous document was created |
| Obsolete documents | None. The Part 3 copy is labelled HISTORICAL; nothing was deprecated |
| Requirements with no owner, stage, or source | None: the checker requires a known prefix (owner and stage) and an existing source section for every requirement |
| Undocumented assumptions | Builder readings are stated in DEC-031 and flagged for the owner. One unsupported statement was found in a note (that a standby holds trading credentials) and reworded to what DEC-030 records |

## Verification gates (owner's rule, DEC-032)

### Gate 1 — implementation / functional: PASS (after fixes)

| Check | Evidence | Result |
|---|---|---|
| Documentation checker | `python3 tools/docs/build_index.py --check-only`: no errors; 723 requirements (Part 1: 228, Part 2: 185, Part 3: 109, decisions: 201), 47 prefixes, 92 findings, 32 decisions, 34 systems, 45 system rules; every Part 3 section accounted for (153 of 200 produce new requirements; the other 47 have a written disposition). Check-only mode now also fails if a generated file is out of date | PASS |
| Generation is idempotent | Two consecutive generator runs produce identical files; `--check-only` confirms the committed generated files are current | PASS |
| No existing requirement changed | `python3 tools/docs/compare_requirements.py a9034ce --strict`: 111 added, 0 removed, 0 changed, now including indented continuation lines such as RSK-015's safety levels; exit status 0 | PASS |
| Preserved sources are exact | Strict round trip, ignoring only separator lines of ten or more "=": Part 3 copy 2,859 content lines identical to the received text; checkpoint rule 176 lines identical | PASS after fix |
| Wording fidelity | Every word of each Part 3 requirement compared with its cited sections: the only words not in the source are the connectives of "in addition to X"; no modal verb added. Per section, the count of "must", "must not", "never", and "should not" in the source was compared with the count across all requirements citing it: the one remaining difference (P3§389, two "must" carried by one "must" in PLT-022 for the same two verbs) keeps the meaning | PASS after fix |
| Conditional wording | No confirmed-class requirement cites a section with approval-conditional wording; P3§509 ("may maintain") is PROPOSED (GOV-018) | PASS |
| §535 checklist | All 140 items traced to existing requirements; none rests on an unapproved class | PASS |
| Checker negative tests | One error injected per case in a scratch copy; the checker rejected all 13: unknown P3 section, missing Part 3 row, Part 3 title mismatch, section with no disposition, SR class mismatch, SR numbering gap, undefined SR reference, SR resting on a PROPOSED requirement, undefined GOV requirement, damaged Part 3 copy, malformed source prefix, stale generated reconciliation column, stale registry | PASS |
| Comparison negative tests | One existing requirement (RSK-005) altered temporarily, then one indented continuation line (RSK-015's SAFE MODE definition): `--strict` reported each change and exited 1; restored, it exited 0 | PASS |

**Defects found and fixed in Gate 1:**

1. **Part 3 copy missing one line.** The converter treated the lone "=" in P3§356 ("AUTHORIZED POLICY = POSSIBLE CAPABILITY EXPANSION") as a separator and dropped it. The first round-trip check ignored every "=" line and therefore could not see it. Fixed: the line is restored, and the round trip now ignores only separator lines of ten or more "=". The same check on the Part 1 copy shows its lone "=" (§13) was kept.
2. **RDY-013** rendered that formula with "→"; corrected to the source's "=".
3. **PFC-016** said "reasons may include" where P3§392 says "Examples:"; corrected to "examples include", adding no modal verb.

### Gate 2 — architecture / consistency: PASS (after fixes)

| Check | Result |
|---|---|
| Platform principles and system rules ("Global Game Constitution equivalent", DEC-032) | Every Part 3 "SYSTEM RULE" and "FINAL SYSTEM RULE" section (38) and every "no ..." item of P3§534 is indexed in the System Rules Register. No new requirement contradicts a platform principle (ARCH-028 index) |
| Safety floor and precedence | The safety floor stays on top (DEC-026); RSK-004 unchanged; Part 3's layers placed by RSK-048 and flagged as CF-17, including its consequence for security controls outside the floor |
| Deterministic vs AI | No new requirement gives AI authority. AIL-018 to AIL-021 only restrict AI; RDY, CAP, and GOV decisions are deterministic |
| Risk, capital, execution controls | Capital growth never widens authorization or exposure by itself (PLT-023, CAP-034, CF-18); rebalancing stays inside SYS-07 and CAP-025 (CAP-042); emergency actions stay deterministic and idempotent (RSK-041 with RSK-018, RSK-019) |
| State and reconciliation | Restart is not resume (REC-025); restore is reconciled (REC-028); one active copy (SR-33) |
| Ownership | No new system (34 before and after). Every Part 3 name maps to an existing owner (system registry, "Named in Part 3"). Every prefix lives in exactly one document |
| Roadmap | Every new ID is placed in the "Part 3 additions by stage" table except GOV-018, which is PROPOSED and listed as "not in any stage" |
| Dependencies | New relationships recorded as D-66 to D-71 |
| Earlier decisions | DEC-006 to DEC-030 re-checked against Part 3 (DEC-031, decision 5) |
| Stale or contradictory statements | See the documentation audit above |

**Defects found and fixed in Gate 2:**

1. A fourth stale note (Market Regime Engine, "expected with Part 2 contracts") was corrected and added to DEC-031's list.
2. A note under REC-029 stated that a standby holds trading credentials; DEC-030 does not say so. Reworded to what is recorded: the lease keeps a standby from trading; how it obtains credentials is decided with the lease authority.

### Gate 3 — independent final audit / regression: FAIL on first review, fixed, PASS on re-run

**Independent reviewer.** A separate review agent that did not write the change audited the working tree against a9034ce, read-only. The first attempt stopped on a usage limit before reviewing anything and was relaunched. The review read all of §351 to §550, checked every "Covered by" row and every new requirement against its source, re-ran the checker and the comparison, and tried changes in a scratch copy. It found **2 blocking and 14 non-blocking defects**. Gate 3 therefore failed. Each defect was fixed and the affected checks re-run:

| # | Severity | Finding | Fix |
|---|---|---|---|
| 1 | BLOCKING | P3§399's "conflicting strategy decisions" (and its list of what concurrency must not create) was not carried by the requirements its "Covered by" row cited | New PERF-022; the row now says "Also"; SR-21 includes it; placed in CORE TRADING FOUNDATION |
| 2 | BLOCKING | TNP-025 dropped P3§394's "must" ("the economics account for") | Now "the system must account for" |
| 3 | Non-blocking | P3§449's admission factors, including "current workload", were not in the cited requirements (RTR-002 is the router's, not the Governor's) | New AIL-021; row and AI note corrected |
| 4 | Non-blocking | The claim that every "no ..." item of PLT-027 is indexed in the register was false | SR-43 (no undocumented production changes), SR-44 (no unsafe migration), SR-45 (no hidden state, no silent assumptions); SR-19 and SR-37 extended |
| 5 | Non-blocking | CF-17 and CF-18 were labelled RESOLVED while awaiting the owner; spec notes and SR-20 stated the readings as fact | Status "RESOLVED BY BUILDER — AWAITING OWNER CONFIRMATION"; markers added to the spec notes, SR-20, and the documentation index |
| 6 | Non-blocking | RSK-048 ranks security controls outside the floor below user hard policy, and CF-17 did not put that to the owner | Stated in CF-17, the risk note, DEC-031, and the project state |
| 7 | Non-blocking | DUP-35 made DEGRADED an alias of a safety level (it is a health state) and narrowed RECOVERY to CRITICAL RECOVERY; the readings were not in DEC-031's list for the owner | Mapping rewritten without merging meanings; glossary, register, DEC-031, and the reliability model updated; DUP-34 and DUP-35 listed for the owner |
| 8 | Non-blocking | REC-029's note said a standby "cannot place orders", but the lease is checked by the platform, not the venue; the credential question was only in a note | Note softened; recorded as TC-09 |
| 9 | Non-blocking | Stale "Canary is defined in STR-011" | Corrected |
| 10 | Non-blocking | DEC-032 had no Alternatives section, contradicting "records from DEC-031 onward include one" | Section added |
| 11 | Non-blocking | V-30 and V-31 not updated for RSK-045, RSK-046; V-39 overlapped V-35 and, as a policy value, would have locked every feature until set | V-30, V-31 updated; V-39 is now derived per feature from evidence (OBSERVED), policy can only tighten it, V-35 stays the operator's bound |
| 12 | Non-blocking | D-71 marked STATED though P3§392, §393 name no system; partly duplicated D-57 | INFERRED; the duplicate edge removed |
| 13 | Non-blocking | Status lines of 16 specifications and the glossary did not mention Part 3 | Updated, with each specification's Part 3 sections |
| 14 | Non-blocking | The registry's Stage column (one per owner) disagreed with the roadmap's per-requirement placement | Column renamed "Default stage"; the registry states that the roadmap is authoritative for individual placement |
| 15 | Non-blocking | Checks that could pass without proving their claim: both parsers ignored indented continuation lines; `--check-only` did not detect stale generated files; garbled docstring | Both parsers read continuation lines; check-only regenerates in memory and fails on any difference; docstring fixed; both proven by new negative tests (Gate 1) |
| 16 | Non-blocking | Some "Covered by" or "loop restated" notes omitted the covering requirement (§422, §441, §517, §521) | Notes now cite PLT-025, CAP-046, RDY-024, CAP-035; DUP-37 and DEC-031 updated |

The reviewer also confirmed as correct: counts across documents; that every condition in the source ("unless explicitly authorized and validated", "where technically possible", "where approved", and others) is kept; every "in addition to" list adds only new items; 38 of the 42 "Covered by" rows held as written (the other four, §399, §422, §441, §449, are findings 1, 3, and 16); the §535 classes; DEC-026, DEC-028, DEC-030, POL-005 to POL-007, and the AI limits are preserved; no duplicate authority; the generated files were current; repository completeness.

**Builder's own separate pass (repository completeness).** `git status`: 35 modified, 10 untracked files, all part of this change; `git status --ignored`: nothing ignored, no `.gitignore`; `git diff --check a9034ce`: clean; untracked files have no trailing whitespace and end in a newline; no secrets, keys, or credentials in the diff or the new files; scratch work stayed in the session scratchpad, outside the repository.

### Gate 3 re-run — PASS

A second independent reviewer, which had not seen the first review's reasoning, re-checked the working tree read-only after the fixes, testing the tool changes in a scratch copy. Result: **no blocking findings**. Of the 16 earlier findings, 15 were confirmed FIXED and one (7, the DUP-35 wording) was only partly fixed. It also reported seven non-blocking items, all fixed before this checkpoint:

| # | Finding | Fix |
|---|---|---|
| 1 | "Aliases" wording for DUP-35 was still in four places (reconciliation row 372, system registry, DEC-031, this record) | Reworded to the corrected mapping everywhere; row 372 now also cites RSK-021, RSK-022; the registry names SYS-29 as well as SYS-09 |
| 2 | Ranges and counts not updated after PERF-022, AIL-021, SR-43 to SR-45 (DEC-031, this record) | Updated; the system registry's AI Resource Governor row cites AIL-021 |
| 3 | "Must be validated" was attached to RSK-046's thresholds (V-31) without a source; P3§435's sentence belongs to loss streaks only | Limited to RSK-045 and V-30; V-31 now cites RSK-046's "legitimate or pathological" determination |
| 4 | The requirements README still described the registry column as "roadmap stage" | Now "default stage", with the roadmap authoritative for individual placement |
| 5 | The tools README did not describe the new check-only and continuation-line behavior | Documented |
| 6 | TC-09 and the DUP-34 and DUP-35 readings were listed inconsistently across documents | One framing everywhere: the owner's items are CF-17, CF-18, OQ-27, TC-08, and the two readings; TC-09 is recorded now and decided when OPERATIONALIZATION is planned |
| 7 | The Readiness System's status line omitted P3§527 | Added |

The reviewer also confirmed: counts agree (111 new, 723 total, 45 rules, 92 findings, 153 of 200 sections); every "no ..." item of P3§534 maps to a rule; PERF-022, TNP-025, and AIL-021 match their sources word for word with the same modal verbs; `--check-only` fails on six kinds of stale generated output and passes when clean; the comparison catches edited, deleted, or separated continuation lines and ignores mere re-indentation; no contradiction with DEC-026, DEC-028, DEC-030, or POL-005 to POL-007; no fix weakens a safety, risk, capital, or AI-authority control; repository completeness.

## Result

| Gate | Result |
|---|---|
| Verification 1 — implementation / functional | **PASS** after three fixes |
| Verification 2 — architecture / consistency | **PASS** after two fixes |
| Verification 3 — independent final audit / regression | **FAIL** on the first review (2 blocking, 14 non-blocking), all fixed; **PASS** on the independent re-run, whose 7 non-blocking items were also fixed |

After the last fixes, the checker, the strict comparison, the round trips, and `git diff --check` were run again before the checkpoint commit; see the [project state](../project-state.md) checkpoint log.

## Remaining issues and limitations

- **For the owner:** CF-17 and CF-18 (confirmations), OQ-27, TC-08, and the DUP-34 and DUP-35 readings; the human review of the whole Part 3 reconciliation (P3§541 items 29–30).
- **Recorded for later:** TC-09 (standby trading keys), decided when OPERATIONALIZATION is planned.
- **Limits of these checks:** they verify documentation only. No platform code, schema, interface, or test exists yet, so nothing here is evidence that the platform works. The wording checks compare words, not meaning; the meaning was checked by reading, by the builder and by two independent reviews.
