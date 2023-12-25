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
subprocess.run(["python", "identifier.py"])
time.sleep(0.1)
from idcpu import cpu
from idmb import mb
from importlib import import_module

module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
osName = "Opti P2"
osVersion = "0.3"

def sleep_timeAppLoad(cFreq):

  sleep_time = 45 / cpu_module.cFreq
  return sleep_time

def sleep_timeInAppLoad(cFreq):

  sleep_time = 15 / cpu_module.cFreq
  return sleep_time

init(autoreset=True)

try:
    from bios import main
except ImportError:
    while True:
        input("SYSTEM HALTED")

config = ConfigParser()
sleep_timeAppL = sleep_timeAppLoad(cpu_module.cFreq)
sleep_timeIAppL = sleep_timeInAppLoad(cpu_module.cFreq)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def open_text(file_name):
    
    if os.path.isfile(file_name):
        time.sleep(sleep_timeAppL)
        subprocess.run(["type", file_name], shell=True)
        print()
    else:
        print(f"File '{file_name}' not found.")

def nameO():
    print(osName, osVersion)

def dvcman():
    time.sleep(sleep_timeAppL)
    print()
    print("Identified Hardware:")
    time.sleep(sleep_timeIAppL)
    print("  Motherboard - "+mb_module.mName)
    time.sleep(sleep_timeIAppL)
    print("  Physical Memory - "+mb_module.mMemS)
    time.sleep(sleep_timeIAppL)
    print("  Processor - "+cpu_module.cName)
    time.sleep(sleep_timeIAppL)
    print("  Processor Speed - "+cpu_module.cFreqS+cpu_module.cFreqUnit)
    print("  Operating System - "+osName, osVersion)
    print()

def info():
    nameO()
    time.sleep(sleep_timeIAppL)
    print(cpu_module.cName, "running at", cpu_module.cFreqS+cpu_module.cFreqUnit)

def help():
    time.sleep(sleep_timeAppL)
    print()
    print("Commands:")
    print("  info - Display information about the OS")
    print("  cls - Clear the screen")
    print("  bios - Enter the BIOS")
    print("  run [FILENAME.EXTENSION] - Run other files (Only Python files work)")
    print("  open [FILENAME.EXTENSION] - Open other files to read their contents (Any files work)")
    print("  dir - Show files in the current working directory (CWD)")
    print("  dvcman - Current Installed Hardware")
    print("  exit - Exit the OS and the CMD")
    print()

def bios():
    time.sleep(sleep_timeAppL)
    clear()
    from bios import main
    main()


def run_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
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
        if inp in ('bios', 'info', 'cls', 'exit', 'help', 'dvcman'):
            eval(inp)()
        elif inp.startswith('run '):
            run_file(inp[4:])
        elif inp == 'dir':
            time.sleep(sleep_timeAppL)
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
