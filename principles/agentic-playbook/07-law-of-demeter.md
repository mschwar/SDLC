---
title: "Law of Demeter (LoD) / Principle of Least Knowledge"
principle: "Law of Demeter"
category: "Timeless"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Law of Demeter (LoD) / Principle of Least Knowledge – Agentic Instruction Sheet

## What It Is
An agent should only interact with its immediate dependencies (its own tools, its direct supervisor, or its designated input state), without having any knowledge of or direct access to the internal state, memory, or tools of other agents.

## Why It Matters for Agentic Systems
Tight coupling in multi-agent systems causes catastrophic cascading failures. If Agent A directly modifies Agent B's memory array, or calls Agent C's specific tools, replacing or upgrading Agent B or C will break Agent A. Enforcing strict communication boundaries ensures fault isolation and graph scalability.

## Core Rules
- Agents communicate *only* via clearly defined message schemas (e.g., standard Graph State updates).
- An agent must never directly mutate the internal memory of another agent.
- A worker agent should return results to its supervisor or the global state, not directly invoke peer workers.
- Agents should not know the implementation details of their tools (e.g., an agent knows `execute_sql`, but doesn't know it connects to Postgres vs MySQL).
- Limit the context passed to an agent to *only* what it needs to execute its specific task.

## How to Apply It
1. Use a State Graph (e.g., LangGraph) where nodes (agents) only receive the global state as input and return a state update.
2. Define explicit Pydantic schemas for state transitions between agents.
3. If Agent A needs Agent B to do something, Agent A returns a "Task Request" to the Supervisor/Router, which then routes to Agent B.
4. Filter the global state before passing it to a sub-agent (e.g., do not pass the entire conversation history to a formatting agent).

## Agentic Patterns & Ready-to-Use Examples

*Bad (Violates LoD): Agent A directly calls Agent B.*
```python
def researcher_agent(query):
    data = search_web(query)
    # BAD: Researcher directly instantiates and calls Writer
    writer = WriterAgent()
    return writer.generate(data)
```

*Good (Applies LoD): Agents communicate via State and Supervisor.*
```python
from typing import TypedDict

class GraphState(TypedDict):
    research_data: str
    final_draft: str
    next_node: str

def researcher_node(state: GraphState):
    data = search_web(state["query"])
    # GOOD: Researcher only updates the state. It knows nothing about the Writer.
    return {"research_data": data, "next_node": "writer"}

def writer_node(state: GraphState):
    # GOOD: Writer only reads the data it needs from state.
    draft = llm.invoke(f"Write based on: {state['research_data']}")
    return {"final_draft": draft, "next_node": "END"}
```

## Common Pitfalls & How to Avoid Them

- **Spaghetti Routing:** Agents directly calling other agents in a massive, tangled web. Fix: Use a Hub-and-Spoke (Supervisor) pattern or strict State Graph.
- **State Leakage:** Passing the massive, raw JSON output of Agent A into Agent B's prompt, blowing up context. Fix: Use a dedicated Reducer node to summarize data before passing it.
- **Tool Sharing:** Giving multiple agents access to a single mutable data store tool without concurrency controls. Fix: Isolate mutations to a single specific agent.

## Quick Checklist (for self-review or automated eval)

- Does each agent only receive the minimum context required for its task?
- Are all agent-to-agent communications handled via a standardized State object or Supervisor?
- Is it impossible for one agent to directly modify the internal memory of another?
- Can you test a worker agent in isolation without instantiating other agents?

## References

- Object-Oriented Programming: An Objective Sense of Style (Lieberherr et al.)
- Multi-Agent Communication Protocols in LangGraph/CrewAI (2026 Documentation)
