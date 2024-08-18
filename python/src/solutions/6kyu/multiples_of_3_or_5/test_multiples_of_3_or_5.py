"""https://www.codewars.com/kata/514b92a657cdc65150000006"""

from solution_multiples_of_3_or_5 import *


def test_sample_tests__should_return_3_for_n_4():
    assert solution(4) == 3


def test_sample_tests__should_return_8_for_n_6():
    assert solution(6) == 8


def test_sample_tests__should_return_60_for_n_16():
    assert solution(16) == 60


def test_sample_tests__should_return_0_for_n_3():
    assert solution(3) == 0


def test_sample_tests__should_return_3_for_n_5():
    assert solution(5) == 3


def test_sample_tests__should_return_45_for_n_15():
    assert solution(15) == 45


def test_sample_tests__should_return_0_for_n_0():
    assert solution(0) == 0


def test_sample_tests__should_return_0_for_n_1():
    assert solution(-1) == 0


def test_sample_tests__should_return_23_for_n_10():
    assert solution(10) == 23


def test_sample_tests__should_return_78_for_n_20():
    assert solution(20) == 78


def test_sample_tests__should_return_9168_for_n_200():
    assert solution(200) == 9168
