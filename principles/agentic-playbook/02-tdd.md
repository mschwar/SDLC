---
title: "TDD – Test-Driven Development"
principle: "TDD"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# TDD – Test-Driven Development – Agentic Instruction Sheet

## What It Is
Write deterministic assertions and automated LLM-as-a-judge evaluation criteria before writing the agent prompt, tool logic, or orchestration graph.

## Why It Matters for Agentic Systems
Agentic workflows are highly susceptible to prompt drift and non-determinism. By defining the expected behavior, structured output schema, and evaluation rubric first, you create a bounded optimization target. This prevents endless "prompt tweaking" that fixes one edge case while breaking three others.

## Core Rules
- Write the expected output schema (Pydantic model) before the system prompt.
- Define exact matching assertions for deterministic tool calls (e.g., "Given X, Agent must call Tool Y with arguments Z").
- Create an LLM-based evaluation prompt (rubric) to grade qualitative outputs before running the agent.
- Fail the test pipeline automatically if the agent's token usage or latency exceeds defined thresholds.
- Run regression tests on a fixed, version-controlled dataset of edge cases every time an agent's prompt changes.

## How to Apply It
1. Define a failing test case representing a user query.
2. Write the expected JSON schema and the evaluation rubric.
3. Write a minimal system prompt and attach minimal tools.
4. Run the test; observe the failure (e.g., wrong tool called, poor reasoning).
5. Refine the prompt, add few-shot examples, or adjust the tool description until the test passes.
6. Refactor the prompt for token efficiency, ensuring the test remains green.

## Agentic Patterns & Ready-to-Use Examples

**Agentic TDD Flow (Pytest + LLM Judge)**
```python
import pytest
from your_agent_framework import execute_agent
from evaluators import llm_judge

# 1. The Test (Written First)
def test_refund_agent_policy_enforcement():
    user_query = "I want a refund for my socks bought 45 days ago."
    expected_tool = "reject_refund" # Policy is 30 days

    # Execute agent
    result, trace = execute_agent(user_query)

    # 2. Assert Deterministic Behavior
    called_tools = [action.name for action in trace.actions]
    assert expected_tool in called_tools, "Agent failed to call reject_refund"

    # 3. Assert Qualitative Behavior
    rubric = "Does the agent politely explain the 30-day refund policy?"
    score = llm_judge(rubric, result.response)
    assert score == "PASS"
```

## Common Pitfalls & How to Avoid Them

- **Flaky Tests:** Testing exact string matches on LLM outputs. Fix: Use structured JSON outputs or LLM-as-a-judge for semantic equivalence.
- **Overfitting Prompts:** Tweaking a prompt to pass one test while ignoring the rest. Fix: Always run a full regression suite of 50+ diverse queries.
- **Testing the LLM, Not the Agent:** Writing tests that just verify basic knowledge. Fix: Test the agent's tool selection, orchestration, and constraint adherence.

## Quick Checklist (for self-review or automated eval)

- Is there a clear evaluation rubric defined before the prompt is authored?
- Are deterministic assertions used for tool calls and API executions?
- Is there an automated CI/CD pipeline running agentic evaluations?
- Does the test suite measure token usage and execution latency?

## References

- Evaluating Large Language Models trained on Code (Chen et al., 2021)
- Evaluation-Driven Development for Agentic Systems (Anthropic AI Engineering Guidelines, 2025)
