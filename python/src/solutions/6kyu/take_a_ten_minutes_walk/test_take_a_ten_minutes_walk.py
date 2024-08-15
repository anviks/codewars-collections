"""https://www.codewars.com/kata/54da539698b8a2ad76000228"""

import unittest

from solution_54da539698b8a2ad76000228 import is_valid_walk


class WalkValidatorFixedTests(unittest.TestCase):
    def test_should_return_true_for_a_valid_walk(self):
        self.assertEqual(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), True,
                         'should return True')

    def test_should_return_false_if_walk_is_too_long(self):
        self.assertEqual(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']), False,
                         'should return False')

    def test_should_return_false_if_walk_is_too_short(self):
        self.assertEqual(is_valid_walk(['w']), False, 'should return False')

    def test_should_return_false_if_walk_does_not_bring_you_back_to_start(self):
        self.assertEqual(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), False,
                         'should return False')
