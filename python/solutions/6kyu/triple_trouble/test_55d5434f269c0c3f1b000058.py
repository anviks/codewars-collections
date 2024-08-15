"""https://www.codewars.com/kata/55d5434f269c0c3f1b000058"""

import unittest

from solution_55d5434f269c0c3f1b000058 import triple_double


class TripleTrouble(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(triple_double(451999277, 41177722899), 1)
        self.assertEqual(triple_double(1222345, 12345), 0)
        self.assertEqual(triple_double(12345, 12345), 0)
        self.assertEqual(triple_double(666789, 12345667), 1)
        self.assertEqual(triple_double(10560002, 100), 1)
        self.assertEqual(triple_double(1112, 122), 0)
