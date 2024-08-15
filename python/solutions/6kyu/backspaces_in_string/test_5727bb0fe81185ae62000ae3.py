"""https://www.codewars.com/kata/5727bb0fe81185ae62000ae3"""

import unittest

from solution_5727bb0fe81185ae62000ae3 import clean_string

class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(clean_string('abc#d##c'), "ac")
        self.assertEqual(clean_string('abc####d##c#'), "")
        self.assertEqual(clean_string("#######"), "")
        self.assertEqual(clean_string(""), "")