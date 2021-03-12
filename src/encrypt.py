import string

"""
Given a message it will shift each letter in the message by a given amount.
The amount shifted is determined by the key
Given a string and int
Returns string
"""
def caesar_encrpt(msg, key):
    """
    Ensures the given data is the correct type
    """
    if isinstance(msg, str) == False:
        raise Exception("1st argument must be string")
    if isinstance(key, int) == False:
        raise Exception("2nd argument must be int")

    """
    ---------------------------------
    """

    encrypted = ''

    #For each letter in the message shift by key
    for letter in msg:
        #Determins which alphabet to use
        if letter.isupper() == True:
            alphabet = string.ascii_uppercase
        else:
            alphabet = string.ascii_lowercase

        letter_index = alphabet.index(letter)
        letter_index = letter_index+key

        #If the key is over 25 ('z'), minus 26
        while True:
            if letter_index < 26:
                break
            letter_index -= 26

        encrypted += alphabet[letter_index]

    return encrypted

"""
Decrypts the caesar encryption from above
Given a string and int
Returns string
"""
def caesar_decrypt(msg, key):
    return msg

if __name__ == '__main__':
    print(caesar_encrpt("Larry",27))
