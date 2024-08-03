"""https://www.codewars.com/kata/52b757663a95b11b3d00062d"""

import unittest

from solution import to_weird_case


class ToWeirdCase(unittest.TestCase):
    def test_should_return_the_correct_value_for_a_single_word(self):
        self.assertEqual(to_weird_case('This'), 'ThIs')
        self.assertEqual(to_weird_case('is'), 'Is')

    def test_should_return_the_correct_value_for_multiple_words(self):
        self.assertEqual(to_weird_case('THIs iS a TEST'), 'ThIs Is A TeSt')
