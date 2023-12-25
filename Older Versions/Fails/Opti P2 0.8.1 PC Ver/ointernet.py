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
global total
total = 0

def main():
    api.clear()
    if api.mdC == True:
        pass
    else:
        exit()
    print("Welcome to Opti Internet Service!")
    api.time.sleep(5)
    while True:
        clear()
        api.linebr(20)
        print("1 - Set up a new account")
try:
    import op2api as api
    api.check()
    if api.apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
        exit()
    elif api.apiverI == 0.5 and api.lega == True:
        main()
    elif api.apiverI == 0.5 or api.apiverI > 0.5 and op2v.op2VER == "0.6.1" or op2v.op2VER == "0.6" or op2v.op2VER == "0.6 R2" or op2v.op2VER == "0.5 R2" or op2v.op2VER == "0.5":
        main()
except ImportError:
    print("API not found/ not working")