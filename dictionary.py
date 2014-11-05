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

    #if the user types 6, Q, q, or Quit
    if response in ['6','Q','q','Quit','quit']:
        #the while loop ends
        break
        
    #if the user types 1, A, a, Add, add
    if response in ['1','A','a','Add','add']:
        #
        insert()
