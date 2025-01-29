import os
import json
import subprocess
import time
from termcolor import colored

def start():
    global green
    green = "green"
    os.system("cls||clear")
    print("Initializing")
    pre_install = f"sudo apt-get -y install nvtop tmux"
    pre_process = subprocess.run(
        pre_install, shell=True, capture_output=True, text=True
    )
    os.system("cls||clear")
    main()

def main():
    try:
        while True:
            cur_dir = os.getcwd()
            print(colored(f"{cur_dir} ", green) + "(python) $ ", end="")
            try:
                syscmd = input("").lower()
            except EOFError:
                os.system("cls||clear")
                print("Program terminated by user")
                break
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
                if len(command_parts) > 1:
                    action = command_parts[1]
                    args = command_parts[2:]

                    if action == "install":
                        if not args:
                            print("Err: No package specified.")
                        else:
                            for pkg in args:
                                if is_installed(pkg):
                                    print(f"{pkg} is already installed.")
                                elif not package_exists(pkg):
                                    print(f"Err: {pkg} does not exist in the repository.")
                                else:
                                    print(f"Installing {pkg}...")
                                    install_cmd = f"sudo apt-get -y install {pkg}"
                                    process = subprocess.run(
                                        install_cmd, shell=True, capture_output=True, text=True
                                    )

                                    if process.returncode == 0:
                                        print(f"Successfully installed: {pkg}")
                                    else:
                                        print(f"Installation failed: {pkg}")
                                        print(f"Error: {process.stderr}")

                    elif action == "ubuntu":
                        if not args:
                            print("Err: No command specified.")
                        else:
                            ubuntu_cmd = f"sudo {' '.join(args)}"
                            process = subprocess.run(
                                ubuntu_cmd, shell=True, capture_output=True, text=True
                            )

                            if process.returncode == 0:
                                print(f"Command executed successfully: {' '.join(args)}")
                            else:
                                print(f"Command execution failed: {' '.join(args)}")
                                print(f"Error: {process.stderr}")
                    else:
                        print("Err: Incorrect arguments")
                else:
                    print("Err: No arguments provided")

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
                elif arg in ["usr.current"]:
                    os.system("whoami")
                elif arg in ["usr.all"]:
                    os.system("cut -d: -f1 /etc/passwd")
                elif arg in ["stat"]:
                    os.system("top")
                else:
                    print("Err: Incorrect argument")
            else:
                print(f"Err: Command '{command}' not found")
            
            def is_installed(package):
                check_cmd = f"dpkg -l | grep -w {package}"
                result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
                return result.returncode == 0

            def package_exists(package):
                check_cmd = f"apt-cache show {package}"
                result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
                return result.returncode == 0

    except (FileNotFoundError, FileExistsError, NameError) as e:
        print(f"Err: {e}")
        main()
    except KeyboardInterrupt:
        print("")
        main()

def startpy():
    os.system("python")



start()
