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

        #Encrypts with ceaser cypher, needs key
        elif commandList[0] == 'CE':
            key = int(commandList[-1])
            commandList.remove(commandList[-1])
            commandList.remove(commandList[0])
            msg = ' '.join(commandList)
            encrypted = caesar_encrpt(msg, key)
            data['channel'] = encrypted
            with open("data.json", "w") as outfile:
                dump(data, outfile)

        #Decrypts with ceaser cypher, needs key
        elif commandList[0] == 'CD':
            decrypted = caesar_decrypt(data['channel'], int(commandList[1]))
            print(f"Msg: {decrypted}")

        #Brute force using ceaser whatever is in channel, returns decrypted and key
        elif commandList[0] == 'CB':
            results = caesar_brute(data['channel'])
            print(f"Possibilites: {results}")

        #Encrypt with columnar transposition, sent message must be block, follow by key
        elif commandList[0] == 'TE':
            encrypted = columnar_transposition_encrypt(commandList[1], commandList[2])
            data['channel'] = encrypted
            with open("data.json", "w") as outfile:
                dump(data, outfile)

        #Decrypt with columnar transposition, needs key
        elif commandList[0] == 'TD':
            decrypted = columnar_transposition_decrypt(data['channel'], commandList[1])
            print(f"Msg: {decrypted}")

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
