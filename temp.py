from dotenv import load_dotenv
load_dotenv()
import os

today = os.getenv("today")
prev_day = os.getenv("prev_day")

if prev_day>=today:
    print("Error: prev_day must be less than today.")
    exit()
else:
    print(f"Today is {today} and yesterday was {prev_day}.")