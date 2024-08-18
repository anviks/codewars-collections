"""https://www.codewars.com/kata/5936371109ca68fe6900000c"""

from solution_simple_fun_number_319_number_and_ip_address import *


def test_basic_tests__should_work_for_sample_tests():
    assert number_and_IP_address('10.0.3.193') == '167773121'
    assert number_and_IP_address('167969729') == '10.3.3.193'
