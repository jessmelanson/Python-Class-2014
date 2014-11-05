def secretCode(word):
    for letter in list(word.lower()):
        if ord(letter) > 96 and ord(letter) < 110:
            print chr(ord(letter) + 13)
        elif ord(letter) > 109 and ord(letter) < 123:
            print chr(ord(letter) - 13)
        else:
            print "Invalid entry. Please do not use spaces or special characters."
