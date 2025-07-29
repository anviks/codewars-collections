"""https://www.codewars.com/kata/55905b7597175ffc1a00005a"""

from math import floor, log10


def page_digits(pages):
    result = 0
    digits = floor(log10(pages)) + 1

    for n in range(1, digits):
        result += n * (10 ** n - 10 ** (n - 1))

    result += (pages - (10 ** (digits - 1) - 1)) * digits

    return result
