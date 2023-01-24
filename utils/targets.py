def get_targets(prev_c, abs_h, l_after_abs_h):
    target_0 = target_25 = target_50 = target_75 = target_100 = None
    if (not prev_c) or (not abs_h) or (not l_after_abs_h):
        return target_0, target_25, target_50, target_75, target_100
    range = abs_h - prev_c
    quartile_percent = 100*((abs_h - l_after_abs_h)/range)
    target_0 = target_25 = target_50 = target_75 = target_100 = 0
    print(f"quartile_percent: {quartile_percent}")
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
