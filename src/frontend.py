import encrypt as e
"""
This file will be calling all functions, initally filled with dummy functions
To run the program this file will be called, this may change in the future.
"""
msg = input("Message to be sent: ")
while True:
    try:
        if msg == '':
            break

        encrypted = e.caesar_encrpt(msg)
        print(f"This is the message encrypted: {encrypted}")

        decrypted = e.caesar_decrypt(msg)

        print(f"This is the message encrypted: {decrypted}")
        raise Exception
    except:
        msg = input("Message to be sent: ")
