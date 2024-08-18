"""https://www.codewars.com/kata/52b7ed099cdc285c300001cd"""

from solution_sum_of_intervals import *


def test_fixed_tests__tests():
    assert sum_of_intervals([(1, 5)]) == 4
    assert sum_of_intervals([(1, 5), (6, 10)]) == 8
    assert sum_of_intervals([(1, 5), (1, 5)]) == 4
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7


def test_fixed_tests__large_numbers():
    assert sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000
    assert sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030
