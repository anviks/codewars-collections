"""https://www.codewars.com/kata/5202ef17a402dd033c000009"""

import unittest

from solution_title_case import title_case


class SampleTests(unittest.TestCase):
    def test_tests(self):
        self.assertEqual(title_case(''), '')
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')
