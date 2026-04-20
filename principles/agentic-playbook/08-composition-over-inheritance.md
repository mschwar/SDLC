---
title: "Composition over Inheritance"
principle: "Composition over Inheritance"
category: "Timeless"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Composition over Inheritance – Agentic Instruction Sheet

## What It Is
Construct agents by composing modular, reusable components (tools, memory backends, guardrails, specific prompt fragments) rather than building deep, rigid class hierarchies of Agent types.

## Why It Matters for Agentic Systems
Agentic requirements change rapidly. If you build a strict class hierarchy (`BaseAgent` -> `SearchAgent` -> `FinancialSearchAgent`), adding a new capability (e.g., a memory module) requires refactoring the entire inheritance tree. Composition allows dynamic injection of capabilities at runtime, making agents highly adaptable.

## Core Rules
- Do not use deep class inheritance (e.g., `class CodeAgent(BaseAgent)`).
- Define agents as simple, pure functions or lightweight orchestration classes.
- Inject tools, LLM clients, memory stores, and system prompts into the agent as parameters (Dependency Injection).
- Build complex behaviors by chaining distinct nodes in a graph rather than adding complex methods to a single Agent class.
- Use Mixins or decorators for non-core logic (e.g., logging, retries) rather than parent classes.

## How to Apply It
1. Define standard interfaces for `Tool`, `Memory`, and `LLM`.
2. Create a generic `AgentExecutor` or graph node function that accepts these interfaces.
3. To create a specific agent (e.g., "Financial Analyst"), compose it: pass the `FinancialTools` list, the `PostgresMemory` module, and the `FinancialPrompt` string to the generic executor.
4. If an agent needs a new capability, pass a new component to it at runtime rather than creating a subclass.

## Agentic Patterns & Ready-to-Use Examples

*Bad (Inheritance):*
```python
class BaseAgent:
    def execute(self): pass

class DatabaseAgent(BaseAgent):
    def connect_db(self): pass

class FinancialDBAgent(DatabaseAgent):
    def calculate_metrics(self): pass
# Rigid: Hard to add web-search to FinancialDBAgent without breaking the hierarchy.
```

*Good (Composition):*
```python
from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Agent:
    llm: Callable              # Composed LLM engine
    tools: List[Callable]      # Composed list of tools
    system_prompt: str         # Composed instructions
    memory_store: Callable     # Composed memory

# Build dynamic agents by composing components at runtime
financial_agent = Agent(
    llm=gpt_4o_client,
    tools=[sql_query_tool, calc_metrics_tool, web_search_tool], # Easily combined!
    system_prompt="You are a financial analyst...",
    memory_store=redis_memory
)
```

## Common Pitfalls & How to Avoid Them

- **Rigid Hierarchies:** Being unable to give a "SupportAgent" coding abilities because it inherits from a strictly non-technical parent class. Fix: Treat agents as empty shells that execute composed tools.
- **Overloaded Parent Classes:** Putting routing, memory, and LLM retry logic all into BaseAgent. Fix: Extract retry logic to a decorator, memory to a separate module.
- **Prompt Inheritance:** Attempting to concatenate strings via super().get_prompt(), leading to messy, unreadable instructions. Fix: Compose prompts using standard template rendering (e.g., Jinja).

## Quick Checklist (for self-review or automated eval)

- Are agents instantiated by passing in components (tools, memory) rather than subclassing?
- Can you easily add a new tool to an agent without modifying its core class?
- Is the system free of deep (3+ levels) inheritance trees for agent definitions?
- Are cross-cutting concerns (logging, retries) handled via composition/decorators?

## References

- Design Patterns: Elements of Reusable Object-Oriented Software (GoF)
- Functional Approaches to LLM Orchestration (2025 AI Engineering Guides)
