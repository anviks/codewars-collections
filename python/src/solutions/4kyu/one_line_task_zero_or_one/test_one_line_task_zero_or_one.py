"""https://www.codewars.com/kata/one-line-task-zero-or-one"""
import pytest

from solution_one_line_task_zero_or_one import *

sample_test_cases = [
    (1, [[1, 1, 0, 1]], [1, 1, 0, 1]),
    (3, [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]], [1, 0, 1, 0, 1]),
    (3, [[1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 1, 1, 1, 0]], [1, 1, 1, 0, 1]),
    (5, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]], [0, 0, 0, 0, 0])]


@pytest.mark.parametrize('n, s, expected', sample_test_cases)
def test_sample_tests__testing_zero_or_one(n, s, expected):
    assert zero_or_one(n, s) == expected
