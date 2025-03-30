import shutil
import os as compy

currentdir = compy.getcwd()
print()
print("░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗")
print("██╔══██╗██╔══██╗████╗░████║██╔══██╗╚██╗░██╔╝")
print("██║░░╚═╝██║░░██║██╔████╔██║██████╔╝░╚████╔╝░")
print("██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░░░╚██╔╝░░")
print("╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░░░░██║░░░")
print("░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░ v1.0")
print("It's Linux but with some changes and twists!")
print()
print("Welcome to Compy v1.0! Type 'help' for information.")
print("by Carlos Eduardo Laborda (Charlie)")
print()
print("Type 'readme' for the history of Compy.")

def cp_command(src, dest):
    try:
        if not compy.path.exists(src):
            print(f"ERROR: Source file/directory '{src}' does not exist.")
            return
        if compy.path.isdir(src):
            if compy.path.isdir(dest):
                dest = compy.path.join(dest, compy.path.basename(src))
            shutil.copytree(src, dest)
            print(f"Copied directory '{src}' to '{dest}'.")
        else:
            if compy.path.isdir(dest):
                dest = compy.path.join(dest, compy.path.basename(src))
            shutil.copy(src, dest)
            print(f"Copied file '{src}' to '{dest}'.")
    except Exception as e:
        print(f"ERROR: {e}")

while True:
    command = input(f"nickylinux@compy {currentdir} $ ")
    
    if command.lower() == "exit":
        print("See you next time. Bye! :D")
        print()
        break
    
    elif command.lower() == "help":
        print("Here are the valid commands:")
        print()
        print("list - Lists files/directories. Here are its variants:")
        print("    list.di - Lists files/directories with detailed information.")
        print("    list.ih - Lists all files/directories, including hidden ones.")
        print("    list.hr - Lists files/directories in a way humans can read.")
        print()
        print("exit - Just exits the terminal, nothing more ._.")
        print()
        print("help - I think you can guess what this one does.")
        print()
        print("l - Clears the screen.")
        print()
        print("chdir - Changes your directory.")
        print()
        print("whereami - Shows in which directory you are.")
        print()
        print("mkdir - Makes a directory.")
        print()
        print("rmv - Removes a file. Here are its variants:")
        print("    rmv.di - Removes a directory with its content.")
        print("    rmv.fo - Removes a file without warning.")
        print()
        print("copy - Copies a file. Here is its variant:")
        print("    copy.di - Copies a directory.")
        print()
        print("mvornm - Moves or renames a file.")
        print()
        print("mkfil - Makes a file.")
        print()
        print("rdfil - Reads a file.")
        print()
        print("ping - Pings a website.")
        print()
        print("edfil - Edits a file.")
        print()
        print("readme - Reads the file 'readme.txt'.")
    elif command.lower() == "l":
        compy.system("clear")
    elif command.lower().startswith("list"):
        if ".di" in command:
            compy.system("ls -l")
        elif ".ih" in command:
            compy.system("ls -a")
        elif ".hr" in command:
            compy.system("ls -h")
        else:
            compy.system("ls")
    elif command.lower().startswith("chdir "):
        path = command[6:].strip()
        if path:
            try:
                compy.chdir(path)
                currentdir = compy.getcwd()
            except FileNotFoundError:
                print(f"ERROR: Directory '{path}' does not exist.")
            except PermissionError:
                print(f"ERROR: Access to directory '{path}' denied.")
        else:
            print(f"ERROR: Path not specified.")
    elif command.lower() == "whereami":
        print(currentdir)
    elif command.lower().startswith("mkdir "):
        newdir = command[6:].strip()
        if newdir:
            compy.system(f"mkdir {newdir}")
            print(f"Made directory '{newdir}'")
        else:
            print("ERROR: Directory name not specified.")
    elif command.lower().startswith("rmv"):
        if ".di " in command:
            targetdir = command[7:].strip()
            if targetdir:
                want = str(input(f"The removal of directory '{targetdir}' may be irreversible. Are you sure you want to remove directory '{targetdir}'?[y/n]"))
                if want == 'y':
                    compy.system(f"rm -r {targetdir}")
                    print(f"Removed directory '{targetdir}'.")
                else:
                    print(f"Cancelled removal of directory '{targetdir}'.")
            else:
                print("ERROR: Directory name not specified.")
        elif ".fo " in command:
            targetfil = command[7:].strip()
            if targetfil:
                compy.system(f"rm -f {targetfil}")
                print(f"Removed file '{targetfil}'.")
            else:
                print("ERROR: File name not specified.")
        else:
            targetfil = command[4:].strip()
            if targetfil:
                want = str(input(f"The removal of file '{targetfil}' may be irreversible. Are you sure you want to remove file '{targetfil}'?[y/n]"))
                if want == 'y':
                    compy.system(f"rm {targetfil}")
                    print(f"Removed file '{targetfil}'.")
                else:
                    print(f"Cancelled removal of file '{targetfil}'.")
            else:
                print("ERROR: File name not specified.")
    elif command.lower().startswith("copy.di"):
        parts = command[8:].strip().split(" ", 1)
        if len(parts) == 2:
            source_dir, destination = parts
            cp_command(source_dir, destination)
        else:
            print("ERROR: Invalid syntax.")
    elif command.lower().startswith("copy"):
        parts = command[5:].strip().split(" ", 1)
        if len(parts) == 2:
            source, destination = parts
            cp_command(source, destination)
        else:
            print("ERROR: Invalid syntax.")
    elif command.lower().startswith("mvornm"):
        parts = command[7:].strip().split(" ", 1)
        if len(parts) == 2:
            file, name = parts
            compy.system(f"mv {file} {name}")
            print(f"Moved/renamed file '{file}' to '{name}'.")
        else:
            print("ERROR: Invalid syntax.")
    elif command.lower().startswith("mkfil "):
        file = command[6:].strip()
        if file:
            compy.system(f"touch {file}")
            print(f"Made file '{file}'.")
        else:
            print("ERROR: Filename not specified.")
    elif command.lower().startswith("rdfil "):
        file = command[6:].strip()
        if file:
            print()
            compy.system(f"cat {file}")
            print()
        else:
            print("ERROR: Filename not specified.")
    elif command.lower().startswith("ping "):
        web = command[5:].strip()
        if web:
            compy.system(f"ping {web}")
        else:
            print("ERROR: Website not specified.")
    elif command.lower().startswith("edfil "):
        file = command[6:].strip()
        if file:
            compy.system(f"vi {file}")
    elif command.lower() == "readme":
        compy.system("clear")
        compy.system("cat readme.txt")
    else:
        print("ERROR: Command not valid. Type 'help' for information.")