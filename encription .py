import random
import string

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")

key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter

print("Encrypted:", cipher_text)

# DECRYPT
cipher_input = input("Enter text to decrypt: ")
plain_text = ""

for letter in cipher_input:
    if letter in key:
        index = key.index(letter)
        plain_text += chars[index]
    else:
        plain_text += letter

print("Decrypted:", plain_text)