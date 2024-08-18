"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048"""

from solution_scramblies import *


def dotest(s1, s2, expected):
    actual = scramble(s1, s2)
    assert actual == expected, f'With\ns1 = "{s1}"\ns2 = "{s2}"'


def test_tests__sample_tests():
    for s1, s2, expected in [
        ('rkqodlw', 'world', True),
        ('cedewaraaossoqqyt', 'codewars', True),
        ('katas', 'steak', False),
        ('scriptjava', 'javascript', True),
        ('scriptingjava', 'javascript', True)
    ]:
        dotest(s1, s2, expected)


def test_tests__example_large_test():
    s1 = 'abcdefghijklmnopqrstuvwxyz' * 10000
    s2 = 'zyxcba' * 9000
    dotest(s1, s2, True)
