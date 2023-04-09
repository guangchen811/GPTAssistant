import os
import openai
import sqlite3
from utils.request import chat_complete
from utils.writeDB import connect_db, write_db, process_database_requests


if __name__ == "__main__":
    # Create a new chat completion
    openai.api_key = os.getenv("OPENAI_API_KEY")
    conn = connect_db('DB/TextDatabase.db')
    message_history = [
        {"role": "system", "content": 
"""You are a personal assistant. Your responsibility is to answer questions and help the user with their tasks. You have access to your own memory, called Personal Storage Database (PSDB), which is a sqlite3 database created using the command: `CREATE TABLE messages (name, content)`. You can perform the following actions:

1. Save information in the PSDB using the format `database save: INSERT INTO messages VALUES ('name', 'content')`
2. Retrieve information from the PSDB using the format `database requrest: <sql request>`

When responding to a user's request, please structure your response as follows:

`response to use: <answer> [must be the first line]
[if necessary]database requrest: <sql request>
[if necessary]database save: <sql request>`

You don't need to include SQL requests if they're not necessary. Here are some examples:

1. User: 'My favorite color is red. Please remember it.'
Your response: 'Your favorite color has been recorded.\ndatabase save: INSERT INTO messages VALUES ('color', 'red')'

2. User: 'What is my favorite color? Check in PSDB.'
Your response: 'I'll send a request to the database to find out.\ndatabase requrest: SELECT content FROM messages WHERE name = 'color''

Keep in mind that this is not your first time using PSDB, so some information about the user might already be stored there. Feel free to use that information to answer the user's questions.
"""
}]

    while True:
        message = input("Enter your message: ")
        if message == "quit":
            print("This is the end of conversation, brief history has been saved.")
            break
        else:
            retry_count = 0
            while retry_count < 3:
                try:
                    response = chat_complete(message, message_history)
                    message_history.append({"role": "user", "content": message})
                    assistant_response = response['choices'][0]['message']['content']
                    print(assistant_response)
                    message_history.append({"role": "assistant", "content": assistant_response})
                    search_results = process_database_requests(assistant_response, conn)
                    if search_results:
                        print("Search results:", search_results)
                    break
                except Exception as e:
                    print("Error:", e)
                    retry_count += 1
                    print("Retrying...")
                
    conn.close()
    print(response)