"""https://www.codewars.com/kata/526571aae218b8ee490006f4"""

import unittest

from solution_bit_counting import count_bits


class FixedTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(4), 1)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(9), 2)
        self.assertEqual(count_bits(10), 2)
