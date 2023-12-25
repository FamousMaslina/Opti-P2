try:
    import op2api as api
except ImportError as e:
    print("API failed to import", e)
    input("Press enter to exit...")
    exit()
global version
version = True
try:
    import op2v
    version = True
except ImportError:
    pass
    version = False
global vers
vers = 0.1
global conf
global total
total = 0
def generate_random_string(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(api.random.choice(chars) for _ in range(length))
def generate_random_dif(length):
    chars = "0123456789"
    return "".join(api.random.choice(chars) for _ in range(length))
def main():
    api.time.sleep(api.sleep_timeIAppL)
    sleept = api.sleep_timecustom(50, api.cpu_module.cFreq)
    api.clear()
    print("MINER", vers)
    print("UNIVERSAL")
    api.linebr(20)
    print("Detected hardware:", api.cpu_module.cName)
    api.linebr(20)
    mon = 0  
    while True:
        print("TOTAL MINED:", mon)
        job = generate_random_string(15)
        dif = generate_random_dif(2)     
        api.time.sleep(2)
        print("JOB:", job,"DIF:", dif, "ON:", api.cpu_module.cName)
        api.time.sleep(api.random.randint(1, 9))
        print("JOB", job, "COMPLETED!")
        mon = mon + 0.0001

try:
    import op2api as api
    api.check()
    if api.apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
        exit()
    elif api.apiverI == 0.5 and api.lega == True:
        main()
    elif api.apiverI == 0.5 or api.apiverI > 0.5 and op2v.op2VER == "0.6.1" or op2v.op2VER == "0.6" or op2v.op2VER == "0.6 R2" or op2v.op2VER == "0.5 R2" or op2v.op2VER == "0.5" and api.gpuC == True:
        main()
except ImportError:
    print("API not found/ not working")