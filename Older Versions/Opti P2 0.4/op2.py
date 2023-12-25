import os
try:
    from bios import main
except ImportError:
    while True:
        input("SYSTEM HALTED")
from importlib import import_module

from idcpu import cpu
from idmb import mb
try:
    from idgpu import gpu
    module_name3 = gpu.replace('.py', '')
    gpu_module = import_module(module_name3)
    gpuC = True
except ImportError:
   gpuC = False
   pass
module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)

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
import re

def find_python_files(directory):
  """Finds all Python files in the specified directory."""
  files = os.listdir(directory)
  python_files = []
  for file in files:
    if file.endswith(".py"):
      python_files.append(os.path.join(directory, file))
  return python_files

def find_variables(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(gpu)", line)
      if match:
        variables.append(match.group(1))
  return variables

def mainG():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "op2.py" and os.path.basename(file) != "idmb.py":
      variables = find_variables(file)
      if variables:
        print(file, variables)
        gpu = os.path.basename(file)
        print(gpu)
        file_id = gpu
        with open("idgpu.py", "w") as f:
          f.write("gpu = '{}'".format(file_id))
          global gpuC
          gpuC = True


    

osName = "Opti P2"
osVersion = "0.4"

def sleep_timeAppLoad(cFreq):

  sleep_time = 45 / cpu_module.cFreq
  return sleep_time

def sleep_timeInAppLoad(cFreq):

  sleep_time = 15 / cpu_module.cFreq
  return sleep_time

init(autoreset=True)



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

def gpuinfo():
    time.sleep(sleep_timeIAppL)
    print()
    if gpuC == False:
        print("GPU not detected. Run 'gpu' to detect.")
    else:
        print("Current Installed GPU information:")
        print("  Graphic Processor - "+gpu_module.gName)
        time.sleep(sleep_timeIAppL)
        print("  Graphic Memory -",gpu_module.gVram, "MB")
        time.sleep(sleep_timeIAppL)
        print("  Graphic Processor Frequency -",gpu_module.gSpeedS)
        time.sleep(sleep_timeIAppL)
        print("  Pixel Shaders -",gpu_module.gps)
        time.sleep(sleep_timeIAppL)
        print("  Vertex Shaders -",gpu_module.gvs)
        time.sleep(sleep_timeIAppL)
        print("  ROPs -",gpu_module.grop)
        print()

def nameO():
    print(osName, osVersion)
def gpu():
    print(gpuC)
    if gpuC == False:
        try:
            os.remove('idgpu.py')
        except FileNotFoundError:
           pass
        time.sleep(sleep_timeAppL)
        print("Detecting GPU...")
        mainG()
        print("Restarting to apply changes...")
        time.sleep(sleep_timeIAppL)
        restart()
        exit()
    else:
       print("GPU already dectected")

def restart():
    os.system("op2.py")

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
    print("  gpu - For detecting a GPU")
    print("  gpuinfo - Extra information about the current installed GPU")
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
        if inp in ('bios', 'info', 'cls', 'exit', 'help', 'gpu', 'restart', 'gpuinfo'):
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
        elif inp == "dvcman":
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
            time.sleep(sleep_timeIAppL)
            if gpuC == False:
                pass
            else:
                print("  Graphic Processor - "+gpu_module.gName)
                time.sleep(sleep_timeIAppL)
                print("  Graphic Memory -",gpu_module.gVram, "MB")
                time.sleep(sleep_timeIAppL)
            print("  Operating System - "+osName, osVersion)
            print()
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
