import datetime

A_GIGASECOND_DELTA = datetime.timedelta(seconds=10 ** 9)


def add(a_datetime: datetime.datetime) -> datetime.datetime:
    return a_datetime + A_GIGASECOND_DELTA
