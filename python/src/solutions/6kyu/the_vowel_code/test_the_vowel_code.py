"""https://www.codewars.com/kata/53697be005f803751e0015aa"""

from solution_the_vowel_code import *


def test_fixed_tests__basic_test_cases():
    assert encode('hello') == 'h2ll4'
    assert encode('How are you today?') == 'H4w 1r2 y45 t4d1y?'
    assert encode('This is an encoding test.') == 'Th3s 3s 1n 2nc4d3ng t2st.'
    assert decode('h2ll4') == 'hello'
