
from common import decide

questions = [
    {
        "name": "team",
        "type": "choice",
        "instructions": "Choose the first support team.",
        "choices": [
            {"value": "billing"},
            {"value": "technical"},
            {"value": "sales"},
            {"value": "general"}
        ]
    },
    {
        "name": "outage",
        "type": "predicate",
        "instructions": (
            "Does this report describe an active "
            "widespread outage?"
        )
    },
    {
        "name": "impact",
        "type": "score",
        "instructions": (
            "Rate business impact: "
            "low = minor issue; "
            "moderate = limited users affected; "
            "high = major feature affected; "
            "critical = widespread outage."
        ),
        "levels": [
            {"label": "low"},
            {"label": "moderate"},
            {"label": "high"},
            {"label": "critical"}
        ]
    }
]

messages = [
    "I was charged twice.",
    "Checkout is down for all customers.",
    "Tell me about enterprise plans."
]

for message in messages:
    print("\nMESSAGE:", message)
    decide(message, questions)

