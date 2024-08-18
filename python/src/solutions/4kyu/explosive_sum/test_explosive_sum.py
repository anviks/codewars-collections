"""https://www.codewars.com/kata/52ec24228a515e620b0005ef"""
import sys

from solution_explosive_sum import *


def test_testing_exp_sum__very_basic_tests():
    assert exp_sum(1) == 1
    assert exp_sum(2) == 2
    assert exp_sum(3) == 3


def test_testing_exp_sum__funcionality_tests():
    assert exp_sum(4) == 5
    assert exp_sum(5) == 7
    assert exp_sum(10) == 42


def test_performance_tests():
    sys.setrecursionlimit(2_147_483_647)
    sys.set_int_max_str_digits(2_147_483_647)
    assert exp_sum(50) == 204226
    assert exp_sum(80) == 15796476
    assert exp_sum(100) == 190569292
    assert exp_sum(200) == 3972999029388
    assert exp_sum(300) == 9253082936723602
    assert exp_sum(400) == 6727090051741041926
    assert exp_sum(500) == 2300165032574323995027
    assert exp_sum(3000) == 496025142797537184410324879054927095334462742231683423624
