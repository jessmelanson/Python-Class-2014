import os

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

codewordList = []

def encrypt(word):
    addtoCiphers(word)
    for letter in word:
        codewordList.append(Ciphers[letter])
    return ''.join(codewordList)

codeWord = encrypt(raw_input("Enter a word to encrypt:\n"))

os.system('cls')

print "Encrypted word: " + codeWord

decodedCiphers = dict()

def addtodecodedCiphers(word):
    for key in Ciphers:
        decodedCiphers[Ciphers[key]] = key

decodedList = []

def decrypt(word):
    addtodecodedCiphers(codeWord)
    for letter in word:
        decodedList.append(decodedCiphers[letter])
    return ''.join(decodedCiphers)

while True:
    os.system('cls') #cls is clear function for Windows Command line
    response = raw_input("Decrypt? y/n \n")
    if response == 'y':
        print decrypt(codeWord)
        break
    elif response == 'n':
        raw_input("Are you sure? y/n \n")
    else:
        raw_input("Please only respond 'y' or 'n' - ok?\n")
