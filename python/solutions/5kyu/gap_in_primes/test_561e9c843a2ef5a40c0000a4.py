"""https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4"""

import unittest

from solution_561e9c843a2ef5a40c0000a4 import gap


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(gap(2, 100, 110), [101, 103])
        self.assertEqual(gap(4, 100, 110), [103, 107])
        self.assertEqual(gap(6, 100, 110), None)
        self.assertEqual(gap(8, 300, 400), [359, 367])
        self.assertEqual(gap(10, 300, 400), [337, 347])
        self.assertEqual(gap(2, 100, 103), [101, 103])
