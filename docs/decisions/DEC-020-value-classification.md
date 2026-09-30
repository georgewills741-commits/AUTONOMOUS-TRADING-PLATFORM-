# DEC-020 — Classifying values: defaults, design targets, policy parameters, hard limits, implementation choices

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([OC-1](../handoffs/owner-correction-01-autonomous-operating-defaults.md) item 31)
- **Amends:** [DEC-003](DEC-003-requirement-ids-and-classification.md)

## Context

OC-1 item 31 requires distinguishing:
- confirmed architectural requirement
- default
- design target
- policy-controlled parameter
- implementation choice
- open question
- future capability

Values such as 5%, 14 days, 50 trades, 50 ms, and 500 ms must not silently become permanent hard-coded requirements.

Handoff §96 already defines a closed list of classes for *features*. Most of item 31's categories describe *values*, not features, so they are applied as a second classification rather than by redefining §96.

## Decision

1. **Requirement classes:** §96's ten classes, plus **IMPLEMENTATION CHOICE** for requirements that choose a technology or implementation mechanism rather than a platform behavior. Item 31's other categories map to existing classes: "confirmed architectural requirement" → CONFIRMED ARCHITECTURAL PRINCIPLE / CONFIRMED REQUIREMENT; "open question" → OPEN QUESTION; "future capability" → FUTURE.
2. **Value classes**, recorded in the [values register](../requirements/values-register.md):

   | Class | Meaning |
   |---|---|
   | DEFAULT | Starting value that operators or configuration may change |
   | DESIGN TARGET | Soft target for design and optimization; never a guarantee (PERF-012) |
   | POLICY-CONTROLLED PARAMETER | Set by the operator in the Policy System; versioned and audited |
   | HARD LIMIT | Safety limit whose crossing makes action unsafe. Enforced deterministically; its value is set in policy |
   | IMPLEMENTATION CHOICE | A version or mechanism choice |
   | OBSERVED | Measured by the running platform |

3. **ARCH-018:** every concrete operating value in a requirement is in the values register. None is a permanent hard-coded requirement unless the owner explicitly approves it as one. So far, none has been approved.
4. **Reclassification:** TEC-001 and TEC-004 to TEC-012 change from CONFIRMED ARCHITECTURAL PRINCIPLE / CONFIRMED REQUIREMENT to IMPLEMENTATION CHOICE. TEC-002 (Rust only for measured hot paths) and TEC-003 (exact decimal arithmetic) remain CONSTRAINT: they limit implementation to protect correctness and PERF-006.

## Consequences

The former 5% / 14 days / 50 trades are withdrawn as rules; the corresponding parameters are POLICY-CONTROLLED, with no value adopted. The former 50 ms / 500 ms are DESIGN TARGETS only.
