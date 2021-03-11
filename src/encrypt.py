import string

"""
Given a message it will shift each letter in the message by a given amount.
The amount shifted is determined by the key
Given a string and int
Returns string
"""
def caesar_encrpt(msg, key):
    if isinstance(msg, str) == False:
        raise Exception("1st argument must be string")
    if isinstance(key, int) == False:
        raise Exception("2nd argument must be int")
    for letter in msg:
        letter_index = string.ascii_lowercase.index(letter)



    return encrypted

"""
Decrypts the caesar encryption from above
Given a string and int
Returns string
"""
def caesar_decrypt(msg, key):
    return msg

if __name__ == '__main__':
    caesar_encrpt("Larry",'Hat')
