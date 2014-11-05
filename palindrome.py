#open the document
f = open('words.txt')
#make a list with each list element being one line of the file
for line in f.readlines():
    #first remove all spaces from the line
    #then remove the new line code \n from each line
    #then check if the word forwards is equivalent to the word backwords
    if(line.replace(" ", "").strip('\n')[::] == line.replace(" ","").strip('\n')[::-1]):
        #if the line is the same forwards and backwards, print the line in the output
        print line
#close the document
f.close()
