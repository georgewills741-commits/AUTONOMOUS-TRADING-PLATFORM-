# DEC-003 — Requirement IDs, classification rules, and spec-embedded requirements

- **Status:** PROPOSED (in effect provisionally)
- **Date:** 2026-09-30
- **Affects:** every specification; `docs/requirements/`
- **Resolves (provisionally):** CF-10 · **Raises:** OQ-23

## Context

The handoff requires every feature to be classified with its §96 vocabulary, requirements to be registered, and no duplicate sources of truth. The constitution has its own type and status vocabularies (Rules 20, 181).

## Decision

1. **Requirement text lives in exactly one place: the owning specification.** Each requirement is one line: `- **ID** Title · CLASS · §source — text`. The [registry](../requirements/registry.md) is an index (ID, title, class, source, owner, document, stage) and never restates the text.
2. **IDs** are `PREFIX-NNN`. The prefix names the owning system or cross-cutting set ([system registry](../architecture/system-registry.md)). IDs are never reused or renumbered.
3. **Classes** use handoff §96 exactly. How they were applied to Part 1:
   - **CONFIRMED REQUIREMENT:** a required capability or behavior stated by the handoff.
   - **CONFIRMED ARCHITECTURAL PRINCIPLE:** a rule about structure, ownership, separation, or flow.
   - **CONSTRAINT:** a prohibition or limit ("must not", "never", "cannot", "only").
   - **SYSTEM REQUIREMENT:** the responsibilities or capabilities of one named system, usually a list.
   - **PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION:** anything the handoff labels as previously discussed (custody §84, venue examples §42, agent roster §54).
   - **PROPOSED:** anything the handoff labels as potential (ledger scope §85).
   - **OPEN QUESTION** and **TECHNICAL CONCERN** are kept in the [open-question register](../open-questions/register.md) (OQ-, TC-), not as requirement lines.
   - FUTURE and DEPRECATED / REPLACED: nothing in Part 1 uses them.
4. **Wording keeps the handoff's strength.** "Must", "should", and "may" are kept as written. Lists introduced by "may include", "possible", or "examples" keep that hedge and are indicative, not final. Classification never upgrades a "should" or a "may".
5. **Constitution vocabularies** are used for status and findings (e.g. VERIFIED, INFERRED, RECOMMENDED — NOT YET APPROVED), not for requirement classes.
6. **Requirement status** is DOCUMENTED for everything in Part 1: recorded, not implemented, not verified.

## Alternatives considered

- **Full requirement text in both the specification and the registry:** rejected. It creates two sources of truth.
- **One ID per bullet item:** rejected. It would produce roughly 700 IDs without adding meaning; each list stays whole inside one requirement.

## Consequences

- The handoff does not define the difference between CONFIRMED REQUIREMENT and SYSTEM REQUIREMENT. The interpretation above needs owner confirmation (OQ-23). If it changes, classes are updated with a record here, not silently (§96).
- A consistency check (every ID unique, in exactly one specification, and indexed in the registry) was run as part of verification. See the [Part 1 verification record](../traceability/part-1-verification.md).
