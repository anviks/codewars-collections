"""https://www.codewars.com/kata/660d55d0ba01e5016c85cfeb"""

from solution_alphabet_slice_puzzle import *


def test_sample_tests__basic_test_cases():
    assert slice('A', 'A') == 'A'
    assert slice('A', 'F') == 'ABCDEF'

    print('lowercase')
    assert slice('l', 'l') == 'l'
    assert slice('a', 'z') == 'abcdefghijklmnopqrstuvwxyz'
