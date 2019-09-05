# Udacity Intro to Python
# Section 40 Quiz: Write a Docstring

"""
Write a docstring for the readable_timedelta function you defined earlier!
"""

def readable_timedelta(days):
    def readable_timedelta(days):
        """Return a string of the number of weeks and days included in days."""
        weeks = days // 7
        remainder = days % 7
        return "{} week(s) and {} day(s)".format(weeks, remainder)

    def readable_timedelta(days):
        """Return a string of the number of weeks and days included in days.

        Args:
            days (int): number of days to convert
        """
        weeks = days // 7
        remainder = days % 7
        return "{} week(s) and {} day(s)".format(weeks, remainder)

    def readable_timedelta(days):
        """
        Return a string of the number of weeks and days included in days.

        Parameters:
        days -- number of days to convert (int)

        Returns:
        string of the number of weeks and days included in days
        """
        weeks = days // 7
        remainder = days % 7
        return "{} week(s) and {} day(s)".format(weeks, remainder)

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
