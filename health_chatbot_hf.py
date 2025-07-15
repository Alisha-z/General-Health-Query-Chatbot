from transformers import pipeline

# Load chatbot from Hugging Face
chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    tokenizer="mistralai/Mistral-7B-Instruct-v0.1",
    revision="main",
    trust_remote_code=True,
    device_map="auto"  # Will run on CPU or GPU automatically
)

def ask_health_bot(question):
    prompt = (
        "You are a helpful and friendly medical assistant. "
        "You do not give serious medical advice. For any health emergency, tell the user to visit a doctor.\n\n"
        f"User: {question}\n"
        "Assistant:"
    )

    response = chatbot(prompt, max_new_tokens=200, do_sample=True)[0]["generated_text"]

    # Extract only the assistant's reply
    answer = response.split("Assistant:")[-1].strip()
    return answer

# Simple chat loop
while True:
    user_input = input("Ask a health question (or type 'exit'): ")
    if user_input.lower() == "exit":
        print("👋 Stay safe! Goodbye!")
        break
    answer = ask_health_bot(user_input)
    print("\n🤖 Assistant:", answer)
    print("-" * 40)
