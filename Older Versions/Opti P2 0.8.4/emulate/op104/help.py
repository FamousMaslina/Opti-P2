import os
import os.path
import sys
import platform
import random
from tabulate import tabulate
from os import system, name
from time import sleep
width = os.get_terminal_size().columns
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
print("Help".center(width))
print()
print()
table = [['Command', 'What does it do', 'Notes'], ['cle', 'Clears the screen', '-'], ['over', 'Shows info about Opti and Python', '-'], ['rconf', 'Read the config file', 'Located in the same directory'], ['usernamechange', 'Changes your username', '-'], ['updlog', 'The update log', '-'], ['write', 'Write something then save it', '-'], ['refil', 'Read the content of a file','-'], ['calculator', 'A calculator bruh', '-'], ['shutdown or exit', 'Closes the console', '-'], ['clock', 'A clock', '-'], ['reboot or restart', 'Restarts the OS', '-'], ['bios', 'Enter the bios', '-']]
print(tabulate(table, headers='firstrow'))
print()
print("-----------------")
print("help.py commands:")
print("Exit - 'exit'")
print()
count = 0
while count <5:
    helpi = input("O:\help.py ")
    if helpi == "exit":
        clear()
        break
        
    else:
        print("Unknown parameter")

