"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9"""

from solution_plus_1_array import *


def test_sample_tests__examples():
    assert up_array([2, 3, 9]) == [2, 4, 0]
    assert up_array([9, 9]) == [1, 0, 0]
    assert up_array([0, 4, 2]) == [0, 4, 3]
    assert up_array([4, 3, 2, 5]) == [4, 3, 2, 6]
    assert up_array([1, 2, 3, 9]) == [1, 2, 4, 0]
    assert up_array([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
    assert up_array([0, 1, 3, 7]) == [0, 1, 3, 8]
    assert up_array([1, -9]) is None
