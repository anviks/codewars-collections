"""https://www.codewars.com/kata/52e88b39ffb6ac53a400022e"""
import unittest

from solution import int32_to_ip


class SolutionTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")
