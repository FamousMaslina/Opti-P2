from tkinter import *
from tkinter.ttk import *
import os
import sys
import platform
import random
from os import system, name
from time import sleep
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Clock')
 
# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'blue',
            foreground = 'white')
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

mainloop()