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

def ciphenate(word):
    addtocipherCodes(word)
    for letter in word:
        return cipherCodes[letter]

decodedCiphers = dict()

def addtodecodedCiphers:
    for key in cipherCodes:
        decodedCiphers[cipherCodes[key]] = key

def unciphenate(cipherWord):
    addtodecodedCiphers(cipherWord)
    for letter in cipherWord:
        return decodedCiphers[letter]

def encryptDecrypt(word):
    print "Encrypted word: " + ciphenate(word)
    print "Decrypted word: " + unciphenate(ciphenate(word))
