import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ============================
# CATCHING SPECIFIC EXCEPTIONS
# ============================

# 1. PRACTICE CATCHING SPECIFIC EXCEPTIONS:
# You are given some code below. There are 2 specific exceptions that might
# be raised here:
#     1: entering an invalid integer (like if the user enters "asdf")
#     2: dividing by zero (if the user enters "0")

# See if you can alter the below code to have 3 except statments:
#     1 that catches the error for an invalid integer
#     1 that catches the error for dividing by zero
#     1 that would catch any other error not caught by the first 2.

# To find out the names of the exceptions to catch, you can either look at the
# bottom of the previous python file where it lists some specific Exception
# names. Or, first write "except Exception as e:" and then print out
# type(e).__name__ to see what kind of exception it is.


def divide_numbers(first_num, second_num):
    return first_num / second_num

try:
    number = input("Enter a number to divide 10 by: ")
    number = int(number)
    print(divide_numbers(10, number))

except:
    print("Something went wrong")


print("Thank you for using our program")

