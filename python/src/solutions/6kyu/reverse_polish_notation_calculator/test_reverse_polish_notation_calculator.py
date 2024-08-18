"""https://www.codewars.com/kata/52f78966747862fc9a0009ae"""

from solution_reverse_polish_notation_calculator import *


def test_example():
    assert calc('') == 0, 'Should work with empty string'
    assert calc('3') == 3, 'Should parse numbers'
    assert calc('3.5') == 3.5, 'Should parse float numbers'
    assert calc('1 3 +') == 4, 'Should support addition'
    assert calc('1 3 *') == 3, 'Should support multiplication'
    assert calc('1 3 -') == -2, 'Should support subtraction'
    assert calc('4 2 /') == 2, 'Should support division'
