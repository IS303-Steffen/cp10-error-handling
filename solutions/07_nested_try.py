from helper_functions import clear_screen
clear_screen()

# =================
# NESTED TRY/EXCEPT
# =================

'''
OVERVIEW
--------
You can nest try/except statements.

If a try/except is nested and you encounter an error, it will just
go to the corresponsing except statement, but continue on in the outer
try statement.

This is good to know about, but we likely won't get into too many situations
like this.
'''

# 1. NESTED TRY / EXCEPT STATEMENTS
# Look through this, and try to predict what except statements will run.
# None of these variables have been defined, so they will all trigger
# exceptions.

# After running the program once, try creating a value for the variable z
# and running it again.

import sys 

print("Welcome to the program!")

try:
    print(z)
    try:
        print(x)
    except:
        print("x is not found")
    
    try:
        print(y)
    except:
        print("y is not found")
    
    try:
        print(x + z)
    except:
        print("x + z did not work")
        
except:
    print("We have encountered a problem with the program.")
    print("Can you please contact customer support at 555-555-1212?")
    print("The program will terminate now.")   
    sys.exit() 
    
print("Let's continue with the program.")