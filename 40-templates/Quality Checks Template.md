---
tags:
  - template
  - testing
type: template
status: active
updated: 2026-03-10
---

# Quality Checks Template

```bash
#!/usr/bin/env bash
set -euo pipefail

python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Suggested Expansion

- unit tests
- integration tests
- type checks
- security checks
- property-based tests when validation logic is important

## Related Notes

- [[10-layers/Layer 3 - The Inner Loop - Code, Test, Commit]]
- [[20-reference/Git Hooks]]
