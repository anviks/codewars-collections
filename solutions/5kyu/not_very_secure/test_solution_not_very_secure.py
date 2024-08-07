"""https://www.codewars.com/kata/526dbd6c8c0eb53254000110"""
import unittest

from parameterized import parameterized

from solution_not_very_secure import alphanumeric


class SampleTests(unittest.TestCase):
    @parameterized.expand([
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ])
    def test_alphanumeric_s(self, s, b):
        self.assertEqual(alphanumeric(s), b)
