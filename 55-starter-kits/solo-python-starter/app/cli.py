from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .models import WorkRequest
from .service import build_work_plan


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a simple work plan from JSON input.")
    parser.add_argument("path")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args(argv)

    raw = json.loads(Path(args.path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SystemExit("Input file must contain a JSON object.")

    plan = build_work_plan(WorkRequest.from_dict(raw)).to_dict()
    if args.pretty:
        print(json.dumps(plan, indent=2, sort_keys=True))
    else:
        print(json.dumps(plan, sort_keys=True))
    return 0
