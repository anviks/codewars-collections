"""https://www.codewars.com/kata/529adbf7533b761c560004e5"""
import unittest

from solution_529adbf7533b761c560004e5 import fibonacci


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(fibonacci(70), 190392490709135)
        self.assertEqual(fibonacci(60), 1548008755920)
        self.assertEqual(fibonacci(50), 12586269025)
