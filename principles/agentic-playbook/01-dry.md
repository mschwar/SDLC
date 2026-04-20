---
title: "DRY – Don't Repeat Yourself"
principle: "DRY"
category: "Foundational"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# DRY – Don't Repeat Yourself – Agentic Instruction Sheet

## What It Is
Every piece of knowledge, tool logic, or prompt constraint must have a single, unambiguous, authoritative representation within the multi-agent system.

## Why It Matters for Agentic Systems
In non-deterministic workflows, redundant instructions confuse LLMs and increase token costs. If a safety constraint or API schema changes and is duplicated across multiple agent prompts, missed updates lead to hallucinated arguments, schema validation failures, and unpredictable trajectory drift.

## Core Rules
- Extract shared context (e.g., company tone, global constraints) into a centralized `BaseSystemPrompt` repository.
- Define tool schemas exactly once using Pydantic, allowing automatic translation to OpenAPI/JSON Schema for LLM consumption.
- Consolidate redundant state-management logic into a single Graph Reducer or Memory node.
- Never copy-paste identical ReAct loop logic; use standard orchestration frameworks.
- Maintain a single source of truth for dynamic context (e.g., a shared vector store or global State object) rather than passing identical strings manually.

## How to Apply It
1. Identify overlapping responsibilities across agents (e.g., both Researcher and Writer agents have formatting rules).
2. Extract the common rules into a shared `config` or global state.
3. Define tools using typed data models (e.g., Pydantic) and inherit them where needed.
4. Dynamically inject the shared context into agent prompts at runtime using string formatting or template engines.
5. Store execution memory in a centralized graph state rather than local agent memory arrays.

## Agentic Patterns & Ready-to-Use Examples

**Centralized Tool Registry (Python)**
```python
from pydantic import BaseModel, Field
from typing import Type

class BaseTool(BaseModel):
    """Single source of truth for tool definitions."""
    name: str
    description: str
    schema_cls: Type[BaseModel]

    def to_openai_schema(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.schema_cls.model_json_schema()
            }
        }
```

**Dynamic Prompt Injection**
```python
GLOBAL_CONSTRAINTS = """
- Always output valid JSON.
- Never access real user PII.
- Format dates as ISO-8601.
"""

def build_agent_prompt(role: str, task: str) -> str:
    return f"""Role: {role}\nTask: {task}\n\nGlobal Constraints:\n{GLOBAL_CONSTRAINTS}"""
```

## Common Pitfalls & How to Avoid Them

- **Prompt Bloat:** Copying global rules into every local prompt. Fix: Use a context builder function that prepends global rules.
- **Divergent Tool Schemas:** Manually typing JSON schemas for OpenAI while using Pydantic for internal logic. Fix: Autogenerate LLM schemas directly from the Pydantic models.
- **State Duplication:** Passing the full conversation history to an agent that only needs the last summary. Fix: Use a shared Graph State with a reducer.

## Quick Checklist (for self-review or automated eval)

- Are tool JSON schemas generated dynamically from source code rather than hardcoded?
- Is the conversation history stored in exactly one central state object?
- Are global guardrails and constraints defined in a single configuration file or string?
- Do multiple agents share the exact same prompt instructions without a base template?

## References

- The Pragmatic Programmer: Your Journey to Mastery (Thomas & Hunt, 20th Anniversary Edition)
- LangGraph State Management Best Practices (2025)
