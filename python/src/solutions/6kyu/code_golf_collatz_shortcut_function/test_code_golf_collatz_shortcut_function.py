"""https://www.codewars.com/kata/664bb069388167b5923b1688"""

import inspect
import unittest

from solution_code_golf_collatz_shortcut_function import g


class CodeLengthTest(unittest.TestCase):
    def test_code_length(self):
        source = inspect.getsource(g)
        self.assertLessEqual(len(source), 26, f"Your code is too long: {len(source)} should be no more than 26.")


class FixedTests(unittest.TestCase):
    def test_testing_simple_numbers(self):
        self.assertEqual(g(5), 8, "Tiny odd input")
        self.assertEqual(g(10), 5, "Tiny even input")
        self.assertEqual(g(15), 23, "Another tiny odd input")
        self.assertEqual(g(1515), 2273.0, "This may or may not be a hint")
