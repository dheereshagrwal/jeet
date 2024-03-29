
# get apiKey from .env file

import yfinance as yf
import re
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


def get_ticker_info(ticker):
    resp = get_response(
        f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apiKey}")
    name = None
    ticker = None
    primary_exchange = None
    type_ = None
    list_date = None
    market_cap = None
    share_class_shares_outstanding = None
    try:
        result = resp.json()["results"]
    except:
        return name, ticker, primary_exchange, type_, list_date, market_cap, share_class_shares_outstanding
    # absolute fields - name, ticker
    name = result["name"]
    ticker = result["ticker"]
    try:
        primary_exchange = result["primary_exchange"]
    except:
        pass
    try:
        type_ = result["type"]
    except:
        pass
    try:
        list_date = result["list_date"]
    except:
        pass
    try:
        market_cap = result["market_cap"]
    except:
        pass
    try:
        share_class_shares_outstanding = result["share_class_shares_outstanding"]
    except:
        pass
    return name, ticker, primary_exchange, type_, list_date, market_cap, share_class_shares_outstanding


'''
def get_descriptions(ticker, today):
    resp = get_response(
        f"https://api.polygon.io/v2/reference/news?published_utc={today}&ticker={ticker}&apiKey={apiKey}")
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


def get_daily_data(ticker,today):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{today}/{today}?adjusted=true&sort=asc&apiKey={apiKey}")
    c = None
    h = None
    l = None
    o = None
    v = None
    vw = None
    n = None
    try:
        results = resp.json()["results"]
    except:
        return c, h, l, o, v, vw, n
    result = results[0]
    c = result["c"]
    h = result["h"]
    l = result["l"]
    o = result["o"]
    v = result["v"]
    try:
        vw = result["vw"]
    except:
        pass
    try:
        n = result["n"]
    except:
        pass
    return c, h, l, o, v, vw, n


def get_2_minute_data(ticker, from_time, to_time):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/2/minute/{from_time}/{to_time}?adjusted=true&sort=asc&apiKey={apiKey}")
    results = None
    try:
        results = resp.json()["results"]
    except:
        pass
    return results


def get_prev_day_data(ticker,prev_day):
    resp = get_response(
        f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{prev_day}/{prev_day}?adjusted=true&sort=asc&apiKey={apiKey}")
    result = None
    try:
        results = resp.json()["results"]
        result = results[0]
    except:
        pass
    return result


def get_result_from_single_description(ticker, description):
    # split description according to '\n'
    description = description.split('\n')
    description = list(filter(None, description))
    description = [x.strip() for x in description]
    print(
        f"len of description: {len(description)} and description: {description}")
    pattern = re.compile(r'\([A-Za-z]+\s*:\s*' + ticker + '\)')
    result = [i for i in description if pattern.search(i)]
    print(f"result: {result}")


def get_news(ticker,prev_day,today):
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
    print(f"prev_day: {prev_day} and today: {today}")
    for n in news:
        try:
            providerPublishTime = n["providerPublishTime"]
            published_date = convert_seconds_to_utc_date(providerPublishTime)
            # if published_date is either prev_day or today, then add title to titles and publisher to publishers
            if published_date == prev_day or published_date == today:
                publisher = n["publisher"]
                title = n["title"]
                publishers += publisher + "\n"
                titles.append(title)
        except:
            continue
    return publishers[:-1], titles
