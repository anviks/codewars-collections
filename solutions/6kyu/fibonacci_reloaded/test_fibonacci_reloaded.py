"""https://www.codewars.com/kata/52549d3e19453df56f0000fe"""

import unittest

from solution_fibonacci_reloaded import fib


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(fib(1), 0, 'fib(1) failed')
        self.assertEqual(fib(2), 1, 'fib(2) failed')
        self.assertEqual(fib(3), 1, 'fib(3) failed')
        self.assertEqual(fib(4), 2, 'fib(4) failed')
        self.assertEqual(fib(5), 3, 'fib(5) failed')
