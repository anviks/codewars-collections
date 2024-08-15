"""https://www.codewars.com/kata/54d512e62a5e54c96200019e"""

import unittest

from solution_54d512e62a5e54c96200019e import prime_factors


class Testing(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        self.assertEqual(prime_factors(7919), "(7919)")
