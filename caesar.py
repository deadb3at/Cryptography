# Caesar Cipher Algorithm
# This .py file performs encryption and decryption on the given inputs
# Any wrong results please inform me : deadb3at@protonmail.com
# Enjoy...!!!
# deadb3at, 17th July 2019, 10:00 PM IST


def encrypt(text,key):
    CT = ""

    for i in range(0,len(text)):
        char = text[i]

        if char.isspace():
            CT += char
        elif char.isupper():
            CT += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            CT += chr((ord(char) + key - 97) % 26 + 97)
        else:
            CT += char

    return CT

def decrypt(text,key):
    PT = ""

    for i in range(0, len(text)):
        char = text[i]

        if char.isspace():
            PT += char
        elif char.isupper():
            PT += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            PT += chr((ord(char) - key - 97) % 26 + 97)
        else:
            PT += char

    return PT

def brute_force(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(alphabet)):

        guess = ""

        for j in text:
            if j in alphabet:
                num = alphabet.find(j)
                num -= i

                if num < 0:
                    num += len(alphabet)

                guess += alphabet[num]
            elif j in alphabet_lower:
                num = alphabet_lower.find(j)
                num -= i

                if num < 0:
                    num += len(alphabet_lower)

                guess += alphabet_lower[num]
            else:
                guess += j


        print(guess + ' @ Key = ' + str(i))



print("\n\n========== Welcome To Caesar Cipher ! ==========\n\n")
print("What You Want To Do...?\n")
print("     Encrypt [1]  or  Decrypt [2]      \n")
print("Enter Your Choice... 1 or 2")
choice = int(input())



if choice == 1:
    print("Enter Your Text To Encrypt...")
    USER_PLAINTEXT_INPUT = input()
    print("\nCool, Now Enter The Key Value (integer)...")
    USER_KEY = int(input())
    CIPHERTEXT = encrypt(USER_PLAINTEXT_INPUT,USER_KEY)
    print("\n+----------------------------------+")
    print('\n' + CIPHERTEXT + '\n')
    print("+----------------------------------+")
else:
    print("Enter Your Text To Decrypt...")
    USER_CIPHERTEXT_INPUT = input()
    print("Do You Have The Key...?")
    print("Type 1 for Yes and 0 for No...")
    luck = int(input())

    if luck == 1:
        print("Alright... Continuing\n")
        print("Enter The Key Value...")
        key = int(input())
        PLAINTEXT = decrypt(USER_CIPHERTEXT_INPUT, key)
        print("\n+----------------------------------+")
        print('\n' + PLAINTEXT + '\n')
        print("+----------------------------------+")
    else:
        print("Awww... :(")
        print("Starting Brute-force...")
        print("Best of luck... :)\n")

        brute_force(USER_CIPHERTEXT_INPUT)

        print('\n' + "Brute Forcing Finished...")
        print("That's my best :)")
