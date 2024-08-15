"""https://www.codewars.com/kata/515f51d438015969f7000013"""

import unittest

from solution_515f51d438015969f7000013 import pyramid


class PyramidArray(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(pyramid(0), [])
        self.assertEqual(pyramid(1), [[1]])
        self.assertEqual(pyramid(2), [[1], [1, 1]])
        self.assertEqual(pyramid(3), [[1], [1, 1], [1, 1, 1]])
