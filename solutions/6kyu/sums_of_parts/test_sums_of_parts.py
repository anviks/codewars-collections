"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b"""

import unittest

from solution_sums_of_parts import parts_sums


class Tests(unittest.TestCase):
    def dotest(self, ls, expected):
        actual = parts_sums(ls)
        self.assertEqual(actual, expected)

    def test_basic(self):
        self.dotest([], [0])
        self.dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0])
        self.dotest([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0])

        self.dotest([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358],
                    [10037855, 9293730, 9292795, 9292388, 9291934,
                     9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0])
