"""https://www.codewars.com/kata/57658bfa28ed87ecfa00058a"""
import unittest

from solution_57658bfa28ed87ecfa00058a import path_finder

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


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(path_finder(a), 4)
        self.assertFalse(path_finder(b))
        self.assertEqual(path_finder(c), 10)
        self.assertFalse(path_finder(d))
