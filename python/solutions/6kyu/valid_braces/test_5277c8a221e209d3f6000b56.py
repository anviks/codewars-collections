"""https://www.codewars.com/kata/5277c8a221e209d3f6000b56"""

import unittest

from solution_5277c8a221e209d3f6000b56 import valid_braces


class ValidBraces(unittest.TestCase):
    def assert_valid(self, string):
        self.assertEqual(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

    def assert_invalid(self, string):
        self.assertEqual(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))

    def test_sample_tests(self):
        self.assert_valid("()")
        self.assert_invalid("(}")
        self.assert_valid("[]")
        self.assert_invalid("[(])")
        self.assert_valid("{}")
        self.assert_valid("{}()[]")
        self.assert_valid("([{}])")
        self.assert_invalid("([}{])")
        self.assert_valid("{}({})[]")
        self.assert_valid("(({{[[]]}}))")
        self.assert_invalid("(((({{")
        self.assert_invalid(")(}{][")
        self.assert_invalid("())({}}{()][][")
