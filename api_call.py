import openai

# Set your OpenAI API key
openai.api_key = "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"

def get_recipe_suggestions(user_message):
    # Create a conversation with the system message as a cooking assistant and the user message
    conversation = [
        {"role": "system", "content": "You are a cooking assistant."},
        {"role": "user", "content": user_message},
    ]

    # Generate a response from the assistant
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract and return the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

# Example usage




