"""https://www.codewars.com/kata/53697be005f803751e0015aa"""

import unittest

from solution_the_vowel_code import encode, decode


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(encode('hello'), 'h2ll4')
        self.assertEqual(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
        self.assertEqual(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
        self.assertEqual(decode('h2ll4'), 'hello')
