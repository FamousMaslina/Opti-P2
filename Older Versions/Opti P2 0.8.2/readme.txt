Opti P2 - an "OS" made in Python. (written for Version 0.8.2| API Version 0.5)

made for fun, of course, and it's pretty nice, tbh. It's inspired by MSDOS and so on.

Scroll all the way down for the update log!


How to use:

Classification:
op2.py - Main File (Needed)
bios.py - Secondary File (Needed by op2.py to run)
op2api.py - API for op2.py (NEEDED)
op2v.py - Version file for op2.py and op2api.py (NEEDED!)
bios.ini - Config File for bios.py (Not needed)
hardwiz.py - File for finding Modems and GPUs
encryp.py 
nguess.py  - Extra (Not needed)
write.py 
dial.mp3 - SFX File for op2.py (Needed when executing 'internet' in op2.py)
'cpus' folder - Important folder (Needed, From the lowest frequency to the highest one):
	c1862.py - 186Cpu, 2MHz
	8088-4.77.py - 8088Cpu, 4.77MHz
	cpuDef.py - 286Cpu, 6MHz
	c28610.py - 286Cpu, 10MHz
	c28612.py - 286Cpu, 12MHz
	c28620.py - 286Cpu, 20MHz
	Cyrix Cx486SLC-25.py - 486Cpu, 25Mhz
	c38630.py - 386Cpu, 30MHz
	c38635.py - 386Cpu, 35MHz
	c38640.py - 386Cpu, 40MHz
	Intel i386DX-40.py - 386Cpu, 40MHz
	AMD 80386DX-40.py - 386Cpu, 40MHz
	Motorola 68040-40.py - 386Cpu, 40MHz
	Cyrix Cx486DLC-40.py - 386Cpu, 40MHz
	Cyrix Cx486DRx2-50.py - 386Cpu, 50MHz
	IBM PowerPC 601-50.py - 386Cpu, 50MHz
	IBM PowerPC 601-60.py - 386Cpu, 60MHz
	Cyrix Cx486DRx2-66.py - 386Cpu, 66MHz
	IBM PowerPC 601-66.py - 386Cpu, 66MHz
	Intel i486SX-66.py - 386Cpu, 66MHz
	IBM PowerPC 601-80.py - 386Cpu, 80MHz
	MIPS R6000.py - 386Cpu, 80MHz
	DEC Alpha 21064-192.py - 386Cpu, 192MHz
	DEC Alpha 21064-200.py - 386Cpu, 200MHz
	DEC Alpha 21064-225.py - 386Cpu, 225MHz
	DEC Alpha 21064-275.py - 386Cpu, 275MHz
	cpu.py - Current CPU in the machine ;) (for fun ofc)
'mbs' folder - Important folder (Needed):
	286basic.py - 286Motherboard, 1024KB
	386basic.py - 386Motherboard, 2048KB
	[MB NAME] - Folder that contains a custom
		    motherboard, with a custom
		    BIOS, that MUST be copied in the same DIRECTORY
		    where op2.py is
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
-Fixed bugs in 'resethardware' and added the ability to delete idsound.py