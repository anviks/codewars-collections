"""https://www.codewars.com/kata/62eedcfc729041000ea082c1"""
import inspect

from solution_code_golf_number_pyramid_series_6_revised_left_or_right import *


def test_code_length():
    function_length = len(inspect.getsource(left_right))
    assert function_length <= 72, f"{function_length} should be less or equal to 72."


def test_sample_tests__basic_tests():
    assert left_right(1) == 'C'
    assert left_right(2) == 'L'
    assert left_right(3) == 'R'
    assert left_right(4) == 'L'
    assert left_right(5) == 'C'
    assert left_right(6) == 'R'
