---
title: "Reflection (Self-Evaluation / Plan-Act-Reflect)"
principle: "Reflection"
category: "Agentic"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Reflection (Self-Evaluation / Plan-Act-Reflect) – Agentic Instruction Sheet

## What It Is
An architectural pattern where an agent (or a secondary evaluator agent) explicitly critiques, scores, and refines an output against a defined rubric before returning the final result to the user.

## Why It Matters for Agentic Systems
LLMs are generally better at critiquing outputs than generating them perfectly on the first try. Implementing reflection loops drastically reduces hallucinations, formatting errors, and logic flaws by forcing the system to catch and correct its own mistakes iteratively.

## Core Rules
- Decouple generation and reflection: Do not ask the LLM to generate and reflect in the same output block.
- Use structured rubrics for reflection (e.g., "Check for: 1. Tone, 2. Factuality, 3. Formatting").
- Implement a hard cap on reflection loops (e.g., max 3 iterations) to prevent infinite looping and excessive cost.
- Pass the exact critique back to the generator agent as explicitly as possible.
- For high-stakes tasks, use a separate, potentially stronger LLM for the Reflection node.

## How to Apply It
1. Create a `Generator` node that produces an initial draft.
2. Create an `Evaluator` node with a strict grading rubric and a structured output schema (`is_valid: bool`, `critique: str`).
3. Set up a conditional graph edge: If `is_valid` is True, route to END. If False, route back to `Generator`.
4. Append the `critique` to the `Generator`'s context so it knows what to fix.
5. Add a `loop_count` to the graph state. Force route to END if `loop_count >= MAX_LOOPS`.

## Agentic Patterns & Ready-to-Use Examples

**Plan-Act-Reflect Loop (LangGraph Style)**
```python
from typing import TypedDict

class State(TypedDict):
    draft: str
    critique: str
    loop_count: int

def evaluator_node(state: State):
    rubric = "Does the draft cite sources? Return valid=true if yes, else provide critique."
    result = llm_structured.invoke(f"{rubric}\nDraft: {state['draft']}")

    return {
        "critique": result.critique,
        "is_valid": result.is_valid,
        "loop_count": state["loop_count"] + 1
    }

def routing_logic(state: State):
    if state["is_valid"]: return "END"
    if state["loop_count"] >= 3: return "END" # Failsafe
    return "generator_node"
```

**Reflection Prompt Template**
```text
You are an expert Reviewer. Review the Draft against the Request.
Request: {request}
Draft: {draft}

Identify specific errors. Do not rewrite it yourself.
Output your critique in the exact format:
ERROR: [description]
FIX: [instruction for generator]
```

## Common Pitfalls & How to Avoid Them

- **Infinite Loops:** The generator repeatedly fails, and the evaluator repeatedly rejects. Fix: Always implement a max_retries counter in the graph state.
- **Vague Critiques:** The evaluator says "Make it better." Fix: Force the evaluator to use a rigid, bulleted rubric and provide actionable fixes.
- **Same-Model Blindness:** A weak model grading its own output will approve its own hallucinations. Fix: Use a larger/smarter model for the Evaluator node, or use deterministic code tests.

## Quick Checklist (for self-review or automated eval)

- Is generation strictly separated from evaluation/reflection?
- Is there a hard-coded maximum limit on the reflection loop?
- Does the evaluator output a structured critique containing actionable fixes?
- Are objective errors (like JSON schema validation) caught deterministically before LLM reflection?

## References

- Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)
- Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)
