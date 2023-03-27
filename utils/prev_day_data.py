from utils.pivot_points import *
from utils.api import *


def get_misc_prev_day_data(ticker, today_o, today_h,prev_day):
    result = get_prev_day_data(ticker,prev_day)
    gap_percent = None
    pdc_range_percent = None
    pp = None
    r4 = None
    r5 = None
    r6 = None
    s4 = None
    s5 = None
    s6 = None
    prev_c = None
    prev_h = None
    prev_l = None
    if result:
        prev_c = result["c"]
        prev_h = result["h"]
        prev_l = result["l"]
        if today_o and prev_c:
            gap_percent = 100*(today_o - prev_c)/prev_c
        if today_h and prev_c:
            pdc_range_percent = 100*(today_h - prev_c)/prev_c
        if prev_c and prev_h and prev_l:
            pp,  r4, r5, r6,  s4, s5, s6 = get_pivot_points(prev_c, prev_h, prev_l)
    return gap_percent, pdc_range_percent, pp, r4, r5, r6, s4, s5, s6, prev_c, prev_h, prev_l
