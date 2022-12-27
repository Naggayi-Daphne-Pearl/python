import datetime

daphne = datetime.datetime(1997, 9, 9)
print(daphne)

y = datetime.date(1997,9,12)
print(y)

print(daphne.year)
print(daphne.month)
print(daphne.day)


# to launch date for today
now = datetime.datetime.today()
print(now)
print(now.year)
print(now.microsecond)

# convert string to datetime
# strptime(): strptime() is a function in the datetime module in Python that allows you to parse a string representation of a date and time and convert it to a datetime object
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%Y-%m-%d")
print(moon_landing_datetime, type(moon_landing_datetime))