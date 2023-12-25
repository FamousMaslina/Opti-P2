try:
    import op2api as api
except ImportError as e:
    print("API failed to import", e)
    input("Press enter to exit...")
    exit()
global vers
vers = 0.1
global nbreak
nbreak = "============"
def num1():
    api.time.sleep(api.sleep_timeIAppL)
    count = 0
    api.clear()
    while True:
        api.clear()
        num = api.random.randint(0, 9)
        print("I'm thinking of a number...")
        while True:
            guess = int(input("Your guess: "))
            if guess == num:
                print("Very well! The number was", num)
                print("It took you", count, "times to guess the number!")
                print()
                pg = input("Play again? Y/N ")
                pg = pg.lower()
                if pg == "y":
                    break
                else:
                    return
            elif guess < num:
                print("Higher...")
                print()
                count = count+1
            elif guess > num:
                print("Lower...")
                print()
                count = count+1

def num2():
    api.time.sleep(api.sleep_timeIAppL)
    count = 0
    api.clear()
    while True:
        api.clear()
        num = api.random.randint(10, 99)
        print("I'm thinking of a number...")
        while True:
            guess = int(input("Your guess: "))
            if guess == num:
                print("Very well! The number was", num)
                print("It took you", count, "times to guess the number!")
                print()
                pg = input("Play again? Y/N ")
                pg = pg.lower()
                if pg == "y":
                    break
                else:
                    return
            elif guess < num:
                print("Higher...")
                print()
                count = count+1
            elif guess > num:
                print("Lower...")
                print()
                count = count+1

def num3():
    api.time.sleep(api.sleep_timeIAppL)
    count = 0
    api.clear()
    while True:
        api.clear()
        num = api.random.randint(100, 999)
        print("I'm thinking of a number...")
        while True:
            guess = int(input("Your guess: "))
            if guess == num:
                print("Very well! The number was", num)
                print("It took you", count, "times to guess the number!")
                print()
                pg = input("Play again? Y/N ")
                pg = pg.lower()
                if pg == "y":
                    break
                else:
                    return
            elif guess < num:
                print("Higher...")
                print()
                count = count+1
            elif guess > num:
                print("Lower...")
                print()
                count = count+1

def num4():
    api.time.sleep(api.sleep_timeIAppL)
    count = 0
    api.clear()
    while True:
        api.clear()
        num = api.random.randint(1000, 9999)
        print("I'm thinking of a number...")
        while True:
            guess = int(input("Your guess: "))
            if guess == num:
                print("Very well! The number was", num)
                print("It took you", count, "times to guess the number!")
                print()
                pg = input("Play again? Y/N ")
                pg = pg.lower()
                if pg == "y":
                    break
                else:
                    return
            elif guess < num:
                print("Higher...")
                print()
                count = count+1
            elif guess > num:
                print("Lower...")
                print()
                count = count+1
        
def main():
    api.time.sleep(api.sleep_timeIAppL)
    while True:
        api.clear()
        print("Number Guessing!", vers)
        print(nbreak)
        print("1 - Easy (1 Digit Number)")
        print("2 - Medium (2 Digit Number)")
        print("3 - Hard (3 Digit Number)")
        print("4 - Extreme (4 Digit Number)")
        print("5 - Exit")
        print(nbreak)
        choice = input("> ")
        if choice == "1":
            num1()
        elif choice == "2":
            num2()
        if choice == "3":
            num3()
        elif choice == "4":
            num4()
        elif choice == "5":
            exit()

try:
    import op2api as api
    api.check()
    if api.apiverI < 0.2:
        print("Cannot load: Too low API version. Expected Version 0.2")
        input("")
        exit()
    elif api.apiverI == 0.2 or api.apiverI > 0.2:
        main()
except ImportError:
    print("API not found/ not working")