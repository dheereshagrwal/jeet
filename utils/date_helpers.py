from datetime import datetime
import pandas as pd



def get_timestamp(date, time):
    date = date + " " + time
    date = pd.to_datetime(date)
    date = date.timestamp()
    date = date * 1000
    return int(date)

def convert_millis_to_local_time(millis):
    #I want only the local time, not the date
    time = datetime.fromtimestamp(millis/1000).strftime("%H:%M:%S")
    return time


def convert_seconds_to_utc_date(seconds):
    #convert to utc not to local time
    return datetime.utcfromtimestamp(seconds).strftime('%Y-%m-%d')
