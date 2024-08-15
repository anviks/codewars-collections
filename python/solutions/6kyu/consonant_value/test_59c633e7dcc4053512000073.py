"""https://www.codewars.com/kata/59c633e7dcc4053512000073"""

import unittest

from solution import solve


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(solve("cozy"), 51)
        self.assertEqual(solve("xyzzy"), 126)
        self.assertEqual(solve("zodiac"), 26)
        self.assertEqual(solve("chruschtschov"), 80)
        self.assertEqual(solve("khrushchev"), 38)
        self.assertEqual(solve("strength"), 57)
        self.assertEqual(solve("catchphrase"), 73)
        self.assertEqual(solve("twelfthstreet"), 103)
        self.assertEqual(solve("mischtschenkoana"), 80)
