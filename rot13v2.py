cipherCodes = dict()

def addtocipherCodes(word):
    for letter in word:
        if ord(letter) > 96 and ord(letter) < 110:
            cipherCodes[letter] = chr(ord(letter) + 13)
        elif ord(letter) > 109 and ord(letter) < 123:
            cipherCodes[letter] = chr(ord(letter) - 13)
        elif ord(letter) > 64 and ord(letter) < 79:
            cipherCodes[letter] = chr(ord(letter) + 13)
        elif ord(letter) > 78 and ord(letter) < 91:
            cipherCodes[letter] = chr(ord(letter) - 13)
        else:
            print "Invalid entry. Please do not use spaces or special characters."
