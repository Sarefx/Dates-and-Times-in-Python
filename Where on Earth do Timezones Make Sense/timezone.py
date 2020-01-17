# my solution to challenges/exercises in Where on Earth do Timezones Make Sense

# the challenge: Create a function named to_timezone that takes a timezone name as a string. Convert starter to that timezone using pytz's timezones and return the new datetime.

import datetime
import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(timezone_name):
    new_timezone = pytz.timezone(timezone_name)
    new_datetime = starter.astimezone(new_timezone)
    return new_datetime

# the challenge: solved
