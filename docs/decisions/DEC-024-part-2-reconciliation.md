# DEC-024 — Reconciliation of Handoff Part 2 with Part 1 and the owner's decisions

- **Status:** ACCEPTED (builder reconciliation under Part 2 §182 and §331, and constitution Rules 30–34; the owner may override any item). CF-14, OQ-24 to OQ-26, and TC-07 are **not** decided here; they wait for the owner.
- **Date:** 2026-09-30
- **Source:** [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N
- **Resolves:** CF-15, CF-16, DUP-23 to DUP-31
- **Changes placement in:** [DEC-016](DEC-016-roadmap-stage-placement.md) (Performance Controller stage), [DEC-023](DEC-023-autonomous-canary-approval.md) (where the Governance and Readiness Engine is registered). The owner's decisions in DEC-023 are unchanged.

## Context

Part 2 asks for Part 1, every earlier decision, and Part 2 to become one knowledge base: reconcile, deduplicate, classify, resolve conflicts, assign ownership, and stop for review (P2§348). Much of Part 2 restates Part 1. §196 to §313 also restate Part 2's own §1 to §195 in shorter form. Part 2 also adds new capabilities and names some systems that already exist under other names.

## Decision 1 — How Part 2 content is classified

- **Wording decides the class.** A Part 2 statement worded with "must" or "should" becomes a requirement in the owning specification, with the same classes used for Part 1 (DEC-003).
- **Conditional wording stays conditional.** "Where approved", "if … approved", "requires architecture approval", and "remains a proposal" become PROPOSED, FUTURE, or PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION (P2§181, §290, §349; ARCH-029).
  - OPS-009: infrastructure as code (PROPOSED).
  - ARCH-034: domain command language (PROPOSED).
  - REC-021: failover (FUTURE).
  - CAP-028: extra capital categories (REQUIRES CONFIRMATION).
  - Custody items CUS-004, CUS-005, and LED-008 apply only if custody is approved.
- **A restatement adds no requirement.** It is mapped to the canonical requirement (DUP-31). Where Part 2 adds items to an existing list, the new requirement says "in addition to X-NNN" and lists only the additions, so no text is duplicated.
- **Sources are cited as `P2§N`,** keeping them apart from Part 1's `§NN`.

## Decision 2 — Duplicate responsibilities (one owner each)

| Finding | Resolution | Requirements |
|---|---|---|
| DUP-23 roles vs agents | Keep [DEC-013](DEC-013-ai-organization.md)'s five agents plus deterministic services. P2§200 allows "final decomposition … based on documented ownership", and P2§6 itself warns against overlapping agents. Every one of the nine roles is kept and mapped to its performer | AGT-017, AGT-018, AGT-022 |
| DUP-24 Readiness System vs Governance and Readiness Engine | One system. Registered as **SYS-34**, no longer a component of SYS-14: Part 2 lists it as a canonical authority separate from the Strategy Registry (P2§184), it aggregates evidence from many owners (P2§67), and it judges system changes too (P2§65). STR-019 to STR-022 stay in Strategy Management because they govern the lifecycle's APPROVAL stage, which SYS-34 performs | RDY-001 to RDY-007 |
| DUP-25 AI Resource & Decision Governor | The AI gateway's deterministic admission and resource-control component. The Model Router selects models; the AI Cost Manager sets budgets | AIL-008, AIL-009 |
| DUP-26 Opportunity Database | One platform-wide database owned by the Opportunity Detection Engine (SYS-05), derived from the event history as ARB-014 already required. The arbitrage database becomes its arbitrage view | OPP-014 to OPP-016 |
| DUP-27 Fee and Slippage Engines | Components of the Quantitative Engine (QNT-004 already computes fees and slippage); the True Net-Profit Engine combines them | QNT-005 to QNT-007 |
| DUP-28 market-data normalization | Adapters translate venue formats into canonical objects. Market-Data Infrastructure is the single normalization layer | EXA-013, MKD-011 |
| DUP-29 lifecycle views | STR-001 and STR-009 stay canonical. Part 2's "READINESS REVIEW" is the APPROVAL stage | STR-001, STR-009 |
| DUP-30 dashboard vs reporting | The Daily System Intelligence Dashboard extends MON-008 inside SYS-28 and reads every figure from its owner | DSI-006 |
| DUP-31 restatements | Mapped, not duplicated | [Part 2 reconciliation](../traceability/part-2-reconciliation.md) |

## Decision 3 — Conflicts resolved by reconciliation

- **CF-15 (environments).** Canary is a limited-exposure stage in the production environment, not a separate environment. A separate canary environment would need live credentials outside production, which P2§161 forbids. Research stays an environment: OPS-004 and constitution Rule 109 have it, and Part 2 does not remove it (OPS-013).
- **CF-16 (stage order).** The Performance Controller's core (PFC-001 to PFC-003, PFC-009 to PFC-013) moves from ARBITRAGE to DIRECTIONAL TRADING. Paper evidence and the Readiness System are built there and depend on it (RMP-011). Arbitrage tracking (PFC-014, PFC-015) stays in ARBITRAGE.

## Decision 4 — Other placements and terminology

- **New systems and requirement sets.**
  - SYS-34 Readiness System (RDY).
  - Two SYS-28 components with their own documents: the Daily System Intelligence Dashboard and Report (DSI) and Incident Management (INC, INC-003).
  - Two cross-cutting requirement sets: Hosting, Backup, and Migration (MIG) and Verification Architecture (VER).
  - Nothing else became a new system.
- **Split-brain, active authority, standby, and failover** belong to Recovery and Reconciliation (REC-019 to REC-022), which already owns the execution lease (REC-013).
- **"Platform principles", not "constitution".** P2§174 lets architecture choose the name for the central non-negotiable principles. They are indexed in the [platform overview](../product/platform-overview.md) as "platform principles", so they are never confused with the builder constitution.
- **"Policy compiler" covers two steps.** Natural language → structured policy is NLP-004, in AI INTELLIGENCE. Structured policy → enforceable rules is deterministic, belongs to the Policy System, and is built in CORE TRADING FOUNDATION. So RMP-009 (policy compiler before safe states) fits the stage order.
- **Unsupported claims = UNVERIFIED.** Part 2's "unsupported" claim is AIV-002's UNVERIFIED claim, and the existing term is kept.
- **Readiness states vs lifecycle states.** The Strategy Registry holds the lifecycle stage (STR-024); the Readiness System holds the readiness verdict (RDY-004, RDY-007). The initial mapping is in the [Readiness System](../systems/readiness-system.md) document. P2§66 allows states to be "refined during architecture".
- **Paper executor.** It belongs to Paper Trading. The execution interface belongs to the Execution Engine (PAP-006).
- **Documentation tooling** is kept in the repository ([DEC-025](DEC-025-documentation-tooling-in-repository.md)).

## Decision 5 — Earlier decisions re-checked against Part 2

| Decision | Result |
|---|---|
| DEC-006 single operator, no custody | Consistent: Part 2 keeps custody a separate, unapproved domain (P2§113, §181) |
| DEC-007 instruments | Consistent: Part 2 does not restrict instruments; funding costs are already in TNP-018 |
| DEC-008 venues | Consistent: P2§44 names three of the five venues and allows others through the same abstraction |
| DEC-009 technology stack | Consistent: P2§146 says the deployment technology "is an architecture decision" and should not be "assumed prematurely". DEC-009 is that decision, made deliberately under the owner's delegation. Docker Compose on one host supports local or server hosting (MIG-001) |
| DEC-010 pre-trade flow | Consistent: Part 2's flows put risk before capital. In DEC-010 the Risk Engine authorizes before any reservation, and Part 2 lists conceptual stages, not every control |
| DEC-011 ownership | Extended by DUP-24 to DUP-30 above; no ownership moved silently |
| DEC-012, DEC-019, DEC-021 safety | Consistent: Part 2's kill-switch scopes, NO NEW POSITIONS, and Safe Mode triggers add to RSK-008 and RSK-015 (RSK-028 to RSK-030) |
| DEC-013 AI organization | Confirmed (DUP-23) |
| DEC-014 net profit | Consistent: P2§29 and §345 |
| DEC-015 modes, policy governance | Consistent: P2§105 policy simulation is a capability for every material change. POL-006 still makes it mandatory before loosening; POL-007 still lets tightening activate at once. Environments: CF-15 |
| DEC-016 stage placement | Changed for the Performance Controller only (CF-16) |
| DEC-017 reporting | Extended by the Daily System Intelligence Dashboard (DUP-30) |
| DEC-018 directional candidates | Consistent |
| DEC-020 values | Applied: new values V-30 to V-33; Part 2's "1% per trade" and similar examples are not operating values |
| DEC-022 restart recovery | Consistent: P2§83 and §86 match REC-014 and REC-015. The lease's limit across hosts is TC-07 |
| DEC-023 autonomous approval | Consistent: P2§111 and §163 are met because the approving component is deterministic, not AI, and live trading needs the operator to raise the platform's maximum mode (MODE-003, POL-005). Only the engine's registration changes (DUP-24) |
| RSK-004 (§26) authority hierarchy | **Conflicts with P2§101 / §279 → CF-14, OPEN.** RSK-004 stays in force |

## Left for the owner

| Item | Question |
|---|---|
| CF-14 | Does system safety or the user's hard policy sit at the top? Recommendation: system safety is a floor no policy can lower; user hard policy outranks everything else |
| OQ-24 | What is the "global platform controller"? Recommendation: the Policy System, the Risk Engine's emergency controller, and System Health together; no new system |
| OQ-25 | Where do PAPER-mode strategies run? Recommendation: the paper environment |
| OQ-26 | What is "adaptive execution"? |
| TC-07 | How is split-brain prevented across two hosts with separate databases? Decide before migration is planned |
| CAP-028, OPS-009, ARCH-034, REC-021 | Confirm, or leave as they are: extra capital categories, infrastructure as code, domain command language, high availability |

## Consequences

- There are 194 new requirements: 185 cite a Part 2 section and 9 cite this record (AIL-009, OPP-016, QNT-007, MKD-011, RDY-006, RDY-007, DSI-006, INC-003, OPS-013). No existing requirement's text or class changed, and none was deprecated. Stale notes were corrected:
  - the Risk Engine's boundary pointed to replaced health rules (now HLT-011, HLT-012);
  - PAP-003, CAP-021, and RSK-010 cite replaced requirements (STR-011, PERF-007, SEC-003) and now have notes naming their replacements;
  - statements that something was "expected from Part 2" were updated in System Health, Deployment and Operational Readiness, the architecture overview, and the open-question register.
- Some earlier records say something is "expected in Part 2": DEC-002 (splitting documents), DEC-010 and DEC-011 (interface contracts), and DEC-014 (slippage and impact methods). Part 2 did not supply these. They now come when the relevant stage is planned (ARCH-025, ARCH-030).
- Implementation is still not authorized (P2§330).
