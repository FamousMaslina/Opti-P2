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
try:
    os.remove("idcpu.py")
except FileNotFoundError:
    pass
try:
    os.remove("idmb.py")
except FileNotFoundError:
    pass
time.sleep(0.5)
subprocess.run(["python", "identifier.py"])
time.sleep(0.2)
from idcpu import cpu
from idmb import mb
from importlib import import_module

module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)

def sleep_time(cFreq):

  sleep_time = 55 / cpu_module.cFreq
  return sleep_time

def sleep_time2(cFreq):

  sleep_time = 5 / cpu_module.cFreq
  return sleep_time
lbreak = '===================='
biosN = 'LBIOS'
biosV = "0.3 Rev B"
biosFN = 'LegacyBIOS'
osfile = 'op2.py'
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
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
if os.path.exists(conf):
    bios = 1
    print(conf, "found. Continuing...")
    time.sleep(sleep_time)

else:
    clear()
    print(conf, "not found. Continuing with basic settings...")
    bios = 0
    time.sleep(1.5)
    #if os.path.exists(osfile):
        #exec(open(osfile).read())
    #else:
        #print("OS not found!")
        #time.sleep(3)
        #main()
