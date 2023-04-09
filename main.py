import os
import openai
import sqlite3
from utils.request import chat_complete
from utils.writeDB import connect_db, write_db


if __name__ == "__main__":
    # Create a new chat completion
    openai.api_key = os.getenv("OPENAI_API_KEY")
    conn = connect_db('DB/TextDatabase.db')
    while True:
        message = input("Enter your message: ")
        if message == "quit":
            print("This is the end of conversation, brief history has been saved.")
            break
        else:
            response = chat_complete(message)
            print(response['choices'][0]['message']['content'])
            # write_db(conn, name, content)
    conn.close()
    print(response)