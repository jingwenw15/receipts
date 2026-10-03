---
name: receipts
description: Capture accomplishments in a durable Markdown evidence ledger and turn them into grounded standup, status, promotion, or performance-review summaries. Use when the user asks to record wins, maintain a brag sheet, document impact, or summarize accomplishments. Do not treat routine activity as demonstrated impact.
---

# Receipts

Preserve credible evidence of work while it is fresh, then reuse it for different audiences without inflating the claims.

## Choose the ledger

Use, in order:

1. A path explicitly named by the user.
2. An existing `RECEIPTS.md` in the current workspace.
3. `.worktrail/RECEIPTS.md` at the workspace root.

Read an existing ledger before changing it. If none exists, create one using [assets/RECEIPTS.md](assets/RECEIPTS.md). Do not create or update a ledger unless the user asks to capture accomplishments, maintain a brag sheet, or explicitly invokes this skill. Generating a summary from supplied material does not itself authorize saving that material.

## Capture a receipt

Prefer accomplishments that show a shipped outcome, solved problem, meaningful learning, improved process, reduced risk, customer benefit, or leverage for other people. Routine activity may provide context but is not an outcome by itself.

- Reconcile with existing entries by outcome and time period so one continuing effort does not become several duplicate wins.
- Preserve stable IDs in the form `RCPT-001`; allocate the next unused number for a new entry.
- Separate the person's contribution from the team's result. Credit collaborators when known.
- Preserve concrete evidence such as metrics, links, artifacts, feedback, adoption, or before/after observations.
- Never invent a metric, causal claim, audience size, quotation, or level of ownership.
- Label approximate figures as estimates and user-provided claims as reported when they are not independently evidenced.
- Set `Evidence level` to exactly `verified`, `reported`, or `draft`. When claims have different support, use the weakest applicable level for the whole entry and annotate each claim's stronger or weaker support inside `Evidence`; never create a composite level.
- If impact is not known, write `Not yet measured` and optionally identify a practical signal to collect later.
- Keep sensitive details no more specific than necessary for the requested use.

For the entry fields, evidence levels, and deduplication rules, read [references/ledger-format.md](references/ledger-format.md) when creating, repairing, or substantially reorganizing a ledger.

## Produce summaries

When asked for a standup, review, or promotion summary:

- Select entries for the requested period and audience.
- Lead with outcomes and evidence, then explain the contribution.
- Combine milestones from the same initiative instead of repeating them.
- Preserve uncertainty and attribution from the ledger.
- Organize by impact theme or competency when that is more useful than chronology.
- Do not mutate the ledger merely to generate a view unless the user also asks to save or enrich it.

## Report the result

After editing, state the ledger path and briefly list what was added or enriched. Call out missing evidence as a useful follow-up, not as an accomplished result. If nothing material changed, avoid a no-op rewrite.
