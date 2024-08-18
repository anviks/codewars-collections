"""https://www.codewars.com/kata/530e15517bc88ac656000716"""

from solution_rot13_1 import *


def test_fixed_tests__should_obtain_correct_rot13_encoding_on_fixed_strings():
    assert rot13('test') == 'grfg', 'Returned solution incorrect for fixed string = test'
    assert rot13('Test') == 'Grfg', 'Returned solution incorrect for fixed string = Test'
    assert (rot13('aA bB zZ 1234 *!?%')
            == 'nN oO mM 1234 *!?%'), \
        'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%'
