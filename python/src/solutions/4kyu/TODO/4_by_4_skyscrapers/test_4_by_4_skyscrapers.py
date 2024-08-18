"""https://www.codewars.com/kata/4-by-4-skyscrapers"""

import pytest

from solution_4_by_4_skyscrapers import solve_puzzle


@pytest.mark.skip("Skip incomplete kata")
@pytest.mark.parametrize('clue, outcome', [
    ((2, 2, 1, 3,
      2, 2, 3, 1,
      1, 2, 2, 3,
      3, 2, 1, 3),
     ((1, 3, 4, 2),
      (4, 2, 1, 3),
      (3, 4, 2, 1),
      (2, 1, 3, 4))),
    ((0, 0, 1, 2,
      0, 2, 0, 0,
      0, 3, 0, 0,
      0, 1, 0, 0),
     ((2, 1, 4, 3),
      (3, 4, 1, 2),
      (4, 2, 3, 1),
      (1, 3, 2, 4)))
])
def test_example(clue, outcome):
    assert solve_puzzle(clue) == outcome
