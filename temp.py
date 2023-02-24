s = '-'

#check if s string is float number
if not s[:-1].replace('.','',1).isdigit():
    print('s is a not a number')
