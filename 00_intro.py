
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MESSAGE = (
    "Our dashboard shows a blank screen after login."
)

def main():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        timeout=30.0
    )

    print("\nCUSTOMER MESSAGE:")
    print(MESSAGE)

    response = client.decisions.create(
        model="gpt-6-luna",
        input=MESSAGE,
        questions=[
            {
                "name": "department",
                "type": "choice",
                "instructions": (
                    "Select the first support team best "
                    "suited to this customer message."
                ),
                "choices": [
                    {"value": "billing"},
                    {"value": "technical"},
                    {"value": "sales"},
                    {"value": "general"}
                ]
            }
        ]
    )

    print("\nDECISION RESPONSE:")
    print(response.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

