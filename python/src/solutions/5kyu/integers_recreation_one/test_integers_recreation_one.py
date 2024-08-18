"""https://www.codewars.com/kata/55aa075506463dac6600010d"""

from solution_integers_recreation_one import *


def test_tests__fixed_tests():
    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]
