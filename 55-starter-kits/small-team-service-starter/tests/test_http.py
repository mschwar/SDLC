from __future__ import annotations

import json
from threading import Thread
import unittest
from urllib.request import Request, urlopen

from service_app.server import make_server


class SmallTeamStarterHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = make_server(host="127.0.0.1", port=0)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def test_plan_endpoint_returns_release_plan(self) -> None:
        request = Request(
            f"{self.base_url}/plan",
            data=json.dumps(
                {
                    "objective": "Ship change",
                    "branch": "feat/ship-change",
                    "environment": "staging",
                    "acceptance_criteria": ["Behavior is tested"],
                    "risk_level": "medium",
                }
            ).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))

        self.assertIn("release-approval", payload["required_gates"])
        self.assertEqual(payload["release_strategy"], "staged-rollout")


if __name__ == "__main__":
    unittest.main()
