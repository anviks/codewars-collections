"""https://www.codewars.com/kata/526989a41034285187000de4"""

import unittest

from solution_count_ip_addresses import ips_between


class Tests(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(ips_between("150.0.0.0", "150.0.0.1"), 1)
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)
        self.assertEqual(ips_between("10.11.12.13", "10.11.13.0"), 243)
        self.assertEqual(ips_between("160.0.0.0", "160.0.1.0"), 256)
