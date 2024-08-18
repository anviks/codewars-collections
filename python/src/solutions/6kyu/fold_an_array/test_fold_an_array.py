"""https://www.codewars.com/kata/57ea70aa5500adfe8a000110"""

import pytest

from solution_fold_an_array import *


@pytest.mark.parametrize('orig_array, runs, expected', [
    ([1, 2, 3, 4, 5], 1, [6, 6, 3]),
    ([1, 2, 3, 4, 5], 2, [9, 6]),
    ([1, 2, 3, 4, 5], 3, [15]),
    ([-9, 9, -8, 8, 66, 23], 1, [14, 75, 0]),
])
def test_example(orig_array, runs, expected):
    array = orig_array.copy()
    actual = fold_array(array, runs)
    assert array == orig_array, 'The input array should not be modified'
    assert actual == expected
