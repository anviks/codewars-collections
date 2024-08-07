"""https://www.codewars.com/kata/53855e4dc25c8adbc5000316"""
import unittest

from solution_email_validation import validate


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(validate('abc@example.com'), True)
        self.assertEqual(validate('_bc@example.com'), False)
