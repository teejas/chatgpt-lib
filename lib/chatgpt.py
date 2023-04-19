import openai
from colorama import Fore

def create_new_msg(msgs: list, msg: str, role: str):
    msgs.append({
        "role": role, "content": msg
    })
    return msgs

def create_new_user_msg(msgs: list, msg: str):
    return create_new_msg(msgs, msg, "user")

def create_new_system_msg(msgs: list, msg: str):
    return create_new_msg(msgs, msg, "system")

def ask_chatgpt(msgs: list, msg: str) -> list:
    messages = create_new_user_msg(msgs, msg)
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        message = response.choices[0]['message']
        messages.append(message)
        print(Fore.GREEN + message.content + "\n")
        return messages
    except:
        print("OPENAI API: Error using ChatCompletion")
    return msgs