"""https://www.codewars.com/kata/52e1476c8147a7547a000811"""

import unittest
from re import fullmatch

from solution_regex_password_validation import regex


class Tests(unittest.TestCase):
    def do_test(self, string: str, expected: bool):
        actual = bool(fullmatch(regex, string))
        self.assertEqual(actual, expected, f'for string "{string}"')

    def test_sample_tests(self):
        self.do_test('fjd3IR9', True)
        self.do_test('ghdfj32', False)
        self.do_test('DSJKHD23', False)
        self.do_test('dsF43', False)
        self.do_test('4fdg5Fj3', True)
        self.do_test('DHSJdhjsU', False)
        self.do_test('fjd3IR9.;', False)
        self.do_test('fjd3  IR9', False)
        self.do_test('djI38D55', True)
        self.do_test('a2.d412', False)
        self.do_test('JHD5FJ53', False)
        self.do_test('!fdjn345', False)
        self.do_test('jfkdfj3j', False)
        self.do_test('123', False)
        self.do_test('abc', False)
        self.do_test('123abcABC', True)
        self.do_test('ABC123abc', True)
        self.do_test('Password123', True)
