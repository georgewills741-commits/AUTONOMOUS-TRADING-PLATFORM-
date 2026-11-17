# Owner Decisions 38 — One reusable temporary backup branch, approved on 2026-11-16 with twelve mandatory conditions

> **Status:** HISTORICAL — source input: three messages of the owner of 2026-11-16 on the builder's proposal of 19:10 UTC to keep one reusable temporary backup branch instead of a new one for each change: at 19:15 UTC, a question on what the proposal is; at 19:21 UTC, the answer to the builder's question of 19:15 UTC, approving it; and at 19:21 UTC, a message delivered while the builder worked, which approves it with twelve mandatory conditions: one reusable branch for sequential changes, only if it preserves every required recovery history; nothing important overwritten, forced away, deleted, reset, or made unreachable; recoverable history and exact checkpoint SHAs, with append-only, fast-forward updates; the previous change's work preserved, reconciled, and traceable before reuse; the eight reconciliation checks and the three gates kept; the secret test before each backup push; an isolated mechanism where work overlaps; no archive branch, deletion attempt, or retirement report for each change where the reusable branch protects as well; the historical branches and archives kept; the canonical rules updated, with no competing system; recovery verified after a container reset, an interruption, or months of inactivity; and the existing process kept until a verified replacement exists. The builder answered at 19:15, 19:21, and 19:22 UTC. This is **not** an active source of truth. It is preserved by [DEC-071](../decisions/DEC-071-one-reusable-backup-branch.md), which applies the approval under its conditions.
>
> **Formatting note:** the question is recorded as [owner decisions 34](owner-decisions-34-approval-to-plan-stage-2-and-answers-on-the-directive.md) records its own: the short label shown above it, the question as asked, the options shown (label, then description), and the owner's answer, in a text block; each message is reproduced inside its own text block exactly as received. Nothing was added, removed, or changed in them. The title, this banner, and the headings are the builder's.

## 2026-11-16, 19:15 UTC

```text
what is proposal that needs my yes or no
```

## The question of 2026-11-16, 19:15 UTC, and the answer of 19:21 UTC

### Q1 — one reusable backup branch

**Label shown:** Backups

**Question as asked:** Should future changes use one reusable temporary backup branch instead of a new backup branch per change? (Today each change gets its own branch, which GitHub won't let me delete afterwards: 15 dead branches plus 15 archive copies so far, and every change spends an archive copy, a refused deletion, 10 retirement checks, and a report on it. With one reusable branch, work is still backed up at once and checked after each commit; only that per-branch cleanup goes away. The three verification gates don't change.)

**Options shown:**

- Yes, one reusable branch (Recommended) — From the next change on, all backups go to one branch. Work is still pushed at once, with the secret test and the 8 reconciliation checks. No new dead branches, and no archive, deletion attempt, retirement checks, or report per change.
- No, keep a branch per change — Nothing changes: each change keeps its own backup branch, which is archived, has its deletion tried once, passes 10 retirement checks, and is kept retired until you delete it on GitHub.

**Owner's answer:**

```text
Yes, one reusable branch (Recommended)
```

## 2026-11-16, 19:21 UTC

```text
I approve Yes, one reusable branch (Recommended).
My objective is to reduce unnecessary branches, Claude Code token consumption, cleanup operations, and development delays without sacrificing any company-grade engineering standards.
However, this approval has mandatory safety conditions:

1. Use one reusable temporary backup branch for future sequential development changes, provided it can preserve all required recovery history safely.
2. Never overwrite, force-push away, delete, reset, or make unreachable any important unfinished or unreconciled work.
3. Preserve recoverable commit history and exact checkpoint SHAs. Prefer append-only, fast-forward backup updates where technically practical.
4. Before reusing the branch, verify that all unique work from the previous change is preserved, reconciled with the authoritative verified checkpoint, and traceable.
5. Maintain the existing eight reconciliation checks and all three verification gates. Reuse the same canonical checks without creating duplicate processes.
6. Continue the required secret scanning before backup pushes, and preserve full testing and verification before any work becomes authoritative.
7. If simultaneous or overlapping work makes one reusable branch unsafe, use an appropriately isolated preservation mechanism rather than risking lost work.
8. Do not create new archive branches, repeated deletion attempts, or redundant retirement reports for each change when the reusable-branch mechanism already provides equivalent, verified protection.
9. Preserve the previously approved historical branches and archives according to their existing retention rules. Do not delete or alter them automatically.
10. Update the existing canonical repository and backup rules to reflect this approved improvement. Do not create another competing governance system.
11. Verify that the new backup process can recover unfinished work after a container reset, session interruption, or months of inactivity.
12. If these guarantees cannot be established, retain the existing safe backup process until a verified replacement is available. Do not claim the change is safe without evidence.

The objective is fewer unnecessary operations, lower token consumption, faster meaningful progress, and unchanged or stronger protection against work loss.
Continue from the exact current authorized checkpoint. Do not restart completed work or weaken project quality.
```
