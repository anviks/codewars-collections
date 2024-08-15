"""https://www.codewars.com/kata/660d55d0ba01e5016c85cfeb"""

import unittest

from solution import slice


class SampleTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(slice("A", "A"), "A", "")
        self.assertEqual(slice("A", "F"), "ABCDEF", "")

        print("lowercase")
        self.assertEqual(slice("l", "l"), "l", "")
        self.assertEqual(slice("a", "z"), "abcdefghijklmnopqrstuvwxyz", "")
