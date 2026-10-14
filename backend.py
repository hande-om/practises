import ollama

MODEL_NAME = "llama3.2"  # Ensure you pulled this model via 'ollama pull llama3.2'

def ask_ollama(question):
    # 1. Store the API result into the 'response' variable
    # 2. Use 'messages' (plural) instead of 'message'
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ]
    )

    # 3. Extract the text correctly using dictionary keys
    return response["message"]["content"]
