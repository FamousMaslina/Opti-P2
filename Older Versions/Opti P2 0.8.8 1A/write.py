try:
    import op2api as api
    api.check()
except ImportError:
    print("API not found/ not working")

api.clear()
vers = "0.1"
def main():
    api.time.sleep(api.sleep_timeIAppL)
    api.clear()
    print("Write")
    print("Pressing enter will save the file.")
    print()
    wr = input("> ")
    namef = input("Name of the file: ")
    with open(namef, 'w') as f:
        f.write(wr)
    print()
    print("Saved file as", namef)
    exit()

main()
