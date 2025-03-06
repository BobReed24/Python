import os
from gpt4all import GPT4All
from pathlib import Path

def clear_console():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def chat_with_ai(model):
    """Start a chat session with the AI model."""
    with model.chat_session():
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the chat. Goodbye!")
                break

            print("AI: ", end='', flush=True)
            try:
                for token in model.generate(user_input, streaming=True):
                    print(token, end='', flush=True)
                print()  
            except Exception as e:
                print(f"\nError: {e}")

def main():
    """Main function to run the chat application."""
    model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf", device="cuda")
    clear_console()
    chat_with_ai(model)

if __name__ == "__main__":
    main()
