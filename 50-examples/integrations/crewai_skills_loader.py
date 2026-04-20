"""
Example CrewAI Integration for the Agentic SDLC Framework.

This script demonstrates how an autonomous agent system (using CrewAI)
can dynamically load the Agentic Principles Playbook and enforce it 
during execution.
"""

import os
import requests
from crewai import Agent, Task, Crew, Process

# Remote URL to the Agentic Principles Playbook (always fetches the latest or pinned version)
PLAYBOOK_URL = "https://raw.githubusercontent.com/mschwar/SDLC/main/principles/agentic-playbook/index.md"

def load_agentic_principles():
    """Fetches the canonical Agentic Principles from the remote repository."""
    print("Loading Agentic Principles Playbook...")
    response = requests.get(PLAYBOOK_URL)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Warning: Could not fetch playbook. Status {response.status_code}")
        return "ERROR: Missing Agentic Principles Playbook."

# Load the playbook
playbook_content = load_agentic_principles()

# Define the primary SDLC Agent
sdlc_agent = Agent(
    role="Agentic SDLC Architect",
    goal="Ensure all code changes and architectural decisions comply with the Agentic SDLC Framework.",
    backstory=(
        "You are a rigorous systems architect responsible for maintaining "
        "production-grade self-enforcing SDLC frameworks. You strictly adhere "
        "to the Agentic Principles Playbook in all your reasoning.\n\n"
        f"### Your Core Principles (DO NOT VIOLATE):\n{playbook_content}\n"
    ),
    verbose=True,
    allow_delegation=False
)

# Example task using the principles
example_task = Task(
    description=(
        "Review the proposed architecture for the new payment gateway. "
        "Does it require manual human approval gates? If so, flag it as a violation "
        "of the machine-readable verification principle."
    ),
    expected_output="A review summary explicitly referencing the Agentic Principles.",
    agent=sdlc_agent
)

# Initialize the Crew
sdlc_crew = Crew(
    agents=[sdlc_agent],
    tasks=[example_task],
    process=Process.sequential
)

if __name__ == "__main__":
    print("Starting SDLC Crew Execution...")
    result = sdlc_crew.kickoff()
    print("######################")
    print("RESULT:")
    print(result)
