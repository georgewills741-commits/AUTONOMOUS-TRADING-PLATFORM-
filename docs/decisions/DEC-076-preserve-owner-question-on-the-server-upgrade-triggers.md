# DEC-076 — Preserve the owner's question of 2026-11-20, 11:01 UTC, on the server's upgrade triggers (owner decisions 43)

- **Status:** ACCEPTED
- **Date:** 2026-11-20
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept). The message is the owner's.

## Context

On 2026-11-20, during the first increment of Stage 2's checkpoint B, the 5-hour usage limit stopped the session at 05:31 UTC, before that change's Gate 3 run was launched; the limit reset at 09:10 UTC, and the worker's restart at 06:58 UTC met the limit again. At 11:01 UTC the owner asked what the builder meant by its report of 04:22 UTC on the server ([DEC-075](DEC-075-owner-operating-decisions-and-future-membership.md)): its estimate that Hetzner's CPX22 carries the first exchange, and the four signs that would call for the CPX32; and whether the CPX22 is not enough. The client delivered the message as a user turn of its own, of origin human, so it is the owner's message.

The builder answered in the same turn, before going on with the change:

- **What it means:** the CPX22 (2 vCPUs, 4 GB of memory, 80 GB of disk) is expected to be enough for the start: one exchange's public market data for a limited set of markets, with 30 days kept; an estimate, since nothing has run on it yet.
- **The signs:** what is watched once the server runs, any one of them showing that it has become too small: the processor or memory near full, or swapping; 30 days of data not fitting on its disk; storage slowing, failing, or backing up; a collector falling behind its exchange's live data; and a second exchange, or deeper order books, calling for a new measurement (the [Stage 2 record](../traceability/stage-02-data-foundation.md), "Hosting options for Stage 2's live work").
- **Is it enough:** yes, for the start; the CPX32 is the next size, only if a sign appears; nothing is upgraded or bought without the owner's approval; no server is approved yet, and Hetzner showed the CPX22 unavailable to order on 2026-11-19.

## Decision

1. **The message is preserved word for word**, as [owner decisions 43](../handoffs/owner-decisions-43-question-on-the-server-upgrade-triggers.md), a HISTORICAL source listed in the preserved-text manifest. It was taken by script from its user turn of 11:01 UTC in the session record and kept byte for byte, including the spaces that end its first and last lines, so `git diff --check` reports those two lines; the text is not trimmed to satisfy it.
2. **It changes nothing.** It asks a question, which the builder answered; the server's assessment and the signs that would call for an upgrade stay as the Stage 2 record states them, RECOMMENDED and not approved, and no server is approved ([DEC-075](DEC-075-owner-operating-decisions-and-future-membership.md), decision 2). The work goes on in the order of the [project state](../project-state.md)'s "Next approved step".
3. **It is preserved with the change in progress, whose record names it** ([checkpoint B (U5) verification](../traceability/stage-02-checkpoint-b-u5-verification.md)): that change's Gate 3 run reviews a copy made after the message ([traceability README](../traceability/README.md), Scope), as with owner decisions 39 ([DEC-072](DEC-072-preserve-owner-question-on-order-and-cleanliness.md), decision 3).

## Alternatives considered

- **Treat it as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps, as the owner's questions of the same kind were kept (DEC-072 and earlier).
- **Preserve it with the next change.** Not chosen: the Scope rule ties a message to the record whose last Gate 3 run reviews a copy made after it, and that record is this change's.
- **Trim its spaces, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 43 is listed in the preserved-text manifest and the documentation index.
- The record of the change in progress names the message.
- No requirement, rule, gate, decision, or code changes, and no server is approved.
