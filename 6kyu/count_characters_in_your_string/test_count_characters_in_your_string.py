"""https://www.codewars.com/kata/52efefcbcdf57161d4000091"""

import unittest

from solution_count_characters_in_your_string import count


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(count('aba'), {'a': 2, 'b': 1})
        self.assertEqual(count(''), {})
        self.assertEqual(count('aa'), {'a': 2})
        self.assertEqual(count('aabb'), {'b': 2, 'a': 2})
