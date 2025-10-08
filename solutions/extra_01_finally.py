from helper_functions import clear_screen
clear_screen()

# =======
# FINALLY
# =======

'''
OVERVIEW
--------
"Finally" is what you may say when this class ends. It also refers to a 
statement that is put after the except. finally will always run, no matter
whether an exception occurred or not.

We will likely not need to use this during the semester. It comes more in handy
when doing some more complex stuff with connections to external databases, etc
and you need to make absolutely sure that you securely close connections even
if an error occurs, etc.

STRUCTURE
---------
try:
    run this code first
except:
    if exception caught, run this
finally:
    ALWAYS run this code. No matter if there is or is not an exception.

'''

# 1. FINALLY
# Run the code below and provide any valid integer. Notice how the finally
# statement runs. Run the code again and provide an improper input.
# Notice that the finally statement runs as well.

import sys

try:
    number = int(input("Enter an integer: "))
    result = 10 / number
except:
    print("That wasn't an integer! Or maybe you divided by zero.")
    sys.exit()
finally:
    print("This will always execute, no matter what!")


