#from op2 import osName, conf
import op2v
from op2api import apiver, apiverI, compver, compver2, compver3, compver4, compver5, compver6
import os
import random
import subprocess
import psutil

def is_script_running(script_name):
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = proc.info['cmdline']
            # Ensure 'cmdline' is not None and then check if the script name is in the command line
            if cmdline and any(script_name in arg for arg in cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    script_name = "op2.py"
    if is_script_running(script_name):
        print(f"{script_name} is running.")
    else:
        print(f"{script_name} is not running.")

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
ver = "1.0.1"
def mainpt():
    while True:
        clear()
        print("OP2 Power Tools", ver)
        linebr(40)
        print("1.Enable DEBUG mode")
        print("2.Disable DEBUG mode")
        #print("3.Direct Function Call (for functions not present in mainOS())")
        print("3.Delete or Reset AUTOSTART")
        print("4.Delete ID Files")
        #print("5.Direct Function Call (for functions not present in mainOS())")
        print("6.Return to OP2")
        linebr2(40)
        #print(osName)
        print("OP2V Reported Version:", op2v.op2VER)
        print("OP2V Reported Intger Version:", op2v.op2VERI)
        print("OP2V Reported String Version:", op2v.op2VERSTRING)
        #print(conf, "DEF CONFIG NAME")
        print("Reported API version:", apiver)
        print("Reported API Intger version:", apiverI)
        if is_script_running(script_name):
            print(f"{script_name} is running.")
        else:
            print(f"{script_name} is not running.")
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
        elif a == "6":
            exit()
        elif a == "5":
            f = input("Name of function: ")
            command = ["python", "op2.py", f, "--external"]
            result = subprocess.run(command, capture_output=True, text=True)
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            print("returncode:", result.returncode)
        else:
            print()
mainpt()
