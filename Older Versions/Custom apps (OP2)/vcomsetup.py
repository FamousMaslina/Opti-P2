from op2api import *
import requests
setupprog("Virtual Command", True, "emulate", True, True, True, 2.0, 4000, 0.8)
#the exact format used!
#program name, custom dir, custom dir name, check api, check cpu, check size, cpu req, size req, api req
u1 = "https://raw.githubusercontent.com/FamousMaslina/Opti-P2/main/Opti%20P2/vcom.py"
response = requests.get(u1)
print("vcom.py...")
print()
with open("vcom.py", "wb") as f:
    f.write(response.content)
    f.close()

print("Done!")
print("You'll need to get your OS files manually.")
input("Press enter to exit")
exit()