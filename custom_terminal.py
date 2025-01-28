import os
import json
import subprocess
from termcolor import colored

def start():
    global green
    green = "green"
    os.system("cls||clear")
    print("Initializing")
    ls_output=subprocess.Popen(["sudo", "apt-get", "-y", "install", "nvtop"])
    ls_output.communicate()
    os.system("cls||clear")
    main()

def main():
    try:
        while True:
            cur_dir = os.getcwd()
            print(colored(f"{cur_dir} ", green) + "(python) $ ", end="")

            syscmd = input("").lower()
            command_parts = syscmd.split()  
            command = command_parts[0]  

            if command == "cd":
                if len(command_parts) > 1:
                    os.chdir(command_parts[1])
                else:
                    print("Err: No directory specified")
            elif command == "peek":
                if len(command_parts) > 1:
                    os.system(f"ls {command_parts[1]}")
                else:
                    os.system("ls")
            elif command == "branch":
                if len(command_parts) > 1:
                    os.system(f"ls {command_parts[1]}/*")
                else:
                    print("Err: No argument specified")
            elif command == "tree":
                os.system("ls *")
            elif command == "task":
                if len(command_parts) > 1 and command_parts[1] == "--show":
                    os.system(f"ps aux | grep {" ".join(command_parts[2:])}")
                elif len(command_parts) > 1 and command_parts[1] == "-s":
                    os.system(f"ps aux | grep {" ".join(command_parts[2:])}")
                else:
                    print("Err: Incorrect arguments")
            elif command == "admin":
                osname = os.name
                if osname == "nt":
                    print("Err: Command not available for Windows")
                elif len(command_parts) > 1 and command_parts[1] == "install":
                    os.system(f"sudo apt install -y {" ".join(command_parts[2:])}")
                elif len(command_parts) > 1 and command_parts[1] == "ubuntu":
                    os.system(f"sudo {" ".join(command_parts[2:])}")
                else:
                    print("Err: Incorrect arguments")
            elif command == "lib.use":
                os.system(f"{" ".join(command_parts[1:])}")
            elif command == "create":
                if len(command_parts) > 1:
                    if command_parts[1] in ["--directory", "-d"]:
                        os.system(f"mkdir {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--file", "-f"]:
                        os.system(f"nano {" ".join(command_parts[2:])}")
                    else:
                        print("Err: Incorrect arguments")
                else:
                    print("Err: No argument specified")
            elif command == "remove":
                if len(command_parts) > 1:
                    if command_parts[1] in ["--directory", "-d"]:
                        os.system(f"rm -r -d -f {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--file", "-f"]:
                        os.system(f"rm {" ".join(command_parts[2:])}")
                    else:
                        print("Err: Incorrect arguments")
                else:
                    print("Err: No argument specified")
            elif command == "read":
                if len(command_parts) > 1:
                    os.system(f"cat {" ".join(command_parts[1:])}")
                else:
                    print("Err: No file specified")
            elif command == "modify":
                if len(command_parts) > 1:
                    if command_parts[1] in ["--editfile", "-ef"]:
                        os.system(f"nano {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--copyfile", "-cf"]:
                        os.system(f"cp {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--copydir", "-cd"]:
                        os.system(f"cp -r {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--movefile", "-mf"]:
                        os.system(f"mv {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--movedir", "-md"]:
                        os.system(f"mv {" ".join(command_parts[2:])}")
                    else:
                        print("Err: Incorrect arguments")
                else:
                    print("Err: No argument specified")
            elif command in ["python", "py"]:
                startpy()
            elif command == "bash":
                if len(command_parts) > 1:
                    os.system(f"bash {" ".join(command_parts[1:])}")
                else:
                    print("Err: No script specified")
            elif command.startswith("./"):
                os.system(f"bash {" ".join(command_parts)}")
            elif command == "output":
                if len(command_parts) > 1:
                    os.system(f"echo {" ".join(command_parts[1:])}")
                else:
                    print("Err: String not specified")
            elif command == "kill":
                if len(command_parts) > 1:
                    if command_parts[1] in ["--all", "-a"]:
                        os.system(f"pkill -f {" ".join(command_parts[2:])}")
                    elif command_parts[1] in ["--specific", "-s"]:
                        os.system(f"kill {" ".join(command_parts[2:])}")
                    else:
                        print("Err: Incorrect arguments")
                else:
                    print("Err: No argument specified")
            elif command.startswith("get."):
                arg = command[4:].strip()  

                if arg in ["cwd"]:
                    os.system("pwd")
                elif arg in ["rds"]:
                    os.system("df -h")
                elif arg in ["cpu"]:
                    os.system("lscpu")
                elif arg in ["ram"]:
                    os.system("watch -n 5 free -m")
                elif arg in ["gpu"]:
                    os.system("nvtop")
                elif arg in ["usr --current", "usr -c"]:
                    os.system("whoami")
                elif arg in ["usr --all", "-a"]:
                    os.system("cut -d: -f1 /etc/passwd")
                else:
                    print("Err: Incorrect argument")
            else:
                print(f"Err: Command '{command}' not found")
    except (FileNotFoundError, FileExistsError, NameError) as e:
        print(f"Err: {e}")
        main()
    except KeyboardInterrupt:
        print("")
        main()

def startpy():
    os.system("python")

start()
