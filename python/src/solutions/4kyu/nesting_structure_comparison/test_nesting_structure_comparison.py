"""https://www.codewars.com/kata/520446778469526ec0000001"""

from solution_nesting_structure_comparison import *


def test_example():
    assert same_structure_as([1, [1, 1]], [2, [2, 2]]) is True, '[1,[1,1]] same as [2,[2,2]]'
    assert same_structure_as([1, [1, 1]], [[2, 2], 2]) is False, '[1,[1,1]] not same as [[2,2],2]'
