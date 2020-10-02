from random import randrange
from datetime import datetime, timedelta


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)