"""https://www.codewars.com/kata/54b42f9314d9229fd6000d9c"""

import unittest

from solution import duplicate_encode


class DuplicateEncoder(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEqual(duplicate_encode("(( @"), "))((")
