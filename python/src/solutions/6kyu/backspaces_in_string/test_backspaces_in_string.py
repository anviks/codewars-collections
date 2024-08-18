"""https://www.codewars.com/kata/5727bb0fe81185ae62000ae3"""

from solution_backspaces_in_string import *


def test_example():
    assert clean_string('abc#d##c') == 'ac'
    assert clean_string('abc####d##c#') == ''
    assert clean_string('#######') == ''
    assert clean_string('') == ''
