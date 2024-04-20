from fileinput import filename
#from configparser import ConfigParser
import os
import time
import requests
import subprocess
from tensorboard import program
global sond
from importlib import import_module
try:
    from idgpu import gpu
    import idgpu as shd
    module_name3 = gpu.replace('.py', '')
    gpu_module = import_module(module_name3)
    gpuC = True
except ImportError:
   gpuC = False
   pass


try:
    from idsound import sound
    module_name6 = sound.replace('.py', '')
    son_module = import_module(module_name6)
    sond = True
except ImportError as sounderror:
    sond = False
    pass
try:
    from idmod import modem
    module_name4 = modem.replace('.py', '')
    md_module = import_module(module_name4)
    mdC = True
except ImportError as e:
   mdC = False
   pass
try:
    from idflo import flo
    module_name7 = flo.replace('.py', '')
    flo_module = import_module(module_name7)
    floC = True
except ImportError:
    floC = False
    pass
try:
    from bios import main
except ImportError as e:
    while True:
        print(e)
        input("SYSTEM HALTED")

from idcpu import cpu
from idmb import mb
from idhd import hd
from idkey import key
from idmon import mon
global intern
intern = 0
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
from os import name, system

#config = ConfigParser()
#conf = 'setup.ini'
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
def linebr(number):
   print("=" * number)
def linebr2(number):
   print("-" * number)
#global fp


#fp = False

def mark(title):
    clear()
    print("Opti P2 Setup")
    linebr(20)
    print(title)


def restarts():
    #while True:
        #global instlibs
        #global delsetuponexit
        #global instapps
        #instlibs = True
        #delsetuponexit = True
        #instapps = True
    mark("Installing...")
    print()
        #print("1. Install all libraries (recommended)", instlibs)
        #print("2. Delete setup on exit (not recommended)", delsetuponexit)
        #print()
        #print("Enter the number of the option you want enabled: ")
        #opt = input("")
        #if opt == 1:
            #if instlibs == False:
                #instlibs = True
            #else:
                #instlibs = False
        #elif opt == 2:
            #if delsetuponexit == False:
                #delsetuponexit = True
            #else:
                #delsetuponexit = False
    #result = subprocess.run(["pip install tabulate"], capture_output=True, text=True)
    #print(result.stdout)
    #result = subprocess.run(["pip install colorama"], capture_output=True, text=True)
    #print(result.stdout)
    #result = subprocess.run(["pip install playsound"], capture_output=True, text=True)
    #print(result.stdout)
    #result = subprocess.run(["pip install ConfigParser"], capture_output=True, text=True)
    #print(result.stdout)
            

def setup():
    clear()
    print("Opti P2 Setup")
    linebr(20)
    print("Checking your computer...")
    freesp = hd_module.hddspace
    if freesp <= 500:
        print()
        print("Your computer does not have enough space to install OP2.")
        print("Press enter to exit...")
        input("")
        mainOS()
    elif freesp < 2500:
        print()
        print("Your computer has enough space to install OP2, but beware that OP2 will warn you every startup about low storage.")
        print("Press enter to continue...")
        input("")
    else:
        pass
    if cpu_module.cFreq < 4.7:
        print("Your CPU does not meet the minnimum requirments!")
        print("Expected Atleast 4.77Mhz! Idendtified:", cpu_module.cFreqS)
        input("Press enter to exit...")
        mainOS()
    time.sleep(3)
    mark("Allocating space")
    print()
    print("Found", freesp, "KB of storage space")
    print("On", hd_module.hddnameS)
    print()
    print("Continue on", hd_module.hddnameS, "?")
    print("Press enter to continue...")
    print("Press CTRL+C to exit and restart the setup program.")
    print()
    input("Enter choice: ")
    mark("Formating drive...")
    time.sleep(5)
    clear()
    time.sleep(6)
    restarts()


def learnm():
    print("Learning More About Setup")

def mainOS():
    #if os.path.exists("setup.ini"): too much work. it dose not work :(
        #config.read("setup.ini")
        #set = config["setup"]
        #if set["fp"] == "TRUE":
            #fp = True
            #restarts()
        #else:
            #fp = False
            #pass
    #else:
        #pass
    clear()
    #print(fp)
    print("Opti P2 Setup")
    linebr(20)
    print("Welcome to the OP2 Setup Program!")
    print("The setup program will guide you through the process of installing OP2.")
    print()
    print("-To set up OP2 now, press ENTER.")
    print("-To learn more about Setup, press 1.")
    print("-To exit Setup, press CTRL+C.")
    print()
    chc = input("Enter Choice: ")
    if chc == "":
        setup()
    elif chc == "1":
        learnm()