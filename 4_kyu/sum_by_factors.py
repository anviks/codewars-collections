"""https://www.codewars.com/kata/54d496788776e49e6b00052f"""
import time
from functools import cache

from utils_anviks import stopwatch

primes = [2, 3, 5, 7, 11]


@cache
def is_prime(n):
    for m in range(3, int(n ** .5) + 1, 2):
        if n % m == 0:
            return False

    return True


def get_primes(start, n: int):
    for m in range(start, n, 2):
        if is_prime(m):
            yield m


@stopwatch
def sum_for_list(lst: list[int]) -> list[list[int]]:
    global primes
    largest = max(abs(x) for x in lst)
    if primes[-1] < largest:
        primes.extend(get_primes(primes[-1] + 2, largest))
    prime_factors = []

    for p in primes:
        is_factor = False
        g = [p, 0]
        for m in lst:
            if m % p == 0:
                is_factor = True
                g[1] += m
        if is_factor:
            prime_factors.append(g)

    return prime_factors


def main():
    from util_funcs import pretty_compare

    a = [12, 15]
    b = [[2, 12], [3, 27], [5, 15]]
    pretty_compare(sum_for_list(a), b)

    a = [15, 21, 24, 30, 45]
    b = [[2, 54], [3, 135], [5, 90], [7, 21]]
    pretty_compare(sum_for_list(a), b)

    a = [15, 21, 24, 30, -45]
    b = [[2, 54], [3, 45], [5, 0], [7, 21]]
    pretty_compare(sum_for_list(a), b)

    a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    b = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158],
         [107, 107]]
    pretty_compare(sum_for_list(a), b)

    a = [-29804, -4209, -28265, -72769, -31744]
    b = [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769],
         [5653, -28265], [7451, -29804]]
    pretty_compare(sum_for_list(a), b)

    a = [442913, -650380, -944971, -954453, -481382, 602709, -239086, -37110, -963440, -780165, 753635, -510133,
         -266904, -291070, -581499]
    print(sum_for_list(a))

    a = [392231, -111062, -824816, -214485, -539253, 282845, -610449, -898122, -637035, -400526]
    print(sum_for_list(a))


if __name__ == '__main__':
    main()
