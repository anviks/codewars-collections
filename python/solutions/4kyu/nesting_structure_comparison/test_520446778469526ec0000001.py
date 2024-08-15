"""https://www.codewars.com/kata/520446778469526ec0000001"""

import unittest

from solution import same_structure_as


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(same_structure_as([1, [1, 1]], [2, [2, 2]]), "[1,[1,1]] same as [2,[2,2]]")
        self.assertFalse(same_structure_as([1, [1, 1]], [[2, 2], 2]), "[1,[1,1]] not same as [[2,2],2]")
