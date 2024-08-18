"""https://www.codewars.com/kata/5541f58a944b85ce6d00006a"""

from solution_product_of_consecutive_fib_numbers import *


def test_fixed_tests__basic_test_cases():
    assert product_fib(4895) == [55, 89, True]
    assert product_fib(5895) == [89, 144, False]
