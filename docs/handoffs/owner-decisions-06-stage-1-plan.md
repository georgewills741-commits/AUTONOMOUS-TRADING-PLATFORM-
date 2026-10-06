# Owner Decisions 6 — Stage 1 plan and Stage 1 authorization

> **Status:** HISTORICAL — source input: the owner's answers of 2026-10-05 to the two decisions the final decision, knowledge-base, consistency, and repository checkpoint found to require the owner ([record](../traceability/final-decision-checkpoint-2026-10-05.md)): approval of the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md)'s decisions D1 to D11, and authorization of Stage 1 implementation. This is **not** an active source of truth. The answers are applied through [DEC-038](../decisions/DEC-038-stage-1-plan-approved.md).
>
> **Formatting note:** the decision batch shown to the owner before the questions is reproduced first, inside a text block exactly as shown. The questions were then asked in one round of multiple choice; each is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the option the owner chose. The owner added no written notes. Nothing was added, removed, or changed in what was shown or answered; the headings and the bold field names are the builder's.

## The decision batch as shown

```text
**DECISION REQUIRED #1 — the Stage 1 plan's eleven choices (D1–D11)**

- **Issue:** The Stage 1 plan (`docs/roadmap/stage-01-foundation-plan.md`) is still only a proposal. It contains eleven choices that no existing requirement or decision settles. Each is marked as recommended but not yet approved.
- **Why it matters:** These choices set the conventions every later stage builds on: names, file locations, tools, how money amounts and interfaces work, and which libraries are added. The project's rule is that any new library needs a decision record.
- **Existing material:**
  - Technology stack: TEC-001, TEC-003, TEC-004, TEC-009 and DEC-009.
  - Feature statuses: GOV-009 and GOV-024, plus your CF-19 decision, which left "where feature statuses are kept" to Stage 1 planning.
  - No second registry: DUP-32 and GOV-014.
  - Interface versioning: ARCH-026 and GOV-006.
- **The choices:**

| # | Choice | Recommendation | Alternative |
|---|---|---|---|
| D1 | Package and command name | `atp` | A longer name |
| D2 | New file locations | `src/`, `tests/`, `contracts/`, `config/examples/`, and named documents | Keep schemas and examples inside the package |
| D3 | Build tool | `uv_build` (same tool family as uv) | `hatchling` |
| D4 | Automatic checks on GitHub | Yes: read-only, no secrets, deploys nothing | Checks only run by me before each commit |
| D5 | Where each feature's lifecycle status is kept | One table in the roadmap | A separate feature registry |
| D6 | How the two status vocabularies relate | "Active" means approved through production. This also settles that part of TC-10 | Keep them unrelated |
| D7 | Money-amount rules | One constructor, no floating point, rounding only when explicitly asked | Python's defaults plus code review |
| D8 | Interface conventions | Strict and versioned, with errors that never show secrets | Looser validation |
| D9 | Configuration format | TOML; secrets only from the environment | YAML or JSON |
| D10 | Linking requirements to code and tests | Generated automatically | A hand-written table |
| D11 | Libraries added | Pydantic, pytest, Hypothesis, ruff, mypy, the build tool, two GitHub actions | — |

- **Options:** (a) approve all eleven as recommended; (b) approve with changes, naming which choice to change and to what; (c) not yet.
- **Consequences:**
  - (a) I record your approval in a decision record (DEC-038) and the plan becomes approved.
  - (b) I revise the plan, re-verify it, and bring it back to you.
  - (c) Nothing changes and the project waits.
- **My recommendation:** (a). The plan passed its final independent review, and every technical claim in it was tested.
- **What I need from you:** approve D1–D11 as written, or tell me what to change.

**DECISION REQUIRED #2 — permission to start building Stage 1**

- **Issue:** The project's rules (constitution Rules 134–135) require your explicit go-ahead before any code is written. A general "okay" does not count.
- **Why it matters:** This would put the first platform code in the repository. Stage 1 still adds no trading, no exchange connection and no credentials.
- **Options:**
  - (a) "Begin Stage 1": I record it and start the plan's first checkpoint, the development setup and automatic checks.
  - (b) Approve the plan, but don't start yet.
  - (c) Not yet.
- **My recommendation:** (a), if you approve #1.
- **What I need from you:** say "Begin Stage 1", or tell me to wait.

**Everything else needs no decision from you:**
- **Already decided by you:** every other decision the repository records matches your recorded answers. I re-checked them against your actual answers in this session's history.
- **Open on purpose:** TC-09 (standby trading keys) and TC-10 (shared state names) are scheduled for when their stages are planned.
- **Settings to be filled in later:** the unset policy values. An unset value means that autonomous action does not run.
- **Already decided as future or ideas:** the future and proposed items (custody, adaptive execution, the command-language idea).
- **Records fixed in this audit:** your first-round answers had never been saved word for word. Three decision records had also quoted them with small edits, one dropping your "and many more" on venues. I'm saving the exact answers and annotating those records; the meaning of every decision is unchanged.
```

## Round 1

### Q1 — D1 to D11

**Label shown:** D1–D11

**Question as asked:** DECISION REQUIRED #1 — Do you approve the Stage 1 plan's eleven choices D1–D11 as recommended (package name atp; file locations; uv_build; GitHub checks; feature statuses in one roadmap table; 'active' = approved through production; money-amount rules; interface conventions; TOML configuration; generated requirement-to-test table; the listed libraries)?

**Options shown:**

- Approve all as recommended — All eleven choices are approved as written in the plan. They are recorded in a decision record (DEC-038), and the plan's status becomes APPROVED.
- Not yet — You want to read the plan first. Nothing changes; the plan stays PROPOSED. (To change specific choices, use the free-text answer and name each D-item and what it should be.)

**Owner's answer:** Approve all as recommended

### Q2 — Stage 1 implementation

**Label shown:** Begin?

**Question as asked:** DECISION REQUIRED #2 — Do you authorize Stage 1 implementation now ('Begin Stage 1')? Stage 1 builds only foundations: no trading, no exchange connection, no credentials.

**Options shown:**

- Begin Stage 1 — Implementation is authorized. After this checkpoint is committed, the builder creates the stage record and starts checkpoint A (development environment and automatic checks), each checkpoint through the three gates.
- Approve, start later — The plan is approved (if you approved D1–D11), but no code is written until you say 'Begin Stage 1' in a later message.
- Not yet — No authorization. The project stays at the end of planning.

**Owner's answer:** Begin Stage 1
