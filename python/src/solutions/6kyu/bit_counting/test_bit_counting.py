"""https://www.codewars.com/kata/526571aae218b8ee490006f4"""

from solution_bit_counting import *


def test_fixed_tests__basic_tests():
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2
