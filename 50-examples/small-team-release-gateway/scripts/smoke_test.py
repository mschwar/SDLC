from __future__ import annotations

import json
import sys
from pathlib import Path
from threading import Thread
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from release_gateway.server import make_server


def main() -> int:
    server = make_server(host="127.0.0.1", port=0)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        base_url = f"http://127.0.0.1:{server.server_port}"

        with urlopen(f"{base_url}/healthz") as response:
            payload = json.loads(response.read().decode("utf-8"))
            if payload != {"status": "ok"}:
                raise SystemExit("Unexpected health response.")

        body = (ROOT / "examples" / "low-risk-request.json").read_bytes()
        request = Request(
            f"{base_url}/plan",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            payload = json.loads(response.read().decode("utf-8"))
            if payload["rollout_strategy"] != "direct":
                raise SystemExit("Unexpected rollout strategy in smoke test.")
            if "ci" not in payload["required_gates"]:
                raise SystemExit("Missing CI gate in smoke test.")

        print("Smoke test passed.")
        return 0
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
