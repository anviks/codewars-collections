"""https://www.codewars.com/kata/549ee8b47111a81214000941"""

import pytest

from solution_shortest_knight_path import *



def test_fixed_tests__basic_test_cases():
    arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
    for x in arr:
        z = knight(x[0], x[1])
        
        assert z == x[2], '{} to {}: expected {}, got {}'.format(x[0], x[1], x[2], z)
