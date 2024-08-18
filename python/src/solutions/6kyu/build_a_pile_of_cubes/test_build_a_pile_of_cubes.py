"""https://www.codewars.com/kata/5592e3bd57b64d00f3000047"""

from solution_build_a_pile_of_cubes import *


def test_fixed_tests__basic_test_cases():
    assert find_nb(4) == -1
    assert find_nb(16) == -1
    assert find_nb(4183059834009) == 2022
    assert find_nb(24723578342962) == -1
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218
