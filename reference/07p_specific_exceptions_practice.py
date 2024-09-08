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
There are 2 specific exceptions that would be raised here:
    1: entering an invalid integer
    2: dividing by zero

See if you can alter the below code to have 3 except statments:
    1 that chatches the error for an invalid integer
    1 that catches the error for dividing by zero
    1 that would catch any other error not caught by the first 2.

    To find out the names of the exceptions to catch, you can either look at the
    previous python file where it lists some specific Exception names.
    
    Or first write "except Exception as e:" and then print out the type of e to see what kind of exception it is.

'''


def divide_numbers(first_num, second_num):
    return first_num / second_num

try:
    number = input("Enter a number to divide 10 by: ")
    number = int(number)
    print(divide_numbers(10, number))

except ValueError:
    print("Not a valid value for an integer. Try again.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
except Exception as e:
    print(f"This was the error message: {e}.")

print("Thank you for using our program")

