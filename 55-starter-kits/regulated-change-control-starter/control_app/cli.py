from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .audit import append_audit_event, verify_audit_chain
from .models import ChangeRequest
from .service import build_control_plan


def _load_request(path: str) -> ChangeRequest:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Input file must contain a JSON object.")
    return ChangeRequest.from_dict(raw)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Plan and audit regulated changes.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("path")
    plan_parser.add_argument("--pretty", action="store_true")

    record_parser = subparsers.add_parser("record")
    record_parser.add_argument("path")
    record_parser.add_argument("--actor", required=True)
    record_parser.add_argument("--action", required=True)
    record_parser.add_argument("--db", default="audit/control.db")
    record_parser.add_argument("--pretty", action="store_true")

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("--db", default="audit/control.db")
    verify_parser.add_argument("--pretty", action="store_true")

    args = parser.parse_args(argv)

    if args.command == "plan":
        payload = build_control_plan(_load_request(args.path)).to_dict()
        if args.pretty:
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            print(json.dumps(payload, sort_keys=True))
        return 0

    if args.command == "record":
        event = append_audit_event(
            args.db,
            actor=args.actor,
            action=args.action,
            plan=build_control_plan(_load_request(args.path)),
        ).to_dict()
        if args.pretty:
            print(json.dumps(event, indent=2, sort_keys=True))
        else:
            print(json.dumps(event, sort_keys=True))
        return 0

    valid, event_count = verify_audit_chain(args.db)
    payload = {"valid": valid, "event_count": event_count}
    if args.pretty:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, sort_keys=True))
    return 0 if valid else 3
