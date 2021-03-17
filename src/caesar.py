import string
from english_words import english_words_set
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
        raise TypeError("1st argument must be string")
    if isinstance(key, int) == False:
        raise TypeError("2nd argument must be int")

    """
    ---------------------------------
    """

    #For each letter in the message shift by key
    encrypted = shift(msg, key)

    return encrypted

"""
Decrypts the caesar encryption from above
Given a string and int
Returns string
"""
def caesar_decrypt(msg, key):
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

    #For each letter in the message shift by key
    decrypted = shift(msg, -key)

    return decrypted

"""
Given the key, ensures it is between and including 0-25
Given an int
Returns an int
"""
def shift_key(key):
    #If the key is over 25 ('z'), minus 26
    #If the key is under 0 ('a'), plus 26
    while True:
        if key > 25:
            key -= 26
        elif key < 0:
            key += 26
        else:
            break
    return key

"""
Given a msg will shift right by key (i.e to decrypt use negative key)
Given a string and int
Returns int
"""
def shift(msg, key):
    decrypted = ''
    for letter in msg:
        #Determins which alphabet to use
        if letter.isupper() == True:
            alphabet = string.ascii_uppercase
        elif letter.islower() == True:
            alphabet = string.ascii_lowercase
        else:
            decrypted += letter
            continue
        letter_index = alphabet.index(letter)
        letter_index = letter_index+key

        letter_index = shift_key(letter_index)

        decrypted += alphabet[letter_index]
    return decrypted

"""
Given a cypher, returns a list of all possiable decypher's.
This is determined by if atleast one word in the decypher
is in the list english_words_set.
Given a string
Returns a list
"""
def caesar_brute(cypher):
    return cypher
