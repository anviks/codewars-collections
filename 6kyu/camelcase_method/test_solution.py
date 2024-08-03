"""https://www.codewars.com/kata/587731fda577b3d1b0001196"""

import unittest

from solution import camel_case


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(camel_case("test case"), "TestCase")
        self.assertEqual(camel_case("camel case method"), "CamelCaseMethod")
        self.assertEqual(camel_case("say hello "), "SayHello")
        self.assertEqual(camel_case(" camel case word"), "CamelCaseWord")
        self.assertEqual(camel_case(""), "")
