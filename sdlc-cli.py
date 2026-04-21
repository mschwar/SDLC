#!/usr/bin/env python3
"""
CLI for the Agentic SDLC framework.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sdlc import GeneratorError, ManifestError, generate_repo, load_manifest


def load_principles() -> int:
    playbook_path = Path("principles/agentic-playbook/index.md")
    if not playbook_path.exists():
        print(f"Error: Playbook not found at {playbook_path}", file=sys.stderr)
        return 1
    print(playbook_path.read_text(encoding="utf-8"))
    return 0


def check_sdlc() -> int:
    checks_passed = True
    print("Running SDLC Baseline Check...")

    if not Path(".husky").exists():
        print("❌ Missing .husky/ directory. Run sdlc-bootstrap-kit/bootstrap-sdlc.sh")
        checks_passed = False
    else:
        print("✅ Git hooks (.husky) are installed.")

    if not Path(".github/workflows/agent-principle-check.yml").exists():
        print("❌ Missing agent-principle-check.yml. GitHub Actions not fully configured.")
        checks_passed = False
    else:
        print("✅ Agent Principle Check action is configured.")

    if checks_passed:
        print("\nAll baseline SDLC checks passed! 🚀")
        return 0
    print("\nSDLC framework is incomplete or misconfigured.", file=sys.stderr)
    return 1


def validate_manifest(path: str | Path, *, pretty: bool) -> int:
    manifest = load_manifest(path)
    payload = {
        "schema_version": manifest.schema_version,
        "profile": manifest.profile.id,
        "repository": manifest.repository.slug,
        "package_name": manifest.service.package_name,
        "canonical_files": list(manifest.docs.canonical_files),
        "founder_surfaces": list(manifest.docs.founder_surfaces),
        "environments": [item.name for item in manifest.environments],
    }
    if pretty:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, sort_keys=True))
    return 0


def generate_from_manifest(path: str | Path, output_dir: str | Path, *, force: bool) -> int:
    manifest = load_manifest(path)
    result = generate_repo(manifest, output_dir, force=force)
    payload = {
        "output_dir": str(result.output_dir),
        "starter_kit": str(result.starter_kit),
        "manifest_path": str(result.manifest_path),
        "written_files": list(result.written_files),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agentic SDLC CLI")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Commands")

    subparsers.add_parser("load-principles", help="Output the Agentic Principles Playbook")
    subparsers.add_parser("check", help="Verify the local repository SDLC setup")

    validate_parser = subparsers.add_parser("validate-manifest", help="Validate a repo manifest")
    validate_parser.add_argument("path", help="Path to the manifest JSON file.")
    validate_parser.add_argument("--pretty", action="store_true", help="Pretty-print the validation summary.")

    generate_parser = subparsers.add_parser("generate-repo", help="Generate a repo baseline from a manifest")
    generate_parser.add_argument("manifest", help="Path to the manifest JSON file.")
    generate_parser.add_argument("output_dir", help="Directory to generate the repo into.")
    generate_parser.add_argument("--force", action="store_true", help="Allow generation into a non-empty output directory.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "load-principles":
            return load_principles()
        if args.command == "check":
            return check_sdlc()
        if args.command == "validate-manifest":
            return validate_manifest(args.path, pretty=args.pretty)
        if args.command == "generate-repo":
            return generate_from_manifest(args.manifest, args.output_dir, force=args.force)
    except (ManifestError, GeneratorError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
