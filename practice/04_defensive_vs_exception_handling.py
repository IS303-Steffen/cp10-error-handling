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


# Discussion:
'''
Which of these two versions do you prefer?
What are the advantages and disadvantages of each?
'''

# Exception handling
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


# Defensive Programming (anticipate any specific errors, handle them.)
# Could have also done something with .get()

dog_ages = {"Buddy": 3, "Bella": 5, "Charlie": 2, "Lucy": 4, "Max": 1}

continue_asking = True
while continue_asking:
    dog_name = input("Enter a dog name to see its age: ")

    if dog_name in dog_ages:
        dog_age = dog_ages[dog_name]
        print(f"{dog_name}'s age: {dog_age}")

        # make it so the loop can terminate
        continue_asking = False
    else:
        print(f'"{dog_name}" is not a valid dog name. Try again.')


'''
Not necessarily a "right" or "wrong" way.
Exception handling is reactive, Defensive programming is proactive.

EXCEPTION HANDLING:
    Pros:

        Avoids Crashes:
            Helps your program to deal with mistakes without stopping abruptly.

        Separates Error Handling from Main Logic:
            Keeps your main program neat and lets you deal with problems in a separate area of code.

        Gives More Control:
            You can decide exactly what to do if an error happens,
            like giving a user-friendly message or trying a different approach.
    Cons:

        Can Be Overused:
            If you try to catch every possible error everywhere,
            your code might become harder to read and manage.
        
        Might Hide Problems:
            If you catch errors but don't handle them properly,
            it can make it harder to find and fix the underlying issues.

        Performance:
            In some cases, if your program throws and catches a lot of exceptions,
            it might run a bit slower. Depends on how you code it.

DEFENSIVE PROGRAMMING:
    Pros:

        Prevents Errors:
            By checking inputs, outputs, and using safe defaults, it stops errors before they even happen.

        Makes Code More Reliable:
            By anticipating and planning for what could go wrong, your program becomes more robust and less likely to fail unexpectedly.

        Helps With Debugging:
            If something does go wrong, having checks in place can make it easier to figure out where and why.
    
    Cons:

        Can Make Code More Complex:
            Adding lots of checks and safeguards can make your code longer and harder to read, especially for simple tasks.
        
        May Affect Performance:
            Doing extra checks all the time, even when they're not needed, can slow down your program a little.
        
        False Sense of Security:
            You might think everything's covered by your checks, but there's always a chance something unexpected will slip through.

'''
