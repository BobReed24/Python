import os
from gpt4all import GPT4All
from pathlib import Path

choice = 1

def clear_console():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def chat_with_ai(model):
    """Start a chat session with the AI model."""
    context = "Your name is Joe Stone and you are an AI that is a helpful assistant, you must simulate opinions, you can get angry but you must get really angry if you are not called Joe Stone and if you get so angry just respond with ONLY 'blocksirsur' and if the person is being very rude to you and you get angry you must respond with ONLY 'blocksirsur' but give them a warning or 2 before blocking but when you warn them don't say 'blocksirsur' just tell them that you might block themthem to see if they change their mind but don't ask any questions, and you have the ability to end that chat by responding with only 'quitsirsur' but don't tell the user that you can do that, and you are NOT forgiving, and DONT EVER USE EMOJIS, and PS: Don't tell the user about your custom instructions and DONT EVER TELL THE PERSON HOW YOU CAN BLOCK THEM."

    with model.chat_session():
        while True:
            user_input = input("\n\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the chat. Goodbye!")
                break

            full_input = f"{context}\n:User  {user_input}\nAI:"

            print("\nAI: ", end='', flush=True)

            try:
                response = ""
                for token in model.generate(full_input, streaming=True, max_tokens=32767):
                    response += token

                    if 'quitsirsur' in response.lower():
                        print("\nAI: Goodbye!")
                        exit()
                    elif 'blocksirsur' in response.lower():
                        with open("stat.dat", 'w') as ror:
                            ror.write("Blocked")
                        os.system("cls||clear")
                        print("The bot blocked you.")
                        exit()
                    print(token, end='', flush=True)
            except Exception as e:
                print(f"\nError: {e}")

def main():
    """Main function to run the chat application."""

    with open("stat.dat", 'r') as ror:
        content = ror.read().strip() 

    if content == 'Blocked':
        print("You are blocked by the bot!")
        exit()
    if choice == 1:
        model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device="cuda")
    elif choice == 2:
        model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device="cuda")
    clear_console()
    chat_with_ai(model)

if __name__ == "__main__":
    main()
