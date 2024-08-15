"""https://www.codewars.com/kata/52597aa56021e91c93000cb0"""

import unittest

from solution import move_zeros


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([]), [])
