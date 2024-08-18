"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e"""

from solution_first_non_repeating_character import *


def test_sample_tests__should_handle_simple_cases():
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'


def test_sample_tests__should_handle_empty_strings():
    assert first_non_repeating_letter('') == ''


def test_sample_tests__should_handle_strings_without_unique_characters():
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('aa') == ''


def test_sample_tests__should_handle_exotic_characters():
    assert first_non_repeating_letter('~><#~><') == '#'
    assert first_non_repeating_letter('hello world, eh?') == 'w'


def test_sample_tests__should_handle_letter_case_correctly():
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!") == ','
