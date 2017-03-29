"""
cryptography.py
Author: Earl
Credit: Sam

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

en=input("Enter e to encrypt, d to decrypt, or q to quit: ")
message=input("Message: ")
key=input("Key: ")


if en is "e":
    print("e")
elif en is "d":
    print("d")
elif not ["e","d","q"]:
    print("Did not understand command, try again.")
elif en is "q":
    print("Goodbye!")