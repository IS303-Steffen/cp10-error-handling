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
# PRACTICE - DEFENSIVE PROGRAMMING
# ================================

# 1. REWRITE TO USE DEFENSIVE PROGRAMMING
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

