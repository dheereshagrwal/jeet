from datetime import datetime
def convert_millis_to_local_date(millis):
    date = datetime.fromtimestamp(millis/1000)
    return date


date = convert_millis_to_local_date(1673240400000)
print(date)