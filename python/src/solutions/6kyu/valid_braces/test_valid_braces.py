"""https://www.codewars.com/kata/5277c8a221e209d3f6000b56"""

from solution_valid_braces import *


def assert_valid(string):
    assert valid_braces(string) is True, 'Expected "{0}" to be valid'.format(string)


def assert_invalid(string):
    assert valid_braces(string) is False, 'Expected "{0}" to be invalid'.format(string)


def test_valid_braces__sample_tests():
    assert_valid('()')
    assert_invalid('(}')
    assert_valid('[]')
    assert_invalid('[(])')
    assert_valid('{}')
    assert_valid('{}()[]')
    assert_valid('([{}])')
    assert_invalid('([}{])')
    assert_valid('{}({})[]')
    assert_valid('(({{[[]]}}))')
    assert_invalid('(((({{')
    assert_invalid(')(}{][')
    assert_invalid('())({}}{()][][')
