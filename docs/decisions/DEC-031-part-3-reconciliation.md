# DEC-031 — Reconciliation of Handoff Part 3 with Parts 1 and 2 and the owner's decisions

- **Status:** ACCEPTED; **confirmed by the owner on 2026-10-02** ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)), with CF-17 changed by the owner (RSK-049 replaces RSK-048) and TC-08 decided differently from this record's recommendation: the older records' alternatives are added now, where sourced (done on 2026-10-02). The text below is the reconciliation as made; the owner's answers are in DEC-035.
- **Original status (2026-09-30):** ACCEPTED (builder reconciliation under Part 3 §351 and §541, constitution Rules 30–34, and the owner's checkpoint rule). **Awaiting human review** (P3§541 item 29): the owner may override any placement or reading here. CF-17 and CF-18 are listed under "Left for the owner" for confirmation.
- **Date:** 2026-09-30
- **Source:** [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N
- **Resolves:** CF-17, CF-18 (both then awaiting the owner's confirmation; since decided, [DEC-035](DEC-035-owner-decisions-part-3-findings.md)), DUP-32 to DUP-38. **Raises:** OQ-27, TC-08, TC-09 (OQ-27 and TC-08 since decided, DEC-035).
- **Changes placement in:** none of the earlier decisions. It adds to [DEC-024](DEC-024-part-2-reconciliation.md) (placement rules) and applies [DEC-026](DEC-026-safety-floor-and-layered-control.md) (safety floor) and [DEC-028](DEC-028-capital-buckets-and-progressive-activation.md) (capital buckets, progressive activation).

## Context

Part 3 asks for Parts 1, 2, and 3, every earlier decision, and the previously discussed system rules to become one knowledge base (P3§351, §550). It is a documentation handoff and "NOT permission to immediately begin production implementation". Much of it restates Parts 1 and 2, sometimes more than once within Part 3 (the loops in §515–§521 and the final principles in §522–§550). It adds a capital-scaled capability model, readiness and blocker rules, autonomous rebalancing details, a set of named "system rules", feature-extensibility governance, and 24/7 reliability rules. It asks for specific artifacts (§541): a System Rules Register, a capability/readiness model, a production-readiness model, a reliability/recovery model, and a feature-extensibility governance model.

## Decision 1 — Classification

DEC-024's rules apply unchanged: wording decides the class; "may maintain", "where approved", and similar wording stays conditional; a restatement adds no requirement and is mapped. The §535 checklist is not approval of its items (§536): each item is traced to its canonical requirement and existing class in the [Part 3 verification record](../traceability/part-3-verification.md). Sources are cited as `P3§N`.

- **One item is conditional:** the feature status registry (P3§509, "the repository may maintain") is GOV-018, PROPOSED.
- **Examples are not values.** The dollar amounts of P3§352, §355, and §502, the canary progression of §380, and the 99.9999% of §490 are illustrations, recorded as such in the [values register](../requirements/values-register.md).

## Decision 2 — Where Part 3 goes (P3§537)

No miscellaneous document was created. Part 3's named homes map onto the existing canonical documents; nothing was renamed (constitution Rule 144).

| P3§537 home | Canonical document here | Part 3 requirements |
|---|---|---|
| Capital Architecture | [Global Capital Authority](../systems/capital-management.md) | CAP-034 to CAP-046 |
| Risk Architecture | [Risk Engine](../risk/risk-engine.md) | RSK-040 to RSK-048 |
| Arbitrage Architecture | [Arbitrage documents](../systems/arbitrage/arbitrage-intelligence.md); rebalancing stays with capital (ARB-007) | — |
| AI Architecture | [AI architecture](../ai/ai-architecture.md) | AIL-018 to AIL-021 |
| Policy Architecture | [Policy System](../systems/policy/policy-system.md) | — (Part 3's policy rules are PLT-023, RSK-048) |
| Deployment Architecture | [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) | OPS-018 to OPS-020; production-readiness model |
| Migration Architecture | [Hosting and migration](../operations/hosting-and-migration.md) | MIG-031, MIG-032 |
| Reliability / Operations | [Reliability and recovery model](../operations/reliability-and-recovery-model.md) (index), with [System Health](../operations/system-health.md), [Recovery and Reconciliation](../systems/recovery-and-reconciliation.md), [Incident Management](../operations/incident-management.md) | HLT-014 to HLT-017, REC-025 to REC-029, INC-004, INC-005 |
| Architecture Governance | [Architecture governance](../architecture/architecture-governance.md) (new, prefix GOV) | GOV-001 to GOV-020 |
| System Rules Register | [System Rules Register](../requirements/system-rules-register.md) (new, SR-01 to SR-45) | ARCH-038, ARCH-039 |
| Master Requirements Registry | [Registry](../requirements/registry.md) (generated; now includes P3 sources) | — |

Other Part 3 requirements went to their owners: PLT-022 to PLT-028 ([platform overview](../product/platform-overview.md)), ARCH-036 to ARCH-040 ([architecture overview](../architecture/overview.md)), RDY-009 to RDY-026 ([Readiness System](../systems/readiness-system.md), which now documents the capability and readiness model), TNP-025, TNP-026, OPP-017 to OPP-020, PFC-016 to PFC-018, STR-027, STR-028, MKD-012, MKD-013, PERF-018 to PERF-022, RMP-012.

## Decision 3 — Duplicate responsibilities (one owner each)

| Finding | Resolution | Requirements |
|---|---|---|
| DUP-32 status sets | Four different questions, four status sets, kept apart: strategy readiness (RDY-004), component readiness (RDY-017), capability availability (RDY-011), and repository feature status (GOV-009, GOV-018). The first three are owned by SYS-34; the last is documentation governance | RDY-026 and the table in the Readiness System |
| DUP-33 Eligibility Engine, Canary Readiness Engine, capability registry, readiness matrix | Components of SYS-34 Readiness System, which already decides capability eligibility (RDY-008) and canary readiness (STR-013, STR-019). No new system | RDY-026 |
| DUP-34 Rebalancing Engine | The rebalancing-decision component of SYS-07 Global Capital Authority, which already decides rebalancing (CAP-018, CAP-023, CAP-031) using Arbitrage Intelligence's evaluation (ARB-006). CAP-038's decisions refine CAP-023's outcomes | CAP-037 to CAP-042 |
| DUP-35 emergency state names (P3§372) | Mapped onto the safety levels the owner adopted (RSK-015) and the health states (HLT-011) without merging meanings: DEGRADED stays the health state; RECOVERY covers transient recovery (RSK-021 to RSK-023) and CRITICAL RECOVERY; RESUMING = RSK-023's limited recovery. The final state machine stays an architecture task (HLT-002) | Mapping in the Risk Engine |
| DUP-36 Part 3 restating Parts 1–2 and itself | Mapped, not duplicated; where Part 3 states one principle several times (§389, §416, §522, §544), it becomes one requirement citing each section | [Part 3 reconciliation](../traceability/part-3-reconciliation.md) |
| DUP-37 the loops (P3§459, §515–§521) | Views of canonical flows: §459 = STR-009; §515 = ARCH-024; §516 = OPP-005 with TNP-020, CAP-016, AIV-016; §517 and §521 = CAP-046 with CAP-035 and RDY-024; §518 = HLT-015; §519 = GOV-002; §520 = REC-026 | Same |
| DUP-38 System Rules Register vs requirements registry vs platform principles index | The register is an index over requirements. Rule wording stays in the canonical requirement; the register holds a short name, owner, enforcement, violation handling, and planned verification. The principles index (ARCH-028) is unchanged | ARCH-038 |

## Decision 4 — Conflicts

- **CF-17 (rule precedence).** P3§471 puts USER HARD POLICY above SYSTEM SAFETY, as P2§101 did. The owner decided this question for P2§101 in DEC-026: the safety floor is on top and changes only through RSK-039. That decision is applied, not re-decided. RSK-048 places Part 3's new layers (security, capital, execution) into RSK-004's hierarchy in Part 3's own order: safety floor → user hard constraints → security → portfolio / risk policy → capital → execution → validated strategy rules → deterministic market conditions → AI analysis / proposal. RSK-004 is unchanged. Recorded, not chosen silently; the owner is asked to confirm the placement.
- **CF-18 (capital growth and automatic scaling).** P3§358 forbids automatically increasing leverage, trade frequency, position size, risk per trade, or market exposure when capital grows "unless explicitly authorized and validated"; P3§441 lists "authorized capital" among what realized profit updates automatically. RSK-036 (owner, DEC-026) lets the platform adjust limits and allocation to available capital inside the policy bounds; CAP-030 and CAP-032 scale buckets and capabilities with capital; POL-005 makes increases in authorized capital, leverage, or venues an important policy change. **Reading applied (all requirements kept):** growth updates available capital and the capability assessment automatically. It raises any of the five items of P3§358, or authorized capital, only where the operator's policy already authorizes that scaling (for example a limit expressed relative to capital, or a reinvestment rule under CAP-011) and the Readiness System has validated it. Anything else is a POL-005 change. The owner is asked to confirm.

## Decision 5 — Earlier decisions re-checked against Part 3

| Decision | Result |
|---|---|
| DEC-006 single operator, no custody | Consistent: P3§533 "users/accounts if applicable" does not add users |
| DEC-007, DEC-008 instruments and venues | Consistent: P3§508 lists future exchanges as future (GOV-017) |
| DEC-009 technology stack | Consistent: P3§512's complexity budget matches the modular monolith (TEC-008); P3§395 and §490 match PERF-006 and TEC choices made by measurement |
| DEC-010 pre-trade flow | Consistent: P3§515 and §516 are conceptual; DEC-010's runtime order (risk authorizes before capital reserves) is kept (CAP-016) |
| DEC-011, DEC-024 ownership | Extended by DUP-32 to DUP-38; no ownership moved |
| DEC-012, DEC-019, DEC-021 safety | Consistent: P3§371 to §376 add to RSK-015 to RSK-030 (RSK-040 to RSK-043); P3§372's names are mapped onto the safety levels and health states without merging meanings (DUP-35) |
| DEC-013 AI organization | Consistent: P3§513 (agent minimality) is what DEC-013 did; P3§535's roles are mapped in the [agents document](../ai/agents.md) (AGT-017) |
| DEC-014 net profit | Consistent: P3§394 adds precision and execution probability (TNP-025) inside the existing formula's "other execution costs" and latency terms |
| DEC-015, DEC-023 modes and autonomous approval | Consistent: P3§381 and §527 (eligibility is not activation) match STR-014 and STR-019 to STR-022 (RDY-016) |
| DEC-016 stage placement | Consistent: Part 3 items placed in the existing seven stages (RMP-012) |
| DEC-017 reporting | Consistent: the readiness matrix is shown through the daily report (DSI) |
| DEC-020 values | Applied: V-36 to V-39 added; examples recorded as illustrations |
| DEC-022 restart recovery | Consistent: P3§368, §369, §489, §526, §549 match REC-014 to REC-018 (REC-025 adds the service level and the readiness check) |
| DEC-025 documentation tooling | Extended: the checker now reads P3 sources and the System Rules Register; a requirement comparison tool is added (ARCH-032, ARCH-033) |
| DEC-026 safety floor | Applied to CF-17 and CF-18 |
| DEC-027 global controller, paper environment, adaptive execution | Consistent: P3§515's "global controller" is ARCH-035; EXE-011 stays FUTURE |
| DEC-028 capital buckets, progressive activation | Extended: P3§352 to §357 detail progressive activation (RDY-009 to RDY-014); CF-18 reading |
| DEC-029 infrastructure as code | Consistent: P3§535 still says "infrastructure-as-code where approved"; it is approved and mandatory (OPS-014) |
| DEC-030 high availability, one active copy | Consistent: P3§493 to §497 match REC-021 to REC-024; P3§494's distributed-execution exception is not designed, so no exception applies |
| DEC-032 checkpoint rule | Applied to this reconciliation |

## Alternatives considered

- **One "Part 3" document holding all of Part 3's content.** Rejected: P3§537 forbids a giant miscellaneous document, and it would compete with the owning specifications (ARCH-017).
- **New systems for the Eligibility Engine, Canary Readiness Engine, capability registry, and Rebalancing Engine.** Rejected: each responsibility already has an owner (RDY-008, STR-019, CAP-018, CAP-023), and new systems would create duplicate authorities (ARCH-027, P3§466, P3§512).
- **A System Rules Register that restates each rule's text.** Rejected: two copies of every rule would drift (constitution Rule 42); the register indexes the canonical requirement instead.
- **Adopting P3§471's order literally (user hard policy above system safety).** Not adopted: the owner already decided the same question the other way in DEC-026; the choice is recorded as CF-17 for confirmation rather than re-decided silently.
- **Merging Part 3's status lists into one state machine.** Rejected: they answer different questions and have different owners (DUP-32); both RDY-004 and P3§383 leave the final state models to architecture.
- **Retrofitting "Alternatives" into DEC-001 to DEC-030 now.** Not done: most alternatives were never recorded, and writing them now would invent history (constitution Rule 181). Recorded as TC-08.

## Consequences

- 111 new requirements: 109 cite a Part 3 section and 2 cite this record (RDY-026, RSK-048). Two of them (PERF-022, AIL-021) were added after the independent review found P3§399 and P3§449 content that the cited requirements did not carry ([verification record](../traceability/part-3-verification.md)). One new prefix, GOV. No existing requirement's text or class changed, none was deprecated, none was removed. [`tools/docs/compare_requirements.py`](../../tools/docs/README.md) shows this against the previous commit.
- New documents: [Architecture governance](../architecture/architecture-governance.md), [System Rules Register](../requirements/system-rules-register.md), [Reliability and recovery model](../operations/reliability-and-recovery-model.md), [Part 3 reconciliation](../traceability/part-3-reconciliation.md), [Part 3 verification](../traceability/part-3-verification.md).
- Stale notes found and corrected during the reconciliation: the roadmap's FOUNDATION status still said the Part 2 findings awaited the owner; the Strategy Management boundary cited replaced STR-011 and "Part 2 verification architecture"; the Recovery and Reconciliation boundary cited replaced REC-009 and "Part 2 contracts"; the Market Regime Engine boundary also expected "Part 2 contracts"; Deployment and Operational Readiness still said "Canary is defined in STR-011"; the Performance Controller's status line still placed it in ARBITRAGE only.
- Implementation is still not authorized (P3 header, P3§541 item 30).

## Left for the owner

| Item | Question |
|---|---|
| CF-17 | Confirm the precedence of RSK-048: the safety floor first (DEC-026), then user hard constraints, security, risk, capital, execution, strategy, market conditions, AI. In particular: security controls outside the floor (for example SEC-006 to SEC-008) then rank below your hard policy. Should they rank above it instead? |
| CF-18 | Confirm the reading: capital growth raises limits or authorized capital only where policy already authorizes that scaling and readiness validates it; otherwise it is a policy change needing the operator |
| OQ-27 | Is a separate Part 4 coming? Part 3's header names "PART 3 / PART 4 MATERIAL PREVIOUSLY DISCUSSED" |
| TC-08 | Accept the approach for ADR alternatives in older records |
| TC-09 | How a standby obtains trading keys for automatic takeover without being able to trade before it holds the lease (decide when OPERATIONALIZATION is planned) |
| Builder readings | Check the DUP-34 mapping of the rebalancing decisions onto CAP-023's outcomes and the DUP-35 mapping of Part 3's emergency state names |
| Review | P3§541 item 29: review the reconciled architecture before normal implementation |
