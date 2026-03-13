from __future__ import annotations

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (
    ROOT / "packages" / "shared_contracts",
    ROOT / "services" / "delivery_api",
)
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from delivery_api.service import build_summary, load_work_items


class DeliveryAPIServiceTests(unittest.TestCase):
    def test_summary_counts_statuses_and_risk(self) -> None:
        items = load_work_items(ROOT / "examples" / "work-items.json")
        summary = build_summary(items)

        self.assertEqual(summary.total_items, 4)
        self.assertEqual(summary.status_counts["blocked"], 1)
        self.assertEqual(summary.high_risk_count, 2)
        self.assertIn("OPS-202", summary.runbook_gaps)
        self.assertIn("OPS-301", summary.blocked_items)


if __name__ == "__main__":
    unittest.main()
