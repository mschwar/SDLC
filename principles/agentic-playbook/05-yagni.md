---
title: "YAGNI – You Aren't Gonna Need It"
principle: "YAGNI"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# YAGNI – You Aren't Gonna Need It – Agentic Instruction Sheet

## What It Is
Never implement agentic capabilities, tools, memory stores, or complex reasoning pathways until there is empirical proof (via evaluation) that they are strictly necessary.

## Why It Matters for Agentic Systems
Developers often preemptively give agents vector databases, web search, and cross-agent memory, assuming they will make the agent "smarter." In reality, giving an LLM unnecessary tools drastically increases the probability of distraction, infinite loops, and decision paralysis. YAGNI ensures lean, highly performant agents.

## Core Rules
- Start with zero tools. Add a tool only when a test case explicitly fails without it.
- Do not implement long-term memory (e.g., RAG/Vector DBs) unless the task strictly requires multi-session historical context.
- Do not build multi-agent hierarchies (Supervisors/Routers) for linear workflows.
- Delay implementing self-reflection/correction loops until the zero-shot error rate is unacceptably high.
- Avoid preemptively tracking extensive metadata in the graph state.

## How to Apply It
1. Build the baseline: A direct LLM call with a static system prompt.
2. Run your evaluation suite.
3. Identify the failure mode: Did it lack real-time data? Add *only* a search tool.
4. Run evaluation again. Did it fail to follow complex formatting? Add structured outputs.
5. Did it make logical errors requiring self-correction? Add a reflection node.
6. Stop adding features as soon as the evaluation metric passes the target threshold.

## Agentic Patterns & Ready-to-Use Examples

**Progressive Complexity Implementation**

*Step 1: Baseline (Start Here)*
```python
def answer_query(query: str):
    # Just ask the model
    return llm.invoke(query)
```

*Step 2: Add Tool (Only because Step 1 hallucinated current events)*
```python
def answer_query(query: str):
    # Bound the model to one specific tool
    return llm.bind_tools([search_web]).invoke(query)
```

*Step 3: Add Reflection (Only because Step 2 failed qualitative metrics)*
```python
# LangGraph edge condition applied ONLY after empirical failure
graph.add_conditional_edges(
    "generate",
    grade_generation,
    {"pass": END, "fail": "reflect"}
)
```

## Common Pitfalls & How to Avoid Them

- **Tool Hoarding:** Giving a coding agent a web browser, a calculator, and a calendar "just in case." Fix: Strictly limit tools to the immediate task requirements.
- **Preemptive Optimization:** Building a complex routing architecture before testing a single prompt. Fix: Prove the single prompt fails first.
- **Unnecessary Vector DBs:** Using RAG for a document that easily fits in the context window. Fix: Use standard context injection (Context Stuffing) until you hit token limits.

## Quick Checklist (for self-review or automated eval)

- Is every tool provided to the agent currently covered by a test case that requires it?
- Can the architecture be simplified by removing a sub-agent without failing tests?
- Is long-term memory or RAG genuinely required, or does the context window suffice?
- Have you verified that zero-shot prompting fails before implementing a ReAct loop?

## References

- Extreme Programming Explained (Kent Beck)
- The Cost of Complexity in AI Systems (AI Engineering Digest, 2025)
