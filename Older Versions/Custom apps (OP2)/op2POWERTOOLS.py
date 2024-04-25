#from op2 import osName, conf
import op2v
from op2api import apiver, apiverI, compver, compver2, compver3, compver4, compver5, compver6
import os
import random
from configparser import ConfigParser
from os import name, system
def linebr(number):
   print("=" * number)
def linebr2(number):
   print("-" * number)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
config = ConfigParser()
config.read("op2.ini")
settings = config["user"]
syst = config["sys"]
ver = "1.0"
def mainpt():
    while True:
        clear()
        print("OP2 Power Tools", ver)
        linebr(40)
        print("1.Enable DEBUG mode")
        print("2.Disable DEBUG mode")
        #print("3.Direct Function Call (for functions not present in mainOS())")
        print("3.Delete\Reset AUTOSTART")
        print("4.Delete ID Files")
        print("5.Return to OP2")
        linebr2(40)
        #print(osName)
        print("OP2V REPORTED VER:", op2v.op2VER)
        print(op2v.op2VERI, "INTGER")
        print(op2v.op2VERSTRING)
        #print(conf, "DEF CONFIG NAME")
        print("API VER", apiver)
        print(apiverI)
        linebr(40)
        a = input("Enter choice: ")
        if a == "1":
            new = "DEBUG_MODE"
            settings['computer_name'] = new
            with open('op2.ini', 'w') as a:
                config.write(a)
            print("SET!")
        elif a == "2":
            new = "DEFAULT"
            settings['computer_name'] = new
            with open('op2.ini', 'w') as a:
                config.write(a)
            print("SET!")
        #elif a == "3":
            #f = input("Function name ('NAME()'): ")
            #import op2
            #op2.f
        elif a == "3":
            os.remove("autostart.txt")
            print("Deleted autostart.txt")
        elif a == "4":
            files = ["idcpu.py", "idmb.py", "idmon.py", "idkey.py", "idhd.py"]
            for filename in files:
                os.remove(filename)
        elif a == "5":
            exit()
        else:
            print()
mainpt()
