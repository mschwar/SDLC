#!/usr/bin/env python3
"""
Tiny Python CLI for the Agentic SDLC framework.
Allows agents to easily check compliance or load principles.
"""

import argparse
import sys
import subprocess
from pathlib import Path

def load_principles():
    """Outputs the Agentic Principles Playbook to stdout."""
    playbook_path = Path("principles/agentic-playbook/index.md")
    if not playbook_path.exists():
        print(f"Error: Playbook not found at {playbook_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(playbook_path, "r", encoding="utf-8") as f:
        print(f.read())

def check_sdlc():
    """Runs a rudimentary check to ensure hooks and configs are in place."""
    checks_passed = True
    print("Running SDLC Baseline Check...")

    # Check for husky
    if not Path(".husky").exists():
        print("❌ Missing .husky/ directory. Run sdlc-bootstrap-kit/bootstrap-sdlc.sh")
        checks_passed = False
    else:
        print("✅ Git hooks (.husky) are installed.")

    # Check for GitHub Actions
    if not Path(".github/workflows/agent-principle-check.yml").exists():
        print("❌ Missing agent-principle-check.yml. GitHub Actions not fully configured.")
        checks_passed = False
    else:
        print("✅ Agent Principle Check action is configured.")

    if checks_passed:
        print("\nAll baseline SDLC checks passed! 🚀")
        sys.exit(0)
    else:
        print("\nSDLC framework is incomplete or misconfigured.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Agentic SDLC CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Command: load-principles
    parser_load = subparsers.add_parser("load-principles", help="Output the Agentic Principles Playbook")

    # Command: check
    parser_check = subparsers.add_parser("check", help="Verify the local repository SDLC setup")

    args = parser.parse_args()

    if args.command == "load-principles":
        load_principles()
    elif args.command == "check":
        check_sdlc()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
