"""https://www.codewars.com/kata/525f47c79f2f25a4db000025"""

from solution_valid_phone_number import *


def test_phone_number_validations__sample_tests():
    assert valid_phone_number('(123) 456-7890') is True
    assert valid_phone_number('(1111)555 2345') is False
    assert valid_phone_number('(098) 123 4567') is False
    assert valid_phone_number('(123)456-7890') is False
    assert valid_phone_number('abc(123)456-7890') is False
    assert valid_phone_number('(123)456-7890abc') is False
    assert valid_phone_number('abc(123)456-7890abc') is False
    assert valid_phone_number('abc(123) 456-7890') is False
    assert valid_phone_number('(123) 456-7890abc') is False
    assert valid_phone_number('abc(123) 456-7890abc') is False
    assert valid_phone_number('(333) 185-0594') is True
