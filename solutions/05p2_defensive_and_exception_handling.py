from helper_functions import clear_screen
clear_screen()

# ===========================================
# PRACTICE - DEFENSIVE AND EXCEPTION HANDLING
# ===========================================

# 1. PRACTICE:
# Below is some functional code that doesn't have any error handling:

list_of_friends = ["Thom", "Jonny", "Ed", "Colin", "Phil"]

num_friend_to_see = input("Enter a number of friend to see: ")

num_friend_to_see = int(num_friend_to_see)

print(list_of_friends[num_friend_to_see -1])


# 1.1 ADD DEFENSIVE ERROR HANDLING
# Rewrite the original code to use defensive error handling.
# If an improper input is given, feel free to print out a nice message instead.
list_of_friends = ["Thom", "Jonny", "Ed", "Colin", "Phil"]

num_friend_to_see = input("Enter a number of friend to see: ")
if num_friend_to_see.isdecimal():
    num_friend_to_see = int(num_friend_to_see)
else:
    print("Improper input")

if num_friend_to_see <= len(list_of_friends):   
    print(list_of_friends[num_friend_to_see -1])
else:
    print("Improper input")



# 1.2 ADD EXCEPTION HANDLING
# Rewrite the original code to use exception handling
# If an improper input is given, feel free to print out a nice message instead.
list_of_friends = ["Thom", "Jonny", "Ed", "Colin", "Phil"]
try:
    num_friend_to_see = input("Enter a number of friend to see: ")
    num_friend_to_see = int(num_friend_to_see)
    print(list_of_friends[num_friend_to_see -1])
except:
    print("Improper input")