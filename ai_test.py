import os
from gpt4all import GPT4All
from pathlib import Path

choice = 2
inputfile = input("Input>: ")
output = input("Output>: ")
main()

def clear_console():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def chat_with_ai(model):
    """Start a chat session with the AI model."""
    context= "You tell funny jokes"

    with model.chat_session():
        user_input = open(inputfile, 'r')
        user_input = user_input.read()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the chat. Goodbye!")

        full_input = f"{context}\n:User  {user_input}\nAI:"

        print("\nPulling...", end='', flush=True)

        try:
            response = ""
            for token in model.generate(full_input, streaming=True, max_tokens=327670000):
                response += token

                if 'quitsirsur' in response.lower():
                    print("\nAI: Done!")
                    exit()
                elif 'blocksirsur' in response.lower():
                    with open("stat.dat", 'w') as ror:
                        ror.write("Blocked")
                    os.system("cls||clear")
                    print("The bot blocked you.")
                    exit()
                with open(output, 'a') as f:
                    f.write(token + '')
                    f.flush()
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

