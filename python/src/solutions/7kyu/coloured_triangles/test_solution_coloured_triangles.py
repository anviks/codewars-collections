"""https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111"""

import unittest

from solution_coloured_triangles import triangle


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(triangle('GB'), 'R')
        self.assertEqual(triangle('RRR'), 'R')
        self.assertEqual(triangle('RGBG'), 'B')
        self.assertEqual(triangle('RBRGBRB'), 'G')
        self.assertEqual(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
        self.assertEqual(triangle('B'), 'B')
