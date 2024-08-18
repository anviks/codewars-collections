"""https://www.codewars.com/kata/5765870e190b1472ec0022a2"""

from solution_path_finder_number_1_can_you_reach_the_exit import *


def test_example_1():
    maze = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])
    assert path_finder(maze) is True, repr(maze)


def test_example_1__example_2():
    maze = "\n".join([
        ".W.",
        ".W.",
        "W.."
    ])
    assert path_finder(maze) is False, repr(maze)


def test_example_1__example_3():
    maze = "\n".join([
        "......",
        "......",
        "......",
        "......",
        "......",
        "......"
    ])
    assert path_finder(maze) is True, repr(maze)


def test_example_1__example_4():
    maze = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
    ])
    assert path_finder(maze) is False, repr(maze)
