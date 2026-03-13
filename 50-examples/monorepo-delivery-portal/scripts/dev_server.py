from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOTS = (
    ROOT / "packages" / "shared_contracts",
    ROOT / "services" / "delivery_api",
)
for path in PACKAGE_ROOTS:
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from delivery_api.server import run_server


if __name__ == "__main__":
    run_server()
