import os
import random
import subprocess
import psutil
from configparser import ConfigParser

import op2v
from op2api import apiver, apiverI, compver, compver2, compver3, compver4, compver5, compver6

def linebr(number):
    print("=" * number)

def linebr2(number):
    print("-" * number)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def is_script_running(script_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = proc.info['cmdline']
            if cmdline and any(script_name in arg for arg in cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def enable_debug_mode():
    config = ConfigParser()
    config.read("op2.ini")
    settings = config["user"]
    new = "DEBUG_MODE"
    settings['computer_name'] = new
    with open('op2.ini', 'w') as a:
        config.write(a)
    print("DEBUG MODE ENABLED")

def disable_debug_mode():
    config = ConfigParser()
    config.read("op2.ini")
    settings = config["user"]
    new = "DEFAULT"
    settings['computer_name'] = new
    with open('op2.ini', 'w') as a:
        config.write(a)
    print("DEBUG MODE DISABLED")

def delete_autostart():
    if os.path.exists("autostart.txt"):
        os.remove("autostart.txt")
        print("Deleted autostart.txt")
    else:
        print("No autostart.txt file found.")

def delete_id_files():
    files = ["idcpu.py", "idmb.py", "idmon.py", "idkey.py", "idhd.py"]
    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Deleted {filename}")
        else:
            print(f"{filename} not found.")

def show_version_info():
    clear()
    ver = "1.0.2"
    print("OP2 Power Tools EXT", ver)
    linebr(40)
    print("1.Enable DEBUG mode")
    print("2.Disable DEBUG mode")
    print("3.Delete or Reset AUTOSTART")
    print("4.Delete ID Files")
    print("5.Return to OP2")
    linebr2(40)
    print("OP2V Reported Version:", op2v.op2VER)
    print("OP2V Reported Integer Version:", op2v.op2VERI)
    print("OP2V Reported String Version:", op2v.op2VERSTRING)
    print("Reported API version:", apiver)
    print("Reported API Integer version:", apiverI)
    script_name = "op2.py"
    if is_script_running(script_name):
        print(f"{script_name} is running.")
    else:
        print(f"{script_name} is not running.")
    linebr(40)

def manage_power_tools():
    show_version_info()
    while True:
        a = input("Enter choice: ").strip()
        if a == "1":
            enable_debug_mode()
        elif a == "2":
            disable_debug_mode()
        elif a == "3":
            delete_autostart()
        elif a == "4":
            delete_id_files()
        elif a == "5":
            break
        else:
            clear()  # Clear the screen
            print("Unknown choice. Please try again.")
            show_version_info()  # Re-display the version info after clearing

# Commands to be exposed
commands = {
    'manage_tools': manage_power_tools
}

info = {
    'title': 'OP2 Power Tools',
    'version': '1.0.2',
    'author': 'FamousMaslina',
    'description': 'Manage various OP2 settings quicker.',
    'commands': ', '.join(commands.keys())
}
