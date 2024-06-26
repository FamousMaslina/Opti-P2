from fileinput import filename
import os
import time
import requests
from importlib import import_module
from tensorboard import program
from idcpu import cpu
module_name = cpu.replace('.py', '')
cpu_module = import_module(module_name)
global sond
from importlib import import_module
try:
    from bios import main
except ImportError as e:
    while True:
        print(e)
        input("SYSTEM HALTED")
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
try:
    from idgpu import gpu
    import idgpu as shd
    module_name3 = gpu.replace('.py', '')
    gpu_module = import_module(module_name3)
    gpuC = True
except ImportError:
   gpuC = False
   pass


try:
    from idsound import sound
    module_name6 = sound.replace('.py', '')
    son_module = import_module(module_name6)
    sond = True
except ImportError as sounderror:
    sond = False
    pass
try:
    from idmod import modem
    module_name4 = modem.replace('.py', '')
    md_module = import_module(module_name4)
    mdC = True
except ImportError as e:
   mdC = False
   pass
try:
    from idflo import flo
    module_name7 = flo.replace('.py', '')
    flo_module = import_module(module_name7)
    floC = True
except ImportError:
    floC = False
    pass

import os
import random
from os import name, system

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

from idmb import mb
from idhd import hd
from idkey import key
from idmon import mon
global intern
intern = 0
  # Remove the .py extension
module_name2 = mb.replace('.py', '')

mb_module = import_module(module_name2)
module_name3 = hd.replace('.py', '')
hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
def restart():
    time.sleep(sleep_timeAppL)
    os.system("op2.py")
    exit()
#from op2api import *
#subprocess.run(["python", "op2api.py"])
time.sleep(0.1)
import re
global cc
global prog
global fla
cc = os.getcwd()
clear()
cwd = os.getcwd()
files = os.listdir(cwd)
def get_file_size_in_kb(file_path):
  """Returns the size of the file in KB."""
  file_size_in_bytes = os.path.getsize(file_path)
  file_size_in_kb = file_size_in_bytes / 1024
  return file_size_in_kb
total_size_in_kb = 0
for file in files:
  file_size_in_kb = get_file_size_in_kb(os.path.join(cwd, file))
  total_size_in_kb += file_size_in_kb
space = round(total_size_in_kb, 2)
freesp = hd_module.hddspace - space
freesp = round(freesp, 2)
if cpu_module.cFreq < 2.0: #was 4.77
    print("Your CPU, does not meet the minnimum requirments!")
    print("Expected Atleast 2MHz! Identified:", cpu_module.cFreqS)
    input("Press enter to exit...")
    exit()
if freesp < 2500:
   print("LOW STORAGE!")
   print(freesp, "KB Remaining")
   input("Press enter to continue...")
def find_python_files(directory):
  """Finds all Python files in the specified directory."""
  files = os.listdir(directory)
  python_files = []
  for file in files:
    if file.endswith(".py"):
      python_files.append(os.path.join(directory, file))
  return python_files
config = ConfigParser()
conf = 'op2.ini'
if os.path.exists("op2.ini"):
    pass
else:
    clear()
    input("OP2.INI NOT FOUND! Press enter to create new one...")
    config.add_section('user')
    config.set('user', 'computer_name', 'DEFAULT')
    config.add_section('sys')
    config.set('sys', 'remids', '0')
    config.set('sys', 'chkfile', '0')
    with open("op2.ini", 'w') as configfile:
        config.write(configfile)
        print("Closing to apply changes. Created", conf)
        time.sleep(3.5)
        #input("Press enter to restart...")
        #restart()
        pass

config.read("op2.ini")
settings = config["user"]
syst = config["sys"]
import op2v
osName = "Opti P2 LW"
osVersion = op2v.op2VER
clear()
#check()
clear()

tt = "System"
ent = "Press enter to continue..."


#init(autoreset=True)

#def api():
   #check()

#if os.path.exists("autostart.txt"):
    #pass
#else:
    #with open("autostart.txt", "w") as file:
        #pass

global ex
ex = False
if os.path.exists('op2.ini'):
    ex = True
else:
    ex = False
def configuration():
    conf = 'op2.ini'
    if ex == False:
        while True:
            print(conf, "not found. Create new one? Y/N ")
            bioscr = input("")
            bioscr = bioscr.lower()
            if bioscr == "y":
                config.add_section('user')
                config.set('user', 'computer_name', 'DEFAULT')
                config.add_section('sys')
                config.set('sys', 'remids', '0')
                config.set('sys', 'chkfile', '0')
                with open("op2.ini", 'w') as configfile:
                    config.write(configfile)
                print("Closing to apply changes. Created", conf)
                time.sleep(3.5)
                restart()
            else:
                while True:
                    print("Unknown command")
                    #errormes(tt, txt1, ent)
                    time.sleep(2)
                    break          
    else:
        while True:
            txt1 =  "config already present. Operation Canceled."
            print(txt1)
            #errormes(tt, txt1, ent)
            time.sleep(2)
            break
if ex == True:
    try:
        config.read("op2.ini")
        settings = config["user"]
        ex = True
    except FileNotFoundError:
        ex = False
        pass
else:
    pass
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



def open_text(file_name):
    
    if os.path.isfile(file_name):
        time.sleep(sleep_timeAppL)
        subprocess.run(["type", file_name], shell=True)
        print()
    else:
        print(f"File '{file_name}' not found.")

def gpuinfo():
    time.sleep(sleep_timeIAppL)
    print()
    if gpuC == False:
        txt1 = "GPU not detected. Run 'gpu' to detect."
        #errormes(tt, txt1, ent)
        print(txt1)
    else:
        print("Current Installed GPU information:")
        print("  Graphic Processor - "+gpu_module.gName)
        time.sleep(sleep_timeIAppL)
        print("  Graphic Memory -",gpu_module.gVram, "MB")
        time.sleep(sleep_timeIAppL)
        print("  Graphic Processor Frequency -",gpu_module.gSpeedS)
        time.sleep(sleep_timeIAppL)
        print("  Pixel Shaders -",gpu_module.gps)
        time.sleep(sleep_timeIAppL)
        print("  Vertex Shaders -",gpu_module.gvs)
        time.sleep(sleep_timeIAppL)
        print("  ROPs -",gpu_module.grop)
        print()

def nameO():
    print(osName, osVersion)


def internet():
    global intern
    time.sleep(sleep_timeAppL)
    if mdC == True:
        if intern == 0:
            import playsound as ps
            print("Enter the User to log into your ISP")
            user = input("> ")
            print()
            print("Enter the Password to log into your ISP")
            passw = input("> ")
            print()
            print("Connecting to internet via", md_module.modemname, "with", md_module.dialupadp+"...")
            print("As:", user)
            try:
                ps.playsound('dial.mp3')
            except FileNotFoundError:
               pass
            print("CONNECTED!")
            intern = 1
        elif intern == 1:
            print("Already connected!")
    else:
       txt1 = "No modem found. Run 'hardware'"
       #errormes(tt, txt1, ent)
       print(txt1)


#def audio():
    

def info():
    print()
    nameO()
    time.sleep(sleep_timeIAppL)
    print("Build", op2v.op2VERSTRING)
    time.sleep(sleep_timeIAppL)
    if ex == True:
        print("Computer name: {}".format(settings["computer_name"]))
    else:
        pass
    time.sleep(sleep_timeIAppL)
    print(cpu_module.cName, "running at", cpu_module.cFreqS+cpu_module.cFreqUnit)
    print()

def resethardware():
    delgpu = False
    delmod = False
    delsou = False
    try:
      os.remove('idmod.py')
      delmod = True
    except FileNotFoundError:
       pass
    try:
       os.remove('idsound.py')
       delsou = True
    except FileNotFoundError:
       pass
    try:
       os.remove('idgpu.py')
       delsou = True
    except FileNotFoundError:
       pass
    print()
    print("Deleted:")
    print("GPU", delgpu)
    print("Modem", delmod)
    print("Sound Card", delsou)
    print()
    restart()



def virtualcommand():
   try:
        subprocess.run(["python", 'vcom.py'])
   except FileNotFoundError:
      pass   
import os, shutil

def upkeep():
    shutil.rmtree("__pycache__")
    #os.remove("idcpu.py")
    #if os.path.exists('idflo.py'):
        #os.remove("idflo.py")
    #else:
        #pass
    #if os.path.exists('idgpu.py'):
        #os.remove("idgpu.py")
    #else:
        #pass
    #os.remove("idhd.py")
    #os.remove("idkey.py")
    #os.remove("idmb.py")
    #os.remove("idmon.py")
    #if os.path.exists('idsound.py'):
        #os.remove("idsound.py")
    #else:
        #pass
    #if os.path.exists('idmod.py'):
        #os.remove("idmod.py")
    #else:
        #pass
    #print("Operation successful!")
def hardwarefast():
    try:
        subprocess.run(["python", 'hardwiz.py'])
    except FileNotFoundError:
      pass
    if os.path.exists('idsound.py'):
        os.remove("idsound.py")
    else:
        pass
    if os.path.exists('idmod.py'):
        os.remove("idmod.py")
    else:
        pass
    if os.path.exists('idflo.py'):
        os.remove("idflo.py")
    else:
        pass
    if os.path.exists('idgpu.py'):
        os.remove("idgpu.py")
    else:
        pass
if syst["remids"] == "1":
    upkeep()
    #hardwarefast()
def confighelp():
    time.sleep(sleep_timeAppL)
    print()
    print("Commands:")
    linebr(80)
    print("OS Related:")
    print("  remids - Automatically delete pycache on startup. Current value: {}".format(syst["remids"]))
    #print("  chkfile - Check for required files on startup (Not used)")
    linebr2(80)
    print("To change values, just type your desired item, and it's value will be replaced.")
    print("0 = disabled; 1 = enabled")
    print()

def remids():
    if syst["remids"] == "1":
        syst["remids"] = "0"
        with open('op2.ini', 'w') as conf:
            config.write(conf)
        print("Turned off pycache deleting on startup")
    else:
        syst["remids"] = "1"
        with open('op2.ini', 'w') as conf:
            config.write(conf)
        print("Turned on pycache deleting on startup")

def help():
    time.sleep(sleep_timeAppL)
    print()
    print("Commands:")
    linebr(20)
    print("OS Related:")
    print("  info - Display information about the OS")
    print("  cls - Clear the screen")
    print("  configuration - Create the configuration file for OP2")
    print("  confighelp - See the configuration commands\entries")
    print("  settings - Change settings from the configuration file")
    print("  upkeep - Remove unused files.")
    print("  restart - Restart OP2")
    print("  exit - Exit the OS and the CMD")
    linebr2(20)
    print("File/Directory Managment:")
    print("  run [FILENAME.EXTENSION] - Run other files (Only Python files work)")
    print("  open [FILENAME.EXTENSION] - Open other files to read their contents (Any files work)")
    print("  dir - Show files in the current working directory (CWD)")
    print("  del [FILENAME.EXTENSION] - Delete Files")
    print("  :a [FILENAME.EXTENSION] - Access file from a floppy drive (if installed)")
    linebr2(20)
    print("Applications (some of them cannot exist, due to your install options or version/build):")
    #print("  encryp - Encrypt Strings into numbers")
    #print("  nguess - Play a little game (Expects API Version 0.2)")
    #print("  write - Write Text Files")
    print("  calc - Calculator")
    print("  internet - Connect to the Internet")
    #print("  virtualcommand - Emulate Py OS or Py OS 2 (if installed)")
    print()
    print("'2' - Page 2")
    print("'exit' - exit help")
    hlp = input("> ")
    hlp = hlp.lower()
    if hlp == "exit":
        print()
        pass
    elif hlp == "2":
        clear()
        help2()
    else:
        print()
        pass

def help2():
    time.sleep(sleep_timeAppL)
    #print("  omclient - Launch Opti Messager (if installed)")
    #print("  omserver - Start a server for Opti Messager (if installed)")
    linebr2(20)
    print("Hardware Related:")
    #print("  hardware - Identify GPUs, Modems, Sound Cards")
    print("  resethardware - Delete idgpu, idmod and idsound")
    #print("  gpuinfo - Extra information about the current installed GPU")
    print("  dvcman - Current Installed Hardware")
    #linebr2(20)
    #print("API Related:") 
    #print("  api - Check API version")
    #print("  api /? - Check API's help")
    #print("  api.update - Update the API")
    linebr2(20)
    print("Advanced:") 
    print("  bios - Enter the BIOS")
    linebr(20)
    print()
    print("'1' - Page 1")
    print("'exit' - exit help")
    hlp = input("> ")
    hlp = hlp.lower()
    if hlp == "exit":
        print()
        pass
    elif hlp == "1":
        clear()
        help()
    else:
        print()
        pass

def bios():
    time.sleep(sleep_timeAppL)
    clear()
    from bios import main
    main()

def encryp():
   try:
        subprocess.run(["python", 'encryp.py'])
   except FileNotFoundError:
      pass
   
def omclient():
   try:
        subprocess.run(["python", 'client.py'])
   except FileNotFoundError:
      print("Opti Messager was not found!")
      pass
   
def omserver():
   try:
        subprocess.run(["python", 'server.py'])
   except FileNotFoundError:
      print("Opti Messager Server was not found!")
      pass


def hardware():
   try:
        subprocess.run(["python", 'hardwiz.py'])
   except FileNotFoundError:
      pass

def run_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
        subprocess.run(["python", file_name])
    except FileNotFoundError:
        txt1 = "File not found."
        #errormes(tt, txt1, ent)
        print(txt1)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

def accfloppy(file_name):
    prog = os.path.join(cc, "a", file_name)
    if floC == True:
        try:
            time.sleep(sleep_timeAppL)
            subprocess.run(["python", prog])
        except FileNotFoundError:
            txt1 = "File not found."
            #errormes(tt, txt1, ent)
            print(txt1)
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
    else:
        pass

def del_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
        os.remove(file_name)
    except FileNotFoundError:
            txt1 = "File not found."
            #errormes(tt, txt1, ent)
            print(txt1)
def nguess():
   try:
        subprocess.run(["python", 'nguess.py'])
   except FileNotFoundError:
      pass
   clear()

def write():
   try:
        subprocess.run(["python", 'write.py'])
   except FileNotFoundError:
      pass

def calc():
  clear()
  print("Type '0000' to exit.")
  while True:
    calci = input(format(syst["path_label"]))
    result = eval(calci)
    if result == 0000:
       clear()
       break
    else:
        print("=", result)
    print()

def gpu():
    print("Moved to 'hardware' command")
def modem():
    print("Moved to 'hardware' command")

#code that runs every python file from autostart.txt
def autos():
    # Read configuration file
    with open("autostart.txt", "r") as file:
        lines = file.readlines()

    # Process each line (assuming lines are valid)
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line.startswith("#"):  # Skip comments
            continue

        # Import modules
        if line.startswith("import"):
            exec(line)  # Use exec with caution (see Security Considerations)

        # Execute functions
        elif line:
            exec(line + "()")  # Execute the function
#autos()
def mainOS():
    clear()
    nameO()
    while True:
        inp = input(f"O:/> ")
        inp = inp.lower()
        if inp in ('bios', 'info', 'cls', 'exit', 'help', 'restart', 'modem', 'internet', 'calc', 'resethardware', 'configuration', 'upkeep', 'confighelp', 'remids'):
            eval(inp)()
        elif inp.startswith('run '):
            run_file(inp[4:])
        elif inp.startswith('del '):
            del_file(inp[4:])
        elif inp.startswith(':a '):
            accfloppy(inp[3:])
        elif inp == 'dir':
            time.sleep(sleep_timeAppL)
            print("Current directory: O:\\")
            files = os.listdir(".")
            for f in files:
                file_type = os.path.isfile(f) and "File" or "Folder"
                size = os.path.getsize(f)
                print(f"{file_type:8s} {f:20s} {size:8,d}")
        elif inp.startswith('open '):
            open_text(inp[5:])
        #elif inp == "api.interface":
           #interface()
        #elif inp == "api /?":
           #apihelp()
        elif inp == "dvcman":
            time.sleep(sleep_timeAppL)
            print()
            print("Identified Hardware:")
            linebr(20)
            time.sleep(sleep_timeIAppL)
            print("ACPI Based Computer:")
            time.sleep(sleep_timeIAppL)
            print("  Motherboard - "+mb_module.mName)
            time.sleep(sleep_timeIAppL)
            print("  Physical Memory - "+mb_module.mMemS)
            time.sleep(sleep_timeIAppL)
            linebr2(20)

            print("Processors:")
            time.sleep(sleep_timeIAppL)
            print("  Processor - "+cpu_module.cName)
            time.sleep(sleep_timeIAppL)
            print("  Processor Speed - "+cpu_module.cFreqS+cpu_module.cFreqUnit)
            time.sleep(sleep_timeIAppL)
            linebr2(20)

            print("Storage Devices:")
            time.sleep(sleep_timeIAppL)
            print("  Hard Disk - "+hd_module.hddnameS)
            time.sleep(sleep_timeIAppL)
            print("  Hard Disk Storage - "+hd_module.hddspaceS)
            time.sleep(sleep_timeIAppL)
            print("  Free Hard Disk Storage -",freesp, "KB")
            
            if floC == True:
                time.sleep(sleep_timeAppL)
                print("  Floppy Drive -",flo_module.floname)
            else:
                pass
            linebr2(20)
            if gpuC == False:
                pass
            else:
                print("Graphics Adapters:")
                time.sleep(sleep_timeIAppL)
                print("  Graphic Processor - "+gpu_module.gName)
                time.sleep(sleep_timeIAppL)
                print("  Graphic Memory -",gpu_module.gVram, "MB")
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            if sond == False:
                pass
            else:
                print("Sound Devices:")
                time.sleep(sleep_timeIAppL)
                print("  Sound Processor - "+son_module.soundName)
                time.sleep(sleep_timeIAppL)
                print("  Sound Chip -",son_module.soundChip)
                time.sleep(sleep_timeIAppL)
                print("  Sound Digital Format -",son_module.soundDF)
                time.sleep(sleep_timeIAppL)
                print("  Stereo Capable -",son_module.stereo)
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            if mdC == False:
                pass
            else:
                print("Internet Devices:")
                time.sleep(sleep_timeIAppL)
                print("  Modem - "+md_module.modemname, "at "+md_module.modemspeeds)
                time.sleep(sleep_timeIAppL)
                print("  Dial-Up Adapter -",md_module.dialupadp)
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            print("Display Adapters:")
            time.sleep(sleep_timeIAppL)
            print("  Monitor Resolution - "+mon_module.monitorRes, mon_module.monitorHz)
            linebr2(20)
            print("  Operating System - "+osName, osVersion)
            linebr(20)
            print()
        elif inp == "var":
           if settings['computer_name'] == "DEBUG_MODE":
                print("osName", osName)
                print("osVersion", osVersion)
                print("config", config)
                print("gpuC", gpuC)
                print("intern", intern)
                print("VERSTRING:", op2v.op2VERSTRING)
                print("sond", sond)
                print("inp", inp)
           #print("files", files)

        elif inp == "settings":
            if ex == True:
                cls()
                while True:
                    cls()
                    print("What do you wanna change?")
                    linebr(20)
                    print("1 - Computer Name")
                    print("2 - Exit")
                    linebr(20)
                    ch = input("> ")
                    if ch == "1":
                        new = input("Type in your desired name: ")
                        settings['computer_name'] = new
                        with open('op2.ini', 'w') as a:
                            config.write(a)
                        print("SET!")
                        break
                    elif ch == "2":
                        break
        elif inp == "api.update":
            if intern == 1:
                print()
                os.remove('op2api.py')
                print("Contacting Server...")
                time.sleep(2)
                print("Downloading...")
                u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Updates/op2api.py"
                response = requests.get(u1)
                print("op2api.py...")
                print()
                with open("op2api.py", "wb") as f:
                    f.write(response.content)
                    f.close()
                print("COMPLETED!")
                print("Make sure to restart...")
                print()
        else:
            print("Unknown command")


