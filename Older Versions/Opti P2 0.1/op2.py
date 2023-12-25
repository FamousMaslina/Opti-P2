import os
import os.path
from configparser import ConfigParser
import sys
import platform
import random
from tabulate import tabulate
from os import system, name
from time import sleep
import time
import subprocess
from colorama import init, Fore, Back, Style
enter = 'Press enter to continue...'
init(autoreset=True)
try:
    from bios import main
except ImportError:
    while True:
        input("SYSTEM HALTED - BIOS NOT FOUND!")

config = ConfigParser()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def open_text(file_name):
    """Opens a text document in the CMD itself."""
    if os.path.isfile(file_name):
        subprocess.run(["type", file_name], shell=True)
    else:
        print(f"File '{file_name}' not found.")

#def dir_cd(folder_name):
#    """Displays the current files in the foldername."""
#    if os.path.isdir(folder_name):
#        files = os.listdir(folder_name)
#        for f in files:
#            file_type = os.path.isfile(f) and "File" or "Folder"
#            size = os.path.getsize(f)
#            print(f"{file_type:8s} {f:20s} {size:8,d}")
#   else:
#        print(f"Directory '{folder_name}' not found.")

def nameO():
    print('Opti P2', 'v0.1')

def help():
    print()
    print("'info' - Display information about the OS")
    print("'cls' - Clear the screen")
    print("'bios' - Enter the BIOS")
    print("'run [FILENAME.EXTENSION]' - Run other files (Only Python files work)")
    print("'open [FILENAME.EXTENSION]' - Open other files to read their contents (Any files work)")
    print("'dir' - Show files in the current working directory (CWD)")
    print("'exit' - Exit the OS and the CMD")
    print()

def oBios():
    clear()
    from bios import main
    main()


def run_file(file_name):
    try:
        subprocess.run(["python", file_name])
    except FileNotFoundError:
        print("File not found.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)


def main():
    clear()
    nameO()
    while True:
        cur_dir = os.getcwd()
        inp = input(f"O:/> ")
        inp = inp.lower()
        if inp == "bios":
            oBios()
        elif inp == "info":
            nameO()
        elif inp == "cls":
            clear()
        elif inp == "exit":
            exit()
        elif inp.startswith("run "):
            run_file(inp[4:])
        elif inp == "dir":
            print("Current directory: O:\\")
            files = os.listdir(".")
            for f in files:
                file_type = os.path.isfile(f) and "File" or "Folder"
                size = os.path.getsize(f)
                print(f"{file_type:8s} {f:20s} {size:8,d}")
        #elif inp.startswith("cd "):
            #new_dir = inp[3:]
            #if os.path.isdir(new_dir):
                #cur_dir = new_dir
                #clear()
                #print(f"Current directory: O:/{cur_dir}")
                #subprocess.run(["cd", new_dir], shell=True)
        elif inp.startswith("open "):
            open_text(inp[5:])
        #elif inp.startswith("dir cd "):
            #dir_cd(inp[7:])
        elif inp == "help":
            help()
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
