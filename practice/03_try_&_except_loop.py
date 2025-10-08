from helper_functions import clear_screen
clear_screen()

# =======================
# LOOPING WITH EXCEPTIONS
# =======================

'''
OVERVIEW
--------
Often, you don't want to terminate the program, you just want it to try again,
especially in cases where you are gathering inputs.

'''

# 1. USING TRY/EXCEPT WITH A LOOP
# Alter this code using a while loop so that it will keep asking how for a
# number of customers to enter until a valid integer has been provided.


try:
    
    num_cust = input("How many customers would you like to enter? ")
    num_cust = int(num_cust)

    #For each customer:
    for count in range(1, num_cust + 1) :
        print("This is just an example, customer #", count)

    
except:
    print(f'"{num_cust}" is not a valid number. Use a valid integer (0-9)')


# BONUS
# If you have time, do the same thing as above, but make your own function
# that gathers input while accounting for ValueErrors and doesen't exit
# the function until a valid value is provided.