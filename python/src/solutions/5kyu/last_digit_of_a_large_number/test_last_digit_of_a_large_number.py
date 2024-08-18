"""https://www.codewars.com/kata/5511b2f550906349a70004e1"""

import pytest

from solution_last_digit_of_a_large_number import *


@pytest.mark.parametrize('n1, n2, exp', [
    (4, 1, 4),
    (4, 2, 6),
    (9, 7, 9),
    (10, 10 ** 10, 0),
    (2 ** 200, 2 ** 300, 6),
    (3715290469715693021198967285016729344580685479654510946723,
     68819615221552997273737174557165657483427362207517952651, 7),
])
def test_should_work_for_example_tests(n1, n2, exp):
    assert last_digit(n1, n2) == exp, f"Testing last_digit({n1}, {n2})"


def test_testing_x_0_must_return_1():
    for nmbr in range(1, 9):
        a = nmbr ** nmbr
        assert last_digit(a, 0) == 1, f"Testing last_digit({a}, 0)"
