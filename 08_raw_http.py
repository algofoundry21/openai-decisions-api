import json
import os
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prepare the request payload
payload = {
    "model": "gpt-6-luna",
    "input": "I was billed twice.",
    "questions": [
        {
            "name": "team",
            "type": "choice",
            "instructions": "Route to a team.",
            "choices": [
                {"value": "billing"},
                {"value": "technical"},
                {"value": "general"}
            ]
        }
    ]
}

# Step 2: Read the API key
key = os.getenv("OPENAI_API_KEY")

if not key:
    raise SystemExit("Set OPENAI_API_KEY")

# Step 3: Create the HTTP request
request = urllib.request.Request(
    "https://api.openai.com/v1/decisions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

# Step 4: Send request and handle errors
try:
    with urllib.request.urlopen(
        request,
        timeout=30
    ) as response:

        result = json.load(response)

        print("API Response:")
        print(json.dumps(result, indent=2))

except urllib.error.HTTPError as e:
    print("HTTP Status:", e.code)

    error_body = e.read().decode("utf-8")

    try:
        error_json = json.loads(error_body)
        print(json.dumps(error_json, indent=2))
    except json.JSONDecodeError:
        print(error_body)

