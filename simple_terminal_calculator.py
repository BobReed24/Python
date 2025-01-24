import os
def start():
    os.system('cls||clear')
    main()
def main():
    try:
        while True:
            try:
                res = float(eval(input(">: ")))
                print(res)
            except (SyntaxError, TypeError, NameError, ValueError) as e:
                print(f"Err: {e}")
    except (KeyboardInterrupt, EOFError):
        os.system('cls||clear')
        print("Program terminated by user.")
start()
