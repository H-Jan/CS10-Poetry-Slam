

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

#Challenge 1

#This function opens the text file and prints it forward. It is very 
#important to remember to open and close the file as well as call the function
filename = open("PNPoem.txt")

def get_file_lines(filename):
    getting_the_file = filename.readlines()
    for line in getting_the_file:
        print(line)
    filename.close()

get_file_lines(filename)

#This function reverses the poem under lines_list. It is identical to get_file_lines function
#With the addition of the slicing trick [::-1] since strings are also sequences. 
#??? Question: Can I keep file open across multiple functions ????
lines_list = open("CTPoem.txt")

def lines_printed_backwards(lines_list):
    getting_the_reverse_file = lines_list.readlines()
    for line in getting_the_reverse_file:
        print(line[::-1])
    lines_list.close()

lines_printed_backwards(lines_list)








