"""https://www.codewars.com/kata/541a354c39c5efa5fa001372"""
import unittest

from solution_541a354c39c5efa5fa001372 import ip_to_num, num_to_ip


class SampleTests(unittest.TestCase):
    def test_ip_to_num(self):
        self.assertEqual(ip_to_num('192.168.1.1'), 3232235777)
        self.assertEqual(ip_to_num('10.0.0.0'), 167772160)
        self.assertEqual(ip_to_num('176.16.0.1'), 2953838593)
        self.assertEqual(ip_to_num('255.255.255.255'), 2 ** 32 - 1)
        self.assertEqual(ip_to_num('0.0.0.0'), 0)
        self.assertEqual(ip_to_num('0.152.13.172'), 9964972)

    def test_num_to_ip(self):
        self.assertEqual(num_to_ip(3232235777), '192.168.1.1')
        self.assertEqual(num_to_ip(167772160), '10.0.0.0')
        self.assertEqual(num_to_ip(2953838593), '176.16.0.1')
        self.assertEqual(num_to_ip(0), '0.0.0.0')
        self.assertEqual(num_to_ip(2 ** 32 - 1), '255.255.255.255')
        self.assertEqual(num_to_ip(9964972), '0.152.13.172')

    def test_combined(self):
        self.assertEqual(num_to_ip(ip_to_num('192.168.1.1')), '192.168.1.1')
        self.assertEqual(num_to_ip(ip_to_num('10.0.0.0')), '10.0.0.0')
        self.assertEqual(num_to_ip(ip_to_num('176.16.0.1')), '176.16.0.1')
        self.assertEqual(ip_to_num(num_to_ip(3232235777)), 3232235777)
        self.assertEqual(ip_to_num(num_to_ip(167772160)), 167772160)
        self.assertEqual(ip_to_num(num_to_ip(2953838593)), 2953838593)
