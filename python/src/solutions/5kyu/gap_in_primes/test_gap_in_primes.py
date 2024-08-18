"""https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4"""

from solution_gap_in_primes import *


def test_fixed_tests__basic_test_cases():
    assert gap(2, 100, 110) == [101, 103]
    assert gap(4, 100, 110) == [103, 107]
    assert gap(6, 100, 110) is None
    assert gap(8, 300, 400) == [359, 367]
    assert gap(10, 300, 400) == [337, 347]
    assert gap(2, 100, 103) == [101, 103]
