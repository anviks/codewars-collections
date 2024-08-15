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
import unittest

from parameterized import parameterized

from solution_58b57f984f353b3dc9000030 import palindrome

MAX_CHARS = 55
MIN_CHEAT = 20


def checkAllChars(c, s):
    return not bool(set(c) ^ set(s))


class SolutionTests(unittest.TestCase):
    def makeAssertion(self, n, s, result):
        print("length = {}, strng = {}".format(n, s))
        print("Your palindrome is : {}".format(result))
        self.assertTrue(result == result[::-1], "Your result should be a palindrome")
        self.assertEqual(len(result), n, "The result should have the specified length")
        self.assertTrue(checkAllChars(s, result),
                        "The result should contain all the characters in 'strng' and only those ones.")

    def test_restrictions(self):
        source = inspect.getsource(palindrome)
        self.assertFalse(checkAllChars('\r\n;', source), "Your solution has to be a pure oneliner")
        self.assertTrue(len(source) <= MAX_CHARS, "Solution is too long!")
        self.assertTrue(len(source) > MIN_CHEAT,
                        "Your code length is smaller than the human being limit, so I guess you are Superman, or you are a cheater. ;-)")

    @parameterized.expand([
        (3, "ab"),
        (10, "ab"),
        (20, "abcd"),
        (1, "a"),
        (51, "abcdefghijklmnopqrstuvwxyz"),
    ])
    def test_solution(self, length, strng):
        self.makeAssertion(length, strng, palindrome(length, strng))
