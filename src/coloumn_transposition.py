import string
from english_words import english_words_alpha_set

def columnar_transposition_encrypt(toEncrypt, key):
    #Find the length of the key
    keyLength = len(key)
    #Break to_encrypt into a number of lists equal in length to key
    coloumns = string_to_2d_array(toEncrypt, keyLength)
    #Associate letter of key with index, sort alphabetically
    keyList = []
    for i in range(keyLength):
        keyList.append([key[i],i])
    sortedKeyList = sort_keyList(keyList)
    print(keyList.sorted())
    #Sort letters alphabetically, the return each coloumn together as one string
    return toEncrypt

def columnar_transposition_decrypt(encrypted, key):
    return encrypted

def string_to_2d_array(toEncrypt, k_len):
    """
    Turns a string into a 2d array.
    Each list in the array has length len
    Returns the 2d array
    """
    #Method from https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    toReturn = [toEncrypt[i:i+k_len] for i in range(0, len(toEncrypt), k_len)]
    return toReturn

def sort_keyList(keyList):
    """
    Return a sorted keyList with given a keyList.
    Returns a list
    """
    return keyList

print(columnar_transposition_encrypt('HelloIamCameronhowareyou?', 'Apples'))
