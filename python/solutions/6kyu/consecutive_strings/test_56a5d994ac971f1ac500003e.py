"""https://www.codewars.com/kata/56a5d994ac971f1ac500003e"""

import unittest

from solution_56a5d994ac971f1ac500003e import longest_consec


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(
            longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1),
            "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(longest_consec([], 3), "")
        self.assertEqual(
            longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
                           2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
                         "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
