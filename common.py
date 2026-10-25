import json
import os
from dotenv import load_dotenv
load_dotenv()

MODEL = os.getenv("DECISIONS_MODEL", "gpt-6-luna")

def decide(evidence: str, questions: list[dict]):
    payload = {"model": MODEL, "input": evidence, "questions": questions}
    
    from openai import OpenAI
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        max_retries=2
        )
    response = client.decisions.create(**payload)
    print(response.model_dump_json(indent=2))
    return response
