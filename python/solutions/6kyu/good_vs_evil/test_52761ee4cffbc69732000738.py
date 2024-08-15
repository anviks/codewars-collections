"""https://www.codewars.com/kata/52761ee4cffbc69732000738"""

import unittest

from solution_52761ee4cffbc69732000738 import good_vs_evil


class SolutionTests(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),
                         'Battle Result: Evil eradicates all trace of Good')
        self.assertEqual(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil')
        self.assertEqual(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), 'Battle Result: No victor on this battle field')
