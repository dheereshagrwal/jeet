from numerize_denumerize import denumerize
def get_daily_ft_percent(v, shs_float):
    if v and shs_float:
        return 100*v/denumerize.denumerize(shs_float)
    return None


def get_premarket_ft_percent(premarket_v_cumulative, shs_float):
    if premarket_v_cumulative and shs_float:
        return 100*premarket_v_cumulative/denumerize.denumerize(shs_float)
    return None


def get_first_hour_ft_percent(first_hour_v, shs_float):
    if first_hour_v and shs_float:
        return 100*first_hour_v/denumerize.denumerize(shs_float)
    return None
