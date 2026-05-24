from openai import OpenAI

# Connect to LM Studio local server
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # LM Studio doesn't need a real key
)

# Send your first message to the AI
response = client.chat.completions.create(
    model="google/gemma-4-e4b",
    messages=[
        {"role": "user", "content": "Explain what an AI agent is in 3 simple sentences."}
    ]
)

# Print the response
print(response.choices[0].message.content)