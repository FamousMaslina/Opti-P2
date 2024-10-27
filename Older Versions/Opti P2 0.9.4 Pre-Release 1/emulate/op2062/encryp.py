try:
    import op2api as api
    api.check()
except ImportError:
    print("API not found/ not working")
a = 124
b = 1241
c = 2145
d = 123154
e = 254
f = 214154
g = 21313123
h = 1231321321
i = 2145465
j = 124124324
k = 123131225
l = 1231231321
m = 12313215478
n = 213123123
o = 1023154
p = 124567012
r = 1245468546
s = 9123428234853
t = 912492395423
u = 12381283
v = 912381923
x = 81283919823
y = 19012093102
w = 123123546
z = 910293102931
global nbreak
nbreak = "============"
encryption_dict = {
    'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h,
    'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p,
    'r': r, 's': s, 't': t, 'u': u, 'v': v, 'x': x, 'y': y, 'w': w, 'z': z,
}

def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            char = char.lower()
            encrypted_text += str(encryption_dict[char]) + ' '
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = ''
    encrypted_tokens = encrypted_text.split()
    for token in encrypted_tokens:
        for char, value in encryption_dict.items():
            if str(value) == token:
                decrypted_text += char
                break
        else:
            decrypted_text += token
    return decrypted_text
api.clear()
vers = "0.1.1"
def main():
    api.time.sleep(api.sleep_timeIAppL)
    while True:
        api.clear()
        print("ENCRYP", vers)
        print(nbreak)
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Exit")
        print(nbreak)
        encr = input("> ")
        if encr == "1":
            api.clear()
            text_to_encrypt = input("Text to encrypt: ")
            encrypted_text = encrypt(text_to_encrypt)
            api.time.sleep(api.sleep_timeIAppL)
            print("Encrypted:", encrypted_text)
            print()
            input("Press enter to go back...")
        elif encr == "2":
            api.clear()
            text_to_ncrypt = input("Text to decrypt: ")
            decrypted_text = decrypt(text_to_ncrypt)
            api.time.sleep(api.sleep_timeIAppL)
            print("Decrypted:", decrypted_text)
            print()
            input("Press enter to go back...")
        elif encr == "3":
            api.clear()
            exit()
main()
