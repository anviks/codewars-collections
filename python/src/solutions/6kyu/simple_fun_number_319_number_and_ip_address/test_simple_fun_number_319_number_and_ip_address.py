"""https://www.codewars.com/kata/5936371109ca68fe6900000c"""

import unittest

from solution_simple_fun_319_number_and_ip_address import number_and_IP_address


class BasicTests(unittest.TestCase):
    def test_should_work_for_sample_tests(self):
        self.assertEqual(number_and_IP_address("10.0.3.193"), "167773121")
        self.assertEqual(number_and_IP_address("167969729"), "10.3.3.193")
