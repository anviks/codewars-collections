"""https://www.codewars.com/kata/52fba2a9adcd10b34300094c"""

import unittest

from solution_matrix_transpose import transpose


class TestCase(unittest.TestCase):
    def test_basic_test(self):
        self.assertEqual(transpose([[1]]), [[1]])
        self.assertEqual(transpose([[1, 2, 3]]), [[1], [2], [3]])
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                         [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])
