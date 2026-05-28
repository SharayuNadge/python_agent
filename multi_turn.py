from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

# This list is our conversation history - starts with just system prompt
messages = [
    {"role": "system", "content": "You are a helpful assistant who remembers everything said in the conversation."}
]

print("Chat started! Type 'quit' to exit.\n")

# Keep chatting until user types quit
while True:
    # Get input from user
    user_input = input("You: ")
    
    # Exit if user types quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    # Send full history to AI
    response = client.chat.completions.create(
        model="google/gemma-4-e4b",
        messages=messages
    )
    
    # Get AI reply
    ai_reply = response.choices[0].message.content
    
    # Add AI reply to history
    messages.append({"role": "assistant", "content": ai_reply})
    
    # Print AI reply
    print(f"\nAI: {ai_reply}\n")