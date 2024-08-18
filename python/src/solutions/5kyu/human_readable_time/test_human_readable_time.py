"""https://www.codewars.com/kata/52685f7382004e774f0001f7"""

from solution_human_readable_time import *


def test_fixed_tests__basic_test_cases():
    assert make_readable(0) == '00:00:00'
    assert make_readable(59) == '00:00:59'
    assert make_readable(60) == '00:01:00'
    assert make_readable(3599) == '00:59:59'
    assert make_readable(3600) == '01:00:00'
    assert make_readable(86399) == '23:59:59'
    assert make_readable(86400) == '24:00:00'
    assert make_readable(359999) == '99:59:59'
