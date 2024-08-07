"""https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08"""

import unittest

from solution_multiplication_table import multiplication_table


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(multiplication_table(1), [[1]])
        self.assertEqual(multiplication_table(2), [[1, 2], [2, 4]])
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        self.assertEqual(multiplication_table(4), [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
        self.assertEqual(multiplication_table(5),
                         [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20],
                          [5, 10, 15, 20, 25]])
