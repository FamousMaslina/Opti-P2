import os
import os.path
import sys
import platform
import random
from os import system, name
from time import sleep
width = os.get_terminal_size().columns
os.system('color 07')
print("Write".center(width))
os.system('color 8f')
print()
print()
print("Start typing... (when pressing enter you cannot continue your writing")
os.system('color 1f')
print("meaning that you need to save the file)")
print()
os.system('color 1f')
wr = input("")
print()
os.system('color 1f')
namef = input("Name of the file: ")
with open(namef, 'w') as f:
    f.write(wr)
os.system('color 1f')
print("File saved")
os.system('color 1f')
input("Press enter to exit")
os.system('color 0f')
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
