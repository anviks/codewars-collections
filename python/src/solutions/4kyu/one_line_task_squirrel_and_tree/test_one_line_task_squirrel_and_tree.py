"""https://www.codewars.com/kata/one-line-task-squirrel-and-tree"""

from solution_one_line_task_squirrel_and_tree import *


def test_tests__fixed_tests():
    assert squirrel(4, 16, 3) == 20
    assert squirrel(4, 4, 3) == 5
    assert squirrel(8, 9, 37) == 42.5869
    assert squirrel(526, 682, 140) == 705.7435
    assert squirrel(247, 857, 669) == 2474.3392
    assert squirrel(2, 11, 47) == 258.7339
    assert squirrel(73, 97, 244) == 338.4185
    assert squirrel(15, 774, 948) == 48922.923
    assert squirrel(21, 29, 60) == 87.7856
    assert squirrel(83, 97, 86) == 139.6799
