from fileinput import filename
#from configparser import ConfigParser
import os
import time
import requests
import subprocess
from tensorboard import program
global sond
from importlib import import_module
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
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/op2v.py"
    response = requests.get(u1)
    #print("op2.py...")
    #print()
    with open("op2v.py", "wb") as f:
        f.write(response.content)
        f.close()
    import op2v
    print("Found version:", op2v.op2VER, op2v.op2VERSTRING)
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/op2.py"
    response = requests.get(u1)
    print("op2.py...")
    print()
    with open("op2.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/encryp.py"
    response = requests.get(u1)
    print("encryp.py...")
    print()
    with open("encryp.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/hardwiz.py"
    response = requests.get(u1)
    print("hardwiz.py...")
    print()
    with open("hardwiz.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/nguess.py"
    response = requests.get(u1)
    print("nguess.py...")
    print()
    with open("nguess.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/op2api.py"
    response = requests.get(u1)
    print("op2api.py...")
    print()
    with open("op2api.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/write.py"
    response = requests.get(u1)
    print("write.py...")
    print()
    with open("write.py", "wb") as f:
        f.write(response.content)
        f.close()
    print("Done!")
    input("Press enter to exit...")
    exit()

def setup():
    clear()
    print("Opti P2 Setup")
    linebr(20)
    print("Checking your computer...")
    time.sleep(3)
    mark("Allocating space")
    print()
    mark("Formating drive...")
    time.sleep(5)
    clear()
    time.sleep(6)
    restarts()


def learnm():
    mark("Learning more")
    print('This will install OP2 and its core components.')
    print("(encryp, hardwiz, nguess, op2, op2api, write)")
    print("After the installation, you can easily delete the setup files directly from OP2.")
    print()
    input("Press enter to return to the main menu...")
    mainOS()
    
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
mainOS()