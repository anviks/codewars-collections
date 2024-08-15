"""https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991"""
import unittest

from solution_reverse_or_rotate import rev_rot


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(rev_rot("1234", 0), "")
        self.assertEqual(rev_rot("", 0), "")
        self.assertEqual(rev_rot("1234", 5), "")
        self.assertEqual(rev_rot("733049910872815764", 5), "330479108928157")
