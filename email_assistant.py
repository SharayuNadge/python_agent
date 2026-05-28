from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

# Your system prompt - you wrote the logic, I just enhanced it slightly
messages = [
    {"role": "system", "content": "You are a professional email writing assistant. Take the user request and compose a professional email keeping it precise. Mention key points in bullets and keep paragraphs concise. Always include a subject line. When the user asks for revisions, modify the previous draft accordingly."}
]

print("=== Email Drafting Assistant ===")
print("Describe the email you need, or ask for revisions.")
print("Type 'quit' to exit.\n")

while True:
    # Get user request
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    print("\nAI: ", end="", flush=True)

    # Stream the response
    stream = client.chat.completions.create(
        model="google/gemma-4-e4b",
        messages=messages,
        stream=True
    )

    # Collect full reply while streaming
    full_reply = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)
            full_reply += text

    # Add complete AI reply to history
    messages.append({"role": "assistant", "content": full_reply})

    print("\n")