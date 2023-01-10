import pandas as pd
import os
from utils.api import *
from utils.helpers import *
import time
from utils.prev_day_data import *
from utils.data_2_minute import *
from utils.dt import *
from utils.targets import *
from utils.finviz import *
from dotenv import load_dotenv
load_dotenv()
sleep_time = int(os.getenv("sleep_time"))
print(f"sleep_time is {sleep_time}")



cols = ["name", "ticker", "primary_exchange", "list_date", "type",
        "market_cap", "share_class_shares_outstanding", "publisher_name", "amp_url", "description", "keywords", "Cash In Hand(M)", "Cash Need", "DT Overall Risk", "DT offering Ability", "DT Amt Excluding Shelf", "DT Historical", "c", "h", "l", "o", "v", "vw", "Total Range %", "Gap %", "Premarket Volume (cumm)", "Premarket High", "Premarket High Time", "Premarket Low", "Premarket Low Time", "Premarket Range %",  "Daily Volume Forecast", "First Hour Volume", "Regular Market High Time", "Regular Market Low Time", "Highest Volume Time", "Highest Volume Time - num_trans", "Highest Volume", "Aggregated Volume Before Highest Volume", "Highest Bar Volume Ratio Percentage", "pp", "r1", "r2", "r3", "r4", "r5", "r6", "s1", "s2", "s3", "s4", "s5", "s6", "Target 0%", "Target 25%",
        "Target 50%", "Target 75%", "Target 100%", "Shs Float", "Inst Own", "Short Float", "Insider Own"]

try:
    file = open("tickers.txt", "r")
    tickers = file.readlines()
    file.close()
    # remove new line character from each ticker
    tickers = [x.strip().upper() for x in tickers]
except:
    print('tickers.txt does not exist, quitting....')
    exit()


df = pd.DataFrame(columns=cols)
for ticker in tickers:
    print(f"ticker is {ticker}")
    cash_in_hand, cash_need, dt_overall_risk, dt_offering_ability, dt_amount_exceeding_shelf, dt_historical = get_dilution_data(
        ticker)
    print(f"cash_in_hand {cash_in_hand} cash_need {cash_need} dt_overall_risk {dt_overall_risk} dt_offering_ability {dt_offering_ability} dt_amount_exceeding_shelf {dt_amount_exceeding_shelf} dt_historical {dt_historical}")
    name, ticker, primary_exchange, type_, list_date, market_cap, share_class_shares_outstanding = get_basic_info(
        ticker)
    print(f"name {name} ticker {ticker} primary_exchange {primary_exchange} type {type_} list_date {list_date} market_cap {market_cap} share_class_shares_outstanding {share_class_shares_outstanding}")
    time.sleep(sleep_time)
    curr_day = get_curr_day()
    c, h, l, o, v, vw, n = get_daily_data(ticker)
    print(f"c {c} h {h} l {l} o {o} v {v} vw {vw} n {n}")
    time.sleep(sleep_time)
    # get previous day misc data
    # if we did not get daily data that means o is None, we will handle that case
    gap_percent, pp, r1, r2, r3, r4, r5, r6, s1, s2, s3, s4, s5, s6, prev_c = get_misc_prev_day_data(
        ticker, o)
    print(f"gap_percent {gap_percent} pp {pp} r1 {r1} r2 {r2} r3 {r3} r4 {r4} r5 {r5} r6 {r6} s1 {s1} s2 {s2} s3 {s3} s4 {s4} s5 {s5} s6 {s6} prev_c {prev_c}")
    # 2-minute bars
    time.sleep(sleep_time)
    total_range_percent = get_total_range_percent(ticker)
    print(f"total_range_percent {total_range_percent}")
    time.sleep(sleep_time)
    highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent = get_misc_2_min_data_today_till_3_58(
        ticker)
    print(f"highest_v_timestamp {highest_v_timestamp} highest_v_n {highest_v_n} highest_v {highest_v} aggregate_v_before_highest_v {aggregate_v_before_highest_v} highest_bar_v_ratio_percent {highest_bar_v_ratio_percent}")
    time.sleep(sleep_time)
    premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast = get_misc_2_min_data_premarket(
        ticker)
    print(f"premarket_v_cumulative {premarket_v_cumulative} premarket_h {premarket_h} premarket_h_timestamp {premarket_h_timestamp} premarket_l {premarket_l} premarket_l_timestamp {premarket_l_timestamp} premarket_range_percent {premarket_range_percent} daily_volume_forecast {daily_volume_forecast}")
    time.sleep(sleep_time)
    first_hour_v = get_misc_2_min_data_first_hour(ticker)
    print(f"first_hour_v {first_hour_v}")
    time.sleep(sleep_time)
    # get regular market high and low timestamps
    regular_market_h_timestamp, regular_market_l_timestamp = get_misc_2_min_data_regular_market(
        ticker)
    print(
        f"regular_market_h_timestamp {regular_market_h_timestamp} regular_market_l_timestamp {regular_market_l_timestamp}")
    time.sleep(sleep_time)
    publisher_name, amp_url, description, keywords = get_news(ticker,curr_day)
    print(
        f"publisher_name {publisher_name} amp_url {amp_url} description {description} keywords {keywords}")
    target_0, target_25, target_50, target_75, target_100 = get_targets(
        prev_c, h, l)
    print(
        f"target_0 {target_0} target_25 {target_25} target_50 {target_50} target_75 {target_75} target_100 {target_100}")
    shs_float, inst_own, short_float_percent, insider_own = get_finviz_data(
        ticker)
    print(
        f"shs_float: {shs_float} inst_own: {inst_own} short_float_percent: {short_float_percent} insider_own: {insider_own}")

    # use concat to add new row to df
    try:
        df = pd.concat([df, pd.DataFrame([[name, ticker, primary_exchange, list_date, type_,
                                           market_cap, share_class_shares_outstanding, publisher_name, amp_url, description, keywords, cash_in_hand, cash_need, dt_overall_risk, dt_offering_ability, dt_amount_exceeding_shelf, dt_historical, c, h, l, o, v, vw, total_range_percent, gap_percent, premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast, first_hour_v, regular_market_h_timestamp, regular_market_l_timestamp, highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent,
                        pp, r1, r2, r3, r4, r5, r6, s1, s2, s3, s4, s5, s6, target_0, target_25, target_50, target_75, target_100, shs_float, inst_own, short_float_percent, insider_own]], columns=cols)], ignore_index=True)
    except:
        print("Error in concat")

# write to excel with a sheet number for the date
curr_day = get_curr_day()
# if file exists then append the sheet
filename = os.getenv('filename')
if os.path.exists(filename):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=curr_day, index=False)
else:
    df.to_excel(filename, sheet_name=curr_day, index=False)

