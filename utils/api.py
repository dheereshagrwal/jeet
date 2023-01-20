
# get apiKey from .env file

from utils.date_helpers import *
# from date_helpers import *
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv("apiKey")


def get_response(url):
    response = requests.get(url)
    return response


def get_basic_info(ticker):
    resp = get_response(
        f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apiKey}")
    try:
        result = resp.json()["results"]
    except:
        return [None]*7
    # absolute fields - name, ticker
    name = result["name"]
    ticker = result["ticker"]
    try:
        primary_exchange = result["primary_exchange"]
    except:
        primary_exchange = None
    try:
        type_ = result["type"]
    except:
        type_ = None
    try:
        list_date = result["list_date"]
    except:
        list_date = None
    try:    
        market_cap = result["market_cap"]
    except:
        market_cap = None
    try:
        share_class_shares_outstanding = result["share_class_shares_outstanding"]
    except:
        share_class_shares_outstanding = None
    return name, ticker, primary_exchange, type_, list_date, market_cap, share_class_shares_outstanding

'''
def get_descriptions(ticker, curr_day):
    resp = get_response(
        f"https://api.polygon.io/v2/reference/news?published_utc={curr_day}&ticker={ticker}&apiKey={apiKey}")
    pattern = re.compile(r'\([A-Za-z]+\s*:\s*' + ticker + '\)')
    try:
        results = resp.json()["results"]
        descriptions = ""
    except:
        return None
    for result in results:
        try:
            #the property description might not exist
            description = result["description"]
            #replace the character \xa0 with a space
            description = description.replace("\xa0", " ")
            description = description.split("\n")
            description = list(filter(None, description))
            description = [x.strip() for x in description]
            matches_index = [i for i,s in enumerate(description) if pattern.search(s)]
            descriptions += description[match_index] + "\n"
            
        except:
            pass
    return descriptions[:-1]
'''

def get_daily_data(ticker):
    curr_day = get_curr_day()
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{curr_day}/{curr_day}?adjusted=true&sort=asc&apiKey={apiKey}")
    try:
        results = resp.json()["results"]
    except:
        return [None]*7
    result = results[0]
    c = result["c"]
    h = result["h"]
    l = result["l"]
    o = result["o"]
    v = result["v"]
    try:
        vw = result["vw"]
    except:
        vw = None
    try:
        n = result["n"]
    except:
        n = None
    return c, h, l, o, v, vw, n


def get_2_minute_data(ticker, from_time, to_time):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/2/minute/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey={apiKey}")
    try:
        results = resp.json()["results"]
    except:
        return None
    return results


def get_prev_day_data(ticker):
    prev_day = get_prev_day()
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{prev_day}/{prev_day}?adjusted=true&sort=asc&apiKey={apiKey}")
    try:
        results = resp.json()["results"]
    except:
        return None
    result = results[0]
    return result



import re
def get_result_from_single_description(ticker,description):
    #split description according to '\n'
    description = description.split('\n')
    description = list(filter(None, description))
    description = [x.strip() for x in description]
    print(f"len of description: {len(description)} and description: {description}")
    pattern = re.compile(r'\([A-Za-z]+\s*:\s*' + ticker + '\)')
    result = [i for i in description if pattern.search(i)]
    print(f"result: {result}")

import yfinance as yf
def get_news(ticker):
    try:
        news = yf.Ticker(ticker).news
        print(f"news: {news}")
        if not news:
            print(f"news does not exist for {ticker}")
            return [None]*2
    except:
        print(f"news does not exist for {ticker}")
        return [None]*2
    publishers = ""
    titles = []
    prev_day = get_prev_day()
    curr_day = get_curr_day()
    print(f"prev_day: {prev_day} and curr_day: {curr_day}")
    for n in news:
        try:
            providerPublishTime = n["providerPublishTime"]
            published_date = convert_seconds_to_utc_date(providerPublishTime)
            # if published_date is either prev_day or curr_day, then add title to titles and publisher to publishers
            if published_date == prev_day or published_date == curr_day:
                publisher = n["publisher"]
                title = n["title"]
                publishers += publisher + "\n"
                titles.append(title)
        except:
            continue
    return publishers[:-1], titles
