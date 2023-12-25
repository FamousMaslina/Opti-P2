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
    from idmod import modem
    module_name4 = modem.replace('.py', '')
    md_module = import_module(module_name4)
    mdC = True
except ImportError as e:
   mdC = False
   pass
from idcpu import cpu
from idmb import mb
from idhd import hd
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
module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
module_name3 = hd.replace('.py', '')
hd_module = import_module(module_name3)
import op2v
apiver = "0.3"
apiverI = 0.3
compver = "0.6"
def sleep_timeAppLoad(cFreq):

  sleep_time = 45 / cpu_module.cFreq
  return sleep_time

def sleep_timeInAppLoad(cFreq):

  sleep_time = 15 / cpu_module.cFreq
  return sleep_time
sleep_timeAppL = sleep_timeAppLoad(cpu_module.cFreq)
sleep_timeIAppL = sleep_timeInAppLoad(cpu_module.cFreq)
def check():
    if compver == op2v.op2VER:
        print("API version", apiver)
        print("API Check done!")
    else:
        print("API version", apiver)
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



