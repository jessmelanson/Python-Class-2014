cipherCodes = dict()

def addtocipherCodes(word):
    for letter in word:
        cipherCodes[letter] = ord(letter)
        if ord(letter) > 96 and ord(letter) < 110:
            cipherCodes[chr(ord(letter) + 13)] = ord(letter) + 13
        else ord(letter) > 109 and ord(letter) < 123:
            cipherCodes[chr(ord(letter) - 13)] = ord(letter) - 13
        else:
            print "Invalid entry. Please do not use spaces or special characters."
