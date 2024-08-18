"""https://www.codewars.com/kata/5270d0d18625160ada0000e4"""

from solution_greed_is_good import *


def test_example_tests__example_cases():
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
