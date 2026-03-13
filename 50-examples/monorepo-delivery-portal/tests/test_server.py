from __future__ import annotations

import json
import sys
from pathlib import Path
from threading import Thread
import unittest
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (
    ROOT / "packages" / "shared_contracts",
    ROOT / "services" / "delivery_api",
)
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from delivery_api.server import DEFAULT_DATA_PATH, DEFAULT_STATIC_ROOT, make_server


class DeliveryAPIServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = make_server(
            host="127.0.0.1",
            port=0,
            data_path=DEFAULT_DATA_PATH,
            static_root=DEFAULT_STATIC_ROOT,
        )
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def test_root_serves_portal_html(self) -> None:
        with urlopen(f"{self.base_url}/") as response:
            html = response.read().decode("utf-8")

        self.assertIn("Delivery Portal", html)
        self.assertIn("/static/app.js", html)

    def test_summary_endpoint_returns_expected_shape(self) -> None:
        with urlopen(f"{self.base_url}/api/summary") as response:
            payload = json.loads(response.read().decode("utf-8"))

        self.assertEqual(payload["total_items"], 4)
        self.assertIn("blocked", payload["status_counts"])
        self.assertIn("runbook_gaps", payload)


if __name__ == "__main__":
    unittest.main()
