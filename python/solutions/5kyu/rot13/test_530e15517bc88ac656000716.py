"""https://www.codewars.com/kata/530e15517bc88ac656000716"""
import unittest

from solution_530e15517bc88ac656000716 import rot13


class FixedTests(unittest.TestCase):
    def test_should_obtain_correct_rot13_encoding_on_fixed_strings(self):
        self.assertEqual(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        self.assertEqual(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
                         'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')
