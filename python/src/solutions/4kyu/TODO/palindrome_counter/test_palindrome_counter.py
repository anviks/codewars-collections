"""https://www.codewars.com/kata/64607242d3560e0043c3de25"""
import unittest

from solution_palindrome_counter import count_palindromes


@unittest.skip("Skip incomplete kata")
class FixedTests(unittest.TestCase):
    def test_integer_tests(self):
        self.assertEqual(5, count_palindromes(1, 5), 'a = 1, b = 5')
        self.assertEqual(8, count_palindromes(2, 10), 'a = 2, b = 10')
        self.assertEqual(2, count_palindromes(35, 64), 'a = 35, b = 64')
        self.assertEqual(10, count_palindromes(5, 55), 'a = 5, b = 55')
        self.assertEqual(4, count_palindromes(0, 3), 'a = 0, b = 3')
        self.assertEqual(10, count_palindromes(150, 250), 'a = 150, b = 250')
        self.assertEqual(2, count_palindromes(10 ** 14, 10 ** 16), 'a = 10 ** 14, b = 10 ** 16')

    def test_decimal_tests(self):
        self.assertEqual(5, count_palindromes(21, 75.9), 'a = 21, b = 75.9')
        self.assertEqual(6, count_palindromes(32.1, 93.2), 'a = 32.1, b = 93.2')
        self.assertEqual(1, count_palindromes(82.9, 97.3), 'a = 82.9, b = 97.3')
        self.assertEqual(4, count_palindromes(29.7, 70.3), 'a = 29.7, b = 70.3')
        self.assertEqual(14, count_palindromes(2.9, 86.6), 'a = 2.9, b = 86.6')
        self.assertEqual(1, count_palindromes(59.2, 71.8), 'a = 59.2, b = 71.8')
        self.assertEqual(4, count_palindromes(38.4, 85.1), 'a = 38.4, b = 85.1')
        self.assertEqual(3, count_palindromes(13.2, 54.4), 'a = 13.2, b = 54.4')
        self.assertEqual(2, count_palindromes(49.8, 70), 'a = 49.8, b = 70')
        self.assertEqual(2, count_palindromes(76, 88.5), 'a = 76, b = 88.5')

    def test_zero_tests(self):
        self.assertEqual(0, count_palindromes(13, 15), 'a = 13, b = 15')
        self.assertEqual(0, count_palindromes(45, 54), 'a = 45, b = 54')
        self.assertEqual(0, count_palindromes(82, 43), 'a = 82, b = 43')
        self.assertEqual(0, count_palindromes(71.1, 75.8), 'a = 71.1, b = 75.8')
        self.assertEqual(0, count_palindromes(2.2, 2.9), 'a = 2.2, b = 2.9')

    def test_large_integer_tests(self):
        self.assertEqual(2, count_palindromes(10 ** 14, 10 ** 16), 'a = 10 ** 14, b = 10 ** 16')
