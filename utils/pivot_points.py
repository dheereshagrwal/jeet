def get_pp(c, h, l):
    pp = None
    if c and h and l:
        pp = (c + h + l) / 3
    else:
        print(f"Error: get_pp() - c: {c}, h: {h}, l: {l}")
    return pp


def get_r4(c, h, l):
    r4 = None
    if c and h and l:
        r4 = c + ((h - l)*(1.1/2))
    else:
        print(f"Error: get_r4() - c: {c}, h: {h}, l: {l}")
    return r4


def get_r5(c, h, l):
    r5 = None
    if c and h and l:
        r5 = c + ((h - l)*(0.865))
    else:
        print(f"Error: get_r5() - c: {c}, h: {h}, l: {l}")
    return r5


def get_r6(c, h, l):
    r6 = None
    if c and h and l:
        r6 = c*(h/l)
    else:
        print(f"Error: get_r6() - c: {c}, h: {h}, l: {l}")
    return r6


def get_s4(c, h, l):
    s4 = None
    if c and h and l:
        s4 = c - ((h - l)*(1.1/2))
    else:
        print(f"Error: get_s4() - c: {c}, h: {h}, l: {l}")
    return s4


def get_s5(c, h, l):
    s5 = None
    if c and h and l:
        s5 = c - ((h - l)*(0.865))
    else:
        print(f"Error: get_s5() - c: {c}, h: {h}, l: {l}")
    return s5


def get_s6(c, h, l):
    s6 = None
    if c and h and l:
        s6 = (c - (h / l * c - c))
    else:
        print(f"Error: get_s6() - c: {c}, h: {h}, l: {l}")
    return s6

def get_PDC(c,h,l):
    pass

def get_pivot_points(c,h,l):
    return get_pp(c,h,l), get_r4(c,h,l), get_r5(c,h,l), get_r6(c,h,l),  get_s4(c,h,l), get_s5(c,h,l), get_s6(c,h,l)