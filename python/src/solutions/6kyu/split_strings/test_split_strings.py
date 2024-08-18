"""https://www.codewars.com/kata/515de9ae9dcfc28eb6000001"""

from solution_split_strings import *


def test_fixed_tests__basic_test_cases():
    tests = (('asdfadsf', ['as', 'df', 'ad', 'sf']), ('asdfads', ['as', 'df', 'ad', 's_']), ('', []), ('x', ['x_']))
    for inp, exp in tests:
        assert solution(inp) == exp
