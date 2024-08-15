"""https://www.codewars.com/kata/5503013e34137eeeaa001648"""

import unittest

from solution_5503013e34137eeeaa001648 import diamond


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        expected = " *\n"
        expected += "***\n"
        expected += " *\n"
        self.assertEqual(diamond(1), "*\n")
        self.assertEqual(diamond(2), None)
        self.assertEqual(diamond(3), expected)
        self.assertEqual(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        self.assertEqual(diamond(0), None)
        self.assertEqual(diamond(-3), None)
