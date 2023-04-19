import os
import openai
from colorama import Fore, Back
from dotenv import load_dotenv
from lib.data import write_msgs_to_file, read_msgs_from_file
from lib.chatgpt import ask_chatgpt

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # run loop, taking user input and passing it to ask_chatgpt then pretty printing the ais response
    messages = [
        {"role": "system", "content": "You are a research assistant."}
    ]
    user_input = input("""
        Would you like to load messages from \"chatlog.txt\"? 
        Please enter Y for yes or anything else for no.\n
    """)
    if user_input != "Y":
        print(Fore.RED + "Not loading messages from \"chatlog.txt\"\n")
    else:
        print(Fore.GREEN + "Loading messages from \"chatlog.txt\"\n")
        messages = read_msgs_from_file("chatlog.txt")

    messages = ask_chatgpt(messages, "Introduce yourself.")
    while True:
        user_input = input(Fore.BLUE + "> ")
        if user_input.lower() == "exit" or "":
            print(Back.RED + "Exiting...")
            write_msgs_to_file(messages, "chatlog.txt")
            break
        
        messages = ask_chatgpt(messages, user_input)
