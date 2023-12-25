try:
    import op2api as api
except ImportError as e:
    print("API failed to import", e)
    input("Press enter to exit...")
    exit()
global version
version = True
try:
    import op2v
    version = True
except ImportError:
    pass
    version = False
global vers
vers = 0.1
global total
total = 0
import re
def find_python_files(directory):
  """Finds all Python files in the specified directory."""
  files = api.os.listdir(directory)
  python_files = []
  for file in files:
    if file.endswith(".py"):
      python_files.append(api.os.path.join(directory, file))
  return python_files

def find_variables(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(odasfsdfds3)", line)
      if match:
        variables.append(match.group(1))
  return variables

def mainG():
  """The main function."""
  directory = api.os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if api.os.path.basename(file) != "op2.py" and api.os.path.basename(file) != "idmb.py" and api.os.path.basename(file) != "bios.py" and api.os.path.basename(file) != "op2api.py" and api.os.path.basename(file) != "hardwiz.py":
      variables = find_variables(file)
      if variables:
        print(file, variables)
        gpu = api.os.path.basename(file)
        print(gpu)
        file_id = gpu
        with open("idgpu.py", "w") as f:
          f.write("gpu = '{}'".format(file_id))
          global gpuC
          gpuC = True

def find_variables2(file_path):
  """Finds all variables in the specified Python file."""
  variables = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"(saiop)", line)
      if match:
        variables.append(match.group(1))
  return variables

def mainM():
  """The main function."""
  directory = api.os.getcwd()
  python_files = find_python_files(directory)
  for file in python_files:
    if api.os.path.basename(file) != "op2.py" and api.os.path.basename(file) != "idmod.py" and api.os.path.basename(file) != "bios.py" and api.os.path.basename(file) != "op2api.py" and api.os.path.basename(file) != "hardwiz.py": 
      variables = find_variables2(file)
      if variables:
        print(file, variables)
        m = api.os.path.basename(file)
        print(m)
        file_id = m
        with open("idmod.py", "w") as f:
          f.write("modem = '{}'".format(file_id))
          global mdC
          mdC = True

global mod
mod = False
global gpu
gp = False
def gpu():
    print(api.gpuC)
    if api.gpuC == False:
        try:
            api.os.remove('idgpu.py')
        except FileNotFoundError:
           pass
        api.time.sleep(api.sleep_timeAppL)
        print("Detecting GPU...")
        mainG()
        api.time.sleep(api.sleep_timeIAppL)
        api.time.sleep(0.1)
        gp = True
    else:
       api.time.sleep(api.sleep_timeAppL)
       print("GPU already dectected")

def modem():
    
    print(api.mdC)
    if api.mdC == False:
        try:
            api.os.remove('idmod.py')
        except FileNotFoundError:
           pass
        api.time.sleep(api.sleep_timeAppL)
        print("Detecting Modem...")
        mainM()
        api.time.sleep(api.sleep_timeIAppL)
        api.time.sleep(0.1)
        mod = True
    else:
       api.time.sleep(api.sleep_timeAppL)
       print("Modem already dectected")



def main():
    api.time.sleep(api.sleep_timeIAppL)
    api.clear()
    print("Hardware Identifier", vers)
    api.linebr(20)
    gpu()
    modem()
    api.time.sleep(api.sleep_timeIAppL)
    api.linebr(20)
    input("Press enter to exit... (Make sure to restart OP2)")
    api.clear()
    exit()
try:
    import op2api as api
    api.check()
    if api.apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
        exit()
    elif api.apiverI == 0.5 and api.lega == True:
        main()
    elif api.apiverI == 0.5 or api.apiverI > 0.5 and op2v.op2VER == "0.6.1" or op2v.op2VER == "0.6" or op2v.op2VER == "0.6 R2" or op2v.op2VER == "0.5 R2" or op2v.op2VER == "0.5":
        main()
except ImportError:
    print("API not found/ not working")