# Owner Decisions 20 — A question on the rules, the order of work, and backups

> **Status:** HISTORICAL — source input: the owner's message of 2026-10-20, 22:04 UTC, sent while the seventh Gate 3 run of the change that commits the reports of earlier Gate 3 runs as evidence was running, and the owner's answers to the three questions the builder then asked. The message asks whether the builder has questions and whether it really follows the rules, recalls the owner's instruction to fix problems at their root and avoid loops, and notes that the project has been in Stage 1 since it started and that the owner's weekly usage has reached 69%. The answers: item 3 first, then checkpoints C and D, with items 4 and 5 after checkpoint D and before Stage 1's final exit report, the rules kept intact; option (b) of OQ-31, a temporary backup branch for each long gate cycle, with the builder doing every step; and, since this environment cannot create tags, archive branches instead. This is **not** an active source of truth. It is preserved by [DEC-052](../decisions/DEC-052-apply-owner-answers-on-order-of-work-and-backups.md).
>
> **Formatting note:** the typed message and each answer are reproduced inside text blocks exactly as the session recorded them. The first two answers begin with the option chosen as the session recorded it, the first with its description, the second with its label and description, followed by the owner's own words; the third is the label of the option chosen. The questions and options are the builder's, recorded with the short label shown above each question, the question as asked, and the options shown (label, then description). Nothing was added, removed, or changed in what was written, shown, or answered; the title, this banner, the headings, and the bold field names are the builder's.

## 2026-10-20, 22:04 UTC

```text
do you have any questions to ask me if yes show me if no continue doing what you're doing and also are you really following the rules or what because i think there is a place i said something like fix the problem from the root and correct to avoid always loops because since this project started is been on stage 1 and now my weekly usage limit is up to 69%. continue what you're doing while answering this questions
```

## The builder's questions, asked at 22:12 UTC and answered at 22:26 UTC

### Q1 — the order of work

**Label shown:** Work order

**Question as asked:** Should I reach checkpoint C sooner? Recorded order: item 3 (adopt your drafting rules; ready to apply), item 4 (your opportunity-and-economics audit), item 5 (map your traceability rules to requirements), then checkpoint C (configuration and security foundation) and D. Items 4 and 5 are documentation; they draft requirements for later stages.

**Options shown:**

- Item 3, then C and D (Recommended) — Finish item 3, then go straight to checkpoints C and D. Items 4 and 5 are done after D, before Stage 1's final exit report. This reaches actual Stage 1 work soonest; item 5's configuration and security rules are checked against U4 and U5 during checkpoint C.
- Keep the recorded order — Items 3, 4, and 5, then checkpoints C and D, as the project state records (DEC-046, DEC-048).
- Go to C now — Stop all three governance steps for now (items 3, 4, 5) and start checkpoint C immediately; do them all before Stage 1's exit.

**Owner's answer, as the session recorded it:**

```text
Finish item 3, then go straight to checkpoints C and D. Items 4 and 5 are done after D, before Stage 1's final exit report. This reaches actual Stage 1 work soonest; item 5's configuration and security rules are checked against U4 and U5 during checkpoint C.
hope it doesn't change anything like causing problems and the rules are still there and intact because i dont want error in my company project i hope you understand so always use the rules as always
```

### Q2 — keeping work safe during a long gate cycle (OQ-31)

**Label shown:** Backup

**Question as asked:** OQ-31: how should unfinished work be kept safe while a change waits in its review gates (it is only in this cloud container until the commit)? This must be decided before checkpoint C.

**Options shown:**

- Backup branch, you tag (Recommended) — (b) A temporary backup branch for each long gate cycle, kept until you push its archive tag, then deleted. Commits stay reachable; each branch waits for your tag. This is what you chose for checkpoint B's backup.
- Backup branch, deleted — (a) A temporary backup branch, deleted once its reconciliation with the verified commit passes and is recorded; its commits may become unreachable afterwards.
- Backup branch, kept — (c) A temporary backup branch, kept as it is after the verified commit.
- No backup — (d) No backup: work stays uncommitted during its gates and is named in the project state, at the risk of losing it if the container is reclaimed.

**Owner's answer, as the session recorded it:**

```text
Backup branch, you tag (Recommended)
(b) A temporary backup branch for each long gate cycle, kept until you push its archive tag, then deleted. Commits stay reachable; each branch waits for your tag. This is what you chose for checkpoint B's backup.

but you're the one doing everything not me you're in charge of doing them professionally like a company not me manually doing it.
```

## The builder's question, asked at 22:27 UTC and answered at 22:28 UTC

### Q3 — archive branches instead of tags

**Label shown:** Archive

**Question as asked:** This cloud environment cannot create git tags (GitHub refuses with 403), so I can't make the archive tags myself. May I keep each archived backup as a branch named claude/archive/<name> instead of a tag? The commits stay kept and findable, I do every step, and nothing is manual for you. This would also finish retiring checkpoint B's old backup (item 1), which is blocked only on that tag.

**Options shown:**

- Yes, archive branches (Recommended) — I create claude/archive/<name> at the backup's last commit, verify it, then delete the temporary backup branch, all by myself. Applies to checkpoint B's backup now and to every future backup.
- No, keep tags — Keep the archive-tag rule. Backups stay as they are until tags become possible from this environment (you would not need to push them yourself; they simply wait).

**Owner's answer, as the session recorded it:**

```text
Yes, archive branches (Recommended)
```
