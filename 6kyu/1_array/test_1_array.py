"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9"""

import unittest

from solution_1_array import up_array


class SampleTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(up_array([2, 3, 9]), [2, 4, 0])
        self.assertEqual(up_array([9, 9]), [1, 0, 0])
        self.assertEqual(up_array([0, 4, 2]), [0, 4, 3])
        self.assertEqual(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
        self.assertEqual(up_array([1, 2, 3, 9]), [1, 2, 4, 0])
        self.assertEqual(up_array([9, 9, 9, 9]), [1, 0, 0, 0, 0])
        self.assertEqual(up_array([0, 1, 3, 7]), [0, 1, 3, 8])
        self.assertEqual(up_array([1, -9]), None)
