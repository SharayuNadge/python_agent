from openai import OpenAI
import json
from openai import OpenAI, APIConnectionError

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

messages = [
    {"role": "system", "content": """You are a professional email writing assistant.
Always respond with a JSON object only - no extra text, no markdown, no code blocks.
The JSON must have exactly these three fields:
- subject: the email subject line
- body: the full email body
- tone: either 'formal' or 'casual'

Example format:
{
    "subject": "Meeting Request",
    "body": "Dear John...",
    "tone": "formal"
}"""}
]

print("=== Structured Email Assistant ===\n")

user_input = input("Describe the email you need: ")
messages.append({"role": "user", "content": user_input})

# Parse the JSON response
try:
    # Check if JSON has all expected fields
    response = client.chat.completions.create(
        model="google/gemma-4-e4b",
        messages=messages
    )

    raw = response.choices[0].message.content
    email_data = json.loads(raw)
    
    if not all(key in email_data for key in ["subject", "body", "tone"]):
        raise KeyError("Missing fields in JSON response")
    
    print("\n--- SUBJECT ---")
    print(email_data["subject"])
    print("\n--- BODY ---")
    print(email_data["body"])
    print("\n--- TONE ---")
    print(email_data["tone"])

except APIConnectionError:
    print("Cannot connect to LM Studio. Please make sure the server is running!")

except json.JSONDecodeError:
    print("AI returned invalid JSON. Please try again.")
    print("Raw response:", raw)

except KeyError as e:
    print(f"AI response missing expected fields: {e}")
    print("Raw response:", raw)

except Exception as e:
    print(f"Something went wrong: {e}")
    print("Make sure LM Studio is running!")