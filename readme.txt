Opti P2 - So-called OS made in python. (Inspired by MS-DOS)

Why?
-it started with some old projects of mine. You can actually check them out in older versions folder. (The oldest is Py OS)

Features (0.8.X):
-Delete, create, edit, open files
-Little games included
-Message Server&Client
-Custom Hardware\Apps (even custom BIOS, if that counts)
-Custom API for certain functions used in OP2
-Flexible Hardware (you can literally put a 186 mb with a 360cpu!)
-Ability to update directly from OP2
-Setup file (if you're too lazy. (Only for 0.8.3 for now...))
-And many more in the OP2 main file!

Instructions:
-If you clone this repo, and go in the Opti P2 folder, you just have to run 'op2.py' and that's it.
-If something happens, it will output the error. (Usually uninstalled modules.)
-If you want older versions, go in the Older Versions folder and explore every version you want (It also has all the readmes with the update logs!!)
-If you want custom hardware, make sure to delete the file of the hardware that you want, and replace it with your desired one, from the folders availabe.
(CPU, MB, HDD, KEYBOARD, MONITORS are REQUIRED to run)

Modding:
-For apps:
	-You just have to program it like normal. If you want to use the API, make sure to import it.
	-Some functions:
		-Custom wait time (based per cpu speed): time.sleep(sleep_timeAppL) (example usage)
		-linebr(NUM) or linebr2(NUM): Separe text with this (linebr: = | linebr2: -)
		-The API also has some imports, like time, os, random, etc. (everything that's used in OP2)
	(You can see some examples of apps from the 'Custom Apps' folder or from the root dir of OP2. (for example: 'hardwiz.py' or 'nguess.py')
	(BIG DISCLAIMER! Custom apps are mostly compatible with the version 0.6.2 and UP!!! You can bypass this by not using any keywords like 'cpu, mb, etc')

-Hardware:
	-The easiest way to add hardware is to copy and paste an existing hardware file and modify it.
	(OP2 has cpus, floppies, gpus, hdds, keyboards, mbs, modems, soundcards and monitors (0.8.6))
	(BIOS is a pain to create. It changes everytime I add a new type of hardware, and I do not recomend it. However, you can try it...)
