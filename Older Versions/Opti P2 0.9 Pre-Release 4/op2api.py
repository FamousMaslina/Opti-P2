import os
import random
from os import name, system
from importlib import import_module
import playsound
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
try:
    from idgpu import gpu
    module_name3 = gpu.replace('.py', '')
    gpu_module = import_module(module_name3)
    gpuC = True
except ImportError:
   gpuC = False
   pass
try:
    from idsound import sou
    module_name6 = sou.replace('.py', '')
    son_module = import_module(module_name6)
    souC = True
except ImportError:
   souC = False
   pass
try:
    from idmod import modem
    module_name4 = modem.replace('.py', '')
    md_module = import_module(module_name4)
    mdC = True
except ImportError as e:
   mdC = False
   pass
global lega
lega = False
try:
  import op2v
except ImportError:
   print("OP2V Not Found! Legacy Mode Enabled!")
   lega = True
apiver = "0.6"
apiverI = 0.8
compver = "0.6"
compver2 = "0.6 R2"
compver3 = "0.6.1"
compver4 = "0.5"
compver5 = "0.5 R2"
compver6 = "0.6.2"

import string
from idcpu import cpu
from idmb import mb
if lega == True:
  pass
elif lega == False:
  if compver4 == op2v.op2VER or compver5 == op2v.op2VER:
    pass
try:
  from idhd import hd
  module_name3 = hd.replace('.py', '')
  hd_module = import_module(module_name3)
except ImportError:
   pass
import time
import os.path
from configparser import ConfigParser
import sys
import platform
import random
from tabulate import tabulate
from os import system, name
from time import sleep
import time
import subprocess
from colorama import init, Fore, Back, Style
module_name = cpu.replace('.py', '') 
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)



def sleep_timeAppLoad(cFreq):

  sleep_time = 13 / cpu_module.cFreq #was 45(og), 35, 25, 15
  return sleep_time

def sleep_timeInAppLoad(cFreq):

  sleep_time = 2 / cpu_module.cFreq #was 15(og), 5
  return sleep_time

def sleep_timecustom(sec, cFreq):

  sleep_time = sec / cpu_module.cFreq
  return sleep_time
sleep_timeAppL = sleep_timeAppLoad(cpu_module.cFreq)
sleep_timeIAppL = sleep_timeInAppLoad(cpu_module.cFreq)

def linebr(number):
   print("=" * number)
def linebr2(number):
   print("-" * number)

def configFile(var, filename):
    var = ConfigParser()
    with open(filename, 'w') as configfile:
      var.write(configfile)                

def check():
    if lega == True:
       pass
    elif compver == op2v.op2VER or compver2 == op2v.op2VER or compver3 == op2v.op2VER or compver4 == op2v.op2VER or compver5 == op2v.op2VER or compver6 == op2v.op2VER or 0.7 < op2v.op2VERI or 0.7 == op2v.op2VERI:
        print("API version", apiverI)
        print("API Check done!")
    else:
        print("API version", apiverI)
        print("API Requires atleast", compver+". Found op2 Version:", op2v.op2VER)
        input("Press enter to continue...")
        exit()


import os

def get_file_size_in_kb(file_path):
  """Returns the size of the file in KB."""
  file_size_in_bytes = os.path.getsize(file_path)
  file_size_in_kb = file_size_in_bytes / 1024
  return file_size_in_kb

cwd = os.getcwd()
files = os.listdir(cwd)
total_size_in_kb = 0
for file in files:
  file_size_in_kb = get_file_size_in_kb(os.path.join(cwd, file))
  total_size_in_kb += file_size_in_kb
space = round(total_size_in_kb, 2)

def errormes(title, text, opttext):
  print()
  linebr(45)
  print(title)
  linebr(45)
  print()
  print(text)
  linebr2(45)
  input(opttext)
  linebr(45)
  print()


def setupprog(progamname, customdirs, customdirspath, checkapi, checkcpu, checksize, checkcpureq, checksizereq, apireq):
  if customdirs == False or None:
    customdirspath = None
    pass
  elif checkapi == False or None:
    apireq = None
    pass
  elif checkcpu == False or None:
    checkcpureq = None
    pass
  elif checksize == False or None:
    checksizereq = None
    pass
  print("Welcome to", progamname, "setup!")#default text 
  linebr(40)
  print("This setup program will help you install", progamname, "on your system. Press enter to continue...")
  input("")
  clear()
  if checkapi == True:
      if apiverI < apireq:
        print("Your API version is lower than expected! The expected version is {apireq} and you have {apiverI}")
        input("Press enter to exit!")
        exit()
      else:
        pass
  else:
    pass
  if checkcpu == True:
    if cpu_module.cFreq < checkcpureq:
      print("Your CPU, does not meet the minnimum requirments!")
      print("Expected Atleast {cpureq} Idendtified:", cpu_module.cFreqS)
      input("Press enter to exit...")
      exit()
    else:
      pass
  else:
    pass
  if checksize == True:
    if hd_module.hddspace < checksizereq:
      print("You don't have enough space to install the program! Expected atleast {checksizereq}!")
      input("Press enter to exit...")
      exit()
    else:
      pass
  else:
    pass
  clear()
  print("Starting to install", progamname)
  print()
  if customdirs == True:
  #create a folder in the cwd with the name being customdirspath (variable)
    os.makedirs(customdirspath, exist_ok=True)
    pass
  else:
    pass
  #now starts the downloading process... best way is through git, or any http request to download required files.
  #you should aslo handle by yourself the files needed to be copied to the custom dir! (sorry...)
def randomints():
    length = int(input("Enter the length of the string: "))
    #password = randomints()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    print(password)
    print()
    return password


def randomsyspass():
    length = int(input("Enter the length of the password: "))
    
    # Custom mappings for characters
    sys = {
        'A': 'asda321',
        'B': 'qwe1234',
        'C': 'zxc1234',
        'D': 'poi0987',
        'E': 'mnb9876',
        'F': 'hndf13r4',
        'G': 'klp4321',
        'H': 'yhn7890',
        'I': 'qaz8765',
        'J': 'vbn6789',
        'K': 'fgh6543',
        'L': 'wsx7654',
        'M': 'edc8765',
        'N': 'ujm5432',
        'O': 'ikl9876',
        'P': 'rfv7654',
        'Q': 'xed7654',
        'R': 'cde4567',
        'S': 'rfv7654',
        'T': 'bhj8765',
        'U': 'plm5432',
        'V': 'wsx7654',
        'W': 'ujm5432',
        'X': 'cvb6789',
        'Y': 'zxc1234',
        'Z': 'qwe1234',
        'a': 'asda321',
        'b': 'qwe1234',
        'c': 'zxc1234',
        'd': 'poi0987',
        'e': 'mnb9876',
        'f': 'hndf13r4',
        'g': 'klp4321',
        'h': 'yhn7890',
        'i': 'qaz8765',
        'j': 'vbn6789',
        'k': 'fgh6543',
        'l': 'wsx7654',
        'm': 'edc8765',
        'n': 'ujm5432',
        'o': 'ikl9876',
        'p': 'rfv7654',
        'q': 'xed7654',
        'r': 'cde4567',
        's': 'rfv7654',
        't': 'bhj8765',
        'u': 'plm5432',
        'v': 'wsx7654',
        'w': 'ujm5432',
        'x': 'cvb6789',
        'y': 'zxc1234',
        'z': 'qwe1234',
        '0': '12345',
        '1': '54321',
        '2': '67890',
        '3': '09876',
        '4': '13579',
        '5': '24680',
        '6': '11111',
        '7': '22222',
        '8': '33333',
        '9': '44444',
        '!': '@#$%^',
        '@': '&*()_',
        '#': '{}|:"',
        '$': '<>?[]'
    }

    password = ''.join(sys.get(c, c) for c in ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length)))

    print("Encrypting...")
    print()
    print(password)
    return password



