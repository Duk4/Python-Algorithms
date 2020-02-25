import math


def century(year):
    return math.ceil(year/100)


print(century(1600))
print(century(1601))
