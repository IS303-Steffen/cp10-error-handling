from helper_functions import clear_screen
clear_screen()

# ==================
# EXCEPTION HANDLING
# ==================

'''
OVERVIEW
--------
Exception handling means elegantly catching exceptions so that your
program can either:
    - Continue running after the error
    - Nicely inform the user what went wrong or log the error.

You do this with try and except statements!

TRY / EXCEPT
------------

purpose:
    catch exceptions and let you elegantly handle them

structure:
    you start with "try:" and then indent any code beneath
    try MUST also have an "except:"

flow:
    It will run the code like normal UNTIL an exception occurs (like a runtime
    error)
    THEN it skips IMMEDIATELY to the except
    This means any code in the try after the error is found
    won't be run.

    When an error is found (e.g. an "exception" is "caught")
    Then the code under "except:" is run, then the program continues on.

other stuff we'll get to:
    you can have multiple excepts
    you can also use a "finally" after the except

'''


# 1. INFORM THE USER AND ELEGANTLY EXIT
# Follow along. We're going to put the code into a try statement.
# Add an except statement after the try. In the except print out
# "You gave an invalid number. Rerun the program and use an integer (0-9)"
# and then run the sys.exit() function to close your program. Remember to 
# import sys to be able to use sys.exit().
# after the try/except, print "We made it past the try and except"

# Run your code with sys.exit() and with sys.exit() commented out. What does
# your program do after it runs the code in the except: block?

# Bonus: Can you change the code so that in your error message it displays the
# incorrect input?



import sys # this lets me get access to sys.exit()

try:
    
    num_cust = int(input("How many customers would you like to enter? "))

    #For each customer:
    for count in range(1, num_cust + 1) :
        print("This is just an example, customer #", count)
    
except:
    print("You gave an invalid number. Rerun the program and use an integer (0-9)")
    # sys.exit() stops the program immediately
    sys.exit() # try getting rid of this too, to see how try/except works

print("We made it past the try and except")

