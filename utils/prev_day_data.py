from utils.pivot_points import *
from utils.api import *


def get_misc_prev_day_data(ticker, today_o):
    result = get_prev_day_data(ticker)
    gap_percent = None
    if result:
        prev_c = result["c"]
        prev_h = result["h"]
        prev_l = result["l"]
        if today_o:
            gap_percent = 100 - (prev_c/today_o * 100)
    # get pivot points
    if result:
        pp, r1, r2, r3, r4, r5, r6, s1, s2, s3, s4, s5, s6 = get_pivot_points(prev_c, prev_h, prev_l)
        # gap_percent could be None if today_o is None
        return gap_percent, pp, r1, r2, r3, r4, r5, r6, s1, s2, s3, s4, s5, s6, prev_c
    else:
        # gap_percent could not be None if today_o exists
        return [gap_percent] + [None]*14
