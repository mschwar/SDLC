from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .audit import append_audit_event, verify_audit_chain
from .models import ChangeRequest
from .service import build_control_packet


def _load_request(path: str) -> ChangeRequest:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Request file must contain a JSON object.")
    return ChangeRequest.from_dict(payload)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plan and audit regulated changes.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan", help="Build a control packet from a JSON file.")
    plan_parser.add_argument("path", help="Path to the request JSON file.")
    plan_parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON response.")

    record_parser = subparsers.add_parser("record", help="Record a planned change in the audit store.")
    record_parser.add_argument("path", help="Path to the request JSON file.")
    record_parser.add_argument("--actor", required=True, help="Actor responsible for the event.")
    record_parser.add_argument("--action", required=True, help="Action name to record.")
    record_parser.add_argument("--db", default="audit/change-control.db", help="Audit database path.")
    record_parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON response.")

    verify_parser = subparsers.add_parser("verify", help="Verify the audit chain.")
    verify_parser.add_argument("--db", default="audit/change-control.db", help="Audit database path.")
    verify_parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON response.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "plan":
            packet = build_control_packet(_load_request(args.path)).to_dict()
            if args.pretty:
                print(json.dumps(packet, indent=2, sort_keys=True))
            else:
                print(json.dumps(packet, sort_keys=True))
            return 0

        if args.command == "record":
            packet = build_control_packet(_load_request(args.path))
            event = append_audit_event(args.db, actor=args.actor, action=args.action, packet=packet).to_dict()
            if args.pretty:
                print(json.dumps(event, indent=2, sort_keys=True))
            else:
                print(json.dumps(event, sort_keys=True))
            return 0

        if args.command == "verify":
            is_valid, event_count = verify_audit_chain(args.db)
            payload = {"valid": is_valid, "event_count": event_count}
            if args.pretty:
                print(json.dumps(payload, indent=2, sort_keys=True))
            else:
                print(json.dumps(payload, sort_keys=True))
            return 0 if is_valid else 3
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    parser.print_help()
    return 1
