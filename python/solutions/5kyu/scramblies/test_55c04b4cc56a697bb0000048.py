"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048"""

import unittest

from solution import scramble


class Tests(unittest.TestCase):
    def dotest(self, s1, s2, expected):
        actual = scramble(s1, s2)
        self.assertEqual(expected, actual, f"With\ns1 = \"{s1}\"\ns2 = \"{s2}\"")

    def test_sample_tests(self):
        for s1, s2, expected in [
            ('rkqodlw', 'world', True),
            ('cedewaraaossoqqyt', 'codewars', True),
            ('katas', 'steak', False),
            ('scriptjava', 'javascript', True),
            ('scriptingjava', 'javascript', True)
        ]:
            self.dotest(s1, s2, expected)

    def test_example_large_test(self):
        s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
        s2 = "zyxcba" * 9_000
        self.dotest(s1, s2, True)
