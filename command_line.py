import os
def start():
    os.system('cls||clear')
    main()
def main():
    try:
        try:
            while True:
                cur_dir = os.getcwd()
                try:
                    res = input(f"{cur_dir} (python) $ ")
                    if "cd" in res:
                        res = res.replace("cd ", "")
                        os.chdir(res)
                    else:
                        os.system(res)
                except (ValueError, TypeError, SyntaxError, NameError) as e:
                    print(f"Err: {e}")
        except KeyboardInterrupt:
            print()
            main()
    except EOFError:
        os.system('cls||clear')
start()
