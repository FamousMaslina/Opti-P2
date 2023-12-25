import os
import time
global sond
from importlib import import_module
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
    print(sounderror)
    time.sleep(4)
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
    from bios import main
except ImportError as e:
    while True:
        print(e)
        input("SYSTEM HALTED")

from idcpu import cpu
from idmb import mb
from idhd import hd
from idkey import key
from idmon import mon
global intern
intern = 0
module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
module_name3 = hd.replace('.py', '')
hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
from op2api import *
subprocess.run(["python", "op2api.py"])
time.sleep(0.1)
import re
clear()
freesp = hd_module.hddspace - space
freesp = round(freesp, 2)
if cpu_module.cFreq < 4.7:
    print("Your CPU, does not meet the minnimum requirments!")
    print("Expected Atleast 4.77Mhz! Idendtified:", cpu_module.cFreqS)
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


    
import op2v
osName = "Opti P2"
osVersion = op2v.op2VER
clear()
check()




init(autoreset=True)

def api():
   check()

def restart():
    time.sleep(sleep_timeAppL)
    os.system("op2.py")
    exit()
config = ConfigParser()
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
                with open("op2.ini", 'w') as configfile:
                    config.write(configfile)
                print("Closing to apply changes. Created", conf)
                time.sleep(3.5)
                restart()
            else:
                while True:
                    print("Invalid command/ config file operation canceled.")
                    time.sleep(2)
                    break          
    else:
        while True:
            print(conf, "already present. Operation Canceled.")
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
        print("GPU not detected. Run 'gpu' to detect.")
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
       print("No Modem Found. Run 'modem'")


#def audio():
    

def info():
    print()
    nameO()
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






def help():
    time.sleep(sleep_timeAppL)
    print()
    print("Commands:")
    linebr(20)
    print("OS Related:")
    print("  info - Display information about the OS")
    print("  cls - Clear the screen")
    print("  configuration - Create the configuration file for OP2")
    print("  settings - Change settings from the configuration file")
    print("  restart - Restart OP2")
    print("  exit - Exit the OS and the CMD")
    linebr2(20)
    print("File/Directory Managment:")
    print("  run [FILENAME.EXTENSION] - Run other files (Only Python files work)")
    print("  open [FILENAME.EXTENSION] - Open other files to read their contents (Any files work)")
    print("  dir - Show files in the current working directory (CWD)")
    linebr2(20)
    print("Applications:")
    print("  encryp - Encrypt Strings into numbers")
    print("  nguess - Play a little game (Expects API Version 0.2)")
    print("  write - Write Text Files")
    print("  calc - Calculator")
    print("  internet - Connect to the Internet")
    linebr2(20)
    print("Hardware Related:")
    print("  hardware - Identify GPUs and Modems")
    print("  resethardware - Delete idgpu, idmod and idsound")
    print("  gpuinfo - Extra information about the current installed GPU")
    print("  dvcman - Current Installed Hardware")
    linebr2(20)
    print("API Related:") 
    print("  api - Check API version")
    print("  api /? - Check API's help")
    linebr2(20)
    print("Advanced:") 
    print("  bios - Enter the BIOS")
    linebr(20)
    print()

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
        print("File not found.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
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
    calci = input("O:/int/> ")
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


def main():
    clear()
    nameO()
    while True:
        inp = input(f"O:/> ")
        inp = inp.lower()
        if inp in ('bios', 'info', 'cls', 'exit', 'help', 'gpu', 'restart', 'gpuinfo', 'modem', 'internet', 'api', 'encryp', 'nguess', 'write', 'calc', 'resethardware', 'hardware', 'configuration'):
            eval(inp)()
        elif inp.startswith('run '):
            run_file(inp[4:])
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
        elif inp == "api.interface":
           interface()
        elif inp == "api /?":
           apihelp()
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
           print("osName", osName)
           print("osVersion", osVersion)
           print("config", config)
           print("gpuC", gpuC)
           print("intern", intern)
           print("VERSTRING:", op2v.op2VERSTRING)
           print("sond", sond)
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
        else:
            print("Unknown command")

try:
    import op2api
    if apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
    elif apiverI == 0.5 or apiverI > 0.5:
        if __name__ == "__main__":
            main()
except ImportError:
    print("API not found/ not working")
