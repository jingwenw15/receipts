# Receipts

An evidence-first accomplishment log for standups, brag sheets, and performance reviews.

Receipts is a Codex skill that records contributions while the evidence is fresh, separates activity from impact, preserves team attribution, and turns the ledger into audience-specific summaries without inflating claims.

## What it captures

- Individual contribution versus team outcome
- Metrics, artifacts, feedback, and adoption evidence
- Evidence confidence and unresolved measurement gaps
- Competencies, collaborators, scope, and reusable review material

By default, the ledger lives at `.worktrail/RECEIPTS.md` in the current workspace.

## Install

Clone the repository into your personal Codex skills directory:

```sh
git clone https://github.com/jingwenw15/receipts.git ~/.codex/skills/receipts
```

Then invoke it explicitly or ask naturally:

```text
Use $receipts to record what we accomplished today.
Draft my weekly standup from the last two weeks of receipts.
```

## Quality

The skill passed all four isolated behavioral scenarios covering unknown impact, team attribution, evidence enrichment without duplication, and summary generation without unauthorized writes. See [evals/REPORT.md](evals/REPORT.md).

Run the dependency-free ledger contract tests with:

```sh
python3 -m unittest discover -s tests -v
```
