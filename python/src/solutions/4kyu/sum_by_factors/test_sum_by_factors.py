"""https://www.codewars.com/kata/54d496788776e49e6b00052f"""

from solution_sum_by_factors import *


def test_fixed_tests__basic_test_cases():
    a = [12, 15]
    assert sum_for_list(a) == [[2, 12], [3, 27], [5, 15]]
    a = [15, 21, 24, 30, 45]
    assert sum_for_list(a) == [[2, 54], [3, 135], [5, 90], [7, 21]]
    a = [15, 21, 24, 30, -45]
    assert sum_for_list(a) == [[2, 54], [3, 45], [5, 0], [7, 21]]
    a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    b = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158],
         [107, 107]]
    assert sum_for_list(a) == b
    a = [-29804, -4209, -28265, -72769, -31744]
    b = [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769],
         [5653, -28265], [7451, -29804]]
    assert sum_for_list(a) == b
