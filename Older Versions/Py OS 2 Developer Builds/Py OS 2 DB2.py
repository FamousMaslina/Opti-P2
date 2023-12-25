count = 0
count1 = 0
import random
upperL = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
lowerL = upperL.lower()
digits = "0123456789"
symbols = ",<>./?;':"

print("Type help to get started!")
while count < 5:   
    os = input("P:Python\ ")
    if os == "about":
        print()
        print("Py OS 2 | Built on 'Count Technology V1'")
        print("Dev Build 2")
        print()
    elif os == "ulog":
        print()
        print("Introducing Py OS 2! Finnaly you")
        print("dont need to get out of the launcher")
        print("After every command typed, thanks to")
        print("'Count Technology'")
        print()
        print("Why did we move to Py OS 2 instead")
        print("of updtaing Py OS?")
        print("Its beacuse the code neded to be writen. :/")
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
        print("'dir' to see the contetns of a folder")
    elif os == "dir":
        print("system.py, virusav.py, cpudoom.py, help.py, ascii.font, about.py, ulog.py")
    elif os == "system.py":
        print("Can't open the file")
    elif os == "virusav.py":
        print("scanning...")
        print("System Clean!")
    elif os == "help.py":
        print()
        print("'ulog' to see the update log")
        print("'about' to see about Py OS 2")
        print("'virusscanner' to scan your system")
        print("'dir' to see the contetns of a folder")
    elif os == "ascii.font":
        print("Can't open the file")
    elif os == "about.py":
        print()
        print("Py OS 2 | Built on 'Count Technology V1'")
        print("Dev Build 2")
        print()
    elif os == "ulog.py":
        print()
        print("Introducing Py OS 2! Finnaly you")
        print("dont need to get out of the launcher")
        print("After every command typed, thanks to")
        print("'Count Technology'")
        print()
        print("Why did we move to Py OS 2 instead")
        print("of updtaing Py OS?")
        print("Its beacuse the code neded to be writen. :/")
        print()
        
    else:
        print("Unknow Command")
