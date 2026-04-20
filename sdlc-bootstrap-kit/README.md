# Agentic SDLC Bootstrap Kit

This toolkit turns any standard repository into an Agentic SDLC-compliant framework, allowing you to instantly enforce self-regulating guidelines and templates for multi-agent systems.

## What it does

When run, the bootstrap script will:
1. **Pull the Agentic Framework Core:** Downloads the Agentic Playbook, Blueprint, `CONTEXT.md`, and the essential `agent-bootstrap-prompt.md` into your repository.
2. **Install Agent PR Judge:** Adds the `.github/workflows/agent-principle-check.yml` workflow which uses an LLM-as-judge to verify every Pull Request against the playbook principles.
3. **Configure Local Guardrails:** 
   - Initializes `package.json` (if missing).
   - Installs `husky` and `@commitlint/config-conventional`.
   - Sets up Git hooks to prevent direct commits/pushes to `main` and enforces Conventional Commits.

## How to use it

To bootstrap an existing repository, simply run:

```bash
curl -sL https://raw.githubusercontent.com/mschwar/SDLC/main/sdlc-bootstrap-kit/bootstrap-sdlc.sh | bash
```

Alternatively, clone this repository, navigate to the target project, and execute the script directly.

## Post-Bootstrap Steps

1. **Commit Changes:** Run `git add . && git commit -m "build: bootstrap agentic sdlc framework"`.
2. **Setup Secrets:** Ensure you have added your `GEMINI_API_KEY` to your GitHub repository's Actions Secrets so the PR Principle Check can run.
3. **Initialize Agent Session:** Give your autonomous agent the `40-templates/agent-bootstrap-prompt.md` at the start of every session!
