"""https://www.codewars.com/kata/626a887e8a33feabd6ad8f25"""

import unittest

from solution_626a887e8a33feabd6ad8f25 import predicate


class ExamplesFromTheDescription(unittest.TestCase):
    def test_1_argument(self):
        @predicate
        def is_even(num):
            return num % 2 == 0

        @predicate
        def is_positive(num):
            return num > 0

        self.assertEqual((is_even & is_positive)(4), True)
        self.assertEqual((is_even & is_positive)(3), False)
        self.assertEqual((is_even | is_positive)(3), True)
        self.assertEqual((~is_even & is_positive)(3), True)

    def test_0_arguments(self):
        @predicate
        def to_be():
            return True

        self.assertEqual((to_be | ~to_be)(), True)

    def test_2_arguments_keyword_arguments(self):
        @predicate
        def is_equal(a, b):
            return a == b

        @predicate
        def is_less_than(a, b):
            return a < b

        self.assertEqual((is_less_than | is_equal)(1, 2), True)
        self.assertEqual((is_less_than | is_equal)(2, b=2), True)
        self.assertEqual((is_less_than | is_equal)(a=3, b=2), False)

    def test_should_be_callable_and_behave_like_the_original(self):
        @predicate
        def is_less_than(a, b):
            return a < b

        self.assertEqual(is_less_than(1, 2), True)
        self.assertEqual(is_less_than(2, 2), False)
        self.assertEqual(is_less_than(3, 2), False)
