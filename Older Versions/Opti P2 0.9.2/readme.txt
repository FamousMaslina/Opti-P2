Opti P2 - an "OS" made in Python. (written for Version 0.9.2| API Version 0.8)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.

Scroll all the way down for the update log!


How to use:

How to?
Check if the root directory has any cpus, mbs, hard, monitors and keyboard files. If not, Opti P2 will not run. If it dosen't check the 'cpu', 'hdd', 'monitors', 'keyboard' and 'mb' folder and copy one of the files from there to the root directory where op2.py, bios.py is.
Execute op2.py and it should run fine. (Executing bios.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.
You can also install GPUs or Modems by copying one of the files from the 'gpus' (or modems) folder to the directory where op2.py is!
Or even sound cards!

CPUs & Motherboards documentation:
Each CPU and Motherboard is unique in it's way. (For now, just the frequency from the CPU). You can modify any 
files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))

GPUs & Modems documentation:
Each GPU and Modem is unique aswell. But now, those values and all aren't used somewhere yet. It could be in the future.

HDD documentation:
The only thing that HDD manipulate is the space: OP2 will throw a warning if it has under 2000KB.


Custom apps Documentation:
All the custom apps, made by me are located in the
'Custom apps (OP2)' folder.
(Make sure to copy op2api.py in the cwd if the OP2 Version you're running is lower than 0.6)

--------------------------
How to enable Debug Mode?
	Either trhough op2POWERTOOLS.py
	Either by changing the computer name to 'DEBUG_MODE' in op2.ini
	Either by executing 'manage_tools' (if extensions are available.)

From there, you can run 'credits' and 'var' commands, exclusive to DEBUG_MODE

UpdateLog:
-----1A-----
-Features Added:
	Added a fancy start-up (enabled through op2.ini by setting 'fancystart' to 1)
	Added Extensions - A way to integrate commands easier. Check documentation for more info. (Main Readme)
	Added 'manage_extensions' command (if extensions are enabled)
	Added op2POWERTOOLS_EXT.py (use - 'manage_tools' if extensions are enabled)
	
-Features Removed:
	Removed TensorBoard Module (Useless)






