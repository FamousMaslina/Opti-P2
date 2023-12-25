Opti P2 - an "OS" made in Python. (written for Version 0.6.1| API Version 0.5)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.

Scroll all the way down for the update log!


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
op2api.py - API for op2.py (NEEDED)
op2v.py - Version file for op2.py and op2api.py (NEEDED!)
bios.ini - Config File for bios.py (Not needed)
encryp.py 
nguess.py  - Extra (Not needed)
write.py 
dial.mp3 - SFX File for op2.py (Needed when executing 'internet' in op2.py)
'cpus' folder - Important folder (Needed):
	c1862.py - 186Cpu, 2MHz
	8088-4.77.py - 8088Cpu, 4.77MHz
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
	Cyrix Cx486DLC-40.py - 386Cpu, 40MHz
	Cyrix Cx486DRx2-50.py - 386Cpu, 50MHz
	Cyrix Cx486DRx2-66.py - 386Cpu, 66MHz
	cpu.py - Current CPU in the machine ;) (for fun ofc)
'mbs' folder - Important folder (Needed):
	286basic.py - 286Motherboard, 1024KB
	386basic.py - 386Motherboard, 2048KB
'hdd' folder - Important folder (Needed):
	hard4.py - IDE, 4MB
	hard8.py - IDE, 8MB
	hard16.py - IDE, 16MB
	hard32.py - IDE, 32MB
	hard64.py - IDE, 64MB
'gpus' folder - Extras folder (Not Needed):
	ATI Mach 32.py - GPU, 10MHz, 2MB
	S3 ViRGE.py - GPU, 5MHz, 2MB
'modems' folder - Extras folder (Not Needed):
	modem144.py - Modem, 14.4K

How to?
Check if the root directory has any cpus or mbs files. If not, Opti P2 will not run. If it dosen't check the 'cpu', 'hdd' and 'mb' folder and
copy one of the files from there to the root directory where op2.py, bios.py is.
Execute op2.py and it should run fine. (Executing bios.py directly will not do anything!)
After executing op2.py, and you see the O:/>  then it's good to go! Execute the command 'help' for more info.
When executing op2.py, you'll see the bios loading. If it says bios.ini found, then it's ok. If not, then execute op2.py,
execute 'bios' and select option 2 by typing '2'. It creates the config file automatically and it should be fine.
You can also install GPUs or Modem by copying one of the files from the 'gpus' (or modems) folder to the directory where op2.py is!

CPUs & Motherboards documentation:
Each CPU and Motherboard is unique in it's way. (For now, just the frequency from the CPU). You can modify any 
files from there to your liking!
And yes, it does affect loading times.
(edit cpuDef.py for comments and tips ;))

GPUs & Modems documentation:
Each GPU and Modem is unique aswell. But now, those values and all aren't used somewhere yet. It could be in the future.

HDD documentation:
The only thing that HDD manipulate is the space: OP2 will throw a warning if it has under 2000KB.

API documentation:
MOVED TO 'apidoc.txt'

Custom apps Documentation:
All the custom apps, made by me are located in the
'Custom apps (OP2)' folder.
(Make sure to copy op2api.py in the cwd if the OP2 Version you're running is lower than 0.6)

UpdateLog:
-Updated the API
-Added a custom optional App (Accessed through op2 using 'run [FILE NAME.EXTENSION]'
-BACKWARD COMPATIBLE API!!! (Works all the way from 0.6.1 to O.3! Just copy the api file
in the current working directory and done! ((ONLY perftest.py works 100% on all version until 0.3)))
-Made all the versions Click-To-Run, so you don't have to copy anything. Just run op2.py.
(If you want to change the hardware, make sure to delete the default ones and replace the ones
to your liking. And yes, every motherboard and CPU is backward compatible, until 0.3)
-Updated nguess