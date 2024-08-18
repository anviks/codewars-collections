"""https://www.codewars.com/kata/52ea928a1ef5cfec800003ee"""

from solution_ipv4_to_int32 import *


def test_basic_tests__basic_tests():
    assert ip_to_int32('128.114.17.104') == 2154959208
    assert ip_to_int32('0.0.0.0') == 0
    assert ip_to_int32('128.32.10.1') == 2149583361
