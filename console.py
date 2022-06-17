from md4 import md4
from md5 import md5
from sha1 import sha1
from sha256 import sha256

# === BASIC CONSOLE PROGRAM ===
option = 0

# === MAIN MENU ===
while option != 5:
    option = int(input("[1]MD4 [2]MD5 [3]SHA-1 [4]SHA-256 [5]Exit: "))

    if option > 5 or option < 1:
        print("Invalid option\n")
        continue
    elif option == 5:
        break

    plain_text = input(" > Plain Text: ").encode('UTF-8')

    if option == 1:
        print(f" > MD4 Hash: {md4(plain_text)}\n")
    elif option == 2:
        print(f" > MD5 Hash: {md5(plain_text)}\n")
    elif option == 3:
        print(f" > SHA-1 Hash: {sha1(plain_text)}\n")
    elif option == 4:
        print(f" > SHA-256 Hash: {sha256(plain_text)}\n")

print("\nGood bye")
