"""https://www.codewars.com/kata/62eedcfc729041000ea082c1"""

import unittest
import inspect
from solution_code_golf_number_pyramid_series_6_revised_left_or_right import left_right


class SampleTests(unittest.TestCase):
    def test_code_length(self):
        self.assertTrue(len(inspect.getsource(left_right)) <= 72,
                        f"{len(inspect.getsource(left_right))} should be less or equal to 72.")

    def test_basic_tests(self):
        self.assertEqual(left_right(1), 'C')
        self.assertEqual(left_right(2), 'L')
        self.assertEqual(left_right(3), 'R')
        self.assertEqual(left_right(4), 'L')
        self.assertEqual(left_right(5), 'C')
        self.assertEqual(left_right(6), 'R')
