import os
from gpt4all import GPT4All
from pathlib import Path

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def chat_with_ai(model):
    with model.chat_session():
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the chat. Goodbye!")
                break

            print("AI: ", end='', flush=True)
            try:
                for token in model.generate(user_input, max_tokens=8096, streaming=True):
                    print(token, end='', flush=True)
                print()  
            except Exception as e:
                print(f"\nError: {e}")

def main():
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device="gpu")
    clear_console()
    chat_with_ai(model)

if __name__ == "__main__":
    main()
