import time
import random
from playsound import playsound
from prettytable import PrettyTable
from os import *
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("Copyright 1982-1990 Python Star")
print("===============================")
time.sleep(1)
print("Starting PS Check...")
time.sleep(0.2)
print("4MB Ram OK")
time.sleep(0.5)
mytable = PrettyTable(["CPU", "GPU", "MODEM", "SOUNDCARD"])

mytable.add_rows([
    ["i486", "BUILT-IN", "UNKONW", "Creative Soundblaster 2.0"],
    ["32-Bit", "-", "-", "8-bit DAC"],
    ["16 MHz", "-", "-", "44 kHZ Play_back"],
])
print(mytable)

time.sleep(0.5)
print("Normal KeyBoard... Detected")
time.sleep(1)
print("Checking HDD Free Space...")
time.sleep(1.5)
print("1.5 MB Free")
time.sleep(0.5)

print("Booting...")
time.sleep(3)
print()
print("-----Type 'help' to get started----- Or 'ulog' to see the update log")
print()
while True: 
    playerChoice = input("P:\Python ")
    if playerChoice == "about":
        print("PyOS V1.4.1")
    elif playerChoice == "install -f framework":
        print("Searching...")
        time.sleep(10)
        print("Found!")
        print("Downloading...")
        time.sleep(8)
        print("Installing...")
        time.sleep(15)
        print("Installation succesful!")
        print("Shutdown to apply changes!")
        print("Saving Data...")
        time.sleep(5)
        input("Prees enter to exit")
        exit()
    
    elif playerChoice == "shutdown":
        print("Saving Data...")
        time.sleep(5)
        input("Prees enter to exit")
    elif playerChoice == "update -f -ps":
        print("No update found!")

#=============================================================
    elif playerChoice == "crash -p":
        print("OyrWj2uiDZQNBGoHf;ARMkIKx")
        input("rePe NEtr ot cLosa..")
        exit()
    elif playerChoice == "D:":
        playerChoice = input("D: ")
        if playerChoice == "dir":
            print("setup.exe")
            playerChoice = input("D:")
            if playerChoice == "setup.exe":
                print("     Welcome To MS-dos Setup")
                playerChoice = input("MS-Dos Setup:")
                if playerChoice == "install":
                    print("Starting..")
                    time.sleep(1)
                    print("Creating Folders")
                    time.sleep(0.2)
                    print("ERROR!")
                    input(" Press enter to restart")
                    exit()
                elif playerChoice == "no":
                    input(" Press enter to restart")
                    exit()
            else:
                input(" Press enter to restart")
                exit()
    elif playerChoice == "drives":
        print("Discoverd - P: D:")
    elif playerChoice == "ulog":
        print()
        print("V1.4.1 The 'Count Update' No more exiting the launcher, added 'cls'")
        print("===============")
        print("V1.4 The 'Media Player Update'. This update adds media player wicth can be used by typing 'player'")
        print("===============")
        print("V1.3 The 'System Utilities And Security Update', is leveling up the Utilities and Security tools for Py OS,")
        print("making it more secure")
        print("===============")
        print("V1.2 'The PS Update' changes the UI from the PS Checker. A new app called 'write' wich you can write!")
        print("===============")
        print("1.1 Brings you new helpful commands and a new easter egg. And some tweaks!")
        print()
    elif playerChoice == "help":
        print("Basic Commands:")
        print()
        print("about")
        print()
        print("install -f (program name)")
        print()
        print("shutdown")
        print()
        print("disclaimer")
        print()
        print("(drive letter):")
        print()
        print("ulog")
        print()
        print("drives")
        print()
        print("dir in a dirve to see his contents")
        print()
        print("internet")
        print()
        print("overclock")
        print()
        print("write")
        print()
        print("save (while in write.py)")
        print()
        print("format (drive letter):")
        print()
        print("tkill -f program name")
        print()
        print("player")
        print()
        print("cls")
        print("========================")
        print("Special")
        print()
        print(" '-f' in installing input means 'fast'.")
        print()
        print("In other cases '-f' means 'force'.")
        print()
    elif playerChoice == "write":
        print("Start typing something: Please note that anything will not be saved")
        print("Even if you type save will not be saved. Wired...")
        print()
        playerChoice = input("")
        print()
        print()
        playerChoice = input("P:\Python ")
        if playerChoice == "save":
            playerChoice = input("Choose format - ASCI | UTF-8 ")
            if playerChoice == "asci":
                print("Saved")
            elif playerChoice == "utf-8":
                print("Saved")
            else:
                input("sytem halted. reason: unknow")

    elif playerChoice == "overclock":
        print("Starting CPU and GPU OverCloking...")
        print("This may approxamitivily 50 seconds. Please be patient")
        time.sleep(1)
        playsound('over.mp3')
        time.sleep(5)
        print("OverClocking Succesful!")
    elif playerChoice == "internet":
        print("Can't open the internet since you dont have a modem")
    elif playerChoice == "install -f proantivirus":
        print("Searching...")
        time.sleep(0.2)
        print("Found!")
        print("Installing")
        time.sleep(1)
        input("Something happend. Please restart your system. Reason: Potential UnWanted Program")
        exit()
    elif playerChoice == "format P:":
        print("Cannot format the main drive")
        input("System halted due sercurity. Please restart. Reason: Inputed format primary drive")
        exit()
    elif playerChoice == "format -f P:":
        print("Formating...")
        time.sleep(1)
        print("Cannot Format P: Drive.")
        print("Reason: driveinfo.cf file reported that P: is primary")
        print("Reason: A file is being used: system.py. Close the program in order to continue")
        input("Restart the system due sercurity resons")
        exit()
    elif playerChoice == "tkill system.py":
        print("Cannot kill a system program")
    elif playerChoice == "tkill -f system.py":
        print("Cannot kill a system program")
    elif playerChoice == "nadder":
        x = input("Type a number ")
        y = input("Type the second number")
        print(x + y)
        x = input("Type a number ")
        y = input("Type the second number")
        print(x + y)
    elif playerChoice == "credit":
        print()
        print("=====The Team=====")
        print()
        print("Programmer - ArielAutomat")
        print("Table - PrettyTable Module")
        print("Sound Effect - YouTube,ChromeExperiments,PlaySound Module")
        print("Inspiration: MS-Dos")
        print("For some commands: ma_joc_minecraft on Tiktok")
        playerChoice = input("P:\Thank You!")
    elif playerChoice == "player":
        print("Type 1/2 to play songs")
        print()
        playerChoice = input("1-Happy Day 2-Exited 3-Happier 4-Great 5-Modern 6-fire 7-Bass")
        if playerChoice == "1":
            playsound('happyday.mid')
        elif playerChoice == "2":
            playsound('ex.mid')
        elif playerChoice == "3":
            playsound('happier.mid')
        elif playerChoice == "4":
            playsound('great.mid')
        elif playerChoice == "5":
            playsound('modern.mid')
        elif playerChoice == "6":
            playsound('fire.mid')
        elif playerChoice == "7":
            playsound('bass.mid')

    elif playerChoice == "cls":
        clear()
    else:
        print("Bad command")

