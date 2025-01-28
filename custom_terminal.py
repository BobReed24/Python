import os
import json

def load_commands():
    try:
        with open('commands.json', 'r') as f:
            commands = json.load(f)
        return commands
    except FileNotFoundError:
        print("Err: 'commands.json' not found. Using default commands.")
        return []

def start():
    os.system('cls||clear')
    main()

def main():
    commands = load_commands()
    try:
        while True:
            cur_dir = os.getcwd()
            syscmd = input(f"{cur_dir} (python) $ ")
            command = syscmd

            # Check if the command is in the loaded commands
            for cmd in commands:
                if command.startswith(cmd['original_command']):
                    command = command.replace(cmd['original_command'], cmd['command_replacement'])
                    break

            # Handle commands based on the replacement logic
            if command.startswith('cd'):
                command = command.replace("cd ", "")
                os.chdir(command)
            elif command.startswith('peek'):
                command = command.replace("peek ", "")
                os.system(f'ls {command}')
            elif command.startswith('get.cwd'):
                command = command.replace("get.cwd", "")
                os.system('pwd')
            elif command.startswith('branch'):
                command = command.replace("branch", "")
                os.system(f"ls {command}/*")
            elif command.startswith('tree'):
                os.system("ls *")
            elif command.startswith('task --show'):
                command = command.replace(f"task --show ", "")
                os.system(f'ps aux | grep {command}')
            elif command.startswith('task -s'):
                command = command.replace(f"task -s ", "")
                os.system(f'ps aux | grep {command}')
            elif command.startswith('admin'):
                osname = os.name
                if osname == 'nt':
                    print("Err: Command not available for Windows")
                elif command.startswith('admin install'):
                    command = command.replace("admin install ", "")
                    os.system(f"sudo apt install -y {command}")
                elif command.startswith('admin ubuntu'):
                    command = command.replace("admin ubuntu ", "")
                    os.system(f"sudo {command}")
                else:
                    print("Err: Incorrect arguments")
            elif command.startswith('lib.use'):
                command = command.replace("lib.use ", "")
                os.system(f"{command}")
            elif command.startswith('create'):
                if command.startswith('create --directory'):
                    command = command.replace("create --directory ", "")
                    os.system(f"mkdir {command}")
                elif command.startswith('create -d'):
                    command = command.replace("create -d ", "")
                    os.system(f"mkdir {command}")
                elif command.startswith('create --file'):
                    command = command.replace("create --file ", "")
                    os.system(f"nano {command}")
                elif command.startswith('create -f'):
                    command = command.replace("create -f ", "")
                    os.system(f"nano {command}")
                else:
                    print("Err: Incorrect arguments")
            elif command.startswith('remove'):
                if command.startswith('remove --directory'):
                    command = command.replace("remove --directory ", "")
                    os.system(f"rm -r -d -f {command}")
                elif 'remove -d' in command:
                    command = command.replace("remove -d ", "")
                    os.system(f"rm -r -d -f {command}")
                elif 'remove --file' in command:
                    command = command.replace("remove --file ", "")
                    os.system(f"rm {command}")
                elif 'remove -f' in command:
                    command = command.replace("remove -f ", "")
                    os.system(f"rm {command}")
                else:
                    print("Err: Incorrect arguments")
            elif 'read' in command:
                command = command.replace("read ", "")
                os.system(f"cat {command}")
            elif 'modify' in command:
                if 'modify --editfile' in command:
                    command = command.replace("modify --editfile" , "")
                    os.system(f"nano {command}")
                elif 'modify -ef' in command:
                    command = command.replace("modify -ef ", "")
                    os.system(f"nano {command}")
                elif 'modify --copyfile' in command:
                    command = command.replace("modify --copy ", "")
                    os.system(f"cp {command}")
                elif 'modify -cf' in command:
                    command = command.replace("modify -cf ", "")
                    os.system(f"cp {command}")
                elif 'modify --copydir' in command:
                    command = command.replace("modify --copyir ", "")
                    os.system(f"cp -r {command}")
                elif 'modify -cd' in command:
                    command = command.replace("modify -cd ", "")
                    os.system(f"cp -r {command}")
                elif 'modify --movefile' in command:
                    command = command.replace("modify --movefile ", "")
                    os.system(f"mv {command}")
                elif 'modify -mf' in command:
                    command = command.replace("modify -mf ", "")
                    os.system(f"mv {command}")
                elif 'modify --movedir' in command:
                    command = command.replace("modify --movedir ", "")
                    os.system(f"mv -r {command}")
                elif 'modify -md' in command:
                    command = command.replace("modify -md ", "")
                    os.system(f"mv -r {command}")
                else:
                    print("Err: Incorrect arguments")
            elif 'python' in command or 'py' in command:
                startpy()
            elif 'kill' in command:
                if 'kill --all' in command:
                    command = command.replace("kill --all ", "")
                    os.system(f"pkill -f {command}")
                elif 'kill -a' in command:
                    command = command.replace("kill -a ", "")
                    os.system(f"pkill -f {command}")
                elif 'kill -specific' in command:
                    command = command.replace("kill --specific ", "")
                    os.system(f"kill {command}")
                elif 'kill -s' in command:
                    command = command.replace("kill -s ", "")
                    os.system(f"kill {command}")
                else:
                    print("Err: Incorrect arguments")
            elif 'bash' in command:
                command = command.replace("bash ", "")
                os.system(f"bash {command}")
            elif './' in command:
                command = command.replace("./ ", "")
                os.system(f"bash {command}")
            else:
                print(f"Err: Command '{command}' not found")
    except (FileNotFoundError, FileExistsError, NameError) as e:
        print(f"Err: {e}")
        main()
    except KeyboardInterrupt:
        print('')
        main()

def startpy():
    os.system("python")

start()
