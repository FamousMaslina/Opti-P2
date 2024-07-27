# Opti P2 - So-called OS made in Python.
Inspired by MS-DOS

## Why?
-it started with some old projects of mine. You can actually check them out in older versions folder. (The oldest is Py OS)

## Features (0.9.X):
* Delete, create, edit, open files
* Little games included
* Message Server&Client
* Custom Hardware\Apps (even custom BIOS, if that counts)
* Custom API for certain functions used in OP2
* Flexible Hardware (you can literally put a 186 mb with a 360cpu!)
* Ability to update directly from OP2
* Setup file (if you're too lazy.)
* Ability to create custom users with password!
* Easibly Moddable!
* Custom Extensions (0.9.2)
* L-Linux... s-support... (ig)

## Instructions:
### Windows:
	First of all, make sure you have Python install WITH PATH!
	The easiest way to run OP2 is to download it from the 'Releases' tab, and then extract the archive. In the root folder there will be a file called 'installlibs.bat' which will install all the needed modules. Then you run op2.py from the 'Opti P2' folder and you're done!
	If you want an older version (which is not in the releases tab), you will need to clone the repo and go in the 'Older Versions' Folder.

### Linux:
	(ᗒᗣᗕ)

### Custom Hardware:
	OP2 requires you to have atleast the CPU, Motherboard, Floppy Drive, Monitor and Keyboard File. All the custom hardware is located in their respective folders. If you want to change/add new hardware, DELETE the old one, and copy the hardware file to where op2.py and bios.py is.

 ## Troubleshooting:
 * Most issues come from modules that aren't installed. Make sure to run 'installibs.bat' to automatically install all modules. (Requires Python with PATH, Windows and 0.9.2 only.)

## Modding:
* A new addition in 0.9.2 are extensions, which are designed to be run as commands in OP2. You have two examples in the 'extensions' folder in the same directory. (Again, only available in 0.9.2)
* Creating apps for OP2 is completly normal. However, if you're lazy and you don't want to import modules, op2api is there for you.
* op2api has those modules:
	* import os
	* import random
	* from os import name, system
	* from importlib import import_module
	* import playsound
	* import time
	* import os.path
	* from configparser import ConfigParser
	* import sys
	* import platform
	* import random
	* from tabulate import tabulate
	* from os import system, name
	* from time import sleep
	* import time
	* import subprocess
	* from colorama import init, Fore, Back, Style

### Advanced Modding
* If you want to create more realistic apps that takes advantage of OP2s functions, the api has plenty of them!
* op2api has some variables, used to check if for example, there is certain HW installed or so on...
	* cwd = Current Working Directory
	* files = List files in the Current Working Directory
	* apiverI = Used to check for the API version
	* gpuC = Can be either True or False, if there is a GPU detected or not
	* mdC = Can be either True or False, if there is a Modem detected or not
	* souC = Can be either True or False, if there is a Sound Card detected or not
	* cpu_module.VARIABLE = Used for accessing the CPU file
	* mb_module.VARIABLE = Used for accessing the MB file

* Before that, let's get comfortable with the CPU's variables.
	* cFreq = Represents the Frequency of the CPU in MHz. Every CPU file has this value in NUMBERS!
	* cFreqS = Is the same as cFreq, but in string.
	* cFreqUnit = Its "MHz" in string.
	* Those Variables are used with the prefix cpu_module.VARIABLE

* Useful Functions:
	* clear/cls = Clears the screen
	* check = Check for the API version

* App Intisialsation:
	* sleep_timeAppLoad(cFreq) - The longest loading time, used for loading apps. (13seconds / cpu_module.cFreq)
	* sleep_timeInAppLoad(cFreq) - The shortest loading time, used for loading stuff in the app (example from OP2: help). (2seconds / cpu_module.cFreq)
	* sleep_timecustom(sec, cFreq) - Custom loading time (X seconds / cpu_module.cFreq) X Value must be a number!

* App Installation:
	* setupprog(progamname, customdirs, customdirspath, checkapi, checkcpu, checksize, checkcpureq, checksizereq, apireq)
	* programname = The name of your program
	* customdirs = If there are custom folders needed to be created (either True or False)
	* customdirspath = The name of the folder
	* checkapi = True or False
	* checkcpu = True or False
	* checksize = True or False
	* checkcpureq = Number, indicating the min MHz of a cpu
	* checksizereq = Number, indicating the min KB for the installation
	* apireq = Number, indicating the min API ver
