"""https://www.codewars.com/kata/56a921fa8c5167d8e7000053"""
import unittest

from solution_56a921fa8c5167d8e7000053 import password


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(password("Abcd1234"), True)
        self.assertEqual(password("Abcd123"), False)
        self.assertEqual(password("abcd1234"), False)
        self.assertEqual(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"), True)
        self.assertEqual(password("ABCD1234"), False)
        self.assertEqual(password(r"Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"), True)
        self.assertEqual(password(r"!@#$%^&*()-_+={}[]|\:;?/>.<,"), False)
        self.assertEqual(password(""), False)
        self.assertEqual(password(" aA1----"), True)
        self.assertEqual(password("4aA1----"), True)
