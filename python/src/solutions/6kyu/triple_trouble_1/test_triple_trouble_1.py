"""https://www.codewars.com/kata/55d5434f269c0c3f1b000058"""

from solution_triple_trouble_1 import *


def test_triple_trouble__sample_tests():
    assert triple_double(451999277, 41177722899) == 1
    assert triple_double(1222345, 12345) == 0
    assert triple_double(12345, 12345) == 0
    assert triple_double(666789, 12345667) == 1
    assert triple_double(10560002, 100) == 1
    assert triple_double(1112, 122) == 0
