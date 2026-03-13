from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .models import ReleaseRequest
from .server import run_server
from .service import build_release_plan


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Plan or serve a small-team service workflow.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("path")
    plan_parser.add_argument("--pretty", action="store_true")

    serve_parser = subparsers.add_parser("serve")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8000)

    args = parser.parse_args(argv)

    if args.command == "plan":
        raw = json.loads(Path(args.path).read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            print("Input file must contain a JSON object.", file=sys.stderr)
            return 2
        plan = build_release_plan(ReleaseRequest.from_dict(raw)).to_dict()
        if args.pretty:
            print(json.dumps(plan, indent=2, sort_keys=True))
        else:
            print(json.dumps(plan, sort_keys=True))
        return 0

    run_server(host=args.host, port=args.port)
    return 0
