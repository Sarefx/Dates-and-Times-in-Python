# my solution to this challenge/exercise in Let's Build a Timed Quiz App

# the challenge: Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. Return the oldest one as a datetime object...
# ... Remember, POSIX timestamps are floats and lists have a .sort() method.

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

import time, datetime

def timestamp_oldest(*args):
    time_list = list(args)
    time_list.sort()
    converted_datetime = datetime.datetime.fromtimestamp(time_list[0])
    return converted_datetime

# the challenge: solved
