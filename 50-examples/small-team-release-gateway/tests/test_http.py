from __future__ import annotations

import json
from threading import Thread
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from release_gateway.server import make_server


class ReleaseGatewayHTTPTests(unittest.TestCase):
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

    def test_health_endpoint(self) -> None:
        with urlopen(f"{self.base_url}/healthz") as response:
            payload = json.loads(response.read().decode("utf-8"))

        self.assertEqual(payload, {"status": "ok"})

    def test_plan_endpoint_returns_release_plan(self) -> None:
        request = Request(
            f"{self.base_url}/plan",
            data=json.dumps(
                {
                    "service": "release-gateway",
                    "objective": "Deploy feature",
                    "branch": "feat/customer-feature",
                    "owner": "platform-team",
                    "environment": "prod",
                    "change_type": "feature",
                    "acceptance_criteria": ["Feature is tested"],
                    "risk_level": "medium",
                    "customer_visible": True,
                    "rollback_ready": True,
                }
            ).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))

        self.assertEqual(payload["service"], "release-gateway")
        self.assertIn("release-approval", payload["required_gates"])
        self.assertEqual(payload["rollout_strategy"], "staged-rollout")

    def test_malformed_json_returns_400(self) -> None:
        request = Request(
            f"{self.base_url}/plan",
            data=b"{bad json",
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with self.assertRaises(HTTPError) as context:
            urlopen(request)

        payload = json.loads(context.exception.read().decode("utf-8"))
        self.assertEqual(context.exception.code, 400)
        self.assertEqual(payload["error"], "Malformed JSON.")


if __name__ == "__main__":
    unittest.main()
