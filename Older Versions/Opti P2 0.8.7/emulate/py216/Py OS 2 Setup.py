import time

print("Welcome to Py OS 2 Setup")
print()
print("available drives: 1-Unformated HDD. Free Space 5MB")
drive = input("Choose a drive where to install Py OS2: ")
if drive == "1":
   format = input("To get on with the installation, do you want to start formatting the selected drive?")
   if format == "y":
      print("Preparing Formating...")
      time.sleep(0.5)
      print("Formating...")
      time.sleep(3)
      print("Done!")
      print()
      print("Starting Installing...")
      print("Approx. 10 Sec")
      time.sleep(1)
      print("Thank you for Choosing Py OS 2!")
      time.sleep(1)
      print()
      print("Py OS 2 was Built on 'Count Technolgy V1' where simplicity is our mission")
      time.sleep(1)
      print()
      print("Py OS 2 is simpler than MS-Dos")
      time.sleep(1)
      print()
      print("Py OS 2 is 2MB total!")
      time.sleep(1)
      print("Simpler File Browsing.")
      print("At every drive or directory, Py OS 2")
      print("autommaticly shows you his contents")
      time.sleep(2)
      print("Type 'help' to get started!")
      time.sleep(3)
      input("Done! Press enter to close the instalation and run Py OS 2 (Ver)")
   else:
      print("Setup Canceld.")
      input("Press enter to restart")

      
else:
   print("Setup Canceld.")
   input("Press enter to restart")