import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPT
USERNAME = input("Enter username: ")
PW = input("Enter Password: ")
name = ""
credential = ""
for letter in USERNAME:
    index = chars.index(letter)
    name += key[index]
for letter in PW:
    index = chars.index(letter)
    credential += key[index]
#print(f"encrypted username: {name}")
#print(f"decrypted username") 
print(f"hidden credential: {credential}")