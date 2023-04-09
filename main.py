import os
import openai
from utils.request import chat_complete


if __name__ == "__main__":
    # Create a new chat completion
    openai.api_key = os.getenv("OPENAI_API_KEY")
    message = "Hello, how are you?"
    response = chat_complete(message)
    print(response)