from fileinput import filename
import os
import time
import importlib
import requests
import subprocess
import platform
modules = [
    "datetime", "bios", "os", "shutil", "playsound", "op2v",
    "configparser", "re", "filename", "time", "requests",
    "subprocess", "platform"
]

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

if os.name == 'nt':  
    python_executable = 'python'
elif os.name == 'posix': 
    python_executable = 'python3'



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
if __name__ == "__main__":
    try:
        from bios import main
    except ImportError as e:
        while True:
            print(e)
            input("SYSTEM HALTED")

from idcpu import cpu
from idmb import mb
global harddriveinstalled
harddriveinstalled = False
try:
    from idhd import hd
    harddriveinstalled = True
except ImportError:
    pass
    harddriveinstalled = False
from idkey import key
from idmon import mon
from idflo import flo
from op2api import *
global intern
intern = 0
module_name = cpu.replace('.py', '')
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
if harddriveinstalled == False:
    pass
else:
    module_name3 = hd.replace('.py', '')
    hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
module_name6 = flo.replace('.py', '')
flo_module = import_module(module_name6)
def restart():
    time.sleep(sleep_timeAppL)
    subprocess.run([python_executable, "op2.py"], check=True)
    exit()
def reboot():
    time.sleep(sleep_timeAppL)
    subprocess.run([python_executable, "op2.py"], check=True)
    exit()
subprocess.run([python_executable, "op2api.py"], check=True)
time.sleep(0.1)
import re
global cc
global prog
global fla
cc = os.getcwd()
clear()

def shutdown():
    time.sleep(sleep_timeAppL)
    print("Saving data...")
    exit()

if cpu_module.cFreq < 2.0: #was 4.77
    print("Your CPU, does not meet the minnimum requirments!")
    print("Expected Atleast 2MHz! Identified:", cpu_module.cFreqS)
    input("Press enter to exit...")
    exit()
if harddriveinstalled == False:
    pass
else:
    freesp = hd_module.hddspace - space
    freesp = round(freesp, 2)
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


config_file = 'op2.ini'

config = ConfigParser()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def handle_user_input():
    custom_section_name = input("Enter a custom section name: ")
    if custom_section_name.lower() in ['user', 'sys']:
        print(f"Error: '{custom_section_name}' is a reserved section name and cannot be used.")
        return None, None
    else:
        user_password = input(f"Enter a password for the '{custom_section_name}' account: ")
        return custom_section_name, user_password


if os.path.exists(config_file):
    config.read(config_file)
else:
    #CONFIG3
    input("OP2.INI NOT FOUND! Press enter to create a new one...")
    config.add_section('user')
    config.set('user', 'computer_name', 'DEFAULT')
    config.add_section('sys')
    config.set('sys', 'remids', '1')
    #config.set('sys', 'chkfile', '0')
    config.set('sys', 'autos', '1')
    config.set('sys', 'extensions', '1')
    config.set('sys', 'fancystart', '0')
    config.set('sys', 'password', generate_password())
    config.set('sys', 'users', '0')
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)
        print(f"Closing to apply changes. Created {config_file}")
        time.sleep(3.5)
    
    config.read(config_file)

if 'user' not in config:
    config.add_section('user')
    config.set('user', 'computer_name', 'DEFAULT')
#CONFIG2
if 'sys' not in config:
    config.add_section('sys')
    config.set('sys', 'remids', '1')
    #config.set('sys', 'chkfile', '0')
    config.set('sys', 'autos', '1')
    config.set('sys', 'extensions', '1')
    config.set('sys', 'fancystart', '0')
    config.set('sys', 'password', generate_password())
    config.set('sys', 'users', '0')


def fake_chinesemodules(modules):
    for module in modules:
        try:
            time.sleep(sleep_timeIAppL)
            imported_module = importlib.import_module(module)
            print(f"Module '{module}' loaded successfully.")
        except ImportError:
            print(f"Module '{module}' not found.")
        except Exception as e:
            print(f"An error occurred while loading module '{module}': {e}")
        

def users():
    if syst['users'] == "0":
        pass
    else:
        custom_section_name, user_password = handle_user_input()
        if custom_section_name and user_password:
            if custom_section_name not in config:
                config.add_section(custom_section_name)
                config.set(custom_section_name, 'password', user_password)
                print(f"Section '{custom_section_name}' with password added successfully.")
            else:
                print(f"Section '{custom_section_name}' already exists.")


    with open(config_file, 'w') as configfile:
        config.write(configfile)

def check_custom_users():
    custom_users = [section for section in config.sections() if section not in ['user', 'sys']]
    
    if not custom_users:
        print()
        print("No custom user made - Using Guest Account. Run 'users'.")
        print()
        return "Guest"
    elif len(custom_users) == 1:
        username = custom_users[0]
        password = config.get(username, 'password')
        linebr(45)
        entered_password = input(f"Enter password for '{username}': ")
        print()
        if entered_password == password:
            #print(f"Welcome, {username}!")
            return username
        else:
            print("Incorrect password. Using Guest Account.")
            print()
            return "Guest"
    else:
        linebr(45)
        username = input("Enter your username: ")
        if username in custom_users:
            password = config.get(username, 'password')
            entered_password = input(f"Enter password for '{username}': ")
            print()
            if entered_password == password:
                #print(f"Welcome, {username}!")
                return username
            else:
                print("Incorrect password. Using Guest Account.")
                print()
                return "Guest"
        else:
            print("Username not found. Using Guest Account.")
            print()
            return "Guest"

import configparser

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def display_config(config):
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
        print()

def modify_config(config):
    while True:
        display_config(config)
        linebr(35)
        print()
        section = input("Enter the section you want to modify (or 'exit' to quit): ")
        if section.lower() == 'exit':
            break
        if not config.has_section(section):
            print("Section does not exist. Try again.")
            time.sleep(1)
            clear()
            continue
        
        key = input(f"Enter the key in section [{section}] you want to modify (or 'exit' to quit): ")
        if key.lower() == 'exit':
            break
        if not config.has_option(section, key):
            print("Key does not exist. Try again.")
            time.sleep(1)
            clear()
            continue
        
        value = input(f"Enter the new value for {key} in section [{section}]: ")
        config.set(section, key, value)
        print(f"{key} in section [{section}] has been set to {value}.")
        time.sleep(2)
        clear()
        
def save_config(config, file_path):
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"Configuration saved to {file_path}")

def test():
    clear()
    file_path = 'op2.ini'
    config = load_config(file_path)
    while True:
        modify_config(config)
        save_config(config, file_path)
        print()
        cont = input("Do you want to continue modifying the config? (yes/no): ")
        print()
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()



settings = config['user']
syst = config['sys']

#print("Configuration settings have been updated.")
#print(f"SYS password: {config.get('sys', 'password')}")
import op2v
osName = "Opti P2"
osVersion = op2v.op2VER
clear()
check()
clear()

tt = "System"
ent = "Press enter to continue..."

def find_variables10(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(nnnnna)", line)
      if match:
        variables.append(match.group(1))
  return variables

def mainF():
  """The main function."""
  directory = os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if os.path.basename(file) != "op2.py" and os.path.basename(file) != "idmb.py" and os.path.basename(file) != "bios.py" and os.path.basename(file) != "op2api.py" and os.path.basename(file) != "hardwiz.py":
      variables = find_variables10(file)
      if variables:
        #print(file, variables)
        nme = os.path.basename(file)
        #print(nme)
        file_id = nme
        with open("idnme.py", "w") as f:
          f.write("nme = '{}'".format(file_id))
          global nmeC
          nmeC = True

mainF()
try:
    from idnme import nme
except ImportError:
    pass
    nmeC = False

init(autoreset=True)

def api():
   check()

if os.path.exists("autostart.txt"):
    pass
else:
    with open("autostart.txt", "w") as file:
        pass

global ex
ex = False
if os.path.exists('op2.ini'):
    ex = True
else:
    ex = False

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
       print(txt1)
       #errormes(tt, txt1, ent)


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
   clear()
   try:
        subprocess.run([python_executable, "vcom.py"], check=True)
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
        subprocess.run([python_executable, "hardwiz.py"], check=True)
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
#def confighelp():
    #time.sleep(sleep_timeAppL)
    #print()
    #print("Commands:")
    #linebr(80)
    #print("OS Related:")
    #print("  remids - Automatically delete pycache on startup. Current value: {}".format(syst["remids"]))
    #print("  chkfile - Check for required files on startup (Not used)")
    #linebr2(80)
    #print("To change values, just type your desired item, and it's value will be replaced.")
    #print("0 = disabled; 1 = enabled")
    #print()

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
    print("  configuration - Create/Modify the configuration file for OP2")
    if syst['users'] == "0":
        pass
    else:
        print("  users - Create new users.")
    if syst['extensions'] == "0":
        pass
    else:
        print("  manage_extensions - Manage Extensions.")
    #print("  settings - Change settings from the configuration file")
    print("  computername - Change Computer Name")
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
    print("  encryp - Encrypt Strings into numbers")
    print("  nguess - Play a little game (Expects API Version 0.2)")
    print("  write - Write Text Files")
    print("  calc - Calculator")
    print("  internet - Connect to the Internet")
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
    print("  virtualcommand - Emulate Py OS or Py OS 2 (if installed)")
    print("  omclient - Launch Opti Messager (if installed)")
    print("  omserver - Start a server for Opti Messager (if installed)")
    linebr2(20)
    print("Hardware Related:")
    print("  hardware - Identify GPUs, Modems, Sound Cards")
    print("  resethardware - Delete idgpu, idmod and idsound")
    print("  gpuinfo - Extra information about the current installed GPU")
    print("  dvcman - Current Installed Hardware")
    print("  ram - Display current remaining RAM")
    print("  flushram - Reset RAM")
    linebr2(20)
    print("API Related:") 
    print("  api - Check API version")
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

def credits():
    if settings['computer_name'] == "DEBUG_MODE":
        clear()
        print(osName,"- Made by FamousMaslina")
        linebr(50)
        print("This types of projects started for me in 2020, and now, 4 years later, I continued the project and my silly nerd\nidea of creating an Operating System.\n")
        print("Development of OP2 has started in the July of 2023 (1 year already!) and has continued ever since, expanding\nmy knowledge, skills and english grammar.\n")
        #print("And now, I consider OP2 to be a finished product, with nothing more to add... The will of updating and working\non it has decreased, and since tough times are approaching me, i'll have to stop development.\n")
        print("I know for a fact that nobody will read this, or nobody will ever download and play around with OP2 or even\nstart a modding community, but I still have hope for it! Who knows what the future holds for OP2!\n")
        #print("Thus,",op2v.op2VER,"will be the last update. (LIAAAR!)\n") #BIG FAT LIAR!
        print("Thank you to everyone who reads this and supported me in this amazing journey. <3")
        print()
        print("FamousMaslina, 4th of July 2024.")
        print("Revisited in 27th of July 2024")
        print()
    else:
        pass


def bios():
    if nmeC == False:
        time.sleep(sleep_timeAppL)
        clear()
        from bios import main
        main()
    elif nmeC == True and nme_module.lockedB == True:
        print("BIOS Locked. Cannot access.")
    elif nmeC == True and nme_module.lockedB == False:
        time.sleep(sleep_timeAppL)
        clear()
        from bios import main
        main()
    elif settings['computer_name'] == "DEBUG_MODE":
        time.sleep(sleep_timeAppL)
        clear()
        from bios import main
        main()
    else:
        time.sleep(sleep_timeAppL)
        clear()
        from bios import main
        main()


def encryp():
   try:
        subprocess.run([python_executable, "encryp.py"], check=True)
   except FileNotFoundError:
      pass
   
def omclient():
   try:
        subprocess.run([python_executable, "client.py"], check=True)
   except FileNotFoundError:
      print("Opti Messager was not found!")
      pass
   
def omserver():
   try:
        subprocess.run([python_executable, "server.py"], check=True)
   except FileNotFoundError:
      print("Opti Messager Server was not found!")
      pass


def hardware():
   try:
        subprocess.run([python_executable, "hardwiz.py"], check=True)
   except FileNotFoundError:
      pass

def run_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
        subprocess.run([python_executable, file_name], check=True)
    except FileNotFoundError:
        txt1 = "File not found."
        #(tt, txt1, ent)
        print(txt1)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

def accfloppy(file_name):
    prog = os.path.join(cc, "a", file_name)
    if floC == True:
        try:
            time.sleep(sleep_timeAppL)
            subprocess.run([python_executable, prog], check=True)
        except FileNotFoundError:
            txt1 = "File not found."
            #errormes(tt, txt1, ent)
            print(txt1)
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
    else:
        pass

#NAMEEEEE
if nmeC == False:
    pass
else:
    module_name7 = nme.replace('.py', '')
    nme_module = import_module(module_name7)





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
        subprocess.run([python_executable, "nguess.py"], check=True)
   except FileNotFoundError:
      pass
   clear()

def write():
   try:
        subprocess.run([python_executable, "write.py"], check=True)
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
import datetime
def date():
    print()
    print(datetime.datetime.now())
    print()

def hour():
    print()
    from datetime import datetime

    now = datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    print(f"Current Time: {hour}:{minute}:{second}")
    print()

def gpu():
    print("Moved to 'hardware' command")
def modem():
    print("Moved to 'hardware' command")


def autos():
    with open("autostart.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("#"):  # Skip comments
            continue

        if line.startswith("import"):
            exec(line)

        elif line:
            exec(line + "()")

def computername():
    print()
    new = input("Type in your desired name (or 'exit' to exit): ")
    if new != "exit":
        settings['computer_name'] = new
        with open('op2.ini', 'w') as a:
            config.write(a)
            print("SET!")
            print()
    else:
        pass



if syst['autos'] == "1":
    autos()
else:
    pass

#CONFIG1
def configuration():
    conf = 'op2.ini'
    if ex == False and syst['users'] == "0":
        while True:
            print(conf, "not found. Create new one? Y/N ")
            bioscr = input("")
            bioscr = bioscr.lower()
            if bioscr == "y":
                config.add_section('user')
                config.set('user', 'computer_name', 'DEFAULT')
                config.add_section('sys')
                config.set('sys', 'remids', '1')
                #config.set('sys', 'chkfile', '0')
                config.set('sys', 'autos', '1')
                config.set('sys', 'fancystart', '0')
                config.set('sys', 'extensions', '1')
                config.set('sys', 'password', generate_password())
                config.set('sys', 'users', '0')
                with open("op2.ini", 'w') as configfile:
                    config.write(configfile)
                print("Closing to apply changes. Created", conf)
                time.sleep(3.5)
                restart()
            else:
                while True:
                    txt1 = "Invalid command/ config file operation canceled."
                    #errormes(tt, txt1, ent)
                    print(txt1)
                    time.sleep(2)
                    break
    elif ex == False and syst['users'] == "1":
        print("Run 'users' instead.")
        pass          
    else:
        while True:
            txt1 =  "config already present. Operation Canceled."
            #errormes(tt, txt1, ent)
            #print(txt1)
            test()
            break
def gen():
    randomints()

def gensys():
    randomsyspass()

if syst['fancystart'] == "0":
    pass
else:
    fake_chinesemodules(modules)
    clear()

import importlib.util
def load_extensions():
    extensions = {}
    extensions_folder = 'extensions'
    if os.path.exists(extensions_folder):
        for filename in os.listdir(extensions_folder):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f'{extensions_folder}.{module_name}')
                if hasattr(module, 'commands'):
                    extensions.update(module.commands)
    return extensions
def manage_extensions():
    extensions_folder = 'extensions'
    extensions_info = []

    for filename in os.listdir(extensions_folder):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            module = importlib.import_module(f'{extensions_folder}.{module_name}')
            if hasattr(module, 'info') and hasattr(module, 'commands'):
                module_info = module.info
                module_info['commands'] = ', '.join(module.commands.keys())
                extensions_info.append(module_info)
    
    print("\n=== Installed Extensions ===")
    for ext in extensions_info:
        print(f"----------------------------------------")
        print(f"Title      : {ext['title']}")
        print(f"Version    : {ext['version']}")
        print(f"Author     : {ext['author']}")
        print(f"Description: {ext.get('description', 'No description available')}")
        print(f"Commands   : {ext['commands']}")
        print(f"----------------------------------------")

    while True:
        action = input("\nEnter 'delete <extension>' or 'exit': ").strip().lower()
        if action == 'exit':
            break
        action_parts = action.split()
        if len(action_parts) != 2:
            print("Invalid command.")
            continue

        command, ext_name = action_parts

        if command == 'delete':
            ext_file = os.path.join(extensions_folder, ext_name + '.py')
            if os.path.exists(ext_file):
                os.remove(ext_file)
                print(f"Extension '{ext_name}' deleted.")
            else:
                print(f"Extension '{ext_name}' not found.")
        else:
            print("Invalid command.")



def flush_ram():
    global available_memory
    available_memory = mb_module.mMem  # Reset the available memory to its initial value

def ram():
    print("\nRAM Available:", available_memory)
    print("Execute 'flushram' to clear programs from the memory.\n")

def mainOS():
    clear()
    nameO()
    if syst['users'] == "0":
        current_user = ""
    else:
        current_user = check_custom_users()

    # Dictionary to track RAM usage for each command
    command_ram_usage = {
        'bios': 25, 'info': 5, 'cls': 1, 'exit': 0, 'help': 20, 'gpu': 0, 
        'restart': 40, 'gpuinfo': 60, 'modem': 40, 'internet': 100, 'api': 50, 
        'encryp': 80, 'nguess': 40, 'write': 90, 'calc': 30, 'resethardware': 100, 
        'hardware': 75, 'users': 20, 'virtualcommand': 256, 'omclient': 45, 'omserver': 45, 
        'upkeep': 35, 'remids': 25, 'date': 10, 'hour': 10, 'gen': 30, 'gensys': 70, 
        'reboot': 100, 'shutdown': 10, 'configuration': 55, 'test': 60, 'credits': 25, 
        'computername': 15, 'manage_extensions': 50, 'ram': 5
    }

    default_commands = set(command_ram_usage.keys())

    extensions = {}
    if syst.get('extensions', "1") == "1":
        extensions = load_extensions()

    global available_memory
    available_memory = mb_module.mMem  # Initial available memory in KB

    while True:
        inp = input(f"O:/{current_user}> ").strip().lower()

        if inp in default_commands:
            ram_required = command_ram_usage[inp]
            if available_memory >= ram_required:
                try:
                    available_memory -= ram_required

                    if inp == 'manage_extensions':
                        if syst['extensions'] == "1":
                            extensions = load_extensions()
                            manage_extensions()
                        else:
                            print("Extensions Disabled.")
                    else:
                        command_function = eval(inp)
                        if callable(command_function):
                            command_function()
                        else:
                            print(f"Command '{inp}' is not callable.")
                except Exception as e:
                    print(f"Error executing command: {e}")
            else:
                print(f"Not enough memory to execute '{inp}'. Required: {ram_required} KB, Available: {available_memory} KB.")
                print("Run 'flushram' to clear the used up memory.")
        elif inp == 'flushram':
            flush_ram()
            print(f"\nRAM flushed. Available memory reset to {available_memory} KB.\n")
        elif inp in extensions:
            ram_required = random.randint(20, 100)  # Randomly assign RAM usage for extension commands
            if available_memory >= ram_required:
                try:
                    available_memory -= ram_required
                    extensions[inp]()
                except Exception as e:
                    print(f"Error executing extension command: {e}")
            else:
                print(f"Not enough memory to execute extension command '{inp}'. Required: {ram_required} KB, Available: {available_memory} KB.")
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
            if nmeC == False:
                pass
            else:
                print("  Computer Name - "+nme_module.pcName)
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
            if harddriveinstalled == False:
                pass
            else:
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

        #elif inp == "settings":
            #if ex == True:
                #cls()
                #while True:
                   #cls()
                    #print("What do you wanna change?")
                    #linebr(20)
                    #print("1 - Computer Name")
                    #print("2 - Exit")
                    #linebr(20)
                    #ch = input("> ")
                    #if ch == "1":
                        #new = input("Type in your desired name: ")
                        #settings['computer_name'] = new
                        #with open('op2.ini', 'w') as a:
                            #config.write(a)
                        #print("SET!")
                        #break
                    #elif ch == "2":
                        #break
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
            elif intern == 0:
                print()
                print("Not Connected to internet.")
                print()
        else:
            print("Unknown command")


try:
    import op2api
    if apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
    elif apiverI == 0.5 or apiverI > 0.5:
        if __name__ == "__main__":
            pass
except ImportError:
    print("API not found/ not working")
