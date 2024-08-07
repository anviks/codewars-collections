"""https://www.codewars.com/kata/52ea928a1ef5cfec800003ee"""

import unittest

from solution_ipv4_to_int32 import ip_to_int32


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(ip_to_int32("128.114.17.104"), 2154959208)
        self.assertEqual(ip_to_int32("0.0.0.0"), 0)
        self.assertEqual(ip_to_int32("128.32.10.1"), 2149583361)
