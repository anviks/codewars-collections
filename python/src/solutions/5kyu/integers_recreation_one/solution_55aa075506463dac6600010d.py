"""https://www.codewars.com/kata/55aa075506463dac6600010d"""

import math


def get_squared_divisors(n: int):
    for num in range(1, int(math.sqrt(n)) + 1):
        if n % num == 0:
            yield num ** 2
            yield (n // num) ** 2


def list_squared(m: int, n: int):
    result = []
    for num in range(m, n + 1):
        squares_sum = sum(set(get_squared_divisors(num)))
        if math.sqrt(squares_sum) % 1 == 0:
            result.append([num, squares_sum])
    return result
