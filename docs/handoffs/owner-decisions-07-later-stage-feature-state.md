# Owner Decisions 7 — The state of the later stages' features

> **Status:** HISTORICAL — source input: the owner's answer of 2026-10-07 to OQ-29, the one question the [quality audit](../traceability/quality-audit-2026-10-06.md) found to require the owner (its Q-07): which GOV-024 state the features of stages 2 to 7 have before their stages are planned. This is **not** an active source of truth. The answer is applied through [DEC-040](../decisions/DEC-040-later-stage-features-proposed.md).
>
> **Formatting note:** the message shown to the owner before the question is reproduced first, inside a text block exactly as shown. The question was then asked as one multiple choice; it is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the option the owner chose. The owner added no written note. Nothing was added, removed, or changed in what was shown or answered; the headings and the bold field names are the builder's.

## The message as shown

```text
The machine checks passed on GitHub for `a6cca83`, all 12 steps. Your directive is now part of the project's rules, and the audit it asked for is done and committed.

**What the audit found and fixed:**
- **One status overstated progress.** The testing foundation was marked as being verified, but one of its parts, the configuration for property-based tests, still comes at checkpoint B. It now says "being built".
- **One document had two names.** It's now called the "developer guide" everywhere, matching the plan you approved.
- **Smaller fixes:**
  - outdated statements about the verification steps were corrected;
  - your 5 October request is now quoted word for word in its record;
  - status labels, glossary and the handover notes for future sessions were completed.
- No requirement changed, and no code or settings changed.

**How it was checked:** my own checks all pass, also on a fresh copy of the repository. Four independent reviews were needed before the third verification step passed. Every blocking problem they found was in how I worded the question below, and all are fixed.

**Still open, not blocking:**
- three small items already scheduled for checkpoint B;
- gaps in the secret-detection test, scheduled for checkpoint C;
- two missing automatic checks for the documentation tools, proposed for their next update.

**The one decision I need from you:**
- **Background:** from checkpoint A, the roadmap showed every feature of stages 2 to 7 as "APPROVED". That was my reading of your acceptance of the documentation review, not something you decided. Until you answer, those rows show "REQUIRES OWNER DECISION".
- **What it does not do:** neither answer authorizes building anything. Each later stage still needs its own plan and your approval.
- **What it covers:** those features include 65 requirements I decided under your delegation. You can still override them either way.

My recommendation is APPROVED. In the project's feature lifecycle, "approved" comes before design, while permission to build comes later with each stage's plan. Checkpoint B is already authorized and doesn't depend on this answer, so I'll start it unless you tell me to wait.

The full question, with the arguments for each side, is in `docs/traceability/quality-audit-2026-10-06.md`.
```

## Round 1

### Q1 — the state of the later stages' features

**Label shown:** Later stages

**Question as asked:** Stages 2 to 7 are not planned yet. What status should their features have in the roadmap now? (Neither answer authorizes building them; checkpoint B goes ahead meanwhile unless you tell me to wait.)

**Options shown:**

- APPROVED (Recommended) — Accepted scope now. Each feature is still designed, approved for building, and authorized only when its stage's plan is approved. Includes the 65 items I decided under your delegation, which you can still override.
- PROPOSED until each plan — Features stay PROPOSED and become APPROVED stage by stage, when you approve that stage's plan. PROPOSED is also the word for unapproved ideas, so some roadmap wording would be adjusted.

**Owner's answer:** PROPOSED until each plan
