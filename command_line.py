import os
def start():
    os.system('cls||clear')
    main()
def main():
    try:
        while True:
            try:
                cur_dir = os.getcwd()
                res = input(f"{cur_dir} (python) % ")
                if "cd" in res:
                    res = res.replace("cd ", "")
                    os.chdir(res)
                else:
                    os.system(res)
            except (SyntaxError, NameError, TypeError, ValueError) as e:
                print(f"Err: {e}")
    except KeyboardInterrupt:
        print("")
        main()
start()
