"""https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004"""

from solution_highest_rank_number_in_an_array import *


def test_fixed_tests__basic_test_cases():
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]) == 10
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]) == 12
    assert highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]) == 3
    assert highest_rank([1, 2, 3]) == 3
    assert highest_rank([1, 1, 2, 3]) == 1
    assert highest_rank([1, 1, 2, 2, 3]) == 2
