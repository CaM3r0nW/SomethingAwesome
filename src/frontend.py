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

        encrypted = e.encrypt(msg)
        print(f"This is the message encrypted: {encrypted}")

        decrypted = e.decrypt(msg)

        raise Exception
    except:
        msg = input("Message to be sent: ")
