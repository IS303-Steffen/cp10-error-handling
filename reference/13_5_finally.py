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

'''
    Beyond try/except there are 2 other statements. We won't cover them besides here,
    but it is good to know they exist (especially finally)


    try:
        run this code first
    except:
        if exception caught, run this
    else:
        if no exception, run this code
    finally:
        ALWAYS run this code. No matter if there is or is not an exception.
'''


try:
    number = int(input("Enter an integer: "))
    result = 10 / number
except:
    print("That wasn't an integer! Or maybe you divided by zero.")
else:
    print(f"10 divided by {number} is {result}")
finally:
    print("This will always execute, no matter what!")


# Why?
'''
    else:
        optional. Your textbook doesn't cover it. Just if you want to logically separate out
        "this is the code that might have errors" and
        "this is what I want to do if the above code actually worked"

    finally:
        useful in some situations where you might have opened up a connection to a database or file
        and want to be absolutely sure that no matter what error might pop up, you can close the connection,
        or save some kind of data that you were working with.
'''
