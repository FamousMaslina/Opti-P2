#uhhhhhhhhhh what?///
#anyway,
from pathlib import Path
import glob
import os.path
from configparser import ConfigParser
from playsound import playsound
appnfound = "The specified application was not found"
appfail = "An app for Opti was not found. Some commands regarding apps will not work"
filnot = "The specified file dosent exist!"
chkfail = "A requierd file to run Opti dosent exist or is not named corectly."
from colorama import init, Fore, Back, Style
os.getcwd()
init(autoreset=True)
def shutdown():
    clear()
    print("Shutting down...")
    clear()
    time.sleep(1)
    exit()
def restart():
    clear()
    print("Restarting...")
    clear()
    time.sleep(1)
    exec(open('Opti P.py').read())
def resbios():
    clear()
    print("Restarting...")
    time.sleep(1)
    clear()
    exec(open('bios.py').read())
from tabulate import tabulate
import time
count = 0
ver = "0.4"
import pathlib
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
exec(open('check.py').read())
config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["USERINFO"]
opticonf = config_object["OPTICONFIG"]
clear()
if opticonf["infostart"] == "1":
    print("Opti P version", ver,"running on Python:", sys.version, platform.system(), platform.release(), platform.machine())
else:
    clear()

print("Welcome, {}".format(userinfo["username"]))
print()
while count <5:
    os = input("O:\ ")
    words = os.split()
    if os == "over":
        print()
        print("Opti P version", ver,"running on Python:", sys.version, platform.system(), platform.release(), platform.machine())
        print()
    elif os == "cle":
        clear()
    elif os == "clrtest":
        print(Style.BRIGHT + Back.CYAN + Fore.RED + "Colors! :D")
    elif os == "mnote":
        print("There are alot more easter eggs than features! Good luck finding all! ;)")
    elif os == "rconf":
        print()
        print("Please note: 0-False, 1-True")
        print()
        a_file = open("config.ini")
        file_contents = a_file.read()
        print(file_contents)
    elif os == "easteregg":
        if userinfo["easteregg"] == "1":
            print("You know stuff! عمل جيد!")
        else:
            print("Not enabled")
    elif os == "usernamechange":
        print()
        print("Type in your new username:")
        nuser = input("")
        userinfo["username"] = nuser
        with open('config.ini', 'w') as conf:
            config_object.write(conf)
            print("New Username Set")
    elif os == "updlog":
        print()
        print(ver, "- Added 'bios.py''")
        print("and made 'help' an external application")
        print()
    elif os == "crd":
        if userinfo["finsetup"] == "1":
            if opticonf["showcred"] == "1":
                print("ArielAutomat - The Main/Lead Dev")
            else:
                print("Not enabled")
        elif opticonf["showcred"] == "1":
            if userinfo["finsetup"] == "0":
                print("Not enabled")
        else:
            print("Not enabled")
    #external apps
    elif os == "write":
        clear()
        try:
            exec(open('wr.py').read())
        except FileNotFoundError:
            print(appnfound)
    elif os == "calculator":
        try:
            exec(open('calc.py').read())
        except FileNotFoundError:
            print(appnfound)
    elif os == "bios":
        try:

            exec(open('bios.py').read())
        except FileNotFoundError:
            print(appnfound)
    elif os == "clock":
        try:
            exec(open('clock.py').read())
        except FileNotFoundError:
            print(appnfound)
    elif os == "help":
        try:
            exec(open('help.py').read())
        except FileNotFoundError:
            print(appnfound)
    elif os == "opti":
        try:
            exec(open('optigui.py').read())
        except FileNotFoundError:
            print(appnfound)
    #ends here
    elif os == "refil":
        print()
        name = input("Name of the file (including extension): ")
        print()
        try:
            a_file = open(name)
            file_contents = a_file.read()
            print(file_contents)
            print()
        except FileNotFoundError:
            print("The file dosent exist")
    elif os == "aloader":
        print()
        print("Remember! Trust the application! It might do some bad things!")
        print("Make sure you trust the file you want to run!")
        print()
        time.sleep(3)
        nameap = input("Name of the file to run (inculding extension): ")
        clear()
        exec(open(nameap).read())
    elif os == "shutdown":
        shutdown()
    elif os == "exit":
        shutdown()
    elif os == "restart":
        restart()
    elif os == "reboot":
        restart()
    elif os == "bios":
        resbios()
    else:
        print("Bad command")
