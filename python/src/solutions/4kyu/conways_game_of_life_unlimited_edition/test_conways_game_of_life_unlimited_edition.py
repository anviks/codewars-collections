"""https://www.codewars.com/kata/52423db9add6f6fc39000354"""

from copy import deepcopy

from preloaded import htmlize
from solution_conways_game_of_life_unlimited_edition import *


def do_test(input, generations, expected):
    actual = get_generation(deepcopy(input), generations)
    message = f'for cells:\n{htmlize(input)}\nafter {generations} generations,' + f' expected:\n{htmlize(expected)}\nbut got:\n{htmlize(actual)}'

    assert actual == expected, message


def test_tests__one_glider():
    do_test([
        [1, 0, 0],
        [0, 1, 1],
        [1, 1, 0]
    ], 1, [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])


def test_tests__two_gliders():
    do_test([
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
