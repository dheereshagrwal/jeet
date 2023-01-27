from utils.api import *
from utils.date_helpers import *


def get_total_range_percent(ticker,day):
    from_time = get_timestamp(day, "14:30:00")  # 2.30pm
    to_time = get_timestamp(day, "21:00:00")  # 9pm
    results = get_2_minute_data(ticker, from_time, to_time)
    total_range_percent = None
    if not results:
        return total_range_percent
    max_h = 0
    min_l = float("inf")
    for res in results:
        max_h = max(max_h, res["h"])
        min_l = min(min_l, res["l"])
    total_range_percent = 100*(max_h - min_l)/min_l
    return total_range_percent


def get_misc_2_min_data_till_3_58(ticker, day):
    # only till 3.58pm
    #return
    highest_v_timestamp = None
    highest_v_n = None
    highest_v = None
    aggregate_v_before_highest_v = None
    highest_bar_v_ratio_percent = None

    from_time = day
    to_time = get_timestamp(day, "20:58:00")  # 8.58pm
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        return highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent
    #we have results
    highest_v = float("-inf")
    aggregate_v_before_highest_v = 0
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


def get_misc_2_min_data_premarket(ticker,day):
    from_time = day
    to_time = get_timestamp(day, "14:28:00")  # 2.28pm
    results = get_2_minute_data(ticker, from_time, to_time)

    premarket_v_cumulative = None
    premarket_h = None
    premarket_h_timestamp = None
    premarket_l = None
    premarket_l_timestamp = None
    premarket_range_percent = None
    daily_volume_forecast = None
    if not results:
        return premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast
    premarket_v_cumulative = 0
    premarket_h = float("-inf")
    premarket_l = float("inf")

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


def get_misc_2_min_data_first_hour(ticker,day):
    from_time = get_timestamp(day, "14:30:00")  # 2.30pm
    to_time = get_timestamp(day, "15:30:00")  # 3.30pm
    results = get_2_minute_data(ticker, from_time, to_time)

    first_hour_v_cumulative = None
    if not results:
        return first_hour_v_cumulative
    first_hour_v_cumulative = 0
    for res in results:
        first_hour_v_cumulative += res["v"]
    return first_hour_v_cumulative


def get_misc_2_min_data_regular_market(ticker,day):
    from_time = day
    to_time = day
    results = get_2_minute_data(ticker, from_time, to_time)
    regular_market_h_timestamp = None
    regular_market_l_timestamp = None
    if not results:
        return regular_market_h_timestamp, regular_market_l_timestamp
    regular_market_h = float("-inf")
    regular_market_l = float("inf")
    for res in results:
        regular_market_h = max(regular_market_h, res["h"])
        regular_market_l = min(regular_market_l, res["l"])
        if regular_market_l == res["l"]:
            regular_market_l_timestamp = res["t"]
        if regular_market_h == res["h"]:
            regular_market_h_timestamp = res["t"]
    return regular_market_h_timestamp, regular_market_l_timestamp


def get_l_after_abs_h(abs_h, abs_h_timestamp, ticker,day):
    from_time = abs_h_timestamp
    to_time = day

    l_after_abs_h = None
    if not from_time or not abs_h:
        print(f"abs_h_timestamp is None for {ticker}")
        return l_after_abs_h
    results = get_2_minute_data(ticker, from_time, to_time)
    if not results:
        print(f"results is None in get_l_after_abs_h for {ticker}")
        return l_after_abs_h
    
    l_after_abs_h = float("inf")
    for res in results:
        l_after_abs_h = min(l_after_abs_h, res["l"])
    # if l_after_abs_h > abs_h:
    #     print(f"l_after_abs_h {l_after_abs_h} > abs_h {abs_h} for {ticker} which means that stock did not go down ")
    #     return 0
    return l_after_abs_h


def get_abs_h(ticker,day):
    from_time = get_timestamp(day, "9:00:00")  # 9.00am
    to_time = day
    results = get_2_minute_data(ticker, from_time, to_time)

    abs_h = None
    abs_h_timestamp = None
    if not results:
        return abs_h, abs_h_timestamp
    abs_h = float("-inf")
    for res in results:
        abs_h = max(abs_h, res["h"])
        if abs_h == res["h"]:
            abs_h_timestamp = res["t"]
    return abs_h, abs_h_timestamp
