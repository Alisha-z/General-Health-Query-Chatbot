from openai import OpenAI

# Step 1: Create the client with your API key
client = OpenAI(api_key="paste your API key here")  # Replace with your real key

# Step 2: Define chatbot function
def ask_health_bot(question):
    prompt = (
        "You are a friendly and careful medical assistant. "
        "You can answer general health questions, but NEVER give personal medical advice. "
        "Always suggest seeing a real doctor for serious concerns.\n"
        f"Question: {question}\n"
        "Answer:"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=150
    )

    return response.choices[0].message.content

# Step 3: Chat loop
while True:
    user_input = input("Ask a health question (or type 'exit'): ")
    if user_input.lower() == "exit":
        print("👋 Goodbye! Stay healthy!")
        break
    answer = ask_health_bot(user_input)
    print("\n🤖 Assistant:", answer)
    print("-" * 40)


