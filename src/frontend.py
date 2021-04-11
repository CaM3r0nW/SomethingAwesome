from caesar import caesar_encrpt, caesar_decrypt
from json import dumps, loads
"""
This file will be calling all functions, initally filled with dummy functions
To run the program this file will be called, this may change in the future.
"""
msg = input("Message to be sent: ")
while True:
    try:
        if msg == '':
            break

        encrypted = caesar_encrpt(msg, 11)

        print(f"This is the message encrypted: {encrypted}")

        decrypted = caesar_decrypt(msg, 11)

        print(f"This is the message encrypted: {decrypted}")
        raise Exception
    except:
        msg = input("Message to be sent: ")
