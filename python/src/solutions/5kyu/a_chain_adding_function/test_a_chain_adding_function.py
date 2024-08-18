"""https://www.codewars.com/kata/539a0e4d85e3425cb0000a88"""

from solution_a_chain_adding_function import *



def test_basic_tests():
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
