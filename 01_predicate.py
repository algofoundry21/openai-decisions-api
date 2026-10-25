from common import decide

message = "I cannot sign in to my account."
questions = [{
    "name": "active_outage",
    "type": "predicate",
    "instructions": "Does this message report an active, widespread production outage?"
}]
print("Customer message:", message)
decide(message, questions)