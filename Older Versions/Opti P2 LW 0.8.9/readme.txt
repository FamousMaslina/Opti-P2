Opti P2 LW- an "OS" made in Python. (written for Version 0.8.9)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.

(THIS IS A CUT DOWN VERSION OF OP2! IT DOESN'T REQUIRE THE USE OF AN API!)

Scroll all the way down for the update log!


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
op2v.py - Version file for op2.py and op2api.py (NEEDED!)
bios.ini - Config File for bios.py (Not needed)

How to?
Check if the root directory has any cpus, mbs, hard, monitors and keyboard files. If not, Opti P2 will not run. If it dosen't check the 'cpu', 'hdd', 'monitors', 'keyboard' and 'mb' folder and copy one of the files from there to the root directory where op2.py, bios.py is.
Execute op2.py and it should run fine. (Executing bios.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.
You can also install GPUs or Modem by copying one of the files from the 'gpus' (or modems) folder to the directory where op2.py is!
Or even sound cards!

CPUs & Motherboards documentation:
Each CPU and Motherboard is unique in it's way. (For now, just the frequency from the CPU). You can modify any 
files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))

HDD documentation:
The only thing that HDD manipulate is the space: OP2 will throw a warning if it has under 2000KB.

UpdateLog:
-----1A (LW)-----
-Removed thousand of lines of code
-Removed API
-Removed GPUs, SoundCards, Floppies.




