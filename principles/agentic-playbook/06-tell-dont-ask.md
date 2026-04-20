---
title: "Tell, Don't Ask (TDA)"
principle: "Tell Don't Ask"
category: "Timeless"
version: "2026-04"
tags: [agentic, principles, playbook]
---

# Tell, Don't Ask (TDA) – Agentic Instruction Sheet

## What It Is
Inject necessary context and explicit commands directly into the agent's state or prompt (Tell), rather than requiring the agent to autonomously fetch basic context via tools (Ask).

## Why It Matters for Agentic Systems
Every tool call an agent makes introduces latency, token costs, and a non-zero probability of failure or hallucination. By proactively fetching data in deterministic code and injecting it into the prompt, you eliminate unnecessary LLM reasoning steps and stabilize the workflow.

## Core Rules
- Do not give the agent a `get_user_profile` tool if you already know the user ID; fetch it in backend code and inject it.
- Pass explicit state directives to the agent (e.g., "The current date is X", "The user's role is Y").
- Use deterministic routing for known intents rather than asking the LLM "Which agent should handle this?" when a simple regex or classifier would work.
- Only use "Ask" (tools) for dynamic exploration where the required information cannot be known prior to LLM reasoning.

## How to Apply It
1. Review the agent's toolset. Identify tools that fetch static or predictable context.
2. Remove those tools from the LLM.
3. Write deterministic code to fetch that data *before* invoking the LLM.
4. Format the fetched data into the system prompt or the initial user message.
5. Reserve tool calling strictly for iterative, multi-step discovery (e.g., searching the web based on a generated hypothesis).

## Agentic Patterns & Ready-to-Use Examples

*Bad (Violates TDA): The agent must Ask.*
```python
# System Prompt: "You are a support agent. Use the get_user_data tool to find out who you are talking to."
tools = [get_user_data, get_order_status, refund_item]
response = agent.invoke("Where is my order?", tools=tools)
# Latency: 2 round trips (fetch user -> fetch order)
```

*Good (Applies TDA): The system Tells.*
```python
# Deterministic pre-fetch
user_data = db.get_user(session.user_id)
order_history = db.get_recent_orders(session.user_id)

# System Prompt dynamically injected
system_message = f"""
You are a support agent talking to {user_data.name}.
Their recent orders are: {order_history}.
Answer their query based on this context.
"""
tools = [refund_item] # Only strictly necessary action tools
response = agent.invoke(system_message + "\nUser: Where is my order?", tools=tools)
# Latency: 1 round trip. Zero chance of failing to fetch user data.
```

## Common Pitfalls & How to Avoid Them

- **Context Starvation:** Forcing the agent to discover basic facts about the environment. Fix: Pre-populate the Graph State with environment variables (time, user info).
- **Over-Reliance on RAG Tools:** Making the agent search for standard operating procedures. Fix: Pre-inject the specific SOP into the system prompt if the intent is known.
- **Infinite Fetch Loops:** The agent calls a fetch tool, gets partial data, calls it again, and gets stuck. Fix: Inject comprehensive context upfront.

## Quick Checklist (for self-review or automated eval)

- Are all predictable, static variables injected directly into the prompt?
- Have you removed "read-only" tools that fetch data easily accessible by the backend before execution?
- Does the agent only use tools for dynamic, unpredictable information retrieval?
- Is the current state/context explicitly declared at the start of the LLM interaction?

## References

- Object-Oriented Software Engineering (Ivar Jacobson)
- Optimizing LLM Latency through Context Pre-fetching (2025 Architectural Patterns)
