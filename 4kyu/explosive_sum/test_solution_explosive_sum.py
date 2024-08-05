"""https://www.codewars.com/kata/52ec24228a515e620b0005ef"""
import sys
import unittest

from solution_explosive_sum import exp_sum


class TestingExpSum(unittest.TestCase):
    def test_very_basic_tests(self):
        self.assertEqual(exp_sum(1), 1)
        self.assertEqual(exp_sum(2), 2)
        self.assertEqual(exp_sum(3), 3)

    def test_funcionality_tests(self):
        self.assertEqual(exp_sum(4), 5)
        self.assertEqual(exp_sum(5), 7)
        self.assertEqual(exp_sum(10), 42)

    def test_performance_tests(self):
        sys.setrecursionlimit(2_147_483_647)
        sys.set_int_max_str_digits(2_147_483_647)
        self.assertEqual(exp_sum(50), 204226)
        self.assertEqual(exp_sum(80), 15796476)
        self.assertEqual(exp_sum(100), 190569292)
        self.assertEqual(exp_sum(200), 3972999029388)
        self.assertEqual(exp_sum(300), 9253082936723602)
        self.assertEqual(exp_sum(400), 6727090051741041926)
        self.assertEqual(exp_sum(500), 2300165032574323995027)
        self.assertEqual(exp_sum(3000), 496025142797537184410324879054927095334462742231683423624)
