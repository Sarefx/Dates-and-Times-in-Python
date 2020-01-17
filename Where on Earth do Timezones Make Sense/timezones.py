# my solution to challenges/exercises in Where on Earth do Timezones Make Sense

# the challenge:
# task 1: Create a variable named moscow that holds a datetime.timezone object at +4 hours.
# task 1: solved

# task 2: Now create a timezone variable named pacific that holds a timezone at UTC-08:00.
# task 2: solved

# task 3: Finally, make a third variable named india that hold's a timezone at UTC+05:30.
# task 3: solved

import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))
india = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

# the challenge: solved
