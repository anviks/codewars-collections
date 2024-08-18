"""https://www.codewars.com/kata/52efefcbcdf57161d4000091"""

from solution_count_characters_in_your_string import *


def test_basic_tests__basic_tests():
    assert count('aba') == {'a': 2, 'b': 1}
    assert count('') == {}
    assert count('aa') == {'a': 2}
    assert count('aabb') == {'b': 2, 'a': 2}
