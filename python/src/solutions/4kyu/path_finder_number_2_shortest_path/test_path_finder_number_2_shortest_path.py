"""https://www.codewars.com/kata/57658bfa28ed87ecfa00058a"""

from solution_path_finder_number_2_shortest_path import *

a = "\n".join([
    ".W.",
    ".W.",
    "..."
])

b = "\n".join([
    ".W.",
    ".W.",
    "W.."
])

c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
])

d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])


def test_example():
    assert path_finder(a) == 4
    assert path_finder(b) is False
    assert path_finder(c) == 10
    assert path_finder(d) is False
