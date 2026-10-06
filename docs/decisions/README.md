# Decision Log

Significant decisions are recorded here as individual records (constitution Rules 49, 142, 176; handoff §98 "Architecture Decisions → docs/decisions/").

**Statuses:**
- **ACCEPTED:** in effect. **ACCEPTED (delegated)** means the builder decided under an explicit owner instruction; the owner may override it with a new record.
- **SUPERSEDED:** links to the replacement.
- **REJECTED.**

Records are never deleted. A changed decision gets a new record that supersedes the old one.

On 2026-09-30 the owner instructed the builder to resolve every unresolved item before Handoff Part 2. Four questions went to the owner directly: custody, instruments, venues, and technology stack. The owner delegated the stack choice back to the builder. Everything else was decided under that instruction. The owner then replaced five operating defaults with the company-grade autonomous model (DEC-019, DEC-020), and decided the three conflicts it raised (DEC-021 to DEC-023).

| ID | Decision | Decided by | Status |
|---|---|---|---|
| [DEC-001](DEC-001-adopt-builder-constitution.md) | Adopt the builder constitution; keep it in `docs/builder/`; load it in every session via `CLAUDE.md` | Builder | ACCEPTED (delegated) |
| [DEC-002](DEC-002-documentation-structure.md) | Documentation structure derived from Handoff Part 1 | Builder | ACCEPTED (delegated) |
| [DEC-003](DEC-003-requirement-ids-and-classification.md) | Requirement IDs, classification rules, spec-embedded requirements with an index registry | Builder | ACCEPTED (delegated); amended by DEC-020 |
| [DEC-004](DEC-004-preserve-original-handoffs.md) | Keep each received handoff verbatim as a HISTORICAL record | Builder | ACCEPTED (delegated) |
| [DEC-005](DEC-005-record-findings-without-resolving.md) | Record findings without resolving them in specifications, until the owner decides | Builder | ACCEPTED (delegated); applied through DEC-006 to DEC-018 |
| [DEC-006](DEC-006-single-operator-and-trading-ledger.md) | Single-operator platform, no custody, internal trading ledger | Owner (model); builder (ledger) | ACCEPTED |
| [DEC-007](DEC-007-instrument-scope.md) | Spot, perpetual futures, and margin, each gated by its risk controls | Owner | ACCEPTED |
| [DEC-008](DEC-008-venues-and-trading-universe.md) | Binance, OKX, Coinbase, Bybit, KuCoin, extensible; trading universe; adapter requirements | Owner (venues); builder (rest) | ACCEPTED |
| [DEC-009](DEC-009-technology-stack.md) | Technology stack, storage, retention, deployment | Builder, by explicit owner delegation | ACCEPTED (delegated) |
| [DEC-010](DEC-010-pre-trade-decision-flow.md) | Canonical pre-trade decision flow | Builder | ACCEPTED (delegated); REC-007 superseded by DEC-022 |
| [DEC-011](DEC-011-ownership-of-shared-responsibilities.md) | Ownership of overlapping responsibilities | Builder | ACCEPTED (delegated) |
| [DEC-012](DEC-012-safety-architecture.md) | Safety architecture: kill switches, health state machine, system safety rules | Builder | ACCEPTED (delegated); partly superseded by DEC-019 |
| [DEC-013](DEC-013-ai-organization.md) | AI organization: five agents, deterministic model services, AI gateway, output contract, validation | Builder | ACCEPTED (delegated) |
| [DEC-014](DEC-014-net-profit-formula-and-uncertainty-margin.md) | True net-profit formula and uncertainty margin | Builder | ACCEPTED (delegated) |
| [DEC-015](DEC-015-modes-canary-and-policy-governance.md) | Operating modes, canary, policy governance | Builder | ACCEPTED (delegated); canary and MODE-004 superseded by DEC-019 |
| [DEC-016](DEC-016-roadmap-stage-placement.md) | Roadmap stage sequence and placement | Builder | ACCEPTED (delegated); Performance Controller stage changed by DEC-024 |
| [DEC-017](DEC-017-reporting-alerting-and-performance-targets.md) | Reporting, alerting, logging, initial performance targets | Builder | ACCEPTED (delegated); performance targets superseded by DEC-019 |
| [DEC-018](DEC-018-initial-directional-research-candidates.md) | Initial directional research candidates | Builder | ACCEPTED (delegated) |
| [DEC-019](DEC-019-company-grade-autonomous-operating-model.md) | Company-grade autonomous operating model (rebalancing, safety levels, 24/7 recovery, canary, performance) | Owner ([OC-1](../handoffs/owner-correction-01-autonomous-operating-defaults.md)) | ACCEPTED; its CF-11 to CF-13 decided in DEC-021 to DEC-023 |
| [DEC-020](DEC-020-value-classification.md) | Value classification and the values register | Owner (OC-1 item 31) | ACCEPTED |
| [DEC-021](DEC-021-kill-switch-recovery.md) | Cause-based, risk-aware kill-switch recovery with escalation | Owner ([owner decisions 2](../handoffs/owner-decisions-02-cf-11-to-cf-13.md)) | ACCEPTED |
| [DEC-022](DEC-022-restart-recovery-sequence.md) | Staged restart recovery; persisted state untrusted until reconciled | Owner (owner decisions 2) | ACCEPTED |
| [DEC-023](DEC-023-autonomous-canary-approval.md) | Policy-driven autonomous approval by the Governance and Readiness Engine | Owner (owner decisions 2) | ACCEPTED; the engine's registration as SYS-34 by DEC-024 |
| [DEC-024](DEC-024-part-2-reconciliation.md) | Reconciliation of Handoff Part 2: classification, one owner per duplicated responsibility, CF-15, CF-16, re-check of DEC-006 to DEC-023 | Builder; confirmed by the owner (owner decisions 3) | ACCEPTED |
| [DEC-025](DEC-025-documentation-tooling-in-repository.md) | Keep the documentation generator and checker in the repository | Builder | ACCEPTED (delegated) |
| [DEC-026](DEC-026-safety-floor-and-layered-control.md) | Safety floor and layered control model (CF-14) | Owner ([owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md)) | ACCEPTED |
| [DEC-027](DEC-027-part-2-open-questions.md) | Global platform controller, paper environment, adaptive execution (FUTURE), command language kept as idea, DEC-024 confirmed | Owner (owner decisions 3) | ACCEPTED |
| [DEC-028](DEC-028-capital-buckets-and-progressive-activation.md) | Capital buckets, automatic rebalancing, progressive capability activation | Owner (owner decisions 3); builder (placement) | ACCEPTED |
| [DEC-029](DEC-029-infrastructure-as-code.md) | Infrastructure as code is a mandatory production requirement | Owner (owner decisions 3) | ACCEPTED |
| [DEC-030](DEC-030-high-availability-and-single-active-copy.md) | High availability approved; only one active copy during migration (TC-07) | Owner (owner decisions 3); builder (lease authority, key-revocation order) | ACCEPTED |
| [DEC-031](DEC-031-part-3-reconciliation.md) | Reconciliation of Handoff Part 3: classification, document homes, one owner per duplicated responsibility (DUP-32 to DUP-38), CF-17 and CF-18, re-check of DEC-006 to DEC-030 | Builder; confirmed by the owner (DEC-035) | ACCEPTED; CF-17 changed and TC-08 decided by the owner (DEC-035) |
| [DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md) | Adopt the owner's checkpoint, version-control, and three-stage verification rule | Owner (rule sent with Handoff Part 3) | ACCEPTED |
| [DEC-033](DEC-033-adopt-master-execution-constitution.md) | Adopt the master execution, consistency, verification and continuity constitution; one three-gate procedure for the four builder texts (DUP-39); ARCH-041, ARCH-042, PERF-023; CF-19, TC-10 | Owner (constitution sent on 2026-10-01); builder (how the texts combine, placement) | ACCEPTED; CF-19 decided by the owner (DEC-035) |
| [DEC-034](DEC-034-verification-and-platform-independence.md) | Adopt the owner's directive on three-level verification and platform independence; PLT-029, OPS-021, GOV-021 to GOV-023 | Owner (directive sent on 2026-10-01); builder (placement) | ACCEPTED |
| [DEC-035](DEC-035-owner-decisions-part-3-findings.md) | Owner decisions on the Part 3 findings: security above the user's hard policy (RSK-049), CF-18 confirmed, the constitution's feature lifecycle (GOV-024), no Part 4, older records' alternatives added now, DUP-34 and DUP-35 confirmed; Part 3 reconciliation approved | Owner ([owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md)) | ACCEPTED |
| [DEC-036](DEC-036-owner-decisions-audit-findings.md) | Owner decisions on the master knowledge-base audit's findings: production never depends on one machine (MIG-033), instrument scope confirmed (PLT-011), PLT-010 matched to DEC-006, retention values only in TEC-012, feature process confirmed; documentation review accepted; Stage 1 planning authorized | Owner ([owner decisions 5](../handoffs/owner-decisions-05-audit-findings.md)) | ACCEPTED |
| [DEC-037](DEC-037-final-decision-and-integrity-checkpoint.md) | Final decision and integrity checkpoint: the owner's first-round instruction and answers, and the options shown with CF-11 to CF-13, preserved verbatim; the quotations in DEC-006 to DEC-009 annotated, not rewritten | Builder (at the owner's request) | ACCEPTED |
| [DEC-038](DEC-038-stage-1-plan-approved.md) | Stage 1 plan approved with D1 to D11 as recommended; Stage 1 implementation authorized | Owner ([owner decisions 6](../handoffs/owner-decisions-06-stage-1-plan.md)) | ACCEPTED |

Handoff Part 2 arrived on 2026-09-30. It came with no instruction to resolve everything. DEC-024 therefore resolves only placement, duplication, and terminology, which reconciliation requires (Part 2 §182). The questions that change meaning went to the owner, who answered them the same day (DEC-026 to DEC-030). Handoff Part 3 arrived the same day with the owner's checkpoint and verification rule (DEC-032). DEC-031 reconciles Part 3 the same way DEC-024 reconciled Part 2 and leaves CF-17, CF-18, OQ-27, TC-08, and the DUP-34 and DUP-35 readings for the owner; TC-09 is recorded now and decided when OPERATIONALIZATION is planned. On 2026-10-01 the owner sent the master execution constitution and a directive on verification and platform independence, adopted by DEC-033 and DEC-034. On 2026-10-02 the owner answered every open item and approved the Part 3 reconciliation (DEC-035). Following the owner's decision on TC-08, the same day every record from DEC-001 to DEC-030 that lacked one got an "Alternatives considered" section, built only from what the repository records; no decision changed. On 2026-10-03, after the complete documentation review (the master knowledge-base audit), the owner decided its four open findings, accepted the review, and authorized Stage 1 planning (DEC-036). On 2026-10-05 the owner's final decision checkpoint preserved the first-round answers verbatim (DEC-037), and the owner approved the Stage 1 plan and authorized Stage 1 implementation (DEC-038).

**Decided does not mean authorized:** only DEC-038 authorizes implementation, and only of Stage 1. Every later stage needs its own plan and the owner's explicit approval (handoff §101; Part 2 §329–§330; constitution Rules 134–136).
