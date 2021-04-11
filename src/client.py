from caesar import caesar_encrpt, caesar_decrypt, caesar_brute
from coloumn_transposition import columnar_transposition_encrypt, columnar_transposition_decrypt
from json import dump, load
"""
This file will be calling all functions, initally filled with dummy functions
To run the program this file will be called, this may change in the future.
"""
msg = input("Enter Command: ")
while True:
    try:
        if msg == '':
            break

        commandList = msg.split()
        with open("data.json", "r") as json_data:
            data = load(json_data)

        #Sends msg over channel in plaintext
        if commandList[0] == 'PT':
            data['channel'] = msg[3:]
            with open("data.json", "w") as outfile:
                dump(data, outfile)

        #Encrypts with ceaser cypher
        elif commandList[0] == 'CE':
            encrypted = caesar_encrpt(msg[3:-1], int(commandList[-1]))
            data['channel'] = encrypted
            with open("data.json", "w") as outfile:
                dump(data, outfile)

        #Brute force using ceaser whatever is in channel, returns decrypted and key
        elif commandList[0] == 'CB':
            results = caesar_brute(data['channel'])
            print(f"Possibilites: {results}")

        elif commandList[0] == 'CB':
            results = caesar_brute(data['channel'])
            print(f"Possibilites: {results}")

        #Prints whatever is in channel
        elif commandList[0] == 'SC':
            print(f"Msg: {data['channel']}")

        raise Exception
    except:
        msg = input("Enter Command: ")

"""
with open("data.json", "r") as json_data:
    data = load(json_data)

with open("data.json", "w") as outfile:
    dump(data, outfile)
"""
