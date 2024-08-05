"""https://www.codewars.com/kata/52423db9add6f6fc39000354"""

import unittest
from copy import deepcopy

from preloaded import htmlize
from solution_conway_s_game_of_life_unlimited_edition import get_generation


class Tests(unittest.TestCase):
    def do_test(self, input_, generations, expected):
        actual = get_generation(deepcopy(input_), generations)
        message = \
            f'for cells:\n{htmlize(input_)}\nafter {generations} generations,' + \
            f' expected:\n{htmlize(expected)}\nbut got:\n{htmlize(actual)}'
        self.assertEqual(actual, expected, message)

    def test_one_glider(self):
        self.do_test([
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ], 1, [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ])

    def test_two_gliders(self):
        self.do_test([
            [1, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 1]
        ], 16, [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        ])
