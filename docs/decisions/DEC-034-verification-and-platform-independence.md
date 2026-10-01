# DEC-034 — Adopt the owner's directive on three-level verification and platform independence

- **Status:** ACCEPTED
- **Date:** 2026-10-01
- **Decided by:** project owner (directive sent on 2026-10-01 with the master execution constitution); the builder's: the split between builder rules and platform requirements, and the placement of the new requirements
- **Text:** [`docs/builder/verification-and-platform-independence-directive.md`](../builder/verification-and-platform-independence-directive.md) (verbatim, ACTIVE; the title is the builder's)

## Context

The directive has two parts. The first ("IMPORTANT: From this point forward …") makes three verification levels mandatory for every stage, feature, module, subsystem, or significant change, and asks for the evidence to be recorded in the repository. The second ("CRITICAL PLATFORM INDEPENDENCE PRINCIPLE" to "FINAL PRINCIPLE") says that Claude Code builds and maintains the platform but is not the platform, that development continues from the existing platform, and that a session ending must never damage the project.

## Decision

1. **The directive is an active builder rule,** loaded in every session by `CLAUDE.md` next to the builder constitution, the checkpoint rule (DEC-032), and the master execution constitution ([DEC-033](DEC-033-adopt-master-execution-constitution.md)). Its three verification levels are part of DEC-033's one three-gate procedure (DUP-39).

2. **Statements about the platform become requirements,** with DEC-034 as their source:

   | Directive section | Requirement | Owning document |
   |---|---|---|
   | Critical platform independence principle | PLT-029 Platform independent of Claude Code | [Platform overview](../product/platform-overview.md) |
   | Continuous engineering model | OPS-021 Continuous engineering lifecycle | [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) |
   | Claude Code as long-term platform engineer; final principle (last paragraph) | GOV-021 Every future change follows the same governance | [Architecture governance](../architecture/architecture-governance.md) |
   | Future development must continue from the existing platform (the inspection list included); future upgrade principle | GOV-022 Future development continues from the existing platform | Architecture governance |
   | The platform must outlive the builder session | GOV-023 Platform knowledge outlives the builder session | Architecture governance |

3. **Statements about Claude's sessions stay builder rules:** session interruption, resumable development, no restart-based knowledge loss, checkpointed development, and the commit and persistence principle. They are applied through the [project state](../project-state.md)'s continuation contract and the checkpoint log. They restate constitution Rules 47 to 53 and 160 and the master execution constitution's §02 to §07 and §85 to §89 (DUP-39).

## Reading notes (builder)

| Phrase | Reading |
|---|---|
| "Claude Code is NOT the platform" (PLT-029) | About Claude Code, the builder. AI models the platform itself calls through its AI gateway (AIL-006) are platform components, provider-agnostic (AIL-007) and with deterministic fallback when unavailable (AIL-011), so they are not excluded |
| "Run builds" (Verification 1) | No build exists before code. Until Stage 1 the tools' checks stand in for it (DEC-033) |
| "Test the completed stage as an actual working system component" (Verification 3) | For documentation checkpoints: the independent review and the tools' failure paths. From Stage 1: end-to-end and failure tests of the platform |
| "Current deployed version where accessible" | Nothing is deployed. The list is the session-start inspection once something is |
| "Modify production directly" (GOV-022) | Already forbidden by OPS-007 and OPS-020; GOV-022 repeats it for user requests |
| GOV-022's subject is Claude Code | It names the builder, as GOV-003 and GOV-005 do. It holds for any engineer who continues the platform (GOV-023) |

## Alternatives considered

- **Keep the whole directive as a builder rule, with no requirements.** Rejected: platform independence, the continuous lifecycle, and the governance of future changes describe the platform, so they need owners in the specifications (constitution Rule 24).
- **Fold PLT-029 into OPS-017 ("rebuild without the owner").** Rejected: OPS-017 is about rebuilding infrastructure without the owner; PLT-029 is about operating without the builder. They are related, not the same.
- **Make GOV-022 part of GOV-002.** Rejected: GOV-002 is Part 3's text and stays unchanged. GOV-022 adds the "upgrade, never rebuild" rule and refers to GOV-002's gate.

## Consequences

- Five new requirements: PLT-029, OPS-021, GOV-021, GOV-022, GOV-023. No existing requirement changes.
- Every checkpoint records its three gate results in the repository ([traceability README](../traceability/README.md)).
- Nothing here authorizes implementation.
