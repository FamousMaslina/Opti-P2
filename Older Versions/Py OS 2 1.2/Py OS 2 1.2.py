count = 0
count5 = 0
import time
from prettytable import PrettyTable
from playsound import playsound
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
count1 = 0
count2 = 0
import random
upperL = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
lowerL = upperL.lower()
digits = "0123456789"
symbols = ",<>./?;':"
#ends here



print("Copyright 1982-1995 Python Star")
print("===============================")
time.sleep(1)
print("Starting PS Check...")
time.sleep(0.2)
print("16MB Ram OK")
time.sleep(0.5)
mytable = PrettyTable(["CPU", "GPU", "MODEM", "SOUNDCARD"])

mytable.add_rows([
    ["i486", "STG2000", "UNKONW", "Audio Blast"],
    ["32-Bit", "32-Bit", "-", "16-bit DAC"],
    ["16 MHz", "75 MHz", "-", "89 kHZ Play_back"],
])
print(mytable)

time.sleep(0.5)
print("Normal KeyBoard... Detected")
time.sleep(1)
print("Checking HDD Free Space...")
time.sleep(1.5)
print("3MB Free Out of 5MB")
time.sleep(0.5)
print("Booting...")
print()
print("Type help to get started!")




while count < 5:   
    os = input("P:\Python ")
    if os == "about":
        print()
        print("Py OS 2 | Built on 'Count Technology V1'")
        print("1.2")
        print()
    elif os == "ulog":
        print()
        print("1.2 Updates:")
        print("Added the 'Colorama' Module to make things")
        print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}L{Fore.MAGENTA}O{Fore.RED}R{Fore.CYAN}F{Fore.RED}U{Fore.WHITE}L{Fore.RED}L{Fore.YELLOW}")
        print("Plus some Quality")
        print()
    elif os == "is it infinite?":
        print("Yes, brother..")
    elif os == "cpudoom.py":
        while count1 < 5:
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 70
            amount = 50

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
        
    elif os == "virusscanner":
        print("scanning...")
        time.sleep(1)
        print("System Clean!")
    elif os == "help":
        print()
        print("'ulog' to see the update log")
        print("'about' to see about Py OS 2")
        print("'virusscanner' to scan your system")
        print("'pybrowser' to acces the internet!")
        print("'drives' to see the connected drives")
        print("'rating' to see how powerful your hardware is")
        print("'overclock' to overclock your CPU")
        print("'write' to write and open .txt files")
        print("'tkill (program name)' or 'tkill -f (program name)' to close a program")
        print("'format (drive letter)' or 'format -f (drive letter)' to format a drive")
        print("'nguesser' to play a little game!")
        print("'passcracker' to crack passwords!")
        print()
        print("-F letters")
        print("In tkill commands those f's just mean 'force'")
        print("Otherwise in format means 'fast'")
        print()
    elif os == "pybrowser":
        print("Can't acces the internet")
        print("Reason: No Modem Found")
        modem = input("Want to search for a modem again? (y=yes n=no)")
        if modem == "y":
            print("Detecting..")
            time.sleep(2)
            print("Not Found!")
            m2 = input("Want to select one from the list manually? (y=yes n=no)")
            if m2 == "y":
                modems = input("1=Py Modem, 2=Standart Modem, 3=Other")
                if modems == "1":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                elif modems == "2":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                elif modems == "2":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                else:
                    print("Internet setup canceld.")
            elif m2 == "2":
                print("Internet setup canceld.")
            else:
                print("Internet setup canceld.")
        elif modem == "n":
            print("Internet setup canceld.")
        else:
            print("Internet setup canceld.")
    
    elif os == "defrag":
        print("starting defraging P:...")
        while count2 < 5:
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 10
            amount = 1

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
                print("1%...")
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 70
            amount = 50

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
                print("?%...")
    elif os == "techhelp":
     upper, lower, nums, syms = True, True, True, True
     all = ""
     if upper:
         all += upperL
     if lower:
         all += lowerL
     if nums:
         all += digits
     if syms:
         all += symbols
     lenght = 70
     amount = 1

     for x in range(amount):
         password = "".join(random.sample(all, lenght))
         print(password)
        
         print("Is a System Parameter that uses to load apps from hdd")
         print("If this shows no your screen then something is not good!")
    elif os == "D:":
         print("Contents of D: setup.py, readme.txt")
         d = input("D: ")
         if d == "setup":
             print()
             print("Windows 95 Setup")
             print()
             print("Installing Windows 95...")
             print("Transforming system.py to system.exe")
             print("The installation was unsuccsesfull")
         elif d == "readme":
             print("Cant open the file")
    elif os == "drives":
        print("Connected drives: P: D:")
    elif os == "rating":
        print("Intialnizing PS Hardware Rating Module...")
        time.sleep(1)
        print("CPU = 8/10")
        time.sleep(1)
        print("GPU = 10/10")
        time.sleep(1)
        print("RAM = 10/10")
        time.sleep(1)
        print("MODEM = ?")
        time.sleep(1)
        print("SOUNDCARD = 9/10")
        time.sleep(1)
        print("HDD = 7/10")
        print("Calculating score...")
        time.sleep(1)
        print("Overall rating: 8")
        playsound('TADA.WAV')
    elif os == "overclock":
        sure = input("Are you sure you want to overclock? ")
        if sure == "y":
            print(f"{Fore.RED}WARNING! THE OVERCLOCK IS LOUD!!")
            print("Starting CPU Overclocking...")
            playsound('over.mp3')
    elif os == "write":
        print("Start typing something: Please note that anything will not be saved")
        print("Even if you type save will not be saved. Wired...")
        print("When you are done type 'save'")
        print()
        print()
        playerChoice = input("")
        print()
        print()
        write = input("Write ")
        if write == "save":
            print("Saved!")
        elif write == "dont save":
            print("Not Saved!")
        else:
            print("Not Saved!")
    elif os == "credit":
        print()
        print("=====The Team=====")
        print()
        print("Programmer - ArielAutomat")
        print("Table - PrettyTable Module")
        print("Sound Effects - YouTube, ChromeExperiments, PlaySound Module")
        print("Inspiration: MS-Dos")
        print("For some commands: ma_joc_minecraft on Tiktok")
        print("Thank You!")
        print()

    elif os == "tkill system.py":
        print("Cannot kill a system program")
    elif os == "tkill -f system.py":
        print("Cannot kill a system program")
    elif os == "format P:":
        print("Cannot format the main drive")
       
    elif os == "format -f P:":
        print("Formating...")
        time.sleep(1)
        print("Cannot Format P: Drive.")
        print("Reason: driveinfo.cf file reported that P: is primary")
        print("Reason: A file is being used: system.py. Close the program in order to continue")
    elif os == "format -f D:":
        print("Formating...")
        time.sleep(1)
        print("Done!")
    elif os == "format D:":
        print("Formating...")
        time.sleep(5)
        print("Done!")
    elif os == "nguess":
        print("     Py Game Studios    ")
        time.sleep(1)
        print("        Presents        ")
        time.sleep(1)
        print()
        print("     Number Guesser     ")
        print()
        print("1-Ez = 1 Number")
        print("2-Mid = 2 Numbers")
        print("3-Hard = 5 Numbers")
        print("4-RAGE QUIT = 10 Numbers :/")
        print()
        dif = input("Choose dificulty: 1-Ez 2-Mid 3-Hard 4-AHH THIS GAME!")
        if dif == "1":
            while count5 < 5:
                nums = True
                all = ""
                if nums:
                    all += digits
                lenght = 1
                amount = 1

                for x in range(amount):
                    password = "".join(random.sample(all, lenght))
                    print("I think about a number...")
                    guess = input("What number do you thing is it? ")
                    if guess == password == guess:
                        print()
                        print("Great!")
                        print()
                else:
                    print(password)
        elif dif == "2":
            while count5 < 5:
                nums = True
                all = ""
                if nums:
                    all += digits
                lenght = 2
                amount = 1

                for x in range(amount):
                    password = "".join(random.sample(all, lenght))
                    print("I think about a number...")
                    guess = input("What number do you thing is it? ")
                    if guess == password == guess:
                        print()
                        print("Great!")
                        print()
                else:
                    print(password)                   
        elif dif == "3":
            while count5 < 5:
                nums = True
                all = ""
                if nums:
                    all += digits
                lenght = 5
                amount = 1

                for x in range(amount):
                    password = "".join(random.sample(all, lenght))
                    print("I think about a number...")
                    guess = input("What number do you thing is it? ")
                    if guess == password == guess:
                        print()
                        print("Great!")
                        print()
                else:
                    print(password)
        elif dif == "4":
            while count5 < 5:
                nums = True
                all = ""
                if nums:
                    all += digits
                lenght = 10
                amount = 1

                for x in range(amount):
                    password = "".join(random.sample(all, lenght))
                    print("I think about a number...")
                    guess = input("What number do you thing is it? ")
                    if guess == password == guess:
                        print()
                        print("Great!")
                        print()
                else:
                    print(password)
    elif os == "text":
        print(f"{Fore.RED}Red Text")
        print(f"{Fore.GREEN}Green Text")
        print(f"{Fore.CYAN}Cyan Text")
        print(f"{Fore.YELLOW}Yellow Text")
        print(f"{Fore.MAGENTA}Magenta Text")
        print(f"{Fore.BLUE}Blue Text")
        print()
        print(f"{Back.RED}Red Text")
        print(f"{Back.GREEN}Green Text")
        print(f"{Back.CYAN}Cyan Text")
        print(f"{Back.YELLOW}Yellow Text")
        print(f"{Back.MAGENTA}Magenta Text")
        print(f"{Back.BLUE}Blue Text")
        print()
    elif os == "asci":
        print("It's great!")
    elif os == "i cant install windows 95!":
        print("Sad For You, Great For Me! :)")
    elif os == "im colorblind!":
        print(f"{Fore.RED}Sad. Really...")
    elif os == "whats the clock?":
        print("idk")
    elif os == "i know your secret!":
        print("*gasp...")
    elif os == "hey! where did you code this os?":
        print("visual code 95!")
    elif os == "unknow command":
        print("Unknow Command?")
    elif os == "i want an error!":
        playsound('CHORD.WAV')
    elif os == "boop":
        playsound('DING.WAV')
     
    else:
        print("Unknow Command")
        print("Type 'help' to see some commands")
