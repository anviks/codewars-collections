"""https://www.codewars.com/kata/529adbf7533b761c560004e5"""


def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)

        return cache[n]

    return wrapper


@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
