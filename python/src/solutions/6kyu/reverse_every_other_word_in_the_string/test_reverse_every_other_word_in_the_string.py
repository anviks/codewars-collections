"""https://www.codewars.com/kata/58d76854024c72c3e20000de"""

import pytest

from solution_reverse_every_other_word_in_the_string import *



def test_fixed_tests__basic_test_cases():
    assert reverse_alternate('Did it work?') == 'Did ti work?'
    assert reverse_alternate('I really hope it works this time...') == 'I yllaer hope ti works siht time...'
    assert reverse_alternate('Reverse this string, please!') == 'Reverse siht string, !esaelp'
    assert reverse_alternate('Have a beer') == 'Have a beer'
    assert reverse_alternate('   ') == ''
    assert reverse_alternate('This is not a test ') == 'This si not a test'
    assert reverse_alternate('This       is a  test ') == 'This si a tset'
