import datetime

dir(datetime)  # shows all parts of datetime library

datetime.datetime.now()
print(datetime.datetime.now())

treehouse_start = datetime.datetime.now()
print(treehouse_start.replace(hour=10, minute=0, second=0, microsecond=0))
print(treehouse_start)
treehouse_start = treehouse_start.replace(hour=10, minute=0, second=0, microsecond=0)
print(treehouse_start)

treehouse_now = datetime.datetime.now() - treehouse_start
print(treehouse_now)

treehouse_now.days

treehouse_now.seconds

now = datetime.datetime.now()

datetime.timedelta(days=3)

print(now)

print(now + datetime.timedelta(days=3))
print(now + datetime.timedelta(days=-10))
print(now - datetime.timedelta(days=10))
print(now.date())
print(now.time())

datetime.datetime.now()
datetime.datetime.today()  # same as now() except now() can take arguments


now.timestamp()

now = datetime.datetime.now()

now.strftime('%B %d')  # strips unnecessary numbers
print(now.strftime('%B %d'))  # January 13
print(now.strftime('%m/%d/%y'))  # 01/13/20

birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')
print(birthday)

birthday_party = datetime.datetime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')
print(birthday_party)


