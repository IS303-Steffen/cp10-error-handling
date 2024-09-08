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


'''
Exception handling: Elegantly catching exceptions so that your program can either:
    - Continue running after the error
    - Nicely inform the user what went wrong (you might also want to log the error.)

You do this with try and except statements!
'''


# try/except:
'''
    purpose:
        catch errors and let you elegantly handle them

    structure:
        you start with "try:" and then indent any code beneath
        try MUST also have an "except:"

    flow:
        It will run the code as is UNTIL it finds an error
        THEN it skips IMMEDIATELY to the except
        This means any code in the try after the error is found
        won't be run.

        When an error is found (e.g. an "exception" is "caught")
        Then the code under "except:" is run, then the program continues on.

    other stuff we'll get to:
        you can have multiple excepts
        you can also use and "else" or a "finally" after the except

'''


# Practice:
'''
Follow along. We're going to put the code into a try statement.
Add an except statement after the try. In the except print out
"You gave an invalid number. Rerun the program and use an integer (0-9)"
and then run the sys.exit() function to close your program.
after everything, print "We made it through the customer loop!"

Bonus: Can you change the code so that in your error message it displays the incorrect input?
'''


import sys # this lets me get access to sys.exit()

num_cust = int(input("How many customers would you like to enter? "))

#For each customer:
for count in range(1, num_cust + 1) :
    print("This is just an example, customer #", count)
    

print("We finished looping throug the number of customers!")

