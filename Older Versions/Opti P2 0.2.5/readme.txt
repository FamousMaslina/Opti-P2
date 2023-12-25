Opti P2 - an "OS" made in Python. (written for Version 0.2.5)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
identifier.py - Secondary File (Needed by op2.py and bios.py)
bios.ini - Config File for bios.py (Not needed)
'cpu' folder - Important folder (Needed):
	cpuDef.py - 286Cpu, 6MHz
	c28610.py - 286Cpu, 10MHz
	c28612.py - 286Cpu, 12MHz
	c28620.py - 286Cpu, 20MHz
	c38630.py - 386Cpu, 30MHz
	c38635.py - 386Cpu, 35MHz
	c38640.py - 386Cpu, 40MHz
	Cyrix Cx486SLC-25.py - 486Cpu, 25Mhz
	Intel i386DX-40.py - 386Cpu, 40MHz
	AMD 80386DX-40.py - 386Cpu, 40MHz
	cpu.py - Current CPU in the machine ;) (for fun ofc)

How to?
Check if the root directory has any cpu's files. If not, Opti P2 will not run. If it dosen't check the 'cpu' folder and
copy one of the files from there to the root directory where op2.py, bios.py and identifier.py is.
Execute op2.py and it should run fine. (Executing bios.py or identifier.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.

CPUs documentation:
Each CPU is unique in it's way. (For now, just the frequency). You can modify any files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))

UpdateLog:
Made bios.py recognize all cpus files. It works by detecting the spMB variable, and creates another file, pointing 
to the identified filename, and it will continue to load just fine. So that means, you can make the most random cpus
and don't have to change the code, and you can name them however you want! (identifier.py does the job, and bios.py
and op2.py just reads idcpu.py)