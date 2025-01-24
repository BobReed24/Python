import os
def main():
    os.system('cls||clear')
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
main()
