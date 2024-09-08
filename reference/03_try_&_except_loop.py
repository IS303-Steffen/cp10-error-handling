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
Often, you don't want to terminate the program, you just want it to try again, especially
in cases where you are gathering inputs.

Alter this code using a while loop so that it will keep asking how for a number of customers to enter
until a valid integer has been provided.
'''

continue_asking = True
while continue_asking:
    try:
        
        num_cust = input("How many customers would you like to enter? ")
        num_cust = int(num_cust)

        #For each customer:
        for count in range(1, num_cust + 1) :
            print("This is just an example, customer #", count)

        # make it so the loop can terminate
        continue_asking = False
        
    except:
        print(f'"{num_cust}" is not a valid number. Use a valid integer (0-9)')


