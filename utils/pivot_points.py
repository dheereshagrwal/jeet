def get_pp(c, h, l):
    pp = (c + h + l) / 3
    return round(pp, 2)


def get_r1(c, h, l):
    r1 = c + ((h - l)*(1.1/12))
    return round(r1, 2)


def get_r2(c, h, l):
    r2 = c + ((h - l)*(1.1/6))
    return round(r2, 2)


def get_r3(c, h, l):
    r3 = c + ((h - l)*(1.1/4))
    return round(r3, 2)


def get_r4(c, h, l):
    r4 = c + ((h - l)*(1.1/2))
    return round(r4, 2)


def get_r5(c, h, l):
    r5 = c + ((h - l)*(0.865))
    return round(r5, 2)


def get_r6(c, h, l):
    r6 = c*(h/l)
    return round(r6, 2)


def get_s1(c, h, l):
    s1 = c - ((h - l)*(1.1/12))
    return round(s1, 2)


def get_s2(c, h, l):
    s2 = c - ((h - l)*(1.1/6))
    return round(s2, 2)


def get_s3(c, h, l):
    s3 = c - ((h - l)*(1.1/4))
    return round(s3, 2)


def get_s4(c, h, l):
    s4 = c - ((h - l)*(1.1/2))
    return round(s4, 2)


def get_s5(c, h, l):
    s5 = c - ((h - l)*(0.865))
    return round(s5, 2)


def get_s6(c, h, l):
    s6 = (c - (h / l * c - c))
    return round(s6, 2)

def get_PDC(c,h,l):
    pass

def get_pivot_points(c,h,l):
    return get_pp(c,h,l), get_r1(c,h,l), get_r2(c,h,l), get_r3(c,h,l), get_r4(c,h,l), get_r5(c,h,l), get_r6(c,h,l), get_s1(c,h,l), get_s2(c,h,l), get_s3(c,h,l), get_s4(c,h,l), get_s5(c,h,l), get_s6(c,h,l)