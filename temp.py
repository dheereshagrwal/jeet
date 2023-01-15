def denumerize(n):
    n = n[:-1]
    if n[-1] == 'K':
        return float(n[:-1])*1000
    elif n[-1] == 'M':
        return float(n[:-1])*1000000
    elif n[-1] == 'B':
        return float(n[:-1])*1000000000
    elif n[-1] == 'T':
        return float(n[:-1])*1000000000000
    else:
        return float(n)