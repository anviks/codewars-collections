"""https://www.codewars.com/kata/515f51d438015969f7000013"""

from solution_pyramid_array import *


def test_pyramid_array__sample_tests():
    assert pyramid(0) == []
    assert pyramid(1) == [[1]]
    assert pyramid(2) == [[1], [1, 1]]
    assert pyramid(3) == [[1], [1, 1], [1, 1, 1]]
