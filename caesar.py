#!/usr/bin/env python3
MAX_KEY     =  26

print("-Caesar Cipher Testprogram-")
print("-Choose the operation to be performed-")
op = input("Type e for encrypting a file, d for decrypting ").lower()

if op == 'e':
    print("Encrypting.")
    key = int(input("Type in key: "))
    filename = input("Type the path to a text file to encrypt: ")

    with open(filename, "r") as f:
        wholetext = f.read()

    encryptedtext = ""
    for character in wholetext:
        if character.isalpha():
            encryptedcharacter = (chr(ord(character) + key))
            if character.isupper():
                if ord(encryptedcharacter) > ord("Z"):
                    encryptedcharacter = (chr(ord(encryptedcharacter) - MAX_KEY))
            else:
                if ord(encryptedcharacter) > ord("z"):
                    encryptedcharacter = (chr(ord(encryptedcharacter) - MAX_KEY))
            encryptedtext = encryptedtext + encryptedcharacter
        else:
            encryptedtext = encryptedtext + character
    print(encryptedtext)
