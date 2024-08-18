"""https://www.codewars.com/kata/5894318275f2c75695000146"""

from solution_simple_fun_number_79_delete_a_digit import *


def test_fixed_tests__basic_test_cases():
    assert delete_digit(152) == 52
    assert delete_digit(1001) == 101
    assert delete_digit(10) == 1
