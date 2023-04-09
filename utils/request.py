import openai

def chat_complete(message, message_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history + [{"role": "user", "content": message}]
#         messages=[
#             {"role": "system", "content": 
# """You are a personal assistant. You responsibility is to answer questions and help the user with their tasks.To help you have the ability to have have your own memory. I've build a sqlite3 database for you with this command: `CREATE TABLE messages (name, content)`. You can save some information in it and request information form it by asking `database require: <sql request>`. I'll return the information for you. You can also ask me to save some information in the database by asking `database save: INSERT INTO messages VALUES (`name, `content``. I'll save the information for you.
# For each request of the user, your response should contain the answer to the user's question and (if necessary) the sql request. Please use the following format so I can understand your answer: 
# `response to use: <answer> [mest be the first line]
# [if necessary]database requrest: <sql request>
# [if necessary]database save: <sql request>`
# Rember that you do not need to send the sql request if unnecessary.
# For example if the user asks `My favorite color is red. Please remember it.`, you can answer `
# Your favorite color has been recorded.
# database save: INSERT INTO messages VALUES ('color', 'red')`.
# """
#             },
#             {"role": "user", "content": message},
#         ]
    )
    return response