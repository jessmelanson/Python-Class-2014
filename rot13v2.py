cipherCodes = dict()

def addtocipherCodes(word):
    for letter in word:
        cipherCodes[letter] = ord(letter)
