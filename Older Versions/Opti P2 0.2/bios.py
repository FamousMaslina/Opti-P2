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

def sleep_time(cFreq):
  """Calculates the amount of time to sleep based on the MHz.

  Args:
    cFreq: The CPU frequency in MHz.

  Returns:
    The amount of time to sleep in seconds.
  """

  sleep_time = 1 / cFreq
  return sleep_time

lbreak = '===================='
biosN = 'LBIOS'
biosV = "0.1 Rev B"
biosFN = 'LegacyBIOS'
osfile = 'op2.py'
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
config = ConfigParser()
conf = 'bios.ini'
init(autoreset=True)
bios = 0
enter = 'Press enter to continue...'
osfileL = 'opticom.py'




def main():
    while True:
        clear()
        print(biosFN, "Menu")
        print(lbreak)
        print("1 - Read Settings")
        print("2 - Config File Configuration")
        print("3 - Legacy Compatibilty")
        print("4 - Exit")
        print()
        print()
        print("====SYSTEM INFO====")
        print(cName, "running at", cFreqS+cFreqUnit)
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
        elif main == "4":
            if os.path.exists(osfile):
               exec(open(osfile).read())
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

if c286 or c2862 or cpuDef or c28620 or cpu:
    pass
else:
    exit()
sleep_time = sleep_time(cFreq)
print(biosFN, biosV, "loading...")
print(c286, c2862, cpuDef)
time.sleep(sleep_time)

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
