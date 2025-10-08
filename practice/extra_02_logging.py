from helper_functions import clear_screen
clear_screen()

# =======
# LOGGING
# =======

'''
OVERVIEW
--------
Sometime you might want to keep track of which errors occur, so you can go back
and fix them. Logging is one way to do that. You can use logging for other
things too, like keeping track when certain actions occur, when people log in, 
etc.
'''


import logging

# configure the logger, where it should output logged information.
logging.basicConfig(filename='example_error_log.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    100 / 0 # purposefully triggering a ZeroDivisionError
except ZeroDivisionError as e:
    print("You tried to divide by zero!") # display nice message to user

    # log a more detailed error message in the log files.
    logging.error(f"Exception object message: {type(e).__name__}: {e}")