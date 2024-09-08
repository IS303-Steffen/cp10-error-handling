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
    write a function that takes two parameters, each an integer,
    divides the first by the second number, and returns the result.
    print out the result that is returned.


    Call the function, but enter a 0 as the second argument.
    Catch the exception and print out "You cannot divide by zero."

    Make it so "thank you for using the program" prints out regardless of whether the error was triggered or not.

'''



