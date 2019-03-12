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
    pass

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
    filename = input("Enter file name to save encrypted text to: ")
    with open(filename, 'w') as f:
        f.write(encrypted_text)

elif op == 'd':
    print("Not implemented yet.")
