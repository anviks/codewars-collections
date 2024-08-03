"""https://www.codewars.com/kata/52549d3e19453df56f0000fe"""


def fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
