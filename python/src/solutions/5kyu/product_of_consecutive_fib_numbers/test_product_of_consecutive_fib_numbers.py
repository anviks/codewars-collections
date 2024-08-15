"""https://www.codewars.com/kata/5541f58a944b85ce6d00006a"""

import unittest

from solution_product_of_consecutive_fib_numbers import product_fib


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(product_fib(4895), [55, 89, True])
        self.assertEqual(product_fib(5895), [89, 144, False])
