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
from colorama import init, Fore, Back, Style
import subprocess
import playsound as plays
import re
try:
    os.remove("idcpu.py")
except FileNotFoundError:
    pass
try:
    os.remove("idmb.py")
except FileNotFoundError:
    pass
time.sleep(0.5)
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
      match = re.search(r"(asdawd2k3a403)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main3():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables(file)
      if variables:
        print(file, variables)
        cpu = os.path.basename(file)
        print(cpu)
        file_id = cpu
        with open("idcpu.py", "w") as f:
          f.write("cpu = '{}'".format(file_id))




def find_variables9(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(kkeyb)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main9():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables9(file)
      if variables:
        print(file, variables)
        key = os.path.basename(file)
        print(key)
        file_id = key
        with open("idkey.py", "w") as f:
          f.write("key = '{}'".format(file_id))



def find_variables2(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(ioaoooss)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main2():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables2(file)
      if variables:
        print(file, variables)
        mb = os.path.basename(file)
        print(mb)
        file_id = mb
        with open("idmb.py", "w") as f:
          f.write("mb = '{}'\n".format(file_id))

def find_variables4(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(kajsaed)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main4():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "idhd.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables4(file)
      if variables:
        print(file, variables)
        hd = os.path.basename(file)
        print(hd)
        file_id = hd
        with open("idhd.py", "w") as f:
          f.write("hd = '{}'\n".format(file_id))

def find_variables5(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(mmmnni)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main5():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "idhd.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables5(file)
      if variables:
        print(file, variables)
        mon = os.path.basename(file)
        print(mon)
        file_id = mon
        with open("idmon.py", "w") as f:
          f.write("mon = '{}'\n".format(file_id))

main3()
main2()
main4()
main9()
main5()
time.sleep(0.2)
from idcpu import cpu
from idmb import mb
from idhd import hd
from idkey import key
from idmon import mon
from importlib import import_module

module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
module_name3 = hd.replace('.py', '')
hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
def sleep_time(cFreq):

  sleep_time = 55 / cpu_module.cFreq
  return sleep_time

def sleep_time2(cFreq):

  sleep_time = 5 / cpu_module.cFreq
  return sleep_time
lbreak = '===================='
biosN = 'LBIOS'
biosV = "0.6"
biosFN = 'LegacyBIOS'
osfile = 'op2.py'
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
config = ConfigParser()
if os.path.exists('bios.ini'):
  config.read("bios.ini")
  settings = config["bios"]
else:
   pass
conf = 'bios.ini'
init(autoreset=True)
bios = 0
enter = 'Press enter to continue...'
osfileL = 'opticom.py'


#from identifier import *

def main():
    while True:
        clear()
        print(biosFN, "Menu")
        print(lbreak)
        print("1 - Read Settings")
        print("2 - Config File Configuration")
        print("3 - Legacy Compatibilty")
        print("4 - Change Settings")
        print("5 - Exit")
        print()
        print()
        print("====SYSTEM INFO====")
        print(mb_module.mName)
        print(cpu_module.cName, "running at", cpu_module.cFreqS+cpu_module.cFreqUnit)
        print(mb_module.mMemS)
        print(hd_module.hddnameS, hd_module.hddspaceS)
        print(biosFN, "version", biosV)
        print()
        #if os.path.exists(osfile):
            #from op2 import osN, ver
            #print("Detected OS - ", osN, ver)
            #pass
        #else:
            #print("OS not installed/ not detected.")
            #pass
        print()
        print()
        osfile = 'op2.py'
        conf = 'bios.ini'
        main = input("bios.py/> ")
        if main == '2':
            if bios == 0:
                conf = 'bios.ini'
                while True:
                    print(conf, "not found. Create new one? Y/N")
                    bioscr = input("")
                    bioscr = bioscr.lower()
                    if bioscr == "y":
                        config.add_section('bios')
                        config.set('bios', 'BIOS', 'LB')
                        config.set('bios', 'l_mode', '0')
                        config.set('bios', 'mem_check', '1')
                        with open("bios.ini", 'w') as configfile:
                            config.write(configfile)
                        print("Closing to apply changes. Created", conf)
                        time.sleep(3.5)
                        exit()
                    else:
                        while True:
                            print("Invalid command/ config file operation canceled.")
                            time.sleep(2)
                            break          
            else:
                while True:
                    print(conf, "already present. Operation Canceled.")
                    time.sleep(2)
                    br = 1
                    break

        elif main == '1':
            if bios == 1:
                while True:
                    clear()
                    print("Read Settings")
                    print(lbreak)
                    print("Please note: 0-False, 1-True")
                    print()
                    a_file = open(conf)
                    file_contents = a_file.read()
                    print(file_contents)
                    print(lbreak)
                    print("'exit' to exit.")
                    cs = input("bios.py/cs()/> ")
                    cs = cs.lower()
                    if cs == "exit":
                        break
                    else:
                        print("Unknown")
            else:
                while True:
                    print(conf, "not found. Try using CFC.")
                    time.sleep(2.2)
                    break
        elif main == "5":
            if os.path.exists(osfile):
               os.system("op2.py")
               exit()
            else:
                exit()
        elif main == "3":
            if bios == 1:
                config.read(conf)
                userinfo = config["bios"]
                if userinfo["l_mode"] == "0":
                    userinfo["l_mode"] = "1"
                    with open('bios.ini', 'w') as conf:
                        config.write(conf)
                        while True:
                            print("Activated Legacy Mode!")
                            time.sleep(1.5)
                            break
                elif userinfo["l_mode"] == "1":
                    userinfo["l_mode"] = "0"
                    with open('bios.ini', 'w') as conf:
                        config.write(conf)
                        while True:
                            print("Deactivated Legacy Mode!")
                            time.sleep(1.5)
                            break
            else:
                while True:
                    print(conf, "not found. Try using CFC.")
                    time.sleep(2.2)
                    break      
        elif main == "4":
            while True:
                clear()
                print("Settings Change")
                print(lbreak)
                print("mem_check {}".format(settings["mem_check"]))         
                print()
                changes = input("bios.py/settings/> ")
                if changes == "mem_check 0":
                    settings["mem_check"] = "0"
                    with open('bios.ini', 'w') as conf:
                        config.write(conf)
                        print("Done!")
                        time.sleep(sleep_time2)
                        clear()
                elif changes == "mem_check 1":
                    settings["mem_check"] = "1"
                    with open('bios.ini', 'w') as conf:
                        config.write(conf)
                        print("Done!")
                        time.sleep(sleep_time2)
                        clear()
                elif changes == "exit":
                    clear()
                    break
                else:
                    clear()


sleep_time = sleep_time(cpu_module.cFreq)
sleep_time2 = sleep_time2(cpu_module.cFreq)
clear()
try:
    subprocess.run(["python", "idgpu.py"])
except ImportError:
    pass
clear()
print(cpu_module.cFreqS+cpu_module.cFreqUnit, "Processor")
print(mb_module.mName, mb_module.mMem, "KB")
print()

print(biosFN, biosV, "loading...")

#print(c286, c2862, cpuDef)
time.sleep(sleep_time)
clear()
memcheck = 1
if os.path.exists('bios.ini'):
  if settings["mem_check"] == "1":
      while memcheck < mb_module.mMem:
          print(biosFN, biosV, "loading...")
          print("Detected memory:", mb_module.mMem, "KB")
          print(memcheck, "OK")
          time.sleep(sleep_time2)
          memcheck = memcheck + 100
          clear()
  else:
      pass

import op2
if os.path.exists(conf):
    bios = 1
    print(conf, "found. Continuing...")
    time.sleep(sleep_time)
    op2.mainOS()
else:
    clear()
    print(conf, "not found. Continuing with basic settings...")
    bios = 0
    time.sleep(1.5)
    op2.mainOS()
    #if os.path.exists(osfile):
        #exec(open(osfile).read())
    #else:
        #print("OS not found!")
        #time.sleep(3)
        #main()
