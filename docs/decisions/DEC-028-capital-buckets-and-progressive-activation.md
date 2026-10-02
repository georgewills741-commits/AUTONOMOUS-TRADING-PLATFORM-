# DEC-028 — Capital buckets, automatic rebalancing, and progressive capability activation

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 3, Q6](../handoffs/owner-decisions-03-part-2-findings.md)); the placement notes below are the builder's
- **Resolves:** CAP-028 (previously discussed, requiring confirmation)
- **Supersedes:** CAP-028, now DEPRECATED / REPLACED by CAP-029 to CAP-033

## Decision

| Requirement | What it says |
|---|---|
| CAP-029 | Three more capital buckets: directional trading capital, an emergency reserve, and a per-exchange reserve. They are policy-set, not fixed hard-coded amounts |
| CAP-030 | Bucket sizes scale dynamically with total available capital, risk exposure, liquidity, exchange requirements, active strategies, withdrawal/transfer constraints, and system health |
| CAP-031 | Buckets are rebalanced automatically when conditions justify it, without the owner online or approving routine movements. Every transfer stays within the hard safety, risk, liquidity, and authorization policies |
| CAP-032 | Progressive capability activation: small accounts operate safely within their capital and do not activate capital-intensive features prematurely. As capital grows and the system proves capacity and safety, more capabilities may become eligible automatically |
| CAP-033 | No capital movement may violate the safety floor, the emergency reserve, the exchange-specific reserves, the exposure limits, or the reconciliation requirements |
| RDY-008 | (Builder placement) The Readiness System decides when a capital-intensive capability becomes eligible, using the Global Capital Authority's figures and its own evidence |

## Placement and terminology (builder)

- **"Capital Allocation & Treasury Engine"** is the owner's name for the Global Capital Authority (SYS-07). There is one capital authority (ARCH-027), and it already owns allocation, reserves, and rebalancing decisions (CAP-017, CAP-018, CAP-023). The name is recorded as an alias in the [glossary](../glossary.md). No new system is created.
- **Capability eligibility** is a readiness question: whether something is ready to progress. So its verdict belongs to the Readiness System (RDY-001, RDY-008). Capital figures come from SYS-07.
- **Eligibility is not authorization.** Eligible capabilities still activate only within the operator's authorizations: the platform's maximum mode (MODE-003), enabled instrument types (PLT-012), and the autonomy bounds (POL-011). The platform never invents authorization (PLT-020).

## Carried forward from CAP-028

CAP-002 already holds the available, reserved, arbitrage-allocated, reserve, per-exchange, and per-strategy categories. The arbitrage reserve is ARB-008 and ARB-009. CAP-029 adds the three new buckets, so nothing from CAP-028 is lost.

## How this fits (no conflict)

| Requirement | Relationship |
|---|---|
| CAP-023 to CAP-025 (autonomous, bounded rebalancing) | CAP-031 applies the same model to the new buckets |
| SEC-006, SEC-007 (transfer authority) | Transfers between venues use the restricted transfer credential |
| DEC-006 (no custody, no withdrawals by the platform) | "Withdrawal constraints" means the operator's own withdrawals at venues, which the ledger detects (LED-005). The platform still withdraws nothing |
| RSK-034 to RSK-036 (safety floor, adaptive operation) | Bucket sizing is adaptive operation inside the envelope. CAP-033 restates the floor for capital |

The sizing rules and the eligibility thresholds are policy values V-34 and V-35 in the [values register](../requirements/values-register.md).

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **No** (Q6 in [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md): keep the current capital categories): not chosen. The owner's own answer begins with the recommended option ("Yes — policy-set") and goes further: dynamic sizing, automatic rebalancing, and progressive capability activation.
- **Amounts fixed in code:** ruled out by the option shown ("with the amounts set in your policy rather than fixed in code") and by the owner's answer ("not fixed hard-coded amounts"; CAP-029).
- **A new system for the "Capital Allocation & Treasury Engine"** the owner named: not created. It is the owner's name for the Global Capital Authority, the one capital authority (ARCH-027; "Placement and terminology" above).
