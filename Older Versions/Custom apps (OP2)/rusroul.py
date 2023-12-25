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

def luck():
    api.clear()
    number = api.random.randint(0, 6)
    while True:
        api.clear()
        input("Press enter to try your luck...")
        num2 = api.random.randint(0, 6)
        if num2 == number:
            while True:
                api.clear()
                print("YOU DIED!")
                print("So unfortunate!", num2,"chamber did have a bullet...")
                yn = input("Play again? Y/N")
                yn = yn.lower()
                if yn == "y":
                    break
                else:
                    return
        if num2 < number or num2 > number:
            api.clear()
            print("Phew! You're lucky!")
            print("Luckily, the", num2,"chamber didn't have a bullet...")
            input("Press enter to continue...")

def main():
    api.time.sleep(api.sleep_timeIAppL)
    while True:
        api.clear()
        print("Russian roulette", vers)
        api.linebr(20)
        print("1 - Start")
        print("2 - Exit")
        api.linebr(20)
        choice = input("> ")
        if choice == "1":
            luck()
        elif choice == "2":
            api.clear()
            exit()
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