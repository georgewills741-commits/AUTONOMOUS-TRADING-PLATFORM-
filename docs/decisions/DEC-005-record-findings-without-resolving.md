# DEC-005 — Record conflicts and duplicate responsibilities without resolving them in the specifications

- **Status:** PROPOSED (in effect provisionally)
- **Date:** 2026-09-30
- **Affects:** every specification; [findings register](../conflicts/register.md); [open-question register](../open-questions/register.md)

## Context

Part 1 contains overlapping responsibilities (e.g. four places that compute net profit), and a few inconsistencies (e.g. whether capital or risk is checked first). The handoff requires these to be identified (§00 items 14–16), and forbids silently converting proposals into requirements or removing requirements (§00 items 18–19). The constitution forbids silent requirement or architecture changes (Rules 56–58).

## Decision

- Specifications keep every Part 1 requirement **as stated**, even where it overlaps another system.
- Each overlap or conflict gets an entry in the findings register, cross-referenced from every affected specification.
- The builder's preferred resolution is written in the register as **RECOMMENDED — NOT YET APPROVED**.
- A resolution is applied to the specifications only after the project owner accepts it. That acceptance is recorded as a new decision record.

## Consequences

- Specifications contain known overlaps until they are resolved. Anyone reading a specification sees the finding IDs next to the affected text.
- Implementation of any system with an OPEN finding that blocks it (the "Blocks" column in the open-question register, or a high-impact CF) must wait for resolution (constitution Rules 34, 81, 193).
