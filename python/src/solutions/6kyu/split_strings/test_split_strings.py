"""https://www.codewars.com/kata/515de9ae9dcfc28eb6000001"""

import unittest

from solution_split_strings import *


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            self.assertEqual(solution(inp), exp)
