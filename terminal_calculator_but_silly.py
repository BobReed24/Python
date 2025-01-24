import time
import os
import sys
import random
def calc():
    try:
        def start():
            dashes2 = "-------------------------------------"
            os.system('cls||clear')
            print(dashes2)
            print(f"Welcome to the evaluation calculator!\nMade by BobReed24\nhttps://github.com/BobReed24\n{dashes2}")
            print("1. Start\n2. Instructions\n3. Exit")
            try:
                op = int(input(">: "))
                if op == 1:
                    main()
                elif op == 2:
                    os.system('cls||clear')
                    print(dashes)
                    print(f"Instructions\n{dashes}\n>: 23-4-2\n17")
                    for remaining in range(5, 0, -1):
                        sys.stdout.write("\r")
                        sys.stdout.write("Instructions clear in {:2d}".format(remaining))
                        sys.stdout.flush()
                        time.sleep(1)
                    start()
                elif op == 3:
                    os.system('cls||clear')
                    print('Program terminated')
                    time.sleep(1)
                    os.system('cls||clear')
                    KeyboardInterrupt
                else:
                    os.system('cls||clear')
                    print("Invalid Choice!")
                    time.sleep(1)
                    idiotic = random.randrange(1, 6)
                    if idiotic == 1:
                        print("Get it right next time!")
                    elif idiotic == 2:
                        print("How do you even get an invalid choice?")
                    elif idiotic == 3:
                        print("You have no rizz!")
                    elif idiotic == 4:
                        print("Bruh, don't get it wrong next time!")
                    elif idiotic == 5 and osname == 'nt':
                        print("The computer chose 5 because it thinks you are stupid.")
                        time.sleep(2)
                        os.system('cls||clear')
                        print("Ok you are safe from the trick because you are on windows.")
                        time.sleep(1.5)
                        calc()
                    elif idiotic == 5 and osname == 'posix':
                        print("The computer chose 5 because it thinks you are stupid.")
                        time.sleep(2)
                        os.system('cls||clear')
                        print("Let me show you what happens now")
                        time.sleep(1.5)
                        os.system('cls||clear')
                        print("In this code\nidiotic = random.randrange(1, 6)\nThe computer chose the number 5")
                        time.sleep(3)
                        print("Now we will go ahead and install ubuntu-desktop")
                        time.sleep(2)
                        os.system('cls||clear')
                        print("Initializing...")
                        time.sleep(1)
                        os.system('cls||clear')
                        print("Initializing..")
                        time.sleep(1)
                        os.system('cls||clear')
                        print("Initializing.")
                        time.sleep(1)
                        os.system('cls||clear')
                        print("Initializing..")
                        time.sleep(1)
                        os.system('cls||clear')
                        print("Initializing...")
                        time.sleep(1)
                        os.system('cls||clear')
                        time.sleep(2)
                        print("\nHere we go!\n")
                        time.sleep(1.5)
                        os.system('cls||clear')
                        time.sleep(1.5)
                        os.system('cls||clear')
                        os.system('sudo apt-get -y install ubuntu-desktop')
                    time.sleep(2)
                    os.system('cls||clear')
                    define()
            except ValueError as e:
                print(f"Err: {e}")
        def define():
            global dashes
            dashes = "------------------------"
            global osname
            osname = os.name
            start()
        def main():
            os.system('cls||clear')
            print(dashes)
            print(f'Evaluation Calculator\n{dashes}\nPress "ctrl+c" to exit the program\n')
            while True:
                try:
                    res = float(eval(input(">: ")))
                    print(res, "\n")
                except (SyntaxError, NameError, TypeError, ValueError) as e:
                    print(f"Err: {e}")
        define()
    except (KeyboardInterrupt, EOFError):
        os.system('cls||clear')
        print("Program terminated by user\n")
        KeyboardInterrupt
calc()
