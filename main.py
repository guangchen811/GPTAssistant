import os
import openai
import sqlite3
from utils.request import chat_complete
from utils.writeDB import connect_db, write_db, process_database_requests


if __name__ == "__main__":
    # Create a new chat completion
    openai.api_key = os.getenv("OPENAI_API_KEY")
    conn = connect_db('DB/TextDatabase.db')
    base_instruction = open("prompts/base_instruction.txt", "r").read()
    
    message_history = [
        {"role": "system", "content": base_instruction}]

    while True:
        message = input("Enter your message: ")
        if message == "quit":
            print("This is the end of conversation, brief history has been saved.")
            break
        else:
            retry_count = 0
            while retry_count < 3:
                try:
                    response = chat_complete(message, message_history, "user")
                    message_history.append({"role": "user", "content": message})
                    assistant_response = response['choices'][0]['message']['content']
                    search_results, save_flag, request_flag = process_database_requests(assistant_response, conn)
                    message_history.append({"role": "assistant", "content": assistant_response})
                    if save_flag:
                        save_message = "Database updated. now you can tell the user about it."
                        response_save = chat_complete(save_message, message_history, "system")['choices'][0]['message']['content']
                        message_history.append({"role": "system", "content": save_message})
                        message_history.append({"role": "assistant", "content": response_save})
                        print(response_save)
                    elif request_flag:
                        request_message = "the command has been executed, here are the results: {}".format(search_results)
                        request_response = chat_complete(request_message, message_history, "system")['choices'][0]['message']['content']
                        message_history.append({"role": "system", "content": request_message})
                        message_history.append({"role": "assistant", "content": request_response})
                        print(request_response)
                    else:
                        print(assistant_response)
                    break
                except Exception as e:
                    print("Error:", e)
                    retry_count += 1
                    print("Retrying...")
                
    conn.close()
    print(response)