# Contributing to the Agentic SDLC Framework

Thank you for your interest in improving the Agentic SDLC Framework! Whether you are a human operator or an autonomous agent, your contributions help refine the standard for production-grade agent operating systems.

## For Human Operators

1. **Proposing Changes:** If you have an idea for a new principle, template, or process improvement, please open an Issue first to discuss it.
2. **Pull Requests:** 
   - Ensure your PR includes a clear description of the problem and your proposed solution.
   - All PRs are subject to the `agent-principle-check.yml` workflow, which uses an LLM to evaluate changes against the framework's 15 core principles.
   - Keep changes focused and surgical.
3. **Bootstrapping Kit:** If you are modifying the `sdlc-bootstrap-kit/bootstrap-sdlc.sh`, ensure the `curl` commands reference the correct paths and that the script remains executable and strictly Bash-compliant.

## For Autonomous Agents

Please see the [AGENT-GUIDE.md](AGENT-GUIDE.md) for detailed operational instructions.

1. Always bootstrap your session with `40-templates/agent-bootstrap-prompt.md`.
2. Prioritize adhering to `principles/agentic-playbook/index.md` in every reasoning trace.
3. Run the self-check instruction before finalizing your work.

## Development Setup

1. Clone the repository.
2. We recommend running the `sdlc-bootstrap-kit/bootstrap-sdlc.sh` script locally to ensure you have the necessary commit hooks installed.
3. Use Conventional Commits (`feat:`, `fix:`, `docs:`, etc.) for all your commit messages.
