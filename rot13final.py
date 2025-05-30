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
        elif letter in [" ", ".",",","!","?",":"]:
        	Ciphers[letter] = letter
        else:
            print "Invalid entry. Please write out numbers and avoid using special characters."

def encryptDecrypt(word):
    addtoCiphers(word)
    codewordList = []
    for letter in word:
        codewordList.append(Ciphers[letter])
    return ''.join(codewordList)

codeWord = encryptDecrypt(raw_input("Enter a word or phrase to encrypt:\n"))

print "Encrypted word: " + codeWord

while True:
    response = raw_input("Decrypt? y/n \n")
    if response == 'y':
        print "Decrypted word: " + encrypt(codeWord)
        break
    elif response == 'n':
        raw_input("Are you sure? y/n \n")
    else:
        raw_input("Please only respond 'y' or 'n' - ok?\n")
