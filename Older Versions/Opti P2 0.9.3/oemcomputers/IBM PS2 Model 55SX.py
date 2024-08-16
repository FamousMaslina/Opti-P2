pcName = "IBM PS/2 Model 55SX"
lockedB = False
nnnnna = True

cName = "Intel 80386SX"
cFreq = 16
cFreqS = "16"
cFreqUnit = "MHz"
asdawd2k3a403 = "386"

mName = "Basic 386 Motherboard"
mMem = 2048
mMemS = "2048 KB"
spCpus = "386"
onboardGPU = False
gName = ""
gFreq = ""
gMem = ""
bcode = ""
ioaoooss = True
mFreqUnit = "MHz"

floname = "3.5 Floppy Drive"
firin = True

monitorName = "VGA & MCGA Compatible Monitor"
monitorRes = "640x480"
monitorHz = "60Hz"
monitorHzI = 60
monitorAspectRation = "4:3"
mmmnni = True


keyName = "BASIC PS/2 KEYBOARD"
kkeyb = True

hddnameS = "GENERIC IDE DISK"
hddspace = 32000
hddspaceS = "32MB"
kajsaed = True

gName = "Generic Graphics Card"
gSpeed = 2
gSpeedS = "2 MHz"
gps = 1
gvs = 0
grop = 1
gVram = 1
gbit = "8 Bits"
odasfsdfds3 = True
import time
from os import *
ver = 1.0
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def shadowgpu():
    clear()
    print(gName, "VGA BIOS.", ver)
    print(gVram, "MB loaded.")
    time.sleep(0.7)

