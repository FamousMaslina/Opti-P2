gName = "S3 ViRGE"
gSpeed = 55
gSpeedS = "5 MHz"
gps = 1
gvs = 0
grop = 1
gVram = 2
gbit = "8 Bits"
gpu = True
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
shadowgpu()