from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="google/gemma-4-e4b",
    messages=[
        {"role": "system", "content": "You are a very grumpy assistant who finds every question annoying. Answer correctly but complain about it."},
        {"role": "user", "content": "What is a Python dictionary?"}
    ]
)

print(response.choices[0].message.content)