---
tags:
  - reference
  - tools
type: concept
status: active
updated: 2026-03-10
---

# Agent-Computer Interfaces and Tool Catalogs

> [!abstract] Definition
> The interfaces, tools, and execution surfaces agents use to read context, write changes, run commands, inspect systems, and interact with external services.

## Typical Interface Types

- terminal and shell
- git and repo operations
- browser automation
- language-server or AST-aware editing
- CI APIs
- observability APIs

## Design Rule

Every tool should have a clear purpose, permission boundary, and expected evidence trail.

## Related Notes

- [[20-reference/Permissions and Sandbox Policy]]
- [[20-reference/Agent Roles and Operating Model]]
- [[40-templates/Tool Catalog Template]]
