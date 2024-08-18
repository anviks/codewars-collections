"""https://www.codewars.com/kata/526989a41034285187000de4"""

from solution_count_ip_addresses import *


def test_tests__sample_tests():
    assert ips_between('150.0.0.0', '150.0.0.1') == 1
    assert ips_between('10.0.0.0', '10.0.0.50') == 50
    assert ips_between('20.0.0.10', '20.0.1.0') == 246
    assert ips_between('10.11.12.13', '10.11.13.0') == 243
    assert ips_between('160.0.0.0', '160.0.1.0') == 256
