import openai

def chat_complete(message, message_history, role):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history + [{"role": role, "content": message}],
        temperature=0.1,
    )
    return response