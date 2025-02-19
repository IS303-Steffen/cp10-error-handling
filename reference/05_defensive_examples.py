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

# ==============================
# DEFENSIVE PROGRAMMING EXAMPLES
# ==============================

'''
OVERVIEW
--------
Defensive programming is a style in which you try to prevent errors from 
occuring (usually through if statements) rather than just handling exceptions
after the errors occur.

In this class, if I say "You need to handle X situation" I don't care if you 
handle it with try/except or with defensive programming. All that matters is
that you handle it.
'''


# 1. .isdigit() EXAMPLE
# Print out the result of .isdigit() on both of the provided strings below:
# Note, you can also use .isdecimal() if you also want to check floats.

example_string_1 = "not a digit"
example_string_2 = "123"

print(example_string_1.isdigit())
print(example_string_2.isdigit())


# 2. REWRITE TO USE DEFENSIVE PROGRAMMING
# Below you're provided with some example code using exception handling
# Try to replicate the same thing, but use defensive programming instead.

maybe_a_number = "123" # change this to something non-numeric, see the result
try:
    maybe_a_number = int(maybe_a_number)
    print(f"This is your number + 10: {maybe_a_number + 10}")

except:
    print(f"The variable maybe_a_number was not actually a number.")

# defensive example
maybe_a_number = "123" # change this to something non-numeric, see the result
if maybe_a_number.isdigit():
    maybe_a_number = int(maybe_a_number)
    print(f"This is your number + 10: {maybe_a_number + 10}")

else:
    print(f"The variable maybe_a_number was not actually a number.")


# 3. REWRITE TO USE DEFENSIVE PROGRAMMING
# Below you're provided with some example code using exception handling
# Try to replicate the same thing, but use defensive programming instead.

possible_key = 111
student_id_dictionary = {123: "Jimmy Jones", 321: "Alice Alms", 332: "Robert Reed"}
try:
    student_name = student_id_dictionary[possible_key]
    print(f"Student ID {possible_key} belongs to {student_name}")
except:
    print(f"Student ID {possible_key} doesn't exist.")


# defensive example
possible_key = 111
student_id_dictionary = {123: "Jimmy Jones", 321: "Alice Alms", 332: "Robert Reed"}

student_name = student_id_dictionary.get(possible_key)
if student_name: 
    print(f"Student ID {possible_key} belongs to {student_name}")
else:
    print(f"Student ID {possible_key} doesn't exist.")



'''
USEFUL CODE FOR DEFENSIVE PROGRAMMING:
--------------------------------------

.isdigit() .isnumeric()
    - useful for checking if a string is a number

isinstance(variable, data type)
    - useful for checking if a variable is a specific data type

.get() (when using dictionaries)
    - useful when you don't know if a key is in the dictionary or not

len() (when accessing lists)
    - useful when you aren't sure if an index is valid



'''