"""https://www.codewars.com/kata/57ea70aa5500adfe8a000110"""

import unittest

from solution_57ea70aa5500adfe8a000110 import fold_array

sample_test_cases = [
    #             array     runs    expected
    ([1, 2, 3, 4, 5], 1, [6, 6, 3]),
    ([1, 2, 3, 4, 5], 2, [9, 6]),
    ([1, 2, 3, 4, 5], 3, [15]),
    ([-9, 9, -8, 8, 66, 23], 1, [14, 75, 0]),
]


class SampleTests(unittest.TestCase):
    def test_sample_tests(self):
        for orig_array, runs, expected in sample_test_cases:
            array = orig_array.copy()
            actual = fold_array(array, runs)
            if array == orig_array:
                self.assertEqual(actual, expected)
            else:
                self.fail('The input array should not be modified')
