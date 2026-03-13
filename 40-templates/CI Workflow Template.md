---
tags:
  - template
  - ci
type: template
status: active
updated: 2026-03-10
---

# CI Workflow Template

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python scripts/run_quality_checks.py
```

## Related Notes

- [[10-layers/Layer 6 - Review, CI-CD, and Merge]]
- [[20-reference/GitHub Actions]]
