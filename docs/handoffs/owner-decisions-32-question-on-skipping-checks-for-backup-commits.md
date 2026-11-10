# Owner Decisions 32 — A question of 2026-11-09 on whether keeping temporary backup commits out of the machine checks could cause problems

> **Status:** HISTORICAL — source input: a message of the owner of 2026-11-09, 15:00 UTC, sent during the second Gate 3 run of the change that writes Stage 1's completion certificate. It quotes the builder's summary of its choice on the emails of failed machine checks, `[skip ci]` in each temporary backup commit and, after Stage 1's exit, the workflow's own rule ([DEC-064](../decisions/DEC-064-retired-branches-kept-and-backup-commits-skip-checks.md)), and hopes that it will not create problems in the future. The builder answered at 15:01 UTC: no. The marker only stops GitHub's run for a backup snapshot, which is still pushed at once; every real commit runs every check, and the marker is never in one; backups are never evidence. What would have to go wrong is named with its guard: the marker reaching a real commit, which cannot happen by accident, since real commits are written fresh, and the builder confirms on GitHub that the checks run on each; or a session forgetting the marker, whose only effect would be the emails again, until the workflow's own rule ([DEC-065](../decisions/DEC-065-preserve-owner-question-on-skipping-checks.md)). It sets no rule and changes nothing. This is **not** an active source of truth. It is preserved by DEC-065, as the owner's questions are kept ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7; [owner decisions 16](owner-decisions-16-short-instructions-approvals-and-questions.md)).
>
> **Formatting note:** the message is reproduced inside one text block exactly as received, including the two spaces after "problem" and the space that ends its first line. Nothing was added, removed, or changed in it. The title, this banner, and the dated heading are the builder's.

## 2026-11-09, 15:00 UTC

```text
I hope this skip of a thing will cause problem  or create problems in the future here is what you said 
The failure emails: every backup snapshot now carries [skip ci]. I checked GitHub: none of the nine backups since then started a run, so they send no emails. After Stage 1 exits, the workflow itself will skip backup branches, as its own reviewed change. The developer guide now says so.

Hope this will not create problems that we dont want
```
