"""https://www.codewars.com/kata/576986639772456f6f00030c"""

import unittest

from solution_path_finder_3_the_alpinist import path_finder


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        a = "\n".join([
            "000",
            "000",
            "000"
        ])

        b = "\n".join([
            "010",
            "010",
            "010"
        ])

        c = "\n".join([
            "010",
            "101",
            "010"
        ])

        d = "\n".join([
            "0707",
            "7070",
            "0707",
            "7070"
        ])

        e = "\n".join([
            "700000",
            "077770",
            "077770",
            "077770",
            "077770",
            "000007"
        ])

        f = "\n".join([
            "777000",
            "007000",
            "007000",
            "007000",
            "007000",
            "007777"
        ])

        g = "\n".join([
            "000000",
            "000000",
            "000000",
            "000010",
            "000109",
            "001010"
        ])

        self.assertEqual(path_finder(a), 0)
        self.assertEqual(path_finder(b), 2)
        self.assertEqual(path_finder(c), 4)
        self.assertEqual(path_finder(d), 42)
        self.assertEqual(path_finder(e), 14)
        self.assertEqual(path_finder(f), 0)
        self.assertEqual(path_finder(g), 4)
