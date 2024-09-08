# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################


# Practice:
'''
You are given a dictionary with dog names and their ages.

Ask the user to enter a dog name, and if it is valid, display their age.
Remember you can access a dictionary like: dog_age = dog_ages["Bella"]

If the user enters an invalid dog name, catch the error and keep asking for a name
until a valid one is given.

Bonus thought: Do this with exception handling, but could you do this without exception handling?
                We'll talk about this on the next file over.
'''

dog_ages = {"Buddy": 3, "Bella": 5, "Charlie": 2, "Lucy": 4, "Max": 1}




