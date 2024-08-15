"""https://www.codewars.com/kata/55aa075506463dac6600010d"""


import unittest
from solution import list_squared

class Tests(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])
