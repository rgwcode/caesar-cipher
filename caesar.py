#!/usr/bin/env python3
MIN_KEY     =   1
MAX_KEY     =  25

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

def getTextFromFile(filename, prompt = "Please enter the text file to be used: "):
    while True:
        try:
            filename = input(prompt)
            with open(filename, 'r') as file:
                text = file.read()
                return text
        except FileNotFoundError:
            print("That file does not exist. Please try again.")

def getKey(prompt = "Please enter the key: "):
    while True:
        try:
            key = int(input(prompt))
            if key >= MIN_KEY and key <= MAX_KEY:
                return key
            else:
                raise ValueError
        except ValueError:
            print(f"Error: Please enter a number between {MIN_KEY} and {MAX_KEY}.")

def saveToFile(filename, prompt = "Please enter the file name to save to: "):
    filename = input(prompt)
    with open(filename, 'w') as f:
        f.write(text)

print("-Caesar Cipher Testprogram-")
print("-Choose the operation to be performed-")

op = ''
while not(op == 'e' or op == 'd'):
    print(op)
    op = operation("Type e for encrypting a file, d for decrypting ")

if op == 'e':
    key = getKey()
    text = getTextFromFile(key)
    text = encrypt(text, key)
    saveToFile(text)

elif op == 'd':
    key = getKey()
    text = getTextFromFile(key)
    text = decrypt(text, key)
    saveToFile(text)
