---
generated: '2026-03-14T01:10:50Z'
generator: ctx/0.1.0
model: llama3.2:3b
content_hash: sha256:a64cb9ec9a4047439b125cd264796ad63f5ad19a3d04579aa98a45291af9ce26
files: 13
dirs: 6
tokens_total: 2290
---
# C:/Users/Matty/Documents/SDLC/50-examples/small-team-release-gateway
One-line purpose.

## Files
- **.gitignore** — This directory contains a `.gitignore` file with rules to ignore Python compiled files.
- **AGENTS.md** — This is a documentation file for a small team's release process, outlining working rules, definition of done, and expected commands.
- **ARCHITECTURE.md** — This is a documentation for a small Python service that evaluates release requests and returns controls required to ship them.
- **CODEOWNERS** — This directory contains a CODEOWNERS file with permissions for specific teams.
- **DECISIONS.md** — This document outlines five key principles for durable decisions in a release gateway.
- **ENVIRONMENTS.md** — This document outlines environment policies for development, staging, and production environments.
- **README.md** — This is a Python service that accepts a release request in JSON and returns a release plan with controls for shipping safely.
- **RISK_REGISTER.md** — The file is a risk register document detailing active risks with their impact and mitigation strategies.
- **ROADMAP.md** — This is a directory manifest for a release gateway, detailing a roadmap with three phases: current horizon, next steps, and later additions.
- **SCHEMA.md** — This is a documentation file for a release request process, outlining required fields, optional fields, validation rules, and returned fields.
- **SLOS.md** — This is a documentation file for a Service Level Objectives (SLO) policy.
- **THREAT_MODEL.md** — This is a threat model document outlining potential security risks and controls for a software release process.
- **requirements.txt** — This is a requirements file for a small-team release gateway, listing dependencies.

## Subdirectories
- **.githooks** — One-line purpose.
- **.github** — Template for GitHub repository configuration.
- **examples** — Ship a production auth and schema change (high risk) - release-gateway
- **release_gateway** — One-line purpose.
- **scripts** — Run scripts for small team release gateway.
- **tests** — One-line purpose.

## Notes
- If a section has no entries, include the heading and write '- None'.