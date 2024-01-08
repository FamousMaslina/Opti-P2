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
import os

from op2api import *
global cur
global virt
global py141
global py141f
cur = os.getcwd()
py141f = os.path.join(cur, "emulate", "py141", "Py OS.py")
py216f = os.path.join(cur, "emulate", "py216", "Py OS 2.py")
op104f = os.path.join(cur, "emulate", "op104", "opticom.py")
def main():
  api.clear()
  while True:
     
    api.clear()
    print("Virtual Command", vers)
    print("op2api CORE")
    api.linebr(20)
    print("1 - Emulate PyOS V1.4.1")
    print("2 - Emulate PyOS 2 V1.6")
    #print("3 - Emulate Opti P V0.4")
    print("3 - Exit")
    linebr2(20)
    ch = input("> ")
    if ch == "1":
      api.clear()
      try:
        time.sleep(sleep_timeIAppL)
        api.subprocess.run(["python", py141f])
      except FileNotFoundError:
        print("File not found!")
        input("Press enter to return")
    elif ch == "2":
      api.clear()
      try:
        time.sleep(sleep_timeIAppL)
        api.subprocess.run(["python", py216f])
      except FileNotFoundError:
        print("File not found!")
        input("Press enter to return")
    elif ch == "3":
       clear()
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