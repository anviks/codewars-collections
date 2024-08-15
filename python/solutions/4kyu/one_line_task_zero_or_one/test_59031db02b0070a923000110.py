"""https://www.codewars.com/kata/one-line-task-zero-or-one"""

import unittest

from solution_59031db02b0070a923000110 import zero_or_one

sample_test_cases = [
    (1, [[1, 1, 0, 1]], [1, 1, 0, 1]),

    (3, [[1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]], [1, 0, 1, 0, 1]),

    (3, [[1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1],
         [0, 1, 1, 1, 0]], [1, 1, 1, 0, 1]),

    (5, [[1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1]], [0, 0, 0, 0, 0]),
]


class SampleTests(unittest.TestCase):
    def test_testing_zero_or_one(self):
        for n, s, expected in sample_test_cases:
            self.assertEqual(expected, zero_or_one(n, s))
