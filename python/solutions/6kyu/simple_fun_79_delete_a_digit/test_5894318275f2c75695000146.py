"""https://www.codewars.com/kata/5894318275f2c75695000146"""

import unittest

from solution_5894318275f2c75695000146 import delete_digit


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(delete_digit(152), 52)
        self.assertEqual(delete_digit(1001), 101)
        self.assertEqual(delete_digit(10), 1)
