
from common import decide

message = (
    "Our checkout is down worldwide "
    "and customers cannot place orders."
)

questions = [
    {
        "name": "business_impact",
        "type": "score",
        "instructions": (
            "Rate the business impact of the incident. "
            "Low means a minor cosmetic issue. "
            "Moderate means limited users are affected. "
            "High means a major feature is affected. "
            "Critical means a widespread outage."
        ),
        "levels": [
            {"label": "low"},
            {"label": "moderate"},
            {"label": "high"},
            {"label": "critical"}
        ]
    }
]

print("Incident:", message)
decide(message, questions)

