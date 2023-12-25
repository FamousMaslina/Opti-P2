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
try:
    from c28610 import *
    c286 = True
except ImportError:
    c286 = False
    pass
try:
    from c28612 import *
    c2862 = True
except ImportError:
    c2862 = False
    pass
try:
    from c28620 import *
    c28620 = True
except ImportError:
    c28620 = False
    pass
try:
    from cpuDef import *
    cpuDef = True
except ImportError:
    cpuDef = False
    pass
try:
    from cpu import *
    cpu = True
except ImportError:
    cpu = False
    pass
try:
    from c38630 import *
    c38630 = True
except ImportError:
    c38630 = False
    pass
try:
    from c38635 import *
    c38635 = True
except ImportError:
    c38635 = False
    pass
try:
    from c38640 import *
    c38640 = True
except ImportError:
    c38640 = False
    pass
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

def nameO():
    print('Opti P2', 'v0.2.2')

def info():
    nameO()
    print(cName, "running at", cFreqS+cFreqUnit)

def help():
    print()
    print("Commands:")
    print("  info - Display information about the OS")
    print("  cls - Clear the screen")
    print("  bios - Enter the BIOS")
    print("  run [FILENAME.EXTENSION] - Run other files (Only Python files work)")
    print("  open [FILENAME.EXTENSION] - Open other files to read their contents (Any files work)")
    print("  dir - Show files in the current working directory (CWD)")
    print("  exit - Exit the OS and the CMD")
    print()

def bios():
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
        inp = input(f"O:/> ")
        inp = inp.lower()
        if inp in ('bios', 'info', 'cls', 'exit', 'help'):
            eval(inp)()
        elif inp.startswith('run '):
            run_file(inp[4:])
        elif inp == 'dir':
            print("Current directory: O:\\")
            files = os.listdir(".")
            for f in files:
                file_type = os.path.isfile(f) and "File" or "Folder"
                size = os.path.getsize(f)
                print(f"{file_type:8s} {f:20s} {size:8,d}")
        elif inp.startswith('open '):
            open_text(inp[5:])
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
