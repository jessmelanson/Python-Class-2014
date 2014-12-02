#gives program access to your computer's files
import os

#declares the function insert()
def insert():
    #word is the user's answer to the question "enter a word"
    word = raw_input("Enter a word:\n")
    #definition is the user's answer to the question "enter a definition"
    definition = raw_input("Enter a definition:\n")
    #prints out the word
    print "word:",word
    #prints out the definition
    print "definition:", definition
    #response is a local variable only in insert()
    #response is the user's answer to "OK?"
    response = raw_input("Ok?\n")
    #if the user answers yes, Yes, Y, or y
    if response in ['Y','y','Yes','yes']:
        #save the word and definition to the database
        store(word,definition)

#declares the function store() with the word and the definition
def store(word,definition):
    #opens the database
    f = open('default.db', 'a') #a for append, tells computer you're editing the file
    #adds a new line with the word and the definition
    #join is adding a comma in between the word and the definition
    #\n adds a new line
    #f.write lets you add to the file
    #use + here to make def & \n a single string
    #which lets you avoid having a comma at the end of definition
    #if you were to put \n as its own string
    f.write(','.join([word,definition+'\n'])) 
    #close the file
    f.close()

#declares the function find()
def find():
    #query is the user's answer to the question "enter a word"
    query = raw_input("Enter a word to look up:\n")
    #declares f as a variable that opens a database in read mode
    f = open('default.db', 'r') # r means read the file rather than edit it
    #create a list of all the lines in the file
    lines = f.readlines()
    #for each item in the lines list
    for line in lines:
        #if the query substring is within a specific line in the lines list
        if query in line:
            #takes each line and splits it into a list at the commas
            #defines "word" as the first item in the list
            word = line.split(',')[0]
            #defines "word" as the second item in the list
            definition = line.split(',')[1]
            #prints a new line, then the word
            print "\nWord: ",word 
            #prints a new line, then the definition
            print "\nDefinition: ",definition
        #otherwise:
        else:
            #tell the reader it's not in the dictionary
            print "Not in dictionary"
            #end the for loop
            break
	#interrupts the while loop so user can read the output
    response = raw_input("Press enter to go back to the menu.")
    #closes the file
    f.close()
    
#declares the function delete()
def delete():
    #query is the user's answer to the question "enter a word"
    wordToDelete = raw_input("Enter a word to delete:\n")
    #declares f as a variable that opens a database in read mode
    f = open('default.db', 'r') #r means just to read the file
    #creates a list that contains all the lines in the database file
    lines = f.readlines()
    #for each index number and list item in lines
    for indexnum,value in enumerate(lines):
    	#if the word the user wants to delete is in the list value
    	if wordToDelete in value:
    	    #delete the specific line, specified by its index number
    	    del lines[indexnum]
    #close the file
    f.close()
    #open the file again, this time to edit it
    f.open('default.db','w') #w here means to write to the file, as opposed to read only or adding on
    #Overwrite everything in the file with the new contents of the lines list
    f.writelines(lines)
    #good practice to use this to get rid of extra junk code
    f.flush()
    #close the file
    f.close()
    #prevents the app from jumping immediately back to the main menu
    raw_input("Word removed.")

#declares the function showAll()
def showAll():
    #opens the database file for reading
    f = open('default.db','r')
    #read all the lines in the file
    f.readlines()
    #close the file
    f.close()
    #stops the app from jumping back to the main menu
    raw_input("End of dictionary. Press any key to go back to the main menu.")
    
#defines a list of menu navigation
menuItems = ['Add','Find','Show All','Update','Delete','Quit']

#while always needs to evaluate to true or false; true is a filler condition
while True:
    #types a terminal/command line command that clears the screen
    os.system('clear')

	#prints each menu item on a new line with the index of the item plus one
	#(to start the numbering at 1 instead of 0)
    for num, item in enumerate(menuItems):
        print num+1, item

    #have to ask for input if you don't want to run the loop forever, you need a menu item
    #defines variable "response" as the user's answer to the string in parentheses
    #raw_input() is like prompt() in javascript
    response = raw_input("Please Choose a Menu Item\n")
        
    #if the user types 1, A, a, Add, add
    if response in ['1','A','a','Add','add']:
        #add a word
        insert()
        
    #if the user types '2','F','f','Find','find'
    if response in ['2','F','f','Find','find']:
        #look up a word in the existing database
        find()
    
    #if the user types 3, Show All, Show, show all, or s
    if response in ['3','Show All','Show','show all','s']:
    	#display all words
    	showAll()
    
    #if the user types 4, Update, update, or u
    if response in ['4','Update','update','u']:
    	#edit the definition of an entry
    	store()

    #if the user types '5','D','d','Delete','delete', 'del'
    if response in ['5','D','d','Delete','delete', 'del']:
        #delete a word in the existing database
        delete()

    #if the user types 6, Q, q, or Quit
    if response in ['6','Q','q','Quit','quit']:
        #the while loop ends
        break
