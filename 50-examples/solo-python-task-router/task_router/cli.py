from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import TaskSpec
from .service import build_workflow_decision


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a task spec and emit the recommended workflow decision."
    )
    parser.add_argument("path", type=Path, help="Path to a task spec JSON file")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON output")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    raw = json.loads(args.path.read_text(encoding="utf-8"))
    spec = TaskSpec.from_dict(raw)
    decision = build_workflow_decision(spec)
    payload = {"task_spec": spec.to_dict(), "workflow_decision": decision.to_dict()}
    if args.pretty:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, sort_keys=True))
    return 0
