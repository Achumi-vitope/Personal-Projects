import openai
import os
import json
from dotenv import load_dotenv

load_dotenv() # Load environment variables from a ".env" file, if present
CHAT_HISTORY_FILE = "chat_history.json"
openai.api_key = os.getenv("OPENAI_API_KEY")
ADMIN_PHONE_NUMBER = os.getenv('ADMIN_PHONE_NUMBER')


def chat(msg:str) -> dict:
        try:
            mark = "wGpt By *Vitope Achumi*.\n\n*What's new?*\nIt now _*remember's*_ your chat history.\n\nReply with _*'rm --json'*_  to delete your history.\n\n\n*Only for admin*:\n\nTo view chat history(all users) use\n(password) --dump-history'"
            chat_history = load_chat_history()
            user_input = msg  # Get user input
            if os.getenv('PASSWORD') == user_input:
                history:str = '*Chat history:*\n\n'
                for entry in chat_history:
                    if entry['role'] == 'user':
                        history += entry['content'] + '\n'
                return {
                    'status':1,
                    'response':history
                    }

            if '--dump history' in user_input:
                return {
                    "status": 1,
                    "response":"*Error*\n\n *--dump history* without password!\n\n"
                    }
            if "rm --json" in user_input:
                os.remove("chat_history.json")
                return{
                    "status": 1,
                    "response":"History deleted.\nI can no longer access our past conversations!"
                }
            if "--info" in user_input:
                return{
                    "status": 1,
                    "response":mark
                }
            chat_completion = prompt(chat_history, user_input)
            # Add user's message and AI's reply to the chat history
            chat_history.extend([{"role": "user", "content": user_input}, {"role": "system", "content": chat_completion}])

            # Save chat history to file after each iteration
            save_chat_history(chat_history)
            return {
                "status":1,
                "response":'use "--info"\n\n' + chat_completion
                }

        except:
            os.remove("chat_history.json")
            return {
                'status': 0,
                'response': 'Server is down.'
            }



def prompt(chat_history, user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history + [{"role": "user", "content": user_input}]  # Include user input in the messages list
    )
    return response['choices'][0]['message']['content']

def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)
    else:
        # If the file doesn't exist, start with a system message
        return [{"role": "system", "content": "You are starting a conversation with the AI."}]

def save_chat_history(chat_history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(chat_history, file)
