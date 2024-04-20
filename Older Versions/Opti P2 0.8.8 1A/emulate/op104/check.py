
import os.path
from configparser import ConfigParser
appnfound = "The specified application was not found"
appfail = "An app for Opti was not found. Some commands regarding apps will not work"
filnot = "The specified file dosent exist!"
chkfail = "A requierd file to run Opti dosent exist or is not named corectly."
from tabulate import tabulate
import time
import os
import sys
import platform
import random
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
print("    ______                    ____  ________  _____    _    ______  __ __")
print("   / ____/___ __________     / __ )/  _/ __ \/ ___/   | |  / / __ \/ // /")
print("  / __/ / __ `/ ___/ __ \   / __  |/ // / / /\__ \    | | / / / / / // /")
print(" / /___/ /_/ / /  / / / /  / /_/ // // /_/ /___/ /    | |/ / /_/ /__  __/")
print("/_____/\__,_/_/  /_/ /_/  /_____/___/\____//____/     |___/\____(_)/_/")   
                                                                            
                                                                      
print()
time.sleep(1)
print("Checking if config.ini is present...")
if os.path.exists('config.ini'):
    pass
else:
    print()
    print(chkfail)
    input("Press enter to continue... (Opti will exit)")
print("Done!")
time.sleep(1)
print()
print("Checking if bios.py is present...")
if os.path.exists('bios.py'):
    pass
else:
    print()
    print(chkfail)
    input("Press enter to continue... (Opti will exit)")
print("Done!")
time.sleep(1)
config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["USERINFO"]
opticonf = config_object["OPTICONFIG"]
if opticonf["chkstart"] == "1":
    print("Running checks...")
    if os.path.exists('calc.py'):
        pass
    else:
        print()
        print(appfail)
        input("Press enter to continue...")
    if os.path.exists('wr.py'):
        pass
    else:
        print()
        print(appfail)
        input("Press enter to continue...")
    if os.path.exists('clock.py'):
        pass
    else:
        print()
        print(appfail)
        input("Press enter to continue...")
    if os.path.exists('help.py'):
        pass
    else:
        print()
        print(appfail)
        input("Press enter to continue...")
print("OK!")