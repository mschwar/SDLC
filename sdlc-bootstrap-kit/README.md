# SDLC Bootstrap Kit

This toolkit automatically configures a "bumper rails" Software Development Life Cycle (SDLC) environment for AI-assisted or greenfield repositories. 

## What it does

When run, the bootstrap script will:
1. Initialize `package.json` (if missing).
2. Install `husky` and `@commitlint/config-conventional`.
3. Set up **Git Hooks**:
   - `pre-commit`: Blocks committing directly to `main` or `master`.
   - `pre-push`: Blocks pushing directly to `main` or `master`.
   - `commit-msg`: Enforces Conventional Commits (e.g., `feat: ...`, `fix: ...`).
4. Copy a **GitHub Actions PR verification workflow** (`.github/workflows/pr-checks.yml`).
5. Copy the **Gate Closeout Protocol** (`GATE_CLOSEOUT.md`) into the project root.

## How to use it

1. Navigate to the root of your target repository in your terminal.
2. Run the bootstrap script from this folder:
   ```bash
   /path/to/sdlc-bootstrap-kit/bootstrap.sh
   ```
3. Append the agent instructions found in `templates/AGENTS-SDLC-SECTION.md` to your repository's primary AI context file (e.g., `AGENTS.md` or `instructions.md`).
4. Update your `RUNBOOK.md` to reference the newly added `GATE_CLOSEOUT.md` file.
5. Commit and push the new setup!
