"""https://www.codewars.com/kata/52b757663a95b11b3d00062d"""

from solution_weird_string_case import *


def test_to_weird_case__should_return_the_correct_value_for_a_single_word():
    assert to_weird_case('This') == 'ThIs'
    assert to_weird_case('is') == 'Is'


def test_to_weird_case__should_return_the_correct_value_for_multiple_words():
    assert to_weird_case('THIs iS a TEST') == 'ThIs Is A TeSt'
