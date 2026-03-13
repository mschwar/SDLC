from __future__ import annotations

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (ROOT / "packages" / "contracts", ROOT / "services" / "api_service")
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from contracts.models import Item


class MonorepoStarterContractTests(unittest.TestCase):
    def test_item_parses(self) -> None:
        item = Item.from_dict(
            {"id": "KIT-1", "title": "Ship change", "owner": "team", "status": "ready", "risk_level": "low"}
        )

        self.assertEqual(item.id, "KIT-1")


if __name__ == "__main__":
    unittest.main()
