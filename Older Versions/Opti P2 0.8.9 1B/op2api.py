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
