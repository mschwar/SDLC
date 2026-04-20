# Agentic SDLC Framework

This repository is an agent-first software development lifecycle framework designed to build self-enforcing, production-ready multi-agent systems. Every agent operating within this repository MUST load and internalize `principles/agentic-playbook/index.md` before initiating any reasoning or tool use. 

## How Agents Use This Repo

- **Mandatory Initialization:** Every agent session must begin by loading the Agent Bootstrap Prompt and reading the core principles.
- **Workflow Alignment:** Agents design and execute tasks in strict accordance with the canonical rules established in the repository blueprint.
- **Continuous Self-Checking:** Agents must continuously self-evaluate their reasoning traces against the non-negotiable principles before taking destructive actions.
- **Template Utilization:** Agents rely on the provided templates to ensure uniform output, comprehensive testing, and standardized PRs.
- **Context Awareness:** Agents consult context files to maintain awareness of repository boundaries, tools, and environmental constraints.

## Key Resources

- [Agentic Principles Playbook](principles/agentic-playbook/index.md)
- [Agentic SDLC Blueprint](agentic-sdlc-blueprint.md)
- [Repository Context](CONTEXT.md)

## Bootstrap Command

To initialize an agent session, apply the following prompt:
`cat 40-templates/agent-bootstrap-prompt.md`
