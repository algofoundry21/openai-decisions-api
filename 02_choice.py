
from common import decide

message = "I was charged twice for my monthly subscription."

questions = [
    {
        "name": "support_team",
        "type": "choice",
        "instructions": (
            "Choose the most suitable FIRST team "
            "for this customer request."
        ),
        "choices": [
            {"value": "billing"},
            {"value": "technical"},
            {"value": "sales"},
            {"value": "general"}
        ]
    }
]

print("Customer message:", message)

decide(message, questions)

