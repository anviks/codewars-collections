"""https://www.codewars.com/kata/5842df8ccbd22792a4000245"""

import unittest

from solution import expanded_form


class SampleTests(unittest.TestCase):
    def test_should_pass_sample_tests(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
