from __future__ import annotations

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (ROOT / "packages" / "contracts", ROOT / "services" / "api_service")
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from api_service.service import build_summary, load_items


class MonorepoStarterServiceTests(unittest.TestCase):
    def test_summary_counts_items(self) -> None:
        summary = build_summary(load_items(ROOT / "examples" / "items.json"))
        self.assertEqual(summary.total_items, 3)
        self.assertEqual(summary.high_risk_count, 1)


if __name__ == "__main__":
    unittest.main()
