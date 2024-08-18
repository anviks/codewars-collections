"""https://www.codewars.com/kata/54d512e62a5e54c96200019e"""

from solution_primes_in_numbers import *


def test_testing__fixed_tests():
    assert prime_factors(7775460) == '(2**2)(3**3)(5)(7)(11**2)(17)'
    assert prime_factors(7919) == '(7919)'
