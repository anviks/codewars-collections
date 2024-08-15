"""https://www.codewars.com/kata/simpler-interactive-interpreter"""
import unittest

from solution_simpler_interactive_interpreter import Interpreter

interpreter = Interpreter()


# Basic arithmetic
@unittest.skip("Skip incomplete kata")
class ArithmeticTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(interpreter.input("1 + 1"), 2)
        self.assertEqual(interpreter.input("2 - 1"), 1)
        self.assertEqual(interpreter.input("2 * 3"), 6)
        self.assertEqual(interpreter.input("8 / 4"), 2)
        self.assertEqual(interpreter.input("7 % 4"), 3)


# Variables
@unittest.skip("Skip incomplete kata")
class VariableTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(interpreter.input("x = 1"), 1)
        self.assertEqual(interpreter.input("x"), 1)
        self.assertEqual(interpreter.input("x + 3"), 4)
        self.assertRaises(Exception, interpreter.input, 'y')
