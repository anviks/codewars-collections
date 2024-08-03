"""https://www.codewars.com/kata/5592e3bd57b64d00f3000047"""

import unittest

from solution import find_nb


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(find_nb(4), -1)
        self.assertEqual(find_nb(16), -1)
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)
