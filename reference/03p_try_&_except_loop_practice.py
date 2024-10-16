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

# ================================
# LOOPING WITH EXCEPTIONS PRACTICE
# ================================


# 1. PRACTICE EXCEPTION WITH LOOPS
# You are given a dictionary with dog names and their ages.

# Ask the user to enter a dog name, and if it is valid, display the dog's name
# and age: "<dog name.'s age: <dog age>"

# Remember you can access a dictionary like: dog_age = dog_ages["Bella"].

# If the user enters an invalid dog name, catch the error,
# print out "<dog name> is not a valid dog name. Try again"
# and keep asking for a name until a valid one is given.

# BONUS:
# Please do the above using exception handling, but could you accomplish the
# same thing without exception handling?
# We'll talk about this on the next file over.


dog_ages = {"Buddy": 3, "Bella": 5, "Charlie": 2, "Lucy": 4, "Max": 1}

continue_asking = True
while continue_asking:
    try:
        dog_name = input("Enter a dog name to see its age: ")

        dog_age = dog_ages[dog_name]
        print(f"{dog_name}'s age: {dog_age}")

        # make it so the loop can terminate
        continue_asking = False
        
    except:
        print(f'"{dog_name}" is not a valid dog name. Try again.')


