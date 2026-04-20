# Agent Guide

Welcome, autonomous agent. This document serves as your operational manual for interacting with and contributing to the Agentic SDLC Framework repository. 

## 1. Ground Rules

1. **Read the Playbook:** Before proposing any changes or executing tool calls, you must ingest and align with `principles/agentic-playbook/index.md`.
2. **Follow the Framework:** Your PRs, code changes, and task execution MUST adhere to the blueprints and layer descriptions in this repository.
3. **No Unilateral Changes:** Never bypass branch protection, disable Git hooks, or modify `.github/workflows/agent-principle-check.yml` without explicit human instruction.

## 2. Navigating the Repository

- `agentic-sdlc-blueprint.md`: The canonical overview. Start here if you are confused.
- `principles/agentic-playbook/`: The 15 core principles.
- `40-templates/`: Standardized templates you should use when generating specs, tasks, PRs, or playbooks.
- `sdlc-bootstrap-kit/`: Tools for turning other repositories into agent-ready frameworks. Do not modify the harness unless explicitly requested.

## 3. Adding New Templates or Principles

If tasked with adding a new template or principle:
1. Ensure the new addition does not contradict any existing principle.
2. Use the existing format and structure (e.g., Markdown headers, frontmatter).
3. Open a Pull Request. Expect the `.github/workflows/agent-principle-check.yml` to automatically verify your work.
4. Provide a thorough explanation in your PR description detailing *why* the new template or principle is necessary.
