import os
from os import name, system
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
import requests
global op2version
op2version = False
try:
    import op2v
    op2version = True
except ImportError:
    op2version = False
    pass

def main():
    cls()
    if op2version == False:
        pass
        print("Cannot identify OP2 version. Most likely under version 0.5")
    elif op2version == True:
        print("Detected Opti P2 Version", op2v.op2VER)
    print()
    input("Press enter to continue the update...")
    if op2version == False:
        try:
            os.remove("identifier.py")
            print("Removed Identifier...")
        except OSError:
            pass
        #os.remove("bios.py")
        #os.remove("bios.ini")
        #print("Removed BIOS...")
        #u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Updates/bios.py"
        #response = requests.get(u1)
        #print("bios.py...")
        #print()
        #with open("bios.py", "wb") as f:
            #f.write(response.content)
            #f.close()
        
        u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Updates/op2api.py"
        response = requests.get(u1)
        print("op2api.py...")
        print()
        with open("op2api.py", "wb") as f:
            f.write(response.content)
            f.close()
        print("Done!")
        #print("If you're under the version 0.6.2, you'll need to get the new hardware files.")
        #print("The new BIOS isn't able to recognize the old hardware files.")
        input("Press enter to exit")
        exit()
    elif op2version == True:
        #os.remove("bios.py")
        #os.remove("bios.ini")
        #print("Removed BIOS...")
        #u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Updates/bios.py"
        #response = requests.get(u1)
        #print("bios.py...")
        #print()
        #with open("bios.py", "wb") as f:
            #f.write(response.content)
            #f.close()
        
        u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Updates/op2api.py"
        response = requests.get(u1)
        print("op2api.py...")
        print()
        with open("op2api.py", "wb") as f:
            f.write(response.content)
            f.close()
        print("Done!")
        #print("If you're under the version 0.6.2, you'll need to get the new hardware files.")
        #print("The new BIOS isn't able to recognize the old hardware files.")
        input("Press enter to exit")
        exit()
main()