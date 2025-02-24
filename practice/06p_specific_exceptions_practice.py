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

# See if you can alter the below code to have 2 except statments:
#     1 that catches the error for an invalid integer
#     1 that catches the error for dividing by zero

'''
How to find out the name of a specific type of exception?
---------------------------------------------------------
1. When you run into the error, just look at the error name in the terminal
2. Handle the error in a general "except Exception as e:" block of code, and
   then look at "e" in the debugger, or print out "type(e)"
3. Ask AI or Google the python exception name for when X error happens
'''


def divide_numbers(first_num, second_num):
    return first_num / second_num

number = input("Enter a number to divide 10 by: ")
number = int(number)
print(divide_numbers(10, number))


print("Something went wrong")


print("Thank you for using our program")

