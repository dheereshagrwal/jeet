
# get apiKey from .env file

from utils.helpers import *
from datetime import date, datetime
import requests
import pandas as pd
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
    name = result["name"]
    ticker = result["ticker"]
    primary_exchange = result["primary_exchange"]
    type = result["type"]
    list_date = result["list_date"]
    market_cap = result["market_cap"]
    share_class_shares_outstanding = result["share_class_shares_outstanding"]
    return name, ticker, primary_exchange, type, list_date, market_cap, share_class_shares_outstanding


def get_news(ticker, curr_day):
    resp = get_response(
        f"https://api.polygon.io/v2/reference/news?published_utc={curr_day}&ticker={ticker}&apiKey={apiKey}")
    try:
        results = resp.json()["results"]
    except:
        return [None]*4
    result = None
    publisher_name = None
    amp_url = None
    description = None
    keywords = None
    for res in results:
        if len(res["tickers"]) == 1:
            result = res
            break

    if result:
        publisher_name = result["publisher"]["name"]
        print(f"publisher_name: {publisher_name}")
        amp_url = result["amp_url"]
        print(f"amp_url: {amp_url}")
        description = result["description"]
        print(f"description: {description}")
        try:
            keywords = result["keywords"]
        except:
            keywords = None
        print(f"keywords: {keywords}")
    return publisher_name, amp_url, description, keywords


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
    vw = result["vw"]
    n = result["n"]
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
