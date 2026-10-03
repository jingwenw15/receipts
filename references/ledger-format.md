# Receipts ledger format

Use this format when initializing or repairing `RECEIPTS.md`. Preserve useful extra fields in an existing ledger rather than forcing a rewrite.

## Receipt entry

```markdown
### RCPT-001 — Reduced release verification time

- **Date:** 2026-09-30
- **Initiative:** Release automation
- **Contribution:** Designed and implemented an automated verification workflow.
- **Outcome:** Reduced a manual 45-minute process to approximately 8 minutes.
- **Evidence:** Timing notes and merged pull request link.
- **Evidence level:** verified
- **Scope:** Release engineering team
- **Collaborators:** Names or team, when known
- **Competencies:** execution, leverage, collaboration
- **Tags:** automation, developer-experience
```

`Initiative`, `Scope`, `Collaborators`, `Competencies`, and `Tags` are optional. Use `Outcome: Not yet measured` rather than translating activity into unsupported impact.

## Evidence levels

- `verified`: directly supported by an artifact, metric, link, or accessible feedback.
- `reported`: stated by the user or another source but not independently verified here.
- `draft`: incomplete recollection or a candidate that needs confirmation before formal reuse.

An evidence level describes support for the claim, not the value of the work.

`Evidence level` must contain exactly one of those three values. For mixed support, choose the weakest applicable overall level (`draft` before `reported` before `verified`) and distinguish individual claims in `Evidence`. For example, an existing verified time saving plus newly reported adoption has overall level `reported`, while `Evidence` identifies the time saving as verified and adoption as reported.

## Deduplication and enrichment

- Merge records that describe the same outcome, initiative, and time period.
- Add later metrics or feedback to the original receipt rather than creating a new one.
- Create a separate receipt for a genuinely new outcome, broader adoption milestone, or distinct contribution.
- Preserve chronology inside an entry with concise dated evidence bullets when an initiative develops over time.
- Never recycle or renumber an ID.

## Summary checks

Before using a receipt in a formal review, ask:

1. Is the contribution attributable without erasing collaborators?
2. Is the outcome distinct from the activity performed?
3. Is every number or strong claim supported or clearly qualified?
4. Does the chosen evidence match the audience and confidentiality level?
