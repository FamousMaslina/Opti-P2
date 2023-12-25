import threading
import time
import os
from op2api import *
def get_user_input():
    global user_input
    try:
        user_input = input("Press Enter to enter the Boot Menu: ")
        clear()
        print("OP2 Boot Menu")
        while True:
            linebr(20)
            print("1 - Verify Integrity")
            print("2 - Boot OP2 normally")
            print("3 - Clear Screen")
            ch = input("> ")
            if ch == "1":
                file_names = ["bios.ini", "op2.ini", "write.py", "nguess.py", "encryp.py", "op2.py", "bios.py", "op2v.py", "op2api.py", "dial.mp3", "hardwiz.py"]
                cwd = os.getcwd()
                for file_name in file_names:
                    file_path = os.path.join(cwd, file_name)
                    if os.path.exists(file_path):
                        print(f"{file_name} exists in the current working directory.")
                    else:
                        print(f"{file_name} does not exist in the current working directory.")
            elif ch == "2":
                clear()
                from op2 import mainOS
                mainOS()
            elif ch == "3":
                clear()
                    

    except EOFError:  # Raised when no input is received
        user_input = None

def bootmenu():
    global user_input
    user_input = None

    # Create a thread to get user input
    input_thread = threading.Thread(target=get_user_input)
    input_thread.daemon = True  # Mark the thread as a daemon so it doesn't prevent program exit

    input_thread.start()

    # Wait for a few seconds for user input
    input_thread.join(timeout=25)  # Change the timeout value as needed (5 seconds in this example)

    # Check if user provided input or if no input was received
    if user_input is None:
        print("No input received. Continuing...")
        from op2 import mainOS
        mainOS()
