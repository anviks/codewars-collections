"""https://www.codewars.com/kata/5765870e190b1472ec0022a2"""

import unittest

from solution_path_finder_1_can_you_reach_the_exit import path_finder


class SolutionTests(unittest.TestCase):
    def test_example_1(self):
        maze = "\n".join([
            ".W.",
            ".W.",
            "..."
        ])
        self.assertTrue(path_finder(maze), repr(maze))

    def test_example_2(self):
        maze = "\n".join([
            ".W.",
            ".W.",
            "W.."
        ])
        self.assertFalse(path_finder(maze), repr(maze))

    def test_example_3(self):
        maze = "\n".join([
            "......",
            "......",
            "......",
            "......",
            "......",
            "......"
        ])
        self.assertTrue(path_finder(maze), repr(maze))

    def test_example_4(self):
        maze = "\n".join([
            "......",
            "......",
            "......",
            "......",
            ".....W",
            "....W."
        ])
        self.assertFalse(path_finder(maze), repr(maze))
