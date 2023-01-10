def get_targets(prev_c, curr_h, curr_l):
    if (not prev_c) or (not curr_h) or (not curr_l):
        return [None]*5
    range = curr_h - prev_c
    quartile_percent = 100*(curr_l/range)
    target_0 = target_25 = target_50 = target_75 = target_100 = 0
    if quartile_percent < 25:
        target_0 = 1
    elif quartile_percent >= 25 and quartile_percent < 50:
        target_0 = 1
        target_25 = 1
    elif quartile_percent >= 50 and quartile_percent < 75:
        target_0 = 1
        target_25 = 1
        target_50 = 1
    elif quartile_percent >= 75 and quartile_percent < 100:
        target_0 = 1
        target_25 = 1
        target_50 = 1
        target_75 = 1
    elif quartile_percent >= 100:
        target_0 = 1
        target_25 = 1
        target_50 = 1
        target_75 = 1
        target_100 = 1
    return target_0, target_25, target_50, target_75, target_100
