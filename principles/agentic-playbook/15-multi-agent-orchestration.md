---
title: "Multi-Agent Orchestration Patterns (ReAct, Supervisor, etc.)"
principle: "Multi-Agent Orchestration"
category: "Agentic"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Multi-Agent Orchestration Patterns (ReAct, Supervisor, etc.) – Agentic Instruction Sheet

## What It Is
Standardized architectural templates for coordinating how autonomous agents plan, delegate tasks, and pass state among themselves to solve complex problems.

## Why It Matters for Agentic Systems
Ad-hoc multi-agent loops degrade quickly into chaos, infinite loops, or context bloat. By utilizing formal orchestration patterns (ReAct, Supervisor, Map-Reduce, Hierarchical), you guarantee predictable control flow, clear boundaries, and scalable task delegation.

## Core Rules
- **Linear Chains:** Use for predictable, static workflows (Agent A -> Agent B -> Output).
- **ReAct (Reason + Act):** Use for single-agent dynamic exploration where the next step depends on the previous tool's output.
- **Supervisor/Router:** Use when multiple specialized agents exist; the Supervisor makes routing decisions but performs no work itself.
- **Map-Reduce:** Use for parallel tasks (e.g., summarizing 10 documents simultaneously, then combining).
- **State Locality:** Pass only relevant state to sub-agents. Supervisors orchestrate; Workers execute.

## How to Apply It
1. Assess the complexity of the workflow. Avoid complex patterns if a simple Chain works.
2. If tasks require parallel execution, implement Map-Reduce using asynchronous nodes.
3. If tasks require dynamic domain expertise, create a Supervisor node.
4. Give the Supervisor a prompt with descriptions of all Worker agents and a structured routing tool.
5. Configure Worker agents to return their output to the global state, then route back to the Supervisor until the task is complete.

## Agentic Patterns & Ready-to-Use Examples

**Supervisor Routing Pattern (LangGraph Style)**
```python
from pydantic import BaseModel
from typing import Literal

# The Supervisor explicitly decides the next node
class RouteOption(BaseModel):
    next_agent: Literal["researcher", "coder", "reviewer", "FINISH"]
    instructions: str

def supervisor_node(state: State):
    system_prompt = """
    You are the Supervisor. Delegate tasks based on the current state.
    - Use 'researcher' for gathering data.
    - Use 'coder' for writing scripts.
    - Use 'reviewer' to test code.
    - Use 'FINISH' when the final objective is met.
    """
    decision = llm_structured.invoke(system_prompt, response_format=RouteOption)

    # State update + routing directive
    return {"route": decision.next_agent, "supervisor_instructions": decision.instructions}

# Graph edges dynamically route based on state["route"]
```

**Map-Reduce Pattern Concept**

- **Map:** Scatter task (e.g., split a 100-page PDF into 10 chunks, spin up 10 parallel summarizer nodes).
- **Reduce:** Gather outputs (e.g., pass 10 summaries to one final Writer node).

## Common Pitfalls & How to Avoid Them

- **Supervisor Doing the Work:** A routing agent tries to answer the user query itself instead of delegating. Fix: Strip the Supervisor of domain tools; strictly limit its output to routing JSON.
- **Deadlocks:** Two agents endlessly passing a task back and forth. Fix: The Supervisor must track attempt_counts and force a termination after N loops.
- **Over-Orchestration:** Using a Supervisor for a task that is always A -> B -> C. Fix: Use a standard sequential graph edge.

## Quick Checklist (for self-review or automated eval)

- Is the chosen orchestration pattern the simplest one possible for the task?
- In a Supervisor pattern, is the routing agent restricted from doing actual domain work?
- Are ReAct loops bounded by a maximum iteration cap?
- Is parallel work correctly fanned out (Map) and gathered (Reduce) to save latency?

## References

- ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022)
- LangGraph Multi-Agent Architectures (LangChain Architecture Guide, 2025)
