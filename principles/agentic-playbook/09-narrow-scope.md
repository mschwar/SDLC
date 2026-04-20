---
title: "Narrow Scope / Single Responsibility per Agent"
principle: "Narrow Scope"
category: "Agentic"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Narrow Scope / Single Responsibility per Agent – Agentic Instruction Sheet

## What It Is
Each agent must have one clearly defined objective, a minimal set of highly specific tools, and a strictly bounded context.

## Why It Matters for Agentic Systems
LLMs suffer from "attention collapse" and instruction drift when tasked with multiple competing objectives or given dozens of tools. Narrowly scoped agents are predictable, easier to test, less prone to hallucination, and allow for granular observability and cost control.

## Core Rules
- An agent should do exactly one thing (e.g., extract entities, format JSON, write code, run tests).
- Never combine generative tasks (creative writing) with analytical tasks (data validation) in the same agent.
- Limit an agent to a maximum of 3–5 tools.
- If an agent's system prompt requires multiple distinct sections (e.g., "Phase 1... Phase 2..."), split it into separate agents in a graph.
- Name agents strictly by their function (e.g., `SQLValidator`, not `DatabaseAssistant`).

## How to Apply It
1. Map out your workflow as a sequence of discrete tasks.
2. For each task, create a single node (agent).
3. Assign only the tools strictly required for that specific task.
4. Write a terse system prompt focusing purely on that task.
5. Connect the agents using a state graph or a routing supervisor.

## Agentic Patterns & Ready-to-Use Examples

*Bad (Broad Scope / God Agent):*
```python
system_prompt = """
You are an AI assistant.
1. Search the web for user queries.
2. Write a blog post about the findings.
3. Check the blog post for grammar.
4. Translate it to Spanish.
"""
tools = [search, write_file, grammar_check, translate]
# High risk of skipping steps, mixing up languages, or failing to use tools correctly.
```

*Good (Narrow Scope / Graph of Agents):*
```python
# Agent 1: Researcher (Only searches and extracts facts)
research_prompt = "Search the web and return a bulleted list of verified facts."
tools = [search]

# Agent 2: Writer (Only writes, NO search tools)
write_prompt = "Convert the provided facts into a well-structured English blog post."
tools = []

# Agent 3: Translator (Only translates)
translate_prompt = "Translate the provided text into Spanish. Preserve formatting."
tools = []

# These are orchestrated sequentially via LangGraph.
```

## Common Pitfalls & How to Avoid Them

- **The "Swiss Army Knife" Prompt:** Adding "Oh, and also do X" to a prompt when a bug occurs. Fix: Route the output to a new validator/fixer agent instead.
- **Tool Overload:** Giving an agent 20 tools, causing it to hallucinate tool names or use the wrong one. Fix: Isolate tools to domain-specific worker agents.
- **Blurred Boundaries:** An agent trying to fix its own inputs. Fix: Ensure strict input validation before the agent is invoked; reject bad inputs.

## Quick Checklist (for self-review or automated eval)

- Can the agent's purpose be described accurately in one short sentence without using "and"?
- Does the agent have 5 or fewer tools assigned to it?
- Are generative tasks separated from evaluative/analytical tasks?
- Is the system prompt free of multi-phase execution instructions?

## References

- The Single Responsibility Principle in Multi-Agent Systems (Scale AI Engineering, 2024)
- LangGraph Patterns: Node Modularity (LangChain Docs, 2026)
