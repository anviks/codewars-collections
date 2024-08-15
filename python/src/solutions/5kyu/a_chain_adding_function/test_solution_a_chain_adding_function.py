"""https://www.codewars.com/kata/539a0e4d85e3425cb0000a88"""

import unittest

from solution_539a0e4d85e3425cb0000a88 import add


class SampleTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(add(1), 1)
        self.assertEqual(add(1)(2), 3)
        self.assertEqual(add(1)(2)(3), 6)
