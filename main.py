

#Let us Begin! Project Requirements
#CHALLENGE 1
#You will store your poem in a .txt file. Feel free to use any poem of your choice!

#CHALLENGE 2
#Create a function called get_file_lines():

#It should have 1 parameter called filename, which is a string of the filename.
#It should return a list of strings containing the lines of the file.
#Create a function called lines_printed_backwards():

#CHALLENGE 3
#It should have 1 parameter called lines_list, which is a list of strings containing lines of your poem.

#It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.

#CHALLENGE 4
#Create a function called lines_printed_random():

#It should have 1 parameter called lines_list, which is a list of strings containing lines of your poem.
#It should print the lines of your poem in randomly order. Repeats are ok, but make sure the number of lines 
#printed is equal to the original lines in the poem (Line numbers do not need to be printed.) Hint: try using a loop 
# and randint() from the random module.
#Create a function called lines_printed_custom():

#It should minimally have 1 parameter called lines_list, which is a list of strings containing lines of your poem.
#It should print the poem in a unique way, be creative!
#Make sure that you carefully comment your custom function so it’s clear what it does.

#CHALLENGE 5
#Your final submitted code should use the four functions (get_file_lines(), lines_printed_backwards(), 
# lines_printed_random(), and lines_printed_custom()) you wrote. It should print out the poem contained in your text file backwards, 
# random, and custom to the terminal.

# STRETCH
#Modify your program to write your poems to a file.
#Modify your program to have a menu that the user can select from rather than printing all the options at once
#Modify your program to read the poem from user input
#Modify your program to randomly rearrange the words on each line




#Challenge 1 GET FILE LINES
#This function opens the text file and prints it forward. It is very 
#important to remember to open and close the file as well as call the function

file1 = input("Please include a poem: ")

filename = open(file1, "r")

def get_file_lines(filename):
    getting_the_file = filename.readlines()
    for line in getting_the_file:
        print(line)
    filename.close()

get_file_lines(filename)


#Challenge 2 LINES PRINTED BACKWARDS
#ADDING A NUMBER TO THE POEM LINE
files2 = input("Please include another poem and I will read it backwards: ")
lines_list = open(files2, "r")

with lines_list as operation:
    poem = operation.readlines()

openfile2 = open(files2, "w")

with openfile2 as operation:
    for(number, line) in enumerate(poem):
        operation.write('%d %s' % (number + 1, line))
    operation.close()
#END OF ADDING A NUMBER TO THE LINE


# PRINTING TEXT BACKWARDS
lines_list = open(files2, "r")

def Lines_printed_backwards(lines_list):
   linear = lines_list.readlines()
   for line in reversed(linear):
       print(line)
   lines_list.close()

Lines_printed_backwards(lines_list)

# END OF PRINTING TEXT BACKWARDS 

#Challenge 3 LINES PRINTED RANDOMLY
import random 

files3 = input("Please include another poem and I will randomize it: ")

lines_list = open(files3, "r")

def Lines_printed_random(lines_list):
    middleman = lines_list.readlines()
    length = (len(middleman)-1)
    for line in middleman:
        randomness = random.randint(0, length)
        print(middleman[randomness])
    lines_list.close()

Lines_printed_random(lines_list)


#Challenge 4 PRINTING POEMS CUSTOM, specifically BACKWARDS  

#This function printed the poem in reverse. I will save this for my special function

file4 = input("Please include one last poem and I will print it backwards: ")

lines_list = open(file4, "r")

def lines_printed_backwards(lines_list):
#This is defining our function lines_printed_backwards with the element lines_list 
#which has our input variable file4 and our read format for the text file
    getting_the_reverse_file = lines_list.readlines()
#The line above breaks each line in lines_list into a list item
    for line in getting_the_reverse_file:
#For every item in the list (lines_list)
       print(line[::-1])
#This is where the magic happens. [::-1] is index slicing, with a start:stop:step-count.
#Above, since there are no defined values for start, Python defaults it to 0 on the list
#the list being in this case the elements (characters/letters) of each line of the poem
# And since there are no defined values for the stop, it defaults to the last value on the
#list and adds +1, which would be the final letter of each line of the poem. The -1 out puts 
#every value, but does so in reverse instead. So the whole function produces a copy of all the
#elements in the list, which is the poem itself, and outputs it in a reversed order
    lines_list.close()

lines_printed_backwards(lines_list)


#END OF PRINTING POEMS IN REVERSE 

