# DEC-005 — Record conflicts and duplicate responsibilities without resolving them in the specifications

- **Status:** ACCEPTED (delegated, 2026-09-30: accepted under the owner's instruction to resolve all open items; first recorded as PROPOSED)
- **Date:** 2026-09-30
- **Affects:** every specification; [findings register](../conflicts/register.md); [open-question register](../open-questions/register.md)

## Context

Part 1 contains overlapping responsibilities (e.g. four places that compute net profit), and a few inconsistencies (e.g. whether capital or risk is checked first). The handoff requires these to be identified (§00 items 14–16), and forbids silently converting proposals into requirements or removing requirements (§00 items 18–19). The constitution forbids silent requirement or architecture changes (Rules 56–58).

## Decision

- Specifications keep every Part 1 requirement **as stated**, even where it overlaps another system.
- Each overlap or conflict gets an entry in the findings register, cross-referenced from every affected specification.
- The builder's preferred resolution is written in the register as **RECOMMENDED — NOT YET APPROVED**.
- A resolution is applied to the specifications only after the project owner accepts it. That acceptance is recorded as a new decision record.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **Resolving each overlap or conflict directly in the specifications while organizing them:** ruled out, because it would silently change requirements or architecture (handoff §00 items 18–19; constitution Rules 56–58; Context). The findings were recorded instead, and later resolved by decision records, as the registers show.

## Consequences

- Specifications contain known overlaps until they are resolved. Anyone reading a specification sees the finding IDs next to the affected text.
- Implementation of any system with an OPEN finding that blocks it (the "Blocks" column in the open-question register, or a high-impact CF) must wait for resolution (constitution Rules 34, 81, 193).
- **Applied 2026-09-30:** at the owner's instruction, every finding was resolved through DEC-006 to DEC-018. The resolutions were then applied to the specifications as new requirements under "Decisions applied" headings, with the handoff text kept as written.
