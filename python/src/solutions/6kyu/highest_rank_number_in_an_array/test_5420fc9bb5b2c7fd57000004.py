"""https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004"""

import unittest

from solution_5420fc9bb5b2c7fd57000004 import highest_rank


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
        self.assertEqual(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
        self.assertEqual(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
        self.assertEqual(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]), 3)
        self.assertEqual(highest_rank([1, 2, 3]), 3)
        self.assertEqual(highest_rank([1, 1, 2, 3]), 1)
        self.assertEqual(highest_rank([1, 1, 2, 2, 3]), 2)
