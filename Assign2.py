import math


def readName():
    """
    readName - A function to read the input from the user and return a list of strings (the names).
    :return: a list of strings
    """
    print("Enter names, one on each line. Type DONE to quit entering names.")
    namesList = []
    name = input()
    while name != "DONE":
        namesList.append(name)
        name = input()
    return namesList


def digitizeWord(word):
    """
    digitizeWord - A function to replace letters with digits.
    :param word: a string of letters
    :return: a string of digits
    """
    D = ""
    for index in range(len(word)):
        if word[index] in ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']:
            D = D + '0'
        elif word[index] in ['b', 'f', 'p', 'v']:
            D = D + '1'
        elif word[index] in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']:
            D = D + '2'
        elif word[index] in ['d', 't']:
            D = D + '3'
        elif word[index] == 'l':
            D = D + '4'
        elif word[index] in ['m', 'n']:
            D = D + '5'
        elif word[index] == 'r':
            D = D + '6'
    return D


def removeRepetition(number):
    """
    removeRepetition - A function to replace multiple digits with a single copy of the digit.
    :param number: string of digits with possible repeats
    :return: a string of digits with no repeats
    """
    repetitionFreeNumber = number[0]
    for i in range(1, len(number)):
        if number[i] == repetitionFreeNumber[len(repetitionFreeNumber) - 1]:
            continue
        else:
            repetitionFreeNumber += number[i]
    return repetitionFreeNumber


def removeZero(num):
    """
    removeZero - A function to remove zero from a string of digits
    :param num: a string of digits
    :return: a string of digits with no zeros
    """
    zeroFreeNumber = ''
    for i in range(0, len(num)):
        if num[i] == '0':
            continue
        else:
            zeroFreeNumber += num[i]
    return zeroFreeNumber


def soundexEncoding(nameToBeEncoded):
    """
    soundexEncoding - A function to encode a name based on phonetic algorithm
    :param nameToBeEncoded: a string of letters
    :return: a string with length four which its first character is a letter and the rest are number
    """
    firstLetter = nameToBeEncoded[0]
    digitizedName = digitizeWord(nameToBeEncoded)
    noRepetition = removeRepetition(digitizedName)
    noZero = removeZero(noRepetition)
    if len(noZero) > 0:
        if noZero[0] == digitizedName[0]:
            if len(noZero) >= 4:
                encodedName = firstLetter + noZero[1:4]
            else:
                encodedName = firstLetter + noZero[1:] + (4 - len(noZero)) * '0'
        else:
            if len(noZero) >= 4:
                encodedName = firstLetter + noZero[0:3]
            else:
                encodedName = firstLetter + noZero[0:] + (3 - len(noZero)) * '0'
    else:
        encodedName = firstLetter + '000'
    return encodedName


def main():
    # read names from input and save as a list and sort the list
    listOfNames = readName()
    listOfNames.sort()

    # get the soundex code of each name and add the name and code as a tuple to a list
    soundexList = []
    for item in listOfNames:
        soundexList.append((item, soundexEncoding(item.lower())))

    # compare each distinct pair of names in the list and determines which have the same Soundex encoding
    for i in range(len(soundexList) - 1):
        for j in range(i + 1, len(soundexList)):
            if soundexList[i][1] == soundexList[j][1]:
                print("{} and {} have the same Soundex encoding.".format(soundexList[i][0], soundexList[j][0]))


main()

