from utils.api import *
from utils.date_helpers import *


def get_total_range_percent(ticker):
    curr_day = get_curr_day()
    from_time = get_timestamp(curr_day, "14:30:00")  # 2.30pm
    to_time = get_timestamp(curr_day, "21:00:00")  # 9pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return None
    max_h = 0
    min_l = float("inf")
    for res in results:
        max_h = max(max_h, res["h"])
        min_l = min(min_l, res["l"])
    total_range_percent = 100*(max_h - min_l)/min_l
    return total_range_percent


def get_misc_2_min_data_today_till_3_58(ticker):
    curr_day = get_curr_day()
    # only till 3.58pm
    highest_v = 0
    highest_v_timestamp = None
    highest_v_n = 0
    aggregate_v_before_highest_v = 0
    from_time = curr_day
    to_time = get_timestamp(curr_day, "20:58:00")  # 8.58pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return [None]*5
    for res in results:
        highest_v = max(highest_v, res["v"])

    # find index of highest v using indexOf
    for idx, res in enumerate(results):
        if res["v"] == highest_v:
            highest_v_index = idx
            break
    highest_v_n = results[highest_v_index]["n"]
    highest_v_timestamp = results[highest_v_index]["t"]

    for res in results[:highest_v_index]:
        aggregate_v_before_highest_v += res["v"]

    highest_bar_v_ratio_percent = highest_v / aggregate_v_before_highest_v * 100
    return highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent


def get_misc_2_min_data_premarket(ticker):
    curr_day = get_curr_day()
    from_time = curr_day
    to_time = get_timestamp(curr_day, "14:30:00")  # 2.30pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return [None]*7
    premarket_v_cumulative = 0
    premarket_h = 0
    premarket_h_timestamp = None
    premarket_l = float("inf")
    premarket_l_timestamp = None

    for res in results:
        premarket_v_cumulative += res["v"]
        premarket_h = max(premarket_h, res["h"])
        premarket_l = min(premarket_l, res["l"])
        if premarket_l == res["l"]:
            premarket_l_timestamp = res["t"]
        if premarket_h == res["h"]:
            premarket_h_timestamp = res["t"]
    premarket_range_percent = 100*(premarket_h - premarket_l)/premarket_l
    daily_volume_forecast = premarket_v_cumulative * 10
    return premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast


def get_misc_2_min_data_first_hour(ticker):
    curr_day = get_curr_day()
    from_time = get_timestamp(curr_day, "14:30:00")  # 2.30pm
    to_time = get_timestamp(curr_day, "15:30:00")  # 3.30pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return None
    first_hour_v_cumulative = 0
    for res in results:
        first_hour_v_cumulative += res["v"]
    return first_hour_v_cumulative


def get_misc_2_min_data_regular_market(ticker):
    curr_day = get_curr_day()
    from_time = get_timestamp(curr_day, "14:30:00")  # 2.30pm
    to_time = get_timestamp(curr_day, "21:00:00")  # 9.00pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return [None]*4
    regular_market_h_timestamp = None
    regular_market_l_timestamp = None
    regular_market_h = 0
    regular_market_l = float("inf")
    for res in results:
        regular_market_h = max(regular_market_h, res["h"])
        regular_market_l = min(regular_market_l, res["l"])
        if regular_market_l == res["l"]:
            regular_market_l_timestamp = res["t"]
        if regular_market_h == res["h"]:
            regular_market_h_timestamp = res["t"]
    return regular_market_h_timestamp, regular_market_l_timestamp


def get_l_after_abs_h(abs_h, abs_h_timestamp, ticker):
    curr_day = get_curr_day()
    from_time = abs_h_timestamp
    to_time = curr_day
    if not from_time or not abs_h:
        print(f"abs_h_timestamp is None for {ticker}")
        return None
    results = get_2_minute_data(ticker, from_time, to_time)
    l_after_abs_h = float("inf")
    if not results:
        print(f"results is None in get_l_after_abs_h for {ticker}")
        return None
    for res in results:
        l_after_abs_h = min(l_after_abs_h, res["l"])
    # if l_after_abs_h > abs_h:
    #     print(f"l_after_abs_h {l_after_abs_h} > abs_h {abs_h} for {ticker} which means that stock did not go down ")
    #     return 0
    return l_after_abs_h


def get_abs_h(ticker):
    curr_day = get_curr_day()
    from_time = get_timestamp(curr_day, "9:00:00")  # 9.00am
    to_time = curr_day
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return [None]*2
    abs_h = float("-inf")
    abs_h_timestamp = None
    for res in results:
        abs_h = max(abs_h, res["h"])
        if abs_h == res["h"]:
            abs_h_timestamp = res["t"]
    return abs_h, abs_h_timestamp
