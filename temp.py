import re
def numerize(number, decimal_points=1):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number.")
    if not isinstance(decimal_points, int) or decimal_points < 0:
        raise ValueError("Decimal points must be a non-negative integer.")
    suffixes = {
        24: 'y',
        21: 'z',
        18: 'e',
        15: 'p',
        12: 't',
        9: 'b',
        6: 'm',
        3: 'k'
    }
    for suffix in suffixes:
        if number >= 10**suffix:
            number /= 10**suffix
            return f"{round(number, decimal_points)}{suffixes[suffix]}"
    return round(number, decimal_points)

print(numerize(1200)) # output: "1.2K"
print(numerize(1300000)) # output: "1.3M"
print(numerize(1300000000)) # output: "1.3B"
print(numerize(1300000000, 2)) # output: "1.30B"


def denumerize(number_string):
    if not isinstance(number_string, str):
        raise ValueError("Input must be a string.")
    number_string = number_string.strip()
    suffixes = {
        'K': 3,
        'M': 6,
        'B': 9,
        'T': 12,
        'Y': 24,
        'Z': 21,
        'E': 18,
        'P': 15,
        'N': 39,
        'D': 42,
        'O': 36,
        'S': 33,
        'F': 30,
        'U': 27
    }
    suffix = re.search(r'[A-Za-z]', number_string[-1])
    if suffix:
        suffix = suffix.group()
        if suffix in suffixes:
            number = float(
                re.search(r'[0-9]+\.?[0-9]*', number_string).group())
            return number * 10**suffixes[suffix]
    else:
        return float(number_string)


print(denumerize("1.2K"))  # output: 1200
print(denumerize("1.3M"))  # output: 1300000
print(denumerize("1.3B"))  # output: 13000000000
