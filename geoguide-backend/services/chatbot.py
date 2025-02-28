import ollama

def chatbot_response(user_input):
    """
    Handles travel-related queries using Ollama (Llama 2 model).
    """
    try:
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": user_input}])
        return response["message"]["content"]
    except Exception as e:
        return f"Chatbot error: {str(e)}"

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot:", chatbot_response(user_input))
