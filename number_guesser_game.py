import random
import os

def main:
    try:
        rang1 = int(input("Enter range 1: "))
        rang2 = int(input("Enter range 2: "))
    except ValueError:
        print("Enter a number and not a letter dipshit!")
    
    secret = random.randrange(rang1, rang2)
    
    while True:
        count += 1
        try:
            guess = int(input("Guess the secret: ")
        except ValueError:
            print("Enter a number and not a letter dipshit!")
        if guess != secret:
            print("Try again!")
        else:
            again = input(f"You got it in {count} tries! Try again? (yes/no)").lower()
            if again == "no":
                print("Ok. Goodbye!")
                os.system("cls||clear")
            if again == "yes":
                os.system("cls||clear")
            else:
                print("The hell?")
                break
main()
            