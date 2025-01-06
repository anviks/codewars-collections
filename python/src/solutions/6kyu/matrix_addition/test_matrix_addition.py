"""https://www.codewars.com/kata/526233aefd4764272800036f"""

from solution_matrix_addition import *


def test_example():
    assert matrix_addition([[1, 2], [1, 2]], [[2, 3], [2, 3]]) == [[3, 5], [3, 5]]
    assert matrix_addition([[1]], [[2]]) == [[3]]
    assert matrix_addition([[1, 2, 3], [3, 2, 1], [1, 1, 1]], [[2, 2, 1], [3, 2, 3], [1, 1, 3]]) == [[3, 4, 4],
                                                                                                     [6, 4, 4],
                                                                                                     [2, 2, 4]]
