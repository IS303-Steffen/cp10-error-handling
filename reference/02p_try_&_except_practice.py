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

# =====================
# TRY / EXCEPT PRACTICE
# =====================




# 1. PRACTICE:
# write a function that takes two parameters, each an integer,
# divides the first by the second number, and returns the result.
# print out the result that is returned.

# Call the function, but enter a 0 as the second argument.
# Catch the exception and print out "You cannot divide by zero."

# Make it so "thank you for using the program" prints out regardless of
# whether the error was triggered or not.



def divide_numbers(first_num, second_num):
    return first_num / second_num

try:
    print(divide_numbers(10, 0))

except:
    print("You cannot divide by zero.")

print("Thank you for using our program")

