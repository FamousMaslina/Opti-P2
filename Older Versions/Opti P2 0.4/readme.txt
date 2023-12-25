Opti P2 - an "OS" made in Python. (written for Version 0.4)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
identifier.py - Secondary File (Needed by op2.py and bios.py)
bios.ini - Config File for bios.py (Not needed)
'cpus' folder - Important folder (Needed):
	c1862.py - 186Cpu, 2MHz
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
'mbs' folder - Important folder (Needed):
	286basic.py - 286Motherboard, 1024KB
	386basic.py - 386Motherboard, 2048KB
'gpus' folder - Extras folder (Not Needed):
	ATI Mach 32.py - GPU, 10MHz, 2MB
	S3 ViRGE.py - GPU, 5MHz, 2MB

How to?
Check if the root directory has any cpus or mbs files. If not, Opti P2 will not run. If it dosen't check the 'cpu' and 'mb' folder and
copy one of the files from there to the root directory where op2.py, bios.py and identifier.py is.
Execute op2.py and it should run fine. (Executing bios.py or identifier.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.
You can also install GPUs by copying one of the files from the 'gpus' folder to the directory where op2.py is!

CPUs & Motherboards documentation:
Each CPU and Motherboard is unique in it's way. (For now, just the frequency from the CPU). You can modify any 
files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))

GPUs documentation:
Each GPU is unique aswell. But now, those values and all aren't used somewhere yet. It could be in the future.

UpdateLog:
-Made bios.py able to change settings in the bios.ini
-Added new entry to bios.ini
-Added GPUs support! (anything works, because they are identified by op2.py itself!)
-Added new commands to Opti P2: 'gpu',  'gpuinfo'
							  
