# convert 2023-01-09 to milliseconds at 9.30.00
import pandas as pd


def get_timestamp(date, time):
    date = date + " "+time
    date = pd.to_datetime(date)
    date = date.timestamp()
    date = date * 1000
    return int(date)



