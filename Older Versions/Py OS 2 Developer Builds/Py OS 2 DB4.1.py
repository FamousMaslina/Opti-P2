count = 0
import time
#for the cpudoom
count1 = 0
count2 = 0
import random
upperL = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
lowerL = upperL.lower()
digits = "0123456789"
symbols = ",<>./?;':"
#ends here

print("Type help to get started!")
while count < 5:   
    os = input("P:Python\ ")
    if os == "about":
        print()
        print("Py OS 2 | Built on 'Count Technology V1'")
        print("Dev Build 4.1")
        print()
    elif os == "ulog":
        print()
        print("Dev Build 4.1 Updates:")
        print("Added 'techhelp'")
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
        print("System Clean!")
    elif os == "help":
        print()
        print("'ulog' to see the update log")
        print("'about' to see about Py OS 2")
        print("'virusscanner' to scan your system")
        print("'dir' to see the contetns of a folder (not availabile on P: Drive. Available on other drives D:, A:, C:, etc. Just type C: dir)")
        print("'pybrowser' to acces the internet!")
    elif os == "dir":
        print("Not available on P: Drive")
    elif os == "pybrowser":
        print("Can't acces the internet")
        print("Reason: No Modem Found")
        modem = input("Want to search for a modem again? (y=yes n=no")
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
                
    else:
        print("Unknow Command")
