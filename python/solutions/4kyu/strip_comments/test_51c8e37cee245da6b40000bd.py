"""https://www.codewars.com/kata/strip-comments"""

import unittest

from solution_51c8e37cee245da6b40000bd import strip_comments


class TestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')
        self.assertEqual(strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
        self.assertEqual(strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
