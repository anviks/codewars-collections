"""https://www.codewars.com/kata/5270d0d18625160ada0000e4"""

import unittest

from solution import score


class ExampleTests(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(score([5, 1, 3, 4, 1]), 250)
        self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
        self.assertEqual(score([2, 3, 4, 6, 2]), 0)
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)
