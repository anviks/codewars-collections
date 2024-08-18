"""https://www.codewars.com/kata/626a887e8a33feabd6ad8f25"""

from solution_combining_predicates import *


def test_examples_from_the_description__1_argument():
    @predicate
    def is_even(num):
        return num % 2 == 0

    @predicate
    def is_positive(num):
        return num > 0

    assert (is_even & is_positive)(4) is True
    assert (is_even & is_positive)(3) is False
    assert (is_even | is_positive)(3) is True
    assert (~is_even & is_positive)(3) is True


def test_examples_from_the_description__0_arguments():
    @predicate
    def to_be():
        return True

    assert (to_be | ~to_be)() is True


def test_examples_from_the_description__2_arguments_keyword_arguments():
    @predicate
    def is_equal(a, b):
        return a == b

    @predicate
    def is_less_than(a, b):
        return a < b

    assert (is_less_than | is_equal)(1, 2) is True
    assert (is_less_than | is_equal)(2, b=2) is True
    assert (is_less_than | is_equal)(a=3, b=2) is False


def test_examples_from_the_description__should_be_callable_and_behave_like_the_original():
    @predicate
    def is_less_than(a, b):
        return a < b

    assert is_less_than(1, 2) is True
    assert is_less_than(2, 2) is False
    assert is_less_than(3, 2) is False
