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
Errors / Exceptions:
    Normally if the program encounters an error, it will just shut down.
    lots of times, runtime errors are caused by improper inputs. When your code
    runs into an error that makes it unable to run, it "throws an exception".
    An exception is just a name for an error that makes the code not run.
    
    Exceptions have names, that you can see when running the code and looking at the terminal
    when an exception is thrown.
'''

# Practice:
# Try entering something like "Three" instead of "3" to the below code.
# What is the name of the exception that is thrown?

num_cust = int(input("How many customers would you like to enter? "))

#For each customer:
for count in range(1, num_cust + 1) :
    print("This is just an example, customer #", count)