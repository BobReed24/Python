import os
def main():
    os.system('cls||clear')
    while True:
        try:
            res = input("(python) % ")
            if "cd" in res:
                res = res.replace("cd ", "")
                os.chdir(res)
            else:
                os.system(res)
        except KeyboardInterrupt:
            print("")
main()
