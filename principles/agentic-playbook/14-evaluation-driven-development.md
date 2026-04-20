---
title: "Evaluation-Driven Development (EDD)"
principle: "EDD"
category: "Agentic"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Evaluation-Driven Development (EDD) – Agentic Instruction Sheet

## What It Is
The continuous integration practice of testing agent updates against a diverse dataset using automated metrics (LLM-as-a-judge, exact match, structural validation) to mathematically prove system improvements and prevent regressions.

## Why It Matters for Agentic Systems
Because LLMs are non-deterministic, a prompt tweak to fix one bug often silently degrades performance in unrelated areas ("whack-a-mole"). Without quantitative evaluation on a golden dataset, you cannot confidently deploy an agent to production.

## Core Rules
- Maintain a "Golden Dataset" of at least 50–100 diverse, version-controlled test cases (inputs and expected outputs/behaviors).
- Use multi-faceted metrics: evaluate not just the final answer, but intermediate tool calls, latency, and token cost.
- Use an LLM-as-a-judge for qualitative metrics (e.g., tone, faithfulness to context, relevance).
- Use deterministic metrics for structural requirements (e.g., JSON schema adherence, specific tool invocation).
- Never merge a prompt or architecture change if the overall evaluation score drops.

## How to Apply It
1. Curate a dataset mapping `user_query` to `expected_trajectory` (which tools to call) and `expected_answer`.
2. Write scoring functions: deterministic checks for tool calls, and LLM-judge prompts for answer quality.
3. Integrate an evaluation framework (e.g., Ragas, DeepEval, LangSmith).
4. Run the evaluation suite locally before committing any changes.
5. Set up CI/CD to run the evaluation suite on every pull request.

## Agentic Patterns & Ready-to-Use Examples

**LLM-as-a-Judge Prompt Template**
```text
You are an impartial judge evaluating an AI Agent's response.
[User Query]: {query}
[Agent Response]: {response}
[Ground Truth Fact]: {truth}

Evaluate if the Agent Response completely answers the User Query based ONLY on the Ground Truth Fact.
Output JSON:
{
  "reasoning": "<step-by-step logic>",
  "score": <0 or 1>
}
```

**Automated Eval Script Example (Python)**
```python
def evaluate_agent_run(run_result, expected_tool):
    score = 0

    # 1. Deterministic check
    if expected_tool in run_result.tools_called:
        score += 0.5

    # 2. LLM-as-a-judge check for hallucination
    judge_result = llm_judge(run_result.response, run_result.context_used)
    if judge_result.is_faithful:
        score += 0.5

    return score # 1.0 is Perfect
```

## Common Pitfalls & How to Avoid Them

- **Judging with the Same Model:** Using the exact same model prompt to evaluate its own output. Fix: Use a different, usually larger model (e.g., Claude 3.5 Sonnet to judge a Haiku agent) or a strict prompt technique.
- **Over-indexing on Final Output:** Only checking the text, missing that the agent burned $2 making 50 redundant API calls. Fix: Evaluate the agent's trajectory (tool call efficiency).
- **Stale Datasets:** Evaluating on tests that no longer reflect real user behavior. Fix: Continuously sample production logs to add new edge cases to the Golden Dataset.

## Quick Checklist (for self-review or automated eval)

- Is there a version-controlled dataset of golden test cases?
- Do evaluations measure both deterministic behavior (tools) and qualitative output (LLM judge)?
- Does the CI/CD pipeline block deployments if evaluation scores drop?
- Are token costs and execution times included in the evaluation metrics?

## References

- Judging LLM-as-a-Judge (Zheng et al., 2023)
- Ragas: Automated Evaluation of Retrieval Augmented Generation (Es et al., 2023)
