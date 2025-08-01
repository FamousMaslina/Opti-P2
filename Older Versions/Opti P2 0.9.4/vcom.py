import sys
import os
import subprocess
from os import name, system
vers = "2.0"
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# Define the paths to your script files
cur = os.getcwd()
py141f = os.path.join(cur, "emulate", "py141", "Py OS.py")
py216f = os.path.join(cur, "emulate", "py216", "Py OS 2.py")
op2062f = os.path.join(cur, "emulate", "op2062", "op2.py")
op104com = os.path.join(cur, "emulate", "op104", "opticom.py")
op104gui = os.path.join(cur, "emulate", "op104", "optigui.py")

# Function to run a script from its own directory
def run_script(script_path):
    script_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)
    subprocess.run(["python", script_name], cwd=script_dir)

def main():
    while True:
        clear()
        print("Virtual Command", vers)
        print("1 - Emulate PyOS V1.4.1")
        print("2 - Emulate PyOS 2 V1.6")
        print("3 - Emulate Opti P V0.4 (CLI)")
        print("4 - Emulate Opti P V0.4 (GUI)")
        print("5 - Emulate Opti P2 V0.6.2")
        #print("6 - Emulate Opti P2 V0.9.3")
        print("6 - Exit")
        ch = input("> ")
        if ch == "1":
            clear()
            try:
                run_script(py141f)
            except FileNotFoundError:
                print("File not found!")
                input("Press enter to return")
        elif ch == "2":
            clear()
            try:
                run_script(py216f)
            except FileNotFoundError:
                print("File not found!")
                input("Press enter to return")
        elif ch == "3":
            clear()
            try:
                run_script(op104com)
            except FileNotFoundError:
                print("File not found!")
                input("Press enter to return")
        elif ch == "4":
            clear()
            try:
                run_script(op104gui)
            except FileNotFoundError:
                print("File not found!")
                input("Press enter to return")
        elif ch == "6":
            exit()
        elif ch == "5":
            clear()
            try:
                run_script(op2062f)
            except FileNotFoundError:
                print("File not found!")
                input("Press enter to return")

try:
    import op2api as api
    api.check()
    api.clear()
    if api.apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
        exit()
    elif api.apiverI >= 0.5 and api.lega == True:
        main()
    elif api.apiverI >= 0.5 or api.apiverI > 0.5:
        main()
except ImportError:
    print("API not found/ not working")
