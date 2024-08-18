"""https://www.codewars.com/kata/5842df8ccbd22792a4000245"""

from solution_write_number_in_expanded_form import *


def test_sample_tests__should_pass_sample_tests():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
