from helper_functions import clear_screen
clear_screen()

# ===================
# ERRORS & EXCEPTIONS
# ===================

'''
OVERVIEW
--------
Normally if the program encounters a runtime error, it will just shut down.
When your code runs into an error that makes it unable to run,
it "raises" an exception (or "throws" an exception, either phrasing works).

An "exception" is an event that immediately disrupts the flow of a program,
and usually occurs when there is an error in your code. If you don't handle
an exception, your program will immediately stop running.

Exceptions have names, that you can see when running the code and looking at
the terminal when an exception is thrown.
'''

# 1. PURPOSEFULLY CAUSING AN EXCEPTION:
# Try entering something like "Three" instead of "3" to the below code.
# What is the name of the exception that is thrown?

num_cust = int(input("How many customers would you like to enter? "))

#For each customer:
for count in range(1, num_cust + 1) :
    print("This is just an example, customer #", count)
