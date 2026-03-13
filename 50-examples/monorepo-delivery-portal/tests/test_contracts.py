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

from shared_contracts.models import WorkItem


class SharedContractTests(unittest.TestCase):
    def test_valid_work_item_parses(self) -> None:
        item = WorkItem.from_dict(
            {
                "id": "OPS-101",
                "title": "Ship portal theme",
                "owner": "frontend-team",
                "area": "ops-portal",
                "status": "ready",
                "risk_level": "low",
            }
        )

        self.assertEqual(item.id, "OPS-101")
        self.assertEqual(item.deployment_target, "none")

    def test_invalid_status_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            WorkItem.from_dict(
                {
                    "id": "OPS-102",
                    "title": "Broken status",
                    "owner": "platform-team",
                    "area": "delivery-api",
                    "status": "done",
                    "risk_level": "low",
                }
            )


if __name__ == "__main__":
    unittest.main()
