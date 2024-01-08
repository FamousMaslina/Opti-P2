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

config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["USERINFO"]
opticonf = config_object["OPTICONFIG"]
setfail = "Same value or incorrect value"
chkfail = "A requierd file to run Opti dosent exist or is not named corectly."

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
def restart():
    clear()
    print("Restarting...")
    time.sleep(1)
    clear()
    exec(open('Opti P.py').read())
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
clear()   
count = 0
print("Welcome! Type 'help' to get started")
print()
while count <5:
    bios = input("bios.py/> ")
    if bios == "help":
        print("--------------------------------")
        print("note:  enable = 1   disable = 0")
        print()
        print("First of all, execute 'rconf' to ")
        print("read the contents of 'config.ini'.")
        print()
        a_file = open("config.ini")
        file_contents = a_file.read()
        print("--------------------------------")
        print(file_contents)
        print("--------------------------------")
        print()
        print("For example 'infostart' from '[OPTICONFIG]'")
        print("section, is on default disabled (0).")
        print("If we want to enable this, we execute:")
        print("enable infostart")
        print("If we want to disable it we execute:")
        print("disable infostart")
        print("--------------------------------")
        print("NOTE! If a setting's value is for")
        print("example '1' and we try to enable it,")
        print("you will get an error saying:")
        print(setfail)
        print("--------------------------------")
        print("So if you want to change a value,")
        print("just execute 'enable/disable' and 'setting'")
        print("from config.ini")
        print("--------------------------------")
        print("If you want to clear the screen then execute 'cle'")
        print("To exit bios type 'exit'")
        print()
    elif bios == "cle":
        clear()
    elif bios == "disable easteregg":
        print()
        if userinfo["easteregg"] == "1":
            userinfo["easteregg"] = "0"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "enable easteregg":
        print()
        if userinfo["easteregg"] == "0":
            userinfo["easteregg"] = "1"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()    
    elif bios == "disable username":
        print()
        print("This cannot be changed in bios. Try in Opti P")
    elif bios == "enable username":
        print()
        print("This cannot be changed in bios. Try in Opti P")
    elif bios == "disable infostart":
        print()
        if opticonf["infostart"] == "1":
            opticonf["infostart"] = "0"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "enable infostart":
        print()
        if opticonf["infostart"] == "0":
            opticonf["infostart"] = "1"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "disable showcred":
        print()
        if opticonf["showcred"] == "1":
            opticonf["showcred"] = "0"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "enable showcred":
        print()
        if opticonf["showcred"] == "0":
            opticonf["showcred"] = "1"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()      
    elif bios == "disable chkstart":
        print()
        if opticonf["chkstart"] == "1":
            opticonf["chkstart"] = "0"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "enable chkstart":
        print()
        if opticonf["chkstart"] == "0":
            opticonf["chkstart"] = "1"
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                print("Done!")
                print()
        else:
            print(setfail)
            print()
    elif bios == "rconf":
        print()
        print("Please note: 0-False, 1-True")
        print()
        a_file = open("config.ini")
        file_contents = a_file.read()
        print(file_contents)
    elif bios == "disable modem":
        print()
        print("This cannot be changed.")
    elif bios == "enable modem":
        print()
        print("This cannot be changed.")   
    elif bios == "exit":
        restart()
    else:
        print("Unknown command")

