import datetime

def next_dow(d,day):
    while d.weekday()!=day:
        d+=datetime.timedelta(1)
    return d  