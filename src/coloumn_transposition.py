import string
from english_words import english_words_alpha_set

def columnar_transposition_encrypt(toEncrypt, key):
    #Find the length of the key
    keyLength = len(key)

    #Break to_encrypt into a number of lists equal in length to key
    coloumns = string_to_2d_array(toEncrypt, keyLength)

    #Case where final entry isn't full
    for i in range(len(coloumns[-1]),keyLength):
        #Finds hash of last added letter, mods by length of toEncrypt, then appends that letter
        addedIndex = hash(coloumns[-1][-1])%len(toEncrypt)
        addedChar = toEncrypt[addedIndex]
        coloumns[-1] += addedChar

    #Associate letter of key with index
    keyList = []
    for i in range(keyLength):
        keyList.append([key[i],i])

    #Sort keyList alphabetically (Case is unimportant)
    sortedKeyList = sort_keyList(keyList)

    #Create a string based on the coloumn number
    returnStr = ''
    for item in sortedKeyList:
        for line in coloumns:
            returnStr += line[item[1]]
    return returnStr

def columnar_transposition_decrypt(encrypted, key):
    #Find the length of the key
    keyLength = len(key)

    #Associate letter of key with index
    keyList = []
    for i in range(keyLength):
        keyList.append([key[i],i])

    #Finds number of coloums needed
    numColumns = int(len(encrypted)/keyLength)

    #Sort keyList alphabetically (Case is unimportant)
    sortedKeyList = sort_keyList(keyList)

    #Method from https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    rows = [encrypted[i:i+numColumns] for i in range(0, len(encrypted), numColumns)]

    #Associates each row with an index, based on the key
    rowList = []
    for i in range(len(sortedKeyList)):
        rowList.append([rows[i],sortedKeyList[i][1]])

    sortedRowList = sort_rowList(rowList)

    #Create a string based on the coloumn number
    returnStr = ''
    for i in range(len(sortedRowList[-1][0])):
        for j in range(len(sortedRowList)):
            returnStr += sortedRowList[j][0][i]
    return returnStr


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
    Return a sorted alphabetically (not caring for case) keyList when given a keyList.
    Returns a list
    """
    sortedKeyList = []
    for item in keyList:
        #If the sortedKeyList is empty, append the first item
        if len(sortedKeyList) == 0:
            sortedKeyList.append(item)
            continue

        #Finds the length of sortedKeyList, which is used later to see if anything was added
        old_len_sortedKeyList = len(sortedKeyList)

        #For each entry in the sorted list, compare with item
        for sorted in sortedKeyList:
            #Compares the letter component of the item and sorted in lowercase
            if ord(item[0].lower()) < ord(sorted[0].lower()):
                sortedKeyList.insert(sortedKeyList.index(sorted), item)
                break

        #If these values equals, it means that item is the largest, so append to end
        if len(sortedKeyList) == old_len_sortedKeyList:
            sortedKeyList.append(item)

    return sortedKeyList

def sort_rowList(rowList):
        """
        Return a sorted ascending rowList when given a rowList.
        Returns a list
        """
        sortedRowList = []
        for item in rowList:
            #If the sortedKeyList is empty, append the first item
            if len(sortedRowList) == 0:
                sortedRowList.append(item)
                continue

            #Finds the length of sortedKeyList, which is used later to see if anything was added
            old_len_sortedRowList = len(sortedRowList)

            #For each entry in the sorted list, compare with item
            for sorted in sortedRowList:
                #Compares the letter component of the item and sorted in lowercase
                if int(item[1]) < int(sorted[1]):
                    sortedRowList.insert(sortedRowList.index(sorted), item)
                    break

            #If these values equals, it means that item is the largest, so append to end
            if len(sortedRowList) == old_len_sortedRowList:
                sortedRowList.append(item)

        return sortedRowList
