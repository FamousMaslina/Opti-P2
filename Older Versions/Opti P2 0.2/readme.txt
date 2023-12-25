Opti P2 - an "OS" made in Python. (written for Version 0.2)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
bios.ini - Config File for bios.py (Not needed)
'cpu' folder - Important folder (Needed):
	c28610.py - 286Cpu, 10MHz
	c28612.py - 286Cpu, 12MHz
	c28620.py - 286Cpu, 20MHz
	cpuDef.py - 286Cpu, 6MHz
	cpu.py - Current CPU in the machine ;) (for fun ofc)

How to?
Check if the root directory has any cpus files. If not, Opti P2 will not run. If it doesn't check the 'cpu' folder and
copy one of the files from there to the root directory where op2.py and bios.py is.
Execute op2.py and it should run fine. (Executing bios.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.

CPUs documentation:
Each CPU is unique in its way. (For now, just the frequency). You can modify any files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))
(and also, don't change the name of any of the files, it will not work otherwise.)