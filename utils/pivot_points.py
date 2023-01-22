def get_pp(c, h, l):
    pp = (c + h + l) / 3
    return pp


def get_r4(c, h, l):
    r4 = c + ((h - l)*(1.1/2))
    return r4


def get_r5(c, h, l):
    r5 = c + ((h - l)*(0.865))
    return r5


def get_r6(c, h, l):
    r6 = c*(h/l)
    return r6


def get_s4(c, h, l):
    s4 = c - ((h - l)*(1.1/2))
    return s4


def get_s5(c, h, l):
    s5 = c - ((h - l)*(0.865))
    return s5


def get_s6(c, h, l):
    s6 = (c - (h / l * c - c))
    return s6

def get_PDC(c,h,l):
    pass

def get_pivot_points(c,h,l):
    return get_pp(c,h,l), get_r4(c,h,l), get_r5(c,h,l), get_r6(c,h,l),  get_s4(c,h,l), get_s5(c,h,l), get_s6(c,h,l)