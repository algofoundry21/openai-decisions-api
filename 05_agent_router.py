from common import decide

message = (
    "Summarize the main changes between "
    "these two contract drafts."
)

allowed_agents = {
    "document_agent",
    "research_agent",
    "email_agent",
    "spreadsheet_agent"
}

questions = [{
    "name": "agent",
    "type": "choice",
    "instructions": (
        "Select the best specialist for the initial task. "
        "Do not execute tools."
    ),
    "choices": [
        {"value": agent}
        for agent in sorted(allowed_agents)
    ]
}]

response = decide(message, questions)