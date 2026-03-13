from __future__ import annotations

import json
import sys
from pathlib import Path
from threading import Thread
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (ROOT / "packages" / "contracts", ROOT / "services" / "api_service")
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from api_service.server import DEFAULT_DATA_PATH, DEFAULT_STATIC_ROOT, make_server


def main() -> int:
    server = make_server(host="127.0.0.1", port=0, data_path=DEFAULT_DATA_PATH, static_root=DEFAULT_STATIC_ROOT)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base_url = f"http://127.0.0.1:{server.server_port}"

        with urlopen(f"{base_url}/") as response:
            html = response.read().decode("utf-8")
            if "Platform Starter" not in html:
                raise SystemExit("Unexpected HTML response.")

        with urlopen(f"{base_url}/api/summary") as response:
            summary = json.loads(response.read().decode("utf-8"))
            if summary["total_items"] < 1:
                raise SystemExit("Unexpected summary response.")

        print("E2E smoke test passed.")
        return 0
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
