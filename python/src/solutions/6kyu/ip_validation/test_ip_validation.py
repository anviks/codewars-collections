"""https://www.codewars.com/kata/515decfd9dcfc23bb6000006"""

from solution_ip_validation import *


def test_sample_tests__tests():
    assert is_valid_IP('12.255.56.1') is True
    assert is_valid_IP('') is False
    assert is_valid_IP('abc.def.ghi.jkl') is False
    assert is_valid_IP('123.456.789.0') is False
    assert is_valid_IP('12.34.56') is False
    assert is_valid_IP('12.34.56 .1') is False
    assert is_valid_IP('12.34.56.-1') is False
    assert is_valid_IP('123.045.067.089') is False
    assert is_valid_IP('127.1.1.0') is True
    assert is_valid_IP('0.0.0.0') is True
    assert is_valid_IP('0.34.82.53') is True
    assert is_valid_IP('192.168.1.300') is False
