"""
https://www.codewars.com/kata/one-line-task-palindrome-string

You can assume that the specified length n will always 
be a positive integer and greater than 2*len(c) - 2.

The function 'makeAssertion(length, strng, result)' do the following:
    1) print the parameters and your result
    2) check that your result is a palindrome with the specified length
    3) check that you use all the characters in strng and only those ones
"""
import inspect

import pytest

from solution_one_line_task_palindrome_string import palindrome

MAX_CHARS = 55
MIN_CHEAT = 20


def check_all_chars(c, s):
    return not bool(set(c) ^ set(s))


def make_assertion(n, s, result):
    print("length = {}, strng = {}".format(n, s))
    print("Your palindrome is : {}".format(result))
    assert result == result[::-1], "Your result should be a palindrome"
    assert len(result) == n, "The result should have the specified length"
    assert check_all_chars(s, result), "The result should contain all the characters in 'strng' and only those ones."


def test_restrictions():
    source = inspect.getsource(palindrome)
    assert not check_all_chars('\r\n;', source), "Your solution has to be a pure oneliner"
    assert len(source) <= MAX_CHARS, "Solution is too long!"
    assert len(
        source) > MIN_CHEAT, "Your code length is smaller than the human being limit, so I guess you are Superman, or you are a cheater. ;-)"


@pytest.mark.parametrize('length, strng', [
    (3, "ab"),
    (10, "ab"),
    (20, "abcd"),
    (1, "a"),
    (51, "abcdefghijklmnopqrstuvwxyz"),
])
def test_solution(length, strng):
    make_assertion(length, strng, palindrome(length, strng))
