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
| [DEC-024](DEC-024-part-2-reconciliation.md) | Reconciliation of Handoff Part 2: classification, one owner per duplicated responsibility, CF-15, CF-16, re-check of DEC-006 to DEC-023 | Builder | ACCEPTED (delegated); CF-14, OQ-24 to OQ-26, TC-07 left to the owner |
| [DEC-025](DEC-025-documentation-tooling-in-repository.md) | Keep the documentation generator and checker in the repository | Builder | ACCEPTED (delegated) |

Handoff Part 2 arrived on 2026-09-30. It came with no instruction to resolve everything. DEC-024 therefore resolves only placement, duplication, and terminology, which reconciliation requires (Part 2 §182). The questions that change meaning are left for the owner.

**Decided does not mean authorized:** none of these decisions authorizes implementation. That still needs the owner's answers on the Part 2 findings, the complete documentation review, and explicit approval (handoff §101; Part 2 §329–§330; constitution Rules 134–135).
