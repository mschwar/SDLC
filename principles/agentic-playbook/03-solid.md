---
title: "SOLID – Five Object-Oriented Design Principles"
principle: "SOLID"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# SOLID – Five Object-Oriented Design Principles – Agentic Instruction Sheet

## What It Is
An adaptation of five software design principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) applied to multi-agent architectures to ensure maintainability, scalability, and modularity.

## Why It Matters for Agentic Systems
Monolithic "God Agents" with massive prompts and dozens of tools degrade in performance rapidly. Applying SOLID principles structures agents into modular, easily updatable systems where new skills can be added without rewriting the core orchestration logic, and underlying models can be swapped effortlessly.

## Core Rules
- **SRP (Single Responsibility):** An agent should have only one reason to change (e.g., a "Researcher" agent only gathers data; it does not format it).
- **OCP (Open/Closed):** Agent graphs should be open for extension (adding a new tool or sub-agent) but closed for modification (not rewriting the router logic).
- **LSP (Liskov Substitution):** Any LLM or tool should be swappable with a mock or alternative model without breaking the agent's execution loop.
- **ISP (Interface Segregation):** Do not give agents tools they do not need. Expose role-specific tool sets.
- **DIP (Dependency Inversion):** Agents should depend on abstractions (e.g., a generic `SearchInterface`), not concrete implementations (e.g., `GoogleSearchAPI`).

## How to Apply It
1. Decompose complex tasks into a graph of single-purpose agents (SRP).
2. Use dynamic routing or dynamic tool registries so new agents/tools can be registered without modifying the supervisor (OCP).
3. Standardize input/output schemas (BaseMessages) so models can be swapped (LSP).
4. Create specific toolkits (e.g., `db_toolkit`, `web_toolkit`) rather than one massive array of all tools (ISP).
5. Inject tools into the agent at runtime rather than hardcoding imports inside the prompt or agent class (DIP).

## Agentic Patterns & Ready-to-Use Examples

**Applying ISP and DIP via Tool Injection**
```python
from typing import List, Protocol

# DIP: Abstraction for search
class SearchInterface(Protocol):
    def execute_search(self, query: str) -> str: ...

# SRP: Agent only formats
class FormatterAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.system_prompt = "You format text to Markdown. Do nothing else."

# ISP: Specific toolset injected at runtime
def run_researcher(llm_client, search_tool: SearchInterface, query: str):
    agent_tools = [search_tool] # Only search, no unrelated DB tools
    return llm_client.invoke("Research this: " + query, tools=agent_tools)
```

## Common Pitfalls & How to Avoid Them

- **The God Agent (SRP Violation):** Giving one agent 50 tools and a 4,000-word prompt. Fix: Split into a Supervisor and specialized Worker agents.
- **Hardcoded Model Dependencies (DIP/LSP Violation):** Hardcoding gpt-4o specific quirks into the core logic. Fix: Use a model-agnostic wrapper (e.g., LiteLLM) and standard message formats.
- **Tool Bloat (ISP Violation):** Passing the same 20 tools to every agent in the graph. Fix: Bind only necessary tools to specific nodes.

## Quick Checklist (for self-review or automated eval)

- Can you swap the underlying LLM provider without changing the agent logic?
- Does each agent in the system have a single, clearly defined objective?
- Can you add a new sub-agent without rewriting the core routing logic?
- Are tools injected dynamically rather than hardcoded inside the agent logic?

## References

- Agile Software Development, Principles, Patterns, and Practices (Robert C. Martin)
- Modular Agent Architecture Patterns (AI Engineering Consortium, 2025)
