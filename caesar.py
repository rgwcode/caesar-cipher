#!/usr/bin/env python3
MAX_KEY     =  26

def operation(instruction):
   return input(instruction).lower()

def encrypt(text, key):
    encrypted_text = ""
    for character in text:
        if character.isalpha():
            encrypted_character = (chr(ord(character) + key))
            # handle overflowing for upper and lower
            if character.isupper():
                if ord(encrypted_character) > ord("Z"):
                    encrypted_character = (chr(ord(encrypted_character) - MAX_KEY))
            else:
                if ord(encrypted_character) > ord("z"):
                    encrypted_character = (chr(ord(encrypted_character) - MAX_KEY))
            encrypted_text = encrypted_text + encrypted_character
        else:
            encrypted_text = encrypted_text + character
    return encrypted_text

def getInputText(file = ""):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def outputText(encrypted_text):
    print("The encrypted text is:\n" + encrypted_text)

def decrypt(text, key):
    decrypted_text = ""
    for character in text:
        if character.isalpha():
            decrypted_character = (chr(ord(character) - key))
            # handle overflowing for upper and lower
            if character.isupper():
                if ord(decrypted_character) < ord("A"):
                    decrypted_character = (chr(ord(decrypted_character) + MAX_KEY))
            else:
                if ord(decrypted_character) < ord("a"):
                    decrypted_character = (chr(ord(decrypted_character) + MAX_KEY))
            decrypted_text = decrypted_text + decrypted_character
        else:
            decrypted_text = decrypted_text + character
    return decrypted_text

print("-Caesar Cipher Testprogram-")
print("-Choose the operation to be performed-")

op = ''
while not(op == 'e' or op == 'd'):
    print(op)
    op = operation("Type e for encrypting a file, d for decrypting ")

if op == 'e':
    print("Encrypting.")
    key = int(input("Type in key: "))

    whole_text = ""
    while whole_text == "":
        try:
            filename = input("Type the path to a text file to encrypt: ")
            whole_text = getInputText(filename)
        except:
            print("That file does not exist. Please try again.")

    encrypted_text = encrypt(whole_text, key)
    outputText(encrypted_text)

elif op == 'd':
    filename = input("Type the path to the text file to decrypt: ")
    with open(filename, 'r') as f:
        text = f.read()
    print(text)
    print(decrypt(text, 13))
