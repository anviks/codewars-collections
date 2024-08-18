"""https://www.codewars.com/kata/52549d3e19453df56f0000fe"""

from solution_fibonacci_reloaded import *


def test_fixed_tests__basic_test_cases():
    assert fib(1) == 0, 'fib(1) failed'
    assert fib(2) == 1, 'fib(2) failed'
    assert fib(3) == 1, 'fib(3) failed'
    assert fib(4) == 2, 'fib(4) failed'
    assert fib(5) == 3, 'fib(5) failed'
