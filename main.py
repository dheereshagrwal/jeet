import pandas as pd
import os
from utils.api import *
from utils.date_helpers import *
import time
from utils.prev_day_data import *
from utils.data_2_minute import *
from utils.dt import *
from utils.targets import *
from utils.finviz import *
from utils.ft import *
from utils.keywords import *
from dotenv import load_dotenv
from numerize_denumerize import numerize
load_dotenv()
sleep_time = int(os.getenv("sleep_time"))
print(f"sleep_time is {sleep_time}")

# '''
try:
    file = open("tickers.txt", "r")
    tickers = file.readlines()
    file.close()
    # remove whitespace  from each ticker
    tickers = [x.strip().upper() for x in tickers]
except:
    print('tickers.txt does not exist, quitting....')
    exit()

print()

df = pd.DataFrame()
for ticker in tickers:
    print(f"ticker is {ticker}")
    cash_in_hand, cash_need, dt_overall_risk, dt_offering_ability, dt_amount_exceeding_shelf, dt_historical = get_dilution_data(
        ticker)
    print(f"cash_in_hand {cash_in_hand} cash_need {cash_need} dt_overall_risk {dt_overall_risk} dt_offering_ability {dt_offering_ability} dt_amount_exceeding_shelf {dt_amount_exceeding_shelf} dt_historical {dt_historical}")
    name, ticker, primary_exchange, type_, list_date, market_cap, share_class_shares_outstanding = get_ticker_info(
        ticker)
    print(f"name {name} ticker {ticker} primary_exchange {primary_exchange} type {type_} list_date {list_date} market_cap {market_cap} share_class_shares_outstanding {share_class_shares_outstanding}")
    if market_cap:
        market_cap = numerize.numerize(market_cap, 2)
    if share_class_shares_outstanding:
        share_class_shares_outstanding = numerize.numerize(
            share_class_shares_outstanding, 2)
    time.sleep(sleep_time)
    curr_day = get_curr_day()
    prev_day = get_prev_day()
    c, h, l, o, v, vw, n = get_daily_data(ticker)
    print(f"c {c} h {h} l {l} o {o} v {v} vw {vw} n {n}")

    time.sleep(sleep_time)
    # get previous day misc data
    # if we did not get daily data that means o is None, we will handle that case
    gap_percent, pdc_range_percent, pp, r4, r5, r6, s4, s5, s6, prev_c = get_misc_prev_day_data(
        ticker, o, h)
    print(
        f"gap_percent {gap_percent} pdc_range_percent {pdc_range_percent} pp {pp} r4 {r4} r5 {r5} r6 {r6} s4 {s4} s5 {s5} s6 {s6} prev_c {prev_c}")
    if gap_percent:
        gap_percent = round(gap_percent, 2)
    if pdc_range_percent:
        pdc_range_percent = round(pdc_range_percent, 2)
    if pp:
        pp = round(pp, 2)
        r4 = round(r4, 2)
        r5 = round(r5, 2)
        r6 = round(r6, 2)
        s4 = round(s4, 2)
        s5 = round(s5, 2)
        s6 = round(s6, 2)
    # 2-minute bars
    time.sleep(sleep_time)
    total_range_percent = get_total_range_percent(ticker)
    print(f"total_range_percent {total_range_percent}")
    if total_range_percent:
        total_range_percent = round(total_range_percent, 2)
    time.sleep(sleep_time)
    highest_v_timestamp, highest_v_n, highest_v, aggregate_v_before_highest_v, highest_bar_v_ratio_percent = get_misc_2_min_data_today_till_3_58(
        ticker)
    print(f"highest_v_timestamp {highest_v_timestamp} highest_v_n {highest_v_n} highest_v {highest_v} aggregate_v_before_highest_v {aggregate_v_before_highest_v} highest_bar_v_ratio_percent {highest_bar_v_ratio_percent}")
    if aggregate_v_before_highest_v:
        aggregate_v_before_highest_v = numerize.numerize(
            aggregate_v_before_highest_v, 2)
    if highest_bar_v_ratio_percent:
        highest_bar_v_ratio_percent = round(highest_bar_v_ratio_percent, 2)
    if highest_v:
        highest_v = numerize.numerize(highest_v, 2)
    if highest_v_timestamp:
        highest_v_timestamp = convert_millis_to_local_time(
            highest_v_timestamp)
    time.sleep(sleep_time)
    premarket_v_cumulative, premarket_h, premarket_h_timestamp, premarket_l, premarket_l_timestamp, premarket_range_percent, daily_volume_forecast = get_misc_2_min_data_premarket(
        ticker)
    print(f"premarket_v_cumulative {premarket_v_cumulative} premarket_h {premarket_h} premarket_h_timestamp {premarket_h_timestamp} premarket_l {premarket_l} premarket_l_timestamp {premarket_l_timestamp} premarket_range_percent {premarket_range_percent} daily_volume_forecast {daily_volume_forecast}")

    if daily_volume_forecast:
        daily_volume_forecast = numerize.numerize(daily_volume_forecast, 2)
    if premarket_range_percent:
        premarket_range_percent = round(premarket_range_percent, 2)
    if premarket_h_timestamp:
        premarket_h_timestamp = convert_millis_to_local_time(
            premarket_h_timestamp)
    if premarket_l_timestamp:
        premarket_l_timestamp = convert_millis_to_local_time(
            premarket_l_timestamp)
    time.sleep(sleep_time)
    first_hour_v = get_misc_2_min_data_first_hour(ticker)
    print(f"first_hour_v {first_hour_v}")
    time.sleep(sleep_time)
    # get regular market high and low timestamps
    regular_market_h_timestamp, regular_market_l_timestamp = get_misc_2_min_data_regular_market(
        ticker)
    print(
        f"regular_market_h_timestamp {regular_market_h_timestamp} regular_market_l_timestamp {regular_market_l_timestamp}")
    if regular_market_h_timestamp:
        regular_market_h_timestamp = convert_millis_to_local_time(
            regular_market_h_timestamp)
    if regular_market_l_timestamp:
        regular_market_l_timestamp = convert_millis_to_local_time(
            regular_market_l_timestamp)

    time.sleep(sleep_time)
    abs_h, abs_h_timestamp = get_abs_h(ticker)
    print(f"abs_h {abs_h} abs_h_timestamp {abs_h_timestamp}")
    l_after_abs_h = get_l_after_abs_h(abs_h, abs_h_timestamp, ticker)
    print(f"l_after_abs_h {l_after_abs_h}")
    target_0, target_25, target_50, target_75, target_100 = get_targets(
        prev_c, abs_h, l_after_abs_h)
    print(
        f"target_0 {target_0} target_25 {target_25} target_50 {target_50} target_75 {target_75} target_100 {target_100}")
    shs_float, inst_own, short_float_percent, insider_own, atr = get_finviz_data(
        ticker)
    print(f"shs_float {shs_float} inst_own {inst_own} short_float_percent {short_float_percent} insider_own {insider_own} atr {atr}")
    daily_ft_percent = get_daily_ft_percent(v, shs_float)
    print(f"daily_ft_percent {daily_ft_percent}")
    if daily_ft_percent:
        daily_ft_percent = round(daily_ft_percent, 2)
    pm_ft_percent = get_premarket_ft_percent(premarket_v_cumulative, shs_float)
    print(f"pm_ft_percent {pm_ft_percent}")
    if pm_ft_percent:
        pm_ft_percent = round(pm_ft_percent, 2)
    first_hour_ft_percent = get_first_hour_ft_percent(first_hour_v, shs_float)
    print(f"first_hour_ft_percent {first_hour_ft_percent}")
    if first_hour_ft_percent:
        first_hour_ft_percent = round(first_hour_ft_percent, 2)
    if v:
        v = numerize.numerize(v, 2)
    if first_hour_v:
        first_hour_v = numerize.numerize(first_hour_v, 2)
    if premarket_v_cumulative:
        premarket_v_cumulative = numerize.numerize(premarket_v_cumulative, 2)
    publishers, titles = get_news(ticker)
    print(f"publishers {publishers} titles {titles}")
    keywords = get_keywords(titles)
    print(f"keywords {keywords}")
    titles = '\n'.join(titles)
    try:
        data = {'prev_day': prev_day, 'curr_day': curr_day,  'ticker': ticker, 'Shs Float': shs_float, 'Inst Own': inst_own, 'Insider Own': insider_own, 'market_cap': market_cap, 'Short Float': short_float_percent, 'ATR': atr, 'PDC Range %': pdc_range_percent, 'total_range_percent': total_range_percent, 'premarket_range_percent': premarket_range_percent, 'gap_percent': gap_percent, 'Cash In Hand': cash_in_hand, 'Cash Need': cash_need, 'DT Overall Risk': dt_overall_risk, 'DT Offering Ability': dt_offering_ability, 'DT Amount Excluding Shelf': dt_amount_exceeding_shelf, 'DT Historical': dt_historical, 'Daily FT %': daily_ft_percent, 'PM FT %': pm_ft_percent, 'First Hour FT %': first_hour_ft_percent, 'v': v,  'Premarket Volume (cumm)': premarket_v_cumulative, 'First Hour Volume': first_hour_v, 'Daily Volume Forecast': daily_volume_forecast, 'Highest Volume': highest_v,  'Highest Volume Time - num_trans': highest_v_n,  'Aggregated Volume Before Highest Volume': aggregate_v_before_highest_v, 'Highest Bar Volume Ratio %': highest_bar_v_ratio_percent, 'c': c, 'h': h, 'l': l, 'o': o,  'vw': vw,  'Target 0%': target_0, 'Target 25%': target_25, 'Target 50%': target_50, 'Target 75%': target_75, 'Target 100%': target_100, 'Premarket High': premarket_h, 'Premarket Low': premarket_l, 'Premarket High Time': premarket_h_timestamp,
                'Premarket Low Time': premarket_l_timestamp,  'Regular Market High Time': regular_market_h_timestamp, 'Regular Market Low Time': regular_market_l_timestamp,  'Highest Volume Time': highest_v_timestamp,  'name': name, 'primary_exchange': primary_exchange, 'list_date': list_date, 'type': type_, 'share_class_shares_outstanding': share_class_shares_outstanding, 'keywords': keywords, 'publishers': publishers, 'titles': titles, 'pp': pp, 'r4': r4, 'r5': r5, 'r6': r6, 's4': s4, 's5': s5, 's6': s6}
        row = pd.DataFrame([data])
        df = pd.concat([df, row])
        # check if the master csv exists and if it does then append to it
        with open('master.csv', 'a') as f:
            row.to_csv(f, header=False, index=False)

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
# '''
