"""https://www.codewars.com/kata/58235a167a8cb37e1a0000db"""

import unittest

from solution_pair_of_gloves import number_of_pairs


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(number_of_pairs(["red", "red"]), 1)
        self.assertEqual(number_of_pairs(["red", "green", "blue"]), 0)
        self.assertEqual(number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]), 3)
        self.assertEqual(number_of_pairs([]), 0)
        self.assertEqual(number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]), 4)
