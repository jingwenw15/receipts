from datetime import date
from pathlib import Path
import re
import unittest


ENTRY = re.compile(r"^### (RCPT-\d{3,})\s+[—-]\s+(.+)$")
FIELD = re.compile(r"^- \*\*([^*]+):\*\*\s*(.*)$")


def validate(text: str) -> list[str]:
    if not text.startswith("# Receipts\n"):
        raise ValueError("invalid title")
    entries = []
    fields = {}
    current_field = None

    def finish() -> None:
        if not entries:
            return
        entry_id = entries[-1]
        required = {"Date", "Contribution", "Outcome", "Evidence", "Evidence level"}
        if required - fields.keys() or not all(fields[field] for field in required):
            raise ValueError(f"{entry_id} missing required fields")
        date.fromisoformat(fields["Date"])
        if fields["Evidence level"] not in {"verified", "reported", "draft"}:
            raise ValueError("invalid evidence level")

    for line in text.splitlines():
        if match := ENTRY.match(line):
            finish()
            entries.append(match[1])
            fields = {}
            current_field = None
        elif match := FIELD.match(line):
            current_field = match[1]
            fields[current_field] = match[2]
        elif current_field and line.startswith("  - "):
            fields[current_field] = f"{fields[current_field]}\n{line.strip()}".strip()
    finish()
    if len(entries) != len(set(entries)):
        raise ValueError("duplicate IDs")
    return entries


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = (Path(__file__).parent / "fixtures" / "valid.md").read_text()

    def test_valid_ledger(self) -> None:
        self.assertEqual(validate(self.valid), ["RCPT-001"])

    def test_rejects_missing_outcome(self) -> None:
        with self.assertRaisesRegex(ValueError, "missing required fields"):
            validate(self.valid.replace("- **Outcome:** Reduced verification time.\n", ""))

    def test_rejects_composite_evidence_level(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid evidence level"):
            validate(self.valid.replace("**Evidence level:** reported", "**Evidence level:** mixed"))

    def test_accepts_claim_level_evidence(self) -> None:
        entries = validate(self.valid)
        self.assertEqual(entries, ["RCPT-001"])


if __name__ == "__main__":
    unittest.main()
