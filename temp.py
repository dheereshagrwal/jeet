# convert 2023-01-09 to milliseconds at 9.30.00
import pandas as pd
date_str = "2023-01-10"

def get_timestamp(date, time):
    date = date + " "+time
    date = pd.to_datetime(date)
    date = date.timestamp()
    date = date * 1000
    return int(date)

print(get_timestamp(date_str, "09:30:00"))


