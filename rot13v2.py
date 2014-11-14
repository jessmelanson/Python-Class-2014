Ciphers = dict()

def addtoCiphers(word):
    for letter in word:
        if ord(letter) > 96 and ord(letter) < 110:
            Ciphers[letter] = chr(ord(letter) + 13)
        elif ord(letter) > 109 and ord(letter) < 123:
            Ciphers[letter] = chr(ord(letter) - 13)
        elif ord(letter) > 64 and ord(letter) < 79:
            Ciphers[letter] = chr(ord(letter) + 13)
        elif ord(letter) > 78 and ord(letter) < 91:
            Ciphers[letter] = chr(ord(letter) - 13)
        else:
            print "Invalid entry. Please do not use spaces or special characters."

def encrypt(word):
    addtoCiphers(word)
    for letter in word:
        return cipherCodes[letter]

decodedCiphers = dict()

def addtodecodedCiphers:
    for key in Ciphers:
        decodedCiphers[Ciphers[key]] = key

def decrypt(codeword):
    addtodecodedCiphers(codeword)
    for letter in codeword:
        return decodedCiphers[letter]
