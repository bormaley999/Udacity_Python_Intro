# Udacity Intro to Python
# Section 38 Quiz: readable_timedelta

"""
Write a function named readable_timedelta.
The function should take one argument, an integer days, and
return a string that says how many weeks and days that is.
"""

# write your function here
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(20))


