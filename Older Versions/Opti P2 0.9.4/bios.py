import os
import os.path
from configparser import ConfigParser
import sys
import platform
import random
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
from os import system, name
from time import sleep
import time
#from colorama import init, Fore, Back, Style
import subprocess
#import playsound as plays
import re
global playsM
global coloramaM
global tabulateM
playsM = True
coloramaM = True
tabulateM = True
try:
  import playsound as plays
except ImportError:
  playsM = False
try:
  from colorama import init, Fore, Back, Style
except ImportError:
  coloramaM = False
try:
  from tabulate import tabulate
except ImportError:
   tabulateM = False



if os.name == 'nt':  
    python_executable = 'python'
elif os.name == 'posix': 
    python_executable = 'python3'

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

def find_cpu(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(asdawd2k3a403)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main_cpu():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_cpu(file)
      if variables:
        #print(file, variables)
        cpu = os.path.basename(file)
        #print(cpu)
        file_id = cpu
        with open("idcpu.py", "w") as f:
          f.write("cpu = '{}'".format(file_id))




def find_keyboard(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(kkeyb)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main_keyboard():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_keyboard(file)
      if variables:
        #print(file, variables)
        key = os.path.basename(file)
        #print(key)
        file_id = key
        with open("idkey.py", "w") as f:
          f.write("key = '{}'".format(file_id))



def find_mb(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(ioaoooss)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main_mb():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_mb(file)
      if variables:
        #print(file, variables)
        mb = os.path.basename(file)
        #print(mb)
        file_id = mb
        with open("idmb.py", "w") as f:
          f.write("mb = '{}'\n".format(file_id))

def find_hdd(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(kajsaed)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main_hdd():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "idhd.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_hdd(file)
      if variables:
        #print(file, variables)
        hd = os.path.basename(file)
        #print(hd)
        file_id = hd
        with open("idhd.py", "w") as f:
          f.write("hd = '{}'\n".format(file_id))

def find_monitor(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(mmmnni)", line)
      if match:
        variables.append(match.group(1))
  return variables

def main_monitor():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "identifier.py" and os.path.basename(file) != "op2.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "idhd.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_monitor(file)
      if variables:
        #print(file, variables)
        mon = os.path.basename(file)
        #print(mon)
        file_id = mon
        with open("idmon.py", "w") as f:
          f.write("mon = '{}'\n".format(file_id))

def find_floppy(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(firin)", line)
      if match:
        variables.append(match.group(1))
  return variables
def main_Floppy():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "op2.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "op2api.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_floppy(file)
      if variables:
        #print(file, variables)
        flo = os.path.basename(file)
        #print(flo)
        file_id = flo
        with open("idflo.py", "w") as f:
          f.write("flo = '{}'".format(file_id))
          global floC
          floC = True
main_cpu()
main_mb()
main_keyboard()
main_Floppy()
main_hdd()
main_monitor()
time.sleep(0.2)
global hdinstall
hdinstall = False
from idcpu import cpu
from idmb import mb
try:
  from idhd import hd
  hdinstall = True
except ImportError:
   pass
   hdinstall = False
from idkey import key
from idmon import mon
from idflo import flo
from importlib import import_module

module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
if hdinstall == False:
   pass
else:
  module_name3 = hd.replace('.py', '')
  hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
module_name6 = flo.replace('.py', '')
flo_module = import_module(module_name6)
def sleep_time(cFreq):

  sleep_time = 15 / cpu_module.cFreq #was 55(og), 30, 15
  return sleep_time

def sleep_time2(cFreq):

  sleep_time = 2 / cpu_module.cFreq #was 5(og), 3
  return sleep_time
lbreak = '===================='
biosN = 'ABIOS'
biosV = "0.3 Rev A"
biosFN = 'Award Modular BIOS'
osfile = 'op2.py'
config = ConfigParser()
try:
    config.read("bios.ini")
    settings = config["bios"]
except FileNotFoundError:
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
        if coloramaM == False:
          print(biosFN, "Menu")
        elif coloramaM == True:
          print(Style.BRIGHT + Fore.GREEN + biosFN + " Menu" + Style.RESET_ALL)
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
        if hdinstall == False:
          pass
        else:
          print(hd_module.hddnameS, hd_module.hddspaceS)
        print(biosFN, "version", biosV)
        if coloramaM == False:
           print("coloramaM", False)
        if tabulateM == False:
           print("tabulateM", tabulateM)
        if playsM == False:
           print("playsound", playsM)
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
               subprocess.run([python_executable, "op2.py"], check=True)
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
print("Award Modular BIOS", biosV, ",An energy star ally")
print(cpu_module.cFreqS+cpu_module.cFreqUnit, "Processor")
print()

#print(biosFN, biosV, "loading...")

#print(c286, c2862, cpuDef)
print("Detected memory:", mb_module.mMem, "KB")

time.sleep(3)
clear()
print("Award Software, Inc.")
print("System Configuration")
print("---------------------")
print("CPU:", cpu_module.cName)
print("Co-Processor: Installed")
print("CPU Clock:", cpu_module.cFreqS+cpu_module.cFreqUnit)
print("---------------------")
print("Base Memory:", mb_module.mMemS)
print("---------------------")
print("Diskette Drive A: None")
print("Pri. Master Disk:", hd_module.hddspace, hd_module.hddnameS)
print("---------------------")
print("Display Type:", mon_module.monitorName)
print("---------------------")

time.sleep(6)
clear()
time.sleep(1)

opexist = False
setup = False
try:
  import op2
  opexist = True
  setup = False
except ImportError:
  pass
  opexist = False
  try:
    import op2setup
    setup = True
  except ImportError:
    setup = False


if os.path.exists(conf):
    bios = 1
    print(conf, "found. Continuing...")
    time.sleep(sleep_time)
    if opexist == True:
      op2.mainOS()
    elif setup == True:
      op2setup.mainOS()
    else:
      print("OP2 not found!")
      time.sleep(3)
      main()
else:
    clear()
    print(conf, "not found. Continuing with basic settings...")
    bios = 0
    time.sleep(1.5)
    if opexist == True:
      op2.mainOS()
    elif setup == True:
      op2setup.mainOS()
    else:
      print("OP2 not found!")
      time.sleep(3)
      main()
    #if os.path.exists(osfile):
        #exec(open(osfile).read())
    #else:
        #print("OS not found!")
        #time.sleep(3)