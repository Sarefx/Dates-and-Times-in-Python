# my solution to the Simple Time Machine challenge/exercise in Let's Build a Timed Quiz App

# the challenge: Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(integer):
    future_time = starter + datetime.timedelta(hours=integer)
    return future_time

# the challenge is solved

# the challenge: Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years"...
# ... This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(integer, string):
    if string == "minutes":
        new_starter = starter + datetime.timedelta(minutes=integer)
        pass
    elif string == "hours":
        new_starter = starter + datetime.timedelta(hours=integer)
        pass
    elif string == "days":
        new_starter = starter + datetime.timedelta(days=integer)
        pass
    elif string == "years":
        new_starter = starter + datetime.timedelta(days=integer * 365)
        pass
    return new_starter

# the challenge is solved
