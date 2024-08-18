"""https://www.codewars.com/kata/52e88b39ffb6ac53a400022e"""

from solution_int32_to_ipv4 import *


def test_example():
    assert int32_to_ip(2154959208) == '128.114.17.104'
    assert int32_to_ip(0) == '0.0.0.0'
    assert int32_to_ip(2149583361) == '128.32.10.1'
