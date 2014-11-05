f = open('words.txt')

for line in f.readlines():
    if((line.replace(" ", "").strip('\n')[::] == line.replace(" ","").strip('\n')[::-1]) == True):
        print line
