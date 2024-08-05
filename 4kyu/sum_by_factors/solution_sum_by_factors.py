"""https://www.codewars.com/kata/54d496788776e49e6b00052f"""

from functools import cache

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
