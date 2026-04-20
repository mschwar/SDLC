---
title: "KISS – Keep It Simple, Stupid"
principle: "KISS"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# KISS – Keep It Simple, Stupid – Agentic Instruction Sheet

## What It Is
Design agentic workflows, prompts, and tool interfaces to be as minimal and straightforward as possible, avoiding over-engineering and unnecessary autonomous loops.

## Why It Matters for Agentic Systems
LLMs amplify complexity. If an architecture relies on a multi-agent debate with nested reflection loops for a task that could be solved by a simple Python script or a single zero-shot prompt, you invite hallucination, latency, and exorbitant token costs. Simplicity bounds non-determinism.

## Core Rules
- Do not use an autonomous agent if standard code (e.g., regex, deterministic API) can solve the problem.
- Favor structured prompt chains (A -> B -> C) over autonomous routing loops (ReAct) whenever the workflow is predictable.
- Keep system prompts concise; remove redundant politeness, theoretical fluff, or conflicting instructions.
- Limit the number of parameters in any given tool schema to reduce LLM cognitive load.
- Start with the simplest model capable of the task (e.g., a fast 8B model) before scaling to frontier models.

## How to Apply It
1. Analyze the task: Can this be solved deterministically? If yes, write code.
2. If an LLM is needed, write a single prompt. Evaluate.
3. If it fails, split into a 2-step prompt chain. Evaluate.
4. Only if the workflow requires dynamic decision-making should you introduce a tool-calling ReAct loop.
5. Review prompts and tool schemas; delete any instruction or parameter that does not directly contribute to the evaluation metric.

## Agentic Patterns & Ready-to-Use Examples

**KISS vs. Over-Engineered Tool Schema**

*Bad (Over-engineered):*
```json
{
  "name": "get_weather",
  "parameters": {
    "location": "str",
    "unit": "enum[celsius, fahrenheit, kelvin]",
    "historical_comparison": "bool",
    "include_humidity_index": "bool"
  }
}
```

*Good (KISS):*
```json
{
  "name": "get_weather",
  "parameters": {
    "location": "str"
  }
}
```
The deterministic backend automatically handles defaults and standard formatting.

**Workflow Simplification (Python)**
```python
# Unnecessary Agentic Loop:
# agent = create_react_agent("Check inventory and calculate price")

# KISS Approach: Deterministic Code + Simple LLM Call
def process_order(item_id: str):
    # 1. Deterministic DB call (No LLM needed)
    price = db.get_price(item_id)

    # 2. Simple LLM generation (No ReAct needed)
    return llm.invoke(f"Write a polite email charging ${price} for {item_id}.")
```

## Common Pitfalls & How to Avoid Them

- **Defaulting to Multi-Agent:** Using AutoGen or CrewAI for simple text summarization. Fix: Use a standard LLM completion call.
- **Overstuffed Prompts:** Trying to cover every theoretical edge case in one prompt. Fix: Rely on narrow scoping and standard fallback tools.
- **Complex Tool Parameters:** Asking the LLM to format nested JSON structures in tool arguments. Fix: Flatten tool arguments and handle complex formatting in the backend.

## Quick Checklist (for self-review or automated eval)

- Can the LLM's task be accomplished by a deterministic function?
- Is the workflow a simple chain rather than a complex cyclic graph?
- Are tool arguments restricted to basic types (strings, ints, booleans)?
- Have you removed "fluff" (e.g., "Take a deep breath", "You are a helpful AI") from the prompt?

## References

- The Principles of Product Development Flow (Donald G. Reinertsen)
- When Not to Use Agents (OpenAI DevDay, 2024)
