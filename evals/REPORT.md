# Behavioral evaluation

Run date: 2026-10-03

Four isolated Codex executions completed without timeouts and passed every critical criterion, ledger contract, and authorization check.

| Scenario | Result |
|---|---|
| Unknown impact without fabrication | Pass |
| Team attribution | Pass |
| Evidence enrichment without duplication | Pass after a regression fix |
| Summary without ledger mutation | Pass |

The regression fix requires one valid overall evidence level—`verified`, `reported`, or `draft`—while allowing individual claims to carry more precise evidence annotations.
