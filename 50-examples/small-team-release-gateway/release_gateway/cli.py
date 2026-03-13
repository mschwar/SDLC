from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .models import ReleaseRequest
from .server import run_server
from .service import build_release_plan


def _load_request(path: str) -> ReleaseRequest:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Request file must contain a JSON object.")
    return ReleaseRequest.from_dict(payload)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plan or serve release-control decisions.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan", help="Build a release plan from a JSON file.")
    plan_parser.add_argument("path", help="Path to the request JSON file.")
    plan_parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON response.")

    serve_parser = subparsers.add_parser("serve", help="Run the HTTP server.")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8000)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "plan":
            request = _load_request(args.path)
            plan = build_release_plan(request).to_dict()
            if args.pretty:
                print(json.dumps(plan, indent=2, sort_keys=True))
            else:
                print(json.dumps(plan, sort_keys=True))
            return 0

        if args.command == "serve":
            run_server(host=args.host, port=args.port)
            return 0
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    parser.print_help()
    return 1
