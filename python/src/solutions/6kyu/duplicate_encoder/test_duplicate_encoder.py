"""https://www.codewars.com/kata/54b42f9314d9229fd6000d9c"""

from solution_duplicate_encoder import *


def test_duplicate_encoder__basic_test_cases():
    assert duplicate_encode('din') == '((('
    assert duplicate_encode('recede') == '()()()'
    assert duplicate_encode('Success') == ')())())', 'should ignore case'
    assert duplicate_encode('(( @') == '))(('
