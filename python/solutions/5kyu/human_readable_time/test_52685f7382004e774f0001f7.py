"""https://www.codewars.com/kata/52685f7382004e774f0001f7"""

import unittest

from solution_52685f7382004e774f0001f7 import make_readable


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(59), "00:00:59")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(3599), "00:59:59")
        self.assertEqual(make_readable(3600), "01:00:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(86400), "24:00:00")
        self.assertEqual(make_readable(359999), "99:59:59")
